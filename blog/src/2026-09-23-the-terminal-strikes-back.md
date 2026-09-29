---
title: The Terminal Strikes Back: Taking the Agent Loop Cross-Platform in Rust and Go
description: Agent! is a Mac app, but a coding agent belongs wherever developers work. Here's how the agent loop became two CLIs, one in Rust and one in Go, with a full-screen TUI on macOS, Windows and Linux.
tags: Announcement, Cross-Platform, Engineering
---
For most of its life, Agent! has been a proud Mac app: native Swift and SwiftUI, deep AppleScript and Accessibility hooks, and a Launch Daemon for root. That's still the flagship. But over the last few days something changed in how we think about coding agents, and today it ships.

**The agent loop now runs in your terminal, on macOS, Windows and Linux.** It comes in two editions with the same capabilities: [AgentiLoopCLI](https://github.com/AgentiLoop/AgentiLoopCLI) in Rust and [AgentiLoopGo](https://github.com/AgentiLoop/AgentiLoopGo) in Go. And yes, Agent! for Mac wrote much of its own little siblings.

## The paradigm shift: back to the terminal

The first wave of AI coding tools lived inside editors and chat windows. The wave that's winning lives in the **terminal**. There are good reasons for that:

- **The terminal is already where the work happens.** Builds, tests, git, package managers and SSH sessions all live there. An agent in the terminal doesn't need an integration for each; it has `bash`.
- **It goes anywhere.** A CLI runs on a Linux build box, inside a container, over SSH on a Raspberry Pi, or in a Windows dev VM. A Mac app runs on a Mac.
- **It composes.** One-shot mode (`agentiloop "explain this project"`) drops straight into scripts and CI.
- **It's honest about what it does.** Every tool call, diff and permission prompt scrolls by in plain text.

The Mac app's superpowers, like driving Photo Booth through Accessibility or scripting Mail with ScriptingBridge, are genuinely Mac-only. The **agent loop** isn't. Reason, call a tool, read the real result, correct, and repeat: that works on any OS with a shell and a filesystem. So we pulled the loop out.

## Why two languages?

We could have picked one. Instead we ported the same design twice, on purpose.

**Rust (AgentiLoopCLI)** was first. The workspace was scaffolded on September 20 with a core loop, the Anthropic provider, built-in tools and the CLI. It's split into five crates: `agentiloop-core` (the loop, messages, sessions and permissions), `agentiloop-provider`, `agentiloop-tools`, `agentiloop-mcp` and `agentiloop-cli`. It runs on `tokio`, uses `reqwest` with `rustls` so there's no OpenSSL to wrangle on Windows, and draws its TUI with `ratatui`. Markdown goes through `pulldown-cmark`, and code gets syntax highlighting from `syntect`.

**Go (AgentiLoopGo)** landed today in a burst of commits: the core (messages, agent loop, compaction, sessions and permissions) with tests, then the providers, then the MCP client, then the CLI with its REPL, TUI, Markdown, syntax highlighting, sessions and slash commands. It draws the TUI with `tcell`, renders Markdown with `goldmark`, highlights with `chroma`, and handles line editing with `liner`. Its release workflow targets the same five platforms as the Rust edition.

Doing it twice is the best design review there is. Anything that was really a Rust-ism or a Go-ism shows up immediately, and what's left is the actual architecture. There's also a practical benefit: pick the toolchain your team already trusts. Then tell us which one does it better. 🦀 vs 🐹

## The same loop, smaller surface

Both CLIs deliberately start with a small, sharp toolset:

| Tool | What it does | Asks first? |
|---|---|---|
| `read_file` | Reads a file with line numbers | No |
| `list_dir` | Lists a folder | No |
| `write_file` | Creates or overwrites a file | **Yes** |
| `edit_file` | Replaces an exact piece of text | **Yes** |
| `bash` | Runs a command (`sh -c` on Mac and Linux, `cmd /C` on Windows) | **Yes** |

Want more? Both editions include an MCP client ported from Agent!'s own AgentMCP, supporting stdio, Streamable HTTP and legacy HTTP+SSE, so any MCP server's tools plug straight in.

Permissions are part of the core, not bolted onto the UI. In Rust, a `PermissionPolicy` trait decides whether each call may run, based on the tool name, whether it mutates, and its input. The answer is `Allow`, `Deny` or `Cancel`. That third option exists because of a real annoyance: pressing **Esc** at a permission prompt should skip *that one call*, not end the whole task. The CLI supplies an interactive policy, and tests and CI use `AllowAll`.

## Cross-platform is in the details

"Runs on Windows" is easy to claim and hard to mean. A few things it took:

- **Killing a runaway command for real.** When `bash` times out, killing the shell isn't enough if the shell spawned children. The Go edition kills the whole process tree: a process group on Unix, and `taskkill /T` on Windows. The code is split into `proc_unix.go` and `proc_windows.go`.
- **CI on all three OSes.** The Go repo runs CI on macOS, Linux and Windows, and the Rust release workflow builds five binaries: macOS arm64 and x86_64, Linux x86_64 and arm64, and Windows x86_64.
- **Signed Mac binaries.** The release workflow can sign and notarize the macOS builds, so Gatekeeper doesn't block them.
- **No config-file archaeology.** The CLI remembers how you launched it: provider, model, TUI mode and session. After the first run, a bare `agentiloop` picks up exactly where you left off.

## A TUI that feels like an app

There are three ways to run it: the full-screen **TUI** (`agentiloop --tui`), a line-by-line **chat** mode for simple terminals, and **one-shot** for scripts. The TUI has had a busy few days:

- an animated busy indicator in the prompt box, with a spinner, the current activity and the elapsed time
- tokens-per-second tracking
- clickable links
- prompt history that persists between launches
- resumed sessions that show the previous conversation, so you're not staring at a blank screen
- `/model` backed by the provider's live model list

And when an API key is missing or wrong, it says so in plain words and names the real provider, instead of dumping a 401.

## Providers

On day one it works with Claude (API key or Claude Code OAuth token in the same credential, with the auth scheme auto-detected), OpenAI and any OpenAI-compatible server, local models through Ollama or LM Studio, and **oMLX** on Apple Silicon. It reads oMLX's address and key from `~/.omlx/settings.json` automatically.

## Try the release

Today we cut **v0.0.4**, a full release. It's early and moving fast, and we want your feedback now, while it's cheap to change. Grab a binary from the [Rust releases](https://github.com/AgentiLoop/AgentiLoopCLI/releases), or build the Go edition from [source](https://github.com/AgentiLoop/AgentiLoopGo).

The Mac app isn't going anywhere. If you're on a Mac, Agent! still does things no terminal can. But if you've ever wanted the same agent on the Linux server, the Windows laptop and the Raspberry Pi, it's here.
