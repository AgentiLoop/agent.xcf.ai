---
title: How Agent! Got Started: Three Days in March
description: Three years of spare parts, one missing loop, and 177 commits in under two days. The real origin of Agent!, straight from git.
tags: Origins, History
updated: 2026-09-30
---
<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 380" role="img" aria-labelledby="lego-title lego-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="lego-title">A friendly robot building a Mac out of toy bricks</title>
<desc id="lego-desc">A smiling blue robot holds a yellow brick over a half-built Mac screen made of red, yellow, green, blue and orange toy bricks. A speech bubble says: Almost done!</desc>
<rect width="760" height="380" rx="20" fill="#eef6ff"/>
<path d="M40 318H720" stroke="#8b684c" stroke-width="13" stroke-linecap="round"/>
<path d="M190 92l-6 26 40-26" fill="#fff"/>
<rect x="120" y="30" width="230" height="64" rx="22" fill="#fff" stroke="#b6c8e4" stroke-width="3"/>
<text x="235" y="72" text-anchor="middle" font-family="system-ui,sans-serif" font-size="26" font-weight="700" fill="#173452">Almost done!</text>
<path d="M140 270V310M210 270V310" stroke="#173452" stroke-width="7" stroke-linecap="round"/>
<path d="M250 200L318 146" stroke="#173452" stroke-width="7" stroke-linecap="round"/>
<rect x="100" y="150" width="150" height="120" rx="28" fill="#559ef5" stroke="#173452" stroke-width="4"/>
<path d="M175 150V124" stroke="#173452" stroke-width="5"/><circle cx="175" cy="115" r="10" fill="#efb943"/>
<circle cx="145" cy="192" r="13" fill="#fff"/><circle cx="205" cy="192" r="13" fill="#fff"/>
<circle cx="149" cy="193" r="5.5" fill="#173452"/><circle cx="209" cy="193" r="5.5" fill="#173452"/>
<path d="M148 228Q175 250 202 228" fill="none" stroke="#173452" stroke-width="6" stroke-linecap="round"/>
<g stroke="#173452" stroke-width="3">
<rect x="300" y="112" width="70" height="34" rx="4" fill="#efb943"/>
<rect x="311" y="102" width="16" height="10" rx="2" fill="#efb943"/><rect x="343" y="102" width="16" height="10" rx="2" fill="#efb943"/>
</g>
<g stroke="#173452" stroke-width="3">
<rect x="430" y="276" width="140" height="34" rx="4" fill="#9aa7b8"/>
<rect x="480" y="244" width="40" height="32" fill="#b8c3d1"/>
<rect x="400" y="210" width="70" height="34" rx="4" fill="#d94877"/>
<rect x="470" y="210" width="70" height="34" rx="4" fill="#4caf6e"/>
<rect x="540" y="210" width="70" height="34" rx="4" fill="#559ef5"/>
<rect x="610" y="210" width="70" height="34" rx="4" fill="#f08a3c"/>
<rect x="400" y="176" width="70" height="34" rx="4" fill="#efb943"/>
<rect x="470" y="176" width="70" height="34" rx="4" fill="#559ef5"/>
<rect x="540" y="176" width="70" height="34" rx="4" fill="#d94877"/>
<rect x="610" y="176" width="70" height="34" rx="4" fill="#4caf6e"/>
<rect x="400" y="142" width="70" height="34" rx="4" fill="#4caf6e"/>
<rect x="470" y="142" width="70" height="34" rx="4" fill="#f08a3c"/>
<rect x="540" y="142" width="70" height="34" rx="4" fill="#efb943"/>
<rect x="400" y="108" width="70" height="34" rx="4" fill="#559ef5"/>
<rect x="470" y="108" width="70" height="34" rx="4" fill="#d94877"/>
<rect x="540" y="108" width="70" height="34" rx="4" fill="#4caf6e"/>
<rect x="610" y="108" width="70" height="34" rx="4" fill="#efb943"/>
</g>
<rect x="610" y="142" width="70" height="34" rx="4" fill="none" stroke="#173452" stroke-width="3" stroke-dasharray="8 6"/>
<text x="190" y="354" text-anchor="middle" font-family="system-ui,sans-serif" font-size="21" fill="#173452">The builder.</text>
<text x="540" y="354" text-anchor="middle" font-family="system-ui,sans-serif" font-size="21" fill="#173452">The Mac. One brick to go.</text>
</svg>
<figcaption>Every big thing starts as a pile of little bricks. The trick is knowing which one goes next.</figcaption>
</figure>

Every app has a first day. Agent!'s first day was a Wednesday: **March 11, 2026, at 3:07 in the afternoon.** We know the minute because git wrote it down.

But the bricks were lying around long before that.

## Three years of spare parts

Before Agent! there were other apps. **ANIE.** **Game Changer.** **BattleScript.** The **XCF MCP Server and Client.** **D1F**, a tool for changing lots of lines in a file at once. And about eight Swift packages, all written by the same person.

Each one could do a piece of the job. Some could talk to an AI. Some could edit code. Some could poke at Xcode. None of them could do the most important thing: **keep going on their own.**

Think of a wind-up toy. You wind it, it walks three steps, it stops. Cute. Not helpful. What was missing was a loop: look at the problem, pick a tool, use it, check what happened, and go again until the job is done. (That loop has [its own post, with a robot and a sandwich](/blog/what-is-an-agent-loop/).)

Once the loop worked, the best of the old parts could snap onto it. That is the whole origin story in one sentence. The rest is details, and the details are fun.

## Day one: a brain, a helper, and a Cancel button

The very first real commit is called *"Autonomous Agent with privileged launch daemon."* It was 20 files and 1,765 lines of Swift. Here is what was in the box:

- A SwiftUI window where you type what you want.
- One AI brain, Claude, doing the thinking.
- A **Launch Daemon**: a small helper that runs in the background with the keys to the whole house, so the agent can do grown-up system chores.
- Task history, screenshots, and paste.

An hour later came the first crash fix (pasting a screenshot crashed it). Minutes after that, a big red **Cancel** button, bound to Escape. When you build something that acts on its own, the stop button comes early.

By 5:27 p.m. there was a second helper, a **Launch Agent**, which runs commands as *you* instead of as the all-powerful root. Asking for the master key to list a folder is like calling the fire department to light a candle. Six minutes after that, Agent! got its second brain: **Ollama**, so it could run on AI models that live on your own Mac.

Before the day was over it could also write and run Swift scripts, drive Xcode, see pictures on vision models, and show a splash screen. It also got little traffic-light status dots, which took about a dozen commits to settle on green, yellow and red. Some things are harder than an agent loop.

## Day two: "May I?"

March 12 is the day Agent! learned that a Mac is polite and very strict about it.

To control another app, like Music or Pages, macOS asks you first: *"Agent! wants to control Music. Allow?"* Getting that little window to actually show up took the whole evening. From about 8:20 to 9:40 p.m. the history is a pile of attempts, a few minutes apart: try it one way, try it on the main thread, open System Settings, try `osascript`, try asking for `every window`, try just `name`. Also: Keynote, Numbers and Pages had changed their bundle IDs, so it was knocking on doors with the wrong names.

It got there. The same night it learned to show images and web pages right inside its own log, so when it makes album art, you see the album art.

## Day three: a name and a version number

On the morning of March 13, the app got its name. The commit at 9:06 a.m. is *"rename app to Agent!"* Exclamation mark included, on purpose.

Twenty minutes later came a change that still matters today: scripts stopped being separate programs and became **dynamic libraries** that load right inside the app. That is why AgentScripts get the same Mac permissions Agent! has, without asking again.

Later that day it was tagged **1.0.0**. Counting from the first commit, that is **177 commits in less than two days.** Versions 1.0.1 through 1.0.16 followed in the next eight days.

One small detail: the author name on those early commits is not a person. It is **"Agent! for MacOS."**

## Growing up

After the first sprint, the story speeds up:

- **April 6.** Almost a month of history was squashed into one clean starting commit. The full history was kept in a backup.
- **April 7.** "Coding mode," "automation mode" and "standard mode" were [ripped out](/blog/why-we-ripped-out-modes/). One agent, all the tools, every time.
- **April.** Apple Intelligence was on board as a brain that runs right on the Mac, for free.
- **August 31.** The project moved from the `macOS26` GitHub organization to **AgentiLoop**, and the website became **agentiloop.ai**.
- **Lately.** Agent! learned to [run on macOS 14.6 and on Intel Macs](/blog/sonoma-intel-and-the-mac-that-was-not-dead-yet/), and it helped build its own terminal siblings, [AgentiLoopCLI](https://github.com/AgentiLoop/AgentiLoopCLI) in Rust and [AgentiLoopGo](https://github.com/AgentiLoop/AgentiLoopGo) in Go.

It started with one brain. Today it works with **23 AI providers**, plus Apple Intelligence. Since that April clean-up, the main branch has picked up more than 1,300 commits.

## Why it looks the way it does

Almost everything odd about Agent! goes back to those first three days.

It has two helpers, one for you and one for root, because day one needed both. It is 100% Swift, like the spare parts it was made from. It is built from original code, not a pile of 65 NPM packages. It drives other apps by name through Accessibility and AppleScript because day two was spent learning how to ask the Mac nicely. And it still has a big Cancel button.

Every big thing starts as a pile of little bricks. This one had been piling up for three years. On March 11, somebody finally found the brick that holds the others together: the loop.
