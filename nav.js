// Shared site nav — mobile burger / X menu (paired with nav.css)
(function() {
    // Language picker: close on outside click or Esc
    var picker = document.querySelector('.lang-picker');
    if (picker) {
        document.addEventListener('click', function(e) {
            if (!picker.contains(e.target)) picker.open = false;
        });
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') picker.open = false;
        });
    }
})();
(function() {
    var toggle = document.getElementById('nav-toggle');
    var links = document.getElementById('nav-links');
    if (!toggle || !links) return;

    function setOpen(open) {
        links.classList.toggle('is-open', open);
        toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
        toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    }

    toggle.addEventListener('click', function() {
        setOpen(!links.classList.contains('is-open'));
    });
    links.addEventListener('click', function(e) {
        if (e.target.tagName === 'A') setOpen(false);
    });
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') setOpen(false);
    });
})();
// Blog "Back to Home": remember the page + scroll position the reader left for the blog,
// and return them to exactly that spot (sessionStorage, same tab only).
(function() {
    var KEY = 'agentiloopBlogReturn', RESTORE = 'agentiloopBlogRestore';
    var isBlog = /^(\/[a-z]{2})?\/blog\//.test(location.pathname);
    var langOf = function(path) { var m = path.match(/^\/([a-z]{2})\//); return m ? m[1] : 'en'; };
    var saved = null;
    try { saved = JSON.parse(sessionStorage.getItem(KEY) || 'null'); } catch (e) {}

    if (!isBlog) {
        document.addEventListener('click', function(e) {
            var a = e.target.closest && e.target.closest('a[href]');
            if (!a || a.origin !== location.origin || !/^(\/[a-z]{2})?\/blog\//.test(a.pathname)) return;
            // Remember the section on screen plus the offset into it, not just a pixel value:
            // content above can load later (images, fetched releases) and shift pixel positions.
            var anchor = null, offset = 0;
            document.querySelectorAll('section[id], [id].section').forEach(function(s) {
                var r = s.getBoundingClientRect();
                if (r.top <= 1 && r.bottom > 0) { anchor = s.id; offset = Math.round(-r.top); }
            });
            sessionStorage.setItem(KEY, JSON.stringify({ path: location.pathname, y: Math.round(window.scrollY), anchor: anchor, offset: offset }));
        });
        if (saved && sessionStorage.getItem(RESTORE) === '1' && saved.path === location.pathname) {
            sessionStorage.removeItem(RESTORE);
            if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
            var target = function() {
                var el = saved.anchor && document.getElementById(saved.anchor);
                return el ? el.getBoundingClientRect().top + window.scrollY + saved.offset : saved.y;
            };
            var done = false;
            var go = function() { if (!done) window.scrollTo({ top: target(), behavior: 'instant' }); };
            // Keep re-pinning while the page settles, until the reader scrolls on their own.
            var stop = function() { done = true; };
            ['wheel', 'touchstart', 'keydown', 'mousedown'].forEach(function(t) { window.addEventListener(t, stop, { once: true, passive: true }); });
            if (window.ResizeObserver) new ResizeObserver(go).observe(document.body);
            go();
            window.addEventListener('load', go);
            setTimeout(stop, 4000);
        }
        return;
    }

    document.querySelectorAll('a[data-back-home]').forEach(function(a) {
        // Only return to the saved page if it's in the same language as this blog page.
        if (saved && langOf(saved.path) === langOf(location.pathname)) a.setAttribute('href', saved.path);
        a.addEventListener('click', function() { sessionStorage.setItem(RESTORE, '1'); });
    });
})();
