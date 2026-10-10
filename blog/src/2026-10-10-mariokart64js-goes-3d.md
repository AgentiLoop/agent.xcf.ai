---
title: MarioKart64JS Goes 3D: Wii Karts, a 3D Title Screen and Finish Fly-Overs
description: Mario Kart 64 draws its racers as flat sprites. Press 3 in MarioKart64JS and every kart becomes a 3D model, Lakitu included, with real shadows, a rebuilt 3D title screen and a camera that flies around your kart after the finish. Here's how the 3D mode was put together, in screenshots.
tags: Showcase, JavaScript
---
<figure style="margin:2rem 0">
<img src="/mk64js-3d-title.jpg" alt="The MarioKart64JS 3D title screen: Wario, Bowser, Mario, Peach and Toad in 3D karts driving at the camera under the Mario Kart 64 logo." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>The 3D title screen. The original is one flat painting. Here the sky, hills and road are built in Three.js and the five drivers are 3D karts driving at the camera.</figcaption>
</figure>

The [last MarioKart64JS post](/blog/mariokart64js-from-scratch-in-javascript/) was about matching Mario Kart 64 as closely as possible: course geometry, sprites and music taken from the cartridge, and new JavaScript doing what the original's C does. This one is about the opposite direction. One key, **3**, turns on a 3D mode that the N64 never had.

## Sprites become models

Mario Kart 64's racers aren't models. Each driver is 321 pre-rendered 64×64 frames, and the game picks the frame that matches the camera angle. That's what MarioKart64JS draws too, and it still does by default.

The 3D mode swaps those sprites for models of the Mario Kart Wii Standard Kart, from Collada exports staged into the project by `tools/build-wii-karts.py`. It started on the evening of October 9 as a single test: at 21:22 the 3 key put a red Standard Kart with Mario in it under the player. By 22:02 all eight drivers had one, split by the Wii's weight classes: the Small kart for Toad, Medium for Mario, Luigi, Peach and Yoshi, and Large for D.K., Wario and Bowser, each with its own livery.

Most of the work in between was small things a model loader gets wrong:

- **The eyes.** Each eye texture is a single eye. On the Wii a texture matrix doubles it and the sampler mirrors it into a pair. Three.js's ColladaLoader drops both, so one eye was stretched across the whole face. `kart3d.js` puts the repeat and the mirror back per character.
- **The tires.** The rear tires are the front tire mesh scaled up. Their size and the axle positions are measured from each kart's assembled menu model, which made the rear tires 1.29× bigger and put them where the Wii has them.
- **The seats.** Each driver gets a seat position so they sit in the reclined seat instead of floating above it.

Agent! can't look at a picture, so it checked the models with numbers instead: ASCII side, rear and top views of each kart, 12-angle turntable sheets, and measured gaps between each driver's hands and the steering wheel.

## Racing in 3D

<figure style="margin:2rem 0">
<img src="/mk64js-3d-race-mario.jpg" alt="MarioKart64JS in 3D mode racing on Mario Raceway with 3D karts." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Mario Raceway in 3D mode. Every kart in the race is a 3D model, each in its own character's Standard Kart.</figcaption>
</figure>

In a race, 3 swaps every kart on the track, not only yours, and the next press brings the sprites back. Two other things change with it.

**Shadows.** The sprites have a flat blob shadow under them. The 3D karts cast real shadow-map shadows onto the course. That needed a trick: the course is drawn with unlit materials that can't receive shadows, so the course gets transparent shadow-catcher copies of its surfaces that only show where a shadow falls.

**Lakitu.** The referee becomes the Mario Kart Wii Lakitu (`src/lakitu3d.js`). His arms are posed through the model's own bones: one holds the fishing rod, the other waves the flag. The start lights, lap boards and wrong-way sign hang from the rod's hook, and the original sprite's animation frame still drives the timing, so the red, red, blue countdown comes on when it always did.

A 3D kart also has a body the sprite didn't. Against walls it is a capsule, a circle over each axle, and it moves and turns as a rigid body. That had side effects. On Koopa Troopa Beach the nose circle reached a ramp's lip before the kart's centre did, and the lip's back face threw the kart off the jump. The fix tests each axle against the ground under it. A later commit stopped walls from turning the player's kart on a head-on hit, because in Mario Kart 64 a wall reflects the kart's motion and never turns its facing.

## A 3D title screen

Mario Kart 64's title background is one flat 320×240 picture. The sky, hills, road and five drivers are all painted in. Pressing 3 on the title rebuilds it (`src/title3d.js`): the sky, hills and road are made in Three.js, and the drivers are the same 3D karts as in the races.

The layout follows the painting. Wario is front left with Bowser behind him, Mario is front right with Peach behind, and Toad is coming out of the right-hand bend. Each kart is placed so its box on screen lands within about 10 pixels of its driver's box in the original art. The camera sits low on the road ahead of them with a wide 64° lens, and the road scrolls underneath, so the karts look like they're driving straight at you. The checkered flag, the logo, PUSH START and the copyright are still the 2D overlays from the original title.

The menus behind it got matching backgrounds too. Turning 3D on at the title also switches to the 4× texture tier, and races start in 3D until you press 3 again.

<figure style="margin:2rem 0">
<img src="/mk64js-3d-game-select.jpg" alt="The MarioKart64JS game select screen with its 3D-mode background." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>The game select screen with its 3D-mode background.</figcaption>
</figure>

## Fly-overs after the finish

When you cross the line, Mario Kart 64 hands the camera to a short cinematic. MarioKart64JS follows the game's camera code for it (`PLAYER_CINEMATIC_MODE` and the cinematic-shot functions in the decompilation): the camera swings round to the front of the kart and watches it cross the line, then cuts between shots while the CPU driver takes over your kart. The sequence repeats nose orbit, roadside, high crane, roadside, low tail shot, roadside. One caveat from the source comments: the shot lengths and distances are tuned by eye, not taken from the ROM's tables.

The tracking shots follow a heavily smoothed copy of the kart's heading. Without it, the AI's small steering corrections wobbled the camera around the kart and made it look like it was turning in jerks. With 3D karts these shots are where the models show the most, since the camera finally sees the karts from the front and the side.

<figure style="margin:2rem 0">
<img src="/mk64js-3d-flyover-front.jpg" alt="Finish fly-over on Mario Raceway: the camera ahead of Mario's 3D kart, looking back at it." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>The nose shot on Mario Raceway: the camera orbits from behind the kart round to its front and rides ahead of it.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-3d-flyover-crane.jpg" alt="Finish fly-over on Mario Raceway: a high crane shot looking down the road behind the kart." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>The high crane shot, above and behind the kart, looking down the road.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-3d-flyover-roadside.jpg" alt="Finish fly-over on Royal Raceway: a camera placed beside the road as the kart drives past." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>A roadside shot on Royal Raceway. The camera stands beside the road ahead and holds until the kart has gone past.</figcaption>
</figure>

## How the screenshots were taken

Every picture in this post was taken in headless Chrome at 1280×960. The title and game select shots press 3 on the title, the same as a player would. The races run on autopilot with the 3D mode saved on, and the fly-overs were captured by putting the player on the last stretch of the final lap and taking a frame every 0.7 seconds after the finish. Agent! picked frames by measuring them: the camera's position against the kart told it which shot each frame was, and pixel statistics weeded out dark or low-detail frames. As with the last post, it didn't look at them itself.

## Trying it

Clone [AgentiLoop/MarioKart64JS](https://github.com/AgentiLoop/MarioKart64JS), run `npm install && npm run dev`, open `http://localhost:5173` and press **3** on the title screen or in a race. The web build ships the 3D karts, Lakitu and the 3D title as well. The staged models live in `public/wii/`; `tools/build-wii-karts.py` and `tools/build-wii-lakitu.py` are the scripts that staged them from the Collada files.

*MarioKart64JS is a fan research project for testing how far AI can go in duplicating a game. Mario Kart 64 and Mario Kart Wii are © Nintendo, and their assets belong to Nintendo. The project isn't affiliated with or endorsed by Nintendo.*
