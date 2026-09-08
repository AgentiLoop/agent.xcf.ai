#!/usr/bin/env python3
"""Build the AgentiLoop Agent! press kit from the files in press/kit.

Run from anywhere:  python3 press/tools/build-kit.py

What it does, in order:
  1. Losslessly optimizes every screenshot in press/kit/screenshots (opaque
     RGBA files are stored as RGB so they shrink without changing a pixel).
  2. Writes WebP previews for the web page into press/img/screenshots.
  3. Renders the 1920x1080 "screenshots" promo banner into press/kit/promo.
  4. Regenerates the screenshot and banner figures inside press/index.html
     between the marker comments, and fixes the screenshot count in the hero.
  5. Stamps press.css and press.js with a content hash in index.html so a
     stale stylesheet can never be served from a browser cache.
  6. Fixes the screenshot count in press/kit/README.txt (the plain-text fact
     sheet) and rebuilds press/agentiloop-agent-press-kit.zip.

Cloudflare Workers static assets refuse files over 25 MiB, so the ZIP size is
checked at the end and the script fails loudly if it is too large.

Requires Pillow (python3 -m pip install pillow).
"""

from __future__ import annotations

import hashlib
import html
import re
import sys
import zipfile
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

PRESS_DIR = Path(__file__).resolve().parent.parent
KIT_DIR = PRESS_DIR / "kit"
SCREENSHOT_DIR = KIT_DIR / "screenshots"
PROMO_DIR = KIT_DIR / "promo"
BRAND_DIR = KIT_DIR / "brand"
PREVIEW_DIR = PRESS_DIR / "img" / "screenshots"
INDEX_HTML = PRESS_DIR / "index.html"
README = KIT_DIR / "README.txt"
ZIP_PATH = PRESS_DIR / "agentiloop-agent-press-kit.zip"
ZIP_TOP_FOLDER = "AgentiLoop Agent Press Kit"
ZIP_LIMIT_BYTES = 25 * 1024 * 1024
# Fixed timestamp for every archive entry. Without it the ZIP is byte-different
# on every build even when nothing changed, which re-commits megabytes for
# nothing and makes it impossible to tell a real asset change from a rebuild.
ZIP_TIMESTAMP = (2026, 1, 1, 0, 0, 0)
PREVIEW_MAX_WIDTH = 1400

# Site palette (mirrors ../styles.css).
BACKGROUND = (7, 11, 22)
ACCENT_BLUE = (59, 130, 246)
ACCENT_CYAN = (34, 211, 238)
TEXT = (232, 236, 244)
TEXT_DIM = (154, 165, 189)


@dataclass(frozen=True)
class Screenshot:
    """One entry in the screenshot grid; `file` lives in press/kit/screenshots."""

    file: str
    title: str
    alt: str
    source: str


# Order here is the order on the page.
SCREENSHOTS = [
    Screenshot(
        "agentiloop-agent-github-release.png",
        "Publishing a GitHub release",
        "AgentiLoop Agent! main window: the LLM Output panel reports that GitHub release v1.1.9.205 was created with the gh command line tool, above the Steps list and the activity log showing the shell commands it ran",
        "from the 1.1.9 release notes",
    ),
    Screenshot(
        "agentiloop-agent-test-verification.png",
        "Verifying a fix with the test suite",
        "AgentiLoop Agent! running the ResponseCompletionTests suite with xcodebuild to verify a fix, with the test output and a green TEST SUCCEEDED line in the activity log",
        "from the 1.1.8 release notes",
    ),
    Screenshot(
        "agentiloop-agent-release-notes.png",
        "Drafting release notes from git history",
        "AgentiLoop Agent! rewriting release notes to match earlier releases, with the Find in log search bar open and the git log it read in the activity log",
        "from the 1.1.4 release notes",
    ),
    Screenshot(
        "agentiloop-agent-markdown-release-notes.png",
        "Markdown rendering in the activity log",
        "AgentiLoop Agent! creating a GitHub release for another project, with emoji section headers and bullet lists rendered in the activity log and the next task typed into the input field",
        "from the 1.0.61 release notes",
    ),
    Screenshot(
        "agentiloop-agent-dmg-attach.png",
        "Building a disk image and attaching it to a release",
        "AgentiLoop Agent! attaching a freshly built DMG to a GitHub release, with the hdiutil output in the activity log",
        "from the 1.0.69 release notes",
    ),
    Screenshot(
        "agentiloop-agent-chess.png",
        "A game of chess in the output panel",
        "AgentiLoop Agent! playing chess: the LLM Output panel shows an ASCII chess board after White's second move and asks for the next move",
        "from the 1.0.93 release notes",
    ),
]

# The two screenshots layered on the composite banner (front, back).
BANNER_FRONT = "agentiloop-agent-github-release.png"
BANNER_BACK = "agentiloop-agent-chess.png"
BANNER_FILE = "agentiloop-agent-banner-screenshots.png"
BANNER_PREVIEW = PRESS_DIR / "img" / "banner-screenshots.webp"

NUMBER_WORDS = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve"}


def optimize_png(path: Path) -> None:
    """Re-save a PNG losslessly; fully opaque RGBA images are stored as RGB."""
    image = Image.open(path)
    if image.mode == "RGBA" and image.getchannel("A").getextrema() == (255, 255):
        image = image.convert("RGB")
    before = path.stat().st_size
    image.save(path, optimize=True)
    print(f"  {path.name}: {image.size[0]}x{image.size[1]} {before // 1024} KB -> {path.stat().st_size // 1024} KB")


def write_preview(source: Path, destination: Path) -> None:
    """WebP preview at page width. Alpha is kept so the window's rounded corners
    stay transparent; flattening them would paint in the wallpaper color that
    still sits under the cropped-away corners."""
    image = Image.open(source)
    image = image.convert("RGBA") if image.mode == "RGBA" else image.convert("RGB")
    if image.width > PREVIEW_MAX_WIDTH:
        ratio = PREVIEW_MAX_WIDTH / image.width
        image = image.resize((PREVIEW_MAX_WIDTH, round(image.height * ratio)), Image.LANCZOS)
    destination.parent.mkdir(parents=True, exist_ok=True)
    image.save(destination, "WEBP", quality=86, method=6)


def load_font(size: int, weight: str) -> ImageFont.FreeTypeFont:
    """San Francisco from the system, falling back to Helvetica Neue."""
    try:
        font = ImageFont.truetype("/System/Library/Fonts/SFNS.ttf", size)
        font.set_variation_by_name(weight)
        return font
    except (OSError, ValueError):
        return ImageFont.truetype("/System/Library/Fonts/HelveticaNeue.ttc", size, index=1 if weight == "Bold" else 0)


def radial_glow(size: tuple[int, int], center: tuple[int, int], radius: int, color: tuple[int, int, int], peak_alpha: int) -> Image.Image:
    """A soft radial highlight, matching the site's hero glow."""
    glow = Image.new("RGBA", size, color + (0,))
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    steps = 40
    for i in range(steps, 0, -1):
        r = radius * i / steps
        alpha = round(peak_alpha * (1 - i / steps) ** 1.6)
        draw.ellipse([center[0] - r, center[1] - r, center[0] + r, center[1] + r], fill=alpha)
    mask = mask.filter(ImageFilter.GaussianBlur(radius / 6))
    glow.putalpha(mask)
    return glow


def rounded_shot(source: Path, width: int, corner: int) -> Image.Image:
    """Scale a screenshot for the banner and round its corners.

    The source captures are already cropped to the window and carry transparent
    corners over leftover wallpaper pixels. The new mask is multiplied into the
    existing alpha rather than replacing it, so a corner that is already
    transparent can never be turned back on and reveal that wallpaper.
    """
    image = Image.open(source).convert("RGBA")
    ratio = width / image.width
    image = image.resize((width, round(image.height * ratio)), Image.LANCZOS)
    mask = Image.new("L", image.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, image.width - 1, image.height - 1], radius=corner, fill=255)
    image.putalpha(ImageChops.multiply(image.getchannel("A"), mask))
    return image


def paste_with_shadow(canvas: Image.Image, image: Image.Image, position: tuple[int, int]) -> None:
    shadow = Image.new("RGBA", (image.width + 160, image.height + 160), (0, 0, 0, 0))
    shadow_mask = Image.new("L", shadow.size, 0)
    ImageDraw.Draw(shadow_mask).rounded_rectangle([80, 100, 80 + image.width, 100 + image.height], radius=28, fill=170)
    shadow.putalpha(shadow_mask.filter(ImageFilter.GaussianBlur(34)))
    canvas.alpha_composite(shadow, (position[0] - 80, position[1] - 80))
    canvas.alpha_composite(image, position)


def render_screenshot_banner() -> Path:
    """1920x1080 composite: two screenshots on the site's dark gradient."""
    canvas = Image.new("RGBA", (1920, 1080), BACKGROUND + (255,))
    canvas.alpha_composite(radial_glow(canvas.size, (1350, 200), 900, ACCENT_BLUE, 120))
    canvas.alpha_composite(radial_glow(canvas.size, (300, 1000), 700, ACCENT_CYAN, 60))

    draw = ImageDraw.Draw(canvas)
    title_font = load_font(64, "Bold")
    sub_font = load_font(30, "Regular")
    draw.text((96, 96), "AgentiLoop", font=title_font, fill=TEXT)
    name_width = draw.textlength("AgentiLoop ", font=title_font)
    draw.text((96 + name_width, 96), "Agent!", font=title_font, fill=ACCENT_CYAN)
    draw.text((98, 176), "Agentic AI for your Mac Desktop", font=sub_font, fill=TEXT_DIM)

    back = rounded_shot(SCREENSHOT_DIR / BANNER_BACK, 1000, 22)
    front = rounded_shot(SCREENSHOT_DIR / BANNER_FRONT, 800, 22)
    paste_with_shadow(canvas, back, (860, 250))
    paste_with_shadow(canvas, front, (96, 330))

    output = PROMO_DIR / BANNER_FILE
    canvas.convert("RGB").save(output, optimize=True)
    canvas.convert("RGB").save(BANNER_PREVIEW, "WEBP", quality=88, method=6)
    print(f"  banner: {output.name} {output.stat().st_size // 1024} KB")
    return output


def figure_html(shot: Screenshot) -> str:
    png = f"kit/screenshots/{shot.file}"
    preview = f"img/screenshots/{Path(shot.file).with_suffix('.webp').name}"
    width, height = Image.open(SCREENSHOT_DIR / shot.file).size
    title = html.escape(shot.title)
    alt = html.escape(shot.alt)
    return (
        "\t\t\t\t\t\t<figure class=\"screenshot-card\">\n"
        f"\t\t\t\t\t\t\t<a class=\"screenshot-image\" href=\"{png}\" download aria-label=\"Download the {title} screenshot as a PNG\">\n"
        f"\t\t\t\t\t\t\t\t<img src=\"{preview}\" width=\"{width}\" height=\"{height}\" alt=\"{alt}\" loading=\"lazy\">\n"
        "\t\t\t\t\t\t\t</a>\n"
        "\t\t\t\t\t\t\t<figcaption>\n"
        f"\t\t\t\t\t\t\t\t<span>{title}<small>{width}×{height} PNG · {html.escape(shot.source)}</small></span>\n"
        f"\t\t\t\t\t\t\t\t<a href=\"{png}\" download>Download PNG</a>\n"
        "\t\t\t\t\t\t\t</figcaption>\n"
        "\t\t\t\t\t\t</figure>\n"
    )


def banner_figure_html() -> str:
    return (
        "\t\t\t\t\t\t<figure class=\"screenshot-card\">\n"
        f"\t\t\t\t\t\t\t<a class=\"screenshot-image\" href=\"kit/promo/{BANNER_FILE}\" download aria-label=\"Download the screenshots banner as a PNG\">\n"
        f"\t\t\t\t\t\t\t\t<img src=\"img/{BANNER_PREVIEW.name}\" width=\"1920\" height=\"1080\" alt=\"Screenshots banner: two AgentiLoop Agent! windows, one publishing a GitHub release and one playing chess, layered on a dark blue background under the AgentiLoop Agent! name\" loading=\"lazy\">\n"
        "\t\t\t\t\t\t\t</a>\n"
        "\t\t\t\t\t\t\t<figcaption>\n"
        "\t\t\t\t\t\t\t\t<span>Screenshots</span>\n"
        f"\t\t\t\t\t\t\t\t<a href=\"kit/promo/{BANNER_FILE}\" download>Download PNG</a>\n"
        "\t\t\t\t\t\t\t</figcaption>\n"
        "\t\t\t\t\t\t</figure>\n"
    )


def replace_between(text: str, start_marker: str, end_marker: str, body: str) -> str:
    pattern = re.compile(rf"(<!-- {start_marker}[^>]*-->\n).*?(\t*<!-- {end_marker} -->)", re.S)
    if not pattern.search(text):
        sys.exit(f"markers {start_marker}/{end_marker} not found in {INDEX_HTML}")
    return pattern.sub(lambda m: m.group(1) + body + m.group(2), text, count=1)


def update_index_html(count: int) -> None:
    text = INDEX_HTML.read_text()
    text = replace_between(text, "screenshots:start", "screenshots:end", "".join(figure_html(s) for s in SCREENSHOTS))
    text = replace_between(text, "banner2:start", "banner2:end", banner_figure_html())
    word = NUMBER_WORDS[count]
    text, n = re.subn(r"Includes \w+ full-resolution PNG screenshots", f"Includes {word} full-resolution PNG screenshots", text)
    if n != 1:
        sys.exit("hero download note not found in index.html")
    INDEX_HTML.write_text(text)
    print(f"  index.html: {count} screenshot figures, banner figure, hero note updated")


def stamp_assets() -> None:
    """Add ?v=<content hash> to the stylesheet and script links.

    Without this a browser that cached an older press.css keeps using it after a
    redeploy, silently rendering the page with missing rules.
    """
    text = INDEX_HTML.read_text()
    for name in ("press.css", "press.js"):
        digest = hashlib.sha256((PRESS_DIR / name).read_bytes()).hexdigest()[:8]
        text, n = re.subn(rf'{re.escape(name)}(\?v=[0-9a-f]+)?"', f'{name}?v={digest}"', text)
        if n != 1:
            sys.exit(f"expected exactly one reference to {name} in index.html, found {n}")
        print(f"  {name}?v={digest}")
    INDEX_HTML.write_text(text)


def update_readme(count: int) -> None:
    """README.txt is the plain-text fact sheet; only its screenshot count is generated."""
    text = README.read_text()
    word = NUMBER_WORDS[count]
    text, n = re.subn(r"^Screenshots contains \w+ full-resolution", f"Screenshots contains {word} full-resolution", text, flags=re.M)
    if n != 1:
        sys.exit("Screenshots line not found in README.txt")
    README.write_text(text)


def build_zip() -> None:
    entries: list[tuple[Path, str]] = [(README, README.name)]
    for folder, label in ((SCREENSHOT_DIR, "Screenshots"), (PROMO_DIR, "Promo"), (BRAND_DIR, "Brand")):
        for path in sorted(folder.iterdir()):
            if path.suffix.lower() == ".png":
                entries.append((path, f"{label}/{path.name}"))
    with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path, arcname in entries:
            info = zipfile.ZipInfo(f"{ZIP_TOP_FOLDER}/{arcname}", date_time=ZIP_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes())
    size = ZIP_PATH.stat().st_size
    print(f"  {ZIP_PATH.name}: {len(entries)} files, {size / 1024 / 1024:.1f} MiB")
    if size > ZIP_LIMIT_BYTES:
        sys.exit(f"ZIP is over the 25 MiB Cloudflare static asset limit ({size} bytes)")


def main() -> None:
    missing = [s.file for s in SCREENSHOTS if not (SCREENSHOT_DIR / s.file).exists()]
    if missing:
        sys.exit(f"missing screenshots: {missing}")
    stray = sorted(p.name for p in SCREENSHOT_DIR.glob("*.png"))
    listed = sorted(s.file for s in SCREENSHOTS)
    if stray != listed:
        sys.exit(f"press/kit/screenshots and the SCREENSHOTS manifest disagree: on disk {stray}, listed {listed}")

    print("Optimizing screenshots")
    for shot in SCREENSHOTS:
        optimize_png(SCREENSHOT_DIR / shot.file)
        write_preview(SCREENSHOT_DIR / shot.file, PREVIEW_DIR / Path(shot.file).with_suffix(".webp").name)
    print("Rendering banner")
    render_screenshot_banner()
    print("Updating page and text")
    update_index_html(len(SCREENSHOTS))
    stamp_assets()
    update_readme(len(SCREENSHOTS))
    print("Building ZIP")
    build_zip()


if __name__ == "__main__":
    main()
