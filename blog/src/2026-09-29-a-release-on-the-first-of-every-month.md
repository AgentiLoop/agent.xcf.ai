---
title: A Release on the First of Every Month, and Pre-Releases in Between
description: Agent! now ships a stable release on the 1st of every month. Daily pre-releases (moving to weekly) are where new features and fixes get tried out, and release candidates lock things down before the big day.
tags: Release Notes, Behind the Scenes
---
Agent! has a new rhythm. Starting **October 1, 2026**, there's a stable release on the **1st of every month**. In between, there are pre-releases: right now about one a day, and we plan to slow that to one a week. Somewhere in the last stretch of each month the pre-releases become **release candidates**, and the best candidate becomes the release on the 1st.

That's the whole plan. The rest of this post is how we got here, with some charts from our own git history.

## Where we've been

Agent! 1.0.0 was tagged on **March 13, 2026**. Since then the repository has picked up **188 version tags**. They didn't arrive evenly.

<figure class="chart"><div class="chart-title">Version tags per month, 2026</div><div class="bars"><div class="lbl">Mar</div><div><div class="bar" style="--w:0.738"><span>57</span></div></div><div class="lbl">Apr</div><div><div class="bar" style="--w:0.880"><span>68</span></div></div><div class="lbl">May</div><div><div class="bar dim" style="width:3.9%"><span>3</span></div></div><div class="lbl">Jun</div><div><div class="bar dim" style="width:3.9%"><span>3</span></div></div><div class="lbl">Jul</div><div><div class="bar dim" style="width:1.3%"><span>1</span></div></div><div class="lbl">Aug</div><div><div class="bar" style="--w:0.194"><span>15</span></div></div><div class="lbl">Sep</div><div><div class="bar" style="--w:0.531"><span>41</span></div></div></div><figcaption>188 tags since 1.0.0 on March 13. Busy spring, quiet summer, and a September comeback. Source: <code>git for-each-ref refs/tags</code>.</figcaption></figure>

March and April were a sprint: 125 tags in two months, sometimes several a day. Then summer happened. May, June and July added seven tags between them. In late August the pace picked up again, and September has 41 tags so far.

Stable releases followed the same bumpy road. The Releases page lists four of them: **1.0.80.170** on April 25, **1.0.88.182** on June 3, **1.0.89.183** on July 26 and **1.1.33.233** on September 12, the 600-star release.

<figure class="chart"><div class="chart-title">Days between stable releases</div><div class="bars"><div class="lbl">1.0.88</div><div><div class="bar" style="--w:0.648"><span>39 days · Apr 25 → Jun 3</span></div></div><div class="lbl">1.0.89</div><div><div class="bar" style="--w:0.880"><span>53 days · Jun 3 → Jul 26</span></div></div><div class="lbl">1.1.33</div><div><div class="bar" style="--w:0.797"><span>48 days · Jul 26 → Sep 12</span></div></div><div class="lbl">Oct 1</div><div><div class="bar next" style="--w:0.315"><span>19 days · Sep 12 → Oct 1</span></div></div></div><figcaption>Each stable release on GitHub, measured from the one before it. The striped bar is the October 1 release, already on the calendar. From there, the gap is one month, every month.</figcaption></figure>

Gaps of 39, 53 and 48 days aren't bad, but you couldn't set your watch by them. If you wanted to know when the next Agent! was coming, the honest answer was "when it's ready." We like ready. We also like knowing when.

## The road to October 1

The new cycle has already had its dress rehearsal. After 1.1.33 shipped, `main` kept moving. From v1.1.37.237 on September 13 to v1.1.77.277 on September 28, every tag was a pre-release build, and on most days there was at least one.

<figure class="chart"><div class="chart-title">Tags per day, September 13–28</div><div class="cols"><div style="height:10.6%"><span>1</span></div><div style="height:10.6%"><span>1</span></div><div style="height:10.6%"><span>1</span></div><div style="height:42.5%"><span>4</span></div><div style="height:0.0%"><span></span></div><div style="height:53.1%"><span>5</span></div><div style="height:10.6%"><span>1</span></div><div style="height:10.6%"><span>1</span></div><div style="height:31.9%"><span>3</span></div><div style="height:21.2%"><span>2</span></div><div style="height:10.6%"><span>1</span></div><div style="height:21.2%"><span>2</span></div><div style="height:85.0%"><span>8</span></div><div class="rc" style="height:42.5%"><span>4</span></div><div class="rc" style="height:42.5%"><span>4</span></div><div class="rc" style="height:10.6%"><span>1</span></div></div><div class="cols-x"><span>13</span><span>14</span><span>15</span><span>16</span><span>17</span><span>18</span><span>19</span><span>20</span><span>21</span><span>22</span><span>23</span><span>24</span><span>25</span><span>26</span><span>27</span><span>28</span></div><div class="legend"><span><i></i>pre-release builds</span><span><i class="rc"></i>RC season (RC1 on the 26th → RC6 on the 28th)</span></div><figcaption>39 tags in 16 days. September 25 alone shipped eight builds, v1.1.61 through v1.1.68.</figcaption></figure>

On September 26 the builds changed their name. **v1.1.72.272 became Release Candidate 1**, with a new headline in its release notes: *Formal Release Date Oct. 1, 2026.* RC2 through RC5 followed on September 27, and RC6 (v1.1.77.277) went up today. Each RC's notes ask testers to report regressions against the v1.1.33.233 stable release, so everyone compares against the same baseline.

The RCs weren't just a relabel. They carried real fixes:

- **RC1** pinned every `Agent*` package in `Package.resolved` to its latest tag, so fixes like AgentTools 2.53.18 actually make it into the build.
- **RC6** got critic review working again with newer Claude models, fixed context-overflow and max_tokens detection across providers, and made the compaction threshold follow the model you're actually using. (That last one has [its own blog post](/blog/context-compaction-half-the-window/).)

Every pre-release goes through the same Release workflow as a stable release: it builds, notarizes and staples the `.zip` and `.dmg`. A pre-release isn't a rough cut. It's a finished build with less mileage.

## How a month works now

| When | What ships | What it's for |
|---|---|---|
| The 1st | Stable release | The one we recommend to everyone. Homebrew and the Latest badge point here. |
| Most days (moving to weekly) | Pre-release | New features, experiments and bug fixes, out early for anyone who wants them. |
| Last stretch of the month | Release candidates | Features freeze. Fixes only, until one RC is boring in the best way. |
| The next 1st | Stable release | The best RC, promoted. Then the loop starts again. |

<figure class="chart"><div class="chart-title">One month, two rhythms</div><div class="month"><span class="lbl">Now</span><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="rc"></b><b class="rc"></b><b class="rc"></b><b class="rc"></b><b class="rc"></b><b class="rc"></b><b class="gold"></b></div><div class="month"><span class="lbl">Soon</span><b></b><b></b><b></b><b></b><b></b><b class="p"></b><b></b><b></b><b></b><b></b><b></b><b></b><b class="p"></b><b></b><b></b><b></b><b></b><b></b><b></b><b class="p"></b><b></b><b></b><b></b><b></b><b class="rc"></b><b></b><b></b><b class="rc"></b><b></b><b></b><b class="gold"></b></div><div class="legend"><span><i></i>pre-release</span><span><i class="rc"></i>release candidate</span><span><i style="background:#22c55e"></i>stable release on the 1st</span></div><figcaption>An illustration, not a schedule: the month runs left to right and ends on the 1st. Today there is a pre-release most days. Soon, one a week.</figcaption></figure>

**Pre-releases are the lab.** It's where we try new things. Some ideas land in a pre-release, get used for real, and get better within a day or two. Some turn out to be a bad idea, and it's much nicer to learn that from a pre-release than from the stable build. Bug fixes land here first too, so if something bothers you, the fix usually shows up in a pre-release within days.

**Release candidates are the calm before the 1st.** The goal of each cycle is simple: reach a stable RC before the release date, then ship it. The RC series for October went from RC1 to RC6 in three days, and every one of them was about fixes, not features.

**The 1st is for everyone.** If you just want a solid Agent! that updates once a month, stay on stable and you're done.

## Why weekly, eventually

A pre-release every day is great for momentum and for us. It's a lot to keep up with if you're a tester. Once the monthly cycle is settled, pre-releases will move to **once a week**. That gives each build a few days of real use before the next one arrives, and it makes each pre-release's notes worth reading from top to bottom.

We'll announce the switch here and in the release notes when it happens.

## How to follow along

- **Stable:** `brew update && brew install --cask agentiloop-agent`, or grab the build marked *Latest* on the [Releases page](https://github.com/AgentiLoop/Agent/releases).
- **Pre-releases and RCs:** they're on the same [Releases page](https://github.com/AgentiLoop/Agent/releases), marked *Pre-release*. Install one, use it for real work, and tell us what broke.
- **Found a regression?** Open an issue with your macOS version, provider and model, and the relevant activity-log output. Please leave out your API keys.

Put **October 1** on your calendar, then November 1, then December 1. See you on the first.
