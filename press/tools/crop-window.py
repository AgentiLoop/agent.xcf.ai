#!/usr/bin/env python3
"""Crop full-screen captures down to the AgentiLoop Agent! window.

Usage:  python3 press/tools/crop-window.py SOURCE DESTINATION [SOURCE DESTINATION ...]
        A SOURCE that is a directory crops every PNG inside it.

The window's chrome is neutral grey at every brightness, from the near-black
title bar to the lighter border ring. The desktop wallpaper and the menu bar over
it are not: they always carry colour. Testing for neutrality rather than
darkness is what makes the edge findable, because the window's own outline fades
into the wallpaper and any brightness threshold picks it up only intermittently.
Rows and columns at least 40% neutral bound the window.

Corners are not drawn as circles. macOS 26 draws a continuous corner (a
squircle), and approximating it with a circular arc removes about ten pixels too
much at the steepest part of the curve, which reads as an over-rounded corner.
Instead the real corner profile is measured off the capture itself: for each row
of the corner region, the column where the window actually begins. That profile,
mirrored into all four corners, is the mask, so the cut follows the window's own
shape rather than an approximation of it.

The script refuses to guess: if no plausible window is found it exits with an
error instead of writing a file.

Requires Pillow.
"""

from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageChops

NEUTRAL_SPREAD_MAX = 10  # max(R, G, B) - min(R, G, B) at or below this counts as neutral
EDGE_FILL = 0.40         # fraction of a row or column that must be neutral to be window
CORNER_PROBE = 160      # how far into the window to look for the corner curve
SUPERSAMPLE = 8         # corner mask is built this many times larger, then averaged down


def window_mask(image: Image.Image) -> Image.Image:
    """White where a pixel is neutral enough to be window chrome, black elsewhere."""
    r, g, b = image.convert("RGB").split()
    maximum = ImageChops.lighter(ImageChops.lighter(r, g), b)
    minimum = ImageChops.darker(ImageChops.darker(r, g), b)
    spread = ImageChops.subtract(maximum, minimum)
    return spread.point(lambda v: 255 if v <= NEUTRAL_SPREAD_MAX else 0)


def window_bounds(mask: Image.Image) -> tuple[int, int, int, int]:
    width, height = mask.size
    pixels = mask.load()
    rows = [sum(1 for x in range(width) if pixels[x, y]) / width for y in range(height)]
    row_hits = [y for y, f in enumerate(rows) if f >= EDGE_FILL]
    if not row_hits:
        raise SystemExit("no window found: no row is 40% dark")
    top, bottom = row_hits[0], row_hits[-1]
    band = bottom - top + 1
    cols = [sum(1 for y in range(top, bottom + 1) if pixels[x, y]) / band for x in range(width)]
    col_hits = [x for x, f in enumerate(cols) if f >= EDGE_FILL]
    if not col_hits:
        raise SystemExit("no window found: no column is 40% dark")
    return col_hits[0], top, col_hits[-1] + 1, bottom + 1


def corner_profile(mask: Image.Image, bounds: tuple[int, int, int, int]) -> list[int]:
    """Inset of the window edge for each row below the top-left corner.

    profile[i] is how many columns in from the left edge the window starts on the
    i-th row. The first dark pixel is the window's own outer outline, so the
    border is kept rather than shaved off; requiring a run of dark pixels instead
    would skip past the light inner border and cut into the frame. The profile is
    forced to be non-increasing so a stray dark wallpaper pixel cannot punch a
    notch into the curve.
    """
    left, top, _, _ = bounds
    pixels = mask.load()
    raw: list[int] = []
    for dy in range(CORNER_PROBE):
        inset = next((dx for dx in range(CORNER_PROBE) if pixels[left + dx, top + dy]), CORNER_PROBE)
        raw.append(inset)
    profile: list[int] = []
    ceiling = raw[0]
    for value in raw:
        ceiling = min(ceiling, value)
        profile.append(ceiling)
    # The curve flattens into the straight edge; stop there so the corner does not
    # keep shaving a sliver off the sides.
    floor = min(profile)
    return [max(0, value - floor) for value in profile]


def corner_wedge(profile: list[int]) -> Image.Image:
    """One anti-aliased top-left corner, as an alpha tile.

    The measured profile has one integer per row, so using it directly would
    leave a visible staircase along the curve. The wedge is drawn SUPERSAMPLE
    times larger with the profile interpolated between rows, then averaged back
    down, which produces the partial alpha a real screenshot edge has.
    """
    extent = sum(1 for inset in profile if inset > 0)
    if extent == 0:
        return Image.new("L", (0, 0), 255)
    scale = SUPERSAMPLE
    big = Image.new("L", (extent * scale, extent * scale), 255)
    pixels = big.load()
    for row in range(extent * scale):
        position = row / scale
        low = min(int(position), extent - 1)
        high = min(low + 1, extent - 1)
        inset = profile[low] + (profile[high] - profile[low]) * (position - low)
        for column in range(min(round(inset * scale), extent * scale)):
            pixels[column, row] = 0
    return big.resize((extent, extent), Image.BOX)


def corner_alpha(size: tuple[int, int], profile: list[int]) -> Image.Image:
    """Opaque everywhere except the four corners, which follow the measured curve."""
    width, height = size
    alpha = Image.new("L", size, 255)
    wedge = corner_wedge(profile)
    if wedge.size[0] == 0:
        return alpha
    extent = wedge.size[0]
    alpha.paste(wedge, (0, 0))
    alpha.paste(wedge.transpose(Image.FLIP_LEFT_RIGHT), (width - extent, 0))
    alpha.paste(wedge.transpose(Image.FLIP_TOP_BOTTOM), (0, height - extent))
    alpha.paste(wedge.transpose(Image.ROTATE_180), (width - extent, height - extent))
    return alpha


def crop(source: Path, destination: Path) -> None:
    image = Image.open(source).convert("RGBA")
    mask = window_mask(image)
    bounds = window_bounds(mask)
    window = image.crop(bounds)
    if window.width < image.width * 0.3 or window.height < image.height * 0.3:
        raise SystemExit(f"{source.name}: detected window {window.size} is implausibly small")
    profile = corner_profile(mask, bounds)
    window.putalpha(corner_alpha(window.size, profile))
    destination.parent.mkdir(parents=True, exist_ok=True)
    window.save(destination, optimize=True)
    print(f"{source.name}: {image.size[0]}x{image.size[1]} -> {window.width}x{window.height} "
          f"at {bounds}, corner inset {profile[0]}px over {sum(1 for p in profile if p)} rows")


def main(argv: list[str]) -> None:
    if len(argv) < 2 or len(argv) % 2:
        raise SystemExit(__doc__)
    for src, dst in zip(argv[0::2], argv[1::2]):
        source, destination = Path(src), Path(dst)
        if source.is_dir():
            for png in sorted(source.glob("*.png")):
                crop(png, destination / png.name)
        else:
            crop(source, destination)


if __name__ == "__main__":
    main(sys.argv[1:])
