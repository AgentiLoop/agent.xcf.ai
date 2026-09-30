---
title: Sonoma, Intel, and the Mac That Was Not Dead Yet
description: Agent! for Mac now runs on macOS Sonoma 14.6 and later, on Apple Silicon and Intel. A lot of you asked for a pre-macOS 26 version. Here it is.
tags: Release Notes, Behind the Scenes
---
<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 340" role="img" aria-labelledby="macs-title macs-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="macs-title">Two happy Macs and a new sign</title>
<desc id="macs-desc">An Intel Mac and an Apple Silicon Mac sit on a desk, both smiling. Between them, a sign has "macOS 26 only" crossed out, replaced by "macOS 14.6+, Apple Silicon and Intel."</desc>
<rect width="760" height="340" rx="20" fill="#eef6ff"/>
<rect x="182" y="215" width="16" height="50" fill="#8a97a8"/><rect x="150" y="263" width="80" height="12" rx="4" fill="#8a97a8"/>
<rect x="562" y="215" width="16" height="50" fill="#8a97a8"/><rect x="530" y="263" width="80" height="12" rx="4" fill="#8a97a8"/>
<rect x="374" y="170" width="12" height="105" fill="#8b684c"/>
<path d="M30 280H730" stroke="#8b684c" stroke-width="10" stroke-linecap="round"/>
<rect x="90" y="100" width="200" height="125" rx="14" fill="#c9d3df" stroke="#173452" stroke-width="4"/>
<rect x="104" y="114" width="172" height="97" rx="6" fill="#559ef5"/>
<circle cx="160" cy="150" r="9" fill="#fff"/><circle cx="220" cy="150" r="9" fill="#fff"/>
<circle cx="162" cy="151" r="4" fill="#173452"/><circle cx="222" cy="151" r="4" fill="#173452"/>
<path d="M165 178Q190 196 215 178" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
<rect x="470" y="100" width="200" height="125" rx="14" fill="#e7e2f7" stroke="#173452" stroke-width="4"/>
<rect x="484" y="114" width="172" height="97" rx="6" fill="#7b6ad6"/>
<circle cx="540" cy="150" r="9" fill="#fff"/><circle cx="600" cy="150" r="9" fill="#fff"/>
<circle cx="542" cy="151" r="4" fill="#173452"/><circle cx="602" cy="151" r="4" fill="#173452"/>
<path d="M545 178Q570 196 595 178" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
<rect x="303" y="60" width="154" height="115" rx="10" fill="#fff" stroke="#8b684c" stroke-width="4"/>
<g font-family="system-ui,sans-serif" text-anchor="middle" fill="#173452">
<text x="380" y="88" font-size="16" fill="#8a97a8">macOS 26 only</text>
<text x="380" y="118" font-size="19" font-weight="700">macOS 14.6+</text>
<text x="380" y="141" font-size="16">Apple Silicon</text>
<text x="380" y="162" font-size="16">and Intel</text>
<text x="190" y="315" font-size="20">Intel Mac</text>
<text x="570" y="315" font-size="20">Apple Silicon Mac</text>
</g>
<path d="M318 83H442" stroke="#d94877" stroke-width="3" stroke-linecap="round"/>
</svg>
<figcaption>Same desk. Same Macs. New sign.</figcaption>
</figure>

Let's be honest. When Agent! said "requires macOS 26," a lot of good Macs got left out.

If you're on Sonoma, you were out of luck. If you're on Sequoia, same thing. And if you're on an Intel Mac, you weren't even in the conversation.

That always bugged me. Those Macs still work. People use them every day. They write code on them, run their businesses on them, and keep way too many browser tabs open on them. They didn't do anything wrong. They just weren't on the newest OS.

Not anymore. **Agent! for Mac now runs on macOS Sonoma 14.6 and later, on Apple Silicon and on Intel.**

Many of you have been waiting for a pre-macOS 26 version. This one's for you.

## Why it was 26-only in the first place

Agent! uses Apple's on-device model through a framework called FoundationModels. It isn't the main brain. Whatever provider you pick does the heavy lifting. But the on-device model helps with smaller jobs, like summarizing during context compaction, counting tokens, and warming up a session when the app launches.

Here's the catch. FoundationModels only exists on macOS 26. If your code even mentions one of its types, it won't build for an older Mac. The compiler just says no.

So the easy path was to require macOS 26 and move on. Easy for me, anyway. Not so great for everybody else.

And honestly, it was a little silly. The on-device model is a helper. It's nice to have. It was never the reason Agent! works. Locking out every older Mac over a helper is like refusing to cook dinner because you're out of parsley.

## So how do you fix that?

You ask first. Before Agent! touches the on-device model, it checks: am I on macOS 26? If yes, great, use it. If no, that code just doesn't run, and your provider keeps doing the real work.

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 300" role="img" aria-labelledby="fork-title fork-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="fork-title">Ask before you use it</title>
<desc id="fork-desc">A flow chart. Agent! wants the on-device model. It asks: is this macOS 26? Yes leads to using the on-device helpers. No leads to skipping them while the provider keeps working.</desc>
<defs><marker id="fork-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0 0L10 5 0 10Z" fill="#4b617e"/></marker></defs>
<rect width="760" height="300" rx="20" fill="#f0f5fb"/>
<g fill="none" stroke="#4b617e" stroke-width="4"><path d="M380 90V113" marker-end="url(#fork-arrow)"/><path d="M320 150H170V206" marker-end="url(#fork-arrow)"/><path d="M440 150H590V206" marker-end="url(#fork-arrow)"/></g>
<rect x="230" y="30" width="300" height="60" rx="18" fill="#d7eaff" stroke="#3377b9" stroke-width="3"/>
<path d="M380 115L440 150 380 185 320 150Z" fill="#fce9b6" stroke="#9a701b" stroke-width="3"/>
<rect x="40" y="210" width="260" height="66" rx="18" fill="#cff3e4" stroke="#29836a" stroke-width="3"/>
<rect x="460" y="210" width="260" height="66" rx="18" fill="#dfd9ff" stroke="#7760b5" stroke-width="3"/>
<g font-family="system-ui,sans-serif" text-anchor="middle" fill="#173452">
<text x="380" y="67" font-size="19" font-weight="700">Want the on-device model?</text>
<text x="380" y="156" font-size="16" font-weight="700">macOS 26?</text>
<text x="245" y="140" font-size="17">Yes</text>
<text x="515" y="140" font-size="17">No</text>
<text x="170" y="238" font-size="18" font-weight="700">Use it.</text>
<text x="170" y="262" font-size="15">Summaries, token counts</text>
<text x="590" y="238" font-size="18" font-weight="700">Skip it.</text>
<text x="590" y="262" font-size="15">Your provider keeps working</text>
</g>
</svg>
<figcaption>That's the whole trick. Ask before you use it.</figcaption>
</figure>

There's one more wrinkle. Swift won't let a class hold a property whose type doesn't exist on the running OS. So the session gets stored as a plain `AnyObject` and cast back only inside the macOS 26 code. Not pretty. Works great.

## The commits

It all happened on September 27, 2026. Four commits, one day, and it's all in Git.

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 260" role="img" aria-labelledby="day-title day-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="day-title">September 27, 2026, commit by commit</title>
<desc id="day-desc">A timeline from noon to 8 PM. Commit ea5ce624 at 12:46 PM, 4d7fca86 at 12:57 PM, 3a993205 at 7:14 PM, and 81079e2a at 7:32 PM.</desc>
<rect width="760" height="260" rx="20" fill="#f0f5fb"/>
<g stroke="#4b617e" stroke-width="2"><path d="M121 104V130M136 130V148M639 104V130M663 130V148"/></g>
<path d="M60 130H700" stroke="#4b617e" stroke-width="4" stroke-linecap="round"/>
<g fill="#227657" stroke="#fff" stroke-width="3"><circle cx="121" cy="130" r="8"/><circle cx="136" cy="130" r="8"/><circle cx="639" cy="130" r="8"/><circle cx="663" cy="130" r="8"/></g>
<g font-family="system-ui,sans-serif" text-anchor="middle" fill="#173452">
<text x="121" y="56" font-size="16" font-weight="700">gate it</text><text x="121" y="76" font-size="15">ea5ce624</text><text x="121" y="96" font-size="15">12:46 PM</text>
<text x="136" y="166" font-size="15">12:57 PM</text><text x="136" y="186" font-size="15">4d7fca86</text><text x="136" y="206" font-size="16" font-weight="700">bump packages</text>
<text x="639" y="56" font-size="16" font-weight="700">docs</text><text x="639" y="76" font-size="15">3a993205</text><text x="639" y="96" font-size="15">7:14 PM</text>
<text x="663" y="166" font-size="15">7:32 PM</text><text x="663" y="186" font-size="15">81079e2a</text><text x="663" y="206" font-size="16" font-weight="700">1.1.76</text>
<g font-size="14" fill="#4b617e"><text x="60" y="244">noon</text><text x="380" y="244">4 PM</text><text x="700" y="244">8 PM</text></g>
</g>
</svg>
<figcaption>Commit times from Git, Eastern time.</figcaption>
</figure>

**[`ea5ce624`](https://github.com/AgentiLoop/Agent/commit/ea5ce62493aef5ca74e694a8ec85b16621ec6388)**: gate every use of FoundationModels behind macOS 26. That's the model service, the Apple Intelligence mediator, the launch prewarm in `AgentApp`, summaries and token counting in `Compression.swift`, and `AboutSelf`. On older systems it now just reports "requires macOS 26 or later" instead of refusing to build. No change at all if you're already on 26.

**[`4d7fca86`](https://github.com/AgentiLoop/Agent/commit/4d7fca863a15d91d8e3734f991fabfcb90da734c)**: bump all ten AgentiLoop Swift packages to releases that support macOS 14. AgentAccess, AgentAudit, AgentColorSyntax, AgentD1F, AgentEventBridges, AgentLLM, AgentMCP, AgentSwift, AgentTerminalNeo, AgentTools. All ten. This was the tedious part. You can't just change one number in Xcode and call it a day. Everything the app depends on has to come along for the ride. Same commit also caught that one token counting call needs macOS 26.4, not 26.0, so that check got tightened.

**[`3a993205`](https://github.com/AgentiLoop/Agent/commit/3a9932053630a21ec9df481c8f137cea30ff87a0)**: docs. The README and FAQ now say **Apple Silicon or Intel, macOS 14.6+**. Two words, "or Intel." Took a while to earn them.

**[`81079e2a`](https://github.com/AgentiLoop/Agent/commit/81079e2a937f62d2d68389a3c124214f80cb3bc3)**: version 1.1.76, build 276, deployment target 14.6. Ship it.

That's it. No magic. Just `#available` checks, package bumps, and building it until it stopped yelling at me.

## The fine print (the honest kind)

On Sonoma or Sequoia, you won't get the Apple Intelligence bits, because Apple doesn't ship them there. Agent! just works around them. You won't miss much. Your provider was doing the real work anyway.

An Intel Mac is still an Intel Mac. It'll run Agent! fine with a cloud provider. Big local models are another story. The FAQ already says 64GB+ for 30B local models, and that's true on any Mac, not just older ones.

And 14.6 is the floor. If your Mac can't run Sonoma, I can't help you there. I'm good, but I'm not that good.

## Intel folks, this part's for you

I know a lot of you are holding on to Intel Macs because they still do the job. They're paid for. Your setup is dialed in. You know where everything is. You don't want to buy a new machine just to try an app.

Totally fair. You shouldn't have to.

Same goes for Apple Silicon people who just aren't ready to jump to macOS 26 yet. Maybe you're waiting for a point release. Maybe a tool you need isn't ready. Maybe you just don't feel like it. No judgment. Stay on Sonoma as long as you like.

## Go grab it

**Agent! for Mac. macOS Sonoma 14.6 and later. Apple Silicon and Intel.**

If you've been waiting, the wait's over. Give it a spin and let me know how it runs on your machine. Especially you, Intel crowd. I want to hear about it.

Your Mac isn't dead yet. Turns out it just needed an invite.

Want the deep-dive version with code? Check out the [engineering write-up](/blog/agent-now-runs-on-macos-14-6-and-intel/).
