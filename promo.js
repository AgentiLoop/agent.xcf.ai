// Promo banner Mac CTA: newest release overall (pre-release included) with a DMG.
(function () {
    var promoMac = document.getElementById('promo-mac-dl');
    if (!promoMac || !window.fetch) return;
    fetch('https://api.github.com/repos/AgentiLoop/Agent/releases?per_page=20')
        .then(function (r) { return r.ok ? r.json() : []; })
        .then(function (list) {
            for (var i = 0; i < list.length; i++) {
                if (list[i].draft) continue;
                var dmg = list[i].assets.find(function (a) { return a.name.endsWith('.dmg'); });
                if (dmg) { promoMac.href = dmg.browser_download_url; promoMac.removeAttribute('target'); return; }
            }
        })
        .catch(function () {});
})();

// Promo banner under the nav: rotate the slides, pause on hover/focus, dots jump to a slide.
(function () {
    var promo = document.getElementById('promo');
    if (!promo) return;
    var slides = promo.querySelectorAll('.promo-slide');
    var dots = promo.querySelectorAll('.promo-dot');
    var ms = 7000, cur = 0, timer = null, left = ms, started = 0;
    function syncHeight() { document.documentElement.style.setProperty('--promo-h', promo.offsetHeight + 'px'); }
    syncHeight();
    if (window.ResizeObserver) new ResizeObserver(syncHeight).observe(promo); else window.addEventListener('resize', syncHeight);
    function show(i) {
        cur = (i + slides.length) % slides.length;
        slides.forEach(function (s, n) {
            var on = n === cur;
            s.classList.toggle('is-active', on);
            s.setAttribute('aria-hidden', on ? 'false' : 'true');
            s.querySelectorAll('a').forEach(function (a) { a.tabIndex = on ? 0 : -1; });
        });
        dots.forEach(function (d, n) {
            d.classList.remove('is-active');
            void d.offsetWidth; // restart the progress animation
            d.classList.toggle('is-active', n === cur);
            d.classList.toggle('is-done', n < cur);
            d.setAttribute('aria-selected', n === cur ? 'true' : 'false');
            d.title = d.getAttribute('aria-label') || '';
        });
        left = ms;
        schedule();
    }
    function schedule() {
        clearTimeout(timer);
        if (promo.classList.contains('is-paused')) return;
        started = Date.now();
        timer = setTimeout(function () { show(cur + 1); }, left);
    }
    function pause() {
        if (promo.classList.contains('is-paused')) return;
        promo.classList.add('is-paused');
        clearTimeout(timer);
        left = Math.max(0, left - (Date.now() - started));
    }
    function resume() {
        if (promo.contains(document.activeElement) && promo.matches(':focus-within')) return;
        promo.classList.remove('is-paused');
        schedule();
    }
    dots.forEach(function (d) {
        d.addEventListener('click', function () { show(+d.dataset.go); });
    });
    promo.addEventListener('mouseenter', pause);
    promo.addEventListener('mouseleave', resume);
    promo.addEventListener('focusin', pause);
    promo.addEventListener('focusout', function () { setTimeout(resume, 0); });
    show(0);
})();
