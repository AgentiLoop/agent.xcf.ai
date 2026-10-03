---
title: Back on Hacker News, Six Months Later, with Auto-Pilot
description: Agent! is on Hacker News again as a Show HN. The April thread was about a native Mac coding harness; this one is about Auto-Pilot, the goal-driven loop that keeps running cycles until the goal is reached, and the Mario Kart-style game it has been building. Here is the post, what is behind each claim in it, and where to join the discussion.
tags: Auto-Pilot, Community, Hacker News
---
Agent! is back on Hacker News today as a Show HN: [Show HN: AgentiLoop Agent Mac GUI Agent Loop for macOS 14.6 or Later](https://news.ycombinator.com/item?id=49948810). If you have a Hacker News account, that thread is the place to ask questions, poke holes, and tell us what you'd want from a Mac agent. This post is the longer version of the submission text, with a pointer to the source of every claim in it.

## The source material

The submission is short, so here it is in full, quoted from [the Hacker News item](https://news.ycombinator.com/item?id=49948810):

> Agent! originally appeared on Hacker News last April. A lot has changed since there. Recently a new feature has been developed called Auto-Pilot. It is given a goal and will not stop until the goal is reached. Think of it as tasks on steroids. What Agent does is create multi tasks. Each task is referred to as a Cycle. By default Auto-Pilot triggered by auto [goal] do not have a time frame. Agent! is told to keep running until its goal is reached. Auto-Pilot has a kill switch, a "Stop All" button. The user can also kill the current Cycle only using auto stop and can also kill all using auto stop all. In November a user will be able to have Multiple Auto-Pilots running on the same project. And an Auto-Pilot tab will be able to automatically spawn other tabs. Currently we are developing a Mario Kart like clone called "GoKart" written in GoDot 4. So far over 20 hours have been recorded developing and improving the game.

Everything below expands on one sentence of that.

## "Agent! originally appeared on Hacker News last April"

The first thread was [Agent — Native macOS coding IDE/harness](https://news.ycombinator.com/item?id=47787127) on April 16, 2026: 83 points and 54 comments. The app then required macOS 26.4 and Apple silicon, had 17 LLM providers, and was pitched mostly as a coding harness that could also drive Mac apps through the Accessibility API. Both threads are listed in the [Reviews](/#reviews) section of this site, alongside the independent write-ups that came in between.

Since April: macOS 14.6 and Intel support ([the story of that port](/blog/sonoma-intel-and-the-mac-that-was-not-dead-yet/)), 23 providers, [context compaction you can recover from](/blog/context-compaction-half-the-window/), a [Rust and Go CLI](/blog/agent-1-1-87-and-agentiloop-cli-0-0-5/) for Mac, Windows and Linux, a release on the first of every month, and the feature the new submission is actually about.

## "It is given a goal and will not stop until the goal is reached"

Auto-Pilot is the `/auto` command in Agent! for Mac. From the README's Auto-pilot section: it runs the task loop in unattended cycles, on the main tab or any LLM tab, until a goal is reached, a time budget runs out, or you press Stop. There is no cycle limit and no per-cycle iteration cap. When a cycle's task ends and the goal isn't reached, the next cycle starts automatically.

| Command | What it does |
|---|---|
| `/auto <goal>` | Work toward the goal until the LLM reports it reached |
| `/auto 4h <goal>` | Same, but stop after 4 hours (`30m`, `1.5h` also work) |
| `/auto` | Review the project first, then ask you for the goal |
| `/auto history`, `/auto last`, `/auto #N` | List previous goals, restart the most recent or the Nth |
| `/auto status` / `/auto stop` | Show the session, or end it after the current cycle |

"Think of it as tasks on steroids" is the right mental model. Each cycle *is* a normal Agent! task, with the same tools, the same guardrails (read-before-edit, goal_state evidence, shell blocklist) and the same `done()` contract. What Auto-Pilot adds is the loop around it: the cycle's summary is appended to `.agent/autopilot/progress.md` inside the project and fed into the next cycle's prompt, so each cycle starts by reading what the previous ones did, assumed and left undone. The session only ends when the LLM begins its final summary with `AUTOPILOT: GOAL REACHED`. Cycles that end with no summary at all, from errors or cancellations, never end the session; the next cycle just waits longer, 15 seconds, then 30, then 60, up to five minutes.

"By default … do not have a time frame" is literal: `/auto <goal>` without a duration runs until the goal is reached or you stop it. If you want a ceiling, `/auto 4h <goal>` gives you one. Active sessions also survive app restarts. Quitting, or a crash, pauses them, and on the next launch each one resumes on its tab with the next cycle.

## "Auto-Pilot has a kill switch"

Three ways to stop, and they do different things:

- **Stop All** (the button) ends every Auto-Pilot session on every tab and stops all running tasks. In `RunStop.swift` the comment is explicit: a single-task stop, Esc or the stop button, keeps Auto-Pilot running; Stop All ends it.
- **`/auto stop`** ends the session after the current cycle finishes, or immediately if you're between cycles. The current cycle is allowed to land.
- **`/auto stop all`** (also `stopall` or `stop-all`) is the same as pressing Stop All, for people who'd rather not reach for the mouse. It's handled in `AutoPilot.swift` right before `/auto stop`.

The submission describes `auto stop` as killing "the current Cycle only". The more precise version is that it ends the *session* after the current cycle; the cycle itself runs to its natural end, which is what keeps the progress log and the git history clean.

## "In November … Multiple Auto-Pilots running on the same project"

This is the part of the submission that's a roadmap item rather than a shipped feature, and it's worth being clear about which is which. As of today the main branch of the Agent repo has a commit titled *Auto-Pilot: multiple tabs per project — per-tab progress, shared registry, auto/forced git worktree isolation, shared memory from worktrees*. That's the groundwork: each tab keeps its own progress log, the tabs register with each other, and when two Auto-Pilots would otherwise edit the same files they get separate git worktrees. It is not in a release yet; it landed after the 1.1.87 tag. Releases ship on the first of the month, so the November 1 release is the earliest it can reach you, and the "tab that spawns other tabs" part is, per the submission, planned for the same window.

## "A Mario Kart like clone called GoKart"

GoKart is the project Auto-Pilot has spent most of its life on. The [earlier post](/blog/gokart-built-on-auto-pilot/) covers the first afternoon in detail, straight from the progress log: Godot 4 installed by cycle 1, custom arcade physics chosen over `VehicleBody3D` so the handling could be unit-tested, drift sparks and boost blur by cycle 2, a track by cycle 3, items by cycle 4, a stall on a stray tab character, a Stop All, and a second session that put a `perl -e 'alarm'` time limit on every shell run and then shipped fifteen features in a row.

It hasn't stopped. The [GoKart repository](https://github.com/AgentiLoop/GoKart) went from its first commit at 12:39 on October 1 to 71 commits by the evening of October 3. The recent commits read like a Mario Kart 64 checklist: Toad's Turnpike-style traffic on Sunset Speedway, Moo Moo Farm-style Monty Moles on Green Hills, a title screen with a live attract demo, a results board, and a drawn item window on the HUD. Each one lands with its own test file and a `tools/*_check.gd` script, because the model still can't see the screen and has to prove a feature is there some other way. The "over 20 hours" in the submission is the wall-clock total of those sessions. [GoKart 0.0.1](https://github.com/AgentiLoop/GoKart/releases/tag/v0.0.1) is downloadable for macOS, Windows and Linux if you'd rather play it than read about it.

## What to ask on the thread

If you're coming from Hacker News, the questions we'd most like to answer there:

- How Auto-Pilot decides a goal is reached, and why we let the model say so rather than a fixed metric.
- What happens when a cycle goes wrong, and why git is the real undo.
- Whether an unattended loop on your Mac is a good idea at all, and what the guardrails do about it.

The thread is at [news.ycombinator.com/item?id=49948810](https://news.ycombinator.com/item?id=49948810). Agent! 1.1.87 with Auto-Pilot is on the [releases page](https://github.com/AgentiLoop/Agent/releases/latest) and in Homebrew: `brew install --cask agentiloop-agent`.
