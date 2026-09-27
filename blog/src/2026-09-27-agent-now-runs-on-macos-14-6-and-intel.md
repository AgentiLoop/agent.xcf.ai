---
title: Agent! Now Runs on macOS 14.6 and Intel Macs: How We Got Off macOS 26
description: Agent! was built around Apple Intelligence on macOS 26. Here's how one day of #available gates and package bumps brought it to macOS 14.6 on Apple Silicon and Intel.
tags: Release Notes, Engineering
---
Until today, Agent! required macOS 26. As of today's pre-release it runs on **macOS 14.6 or later, on Apple Silicon and Intel**. That covers a lot of perfectly good Macs that were locked out, many of which can't run Apple Intelligence at all.

Here's what it took, commit by commit, in one day.

## The blocker: FoundationModels

Agent! uses Apple's on-device model through the **FoundationModels** framework, which only exists on macOS 26. It isn't the main brain, since your chosen provider handles that. But it does several jobs: fast summaries during context compaction, on-device token counting, a prewarmed session at launch, and some triage.

Code that names a macOS 26 type won't build for an older deployment target. So step one (`ea5ce624`) was to put **every** use of FoundationModels behind `#available(macOS 26, *)`. That covered `FoundationModelService`, `AppleIntelligenceMediator`, the prewarm in `AgentApp`, compaction summaries and token counting in `Compression.swift`, and `AboutSelf`.

## The trick: type-erase the stored property

`#available` works for code paths, but not for a stored property. A class can't hold a `LanguageModelSession?` when the type doesn't exist on the running OS. The fix is to store it as `AnyObject?` and cast it back where it's used, inside gated code:

```swift
/// Type-erased `LanguageModelSession` so the stored property compiles below macOS 26.
private(set) var session: AnyObject?

@available(macOS 26.0, *)
var transcript: Transcript? {
    (session as? LanguageModelSession)?.transcript
}
```

As the commit message puts it, the stored properties no longer "drag the framework type into the class layout."

Availability checks also got an honest answer for older systems:

```swift
static var unavailabilityReason: String {
    guard #available(macOS 26.0, *) else { return "Apple Intelligence requires macOS 26 or later." }
    ...
}
```

So on macOS 14 or 15, Apple Intelligence just shows as unavailable with a clear reason, and everything else works. On macOS 26, nothing changes.

## The long tail: ten packages

Agent! is built from its own Swift packages, and each one declared its own minimum OS. Commit `4d7fca86` bumped all ten to releases that declare `.macOS(.v14)`:

| Package | Version |
|---|---|
| AgentAccess | 2.10.24 |
| AgentAudit | 1.3.9 |
| AgentColorSyntax | 1.2.8 |
| AgentD1F | 1.0.15 |
| AgentEventBridges | 1.1.8 |
| AgentLLM | 1.0.8 |
| AgentMCP | 1.6.10 |
| AgentSwift | 1.1.11 |
| AgentTerminalNeo | 1.37.9 |
| AgentTools | 2.53.19 |

Owning every dependency pays off on days like this. There was no waiting on an upstream maintainer, just ten tags.

## The surprise: 26.4

One API needed more than a 26.0 gate. `SystemLanguageModel.tokenCount(for:)` only exists from **macOS 26.4**, so its availability check moved from 26.0 to 26.4. Without that, a Mac on 26.0 through 26.3 would have tried to call a method that doesn't exist yet. It's a good reminder that "the framework is available" and "this method is available" aren't the same question.

## What you get on older Macs

On macOS 14.6 and 15, on Apple Silicon or Intel, Agent! works the same way:

- all 23 cloud and local LLM providers
- the full tool loop: coding, Xcode builds, git, shell as you or as root, Accessibility, AppleScript, JXA, AgentScript, Safari automation and MCP
- context compaction, which uses the model's own summaries and the provider's token counts, just without the Apple Intelligence tier

Only the on-device Apple Intelligence features need macOS 26.

## Get it

Every release and pre-release ships a signed, notarized and stapled binary. You never need to build from source:

```sh
brew update && brew install --cask agentiloop-agent
```

Or download the `.dmg` from [GitHub Releases](https://github.com/AgentiLoop/Agent/releases). If you've been waiting on an older MacBook or an Intel Mac mini, today's the day.
