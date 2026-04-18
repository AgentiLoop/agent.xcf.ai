// TickyTacky — a cool tic-tac-toe
(() => {
  "use strict";

  const WIN_LINES = [
    [0,1,2],[3,4,5],[6,7,8],   // rows
    [0,3,6],[1,4,7],[2,5,8],   // cols
    [0,4,8],[2,4,6]            // diagonals
  ];

  // DOM
  const boardEl = document.getElementById("board");
  const cells = Array.from(document.querySelectorAll(".cell"));
  const scoreXEl = document.getElementById("scoreX");
  const scoreOEl = document.getElementById("scoreO");
  const scoreTieEl = document.getElementById("scoreTie");
  const turnMarkEl = document.getElementById("turnMark");
  const bannerEl = document.getElementById("banner");
  const resetBtn = document.getElementById("resetBtn");
  const clearBtn = document.getElementById("clearBtn");
  const modeBtns = document.querySelectorAll(".mode-btn");
  const diffBtns = document.querySelectorAll(".diff-btn");
  const diffWrap = document.getElementById("difficultyWrap");
  const strikeEl = document.getElementById("strike");
  const strikeLine = document.getElementById("strikeLine");

  // Persistence
  const STORAGE_KEY = "tickytacky:v1";
  function loadState() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return {};
      const s = JSON.parse(raw);
      return (s && typeof s === "object") ? s : {};
    } catch { return {}; }
  }
  function saveState() {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify({
        scores, mode, difficulty,
      }));
    } catch {}
  }
  const saved = loadState();

  // State
  let board = Array(9).fill(null);
  let current = "X";
  let scores = (saved.scores && typeof saved.scores === "object" &&
                typeof saved.scores.X === "number" &&
                typeof saved.scores.O === "number" &&
                typeof saved.scores.T === "number")
               ? { X: saved.scores.X, O: saved.scores.O, T: saved.scores.T }
               : { X: 0, O: 0, T: 0 };
  let mode = (saved.mode === "pvp" || saved.mode === "pvc") ? saved.mode : "pvc";
  let difficulty = ["easy","medium","hard"].includes(saved.difficulty)
                   ? saved.difficulty : "hard";
  let gameOver = false;
  let botThinking = false;

  // ---------- Rendering ----------
  function render() {
    cells.forEach((c, i) => {
      const mark = board[i];
      c.classList.remove("mark-x", "mark-o", "win");
      c.textContent = mark || "";
      if (mark === "X") c.classList.add("mark-x");
      if (mark === "O") c.classList.add("mark-o");
      c.disabled = gameOver || !!mark || botThinking;
    });

    turnMarkEl.textContent = current;
    turnMarkEl.classList.toggle("turn-x", current === "X");
    turnMarkEl.classList.toggle("turn-o", current === "O");
  }

  function setBanner(text, cls) {
    bannerEl.textContent = text;
    bannerEl.className = "banner";
    if (text) {
      bannerEl.classList.add("show");
      if (cls) bannerEl.classList.add(cls);
    }
  }

  function bumpScore(el) {
    el.parentElement.classList.add("bump");
    setTimeout(() => el.parentElement.classList.remove("bump"), 500);
  }

  // ---------- Strike line (SVG) ----------
  // Board viewBox is 0..300. Each cell center is at 50, 150, 250 (with the
  // board grid gap + padding roughly at 10px; visual is close enough).
  const STRIKE_COORDS = {
    "0,1,2": [10, 50, 290, 50],
    "3,4,5": [10, 150, 290, 150],
    "6,7,8": [10, 250, 290, 250],
    "0,3,6": [50, 10, 50, 290],
    "1,4,7": [150, 10, 150, 290],
    "2,5,8": [250, 10, 250, 290],
    "0,4,8": [15, 15, 285, 285],
    "2,4,6": [285, 15, 15, 285],
  };
  function drawStrike(line, winner) {
    const key = line.join(",");
    const coords = STRIKE_COORDS[key];
    if (!coords) return;
    strikeLine.setAttribute("x1", coords[0]);
    strikeLine.setAttribute("y1", coords[1]);
    strikeLine.setAttribute("x2", coords[2]);
    strikeLine.setAttribute("y2", coords[3]);
    strikeEl.classList.remove("x", "o", "active");
    strikeEl.classList.add(winner === "X" ? "x" : "o");
    // Force reflow so the dash animation plays from 0
    void strikeEl.getBoundingClientRect();
    strikeEl.classList.add("active");
  }
  function clearStrike() {
    strikeEl.classList.remove("active", "x", "o");
    strikeLine.setAttribute("x1", 0);
    strikeLine.setAttribute("y1", 0);
    strikeLine.setAttribute("x2", 0);
    strikeLine.setAttribute("y2", 0);
  }

  // ---------- Game logic ----------
  function checkWinner(b) {
    for (const line of WIN_LINES) {
      const [a, c, d] = line;
      if (b[a] && b[a] === b[c] && b[a] === b[d]) {
        return { winner: b[a], line };
      }
    }
    if (b.every(Boolean)) return { winner: "T", line: null };
    return null;
  }

  function endGame(result) {
    gameOver = true;
    if (result.winner === "T") {
      scores.T += 1;
      scoreTieEl.textContent = scores.T;
      bumpScore(scoreTieEl);
      setBanner("It's a tie — run it back!", "tie");
    } else {
      const w = result.winner;
      scores[w] += 1;
      if (w === "X") { scoreXEl.textContent = scores.X; bumpScore(scoreXEl); }
      else { scoreOEl.textContent = scores.O; bumpScore(scoreOEl); }
      if (result.line) {
        result.line.forEach(i => cells[i].classList.add("win"));
        drawStrike(result.line, w);
      }
      const who = mode === "pvc"
        ? (w === "X" ? "You win! ✦" : "Bot wins. Try again.")
        : `Player ${w} wins!`;
      setBanner(who, w === "X" ? "win-x" : "win-o");
      if (mode === "pvp" || w === "X") confettiBurst();
    }
    render();
    saveState();
  }

  function makeMove(i, mark) {
    if (gameOver || board[i]) return false;
    board[i] = mark;
    const res = checkWinner(board);
    if (res) {
      render();
      endGame(res);
      return true;
    }
    current = mark === "X" ? "O" : "X";
    render();
    return true;
  }

  function onCellClick(e) {
    const cell = e.currentTarget;
    const i = Number(cell.dataset.i);
    if (gameOver || botThinking || board[i]) return;

    if (mode === "pvp") {
      makeMove(i, current);
      return;
    }

    // PvC: human is always X
    if (current !== "X") return;
    makeMove(i, "X");
    if (!gameOver) scheduleBot();
  }

  function scheduleBot() {
    botThinking = true;
    render();
    const delay = 280 + Math.random() * 260;
    setTimeout(() => {
      if (gameOver) { botThinking = false; render(); return; }
      const move = chooseBotMove();
      botThinking = false;
      if (move != null) makeMove(move, "O");
    }, delay);
  }

  // ---------- AI ----------
  function availableMoves(b) {
    const out = [];
    for (let i = 0; i < 9; i++) if (!b[i]) out.push(i);
    return out;
  }

  // Find an immediate winning/blocking move for `mark` — returns cell index or null.
  function findImmediate(mark) {
    for (const i of availableMoves(board)) {
      board[i] = mark;
      const res = checkWinner(board);
      board[i] = null;
      if (res && res.winner === mark) return i;
    }
    return null;
  }

  // "Toddler random" — like a 3-year-old picking a square: drawn to the
  // shiny center, then corners, then edges. Not uniform, not optimal,
  // just plausibly distracted. Center weight 4, corner weight 2, edge weight 1.
  function toddlerMove() {
    const moves = availableMoves(board);
    if (!moves.length) return null;
    const corners = new Set([0, 2, 6, 8]);
    const center = 4;
    const weighted = [];
    for (const m of moves) {
      const w = m === center ? 4 : corners.has(m) ? 2 : 1;
      for (let i = 0; i < w; i++) weighted.push(m);
    }
    return weighted[Math.floor(Math.random() * weighted.length)];
  }

  function chooseBotMove() {
    const moves = availableMoves(board);
    if (!moves.length) return null;

    if (difficulty === "easy") {
      // Easy: often misses threats like a casual player — but not clueless.
      // Takes an immediate win 65% of the time.
      // Blocks an immediate loss 45% of the time.
      // Plays optimally 30% of the time when there's no immediate threat.
      // Otherwise: toddler-random (center > corners > edges).
      const win = findImmediate("O");
      if (win != null && Math.random() < 0.65) return win;
      const block = findImmediate("X");
      if (block != null && Math.random() < 0.45) return block;
      if (Math.random() < 0.30) return minimaxMove("O");
      return toddlerMove();
    }
    if (difficulty === "medium") {
      // Medium: mostly competent but still misses sometimes.
      // Takes an immediate win 85% of the time.
      // Blocks an immediate loss 70% of the time.
      // Plays optimally 50% of the time otherwise.
      // Otherwise: toddler-random (center > corners > edges).
      const win = findImmediate("O");
      if (win != null && Math.random() < 0.85) return win;
      const block = findImmediate("X");
      if (block != null && Math.random() < 0.70) return block;
      if (Math.random() < 0.50) return minimaxMove("O");
      return toddlerMove();
    }
    return minimaxMove("O");
  }

  function minimaxMove(me) {
    const opp = me === "O" ? "X" : "O";
    let bestScore = -Infinity;
    let best = null;
    // Tiny randomness among equal-score moves for variety
    const candidates = [];
    for (const i of availableMoves(board)) {
      board[i] = me;
      const s = minimax(board, false, me, opp, 0);
      board[i] = null;
      if (s > bestScore) {
        bestScore = s;
        candidates.length = 0;
        candidates.push(i);
      } else if (s === bestScore) {
        candidates.push(i);
      }
    }
    best = candidates[Math.floor(Math.random() * candidates.length)];
    return best;
  }

  function minimax(b, maximizing, me, opp, depth) {
    const res = checkWinner(b);
    if (res) {
      if (res.winner === me) return 10 - depth;
      if (res.winner === opp) return depth - 10;
      return 0;
    }
    if (maximizing) {
      let best = -Infinity;
      for (const i of availableMoves(b)) {
        b[i] = me;
        best = Math.max(best, minimax(b, false, me, opp, depth + 1));
        b[i] = null;
      }
      return best;
    } else {
      let best = Infinity;
      for (const i of availableMoves(b)) {
        b[i] = opp;
        best = Math.min(best, minimax(b, true, me, opp, depth + 1));
        b[i] = null;
      }
      return best;
    }
  }

  // ---------- Confetti ----------
  function confettiBurst() {
    const colors = ["#ff4d8d", "#4df0ff", "#7b5bff", "#c79cff", "#ffd86b"];
    const n = 60;
    for (let i = 0; i < n; i++) {
      const piece = document.createElement("div");
      piece.className = "confetti";
      piece.style.left = Math.random() * 100 + "vw";
      piece.style.background = colors[Math.floor(Math.random() * colors.length)];
      piece.style.animationDuration = (1.6 + Math.random() * 1.8) + "s";
      piece.style.animationDelay = (Math.random() * 0.25) + "s";
      piece.style.transform = `rotate(${Math.random() * 360}deg)`;
      piece.style.borderRadius = Math.random() < 0.3 ? "50%" : "2px";
      document.body.appendChild(piece);
      setTimeout(() => piece.remove(), 3500);
    }
  }

  // ---------- Controls ----------
  function newRound(keepScores = true) {
    board = Array(9).fill(null);
    gameOver = false;
    botThinking = false;
    current = "X";
    clearStrike();
    setBanner("", "");
    if (!keepScores) {
      scores = { X: 0, O: 0, T: 0 };
      scoreXEl.textContent = "0";
      scoreOEl.textContent = "0";
      scoreTieEl.textContent = "0";
    }
    render();
    saveState();
  }

  function setMode(next) {
    mode = next;
    modeBtns.forEach(b => {
      const active = b.dataset.mode === next;
      b.classList.toggle("active", active);
      b.setAttribute("aria-selected", active ? "true" : "false");
    });
    diffWrap.classList.toggle("hidden", next !== "pvc");
    newRound(false);
    saveState();
  }

  function setDifficulty(next) {
    difficulty = next;
    diffBtns.forEach(b => b.classList.toggle("active", b.dataset.diff === next));
    newRound(true);
    saveState();
  }

  // ---------- Hover glow tracking ----------
  function onCellMove(e) {
    const cell = e.currentTarget;
    const r = cell.getBoundingClientRect();
    const x = ((e.clientX - r.left) / r.width) * 100;
    const y = ((e.clientY - r.top) / r.height) * 100;
    cell.style.setProperty("--mx", x + "%");
    cell.style.setProperty("--my", y + "%");
  }

  // ---------- Keyboard ----------
  function onKey(e) {
    // number keys 1-9 map to cells 0-8 (numpad layout: top row = 1,2,3)
    const n = Number(e.key);
    if (n >= 1 && n <= 9) {
      const i = n - 1;
      const cell = cells[i];
      if (cell && !cell.disabled) cell.click();
    } else if (e.key === "r" || e.key === "R") {
      newRound(true);
    }
  }

  // ---------- Wire up ----------
  cells.forEach(c => {
    c.addEventListener("click", onCellClick);
    c.addEventListener("mousemove", onCellMove);
  });
  resetBtn.addEventListener("click", () => newRound(true));
  clearBtn.addEventListener("click", () => newRound(false));
  modeBtns.forEach(b => b.addEventListener("click", () => setMode(b.dataset.mode)));
  diffBtns.forEach(b => b.addEventListener("click", () => setDifficulty(b.dataset.diff)));
  window.addEventListener("keydown", onKey);

  // Initial render — reflect persisted mode, difficulty, and scores
  scoreXEl.textContent = String(scores.X);
  scoreOEl.textContent = String(scores.O);
  scoreTieEl.textContent = String(scores.T);
  modeBtns.forEach(b => {
    const active = b.dataset.mode === mode;
    b.classList.toggle("active", active);
    b.setAttribute("aria-selected", active ? "true" : "false");
  });
  diffBtns.forEach(b => b.classList.toggle("active", b.dataset.diff === difficulty));
  diffWrap.classList.toggle("hidden", mode !== "pvc");
  render();
})();
