const GITHUB_API = 'https://api.github.com/repos/AgentiLoop/Agent/releases';

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
            const navBtn = document.getElementById('nav-download');
            if (navBtn) {
                navBtn.href = latestDmg.url;
                navBtn.textContent = 'Download v' + latestDmg.version;
            }
        }

        // Build the release history table
        const tbody = document.getElementById('release-history-body');
        if (!tbody) return;

        let rows = '';
        let dmgCount = 0;
        for (const release of releases) {
            if (dmgCount >= 7) break;
            // Combine DMG + ZIP download counts into one entry per release
            let dmgAsset = null;
            let combinedDownloads = 0;
            for (const asset of release.assets) {
                if (asset.name.endsWith('.dmg') || asset.name.endsWith('.zip')) {
                    combinedDownloads += asset.download_count;
                    if (!dmgAsset && asset.name.endsWith('.dmg')) dmgAsset = asset;
                }
            }
            if (!dmgAsset) continue;
            dmgCount++;
            const version = extractVersion(dmgAsset.name);
            const dateObj = new Date(release.published_at || release.created_at);
            const date = formatDate(dateObj);
            const dateShort = formatDateShort(dateObj);
            const size = formatFileSize(dmgAsset.size);
            const url = dmgAsset.browser_download_url;

            rows += '<tr>'
                + '<td><a href="' + url + '" class="version-badge">' + version + '</a></td>'
                + '<td><span class="date-full">' + date + '</span><span class="date-short">' + dateShort + '</span></td>'
                + '<td class="col-size">' + size + '</td>'
                + '<td class="col-sha">' + combinedDownloads.toLocaleString() + '</td>'
                + '</tr>';
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

// Contact form — opens a pre-filled GitHub issue
(function() {
    var form = document.getElementById('contact-form');
    if (!form) return;

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        var name = form.name.value.trim();
        var email = form.email.value.trim();
        var message = form.message.value.trim();

        if (!name || !email || !message) return;

        var title = encodeURIComponent('Contact: ' + name);
        var body = encodeURIComponent('From: ' + name + ' (' + email + ')\n\n' + message);
        window.open('https://github.com/AgentiLoop/Agent/issues/new?title=' + title + '&body=' + body, '_blank');

        var status = document.getElementById('contact-status');
        if (status) status.textContent = 'Opening GitHub — submit the pre-filled issue to send your message.';
    });
})();