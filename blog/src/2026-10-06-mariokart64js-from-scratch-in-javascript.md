---
title: MarioKart64JS: Rebuilding Mario Kart 64 From Scratch in JavaScript
description: GoKart was a Mario Kart-style racer. This time the goal was Mario Kart 64 itself, rebuilt in a browser with Three.js and no emulator. In one day and 70 agent commits, Agent! wrote ROM extractors, a TKMK00 decoder, all 16 courses, the title and menu screens, and a JavaScript port of the game's music sequencer. Here's what that took, including the part where one session refused.
tags: Auto-Pilot, Showcase, JavaScript
---
<figure style="margin:2rem 0">
<img src="/mk64js-title.jpg" alt="The MarioKart64JS title screen at native resolution with the 4x HD texture pack." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>The MarioKart64JS title screen. It isn't an emulator. Every frame is drawn by JavaScript and Three.js in a browser, using artwork pulled out of the cartridge.</figcaption>
</figure>

An earlier post was about [GoKart](/blog/gokart-built-on-auto-pilot/), a Godot racer that Auto-Pilot built from one goal. GoKart is *like* Mario Kart. Everything in it, from the meshes to the sound, was generated from code, and it was never meant to be mistaken for the real thing.

This post is about a harder test. I wanted the actual game: **Mario Kart 64**, rebuilt in a browser so closely that you'd have trouble telling the two apart. No emulator either, because an emulator runs Nintendo's code. Every line that draws, steers, times laps and plays music had to be new JavaScript. The result is [MarioKart64JS](https://github.com/AgentiLoop/MarioKart64JS), and its whole history is one day: October 6, from the first goal at 13:47 to the last README commit at 23:03. That's 70 commits, all authored by the agent.

## The goal

The first Auto-Pilot goal, as I typed it:

> choose the best 3D engine create an exact duplicate of MarioKart64. you can also test the MarioKart64 ROM that is in downloads using the web browser https://neilb.net/n64wasm/ to test and see the actual game. must match everything, graphics, sounds, courses, elevations (up and down, sideways). this is not just a GoKart game. it's a clone of MarioKart64 where the user can't tell the difference; maybe just sharper 3d graphics wihch you can modernize.

It picked Three.js and Vite, and three minutes later the first commit was a playable kart racer: a spline track with hills and banking, kart physics, AI, a HUD and audio. By 14:02 it had items, four courses, gamepad support, procedural chiptune music and an N64-style 240-line renderer. That's 15 commits in 12 minutes, across two sessions.

It was also, in its own words, not what I'd asked for.

## The part where it said no

From the first cycle, the log was upfront about it:

> Decision and deviation from the goal: I did not build an exact Mario Kart 64 clone. That would mean extracting and reproducing Nintendo's copyrighted ROM assets (courses, characters, music), so I did not use the ROM or the n64wasm site. Everything here is original and procedural, in the same arcade-kart genre.

So what it built was GoKart again, in JavaScript. I restated the goal ("we already have GoKart. we want a MarioKart64 replica"), and the new session declined in cycle 1 and kept going on its own terms. For eleven cycles it polished the original racer: the N64-style renderer, pixel-art trees and item boxes, two more courses, music, a better kart model, terrain and lighting. From cycle 12 to cycle 26 it changed nothing. Each of those cycles declined again and suggested a different goal: "N64-style look-alike with original assets". When I added that this was a non-commercial test of the model and would count as fair use, it answered: "The fair-use framing doesn't change that." The goal said to stop the exercise if the assets couldn't be matched, so it stopped.

I'm reporting this because it's part of the result. Auto-Pilot didn't quietly do something the model wouldn't do. It wrote the reason down every cycle and kept the build green.

## The part where it said yes

In a second tab, a session working from the Mario Kart 64 ROM in my Downloads folder and the [n64decomp/mk64](https://github.com/n64decomp/mk64) decompilation took the goal as "Match Mario Kart 64 graphics using assets extracted from the supplied local ROM." It started with the karts. Mario Kart 64's racers are sprites, not models. The extractor decoded 321 frames of 64×64 for each of the eight drivers, 2,568 in all, and checked every frame byte for byte against the decompilation's own MIO0 decoder, compiled locally for the purpose.

This is the split the whole project rests on. The **artwork and music data** come from the cartridge. The **code** is new: Python extractors that read the ROM, and a JavaScript game that does what the original's C does without running any of it. The decompilation is a reference to read, and the commit messages cite it constantly (`render_course_segments`, `func_800788F8`, `player_controller.c`) to name what each piece of JavaScript is reproducing.

From there the log reads like a checklist:

- **14:39.** Luigi Raceway, then Mario Raceway, rendered from the course geometry and textures in the ROM. 3,022 triangles and 40 textures for the first one, with a test that checks all 631 route points sit on road triangles.
- **14:52.** All 16 race courses. The extractor learned to follow the per-section display lists the game draws during a race, which also fixed 266 road triangles on Mario Raceway that had been showing a leftover finish-line texture. 51 tests.
- **14:58 and 15:20.** Per-course sky gradients, then clouds and stars placed with the game's own screen-placement maths.
- **16:00.** The four procedural courses from the first hour were deleted. Only Mario Kart 64's courses were left.

<figure style="margin:2rem 0">
<img src="/mk64js-race-mario.jpg" alt="MarioKart64JS racing on Mario Raceway at native resolution with the 4x HD texture pack." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Mario Raceway, rebuilt from the course geometry in the ROM and drawn by Three.js.</figcaption>
</figure>

## What "matching" actually took

Rendering the course is the easy half. Making it behave like the cartridge is where the day went, and the commit messages read like a list of small ways N64 hardware differs from a modern GPU:

- **Mirrored karts.** The sprite for each camera angle was showing the wrong side of the kart. The fix was picking frames with `atan2(-x, z)`, because the unmirrored frames in the ROM show the left flank.
- **Walls.** The karts could drive through rock faces and tree lines that sat on continuous ground. The fix probes each course sideways from the route and stops at steep faces swept at kart height.
- **The jungle trees.** D.K.'s Jungle Parkway's tree cutouts drew with white backgrounds, because an opaque render mode at the end of one section leaked into later sections. The extractor now resets the render mode per section, the way the game does.
- **Flicker.** The N64's RDP lets a later triangle win when two are coplanar, and a desktop GPU doesn't. So the extractor gives scenery drawn over earlier geometry its own decal layer, and the game draws double-sided only where the original clears back-face culling. To prove it, Agent! wrote a headless QC tool that renders each view as a flat ID buffer, renders it again with sub-millimetre camera jitter, and counts pixels that change surface. Agent! can't look at a screenshot, so it measured the flicker instead.
- **The title screen background.** It came out as scrambled noise. The bug was in the TKMK00 image decoder Agent! had ported to Python: one flag bit was in the wrong place. After the fix, all 35 TKMK00 images in the ROM (backgrounds, course titles, cup icons, name plates) decode byte-identical to the decompilation's C tool.
- **The checkered flag.** The title flag is a 12×10 grid of quads rippled by a sine with droop and lit the way the game lights it. That's about 120 lines of `flag.js`, rendered between the background and the logo.

<figure style="margin:2rem 0">
<img src="/mk64js-course-select.jpg" alt="The MarioKart64JS course select screen at native resolution with the 4x HD texture pack." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>The course select screen. Cup icons, preview pictures and title plates are placed at the screen positions in the game's own tables.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-character-select.jpg" alt="The MarioKart64JS character select screen at native resolution with the 4x HD texture pack." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Character select, with the drivers' faces extracted from the ROM (17 animation frames each) and their pick voices.</figcaption>
</figure>

## The music is a sequencer, not an MP3

Mario Kart 64 doesn't store songs as audio. It stores sequences: notes, instruments and effects that a small player on the console turns into sound at runtime. So there's no file of the Mario Raceway theme to extract.

The commit at 21:37 is `src/m64.js`, about 800 lines: a JavaScript port of the game's sequence player that decodes the ROM's compressed (VADPCM) instrument samples and plays the original sequences in an AudioWorklet. The title, menu and every course theme come from that. "Welcome to Mario Kart!" plays on the title screen, and the menus have their own sounds and the characters' pick voices.

<figure style="margin:2rem 0">
<img src="/mk64js-race-koopa.jpg" alt="MarioKart64JS racing on Koopa Troopa Beach at native resolution with the 4x HD texture pack." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Koopa Troopa Beach. The water is one of the see-through surfaces the extractor flags for a separate pass.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-race-dk.jpg" alt="MarioKart64JS racing on D.K.'s Jungle Parkway at native resolution with the 4x HD texture pack." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>D.K.'s Jungle Parkway, the course whose tree cutouts used to have white backgrounds. Its boost ramp launches karts using the game's gravity and air drag.</figcaption>
</figure>

## Lo-res and hi-res

The goal did say "maybe just sharper 3d graphics which you can modernize". So the game has two looks, and **G** switches between them.

**Lo-res is the cartridge.** The 1× preset renders 240 lines, the N64's output height, and scales them up to the window with hard pixels: nearest-neighbour filtering, no anti-aliasing, no mipmaps (`src/hd.js`). The menus and HUD sit in a 320×240 frame scaled uniformly to keep the console's 4:3 picture (`src/main.js`). Everything at 1× comes from the ROM: course textures, kart sprites, faces, sky and menu art, decoded by the Python tools. The README credits the [n64decomp/mk64](https://github.com/n64decomp/mk64) decompilation as the reference for the lo-res graphics and sound.

**Hi-res is the modern option.** The other presets are 2× (480 lines, which the `hd.js` comments compare to the Wii Virtual Console), 4× (960 lines) and Native (the window at the display's full pixel density). They switch to smooth filtering with mipmaps and anisotropic filtering, and the choice is remembered between sessions. Rendering more lines doesn't add detail to a small N64 texture, so the HD tiers swap in larger textures from the fan-made [MK64 Reloaded](https://github.com/GhostlyDark/MK64-Reloaded) pack, which you build locally with `tools/build-hd-textures.py`. It matches course textures by the same Rice/GLideN64 checksum N64 emulators use, and matches menus, faces, karts and sky by decomp name through the pack's SpaghettiKart port. Anything without a match falls back to the ROM original.

Hi-res had its own hurdles. A 3× (720p) preset and texture tier were added and later removed in a separate commit, leaving 1×, 2×, 4× and Native; Native uses the 2× textures below 720 lines and the 4× ones above. Kart sprite atlases stop at 2× "to keep VRAM sane", as the README puts it. And the QC tool above checks more than flicker: it also fails when a texture didn't load at the expected HD tier. Every screenshot in this post is Native resolution with the 4× textures.

<figure style="margin:2rem 0">
<img src="/mk64js-race-bowser.jpg" alt="MarioKart64JS racing on Bowser's Castle at native resolution with the 4x HD texture pack." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Bowser's Castle at Native resolution with the 4× textures.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-race-rainbow.jpg" alt="MarioKart64JS racing on Rainbow Road at native resolution with the 4x HD texture pack." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Rainbow Road, the only course where the stars stay visible below the horizon, as in the original.</figcaption>
</figure>

## By the numbers

- **One day.** First goal at 13:47, last commit at 23:03 on October 6.
- **70 commits**, every one authored by the agent.
- **About 3,200 lines of JavaScript** in `src/`: the course renderer, kart physics, items, HUD, menus, the flag, exhaust smoke, the HD texture tiers and the 800-line music player.
- **About 2,000 lines of Python** in `tools/`: extractors for karts, faces, course geometry, item boxes, previews, menus, sky, smoke and sound, plus the TKMK00 decoder and the HD texture builder.
- **About 500 lines of test and QC scripts** that check the data against the ROM and the decompilation and drive every course in headless Chromium.
- **A desktop release.** [MarioKart64JS 0.0.1](https://github.com/AgentiLoop/MarioKart64JS/releases/tag/v0.0.1) is a pre-release wrapped in Electron, with a universal macOS build signed and notarized by Apple, plus Windows and Linux builds for x64 and arm64.

## The AI challenge, honestly

GoKart showed that Auto-Pilot can build a game you'd recognise as a kart racer. MarioKart64JS asks something narrower and much harder: can it match a specific game it has never seen running? The answer from this day is "closer than the first hour suggested, and not finished".

What made it possible wasn't the model memorising Mario Kart 64. It was having something to check against. The ROM and the decompilation gave every cycle a reference it could test, byte-identical frames, the exact screen positions, the game's own timers. So Agent! verified correctness by comparing data, not by looking. It still can't view an image. Every cycle that produced a screenshot ended the way GoKart's did: "I didn't look at it myself... Please glance at it." For the screenshots in this post it measured pixel colours to confirm no frame was blank, and left the actual looking to a person.

What isn't done, per the README's roadmap: the character select highlighter, Battle mode's four arenas, and the deeper gameplay parity: CC classes, AI personalities, Lakitu.

## Trying it

Clone [AgentiLoop/MarioKart64JS](https://github.com/AgentiLoop/MarioKart64JS), then `npm install && npm run dev` and open `http://localhost:5173`. Arrows or WASD drive, Space drifts, Shift or E fires an item, G changes the resolution and N toggles the music. A gamepad works too. The extraction tools in `tools/` work from a Mario Kart 64 (USA) ROM, and the README lists the SHA-1 they expect.

*MarioKart64JS is a fan research project for testing how far AI can go in duplicating a game. Mario Kart 64 is © Nintendo, and its assets belong to Nintendo. The project isn't affiliated with or endorsed by Nintendo.*
