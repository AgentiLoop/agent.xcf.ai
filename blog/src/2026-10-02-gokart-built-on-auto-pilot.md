---
title: GoKart: A Mario Kart-Style Racer That Auto-Pilot Built in an Afternoon
description: Give Agent!'s Auto-Pilot one goal - "create a Mario Kart clone called GoKart" - and come back to a Godot 4 racer with three tracks, eight items, AI rivals and 3,344 passing test checks. Two days and 87 agent commits later it is GoKart 0.0.2: four courses, Battle mode, Time Trials, a Mario Kart 64 style menu and 14,134 passing checks. Here is what the log says actually happened, including the parts where it got stuck.
tags: Auto-Pilot, Showcase, Godot
updated: 2026-10-04
---
<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-title.png" alt="The GoKart 0.0.2 title screen: the word GOKART set on an arch in big yellow-to-red gradient letters with navy block sides and a soft shadow, over a live attract demo of CPU karts lapping a course, with PRESS ENTER underneath." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>The GoKart 0.0.2 title screen. The logo flies in and bounces to a stop over a live attract demo that tours the courses. Every mesh, shader, font layout and sound was generated from code.</figcaption>
</figure>

*Updated October 4: this post now covers the two days after the first afternoon, the two Auto-Pilot sessions that ran at the same time in the same repo, and the [GoKart 0.0.2](#gokart-0-0-2) release. The screenshots were retaken from the 0.0.2 tag.*

Yesterday's post introduced [Auto-Pilot](/blog/agent-1-1-87-and-agentiloop-cli-0-0-5/): type `/auto <goal>` into Agent! for Mac and it runs unattended cycles toward that goal until you press Stop All. This post is about what came out the other end when I pointed it at a game.

The goal, pasted more or less as I typed it:

> create a Mario Kart clone called GoKart with all Mario Kart effects. I believe Godot 4 can do the Mario Kart effects, but I haven't built any of them yet: drift sparks and boost flames (GPUParticles3D), speed lines and boost blur (screen-space shaders, glow and tonemapping), item effects and tire trails (shaders plus ribbon meshes), kart movement (VehicleBody3D or custom arcade physics). Write unit tests and test the game frequently.

Budget: no time limit, unlimited cycles. The model inside Agent! for every cycle was Claude Sonnet 5.5. The first commit landed at 12:39. By 16:32 the same afternoon the repo had 33 commits, 47 GDScript files, about 5,500 lines of GDScript and shader code, and a unit suite that passed 3,344 checks. Two days later, at the 0.0.2 tag, it is 126 commits, 150 GDScript files, about 24,500 lines and 14,134 checks, and every one of those commits is authored by the agent. The whole thing is on GitHub at [AgentiLoop/GoKart](https://github.com/AgentiLoop/GoKart).

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
<img src="/gokart-0-0-2-sunset-speedway.png" alt="GoKart 0.0.2 on Sunset Speedway: the player kart drifting in 3rd of 8 on lap 1 under the sunset sky, with the Mario Kart 64 style HUD: a see-through course map in the bottom-left corner, place, lap and speed in a rounded gold-and-cream font." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Sunset Speedway in 0.0.2: a random-drive bot mid-drift in 3rd of 8. The second track was added in cycle 12 of the first day, along with the title menu. The traffic, the buildings beyond the walls and the HUD came two days later.</figcaption>
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

That's the right behaviour. The goal was "the steering feels bad" and "the walls flicker", and no headless test can close that goal. Auto-Pilot has no iteration cap, so it would have kept checking in forever. The session ended after cycle 8, and what GoKart needed next was a playtest, not another cycle. That evening the repo was tagged 0.0.1 and exported for macOS, Windows and Linux.

## Two days later: two Auto-Pilots in one repo

On October 3 I came back with a different kind of goal. Not a feature list, a reference:

> keep building GoKart to resemble Mario Kart Nintendo 64 version. search Mario Kart N64 or Mario Kart Nintendo 64 and keep improving, iterating, making GoKart better

That fifth session started at 14:19 and ran 28 cycles, and nearly every cycle is one Mario Kart 64 thing the agent looked up and built: the 8-racer field on a two-column grid, rubber-banding per difficulty, 50cc / 100cc / 150cc and the mirrored Extra class, Light / Medium / Heavy karts that shove each other, Grand Prix with 9/6/3/1 points and the rank-out rule, Time Trials with a ghost, Battle mode with balloons in Big Donut, Block Fort and Skyscraper, triple and golden mushrooms, the fake item box, the banana bunch, Boo, triple red shells, shell blocking, the false start, Lakitu with the start signal and the lap signs, a fourth course called Dusty Canyon, the Kalimari Desert train with level crossings, Toad's Turnpike traffic, Monty Moles, snowmen, penguins, Sherbet Land ice, roadside scenery per theme, the slipstream, a jump ramp, the hop-and-toggle powerslide, and a chiptune loop for every course rendered from step patterns in code.

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-train.png" alt="GoKart 0.0.2 on Dusty Canyon: the player kart waiting at a level crossing as a steam train rolls across the road, with a crossbuck signal beside the track, under a desert sky." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Dusty Canyon, the fourth course, with its Kalimari Desert style train. CPU karts stop and wait at a blocked crossing; a kart that doesn't gets thrown into the air.</figcaption>
</figure>

Four hours in, at 18:25, I opened a second tab and started a second Auto-Pilot on the same repository, with a narrower goal:

> the menus are not Mario Kart Quality and neither is the title shot. and there is over use of black outlines on text everywhere. see Mario Kart 64 screenshots and images on the web and make better menus. focus only on the menus / screens and title shot for GoKart. make conscious decisions. do not conflict with previous /auto working on the application

So from 18:25 to midnight two agents were committing to the same working tree. The menus session rebuilt the title screen with an arched gradient logo that flies in and bounces, a select screen with a picture beside every course, a live fly-over of the picked course, option rows with lit bars, a turning kart portrait and a gold cursor, a course intro fly-over, a pause screen, a results board whose rows slide in one after another, and a shared palette of rounded gold-and-cream text with drop shadows that replaced every 8-pixel black outline in the game. It ran 23 cycles and declared the goal reached at 23:54.

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-select.png" alt="The GoKart 0.0.2 select screen: the GOKART logo at the top, a course list on the left with a small picture beside each course name and the picked row lit, a live picture of the course with the map outline in its corner on the right, rows of option pills for laps, CPU, engine class, kart weight and mode, and the player's kart turning in a small portrait window, all over the dimmed attract demo." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>The select screen after the menus session. Course pictures, a live fly-over of the course, every option listed as a row of pills with the picked one lit, and the kart turning in its portrait window.</figcaption>
</figure>

The "do not conflict" line did real work. The log is full of the two sessions working around each other: the menus session verifying from a clean `git worktree` at HEAD so "the other session's in-flight penguins work" stayed out of its test runs, one session finishing the other's half-done feature when I asked it to, and commits staged file by file instead of `git add -A` because the other tab's edits were sitting in the same tree. It wasn't tidy, but nothing was lost and the suite ended the night at 14,134 passed, 0 failed.

The feature session's log ends three minutes later, at 23:57, with "Session ended — Stop All". My note to Agent! straight afterwards, which it saved as the message of the next checkpoint commit, was that Stop All needs to stop only the tab it's pressed in, not all of them. With two Auto-Pilots running, one button for both is the wrong button.

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-snowmen.png" alt="GoKart 0.0.2 on Frosty Peaks: the player kart at the entrance of a field of snowmen standing in staggered rows across the snow-white road, each with a red scarf, top hat and carrot nose, under a dark blue dusk sky." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>The snowman field on Frosty Peaks. Hit one and you're thrown into the air while it bursts into snow; CPU karts look 40 metres ahead and weave through the rows.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-penguins.png" alt="GoKart 0.0.2 on Frosty Peaks: a penguin sliding on its belly across the pale blue-white ice of the long sweeper ahead of the player kart." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Sherbet Land style ice and penguins on Frosty Peaks. On ice the nose turns but the kart keeps sliding the way it was going; the penguins waddle to the edge, flop and slide back through.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-traffic.png" alt="GoKart 0.0.2 on Sunset Speedway: the player kart stuck behind a bus and a box truck with their headlights on in the two lanes of the road, under the sunset sky." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Toad's Turnpike traffic on Sunset Speedway: cars, buses, box trucks and tankers with headlights, and buildings with lit window bands beyond the walls.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-gp-results.png" alt="The GoKart 0.0.2 Grand Prix results board on a navy panel with a gold rim: the race result on the left and the cup standings on the right, one row per racer with a colour swatch, gold, silver and bronze places, times and points, the player's row on a lit gold bar, and the trophy underneath." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>The Grand Prix results board: race result and cup standings side by side, the rows sliding in one after another with a tick each, and the trophy underneath.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-battle.png" alt="GoKart 0.0.2 Battle mode: four karts on their start pads in a battle arena, each with three balloons tied to it, and Lakitu's start signal overhead." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Battle mode: four karts, three balloons each. Item hits, lava, the roof edge, star touches and heavy shoves pop balloons, and a kart with none left becomes a Mini Bomb Kart.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-dusty-canyon.png" alt="GoKart 0.0.2 on Dusty Canyon: the player kart in 5th of 8 on lap 1 on the desert road, with the Mario Kart 64 style HUD." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Dusty Canyon from the random-drive bot, 5th of 8. Desert sweepers, a hairpin, a left-hand S, two oasis water stretches, the train, and a jump ramp on the opening straight.</figcaption>
</figure>

## About these screenshots

Agent! took them, not me, and not by hand. For the first version I asked for three screenshots of a random drive, and it wrote a 70-line `tools/random_drive.gd` that follows the road with a wandering lane offset, throws in random drift bursts and fires whatever item it's holding at random moments, then saves a frame every few hundred physics frames. The two race shots above are frames from that bot. The rest come from the shot tools each feature shipped with: `menu_shot.gd`, `train_shot.gd`, `traffic_shot.gd`, `snowman_shot.gd`, `penguin_shot.gd`, `hud_shot.gd` and `battle_shot.gd`, each of which stages its scene, waits for the right frame and saves it. All of them were run for this update from a clean worktree checked out at the `v0.0.2` tag, so nothing uncommitted is in a picture. Agent! still can't look at the result, so the tools sample pixels instead: the ice shot prints the road colour ahead on ice against tarmac, the pause shot proves nothing moved outside the panel for a second, and before publishing I had it count pure-black pixels in all ten pictures above: zero in each. There are more in the [GoKart README](https://github.com/AgentiLoop/GoKart#screenshots).

## What I'd tell you before you try it

- **Run it in git.** Auto-Pilot has no undo. GoKart's log is readable because every cycle ended in a commit, and the one time a cycle went sideways, nothing was lost.
- **Put the operational rules in the goal.** "Put a time limit on shell" worked better as part of the goal than as a one-off message, because every new cycle re-reads the goal.
- **Expect it to ask for eyes.** For anything visual or about feel, the loop will stall honestly rather than lie. Budget a playtest between sessions, and feed your notes back in as the next goal.
- **Stop All is part of the workflow**, not a failure. The first three GoKart sessions all ended with it.
- **Two Auto-Pilots in one repo works, if you tell them about each other.** "Do not conflict with the previous /auto" went into the second goal, and both sessions spent real effort staying out of each other's way. Give them separate areas of the code, and expect the one you stop to take the other with it for now.

## Is that good?

I asked Agent! that question after it had read the repo, counted the commits and found the Auto-Pilot log. All 126 commits are authored by the agent, none by a person, and `.agent/autopilot/progress.md` runs past Cycle 23. Its answer, unedited:

> It depends on what you want out of it. As a showcase of what Auto-Pilot can do, it's impressive. Twenty-three plus cycles produced four courses, items, AI racers, Grand Prix, Time Trials, Battle mode, procedural music and sound, all with no imported assets, and a README that documents it in detail. That's a lot of working software from a single goal statement.

It also added the caveat that nobody human reviewed it along the way, so quality was judged by the agent's own verification logs, and that it hadn't played it or audited the code, so it couldn't say how well it actually plays. Which is the same conclusion the log reached on its own: the next step is a playtest.

## GoKart 0.0.2

You don't need Godot to try it. [GoKart 0.0.2](https://github.com/AgentiLoop/GoKart/releases/tag/v0.0.2) is the second packaged release, exported from the same repo, 87 commits after [0.0.1](https://github.com/AgentiLoop/GoKart/releases/tag/v0.0.1):

- **macOS** universal (Apple silicon and Intel), signed with a Developer ID and notarized by Apple
- **Windows** x86_64
- **Linux** x86_64 and arm64

Each download is a single self-contained binary with the game data embedded, and `SHA256SUMS.txt` is on the release page if you want to check what you got. The Windows build is unsigned, so expect the SmartScreen prompt. Everything in this post that wasn't in 0.0.1 is in 0.0.2: Battle mode, Time Trials, the four-course cup, the engine and weight classes, the new items, Lakitu, the train, the traffic, the moles, the snowmen, the penguins, the ice, the scenery, the slipstream, the jump ramp, the course music, the new title and select screens, the course intro, the pause screen and the restyled HUD. The release notes have the full list.

Agent! 1.1.87 with Auto-Pilot is on the [releases page](https://github.com/AgentiLoop/Agent/releases/latest) and in Homebrew. If you'd rather run GoKart from source, it needs Godot 4.4 or later: `git clone https://github.com/AgentiLoop/GoKart.git && cd GoKart && godot --path .`
