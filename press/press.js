// Live GitHub counts for the press page.
//
// The HTML ships with dated numbers so the page is complete without JavaScript
// or when the unauthenticated GitHub API (60 requests per hour per address) is
// rate limited. When the API answers, the numbers and their labels are replaced
// with live values; on any failure the dated numbers stay as they are.
(function () {
    var REPO_API = 'https://api.github.com/repos/AgentiLoop/Agent';
    var RELEASES_API = REPO_API + '/releases?per_page=100';

    function setCount(id, value, label) {
        var card = document.getElementById(id);
        if (!card) return;
        var number = card.querySelector('strong');
        var text = card.querySelector('span');
        if (number) number.textContent = value.toLocaleString('en-US');
        if (text) text.textContent = label;
    }

    function fetchJSON(url) {
        return fetch(url, { headers: { Accept: 'application/vnd.github+json' } }).then(function (response) {
            if (!response.ok) throw new Error('GitHub API ' + response.status + ' for ' + url);
            return response.json();
        });
    }

    function updateCounts() {
        Promise.all([fetchJSON(REPO_API), fetchJSON(RELEASES_API)]).then(function (results) {
            var repo = results[0];
            var releases = results[1].filter(function (release) { return !release.draft && !release.prerelease; });
            setCount('proof-stars', repo.stargazers_count, 'GitHub stars');
            setCount('proof-forks', repo.forks_count, 'Forks on GitHub');
            setCount('proof-releases', releases.length, 'Public releases since April 12, 2026');
        }).catch(function (error) {
            console.warn('Live GitHub counts unavailable; showing the dated figures.', error);
        });
    }

    updateCounts();
    setInterval(updateCounts, 20 * 60 * 1000);
})();
