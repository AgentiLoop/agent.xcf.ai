---
title: AgentiLoop Racing, Prototype III: an F1 Simulator in Your Browser
description: AgentiLoop Racing is an open-wheel racing simulator that runs in the browser, built with Agent! in Three.js. It has 240 Hz physics, 18 real circuits, an AI field, pit stops, tyre compounds, fuel, ERS and DRS. Play it at f1.gokart.games.
tags: Showcase, JavaScript
---
<figure style="margin:2rem 0">
<img src="/agentiloop-racing-og.jpg" alt="AgentiLoop Racing: an open-wheel race car on track in the browser simulator." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>AgentiLoop Racing, Prototype III. Every car on the grid is a 2026 RB22 model, repainted in its own colours and sponsor names.</figcaption>
</figure>

**Play it now: [f1.gokart.games](https://f1.gokart.games).** No download, no install. It needs a WebGL browser and plays with a keyboard or an Xbox (or other standard) controller.

AgentiLoop Racing is an F1-style racing simulator written in plain JavaScript and Three.js. The first commit, a deterministic four-wheel vehicle model, went in on the evening of October 16. Three days and 109 commits later it races a full AI field on 18 real circuits, with pit stops, tyre compounds, fuel, ERS and DRS, engine sound made from the physics, and a cockpit camera whose mirrors show the cars behind you. Agent! wrote it, one small, tested commit at a time.

One honest label up front, the same one the README carries: it is a **prototype, not a validated Formula 1 simulator**. The car's parameters are illustrative assumptions, not measured F1 data.

## Physics first

The project started as a physics testbed and the 3D came second. `physics.mjs` steps the car at a fixed **240 Hz**. Each wheel has its own inertia and its own slip, and each tyre has a grip envelope that goes from peak grip to sliding, slip-angle relaxation, temperature and wear. The sprung body rolls, pitches and squats under aero load, and you can see it on the 3D car. The gearbox is automatic or paddle-shift, and there is a guarded reverse gear for when you end up facing a wall.

The power unit is modelled too. Fuel is carried as real mass, so the car gets lighter as it burns off. The hybrid deploys up to 120 kW above 100 km/h, within 4 MJ a lap, and harvests under braking.

The test suite is Node's built-in test runner and nothing else: `node --test` runs 158 tests today, all passing. They check things like a car at full throttle never tunnelling through a wall, and the 3D model touching the ground only with its tyres and plank.

## 18 real circuits

<figure style="margin:2rem 0">
<img src="/agentiloop-racing-monza.jpg" alt="AgentiLoop Racing: a race at Monza against the AI field." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>A race at Monza. The timing box, the standings and the minimap are live during the race.</figcaption>
</figure>

Besides a fictional stadium test track there are 18 real circuits, from Bahrain to Miami, including Monza, Silverstone, Spa and Monaco, with layouts built from real car positions. Real data tuned the rest:

- **DRS zones** come from 2024 race telemetry (OpenF1): where drivers actually opened and closed the flap. Monaco gets one zone, on the pit straight.
- **Grip was calibrated against real corner speeds.** Over the 18 circuits the gap between the autopilot's laps and the fastest real race laps went from 17.9% to 5.8%. At Monaco the autopilot's lap went from 84.2 s to 74.4 s, against a real 73.9 s.
- **Tight corners were opened up** to a minimum radius of 15 m, so the cars can make Monaco's Ste Devote.
- **Every circuit has a pit lane** beside the start/finish straight, with an 80 km/h limit and a box for each car.

<figure style="margin:2rem 0">
<img src="/agentiloop-racing-monaco.jpg" alt="AgentiLoop Racing: a race at Monaco." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Monaco, raced with the AI field.</figcaption>
</figure>

## Racing the AI

A real circuit opens as a solo time trial; press **O**, or add `?race` to the URL, to race the field. The start is five red lights, one a second, then a random hold before they go out. Move more than half a metre early and it's a 5-second jump-start penalty. While the lights are on, keys **1–5** put you in the car on that grid slot.

The AI cars follow the racing line, tow each other down the straights, pull out of the slipstream, use DRS when they're within a second at the detection point, and dive down the inside under braking. In the commit that tuned overtaking, 3-lap races on all 18 circuits went from 16 passes to 34 and from 8 contacts to none. A car that ends up stuck against a barrier selects reverse, backs out along a path checked for traffic and walls, and rejoins.

Race rules apply. Every finisher has to run two tyre compounds, so you have to stop once or be disqualified. **B** asks the crew for softs, mediums or hards. Speed in the pit lane and it's +5 s.

Every session starts on autopilot, so the car drives itself until you take over. Press **P**, touch a gamepad or shift gear, and it's yours.

## The car and the cockpit

Every car on the grid uses a 2026 RB22 model by Tyler_Dave (CC BY 4.0, from Sketchfab). At load time `rb22.mjs` repaints it in each car's colours and projects the project's sponsor names and a race number onto it. Up close, each part of the model is subdivided and smoothed, with lower-detail versions further away.

Press **C** for the cockpit. The driver's eye rides on the sprung body, so roll, pitch and heave move the view, and the head moves a little with g-forces. The mirrors render the scene reflected through each glass, with your own rear tyres left out so you see the track and the cars behind.

Sound is synthesised from the physics too: a V6 firing note that follows the revs, turbo whine, tyre squeal from slip and wind noise that grows with speed.

<figure style="margin:2rem 0">
<img src="/agentiloop-racing-spa.jpg" alt="AgentiLoop Racing: a time trial at Spa-Francorchamps." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>The Spa time trial.</figcaption>
</figure>

## Watch it

<figure style="margin:2rem 0">
<div style="position:relative;padding-top:56.25%;border-radius:20px;overflow:hidden">
<iframe src="https://www.youtube-nocookie.com/embed/2RluAIH3iQw?rel=0&amp;modestbranding=1&amp;color=white" title="AgentiLoop Racing — F1 simulator built with AgentiLoop.ai in Three.js" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="position:absolute;inset:0;width:100%;height:100%;border:0"></iframe>
</div>
</figure>

## Try it

- [A race at Monza](https://f1.gokart.games/?track=monza&race)
- [The Spa time trial](https://f1.gokart.games/?track=spa)
- [A 5-lap race at Spa on softs](https://f1.gokart.games/?track=spa&race&laps=5&tyre=soft)

The source is at [AgentiLoop/F1](https://github.com/AgentiLoop/F1). It has no npm dependencies and no bundler: Three.js is vendored, so `python3 -m http.server` in the folder is enough to run it locally. The site itself is a Cloudflare Worker that serves the repository as static files.

*AgentiLoop Racing is an independent project and isn't affiliated with Formula 1, the FIA or any team. The 3D models keep their own licences; see `models/CREDITS.md` in the repository.*
