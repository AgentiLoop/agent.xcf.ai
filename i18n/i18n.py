#!/usr/bin/env python3
"""Static translations of the homepage (index.html -> /<lang>/index.html).

    python3 i18n/i18n.py extract   # writes i18n/strings.json (English segments to translate)
    python3 i18n/i18n.py build     # writes /<lang>/index.html from i18n/<lang>.json

index.html stays the single source of truth. Every translated page is regenerated
from it, so edit English first, run `extract`, translate the new/changed strings
in i18n/<lang>.json, then run `build`. Missing translations fall back to English.
"""
import html
import json
import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, 'i18n')
SRC = os.path.join(ROOT, 'index.html')
SITE = 'https://agentiloop.ai'

LANGS = {  # code: (native name, og:locale, Intl locale)
    'en': ('English', 'en_US', 'en-US'),
    'es': ('Español', 'es_ES', 'es'),
    'fr': ('Français', 'fr_FR', 'fr'),
    'de': ('Deutsch', 'de_DE', 'de'),
    'zh': ('中文 (简体)', 'zh_CN', 'zh-CN'),
    'ru': ('Русский', 'ru_RU', 'ru'),
    'ko': ('한국어', 'ko_KR', 'ko'),
    'ja': ('日本語', 'ja_JP', 'ja'),
}
HREFLANG = {'zh': 'zh-Hans'}

VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source', 'track', 'wbr'}
INLINE = {'a', 'abbr', 'b', 'br', 'code', 'em', 'i', 'img', 'kbd', 'mark', 'small', 'span', 'strong', 'sub', 'sup', 'u', 'wbr', 'time'}
TEXTBLOCK = {'p', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'td', 'th', 'figcaption', 'dt', 'dd', 'label',
             'summary', 'button', 'blockquote', 'title', 'option', 'a', 'span', 'strong', 'em', 'b', 'small'}
SKIP = {'script', 'style', 'svg', 'pre', 'code', 'textarea'}
ATTRS = ('alt', 'title', 'aria-label', 'placeholder')
META = {'description', 'og:title', 'og:description', 'og:image:alt',
        'twitter:title', 'twitter:description', 'twitter:image:alt'}


class Node:
    def __init__(self, tag, attrs, start, inner_start):
        self.tag, self.attrs = tag, dict(attrs)
        self.start, self.inner_start = start, inner_start
        self.inner_end = self.end = inner_start
        self.children = []  # Node or (text, start, end)


class Tree(HTMLParser):
    def __init__(self, src):
        super().__init__(convert_charrefs=False)
        self.src = src
        self.lines = [0]
        for m in re.finditer('\n', src):
            self.lines.append(m.end())
        self.root = Node('#root', [], 0, 0)
        self.stack = [self.root]
        self.feed(src)
        self.close()

    def off(self):
        line, col = self.getpos()
        return self.lines[line - 1] + col

    def handle_starttag(self, tag, attrs):
        start = self.off()
        n = Node(tag, attrs, start, start + len(self.get_starttag_text()))
        self.stack[-1].children.append(n)
        if tag in VOID:
            n.end = n.inner_end = n.inner_start
        else:
            self.stack.append(n)

    def handle_startendtag(self, tag, attrs):
        start = self.off()
        n = Node(tag, attrs, start, start + len(self.get_starttag_text()))
        self.stack[-1].children.append(n)

    def handle_endtag(self, tag):
        pos = self.off()
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                for n in self.stack[i:]:
                    n.inner_end = pos
                    n.end = self.src.index('>', pos) + 1
                del self.stack[i:]
                return

    def _text(self, data):
        start = self.off()
        self.stack[-1].children.append((data, start, start + len(data)))

    handle_data = _text

    def handle_entityref(self, name):
        self._text('&%s;' % name)

    def handle_charref(self, name):
        self._text('&#%s;' % name)


def has_letters(s):
    return re.search(r'[^\W\d_]', html.unescape(re.sub(r'<[^>]+>', '', s))) is not None


def inline_only(n):
    for c in n.children:
        if isinstance(c, Node):
            if c.tag not in INLINE or not inline_only(c):
                return False
    return True


def direct_text(n):
    return any(not isinstance(c, Node) and c[0].strip() for c in n.children)


def norm(s):
    return re.sub(r'\s+', ' ', s).strip()


def collect(src):
    """Return list of (start, end, kind, key, extra). kind: 'inner' | 'attr'."""
    tree = Tree(src)
    out = []

    def attrs_of(n):
        if n.tag == 'meta':
            name = n.attrs.get('name') or n.attrs.get('property')
            if name in META and n.attrs.get('content'):
                out.append((n.start, n.inner_start, 'attr', html.unescape(n.attrs['content']), 'content'))
            return
        for a in ATTRS:
            v = n.attrs.get(a)
            if v and has_letters(v):
                out.append((n.start, n.inner_start, 'attr', v, a))

    def walk(n):
        for c in n.children:
            if not isinstance(c, Node):
                text, s, e = c
                if text.strip() and has_letters(text) and n.tag not in SKIP:
                    out.append((s, e, 'inner', norm(text), None))
                continue
            if c.tag in SKIP or c.attrs.get('translate') == 'no':
                continue
            if c.tag not in VOID and inline_only(c) and (direct_text(c) or c.tag in TEXTBLOCK) \
                    and has_letters(src[c.inner_start:c.inner_end]):
                inner = src[c.inner_start:c.inner_end]
                if c.tag in TEXTBLOCK - INLINE or direct_text(c):
                    attrs_of(c)
                    out.append((c.inner_start, c.inner_end, 'inner', norm(inner), None))
                    continue
            attrs_of(c)
            walk(c)

    walk(tree.root)
    return out


def extract():
    src = open(SRC, encoding='utf-8').read()
    keys = []
    for _, _, kind, key, _ in collect(src):
        if key not in keys:
            keys.append(key)
    for k in script_strings():
        if k not in keys:
            keys.append(k)
    with open(os.path.join(HERE, 'strings.json'), 'w', encoding='utf-8') as f:
        json.dump(keys, f, ensure_ascii=False, indent=1)
    print(len(keys), 'strings ->', os.path.relpath(os.path.join(HERE, 'strings.json'), ROOT))


# Strings that script.js writes at runtime; {v}, {p}, {n} are placeholders.
def script_strings():
    return ['Download Pre-Release {v}', 'Pre-Release', '{v} Downloads', 'Download v{v}',
            'No releases found.', 'Opening GitHub — submit the pre-filled issue to send your message.',
            'Page {p} of {n}']


def relink(tag, lang):
    """Rewrite root-relative asset/page links inside one start tag for /<lang>/."""
    def fix(m):
        attr, q, url = m.group(1), m.group(2), m.group(3)
        if re.match(r'^(https?:|//|mailto:|data:|javascript:|#)', url):
            return m.group(0)
        if url == '/':
            url = '/%s/' % lang
        elif url.startswith('/#'):
            url = '/%s/%s' % (lang, url[1:])
        elif url.startswith('/'):
            pass
        else:
            if url == 'sponsors/fluxion-ai-silver-ad.svg':
                url = 'sponsors/fluxion-ai-silver-ad_%s.svg' % lang
            url = '/' + url
        return '%s=%s%s%s' % (attr, q, url, q)
    return re.sub(r'\b(src|href)=(["\'])(.*?)\2', fix, tag)


def set_attr(tag, attr, value):
    esc = html.escape(value, quote=True)
    return re.sub(r'(\s%s=)(["\']).*?\2' % re.escape(attr), lambda m: '%s"%s"' % (m.group(1), esc), tag, count=1)


def alternates():
    lines = ['    <!-- i18n:alternates (generated by i18n/i18n.py) -->']
    for code in LANGS:
        url = SITE + ('/' if code == 'en' else '/%s/' % code)
        lines.append('    <link rel="alternate" hreflang="%s" href="%s">' % (HREFLANG.get(code, code), url))
    lines.append('    <link rel="alternate" hreflang="x-default" href="%s/">' % SITE)
    lines.append('    <!-- /i18n:alternates -->')
    return '\n'.join(lines)


def picker(current):
    items = []
    for code, (name, _, _) in LANGS.items():
        url = '/' if code == 'en' else '/%s/' % code
        cur = ' aria-current="true"' if code == current else ''
        items.append('<a href="%s" hreflang="%s" lang="%s"%s>%s</a>' % (url, HREFLANG.get(code, code), code, cur, name))
    return ('<!-- i18n:picker --><details class="lang-picker" translate="no"><summary aria-label="Language">'
            '<svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9.5" fill="none" stroke="currentColor" stroke-width="1.8"/>'
            '<path d="M2.5 12h19M12 2.5c2.8 3 2.8 16 0 19M12 2.5c-2.8 3-2.8 16 0 19" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>'
            '<span>%s</span></summary><div class="lang-menu">%s</div></details><!-- /i18n:picker -->'
            % (current.upper(), ''.join(items)))


def inject_shared(src, lang):
    """Hreflang block + language picker (idempotent; used for English too)."""
    src = re.sub(r'\s*<!-- i18n:alternates.*?<!-- /i18n:alternates -->', '', src, flags=re.S)
    src = src.replace('    <link rel="canonical"', alternates() + '\n    <link rel="canonical"', 1)
    src = re.sub(r'<!-- i18n:picker -->.*?<!-- /i18n:picker -->', '', src, flags=re.S)
    src = src.replace('<button type="button" class="nav-toggle"', picker(lang) + '\n            <button type="button" class="nav-toggle"', 1)
    return src


def build():
    src = open(SRC, encoding='utf-8').read()
    src = inject_shared(src, 'en')
    with open(SRC, 'w', encoding='utf-8') as f:
        f.write(src)

    segs = collect(src)
    for lang, (_, locale, intl) in LANGS.items():
        if lang == 'en':
            continue
        path = os.path.join(HERE, '%s.json' % lang)
        tr = json.load(open(path, encoding='utf-8')) if os.path.exists(path) else {}
        missing = 0
        edits = []  # (start, end, replacement)
        tags = {}   # start -> (end, tagtext) for attribute edits
        for s, e, kind, key, attr in segs:
            t = tr.get(key)
            if not t:
                missing += 1
                continue
            if kind == 'inner':
                edits.append((s, e, t))
            else:
                end, tag = tags.get(s, (e, src[s:e]))
                tags[s] = (end, set_attr(tag, attr, t))
        for s, (e, tag) in tags.items():
            edits.append((s, e, tag))

        edits.sort(key=lambda x: x[0], reverse=True)
        out, last = src, None
        for s, e, rep in edits:
            if last is not None and e > last:
                continue  # overlapping edit (shouldn't happen)
            out = out[:s] + rep + out[e:]
            last = s
        # Point relative links at the site root (relink is idempotent)
        out = re.sub(r'<[a-zA-Z][^>]*\b(?:src|href)=["\'][^"\']*["\'][^>]*>', lambda m: relink(m.group(0), lang), out)

        out = out.replace('<html lang="en">', '<html lang="%s">' % lang, 1)
        out = out.replace('<link rel="canonical" href="%s/">' % SITE, '<link rel="canonical" href="%s/%s/">' % (SITE, lang), 1)
        out = out.replace('content="%s/"' % SITE, 'content="%s/%s/"' % (SITE, lang), 1)  # og:url
        out = out.replace('<meta property="og:locale" content="en_US">', '<meta property="og:locale" content="%s">' % locale, 1)
        out = out.replace("'<script src=\"version.js", "'<script src=\"/version.js", 1)
        desc = tr.get(next((k for _, _, kind, k, a in segs if a == 'content'), ''), '')
        if desc:
            out = re.sub(r'("description": )"[^"]*"', lambda m: m.group(1) + json.dumps(desc, ensure_ascii=False), out, count=1)
            out = out.replace('"url": "%s/",\n      "image"' % SITE, '"url": "%s/%s/",\n      "inLanguage": "%s",\n      "image"' % (SITE, lang, lang), 1)
        out = inject_shared(out, lang)
        runtime = {k: tr.get(k, k) for k in script_strings()}
        runtime['locale'] = intl
        out = out.replace('<script src="/script.js"></script>',
                          '<script>window.I18N = %s;</script>\n    <script src="/script.js"></script>'
                          % json.dumps(runtime, ensure_ascii=False), 1)

        os.makedirs(os.path.join(ROOT, lang), exist_ok=True)
        with open(os.path.join(ROOT, lang, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(out)
        print('%s/index.html  (%d untranslated)' % (lang, missing))


def shape(s):
    """Markup that a translation must keep: tag names, href/src values, placeholders."""
    return (sorted(re.findall(r'</?([a-zA-Z0-9]+)', s)),
            sorted(re.findall(r'(?:href|src)="([^"]*)"', s)),
            sorted(re.findall(r'\{[a-z]\}', s)))


def check(lang):
    keys = json.load(open(os.path.join(HERE, 'strings.json'), encoding='utf-8'))
    tr = json.load(open(os.path.join(HERE, '%s.json' % lang), encoding='utf-8'))
    bad = 0
    for i, k in enumerate(keys):
        t = tr.get(k)
        if not t:
            print('MISSING [%d] %s' % (i, k[:80]))
            bad += 1
        elif shape(k) != shape(t):
            print('MARKUP  [%d] %s\n     ->  %s' % (i, k[:120], t[:120]))
            bad += 1
    print('%s: %d/%d ok' % (lang, len(keys) - bad, len(keys)))


def merge(lang):
    """Combine i18n/work/<lang>_*.json ({"index": translation}) into i18n/<lang>.json."""
    keys = json.load(open(os.path.join(HERE, 'strings.json'), encoding='utf-8'))
    path = os.path.join(HERE, '%s.json' % lang)
    tr = json.load(open(path, encoding='utf-8')) if os.path.exists(path) else {}
    work = os.path.join(HERE, 'work')
    for name in sorted(os.listdir(work)):
        if name.startswith(lang + '_') and name.endswith('.json'):
            for i, t in json.load(open(os.path.join(work, name), encoding='utf-8')).items():
                tr[keys[int(i)]] = t
    with open(path, 'w', encoding='utf-8') as f:
        json.dump({k: tr[k] for k in keys if k in tr}, f, ensure_ascii=False, indent=1)
    check(lang)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'build'
    if cmd in ('merge', 'check'):
        {'merge': merge, 'check': check}[cmd](sys.argv[2])
    else:
        {'extract': extract, 'build': build}[cmd]()
