// Old-school footer hit counter. Page views (all languages) come from Cloudflare Web Analytics
// via the blog-cron-trigger Worker's /hits.json (cached 60s).
(function () {
    var m = /^(?:\/(?:es|fr|de|zh|ru|ko|ja))?\/(|index\.html|blog\/?|blog\/index\.html|press\/?|press\/index\.html|legal(?:\.html)?|stats(?:\.html)?|setup(?:\.html)?)$/.exec(location.pathname);
    var box = document.querySelector('.footer .container');
    if (!m || !box) return;
    var key = m[1].split(/[/.]/)[0];
    if (key === '' || key === 'index') key = 'home';
    var label = {
        en: 'You are visitor #', es: 'Eres el visitante n.º', fr: 'Vous êtes le visiteur n°', de: 'Sie sind Besucher Nr.',
        zh: '您是第', ru: 'Вы посетитель №', ko: '당신은 방문자 #', ja: 'あなたは'
    };
    var after = { zh: '位访客', ja: '人目の訪問者です' };
    var lang = (document.documentElement.lang || 'en').slice(0, 2);
    fetch('https://blog-cron-trigger.todd-de8.workers.dev/hits.json').then(function (r) { return r.json(); }).then(function (v) {
        var n = v[key];
        if (!n) return;
        var p = document.createElement('p');
        p.className = 'hit-counter';
        var odo = document.createElement('span');
        odo.className = 'hit-counter-digits';
        odo.setAttribute('aria-label', String(n));
        String(n).padStart(7, '0').split('').forEach(function (d) {
            var s = document.createElement('span');
            s.textContent = d;
            odo.appendChild(s);
        });
        p.appendChild(document.createTextNode((label[lang] || label.en) + ' '));
        p.appendChild(odo);
        if (after[lang]) p.appendChild(document.createTextNode(' ' + after[lang]));
        box.appendChild(p);
    }).catch(function () {});
})();
