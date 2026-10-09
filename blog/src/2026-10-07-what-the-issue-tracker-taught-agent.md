---
title: What the Issue Tracker Taught Agent!
description: Sixty-seven issues, a dozen outside pull requests and three releases in a week. Here is what people have said about Agent! where it counts most, in GitHub issues, and what each report changed in the app, from an LLM-written security review in March to a Claude OAuth break this week.
tags: Community, GitHub, Releases
---
The [previous post](/blog/what-people-are-saying-about-agent/) rounded up what reviewers and Hacker News say about Agent!. This one is about the people who said something more useful: they opened an [issue](https://github.com/AgentiLoop/Agent/issues). There are 67 numbers in the tracker today (issues and pull requests share them), and almost every one that came from outside the project changed something you can point to in the app.

Below is the tracker read in order, with what each report taught us. Every number links to the thread, so you can check the details.

## March: a security review written by Gemini (#1)

The first issue ever filed, [#1](https://github.com/AgentiLoop/Agent/issues/1), arrived on March 31. A reader had asked Gemini to do an initial security review of the code and posted the output, with an unusually fair framing: it was an LLM-generated review, not a formal audit, and readers should do their own research. Their own instinct was that the findings reflected an early-stage project rather than a deliberate trojan, but they warned that the way the repo was organized could set off remote-access-trojan alarms.

That's a hard first issue to receive, and an easy one to get defensive about. Some of the findings did misread the architecture, and the reply said so point by point. Others were right. Logging moved to OSLog in a new AgentAudit package (1.0.13), and Apple Event Query, an experimental path the review flagged, was turned off by default and slated for removal, since AppleScript and AgentScript already did the job better.

**What it taught us:** an app that runs shell commands, drives other apps and has an optional root helper will be judged as a security product first. That's the right default. It's why there is now a [post about the shell guardrails](/blog/inside-agent-shell-guardrails/) and why least privilege appears in every explanation of the helpers.

## April: "Did that tool actually run?" (#2)

[#2](https://github.com/AgentiLoop/Agent/issues/2) was titled *Mini audit: possible false-action-claim gap*. It proposed a simple test. Tell the assistant to answer `ACTION_NOT_PERFORMED` if no real tool event happens, then check whether it claims success anyway. The suggested mitigation: gate every user-visible completion claim on actual tool receipts from the host.

It found something. At the time Agent! was testing Apple Intelligence as a fast local helper for simple tasks, and it could believe it had completed a tool call that never ran. The fix showed its tool calls and forwarded failures to the main model you'd chosen, and the follow-up was to check that the main LLM path didn't do the same. Today, `done` can't be accepted until each `goal_state` criterion is marked with evidence from a tool result, which is the feature reviewers quote most. It's also why the system prompt Agent! runs under tells the model to say "action not performed" rather than describe a result it didn't get.

**What it taught us:** the most dangerous thing an agent says isn't a wrong answer, it's a confident report of work that didn't happen.

## April: OAuth, OpenRouter, and the price of a token (#3, #4)

Right after the first Hacker News thread, two requests landed back to back: OpenRouter support ([#3](https://github.com/AgentiLoop/Agent/issues/3)) and OAuth for Claude, Codex and Gemini ([#4](https://github.com/AgentiLoop/Agent/issues/4)). The OAuth thread got a second voice quickly: many people use agent harnesses through a Claude or OpenAI plan because paying API prices for every prompt adds up. Preliminary Claude and Codex OAuth shipped within days.

That decision has a cost that showed up this week. [#67](https://github.com/AgentiLoop/Agent/issues/67), filed against 1.1.88 on macOS 27, reports that Claude OAuth requests started failing with an "out of extra usage" error even with usage to spare. Pre-release [1.1.89](https://github.com/AgentiLoop/Agent/releases/tag/v1.1.89.289) changed how OAuth requests identify themselves (a Claude Code client profile and a billing-context block), and also made a new tab clear every provider's Retry-After backoff, so one rate-limited provider doesn't freeze the next attempt.

**What it taught us:** supporting the way people actually pay for models matters more than supporting the newest model. It also means you inherit someone else's API changes.

## May and June: the bugs only real Macs find (#20, #22, #23, #24)

These four came from people running Agent! on setups we didn't have, and each one is specific enough to be a small lesson in macOS.

- **[#20](https://github.com/AgentiLoop/Agent/issues/20): a Mac mini with no microphone.** Pressing Start Dictation crashed the app, because a Mac mini has no audio input unless something is plugged in. The reporter included a working fix that checked for a physical default input and filtered out virtual devices. It shipped in the next release.
- **[#22](https://github.com/AgentiLoop/Agent/issues/22): DeepSeek's thinking mode.** The first call worked, tools ran, then the follow-up call failed with a 400 because DeepSeek requires the model's `reasoning_content` to be passed back. The first fix didn't hold. The reporter came back with a log from the next build showing the same error, and the issue was only closed after they confirmed it worked. That's the standard: fixed means the reporter says it's fixed.
- **[#23](https://github.com/AgentiLoop/Agent/issues/23): System Settings panes that hide their controls.** On macOS 26.5.1, the Apple Intelligence mediator tried to open a Settings pane, found it, and then found nothing inside: the Catalyst-based panes don't expose their toggles to the Accessibility API. The report suggested four fixes, including reading the setting directly instead of clicking. The outcome was simpler: Accessibility was taken away from the Apple Intelligence mediator and left to the main LLM, which has better tools to work around a pane like that.
- **[#24](https://github.com/AgentiLoop/Agent/issues/24): Ollama on another machine.** A common setup is a big box running Ollama on the LAN or over Tailscale and a laptop running the agent. App Transport Security blocked plain HTTP to anything but localhost, and the only workaround was re-patching `Info.plist` with `plutil` after every update. The report suggested the narrowest fix, `NSAllowsLocalNetworking`, and that's exactly what shipped.

**What they taught us:** local models and odd hardware are not edge cases for a Mac agent. A lot of the people who care most about Agent! are the ones running Ollama in a closet.

## August: compaction that ate the task (#37)

[#37](https://github.com/AgentiLoop/Agent/issues/37), *Overagressive compaction crippling actions*, is our favorite bug report. The reporter had been productive for months, then after two updates their model (Qwen in LM Studio) would read four source files, compact the earlier ones away, and start again, never finishing. They found the number in the log, a threshold of 17,600 tokens, and asked where it came from.

The first suggestion, turning off Apple AI compaction, didn't help, and they said so. The fix in 1.0.99 did. They retested the same task with the same model and wrote back that there were no more indecision loops, but that they'd wait a day to be sure. That exchange is where [recoverable compaction](/blog/context-compaction-half-the-window/) comes from: if you have to drop context, leave a preview and a way back. Two independent reviews later singled that change out. In 1.1.87 compaction thresholds are sized from the model actually in use, and fetched Ollama context windows persist, which fixed a separate 16K threshold.

**What it taught us:** the best bug reports contain a number. Also: let the reporter close the issue.

## September: contributors, not just reporters

In late August a set of "good first issue" tickets went up: unit tests for an untested service ([#28](https://github.com/AgentiLoop/Agent/issues/28)), a Homebrew cask ([#29](https://github.com/AgentiLoop/Agent/issues/29)), an FAQ ([#30](https://github.com/AgentiLoop/Agent/issues/30)), README translations ([#31](https://github.com/AgentiLoop/Agent/issues/31)), a build troubleshooting section ([#32](https://github.com/AgentiLoop/Agent/issues/32)). They all got closed, and most by people outside the project. GitHub lists seven contributors besides the AgentiLoop account. Their merged pull requests include:

- `FallbackChainService` tests ([#43](https://github.com/AgentiLoop/Agent/pull/43)) and a single home for `ToolErrorClassifier` tests ([#40](https://github.com/AgentiLoop/Agent/pull/40))
- The build-from-source Troubleshooting section ([#41](https://github.com/AgentiLoop/Agent/pull/41)) and the FAQ's Setup & Providers section ([#38](https://github.com/AgentiLoop/Agent/pull/38))
- READMEs in four more languages ([#39](https://github.com/AgentiLoop/Agent/pull/39))
- New providers and tools: Requesty ([#49](https://github.com/AgentiLoop/Agent/pull/49)), Exa search ([#19](https://github.com/AgentiLoop/Agent/pull/19)), a Parallel Search MCP preset ([#26](https://github.com/AgentiLoop/Agent/pull/26)) and MiniMax M3 as a default ([#21](https://github.com/AgentiLoop/Agent/pull/21))

Even the pull requests that weren't merged pointed at something real: [#63](https://github.com/AgentiLoop/Agent/pull/63) caught a wrong Homebrew install command in the translated READMEs, tracked and closed as [#62](https://github.com/AgentiLoop/Agent/issues/62).

Provider teams started showing up too. OrcaRouter ([#48](https://github.com/AgentiLoop/Agent/issues/48)) and A2Agent ([#47](https://github.com/AgentiLoop/Agent/issues/47)) asked for integrations, and both shipped in 1.1.87. The A2Agent team later wrote one of the reviews in the previous post. A MemCode proposal to back Agent!'s memory with their service ([#65](https://github.com/AgentiLoop/Agent/issues/65)) is open now, and would most naturally start through the existing MCP client.

## October: three releases in a week

The issues that are open today are mostly the project talking to itself in public: [#64](https://github.com/AgentiLoop/Agent/issues/64) announced Auto-Pilot before it shipped, [#66](https://github.com/AgentiLoop/Agent/issues/66) proposed [the face](/blog/agent-gets-a-face/). Both are now in the releases:

| Release | Date | What changed | DMG downloads |
|---|---|---|---|
| [1.1.87](https://github.com/AgentiLoop/Agent/releases/tag/v1.1.87.287) | Oct 1 | `/auto` Auto-Pilot, six new providers including Sidrune AI, an enforced critic gate, Jev, compaction sized to the model | 293 |
| [1.1.88](https://github.com/AgentiLoop/Agent/releases/tag/v1.1.88.288) (pre) | Oct 4 | Avatar tabs with a talking face, several Auto-Pilot tabs per project with git worktree isolation, a hard timeout on every shell command | 3 |
| [1.1.89](https://github.com/AgentiLoop/Agent/releases/tag/v1.1.89.289) (pre) | Oct 5 | Claude OAuth fix (#67), an in-process shell hang fixed when an orphaned background job held the pipe open | 5 |

Those download numbers are worth being honest about. Almost everyone takes the stable release; pre-releases are tested by a handful of people. If you're one of them, the most useful thing you can do is the thing the people in this post did: open an issue with your macOS version, provider, model and the log, and stay until it's fixed.

The shell changes in both pre-releases rhyme with a lesson Auto-Pilot wrote down for itself in its own progress log rather than on GitHub: after [the first GoKart session](/blog/gokart-built-on-auto-pilot/) stalled and had to be stopped, the second session put a time limit on every shell run. An unattended loop can't afford a command that never returns, so now neither can the app.

## The pattern

Read top to bottom, the tracker tells a consistent story. The issues that changed Agent! the most weren't feature requests. They were someone saying *this didn't do what it said it did*: a tool call that didn't run, a compaction that undid the work, a fix that wasn't fixed yet. Those are the reports the whole design is now built around.

If you've got one, the [new-issue form](https://github.com/AgentiLoop/Agent/issues/new/choose) asks for exactly what helps: Agent! version, macOS version, install method, provider and model, and the activity log. Please never paste API keys.
