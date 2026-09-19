// Shared site nav — mobile burger / X menu (paired with nav.css)
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
