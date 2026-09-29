---
title: Sonoma, Intel, and the Mac That Was Not Dead Yet
description: AgentiLoop Agent! welcomes macOS Sonoma 14.6 and later on Apple Silicon and Intel—a compatibility comeback for perfectly good Macs with absolutely no intention of retiring.
tags: Release Notes, Behind the Scenes
---
Somewhere, an Intel Mac heard the words “requires macOS 26,” closed its imaginary newspaper, and sighed.

“I have a keyboard,” it said. “I have a screen. I have processed approximately eleven billion browser tabs. And now I am apparently a decorative rectangle.”

Not so fast, you magnificent aluminum biscuit.

**AgentiLoop Agent! for Mac supports macOS Sonoma 14.6 and later, on both Apple Silicon and Intel.** The compatibility work landed on September 27, 2026, and this is our small, confetti-strewn celebration of opening the door wider.

Many of you have been waiting for a version that runs on **pre-macOS 26 systems**. This one's for you: the people with perfectly useful Macs, carefully maintained setups, and no desire to turn an operating-system upgrade into a weekend expedition.

## The velvet rope has been moved

Picture a tiny nightclub called The Agent Loop.

Inside: tools, tasks, and a very earnest computer trying to get something done. Outside: a bouncer checking operating-system versions with the gravity of someone guarding the crown jewels.

“macOS 26?”

“No. Sonoma.”

“I'm afraid—”

We have interrupted this conversation.

The new sign says **macOS 14.6 or later. Apple Silicon or Intel.**

That is the important bit. Not “every Mac ever manufactured.” Not “please excavate your PowerBook.” Your Mac still needs to run a supported operating system. But macOS 26 is no longer the ticket required to enter.

| Your Mac | The compatibility headline |
| --- | --- |
| Apple Silicon, running macOS 14.6 or later | Welcome aboard |
| Intel, running macOS 14.6 or later | Also welcome aboard |
| Running something older than macOS 14.6 | Still below the minimum requirement |

Two processor families. One much less exclusive guest list.

## This comeback has Git receipts

The whimsical explanation is that we asked the compatibility goblin to stop sitting on the door.

The actual explanation is more useful, and it is written in Git.

On **September 27, 2026**, commit **`ea5ce624`** put uses of Apple's FoundationModels framework behind macOS 26 availability checks. That included the model service, mediator, startup prewarming, and relevant compaction paths.

In human language: **check whether the newer facility is available before trying to use it.**

You would not cancel a dinner party because one guest's kitchen lacked a waffle iron. You would stop making the waffle iron a condition of admission.

Next came **`4d7fca86`**: updates to ten AgentiLoop packages whose releases declare macOS 14 support, plus a more specific macOS 26.4 availability check for a token-counting API.

That second detail matters. Compatibility is not simply changing one number and declaring yourself the mayor of Sonoma. The things your app depends on have to cooperate, too.

Then **`3a993205`** updated the documentation to say **Apple Silicon or Intel, macOS 14.6+**. The release-preparation checkpoint **`81079e2a`** records version **1.1.76, build 276**, with the application deployment target set to **14.6**.

No séance. No time machine. Availability checks, dependency updates, documentation, and a release checkpoint. Software engineering: occasionally less glamorous than the confetti suggests, considerably more useful.

## Your processor is not your personality

Apple Silicon users: you are invited.

Intel users: you are invited, too. You do not have to stand near the coats and pretend you only came to pick somebody up.

A computer that still does the work you need has not personally offended the future. Sometimes you keep an older system because it fits your workflow. Sometimes because changing it is inconvenient. Sometimes because the machine is already paid for, which is a remarkably persuasive technical specification.

This change makes Agent! available to a broader set of those Macs. It does **not** promise that every machine has identical performance or that every newer Apple feature exists on an older operating system.

That distinction deserves a proper sentence, not microscopic text hiding behind the plant.

## A wider welcome is not a magic wand

**Running Agent! and having access to every Apple Intelligence feature are different things.**

The compatibility work gates the FoundationModels paths; it does not transplant a macOS 26 framework into Sonoma. Nor does supporting Intel turn an Intel processor into Apple Silicon by sheer enthusiasm.

Your chosen model provider and its requirements still matter. So do the tools and permissions involved in a task. The operating-system minimum is an entry requirement, not a guarantee that every possible configuration can do every possible thing.

Think of it as opening the library to more readers. We have not promised that every reader's backpack contains a printing press.

If you want the nuts and bolts, our [engineering walkthrough](/blog/agent-now-runs-on-macos-14-6-and-intel/) follows the compatibility changes in more detail. This article is the welcome-back party. That one knows where the screws go.

## To everyone who was waiting

If you have been asking for Agent! without the macOS 26 requirement: **welcome in**.

If your Intel Mac has been patiently humming on the desk while newer machines got the invitations: pull up a chair.

If you are on Apple Silicon but prefer to stay on a supported earlier macOS release: you do not need to justify your life choices to a download button.

**AgentiLoop Agent! for Mac. macOS Sonoma 14.6 and later. Apple Silicon and Intel.**

More Macs at the table. Fewer perfectly good computers peering through the window.

The aluminum biscuit lives to agent another day.

## The receipts drawer

These are the September 27, 2026 commits behind this story—not claims about whichever release happens to be newest when you read it:

- [Gate FoundationModels usage for earlier macOS targets: `ea5ce624`](https://github.com/AgentiLoop/Agent/commit/ea5ce62493aef5ca74e694a8ec85b16621ec6388)
- [Update package requirements and token-count availability: `4d7fca86`](https://github.com/AgentiLoop/Agent/commit/4d7fca863a15d91d8e3734f991fabfcb90da734c)
- [Document Apple Silicon and Intel support: `3a993205`](https://github.com/AgentiLoop/Agent/commit/3a9932053630a21ec9df481c8f137cea30ff87a0)
- [Release-preparation checkpoint for 1.1.76: `81079e2a`](https://github.com/AgentiLoop/Agent/commit/81079e2a937f62d2d68389a3c124214f80cb3bc3)
