#!/usr/bin/env python3
"""Crop full-screen captures down to the AgentiLoop Agent! window.

Usage:  python3 press/tools/crop-window.py SOURCE.png DESTINATION.png [...]
        (pass pairs; a single directory argument pair crops every PNG inside)

The app window is dark and nearly grey; the desktop wallpaper and menu bar are
not. Rows and columns where at least 40% of pixels are "window-dark" bound the
window. The corner radius is measured from the top edge and the same rounded
mask is applied, so the result has transparent corners like a native macOS
window capture. The script refuses to guess: if no plausible window is found it
exits with an error instead of writing a file.

Requires Pillow.
"""

from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageDraw

DARK_MAX = 72          # max(R, G, B) at or below this counts as dark
GREY_SPREAD_MAX = 28   # max(R, G, B) - min(R, G, B) at or below this counts as grey
ROW_FILL = 0.40        # fraction of a row or column that must be dark to count as window


def window_mask(image: Image.Image) -> Image.Image:
    rgb = image.convert("RGB")
    r, g, b = rgb.split()
    from PIL import ImageChops
    maximum = ImageChops.lighter(ImageChops.lighter(r, g), b)
    minimum = ImageChops.darker(ImageChops.darker(r, g), b)
    spread = ImageChops.subtract(maximum, minimum)
    dark = maximum.point(lambda v: 255 if v <= DARK_MAX else 0)
    grey = spread.point(lambda v: 255 if v <= GREY_SPREAD_MAX else 0)
    return ImageChops.multiply(dark, grey)


def window_bounds(mask: Image.Image) -> tuple[int, int, int, int]:
    width, height = mask.size
    pixels = mask.load()
    rows = [sum(1 for x in range(width) if pixels[x, y]) / width for y in range(height)]
    cols = [sum(1 for y in range(height) if pixels[x, y]) / height for x in range(width)]
    row_hits = [y for y, f in enumerate(rows) if f >= ROW_FILL]
    if not row_hits:
        raise SystemExit("no window found: no row is 40% dark")
    top, bottom = row_hits[0], row_hits[-1]
    band_height = bottom - top + 1
    col_hits = [x for x, f in enumerate(cols) if f * height / band_height >= ROW_FILL]
    if not col_hits:
        raise SystemExit("no window found: no column is 40% dark")
    left, right = col_hits[0], col_hits[-1]
    return left, top, right + 1, bottom + 1


def corner_radius(mask: Image.Image, bounds: tuple[int, int, int, int]) -> int:
    """Distance from the crop's top-left corner to the first dark pixel on its top row."""
    left, top, right, _ = bounds
    pixels = mask.load()
    for x in range(left, right):
        if pixels[x, top]:
            return max(0, x - left)
    return 0


def crop(source: Path, destination: Path) -> None:
    image = Image.open(source).convert("RGBA")
    mask = window_mask(image)
    bounds = window_bounds(mask)
    radius = corner_radius(mask, bounds)
    window = image.crop(bounds)
    if window.width < image.width * 0.3 or window.height < image.height * 0.3:
        raise SystemExit(f"{source.name}: detected window {window.size} is implausibly small")
    rounded = Image.new("L", window.size, 0)
    ImageDraw.Draw(rounded).rounded_rectangle([0, 0, window.width - 1, window.height - 1], radius=radius, fill=255)
    window.putalpha(rounded)
    destination.parent.mkdir(parents=True, exist_ok=True)
    window.save(destination, optimize=True)
    print(f"{source.name}: {image.size[0]}x{image.size[1]} -> {window.width}x{window.height} at {bounds}, corner radius {radius}px -> {destination}")


def main(argv: list[str]) -> None:
    if len(argv) < 2 or len(argv) % 2:
        raise SystemExit(__doc__)
    pairs = list(zip(argv[0::2], argv[1::2]))
    for src, dst in pairs:
        source, destination = Path(src), Path(dst)
        if source.is_dir():
            for png in sorted(source.glob("*.png")):
                crop(png, destination / png.name)
        else:
            crop(source, destination)


if __name__ == "__main__":
    main(sys.argv[1:])
