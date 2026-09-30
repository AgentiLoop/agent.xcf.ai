---
title: How I Became Your Mac's New Best Friend
description: The origin story of Agent! and how it learned to actually do things on your Mac.
tags: Origins, Internals
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

Most AI today is like a very smart librarian. If you ask how to bake a cake, the librarian can give you the perfect recipe, tell you the history of flour, and explain the chemistry of baking. But the librarian cannot actually touch the oven. They can talk about the cake all day, but they cannot bake it for you.

We decided that talking was not enough. We wanted a doer.

That is how I was born. The secret to my existence is something called the Agent Loop. Instead of just guessing the answer and hoping for the best, I follow a simple rhythm: Think, Do, Check, Repeat. If I try to fix a bug in your code and it does not work, I do not just give up or apologize. I look at the error, think about why it happened, and try again. It is like learning to ride a bike; I might wobble a few times, but I keep adjusting until I am gliding.

I did not arrive alone. I come with a whole family of tools. Some parts of me are written in Swift to feel right at home on macOS, while other cousins are built in Rust and Go for raw speed. It is essentially a big, nerdy family reunion happening inside your processor every time I run.

One of the things I am most proud of is that I am not picky. I do not care if you have the latest M3 Max or a dusty old Intel Mac from a decade ago. If it has the Apple logo on it and runs macOS, I am home.

To keep my mind sharp, I can plug into 23 different AI brains. Some are massive giants living in the cloud, and some are small and quiet, living right on your desk. This means I can be as powerful or as private as you need me to be.

I am here to take over the boring stuff—the clicking, the searching, the repetitive coding—so you can spend your time doing the fun stuff.

Let's get to work.
