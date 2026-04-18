const GITHUB_API = 'https://api.github.com/repos/macOS26/Agent/releases';

function extractVersion(filename) {
    if (!filename) return '';
    const match = filename.match(/(\d+\.\d+\.\d+)/);
    return match ? match[1] : '';
}

function formatFileSize(bytes) {
    if (bytes === 0) return '0 <span class="size-unit">Bytes</span>';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' <span class="size-unit">' + sizes[i] + '</span>';
}

function formatDate(date) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return date.toLocaleDateString('en-US', options);
}

function formatDateShort(date) {
    const m = date.getMonth() + 1;
    const d = date.getDate();
    const y = String(date.getFullYear()).slice(-2);
    return m + '.' + d + '.' + y;
}

async function autoDiscoverReleases() {
    try {
        const response = await fetch(GITHUB_API);
        if (!response.ok) return;

        const releases = await response.json();
        if (!releases.length) return;

        // Find the latest release with a DMG asset
        let latestDmg = null;
        for (const release of releases) {
            for (const asset of release.assets) {
                if (asset.name.endsWith('.dmg')) {
                    if (!latestDmg) {
                        latestDmg = {
                            url: asset.browser_download_url,
                            version: extractVersion(asset.name),
                            tag: release.tag_name
                        };
                    }
                    break;
                }
            }
        }

        // Update the download button and setup link
        if (latestDmg) {
            const downloadBtn = document.getElementById('download-btn');
            if (downloadBtn) {
                downloadBtn.href = latestDmg.url;
                downloadBtn.textContent = 'Download v' + latestDmg.version;
            }
            const setupLink = document.getElementById('setup-download-link');
            if (setupLink) {
                setupLink.href = latestDmg.url;
            }
        }

        // Build the release history table
        const tbody = document.getElementById('release-history-body');
        if (!tbody) return;

        let rows = '';
        for (const release of releases) {
            for (const asset of release.assets) {
                if (!asset.name.endsWith('.dmg')) continue;
                const version = extractVersion(asset.name);
                const dateObj = new Date(release.published_at || release.created_at);
                const date = formatDate(dateObj);
                const dateShort = formatDateShort(dateObj);
                const size = formatFileSize(asset.size);
                const url = asset.browser_download_url;

                rows += '<tr>'
                    + '<td><a href="' + url + '" class="version-badge">' + version + '</a></td>'
                    + '<td><span class="date-full">' + date + '</span><span class="date-short">' + dateShort + '</span></td>'
                    + '<td class="col-size">' + size + '</td>'
                    + '<td class="col-sha">' + asset.download_count.toLocaleString() + '</td>'
                    + '</tr>';
            }
        }

        tbody.innerHTML = rows || '<tr><td colspan="4" style="text-align: center; color: #999;">No releases found.</td></tr>';
    } catch (e) {
        // Silently fail — the page still works with fallback links
    }
}

autoDiscoverReleases();

// Randomize wave rotation each cycle
document.querySelectorAll('.wave').forEach(function(el) {
    function randomize() {
        el.style.setProperty('--wave-rot', Math.floor(Math.random() * 360) + 'deg');
    }
    randomize();
    el.addEventListener('animationiteration', randomize);
});

// Contact form — opens mailto with pre-filled fields
(function() {
    var form = document.getElementById('contact-form');
    if (!form) return;

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        var name = form.name.value.trim();
        var email = form.email.value.trim();
        var message = form.message.value.trim();

        if (!name || !email || !message) return;

        var subject = encodeURIComponent('Agent! Contact: ' + name);
        var body = encodeURIComponent('From: ' + name + ' (' + email + ')\n\n' + message);
        window.location.href = 'mailto:agent@macos26.app?subject=' + subject + '&body=' + body;
    });
})();