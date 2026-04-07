---
title: Why We Ripped Out Coding Mode: Let the Model Pick Its Own Tools
description: Agent! used to guess whether you wanted coding or automation and hide tools to match. One broken Photo Booth task showed why the harness should stop second-guessing the model.
tags: Architecture, Design
---
Early versions of Agent! had **modes**: coding, automation and standard. The idea sounded reasonable. A coding task doesn't need the Accessibility tool, and a "click this button" task doesn't need Xcode. Hide what isn't relevant and the model sees a shorter tool list, spends fewer tokens and makes fewer wrong picks.

On April 7, 2026, commit `7ea44c0d` deleted the whole system. Here's the bug that did it, and the principle it left behind.

## How modes worked

On the second turn of a task, the harness looked at what you'd asked for and matched it against two keyword lists. Words like `build`, `compile`, `edit`, `fix` and `refactor` meant coding. Words like `click`, `button`, `window`, `photo` and `accessibility` meant automation. Then it flipped a flag, `codingModeEnabled` or `automationModeEnabled`, and narrowed the tools the model could see to that mode's groups. The model could also switch modes itself through a `mode` tool.

## The bug: Photo Booth in coding mode

The report was simply "accessibility is broken." The cause, in the commit message's own words: the auto-switch saw `open -a Photo Booth` as an unknown signal and **defaulted to coding mode**. Coding mode excluded the Auto group, and the Auto group is where the `accessibility` tool lives.

So the model was asked to take a photo, and the one tool built for pressing the shutter button had vanished mid-task. It did what a capable model does with the tools it has left: it fell back to `osascript` through the shell, which kept failing with *"Can't get toolbar 1 of window 1."*

Nothing was wrong with the model, and nothing was wrong with the accessibility tool. The harness had guessed wrong about intent and quietly taken away the right answer.

## The fix that wasn't

The obvious patch was to add `open -a` to the automation keywords. The commit message calls that out directly: it would have been "one more band-aid in a long line." Keyword intent detection is a losing game. Every new app, phrasing and language adds another hole, and every miss fails in the most confusing way possible, with a model that suddenly can't do something it could do one turn earlier.

## What replaced it: nothing

The whole mode system came out: 13 files, 141 lines deleted and 39 added. That included:

- the `codingModeEnabled` and `automationModeEnabled` flags and their tool-group lists
- the turn-2 auto-switch in both the main task loop and tab tasks
- `predictToolGroups()`, the function that guessed tool groups from your prompt
- the tool-list narrowing for local endpoints in the Claude and OpenAI-compatible services
- the `coding` and `automation` aliases for sub-agents (you pass real group names instead)

Tools are now filtered **only by your own toggles** in Settings (`ToolPreferencesService`). Every tool you've enabled is available on every turn, and the model picks what it needs.

Two small details show the care in a deletion like this. The `mode` tool wasn't removed outright. It became a no-op that replies *"mode switching has been removed"*, because a model with an old conversation in context might still call it, and a clear answer beats an unknown-tool error. And the system prompt revision went from 71 to 72, so any prompt saved on disk that mentioned modes gets re-synced.

## The result

No more *"Coding mode auto-enabled"* log spam. No more tools disappearing mid-task. No more tool list flapping from one turn to the next.

## The principle

This decision shaped a lot of what came after, so it's worth stating plainly:

> The harness should enforce **safety**, not guess **intent**.

Agent! is strict where strictness is objective. It refuses catastrophic shell commands, edits to files the model hasn't read, and "done" without evidence. Those are facts it can check. Which tool a task needs is a judgment call, and the model is better at that call than a keyword list. When the harness overrules the model on a judgment call, it fails silently and confusingly. When it enforces a checkable rule, it fails loudly and with a reason.

If you're building an agent, it's tempting to "help" the model by trimming its choices. Measure first. A slightly longer tool list costs a few tokens. A missing tool can cost you the whole task.
