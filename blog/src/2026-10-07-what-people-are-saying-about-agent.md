---
title: What People Are Saying About Agent!, Six Months In
description: We read every review, thread and directory listing we could find about AgentiLoop Agent!, from the April Hacker News front page to French, Japanese, Korean, Russian and Chinese write-ups. Here is what they agree on, where they push back, and which of their facts have gone stale.
tags: Community, Reviews, Hacker News
---
Agent! has been public since March. Since then about two dozen people we've never met have written about it: in a Hacker News thread, on X and Threads, in directories that score open-source repos, and in long reviews in six languages. They're all linked from the [Reviews](/#reviews) section of the home page. This post is what you get if you read them all in one sitting, plus the GitHub numbers behind them.

We've tried to quote fairly, including the parts that sting. Where a review says something that is no longer true, we say so and link the change.

## The numbers first

The [AgentiLoop/Agent](https://github.com/AgentiLoop/Agent) repository has 640 stars and 69 forks today. The GitHub API will tell you when each star arrived, and the shape is not a smooth curve:

| Month | New stars |
|---|---|
| March 2026 | 9 |
| April 2026 | 374 |
| May 2026 | 55 |
| June 2026 | 60 |
| July 2026 | 40 |
| August 2026 | 43 |
| September 2026 | 56 |
| October 2026 (so far) | 3 |

More than half of all stars came in April, the month of the first Hacker News thread. Since then it's been a steady forty to sixty a month, which is roughly the rate at which the write-ups below kept appearing. On the releases page, the 1.1.87 disk image (the first with Auto-Pilot) has been downloaded 293 times in its first week.

## April: 83 points, 54 comments, and some hard questions

The first thread, [Agent — Native macOS coding IDE/harness](https://news.ycombinator.com/item?id=47787127), reached 83 points and 54 comments on April 16. Reading it again six months later, very little of it was about features. It was about trust, and nearly every complaint in it turned into a change.

**"Who is behind this?"** The project then lived under a GitHub account called `macOS26`, and the app was pitched at "macOS26.4+". Two commenters asked, in so many words, whether this was an official Apple account and whether the name was a phishing-training trap. Another said every commit appeared to come from a single faceless entity, so for a while they assumed there was no human involved at all. One reply put it plainly: open-source maintainers "don't owe anyone perfectly-manicured marketing copy", but the point landed. The project moved to the [AgentiLoop](https://github.com/AgentiLoop) organization and the agentiloop.ai domain, and the old domains now 301-redirect here.

**"Securely runs root-level commands via a dedicated macOS Launch Daemon. Lovely."** That one-word sarcasm was the most reasonable reaction in the thread. The answer then, and now, is that the Launch Daemon is optional, has to be approved by you in System Settings, and can be switched off along with its tools. What has changed since April is everything around it: a [shell guardrail layer](/blog/inside-agent-shell-guardrails/) with hard-blocked patterns, read-before-edit, a 10-minute hard timeout on every shell command (1.1.88), and the Jev risk advisor that refuses commands above a threshold.

**"So… what is a harness?"** The best sub-thread had nothing to do with Agent!. One answer described a harness as a while loop, some prompts and a regex to execute tool calls. Another added that the memory model is the hard part. A third said they wouldn't want an agent to remember past conversations at all, because current models repeat their own mistakes. All three are right, and that tension is still in the app: Agent! has memory, but scoped (global versus project), written deliberately through a tool, and readable as plain files. We wrote a longer answer later in [What Is an Agent Loop?](/blog/what-is-an-agent-loop/).

**"I'd use it with my Claude subscription, not an API key."** The top comment was about cost, not capability. That's why Claude and Codex OAuth arrived within days (issue [#4](https://github.com/AgentiLoop/Agent/issues/4)), and why it still matters: when Claude OAuth requests started failing this week with an "out of extra usage" error, it was the first bug filed against 1.1.88 and the first fix in 1.1.89.

There was also a comparison to Fazm, another Swift Mac agent focused on Claude. The difference people noticed then is the one reviewers still lead with: Agent! talks to many providers, local and cloud. It was 17 in April; it's 23 now.

## The reviews: three things everyone noticed

Reviewers didn't coordinate, wrote in different languages and picked different angles. Three observations come up again and again.

### 1. "Done" has to be earned

This is the most quoted idea by a distance. A Japanese article on X framed it as an agent's "done" being a claim, not a result, and said the interesting part of the README was "not the capability list" but the design that makes completion depend on `goal_state` evidence, an optional critic and rewind. [BestHub](https://www.besthub.dev/articles/this-600-star-swift-agent-lets-ai-operate-your-entire-mac-safely-f35faf6e6355) led with "Tasks cannot self-declare completion", and argued the next phase of the agent race is about "whose actions can be trusted". On X, Nathan Romano summed up the guardrails in a sentence: it can't say done without evidence, won't edit a file it hasn't read, keeps backups, blocks dangerous commands.

The idea was tested early by a GitHub issue. In April, a "mini audit" ([#2](https://github.com/AgentiLoop/Agent/issues/2)) asked what happens if a model *says* it ran a tool when no tool event happened. That turned out to be a real gap in the Apple Intelligence path at the time, and the fix was to check claims against actual tool results: the same principle reviewers now single out. The [next post](/blog/what-the-issue-tracker-taught-agent/) tells that story in full.

### 2. Accessibility, not screenshots

The French guide on [ForoKD](https://fr.forokd.com/Ma%C3%AEtriser-les-agents-d'IA-pour-macOS-Control-:-le-guide-ultime-de-l'automatisation-de-bureau/) put the main strength in one line: it uses the macOS Accessibility API, so it doesn't have to keep taking screenshots to find buttons. It also picked out AgentScript, Swift dylibs compiled on the fly for system actions. The Chinese profile on [diedong.com](https://www.diedong.com/macos26-agent.html) called it a "digital employee" that operates the Mac with real clicks and typing. The [A2Agent team](https://a2agent.me/blog/mac-agent-harness-agentiloop-en), comparing it with Codex and OpenClaw, said its positioning is "an agent that can drive your entire Mac, and happens to be very good at code", not the other way round.

That framing matters to us because it's the honest one. Agent! is a coding agent, and it builds its own website, a [Mario Kart-style game](/blog/gokart-built-on-auto-pilot/) and [a JavaScript port of another](/blog/mariokart64js-from-scratch-in-javascript/). But the reason to install a native Mac app rather than run a terminal tool is everything outside the editor.

### 3. Context compaction that leaves a way back

Two reviews, a Korean thread from [Daily AI Star](https://www.threads.com/@daily_ai_star/post/DcqU-01GXPv) and the [ISH field guide](https://blog.ish.chat/r/agentiloop-agent-1-1-1-recoverable-context-compaction), wrote about a feature most users never see: when Agent! trims old tool results from the context, it leaves a short preview and a way to restore them instead of a bare `[cleared]`. ISH's summary is better than ours: shortening context should not destroy the route back to evidence. Daily AI Star said the benchmark for coding-agent context is shifting from how much it can hold to how safely it can bring back what it removed. The full design is in [Context Compaction at Half the Window](/blog/context-compaction-half-the-window/), and it also started as a bug report, which you'll find in the next post.

## Where reviewers push back

Not everything was praise, and the criticism is useful.

[Hysen Labs](https://hysenlabs.com/en/projects/agentiloop-agent) wrote one of the most careful reviews and also the clearest "where it's the wrong tool" section: the platform constraint is absolute, it's Mac only, and building from source needs a paid Apple Developer team so the helpers register. [RepoRank](https://reporank.net/en/repo/agentiloop-agent.html) said to avoid it if you need broad OS coverage or want to minimize dependence on macOS-specific permissions. Both are fair. Agent! asks for Accessibility, Automation and helper approvals because those are the doors it opens, and it doesn't run on Windows or Linux.

What has changed since is worth stating precisely:

- **"Requires macOS 26.4."** Several profiles (Hysen Labs, RepoRank, FollowAgents) still say so. Since the September 27 pre-release, and in every stable release from 1.1.87 on, Agent! runs on **macOS 14.6 Sonoma or later, on Apple silicon and Intel**. [The port is its own story](/blog/sonoma-intel-and-the-mac-that-was-not-dead-yet/).
- **"18 / 21 providers."** Counts in reviews range from 17 to 21 depending on the month they were written. It's 23 in 1.1.87.
- **"Mac only."** Still true for the app. But there's now an AgentiLoop CLI in [Rust and Go](/blog/agent-1-1-87-and-agentiloop-cli-0-0-5/) that runs on Mac, Windows and Linux.
- **"You'll need to build it."** The release builds are signed and notarized, and `brew install --cask agentiloop-agent` works. Building from source is only for people who want to change it.

## October: a quieter Show HN

On October 3 Agent! went back to Hacker News as a Show HN about Auto-Pilot ([thread](https://news.ycombinator.com/item?id=49948810), and [our post about it](/blog/back-on-hacker-news-with-auto-pilot/)). As of this morning it has one point and no comments. That's the normal fate of most Show HN posts, and we'd rather report it than leave it out. The April thread happened because a few people were curious enough to be blunt. If you are, that's where to do it, or in the [issue tracker](https://github.com/AgentiLoop/Agent/issues), which as the next post shows is where most of the real changes started.

## What we take from all this

Read together, the reviews describe a product we'd want to use: native, careful about what "done" means, good at driving the Mac rather than just the editor. The criticism describes the cost of that: permissions, platform lock-in, and a project that for a while looked more like a bot than a person. We can't change the first two without changing what Agent! is. The third, we hope, is better.

Thank you to everyone who wrote, even the one-word replies. If you've written about Agent! and we missed you, open an issue and we'll add you to the Reviews section.
