AGENTILOOP AGENT! PRESS KIT
Updated September 8, 2026

PRESS CONTACT
Todd Bruss
agent@agentiloop.ai

FACT SHEET
App: AgentiLoop Agent! (shown as "Agent!" in the menu bar and in Finder)
What it is: AgentiLoop Agent! is the Mac app that puts an AI to work on the desktop: type what should happen, pick a provider, and the agent reads, writes, builds, clicks, and scripts until the job is finished. Open source under the MIT License.
Price: Free. Users bring their own API key for cloud providers or run local models at no cost. A PayPal donation is requested.
Platform: Mac with Apple Silicon; macOS 26.4 or later. English.
Distribution: Direct download from GitHub Releases as a DMG or ZIP, signed with an Apple Developer ID and notarized by Apple. Not on the Mac App Store.
Public launch: April 12, 2026
Latest release: 1.1.9 (build 205), September 2, 2026
Developer: Todd Bruss, Logos InkPen LLC - Charlotte, North Carolina, USA
Developer contact: agent@agentiloop.ai | X: https://x.com/SuperBox64 | LinkedIn: https://www.linkedin.com/in/agentiloop-agent/
Download: https://github.com/AgentiLoop/Agent/releases/latest
Website: https://agentiloop.ai
Source: https://github.com/AgentiLoop/Agent
Press kit: https://agentiloop.ai/press/

ONE SENTENCE
A free, open-source macOS autonomous agent powered by 21 LLMs that writes code, controls apps, runs shell commands, and automates workflows from plain English.

ONE PARAGRAPH
AgentiLoop Agent! is a native macOS app that turns any large language model into an autonomous agent for the whole Mac, not just a code editor. Written entirely in Swift 6.2 and SwiftUI with no Electron, no Node.js packages, and no telemetry, it runs a self-verifying loop: plan, call a tool, observe the real result, correct course, and repeat until the task's goal criteria are met with evidence. It builds Xcode projects, drives other apps through the Accessibility API, AppleScript, JavaScript for Automation, and 51 ScriptingBridge bridges, runs shell commands as the user or as root through helpers the user approves once, and extends through MCP servers, Swift scripts compiled at runtime, sub-agents, voice, and iMessage. It works with 21 providers, from Claude, OpenAI, and Gemini to local Ollama, vLLM, and LM Studio, plus on-device Apple Intelligence. It is free and open source under the MIT License; users bring their own API key.

DEVELOPER QUOTE
"I set out to build a Cursor killer. Somewhere along the way I realized what I really wanted was to automate the Mac itself, so the agent could drive any app through Accessibility and AppleScript instead of only editing files in an editor. AgentiLoop Agent! is the result: one native app that takes any AI and puts it to work on the whole desktop." - Todd Bruss, Developer

KEY FEATURES
- Self-verifying task loop: a task cannot be marked complete until its goal criteria are verified with evidence; an opt-in critic reviews the diff first.
- Agentic coding with native Xcode integration: reads codebases, edits with string-replace diffs, builds and runs Xcode projects with clickable errors, manages git, and indexes repositories into a portable JSONL repo map.
- Desktop automation through the Accessibility API, plus AppleScript, JavaScript for Automation, and 51 ScriptingBridge app bridges.
- AgentScript: the agent writes Swift files, compiles them to dynamic libraries, and loads them in-process with the app's own permissions.
- Every file edit is snapshotted first, with one-click rollback, undo, or whole-task rewind.
- 21 LLM providers with a fallback chain: Claude, Codex, OpenAI, Google Gemini, Grok, Mistral, Codestral, Mistral Vibe, DeepSeek, Hugging Face, MiniMax, Z.ai, BigModel, Qwen, OpenRouter, Requesty, Ollama cloud, local Ollama, vLLM, LM Studio, and on-device Apple Intelligence.
- Apple Intelligence as an on-device agent: local triage, task summaries, plain-English error translation, next-step suggestions, and context compression at no token cost.
- Privileged execution the user approves once: a Launch Agent for user-level shell commands and an optional Launch Daemon for root, registered with SMAppService and connected over XPC.
- Defense in depth: a shell safety service enforced on both client and daemon, same-team code-signing checks on both XPC listeners, a read-before-edit gate, and a Console audit trail of every tool call. See docs/SECURITY.md in the repository.
- MCP servers and sub-agents: any Model Context Protocol server can be added in Settings; up to three concurrent sub-agents (six read-only) run in isolation with per-agent model overrides.
- Voice and iMessage remote control: say "Agent!" followed by a task, or text a task from an iPhone and get the result back over iMessage.
- Tabs, memory, plans, and skills, with context compaction sized to each model's real context window.

DEVELOPER
Todd Bruss is a software engineer in Charlotte, North Carolina, and the founder of Logos InkPen LLC. He has shipped software for Apple platforms for more than fifteen years: his StarPlayr software-defined radio player was trademarked in 2009, and his later work includes StarPlayrX, a SiriusXM player for macOS built for visually impaired listeners; Logos InkPen, a vector drawing app for macOS; the XCF Xcode MCP server; and SuperBox64, a line of handmade arcade controllers and Raspberry Pi retro consoles. He works on the Identity team at Iru. AgentiLoop Agent! grew out of three years of building agentic AI apps, and the ten Agent-prefixed Swift packages it is built on are his own work.
X: https://x.com/SuperBox64
LinkedIn: https://www.linkedin.com/in/agentiloop-agent/
GitHub: https://github.com/AgentiLoop

CONTENTS
Screenshots contains six full-resolution PNG captures of the AgentiLoop Agent! window on macOS 26, cropped to the window with transparent rounded corners, showing real tasks from the developer's own projects. Captures from earlier versions show the project's previous GitHub organization name, macOS26.
Promo contains two 1920x1080 PNG banners for hero images and social cards.
Brand contains the app icon at 1024, 512, and 256 pixels as transparent PNGs, rendered exactly as macOS 26 draws it. Please use it unmodified: no recoloring, cropping, or added effects.

AgentiLoop Agent! is free and open source (MIT License): https://github.com/AgentiLoop/Agent
(c) 2026 Logos InkPen LLC. The AgentiLoop Agent! name and logo are trademarks of Logos InkPen LLC.
