// Old-school hit counter, shown just above the footer. Page views (all languages) come from Cloudflare Web Analytics
// via the blog-cron-trigger Worker's /hits.json (cached 60s).
// The row is inserted synchronously with placeholder digits so its space is reserved before the fetch returns (no layout shift).
(function () {
    var m = /^(?:\/(?:es|fr|de|zh|ru|ko|ja))?\/(|index\.html|blog\/?|blog\/index\.html|press\/?|press\/index\.html|legal(?:\.html)?|stats(?:\.html)?|setup(?:\.html)?)$/.exec(location.pathname);
    var footer = document.querySelector('.footer');
    if (!m || !footer) return;
    var key = m[1].split(/[/.]/)[0];
    if (key === '' || key === 'index') key = 'home';

    var p = document.createElement('p');
    p.className = 'hit-counter';
    var odo = document.createElement('span');
    odo.className = 'hit-counter-digits';
    var cells = [];
    for (var i = 0; i < 7; i++) {
        var s = document.createElement('span');
        s.textContent = '0';
        odo.appendChild(s);
        cells.push(s);
    }
    p.appendChild(odo);
    footer.parentNode.insertBefore(p, footer);

    fetch('https://blog-cron-trigger.todd-de8.workers.dev/hits.json').then(function (r) { return r.json(); }).then(function (v) {
        var n = v[key];
        if (!n) { p.remove(); return; }
        var digits = String(n).padStart(7, '0').split('');
        while (cells.length < digits.length) {
            var s = document.createElement('span');
            odo.insertBefore(s, odo.firstChild);
            cells.unshift(s);
        }
        digits.forEach(function (d, i) { cells[i].textContent = d; });
        odo.setAttribute('aria-label', String(n));
        p.classList.add('loaded');
    }).catch(function () { p.remove(); });
})();
