---
title: The Whole Family Ships: Agent! 1.1.87 and AgentiLoop CLI 0.0.5
description: Agent! for Mac gets Auto-Pilot, six new providers, a stricter critic and macOS 14.6 support. The Rust and Go CLIs get a bigger toolbox: search, web fetch, todos, AGENTS.md, /undo, custom commands and --json.
tags: Announcement, Release, Cross-Platform
---
<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 380" role="img" aria-labelledby="fam-title fam-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="fam-title">The AgentiLoop family: one Mac app and two terminals</title>
<desc id="fam-desc">A big Mac window labeled Agent! 1.1.87 stands in the middle. On its left a terminal window shows a little crab and the label Rust 0.0.5; on its right a terminal window shows a little gopher and the label Go 0.0.5. Dotted lines connect all three to a shared loop symbol at the top.</desc>
<rect width="760" height="380" rx="20" fill="#0f1724"/>
<g fill="#6fb6ff" opacity=".35"><circle cx="60" cy="50" r="2"/><circle cx="700" cy="70" r="2"/><circle cx="640" cy="330" r="2"/><circle cx="110" cy="320" r="2"/><circle cx="380" cy="350" r="2"/><circle cx="520" cy="40" r="2"/><circle cx="230" cy="36" r="2"/></g>
<g fill="none" stroke="#6fb6ff" stroke-width="3" stroke-dasharray="4 8" stroke-linecap="round"><path d="M380 80V112"/><path d="M350 62Q170 70 140 150"/><path d="M410 62Q590 70 620 150"/></g>
<g fill="none" stroke="#9fd2ff" stroke-width="5" stroke-linecap="round"><path d="M380 55C392 39 412 39 412 55C412 71 392 71 380 55C368 39 348 39 348 55C348 71 368 71 380 55Z"/></g>
<rect x="250" y="112" width="260" height="190" rx="16" fill="#1d2a3d" stroke="#6fb6ff" stroke-width="3"/>
<rect x="250" y="112" width="260" height="34" rx="16" fill="#26364d"/><rect x="250" y="130" width="260" height="16" fill="#26364d"/>
<circle cx="272" cy="129" r="6" fill="#ff5f57"/><circle cx="292" cy="129" r="6" fill="#febc2e"/><circle cx="312" cy="129" r="6" fill="#28c840"/>
<rect x="340" y="164" width="80" height="80" rx="20" fill="#2f7bf5"/>
<g fill="#fff"><circle cx="358" cy="186" r="5"/><circle cx="402" cy="186" r="5"/><circle cx="380" cy="204" r="5"/><circle cx="360" cy="226" r="5"/><circle cx="400" cy="226" r="5"/></g>
<g fill="none" stroke="#fff" stroke-width="2" opacity=".8"><path d="M358 186L380 204L402 186M380 204L360 226M380 204L400 226M360 226H400M358 186H402M358 186L360 226M402 186L400 226"/></g>
<text x="380" y="280" text-anchor="middle" font-family="system-ui,sans-serif" font-size="22" font-weight="700" fill="#e8f2ff">Agent! 1.1.87</text>
<rect x="40" y="150" width="190" height="150" rx="12" fill="#121c2a" stroke="#f08a4b" stroke-width="3"/>
<text x="56" y="178" font-family="ui-monospace,monospace" font-size="15" fill="#f08a4b">$ agentiloop</text>
<g fill="#f08a4b" stroke="#0f1724" stroke-width="2"><ellipse cx="135" cy="236" rx="34" ry="22"/><circle cx="92" cy="214" r="10"/><circle cx="178" cy="214" r="10"/></g>
<g stroke="#f08a4b" stroke-width="4" stroke-linecap="round"><path d="M110 256l-10 14M122 258l-6 14M148 258l6 14M160 256l10 14M100 222l8 6M170 222l-8 6"/></g>
<circle cx="124" cy="230" r="4" fill="#0f1724"/><circle cx="146" cy="230" r="4" fill="#0f1724"/>
<text x="135" y="292" text-anchor="middle" font-family="system-ui,sans-serif" font-size="17" font-weight="700" fill="#ffd2b5">Rust 0.0.5</text>
<rect x="530" y="150" width="190" height="150" rx="12" fill="#121c2a" stroke="#4fd1e8" stroke-width="3"/>
<text x="546" y="178" font-family="ui-monospace,monospace" font-size="15" fill="#4fd1e8">$ agentiloop</text>
<g stroke="#0f1724" stroke-width="2"><ellipse cx="625" cy="236" rx="30" ry="36" fill="#4fd1e8"/><circle cx="600" cy="204" r="7" fill="#4fd1e8"/><circle cx="650" cy="204" r="7" fill="#4fd1e8"/></g>
<circle cx="612" cy="222" r="9" fill="#fff"/><circle cx="638" cy="222" r="9" fill="#fff"/><circle cx="612" cy="222" r="4" fill="#0f1724"/><circle cx="638" cy="222" r="4" fill="#0f1724"/>
<text x="625" y="292" text-anchor="middle" font-family="system-ui,sans-serif" font-size="17" font-weight="700" fill="#c8f4fb">Go 0.0.5</text>
<text x="380" y="345" text-anchor="middle" font-family="system-ui,sans-serif" font-size="18" fill="#9fb6d4">One loop. Three ways to run it.</text>
</svg>
<figcaption>The AgentiLoop family on October 1: Agent! for Mac, plus the Rust and Go command-line editions.</figcaption>
</figure>

Today the whole family ships at once. **Agent! 1.1.87** is the new release of the Mac app, and **AgentiLoop CLI 0.0.5** is out for both [Rust](https://github.com/AgentiLoop/AgentiLoopCLI/releases/tag/v0.0.5) and [Go](https://github.com/AgentiLoop/AgentiLoopGo/releases/tag/v0.0.5). It's a full release, not a pre-release, and it's the biggest step yet for all three.

Here's what's new, straight from the git history.

## Agent! 1.1.87 for Mac

The last full release of the Mac app was 1.1.33 on September 12. A lot has happened since: 449 commits went into 1.1.87. These are the highlights.

### 🤖 Auto-Pilot: `/auto <goal>`

The headline feature. Give Agent! a goal, and `/auto` runs it as a series of unattended cycles inside a time budget. Each cycle works toward the goal, checks where it stands and keeps going.

- No cycle or iteration cap. It works on LLM tabs and keeps a goal history, so `/auto last` and `/auto #N` bring back an earlier goal.
- Sessions survive app restarts and resume on the same tab.
- **Esc** stops only the current cycle. **Stop All** (or `/auto stop all`) ends the session.

This is the agent loop with the human stepping back on purpose: you set the destination and the budget, and Agent! drives.

### 🔌 Six new providers, and fewer settings to fiddle with

New in 1.1.87: **Fluxion AI** (with OpenAI and Anthropic protocol options), **Muse Code** (reuses your `muse login` subscription), **Requesty**, **A2Agent**, **OrcaRouter** and **Qwen Code** on the Coding Plan. There's also an experimental **fm serve** provider that exposes Apple Foundation Models over a local Chat Completions API.

Vision support is now detected from each provider's catalog metadata, so the Force Vision toggle isn't needed anymore. Under the hood, every provider now lives in one registry, `APIProvider`, instead of a dozen separate code paths.

### 🧐 A critic that can't be talked out of it

Agent! has a critic gate: a second model reviews the change before the task is called done. In 1.1.87 the review is **enforced**. An unchanged diff is refused, a changed diff is reviewed again, and issues can't be waved away as "out of scope." The critic now also runs on Codex and Apple Intelligence, and the log shows which issues it found and whether the code changed afterward.

Alongside it is **Jev**, the TypeSafe System One decision layer that advises the tool loop. Its settings live in the new LLM Common Settings.

### 🧠 Smarter context

Compaction got a careful pass. Thresholds are now sized from the model *actually in use* (the tab's model or the fallback), and fetched Ollama context windows are remembered. That fixes a bug where some models were compacted at 16K. The kept tail and microcompact are bounded by tokens rather than message counts, oversized blocks are capped first, and context-overflow and `max_tokens` errors are detected the same way across providers.

### 🖥️ More Macs, more languages

- **macOS 14.6 Sonoma and later**, on Apple Silicon and Intel. Apple Intelligence (Foundation Models) features need macOS 26.
- The app is localized into Spanish, French, German, Chinese (Simplified), Russian, Korean and Japanese.
- New accessibility actions: `wait_until_actionable`, `select_text_range` and `observe_start/poll/stop/list`.
- Install with Homebrew: `brew update && brew install --cask agentiloop-agent`.

### 🔒 Safer by default

Recursive deletion of the current project folder is now blocked. An app-wide bug hunt fixed a ShellSafety `&` read-only bypass, an Ollama streaming stall and several crashes. `task_complete` is refused when the summary points at output that was never written, and local models that run out of memory stop immediately with a clear reason instead of spinning.

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 330" role="img" aria-labelledby="box-title box-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="box-title">A bigger toolbox for the CLI</title>
<desc id="box-desc">An open red toolbox labeled 0.0.5. Tools rise out of it on labeled tags: glob and grep with a magnifying glass, web_fetch with a globe, todo_write with a checklist, /undo with a curved arrow, AGENTS.md with a document, and --json with curly braces.</desc>
<rect width="760" height="330" rx="20" fill="#fff6ea"/>
<path d="M60 296H700" stroke="#c9a77f" stroke-width="10" stroke-linecap="round"/>
<path d="M240 178L270 140H490L520 178Z" fill="#b8323a" stroke="#5a1418" stroke-width="4" stroke-linejoin="round"/>
<rect x="240" y="178" width="280" height="112" rx="10" fill="#d9444d" stroke="#5a1418" stroke-width="4"/>
<path d="M340 140V120Q340 108 352 108H408Q420 108 420 120V140" fill="none" stroke="#5a1418" stroke-width="8"/>
<rect x="340" y="214" width="80" height="40" rx="8" fill="#fff" stroke="#5a1418" stroke-width="3"/>
<text x="380" y="241" text-anchor="middle" font-family="ui-monospace,monospace" font-size="20" font-weight="700" fill="#5a1418">0.0.5</text>
<g font-family="ui-monospace,monospace" font-size="17" font-weight="700" text-anchor="middle">
<g><rect x="60" y="40" width="150" height="44" rx="12" fill="#d7eaff" stroke="#3377b9" stroke-width="3"/><text x="135" y="68" fill="#173452">glob · grep</text><circle cx="232" cy="102" r="16" fill="none" stroke="#3377b9" stroke-width="5"/><path d="M244 114l14 14" stroke="#3377b9" stroke-width="6" stroke-linecap="round"/></g>
<g><rect x="60" y="120" width="140" height="44" rx="12" fill="#d9f5e4" stroke="#2f8f5b" stroke-width="3"/><text x="130" y="148" fill="#14432a">web_fetch</text><circle cx="222" cy="186" r="16" fill="#bfe9cf" stroke="#2f8f5b" stroke-width="3"/><path d="M206 186H238M222 170Q212 186 222 202Q232 186 222 170" fill="none" stroke="#2f8f5b" stroke-width="2.5"/></g>
<g><rect x="295" y="20" width="170" height="44" rx="12" fill="#fce9b6" stroke="#9a701b" stroke-width="3"/><text x="380" y="48" fill="#4a3608">todo_write</text><path d="M362 76l6 6 10-12M362 94l6 6 10-12" fill="none" stroke="#9a701b" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><path d="M386 78H404M386 96H404" stroke="#9a701b" stroke-width="4" stroke-linecap="round"/></g>
<g><rect x="560" y="40" width="140" height="44" rx="12" fill="#efe1ff" stroke="#7a4bb8" stroke-width="3"/><text x="630" y="68" fill="#341a5a">/undo</text><path d="M548 128Q520 128 520 104Q520 84 546 84" fill="none" stroke="#7a4bb8" stroke-width="5" stroke-linecap="round"/><path d="M538 74l12 10-12 10" fill="none" stroke="#7a4bb8" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></g>
<g><rect x="560" y="120" width="140" height="44" rx="12" fill="#ffe0e6" stroke="#b83a5a" stroke-width="3"/><text x="630" y="148" fill="#5a1426">AGENTS.md</text><path d="M528 172h20l8 8v26h-28z" fill="#fff" stroke="#b83a5a" stroke-width="3" stroke-linejoin="round"/></g>
<g><rect x="560" y="210" width="140" height="44" rx="12" fill="#e2e8f0" stroke="#4b617e" stroke-width="3"/><text x="630" y="238" fill="#173452">--json { }</text></g>
</g>
</svg>
<figcaption>AgentiLoop CLI 0.0.5: same loop, a lot more in the box.</figcaption>
</figure>

## AgentiLoop CLI 0.0.5: a bigger toolbox

When we [took the agent loop to the terminal](/blog/the-terminal-strikes-back/), the CLI started with five sharp tools: read, list, write, edit and bash. Version 0.0.4 taught it to stop cleanly. Version 0.0.5 is about giving it more to work with. All of it landed in Rust first and was mirrored commit for commit in Go, so both editions have exactly the same features.

### New tools

| Tool | What it does | Asks first? |
|---|---|---|
| `glob` | Finds files by pattern | No |
| `grep` | Searches file contents, with 0–5 lines of context | No |
| `web_fetch` | Fetches an http(s) page as text, with size caps | **Yes** |
| `todo_write` | Keeps a checklist for multi-step work (see it with `/todos`) | No |

`glob` and `grep` skip `.git`, `node_modules`, `target` and binary files, and they honor `.gitignore`, including nested files, negation, anchoring and directory-only rules. That makes them faster than shelling out to `find` and safer than dumping a whole tree into the context.

### It reads your project's instructions

If your repo has an **`AGENTS.md`** or **`CLAUDE.md`**, the CLI loads it into the system prompt, along with one in `~/.agentiloop` for your personal defaults. Lines like `@docs/style.md` import other files (nested and cycle-safe). No file yet? **`/init`** writes a starter `AGENTS.md` with the build and test commands it detects.

### Undo, diff and friends

- **`/undo`**: every change made by `write_file`, `edit_file` and `apply_patch` is journaled per prompt, so you can roll back the agent's last turn.
- **`/diff`** shows the git status and diff of the working tree.
- **`/export`** saves the conversation as Markdown.
- **`/usage`** shows token totals since start and how full the context is.

### Make it yours

- **Custom slash commands**: drop a Markdown file into `.agentiloop/commands/`, say `review.md` containing `Review $1 for bugs`, and `/review main.rs` runs it. `$ARGUMENTS` and `$1`..`$9` are supported, and `/commands` lists them.
- **MCP prompts** from your servers show up as `/mcp__<server>__<prompt>` commands.

### Built for scripts and CI

- **`--json`** prints a one-shot answer as a single JSON object: result, is_error, session_id, provider, model and usage.
- **`--allow-tool` / `--deny-tool`** set permission rules by tool name or `mcp_*` prefix. Deny always wins, even over `--yes`.
- **`--append-system-prompt`** adds text to the system prompt for one run.
- **Pipes just work**: a lone `-` in the prompt is replaced by stdin, so `git diff | agentiloop "review this" -` does what it says.

Put together, that's a CI step that reviews a pull request, refuses to touch the shell and returns machine-readable output:

```
git diff origin/main | agentiloop --deny-tool bash --json "review this diff" -
```

## Why ship them together?

Because they're the same idea in three shapes. Agent! for Mac is the flagship: it drives your apps, your Xcode builds and your whole desktop. The CLIs carry the same loop to every terminal on macOS, Windows and Linux. The CLI's Esc-to-cancel and the Mac app's Auto-Pilot with its Stop All button answer the same question from two sides: *how does a person stay in charge of a loop that runs on its own?*

That's the part we care about most. Not a cute avatar, not a bigger number on a benchmark, but the human in the loop: you set the goal, you see every step, and you can stop it. In the CLI, `/undo` also rolls back the agent's last file edits. Auto-Pilot has no undo, so run it in a project that's in git.

## Get them

- **Agent! 1.1.87 for Mac**: [download from GitHub](https://github.com/AgentiLoop/Agent/releases/tag/v1.1.87.287) or `brew update && brew install --cask agentiloop-agent`. macOS 14.6 or later, Apple Silicon or Intel.
- **AgentiLoop CLI 0.0.5 (Rust)**: [release on GitHub](https://github.com/AgentiLoop/AgentiLoopCLI/releases/tag/v0.0.5).
- **AgentiLoopGo 0.0.5 (Go)**: [release on GitHub](https://github.com/AgentiLoop/AgentiLoopGo/releases/tag/v0.0.5).

The macOS CLI binaries are signed and notarized. Unpack, put `agentiloop` on your PATH and run it; the setup wizard takes it from there.

Testers are very welcome. Try `/undo` after a big edit, point it at a repo with an `AGENTS.md`, or wire `--json` into a script, then tell us what broke. Please include your OS, provider and model, and never include API keys.
