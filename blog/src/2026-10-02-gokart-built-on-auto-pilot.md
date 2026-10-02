---
title: GoKart: A Mario Kart-Style Racer That Auto-Pilot Built in an Afternoon
description: Give Agent!'s Auto-Pilot one goal - "create a Mario Kart clone called GoKart" - and come back to a Godot 4 racer with three tracks, eight items, AI rivals and 3,344 passing test checks. Here is what the log says actually happened, including the parts where it got stuck.
tags: Auto-Pilot, Showcase, Godot
---
<figure style="margin:2rem 0">
<img src="/gokart-green-hills-drift.png" alt="GoKart on the Green Hills track: a chase-camera view of the player kart mid-drift on a grey road with red and white striped walls, green ground and blue sky. The HUD shows 1st place, lap and time counters and a track minimap in the bottom-left corner." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Green Hills, lap 1, drifting in first. Every mesh, shader and sound in this frame was generated from code.</figcaption>
</figure>

Yesterday's post introduced [Auto-Pilot](/blog/agent-1-1-87-and-agentiloop-cli-0-0-5/): type `/auto <goal>` into Agent! for Mac and it runs unattended cycles toward that goal until you press Stop All. This post is about what came out the other end when I pointed it at a game.

The goal, pasted more or less as I typed it:

> create a Mario Kart clone called GoKart with all Mario Kart effects. I believe Godot 4 can do the Mario Kart effects, but I haven't built any of them yet: drift sparks and boost flames (GPUParticles3D), speed lines and boost blur (screen-space shaders, glow and tonemapping), item effects and tire trails (shaders plus ribbon meshes), kart movement (VehicleBody3D or custom arcade physics). Write unit tests and test the game frequently.

Budget: no time limit, unlimited cycles. The first commit landed at 12:39. By 16:32 the same afternoon the repo had 33 commits. Today it has 47 GDScript files, about 5,500 lines of GDScript and shader code, and a unit suite that passes 3,344 checks. The whole thing is on GitHub at [AgentiLoop/GoKart](https://github.com/AgentiLoop/GoKart).

## What Auto-Pilot does, one cycle at a time

Auto-Pilot keeps a running log at `.agent/autopilot/progress.md` inside the project, and every cycle appends what it did, what it assumed, what remains and whether anything blocked it. That log is the source for everything below. I'm quoting it rather than my memory because the log is more honest than I am.

**Cycle 1** had no Godot on the machine. It ran `brew install --cask godot`, symlinked the binary, did `git init`, and wrote `kart_physics.gd` as a pure model with no scene dependencies: acceleration, braking, reverse, friction, steering, a drift locked to the direction you started in, and three mini-turbo levels. It chose custom arcade physics over `VehicleBody3D` on purpose, and said why: "so the Mario Kart handling is easy to unit test." Eleven tests, 17 checks, first commit.

**Cycle 2** added the effects I had asked for by name: GPUParticles3D drift sparks coloured by mini-turbo level, exhaust flames, ribbon-mesh tire trails, and a screen-space shader for radial boost blur, speed lines and a vignette. 43 checks.

**Cycle 3** built a track. A Catmull-Rom loop resampled every 3 metres, a road ribbon, red-and-white striped walls with colliders, boost pads with a scrolling chevron shader, eight ordered checkpoints and a lap tracker that refuses to count shortcuts or wrong-way laps. One of the new tests is a pursuit bot that drives three full laps using the real physics model. It finished in 1:02.5. 90 checks.

**Cycle 4** added item boxes with a rainbow fresnel shader, a roulette, and the first three items: mushroom, banana, and a green shell that ricochets off the walls. Getting hit spins the kart out for 1.2 seconds. 235 checks.

Then it got stuck.

## The part where it got stuck

The next cycle started adding AI karts and a headless smoke race, and never came back. The cause, found in the next session, was a single stray tab on line 115 of `main.gd`: a parse error that made the smoke script spam errors forever, with no time limit on the shell command that was running it.

I pressed **Stop All**, and started a new session with the same goal plus a note in capitals that I will not reproduce in full. The gist: *you got stuck testing the smoke run, do not get stuck, put a time limit on shell.*

The second session's first cycle fixed the tab, cut the AI lookahead from 10 road samples to 6 so the AI stopped cutting corners into the inner wall, added a corner-speed limiter, and wrapped every shell run in `perl -e 'alarm 100; exec @ARGV'`, because macOS ships without a `timeout` command. From then on the log says "all runs were behind perl alarm limits" at the end of nearly every cycle. It learned the lesson from the goal text and kept applying it.

That session ran 15 cycles in about an hour and a quarter, and each one is a feature: start countdown with a rocket-start boost for well-timed throttle; mini-turbo level-up pops and a screen-edge flash; a minimap; the homing red shell and the star; a procedural kart model with spinning wheels, steering front wheels and a driver whose head turns; lightning that shrinks every rival; triple shells that orbit the kart; the blue spiny shell that hunts the leader along the road; a results screen with points; fully synthesized audio with no audio files, from the engine loop to the finish jingle; a title menu with a second track; a lap-count option; a third track; and positional 3D engine hum on each AI kart.

<figure style="margin:2rem 0">
<img src="/gokart-sunset-speedway.png" alt="GoKart on the Sunset Speedway track: the player kart at full speed on a sandy circuit under an orange-to-violet sunset sky. The HUD shows 4th place, lap 1, and the minimap outline of a long track with a hairpin." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Sunset Speedway, the second track, added in cycle 12 along with the title menu. Longer than Green Hills, with a hairpin and a chicane.</figcaption>
</figure>

## The part where it was honest

What I like most in the log is the pattern of confessions. Agent! cannot look at a PNG, and it said so, cycle after cycle:

> The windowed screenshot run logged no errors, but I can't view images, so I haven't looked at how the track or HUD render.

> I haven't heard the sounds, and I didn't run the smoke race or the screenshot tool.

> I can't view images with my tools, so that review needs a person.

So it tested what it could: headless scene checks that instantiate the real scene and assert on state. Fire lightning, confirm three rivals are at scale 0.5 and spinning and the bolts are cleaned up afterwards. Fire a blue shell at a bunched start grid, confirm the explosion at frame 12 and two karts spinning. Force the player to finish, confirm the autopilot hands the kart to an `AiDriver` and the results panel shows "1st YOU".

A third session stalled the same way, this time behind a 240-second alarm that was far too generous, and I stopped it after one cycle. Then a person looked. That person was me, and the fourth session's goal was my playtest notes, lightly tidied:

> the UI needs to scale with the window. the UI should not be prone to the screen speed effects and blurry. Should be able to use cursor keys. it's not clear when power ups are released. the tops of the walls flicker. Little too hard to steer the kart. hard to keep up with the computer AI karts. maybe have AI difficulty levels Easy Medium and Hard.

One cycle later: canvas-items stretch so the UI scales with the window, the HUD moved to a canvas layer above the speed-effects overlay, arrow keys, Enter and Ctrl for items with an on-screen hint, eased-in steering, a z-fighting fix for the wall stripes (neighbouring red and white segments were fighting over the same pixels, so the white ones got very slightly larger), 4x MSAA, and Easy / Medium / Hard that scale AI top speed to 0.72, 0.85 and 1.0. Tests went from 2,156 to 3,344 checks, partly because it also found and fixed a pre-existing parse error in `tests/test_items.gd` that had stopped the suite from loading.

## The part where it stopped itself

Cycles 2 through 8 of that last session made no code changes. Each one re-read the repo, re-ran the suite, and wrote a variant of the same paragraph:

> I couldn't see the result on screen, so I'm not declaring the goal reached. Four items still need a human to try them in the game.

That's the right behaviour. The goal was "the steering feels bad" and "the walls flicker", and no headless test can close that goal. Auto-Pilot has no iteration cap, so it would have kept checking in forever. The session ended after cycle 8, and what GoKart needed next was a playtest, not another cycle.

<figure style="margin:2rem 0">
<img src="/gokart-frosty-peaks.png" alt="GoKart on the Frosty Peaks track: the player kart at full speed on a snow-white circuit under a dark blue dusk sky. The HUD shows 2nd place, lap 1, speed in km/h and the minimap." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Frosty Peaks, added in cycle 14 as a new entry in the track library. The per-track tests picked it up automatically.</figcaption>
</figure>

## About these screenshots

Agent! took them, not me, and not by hand. I asked for three screenshots of a random drive, and it wrote a 70-line `tools/random_drive.gd` that follows the road with a wandering lane offset, throws in random drift bursts and fires whatever item it's holding at random moments, then saves a frame every few hundred physics frames. It ran once per track, and the three above are one frame from each. They're in the [GoKart README](https://github.com/AgentiLoop/GoKart#screenshots) too.

## What I'd tell you before you try it

- **Run it in git.** Auto-Pilot has no undo. GoKart's log is readable because every cycle ended in a commit, and the one time a cycle went sideways, nothing was lost.
- **Put the operational rules in the goal.** "Put a time limit on shell" worked better as part of the goal than as a one-off message, because every new cycle re-reads the goal.
- **Expect it to ask for eyes.** For anything visual or about feel, the loop will stall honestly rather than lie. Budget a playtest between sessions, and feed your notes back in as the next goal.
- **Stop All is part of the workflow**, not a failure. The first three GoKart sessions all ended with it.

Agent! 1.1.87 with Auto-Pilot is on the [releases page](https://github.com/AgentiLoop/Agent/releases/latest) and in Homebrew. GoKart needs Godot 4.4 or later: `git clone https://github.com/AgentiLoop/GoKart.git && cd GoKart && godot --path .`
