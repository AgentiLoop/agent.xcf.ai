#!/usr/bin/env python3
"""Build the agentiloop.ai blog from Markdown.

Source posts live in blog/src/YYYY-MM-DD-slug.md with a small front-matter block:

    ---
    title: Post title
    description: One-sentence summary (used for meta tags, the index and RSS)
    tags: Security, Internals
    ---

Posts dated after today are skipped, so you can queue posts ahead and publish one a day
by re-running this script (e.g. from a daily job) and committing the output.

Writes:  blog/<slug>/index.html   blog/index.html   blog/feed.xml
Updates: the <!-- blog:start --> ... <!-- blog:end --> block in sitemap.xml

Usage:   python3 blog/tools/build.py
"""
import datetime
import html
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
BLOG = ROOT / 'blog'
SRC = BLOG / 'src'
SITE = 'https://agentiloop.ai'
AUTHOR = 'Todd Bruss'


# ---------------------------------------------------------------- Markdown ---

def inline(text):
    """Inline Markdown: code, links, bold, italic. Code spans are protected first."""
    codes = []

    def keep_code(m):
        codes.append('<code>' + html.escape(m.group(1)) + '</code>')
        return '\x00%d\x00' % (len(codes) - 1)

    text = re.sub(r'`([^`]+)`', keep_code, text)
    text = html.escape(text, quote=False)
    text = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', lambda m: link(m.group(1), m.group(2)), text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', text)
    return re.sub('\x00(\\d+)\x00', lambda m: codes[int(m.group(1))], text)


def link(label, url):
    external = url.startswith('http') and not url.startswith(SITE)
    extra = ' target="_blank" rel="noopener"' if external else ''
    return '<a href="%s"%s>%s</a>' % (html.escape(url), extra, label)


def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')


def markdown(md):
    lines = md.split('\n')
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        if line.startswith('```'):
            lang = line[3:].strip()
            i += 1
            code = []
            while i < len(lines) and not lines[i].startswith('```'):
                code.append(lines[i])
                i += 1
            i += 1
            cls = ' class="language-%s"' % lang if lang else ''
            out.append('<pre><code%s>%s</code></pre>' % (cls, html.escape('\n'.join(code))))
            continue
        m = re.match(r'(#{2,4}) (.+)', line)
        if m:
            n = len(m.group(1))
            out.append('<h%d id="%s">%s</h%d>' % (n, slugify(m.group(2)), inline(m.group(2)), n))
            i += 1
            continue
        if line.strip() == '---':
            out.append('<hr>')
            i += 1
            continue
        if line.startswith('> '):
            quote = []
            while i < len(lines) and lines[i].startswith('>'):
                quote.append(lines[i][1:].strip())
                i += 1
            out.append('<blockquote><p>%s</p></blockquote>' % inline(' '.join(quote)))
            continue
        if line.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')])
                i += 1
            head, body = rows[0], [r for r in rows[1:] if not all(re.fullmatch(r':?-+:?', c) for c in r)]
            t = '<div class="table-wrap"><table><thead><tr>' + ''.join('<th>%s</th>' % inline(c) for c in head)
            t += '</tr></thead><tbody>'
            t += ''.join('<tr>' + ''.join('<td>%s</td>' % inline(c) for c in r) + '</tr>' for r in body)
            out.append(t + '</tbody></table></div>')
            continue
        if re.match(r'(- |\d+\. )', line):
            tag = 'ol' if line[0].isdigit() else 'ul'
            items = []
            while i < len(lines) and re.match(r'(- |\d+\. )', lines[i]):
                items.append(re.sub(r'^(- |\d+\. )', '', lines[i]))
                i += 1
                while i < len(lines) and lines[i].startswith('  ') and lines[i].strip():
                    items[-1] += ' ' + lines[i].strip()
                    i += 1
            out.append('<%s>%s</%s>' % (tag, ''.join('<li>%s</li>' % inline(t) for t in items), tag))
            continue
        if not line.strip():
            i += 1
            continue
        para = []
        while i < len(lines) and lines[i].strip() and not re.match(r'(```|#{2,4} |> |\||- |\d+\. |---$)', lines[i]):
            para.append(lines[i].strip())
            i += 1
        out.append('<p>%s</p>' % inline(' '.join(para)))
    return '\n'.join(out)


# ------------------------------------------------------------------ Posts ---

def load_posts(today):
    posts = []
    for path in sorted(SRC.glob('*.md')):
        m = re.match(r'(\d{4}-\d{2}-\d{2})-(.+)\.md$', path.name)
        if not m:
            sys.exit('Bad post filename (want YYYY-MM-DD-slug.md): %s' % path.name)
        date = datetime.date.fromisoformat(m.group(1))
        if date > today:
            print('queued (not yet published): %s' % path.name)
            continue
        text = path.read_text(encoding='utf-8')
        fm = re.match(r'---\n(.*?)\n---\n', text, re.S)
        if not fm:
            sys.exit('Missing front matter: %s' % path.name)
        meta = dict(l.split(':', 1) for l in fm.group(1).splitlines() if ':' in l)
        meta = {k.strip(): v.strip() for k, v in meta.items()}
        body = text[fm.end():]
        words = len(re.findall(r'\w+', body))
        posts.append({
            'slug': m.group(2), 'date': date, 'title': meta['title'],
            'description': meta['description'],
            'tags': [t.strip() for t in meta.get('tags', '').split(',') if t.strip()],
            'html': markdown(body), 'minutes': max(1, round(words / 230)),
        })
    posts.sort(key=lambda p: (p['date'], p['slug']), reverse=True)
    return posts


def nice_date(d):
    return d.strftime('%B ') + str(d.day) + d.strftime(', %Y')


# -------------------------------------------------------------- Templates ---

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-14FE9YDJ2D"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', 'G-14FE9YDJ2D');
    </script>

    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="{url}">
    <link rel="alternate" type="application/rss+xml" title="AgentiLoop Agent! Blog" href="{site}/blog/feed.xml">

    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="{og_type}">
    <meta property="og:url" content="{url}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:image" content="{site}/agent-og.png">
    <meta name="theme-color" content="#3b82f6">

    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:site" content="@SuperBox64">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{description}">
    <meta name="twitter:image" content="{site}/agent-og.png">

    <!-- Favicon -->
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    <link rel="manifest" href="/site.webmanifest">

    <!-- Stylesheet -->
    <link rel="stylesheet" href="/styles.css">
    <link rel="stylesheet" href="/nav.css">
    <link rel="stylesheet" href="/footer.css">
    <link rel="stylesheet" href="/blog/blog.css">
{jsonld}</head>
<body>

    <!-- NAV (shared — keep identical on every page; styles in nav.css, burger in nav.js) -->
    <header class="nav">
        <div class="nav-inner">
            <a href="/" class="nav-brand">
                <img src="/agent_icon.png" alt="AgentiLoop Agent! icon">
                <span>AgentiLoop</span>
            </a>
            <nav class="nav-links" id="nav-links">
                <a href="/#features">Features</a>
                <a href="/#sponsors">Sponsors</a>
                <a href="/#showcase">Showcase</a>
                <a href="/#reviews">Reviews</a>
                <a href="/#providers">Providers</a>
                <a href="/setup.html">Setup</a>
                <a href="/#releases">Releases</a>
                <a href="/blog/">Blog</a>
                <a href="https://github.com/AgentiLoop/Agent" target="_blank" rel="noopener">GitHub</a>
            </nav>
            <button type="button" class="nav-toggle" id="nav-toggle" aria-label="Open menu" aria-controls="nav-links" aria-expanded="false">
                <span class="nav-toggle-bar"></span>
                <span class="nav-toggle-bar"></span>
                <span class="nav-toggle-bar"></span>
            </button>
        </div>
    </header>
'''

FOOT = '''
    <!-- FOOTER (shared — keep identical on every page; styles in footer.css) -->
    <footer class="footer">
        <div class="container">
            <div class="footer-links">
                <a href="/">Home</a>
                <a href="/setup.html">Setup</a>
                <a href="/#reviews">Reviews</a>
                <a href="/#sponsors">Sponsors</a>
                <a href="/#midnight">Bored</a>
                <a href="/stats.html">Stats</a>
                <a href="/blog/">Blog</a>
                <a href="https://github.com/AgentiLoop/Agent" target="_blank" rel="noopener">GitHub</a>
                <a href="https://github.com/AgentiLoop/Agent/releases" target="_blank" rel="noopener">Releases</a>
                <a href="https://x.com/AgentiLoopAgent/" target="_blank" rel="noopener">X</a>
                <a href="https://www.paypal.com/ncp/payment/9C6RY2UAE5M3S" target="_blank" rel="noopener">Donate</a>
                <a href="mailto:agent@agentiloop.ai">Email</a>
                <a href="/press/">Press</a>
                <a href="/legal.html">Legal</a>
            </div>
            <p class="footer-tagline">© 2026 AgentiLoop.ai, a <a href="https://inkpen.io" target="_blank" rel="noopener">Logos InkPen LLC</a> company. All rights reserved. · Agentic AI for your entire Mac and More!</p>
        </div>
    </footer>

    <script src="/nav.js"></script>
</body>
</html>
'''

CTA = '''
            <aside class="post-cta">
                <h2>Try Agent! on your Mac</h2>
                <p>Free for personal use. macOS 14.6 or later, Apple Silicon or Intel. Bring any of 23 LLM providers, or run local.</p>
                <pre><code>brew update &amp;&amp; brew install --cask agentiloop-agent</code></pre>
                <div class="post-cta-buttons">
                    <a class="btn btn-primary" href="https://github.com/AgentiLoop/Agent/releases/latest" target="_blank" rel="noopener">Download the latest release</a>
                    <a class="btn btn-ghost" href="https://github.com/AgentiLoop/Agent" target="_blank" rel="noopener">Read the source</a>
                </div>
            </aside>'''


def tags_html(tags):
    return ''.join('<span class="post-tag">%s</span>' % html.escape(t) for t in tags)


def head(title, description, url, og_type='website', jsonld=''):
    return HEAD.format(title=html.escape(title), description=html.escape(description), url=url,
                       site=SITE, og_type=og_type, jsonld=jsonld)


def render_post(p, newer, older):
    url = '%s/blog/%s/' % (SITE, p['slug'])
    ld = ('    <script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting",'
          '"headline":%s,"description":%s,"datePublished":"%s","author":{"@type":"Person","name":"%s"},'
          '"publisher":{"@type":"Organization","name":"AgentiLoop.ai"},"mainEntityOfPage":"%s",'
          '"image":"%s/agent-og.png"}</script>\n') % (
        json_str(p['title']), json_str(p['description']), p['date'].isoformat(), AUTHOR, url, SITE)
    nav = '<nav class="post-nav">'
    nav += ('<a class="post-nav-older" href="/blog/%s/"><span>← Older</span>%s</a>' % (older['slug'], html.escape(older['title']))) if older else '<span></span>'
    nav += ('<a class="post-nav-newer" href="/blog/%s/"><span>Newer →</span>%s</a>' % (newer['slug'], html.escape(newer['title']))) if newer else '<span></span>'
    nav += '</nav>'
    body = '''
    <main class="section blog">
        <div class="container">
            <article class="post">
                <p class="post-back"><a href="/blog/">← All posts</a></p>
                <header class="post-header">
                    <div class="post-tags">{tags}</div>
                    <h1>{title}</h1>
                    <p class="post-dek">{desc}</p>
                    <p class="post-meta">By {author} · <time datetime="{iso}">{date}</time> · {mins} min read</p>
                </header>
                <div class="post-body">
{body}
                </div>
{cta}
            </article>
            {nav}
        </div>
    </main>
'''.format(tags=tags_html(p['tags']), title=html.escape(p['title']), desc=html.escape(p['description']),
           author=AUTHOR, iso=p['date'].isoformat(), date=nice_date(p['date']), mins=p['minutes'],
           body=p['html'], cta=CTA, nav=nav)
    return head(p['title'] + ' – AgentiLoop Agent! Blog', p['description'], url, 'article', ld) + body + FOOT


def render_index(posts):
    cards = []
    for n, p in enumerate(posts):
        cards.append('''
                <a class="post-card{feat}" href="/blog/{slug}/">
                    <div class="post-tags">{tags}</div>
                    <h2>{title}</h2>
                    <p>{desc}</p>
                    <p class="post-meta"><time datetime="{iso}">{date}</time> · {mins} min read</p>
                </a>'''.format(feat=' post-card-featured' if n == 0 else '', slug=p['slug'],
                               tags=tags_html(p['tags']), title=html.escape(p['title']),
                               desc=html.escape(p['description']), iso=p['date'].isoformat(),
                               date=nice_date(p['date']), mins=p['minutes']))
    body = '''
    <main class="section blog">
        <div class="container">
            <div class="section-head">
                <h2>The Agent! <span class="grad">Blog</span></h2>
                <p>Straight from the codebase: how AgentiLoop Agent! works, what changed, and why. New posts daily.</p>
                <p class="blog-rss"><a href="/blog/feed.xml">RSS feed</a></p>
            </div>
            <div class="post-list">{cards}
            </div>
        </div>
    </main>
'''.format(cards=''.join(cards))
    desc = 'The AgentiLoop Agent! blog: deep dives into the native macOS AI agent, its codebase, releases and the ideas behind it.'
    return head('Blog – AgentiLoop Agent!', desc, SITE + '/blog/') + body + FOOT


def json_str(s):
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'


def render_feed(posts):
    items = ''.join('''
    <item>
      <title>{t}</title>
      <link>{site}/blog/{slug}/</link>
      <guid>{site}/blog/{slug}/</guid>
      <pubDate>{d}</pubDate>
      <description>{desc}</description>
    </item>'''.format(t=html.escape(p['title']), site=SITE, slug=p['slug'], desc=html.escape(p['description']),
                      d=p['date'].strftime('%a, %d %b %Y 12:00:00 +0000')) for p in posts)
    return '''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>AgentiLoop Agent! Blog</title>
    <link>{site}/blog/</link>
    <description>Deep dives into AgentiLoop Agent!, the native macOS AI agent.</description>
    <language>en</language>{items}
  </channel>
</rss>
'''.format(site=SITE, items=items)


def update_sitemap(posts):
    path = ROOT / 'sitemap.xml'
    xml = path.read_text(encoding='utf-8')
    entries = ['  <url>\n    <loc>%s/blog/</loc>\n    <lastmod>%s</lastmod>\n    <priority>0.7</priority>\n  </url>'
               % (SITE, posts[0]['date'].isoformat() if posts else datetime.date.today().isoformat())]
    entries += ['  <url>\n    <loc>%s/blog/%s/</loc>\n    <lastmod>%s</lastmod>\n    <priority>0.6</priority>\n  </url>'
                % (SITE, p['slug'], p['date'].isoformat()) for p in posts]
    block = '  <!-- blog:start (generated by blog/tools/build.py) -->\n' + '\n'.join(entries) + '\n  <!-- blog:end -->\n'
    if '<!-- blog:start' in xml:
        xml = re.sub(r'  <!-- blog:start.*?<!-- blog:end -->\n', lambda m: block, xml, flags=re.S)
    else:
        xml = xml.replace('</urlset>', block + '</urlset>')
    path.write_text(xml, encoding='utf-8')


def main():
    today = datetime.date.today()
    posts = load_posts(today)
    for n, p in enumerate(posts):
        newer = posts[n - 1] if n > 0 else None
        older = posts[n + 1] if n + 1 < len(posts) else None
        out = BLOG / p['slug'] / 'index.html'
        out.parent.mkdir(exist_ok=True)
        out.write_text(render_post(p, newer, older), encoding='utf-8')
        print('built  /blog/%s/' % p['slug'])
    (BLOG / 'index.html').write_text(render_index(posts), encoding='utf-8')
    (BLOG / 'feed.xml').write_text(render_feed(posts), encoding='utf-8')
    update_sitemap(posts)
    print('built  /blog/ (%d posts), feed.xml, sitemap.xml' % len(posts))


if __name__ == '__main__':
    main()
