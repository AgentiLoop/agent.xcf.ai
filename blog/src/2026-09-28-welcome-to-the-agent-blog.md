---
title: Welcome to the Agent! Blog: One App, Any AI, Total Command Over Your Mac
description: What AgentiLoop Agent! is, how it's built, and what this daily blog will cover, straight from the source code.
tags: Announcement, Architecture
---
This is the official blog for **AgentiLoop Agent!**, the native macOS AI agent. The plan is simple: one post a day, written mostly from the thing we know best, the codebase itself. Expect deep dives into how the agent loop works, why a guardrail is shaped the way it is, what changed in the latest release candidate, and the occasional look at the wider world of AI agents.

If you are new here, this first post is the map.

## What Agent! is

Agent! is a 100% native Swift / SwiftUI app. You type (or say) what you want, and it does the work on your Mac instead of just describing it:

- **It codes for real.** It reads your project, edits files with string-replace diffs, builds in Xcode, reads the errors, fixes them, and commits with git.
- **It drives any Mac app** through the Accessibility API, plus AppleScript, JXA and 51 ScriptingBridge app bridges.
- **It runs shell commands as you or as root**, through a Launch Agent and a Launch Daemon registered with SMAppService and reached over XPC.
- **It talks to 23 LLM providers** plus on-device Apple Intelligence: Claude, Codex, OpenAI, Gemini, Grok, Mistral, DeepSeek, Qwen, Z.ai, OpenRouter, Ollama, vLLM, LM Studio and more.
- **It listens.** Say *"Agent!"* followed by a task, or text it from your iPhone over iMessage (approved senders only).

The README puts it in one line: *Siri answers. Agent! acts.*

## No NPM, no Electron

The part that surprises people most is what Agent! *doesn't* ship. There's no Electron shell, no Node runtime and no `node_modules`. Every Swift package it depends on was written by the same author, and each one lives in its own repo under the [AgentiLoop](https://github.com/AgentiLoop) org:

| Package | Job |
|---|---|
| AgentTools | Tool schemas, system prompts and provider management |
| AgentLLM | LLM provider protocols, types and registry |
| AgentMCP | MCP client (stdio and HTTP) |
| AgentAccess | Accessibility automation |
| AgentEventBridges | ScriptingBridge protocols for 50+ Mac apps |
| AgentD1F | Multi-line diff engine |
| AgentSwift | SwiftSyntax code analysis |
| AgentColorSyntax · AgentTerminalNeo | Syntax highlighting · retro terminal markdown |
| AgentAudit | `os.log` audit logging |

The result is an app that uses very little RAM and gets Xcode automation, Swift syntax analysis, Accessibility, AppleScript, Safari automation and MCP out of the box.

## The loop at the center

Everything hangs off one idea: a **self-verifying task loop**. The model reasons, calls a tool, sees the real result, and corrects itself. A few rules make that loop trustworthy:

- **Tools can't be faked.** Every call flows through a single dispatcher and returns real output. If the model claims *"I clicked it"* without a tool call, Agent! injects a correction.
- **"Done" needs evidence.** A task can't declare itself finished until its `goal_state` criteria are marked done with proof, such as a green build or a passing test.
- **You read before you edit.** Edits to a file the model hasn't read, or one that changed on disk since it was read (checked with SHA-256), are refused. The refusal reads the file for the model so the next attempt uses fresh lines.
- **Everything is reversible.** Every edit is snapshotted for a week. You can roll back one file, or rewind a whole task with `rewind_task`.

We'll take each of these apart in future posts.

## AgentScript: Swift with full permissions

One of the most distinctive pieces is **AgentScript**. Scripts are plain Swift files. Agent! compiles each one to a `.dylib` with SwiftPM and loads it in-process with `dlopen`, so the script inherits Agent!'s own macOS permissions: Accessibility, Automation, Calendar, Contacts, Mail, Photos and so on. Writing one takes a single entry point:

```swift
import Foundation
import CalendarBridge   // any `import XBridge` auto-wires, no Package.swift edits

@_cdecl("script_main")
public func scriptMain() -> Int32 {
    print("Hello from AgentScript! 👋")
    return 0
}
```

Whatever the script prints goes back to the model, and the return value is the exit status. About 35 examples ship with the app, including `TodayEvents`, `NowPlaying`, `CheckMail` and `CreateDmg`.

## Safety you can read

Agent! can run as root, so safety isn't a slide in a deck. It's code you can open on GitHub. A hard-coded `ShellSafetyService` refuses catastrophic commands before they're dispatched, and the privileged daemon runs the same check again on its side. An optional second opinion called **Jev** rates how likely a command is to destroy data. Our [first deep dive](/blog/inside-agent-shell-guardrails/) covers exactly how that works.

## The family keeps growing

The same agent loop now also runs in the terminal on macOS, Windows and Linux, as two CLIs with the same capabilities: [AgentiLoopCLI](https://github.com/AgentiLoop/AgentiLoopCLI) in Rust and [AgentiLoopGo](https://github.com/AgentiLoop/AgentiLoopGo) in Go. Fun fact from the README: Agent! for Mac wrote its own little siblings.

## What to expect here

- **Internals:** the agent loop, context compaction, tool dispatch, sub-agents, memory and plans.
- **Security:** guardrails, the XPC trust model, and what recent agent incidents teach builders.
- **Release notes with the why:** what changed in each build, and the bug that caused it.
- **How-tos:** AgentScript recipes, picking a provider on a budget, running fully local.
- **The wider agent world:** news and reviews, always tied back to what it means for your Mac.

Agent! runs on macOS 14.6 or later, on Apple Silicon and Intel, and it's free for personal use. Grab it below, then come back tomorrow.
