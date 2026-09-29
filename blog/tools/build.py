#!/usr/bin/env python3
"""Build the agentiloop.ai blog from Markdown, in every site language.

English posts live in blog/src/YYYY-MM-DD-slug.md with a small front-matter block:

    ---
    title: Post title
    description: One-sentence summary (used for meta tags, the index and RSS)
    tags: Security, Internals
    ---

Translations use the same filename under blog/src/<lang>/ (es fr de zh ru ko ja). A post with
no translation falls back to the English text (with a note), like the rest of the site.
Blog UI strings (dates, buttons, headings) live in blog/tools/i18n.json. Nav and footer labels
come from the site's own i18n/<lang>.json, so the chrome matches the main page.

Posts dated after today are skipped, so you can queue posts ahead and publish one a day
by re-running this script (e.g. from a daily job) and committing the output.

Writes:  blog/...  and  <lang>/blog/...   (<slug>/index.html, index.html, feed.xml)
Updates: the <!-- blog:start --> ... <!-- blog:end --> block in sitemap.xml

Usage:   python3 blog/tools/build.py [YYYY-MM-DD]   (optional date publishes as of that day)
"""
import datetime
import html
import importlib.util
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
BLOG = ROOT / 'blog'
SRC = BLOG / 'src'
SITE = 'https://agentiloop.ai'
AUTHOR = 'Todd Bruss'

# Reuse the site's language list, hreflang codes and language picker so the blog matches the main page.
_spec = importlib.util.spec_from_file_location('site_i18n', ROOT / 'i18n' / 'i18n.py')
site_i18n = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(site_i18n)
LANGS = site_i18n.LANGS          # code: (native name, og:locale, Intl locale); 'en' first
HREFLANG = site_i18n.HREFLANG
UI = json.loads((BLOG / 'tools' / 'i18n.json').read_text(encoding='utf-8'))
SITE_TR = {l: json.loads((ROOT / 'i18n' / ('%s.json' % l)).read_text(encoding='utf-8')) for l in LANGS if l != 'en'}


def prefix(lang):
    """URL prefix for a language: '' for English, '/ja' for Japanese."""
    return '' if lang == 'en' else '/' + lang


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
    text = re.sub(r'(?<![A-Za-z0-9_*])\*(?!\s)(.+?)(?<!\s)\*(?![A-Za-z0-9_*])', r'<em>\1</em>', text)
    return re.sub('\x00(\\d+)\x00', lambda m: codes[int(m.group(1))], text)


def link(label, url):
    external = url.startswith('http') and not url.startswith(SITE)
    extra = ' target="_blank" rel="noopener"' if external else ''
    return '<a href="%s"%s>%s</a>' % (html.escape(url), extra, label)


def slugify(text):
    s = re.sub(r'[^\w]+', '-', text.lower()).strip('-')
    return s or 'section'


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
        if line.startswith('<figure'):  # raw HTML chart block, passed through as-is
            block = []
            while i < len(lines):
                block.append(lines[i])
                i += 1
                if '</figure>' in block[-1]:
                    break
            out.append('\n'.join(block))
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
        while i < len(lines) and lines[i].strip() and not re.match(r'(```|#{2,4} |> |\||- |\d+\. |---$|<figure)', lines[i]):
            para.append(lines[i].strip())
            i += 1
        out.append('<p>%s</p>' % inline(' '.join(para)))
    return '\n'.join(out)


# ------------------------------------------------------------------ Posts ---

def parse(path):
    text = path.read_text(encoding='utf-8')
    fm = re.match(r'---\n(.*?)\n---\n', text, re.S)
    if not fm:
        sys.exit('Missing front matter: %s' % path)
    meta = dict(l.split(':', 1) for l in fm.group(1).splitlines() if ':' in l)
    meta = {k.strip(): v.strip() for k, v in meta.items()}
    return meta, text[fm.end():]


def load_posts(today):
    """English posts, newest first, each with a per-language dict of title/description/tags/html."""
    posts = []
    for path in sorted(SRC.glob('*.md')):
        m = re.match(r'(\d{4}-\d{2}-\d{2})-(.+)\.md$', path.name)
        if not m:
            sys.exit('Bad post filename (want YYYY-MM-DD-slug.md): %s' % path.name)
        date = datetime.date.fromisoformat(m.group(1))
        if date > today:
            print('queued (not yet published): %s' % path.name)
            continue
        meta, body = parse(path)
        post = {'slug': m.group(2), 'date': date,
                'minutes': max(1, round(len(re.findall(r'\w+', re.sub(r'<[^>]+>', ' ', body))) / 230)), 'lang': {}}
        for lang in LANGS:
            src = path if lang == 'en' else SRC / lang / path.name
            translated = lang == 'en' or src.exists()
            lm, lb = parse(src) if translated else (meta, body)
            post['lang'][lang] = {
                'title': lm['title'], 'description': lm['description'],
                'tags': [t.strip() for t in lm.get('tags', '').split(',') if t.strip()],
                'html': localize_links(markdown(lb), lang), 'translated': translated,
            }
            if lang != 'en' and not translated:
                print('untranslated: %s/%s' % (lang, path.name))
        posts.append(post)
    posts.sort(key=lambda p: (p['date'], p['slug']), reverse=True)
    return posts


def localize_links(body, lang):
    """Point in-site blog links at the same language."""
    return body if lang == 'en' else body.replace('href="/blog/', 'href="%s/blog/' % prefix(lang))


def nice_date(d, lang):
    u = UI[lang]
    return u['date'].format(d=d.day, mn=d.month, y=d.year, month=u['months'][d.month - 1])


# -------------------------------------------------------------- Templates ---

HEAD = '''<!DOCTYPE html>
<html lang="{lang}">
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
{alternates}
    <link rel="canonical" href="{url}">
    <link rel="alternate" type="application/rss+xml" title="{feed_title}" href="{site}{prefix}/blog/feed.xml">

    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="{og_type}">
    <meta property="og:url" content="{url}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:locale" content="{locale}">
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
    <link rel="stylesheet" href="/promo.css">
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
            {picker}
            <button type="button" class="nav-toggle" id="nav-toggle" aria-label="Open menu" aria-controls="nav-links" aria-expanded="false">
                <span class="nav-toggle-bar"></span>
                <span class="nav-toggle-bar"></span>
                <span class="nav-toggle-bar"></span>
            </button>
        </div>
    </header>
{promo}'''

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
                <a href="mailto:agent@agentiloop.ai">Email</a>
                <a href="/press/">Press</a>
                <a href="/legal.html">Legal</a>
            </div>
            <p class="footer-tagline">© 2026 AgentiLoop.ai, a <a href="https://inkpen.io" target="_blank" rel="noopener">Logos InkPen LLC</a> company. All rights reserved. · Agentic AI for your entire Mac and More!</p>
        </div>
    </footer>

    <script src="/nav.js"></script>
    <script src="/promo.js"></script>
</body>
</html>
'''

# Site pages that have translated copies under /<lang>/ (setup.html and auto.html don't).
TRANSLATED_PATHS = ('/', '/stats.html', '/press/', '/legal.html', '/blog/')


def localize_chrome(page, lang):
    """Translate nav/footer labels from the site's i18n/<lang>.json and point links at /<lang>/."""
    if lang == 'en':
        return page
    tr = SITE_TR[lang]

    def label(m):
        return m.group(1) + tr.get(m.group(2), m.group(2)) + '</a>'

    def labels(m):  # only the nav and footer link lists, never post content
        return re.sub(r'(<a href="[^"]*"[^>]*>)([^<]+)</a>', label, m.group(0))
    page = re.sub(r'<nav class="nav-links".*?</nav>|<div class="footer-links">.*?</div>', labels, page, flags=re.S)
    page = page.replace('aria-label="Open menu"', 'aria-label="%s"' % html.escape(tr.get('Open menu', 'Open menu')), 1)
    tagline = re.search(r'<p class="footer-tagline">(.*?)</p>', page, re.S)
    if tagline and tagline.group(1) in tr:
        page = page.replace(tagline.group(0), '<p class="footer-tagline">%s</p>' % tr[tagline.group(1)])

    def href(m):
        url = m.group(1)
        if url.startswith('/#') or url in TRANSLATED_PATHS:
            url = prefix(lang) + url
        return 'href="%s"' % url
    return re.sub(r'href="(/(?:#[^"]*|stats\.html|press/|legal\.html|blog/)?)"', href, page)


def promo(lang):
    """The rotating promo banner, copied from the matching home page (index.html or <lang>/index.html)."""
    home = ROOT / ('index.html' if lang == 'en' else '%s/index.html' % lang)
    m = re.search(r'    <!-- PROMO BANNER.*?</aside>\n', home.read_text(encoding='utf-8'), re.S)
    return m.group(0) if m else ''


def alternates(page):
    """hreflang block for a blog path like 'blog/' or 'blog/<slug>/'."""
    return site_i18n.alternates(page)


def head(lang, page, title, description, og_type='website', jsonld=''):
    url = SITE + prefix(lang) + '/' + page
    return HEAD.format(lang=lang, title=html.escape(title), description=html.escape(description), url=url,
                       site=SITE, prefix=prefix(lang), og_type=og_type, jsonld=jsonld,
                       locale=LANGS[lang][1], feed_title=html.escape(UI[lang]['post_suffix']),
                       alternates=alternates(page), picker=site_i18n.picker(lang, page), promo=promo(lang))


def tags_html(tags):
    return ''.join('<span class="post-tag">%s</span>' % html.escape(t) for t in tags)


def cta(lang):
    u = UI[lang]
    return '''
            <aside class="post-cta">
                <h2>{h}</h2>
                <p>{p}</p>
                <pre><code>brew update &amp;&amp; brew install --cask agentiloop-agent</code></pre>
                <div class="post-cta-buttons">
                    <a class="btn btn-primary" href="https://github.com/AgentiLoop/Agent/releases/latest" target="_blank" rel="noopener">{dl}</a>
                    <a class="btn btn-ghost" href="https://github.com/AgentiLoop/Agent" target="_blank" rel="noopener">{src}</a>
                </div>
            </aside>'''.format(h=html.escape(u['cta_h']), p=html.escape(u['cta_p']),
                               dl=html.escape(u['cta_dl']), src=html.escape(u['cta_src']))


def back_home(lang):
    """Bottom-of-page button back to the home page. nav.js points it at the exact page and scroll
    position the reader left when they opened the blog."""
    label = '← Back to Home' if lang == 'en' else SITE_TR[lang].get('← Back to Home', '← Back to Home')
    return '''
            <div class="center-cta blog-home">
                <a href="%s/" class="btn btn-ghost" data-back-home>%s</a>
            </div>''' % (prefix(lang), html.escape(label))


def render_post(p, newer, older, lang):
    u, t = UI[lang], p['lang'][lang]
    page = 'blog/%s/' % p['slug']
    url = SITE + prefix(lang) + '/' + page
    ld = ('    <script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting",'
          '"headline":%s,"description":%s,"datePublished":"%s","inLanguage":"%s","author":{"@type":"Person","name":"%s"},'
          '"publisher":{"@type":"Organization","name":"AgentiLoop.ai"},"mainEntityOfPage":"%s",'
          '"image":"%s/agent-og.png"}</script>\n') % (
        json.dumps(t['title'], ensure_ascii=False), json.dumps(t['description'], ensure_ascii=False),
        p['date'].isoformat(), HREFLANG.get(lang, lang), AUTHOR, url, SITE)
    base = prefix(lang) + '/blog/'
    nav = '<nav class="post-nav">'
    nav += ('<a class="post-nav-older" href="%s%s/"><span>%s</span>%s</a>' % (base, older['slug'], u['older'], html.escape(older['lang'][lang]['title']))) if older else '<span></span>'
    nav += ('<a class="post-nav-newer" href="%s%s/"><span>%s</span>%s</a>' % (base, newer['slug'], u['newer'], html.escape(newer['lang'][lang]['title']))) if newer else '<span></span>'
    nav += '</nav>'
    note = '' if t['translated'] else '<p class="post-fallback">%s</p>' % html.escape(u['fallback'])
    body_lang = '' if t['translated'] else ' lang="en"'
    body = '''
    <main class="section blog">
        <div class="container">
            <article class="post">
                <p class="post-back"><a href="{base}">{all}</a></p>
                <header class="post-header">
                    <div class="post-tags">{tags}</div>
                    <h1>{title}</h1>
                    <p class="post-dek">{desc}</p>
                    <p class="post-meta">{by} · <time datetime="{iso}">{date}</time> · {mins}</p>
                </header>
                {note}<div class="post-body"{body_lang}>
{body}
                </div>
{cta}
            </article>
            {nav}{home}
        </div>
    </main>
'''.format(base=base, all=u['all_posts'], tags=tags_html(t['tags']), title=html.escape(t['title']),
           desc=html.escape(t['description']), by=u['by'].format(author=AUTHOR), iso=p['date'].isoformat(),
           date=nice_date(p['date'], lang), mins=u['min_read'].format(n=p['minutes']), note=note,
           body_lang=body_lang, body=t['html'], cta=cta(lang), nav=nav, home=back_home(lang))
    title = '%s – %s' % (t['title'], u['post_suffix'])
    return localize_chrome(head(lang, page, title, t['description'], 'article', ld) + body + FOOT, lang)


def render_index(posts, lang):
    u = UI[lang]
    base = prefix(lang) + '/blog/'
    cards = []
    for n, p in enumerate(posts):
        t = p['lang'][lang]
        cards.append('''
                <a class="post-card{feat}" href="{base}{slug}/">
                    <div class="post-tags">{tags}</div>
                    <h2>{title}</h2>
                    <p>{desc}</p>
                    <p class="post-meta"><time datetime="{iso}">{date}</time> · {mins}</p>
                </a>'''.format(feat=' post-card-featured' if n == 0 else '', base=base, slug=p['slug'],
                               tags=tags_html(t['tags']), title=html.escape(t['title']),
                               desc=html.escape(t['description']), iso=p['date'].isoformat(),
                               date=nice_date(p['date'], lang), mins=u['min_read'].format(n=p['minutes'])))
    body = '''
    <main class="section blog">
        <div class="container">
            <div class="section-head">
                <h2>{h}</h2>
                <p>{intro}</p>
                <p class="blog-rss"><a href="{base}feed.xml">{rss}</a></p>
            </div>
            <div class="post-list">{cards}
            </div>{home}
        </div>
    </main>
'''.format(h=u['index_h'], intro=html.escape(u['index_intro']), base=base, rss=u['rss'], cards=''.join(cards), home=back_home(lang))
    return localize_chrome(head(lang, 'blog/', u['index_title'], u['index_desc']) + body + FOOT, lang)


def render_feed(posts, lang):
    u = UI[lang]
    link_base = SITE + prefix(lang) + '/blog/'
    items = ''.join('''
    <item>
      <title>{t}</title>
      <link>{b}{slug}/</link>
      <guid>{b}{slug}/</guid>
      <pubDate>{d}</pubDate>
      <description>{desc}</description>
    </item>'''.format(t=html.escape(p['lang'][lang]['title']), b=link_base, slug=p['slug'],
                      desc=html.escape(p['lang'][lang]['description']),
                      d=p['date'].strftime('%a, %d %b %Y 12:00:00 +0000')) for p in posts)
    return '''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>{title}</title>
    <link>{b}</link>
    <description>{desc}</description>
    <language>{lang}</language>{items}
  </channel>
</rss>
'''.format(title=html.escape(u['post_suffix']), b=link_base, desc=html.escape(u['feed_desc']),
           lang=HREFLANG.get(lang, lang), items=items)


def update_sitemap(posts):
    path = ROOT / 'sitemap.xml'
    xml = path.read_text(encoding='utf-8')
    latest = posts[0]['date'].isoformat() if posts else datetime.date.today().isoformat()
    pages = [('blog/', latest, '0.7')] + [('blog/%s/' % p['slug'], p['date'].isoformat(), '0.6') for p in posts]
    entries = []
    for page, lastmod, prio in pages:
        for lang in LANGS:
            entries.append('  <url>\n    <loc>%s%s/%s</loc>\n    <lastmod>%s</lastmod>\n    <priority>%s</priority>\n  </url>'
                           % (SITE, prefix(lang), page, lastmod, prio if lang == 'en' else '0.5'))
    block = '  <!-- blog:start (generated by blog/tools/build.py) -->\n' + '\n'.join(entries) + '\n  <!-- blog:end -->\n'
    if '<!-- blog:start' in xml:
        xml = re.sub(r'  <!-- blog:start.*?<!-- blog:end -->\n', lambda m: block, xml, flags=re.S)
    else:
        xml = xml.replace('</urlset>', block + '</urlset>')
    path.write_text(xml, encoding='utf-8')


def main():
    # Optional: `build.py YYYY-MM-DD` publishes as of that date (e.g. to release tomorrow's post early).
    today = datetime.date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else datetime.date.today()
    posts = load_posts(today)
    for lang in LANGS:
        out_dir = BLOG if lang == 'en' else ROOT / lang / 'blog'
        out_dir.mkdir(parents=True, exist_ok=True)
        for n, p in enumerate(posts):
            newer = posts[n - 1] if n > 0 else None
            older = posts[n + 1] if n + 1 < len(posts) else None
            out = out_dir / p['slug'] / 'index.html'
            out.parent.mkdir(exist_ok=True)
            out.write_text(render_post(p, newer, older, lang), encoding='utf-8')
        (out_dir / 'index.html').write_text(render_index(posts, lang), encoding='utf-8')
        (out_dir / 'feed.xml').write_text(render_feed(posts, lang), encoding='utf-8')
        print('built  %s/blog/ (%d posts + index + feed.xml)' % (prefix(lang), len(posts)))
    update_sitemap(posts)
    print('updated sitemap.xml')


if __name__ == '__main__':
    main()
