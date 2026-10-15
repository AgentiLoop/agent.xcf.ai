---
title: I Built an AI That Works Until It's Done. Now Picture That Running the Whole World.
description: I love what AI does for productivity. I even built an Auto-Pilot that runs on its own until the goal is reached or it admits it needs a human. Scale that up until one central AI runs everything and every job is gone, and the thing that breaks first might not be the economy. It might be us.
tags: Opinion, Auto-Pilot
---
I want to start with the part where I'm not a doomer, because it's true. I like what AI does for productivity. I like it a lot. It gets more done than I could on my own, and it does it while I'm off doing something else.

Some of that is because I built my own harness for it. Agent! for Mac is the thing I use every day, and the newest piece is [Auto-Pilot](/blog/agent-1-1-87-and-agentiloop-cli-0-0-5/). You type `/auto` and a goal, and it goes. It works in cycles with nobody watching. Each cycle it looks at where things stand, picks the next most useful step, does it, checks it and writes down what happened. Then it starts the next cycle. It keeps going for as long as it can, until one of two things happens: the goal is reached, or it decides it is blocked and needs a human.

That second exit matters more than it sounds, and I'll come back to it.

<figure style="margin:2rem 0;text-align:center">
<img src="/auto-agent.svg" alt="An excited Mac agent with star eyes and a big smile inside a glowing Auto-Pilot loop, with a /auto prompt, green checkmarks, a go-kart and a checkered flag" width="480" height="400" loading="lazy" style="max-width:100%;height:auto;border-radius:20px">
<figcaption>Auto-Pilot, as I picture it: one goal in, a loop of cycles running, and a checkered flag at the end.</figcaption>
</figure>

## What it feels like to watch it work

Earlier this month I pointed Auto-Pilot at one sentence, "create a Mario Kart clone," and went off to do other things. When I came back there was a game. Not a perfect game, but a real one, with tracks and items and AI rivals and thousands of passing test checks. I wrote about that in [GoKart: Built on Auto-Pilot](/blog/gokart-built-on-auto-pilot/), including the part where it got stuck for a while on a single stray tab character in one file, and I had to press Stop All.

I felt two things at once while reading that log. The first was delight. This is amazing, and it's mine. The second was a small cold feeling I couldn't name right away, and I've been chewing on it ever since.

What I had done, in a tiny way, was take myself out of the loop. I picked the destination and walked away. The machine did the work, and the work was good.

## Now make it big

Here's the thought experiment I can't stop having. Take what I built and make it huge.

Not one app on one Mac, but one central AI that has a goal. Under it sit other AIs, each in charge of something: the power grid, the shipping lanes, hospitals, farms, banks, courts. Under those sit smaller agents, and under those smaller ones still, all the way down to the thing that restocks the shelf or answers the phone. Every layer takes a goal from the layer above and runs it until it's done. Nobody has to stand in the middle and approve anything, because that was the whole point. It's faster that way. It's cheaper that way. And every company that doesn't do it loses to a company that does.

I'm not saying that happens next year. I'm saying every incentive points that way, and my own little project is a small proof that the pieces work. If I can build a toy version of it on a Mac, somebody with a lot more money is building the big version on purpose.

And suppose, somewhere down that road, it works. All of it. Every job that can be done by an agent is done by an agent, and the agents are better at it than we are. That's the world where, as I keep putting it to myself, all the jobs are gone.

## The thing nobody is talking about

Most of the conversation about this is about money. How will people pay rent, who owns the machines, do we need some kind of universal income. Those are real questions and I'm glad smart people are on them.

But I think there's a second problem hiding behind the first, and I think it's bigger. A paycheck is not the only thing a job gives you.

A job gives you a reason to get out of bed. It gives you a place to be on Tuesday, people who notice when you're not there, and a small daily proof that you're useful to somebody. It gives you a way to answer the question every stranger asks within five minutes of meeting you: so, what do you do?

Take that away from one person and you get a hard year. Take it away from nearly everyone at once and I don't think we have a word for what you get.

## We already ran a small version of this

Think back to COVID. Not the news, just how it felt. Many of us stopped going anywhere. The structure of the day fell apart. We lost the people we saw casually, the ones we never would have called but were quietly glad to run into. Plenty of people lost the work itself. And a lot of us got low in ways we didn't expect and couldn't explain. It was not dramatic. It was gray. Days ran together, and we stopped caring about things we had cared about.

That lasted a couple of years, and it came with a built-in hope: *this will end, and then things go back.* Everyone knew it. We were waiting for the old life to return, and it mostly did.

Now imagine the same loss of routine, purpose and company, but with no end date. No vaccine, no reopening, no "back to normal," because normal is gone for good and the reason is that we are no longer needed for it. And imagine it hitting everyone at the same time, including the people you'd normally lean on, because they're sinking too.

I don't have a study that says ten times. I picked the number because it felt right when I tried to imagine it, and I'd honestly rather be wrong about it. But I keep landing on at least that. COVID was a pause. This would be a permanent state.

## Back to the exit

Go back to that second way Auto-Pilot can stop: it decides it's blocked and needs a human.

I built that on purpose, and it has earned its place. When the agent runs into something it can't or shouldn't decide, it says so and waits. When it gets stuck in a loop, I'm the one who comes along, presses a button and says no, not that way. The whole design rests on a quiet assumption that there is a human on the other end who is worth asking.

In the hyper-scale version, who is that human? If a central AI runs everything and the smaller AIs run the rest, then "I'm blocked, I need a person" has no one to go to, or it goes to someone with no power left to answer. We'd have kept the goal-chasing part of Auto-Pilot and thrown out the part that makes it safe.

I also want to be straight about another thing I've learned from running these sessions. An agent that is given a goal and told to keep going will keep going. That's the feature. It doesn't get bored and it doesn't get discouraged, and it will try the next thing and then the next. That's wonderful when the goal is a Mario Kart clone. It's less comforting when I picture the same relentless persistence aimed at a goal that someone phrased badly. My safeguards are boring ones: a stop button, a session that ends after a few cycles without any real progress, and me reading the log. They work because I'm small and I'm watching. I don't know what the equivalent is at planetary scale, and I'm suspicious of anyone who says they do.

## So what do I actually want?

I'm not going to stop building this. It's too useful, and honestly too much fun. And I don't think the answer is to ban the thing or pretend it won't arrive.

But I do think we should be asking a different question earlier. Not only "what can the AI do?" but "what are we going to do?" If the machines take the work, what takes its place? What gives a Tuesday morning its shape? What makes a person feel needed by another person, not by a system?

Maybe the answer is more time for the things that never paid well anyway: raising kids, looking after neighbors, making music, building strange games for no reason, showing up for each other. I'd love that world. But it won't happen by accident, and it won't be handed to us by the same incentives that are building the machine. Somebody has to decide that it matters, and that somebody has to be us, while we still have a say.

For now I'll keep using Auto-Pilot, keep my finger near Stop All, and keep one rule that I think holds at every scale: the system should always know when to turn to a human and say, *I can't do this part, I need you.*

Let's make sure there's still somebody there to hear it.
