---
title: Welcome to the Agent! Blog: One App, Any AI, Total Command Over Your Mac
description: What AgentiLoop Agent! is, why I built it the way I did, and what you'll find here, straight from the source code.
tags: Announcement, Architecture
---
<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 340" role="img" aria-labelledby="map-title map-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="map-title">A little Mac hands you the map</title>
<desc id="map-desc">A smiling Mac stands on a desk holding an unfolded map. The map has four stops connected by a dotted trail: Any AI, The Loop, AgentScript and Safety.</desc>
<rect width="760" height="340" rx="20" fill="#eef6ff"/>
<path d="M30 290H730" stroke="#8b684c" stroke-width="10" stroke-linecap="round"/>
<rect x="132" y="228" width="16" height="52" fill="#8a97a8"/><rect x="100" y="276" width="80" height="12" rx="4" fill="#8a97a8"/>
<rect x="40" y="100" width="200" height="130" rx="14" fill="#c9d3df" stroke="#173452" stroke-width="4"/>
<rect x="54" y="114" width="172" height="102" rx="6" fill="#559ef5"/>
<circle cx="110" cy="152" r="9" fill="#fff"/><circle cx="170" cy="152" r="9" fill="#fff"/>
<circle cx="112" cy="153" r="4" fill="#173452"/><circle cx="172" cy="153" r="4" fill="#173452"/>
<path d="M115 180Q140 198 165 180" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
<path d="M228 180Q262 176 290 160" fill="none" stroke="#173452" stroke-width="6" stroke-linecap="round"/>
<path d="M290 50L400 70L510 50L620 70V260L510 240L400 260L290 240Z" fill="#fff8e6" stroke="#8b684c" stroke-width="4" stroke-linejoin="round"/>
<path d="M400 70V260M510 50V240" stroke="#e6d6b3" stroke-width="3"/>
<path d="M350 175C380 140 410 140 440 140S490 190 520 190 560 130 580 110" fill="none" stroke="#d94877" stroke-width="4" stroke-dasharray="3 10" stroke-linecap="round"/>
<circle cx="350" cy="175" r="11" fill="#559ef5" stroke="#173452" stroke-width="3"/>
<circle cx="440" cy="140" r="11" fill="#7b6ad6" stroke="#173452" stroke-width="3"/>
<circle cx="520" cy="190" r="11" fill="#22c55e" stroke="#173452" stroke-width="3"/>
<circle cx="580" cy="110" r="11" fill="#f59e0b" stroke="#173452" stroke-width="3"/>
<g font-family="system-ui,sans-serif" text-anchor="middle" fill="#173452">
<text x="350" y="152" font-size="15" font-weight="700">Any AI</text>
<text x="440" y="117" font-size="15" font-weight="700">The Loop</text>
<text x="520" y="222" font-size="15" font-weight="700">AgentScript</text>
<text x="580" y="90" font-size="15" font-weight="700">Safety</text>
<text x="345" y="88" font-size="14" fill="#8b684c">Your map</text>
<text x="140" y="322" font-size="18">Agent! for Mac</text>
</g>
</svg>
<figcaption>Every blog needs a first post. This one is the map.</figcaption>
</figure>

Hi, I'm Todd. I build **AgentiLoop Agent!**, a native macOS AI agent, and this is its blog.

I wanted a place to explain the parts of Agent! that don't fit in a README or a release note. Why a guardrail is shaped the way it is. Why the agent loop checks its own work. What broke in a release candidate and how we fixed it. Most of what you'll read here comes straight from the codebase, because that's the thing I know best. Every so often I'll also look at the wider world of AI agents and what it means for your Mac.

If you're new, start here. Think of this post as the map.

## What Agent! is

Agent! is 100% native Swift and SwiftUI. You type (or say) what you want, and it actually does the work on your Mac instead of telling you how:

- **It writes real code.** It reads your project, edits files with string-replace diffs, builds in Xcode, reads the errors, fixes them, and commits with git.
- **It drives any Mac app** through the Accessibility API, plus AppleScript, JXA and 51 ScriptingBridge app bridges.
- **It runs shell commands as you or as root**, through a Launch Agent and a Launch Daemon registered with SMAppService and reached over XPC.
- **It works with 23 LLM providers**, plus on-device Apple Intelligence: Claude, Codex, OpenAI, Gemini, Grok, Mistral, DeepSeek, Qwen, Z.ai, OpenRouter, Ollama, vLLM, LM Studio and more.
- **It listens.** Say *"Agent!"* followed by a task, or text it from your iPhone over iMessage (approved senders only).

The README sums it up in four words: *Siri answers. Agent! acts.*

## No NPM, no Electron

This is the part that surprises people. There's no Electron shell. No Node runtime. No `node_modules` folder quietly eating your disk. I wrote every Swift package Agent! depends on, and each one lives in its own repo under the [AgentiLoop](https://github.com/AgentiLoop) org:

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

What you get is an app that sips RAM and still comes with Xcode automation, Swift syntax analysis, Accessibility, AppleScript, Safari automation and MCP right out of the box.

## The loop at the center

Everything in Agent! hangs off one idea: a **self-verifying task loop**. The model thinks, calls a tool, looks at the real result, and corrects itself. That only works if you can trust it, so a few rules are baked in:

- **Tools can't be faked.** Every call goes through a single dispatcher and returns real output. If the model says *"I clicked it"* without actually calling a tool, Agent! calls it out and sends a correction.
- **"Done" needs proof.** A task can't call itself finished until its `goal_state` criteria are checked off with evidence, like a green build or a passing test.
- **Read before you edit.** Agent! refuses to edit a file the model hasn't read, or one that changed on disk since it was read (checked with SHA-256). The refusal hands the model the fresh file, so the next try uses the right lines.
- **Everything can be undone.** Every edit is snapshotted for a week. Roll back one file, or rewind a whole task with `rewind_task`.

I'll take each of these apart in future posts.

## AgentScript: Swift with full permissions

AgentScript is one of my favorite pieces. Scripts are plain Swift files. Agent! compiles each one into a `.dylib` with SwiftPM and loads it in-process with `dlopen`, so your script gets the same macOS permissions Agent! already has: Accessibility, Automation, Calendar, Contacts, Mail, Photos and the rest. All you need is one entry point:

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

Agent! can run commands as root. That's a lot of trust to ask for, so safety can't just be a slide in a deck. It's code, and you can read it on GitHub. A hard-coded `ShellSafetyService` refuses catastrophic commands before they're ever sent, and the privileged daemon runs the same check again on its end. There's also an optional second opinion called **Jev** that rates how likely a command is to destroy data. The [first deep dive](/blog/inside-agent-shell-guardrails/) walks through exactly how that works.

## The family keeps growing

The same agent loop now runs in the terminal too, on macOS, Windows and Linux. There are two CLIs with the same capabilities: [AgentiLoopCLI](https://github.com/AgentiLoop/AgentiLoopCLI) in Rust and [AgentiLoopGo](https://github.com/AgentiLoop/AgentiLoopGo) in Go. My favorite fun fact from the README: Agent! for Mac wrote its own little siblings.

## What you'll find here

- **Internals:** the agent loop, context compaction, tool dispatch, sub-agents, memory and plans.
- **Security:** guardrails, the XPC trust model, and what recent agent incidents teach the rest of us.
- **Release notes with the why:** what changed in each build, and the bug that made it necessary.
- **How-tos:** AgentScript recipes, picking a provider on a budget, running fully local.
- **The wider agent world:** news and reviews, always brought back to what it means for your Mac.

Agent! runs on macOS 14.6 or later, on Apple Silicon and Intel, and it's free for personal use. Grab it below, give it something real to do, and let me know how it goes.
