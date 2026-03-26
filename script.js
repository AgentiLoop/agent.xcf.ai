// Synthesized whoosh sound for dot animation
function playWhoosh() {
    var ctx = new (window.AudioContext || window.webkitAudioContext)();
    var now = ctx.currentTime;
    var dur = 1.8;

    // White noise swoosh
    var bufLen = ctx.sampleRate * dur;
    var buf = ctx.createBuffer(1, bufLen, ctx.sampleRate);
    var data = buf.getChannelData(0);
    for (var i = 0; i < bufLen; i++) data[i] = (Math.random() * 2 - 1);

    var noise = ctx.createBufferSource();
    noise.buffer = buf;

    // Bandpass filter sweeps down like something spiraling in
    var filter = ctx.createBiquadFilter();
    filter.type = 'bandpass';
    filter.Q.value = 5;
    filter.frequency.setValueAtTime(3000, now);
    filter.frequency.exponentialRampToValueAtTime(200, now + dur);

    // Volume envelope: fade in, sustain, fade out
    var gain = ctx.createGain();
    gain.gain.setValueAtTime(0, now);
    gain.gain.linearRampToValueAtTime(0.1215, now + 0.1);
    gain.gain.setValueAtTime(0.1215, now + dur * 0.6);
    gain.gain.exponentialRampToValueAtTime(0.001, now + dur);

    // Subtle tone that drops in pitch
    var osc = ctx.createOscillator();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(800, now);
    osc.frequency.exponentialRampToValueAtTime(100, now + dur);
    var oscGain = ctx.createGain();
    oscGain.gain.setValueAtTime(0.0486, now);
    oscGain.gain.linearRampToValueAtTime(0.0486, now + dur * 0.5);
    oscGain.gain.exponentialRampToValueAtTime(0.001, now + dur);

    noise.connect(filter);
    filter.connect(gain);
    gain.connect(ctx.destination);

    osc.connect(oscGain);
    oscGain.connect(ctx.destination);

    noise.start(now);
    noise.stop(now + dur);
    osc.start(now);
    osc.stop(now + dur);
}

// "Dah dah dahhh!" reveal chime after the whoosh
function playReveal() {
    var ctx = new (window.AudioContext || window.webkitAudioContext)();
    var start = ctx.currentTime;
    var vol = 0.1;

    function playNote(freq, time, length) {
        var osc = ctx.createOscillator();
        osc.type = 'sine';
        osc.frequency.value = freq;

        var g = ctx.createGain();
        g.gain.setValueAtTime(0, start + time);
        g.gain.linearRampToValueAtTime(vol, start + time + 0.03);
        g.gain.setValueAtTime(vol, start + time + length * 0.6);
        g.gain.exponentialRampToValueAtTime(0.001, start + time + length);

        // Soft harmonic layer
        var osc2 = ctx.createOscillator();
        osc2.type = 'triangle';
        osc2.frequency.value = freq * 2;
        var g2 = ctx.createGain();
        g2.gain.setValueAtTime(0, start + time);
        g2.gain.linearRampToValueAtTime(vol * 0.3, start + time + 0.03);
        g2.gain.exponentialRampToValueAtTime(0.001, start + time + length);

        osc.connect(g);
        g.connect(ctx.destination);
        osc2.connect(g2);
        g2.connect(ctx.destination);

        osc.start(start + time);
        osc.stop(start + time + length);
        osc2.start(start + time);
        osc2.stop(start + time + length);
    }

    // Dah (C5) - Dah (E5) - Dahhh! (G5, held longer)
    playNote(523.25, 0, 0.25);   // C5
    playNote(659.25, 0.28, 0.25); // E5
    playNote(783.99, 0.56, 0.6);  // G5 held
}

function replayAnimation() {
    // Restart CSS animations
    var wrap = document.querySelector('.icon-anim-wrap');
    var clone = wrap.cloneNode(true);
    wrap.parentNode.replaceChild(clone, wrap);
    // Restart all text animations
    ['.main-title', '.subtitle', '.description', '.cta-section'].forEach(function(sel) {
        var el = document.querySelector(sel);
        if (el) { el.style.animation = 'none'; el.offsetHeight; el.style.animation = ''; }
    });
    // Play sound in sync
    playWhoosh();
    setTimeout(playReveal, 2100);
}

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