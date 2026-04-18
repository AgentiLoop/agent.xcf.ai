# TickyTacky ✦

A cool neon tic-tac-toe game. Runs in the browser — no build step, no dependencies.

## Features

- **vs Bot** with three difficulty levels:
  - *Easy* — threat-aware: always takes wins, always blocks, 60% optimal otherwise
  - *Medium* — near-perfect: takes wins, blocks, 90% optimal
  - *Impossible* — full minimax with depth-weighted scoring (never loses)
- **2 Player** hot-seat mode
- Animated neon title, glowing X/O marks, confetti on win
- Animated SVG strike line through the winning row/column/diagonal
- Score tracking across rounds (X / Ties / O)
- Keyboard play: `1`–`9` (numpad layout, top-left = 1), `R` to reset the round
- Pointer-follow hover glow on every cell

## Play

Open `index.html` in any modern browser:

```bash
open index.html
```

Or serve the folder with any static server — it's three files and no build step.

## Files

- `index.html` — markup
- `style.css`  — all the glow
- `game.js`    — game state, minimax AI, rendering
