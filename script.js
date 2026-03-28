const GITHUB_API = 'https://api.github.com/repos/macOS26/Agent/releases';

function extractVersion(filename) {
    if (!filename) return '';
    const match = filename.match(/(\d+\.\d+\.\d+)/);
    return match ? match[1] : '';
}

function formatFileSize(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
}

function formatDate(date) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return date.toLocaleDateString('en-US', options);
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
                const date = formatDate(new Date(release.published_at || release.created_at));
                const size = formatFileSize(asset.size);
                const url = asset.browser_download_url;

                rows += '<tr>'
                    + '<td><a href="' + url + '" class="version-badge">' + version + '</a></td>'
                    + '<td>' + date + '</td>'
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

// Contact form
(function() {
    var form = document.getElementById('contact-form');
    if (!form) return;

    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        var btn = document.getElementById('contact-submit');
        var status = document.getElementById('contact-status');
        status.textContent = '';
        status.className = 'contact-status';
        btn.disabled = true;
        btn.textContent = 'Sending...';

        try {
            var res = await fetch('/api/contact', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    name: form.name.value.trim(),
                    email: form.email.value.trim(),
                    message: form.message.value.trim()
                })
            });

            if (res.ok) {
                status.textContent = 'Message sent. Thank you!';
                status.className = 'contact-status success';
                form.reset();
            } else {
                var data = await res.json().catch(function() { return {}; });
                status.textContent = data.error || 'Failed to send. Please try again.';
                status.className = 'contact-status error';
            }
        } catch (err) {
            status.textContent = 'Network error. Please try again.';
            status.className = 'contact-status error';
        }

        btn.disabled = false;
        btn.textContent = 'Send Message';
    });
})();