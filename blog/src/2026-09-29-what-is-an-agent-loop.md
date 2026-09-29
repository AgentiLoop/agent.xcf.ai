---
title: What Is an Agent Loop? A Robot, a Sandwich, and the Art of Trying Again
description: Look, choose, act, check. A playful, illustrated guide to agent loops—simple enough for a five-year-old, with plenty for the grown-ups.
tags: Explainers, Agent Loops
---
Imagine a little robot named Pip.

You say, **“Please make me a jam sandwich.”**

Pip looks at the table. There is bread. There is jam. There is a spoon wearing a suspicious amount of peanut butter.

Does Pip announce, “Sandwich complete!”?

No. That would be a speech, not a sandwich.

Pip needs to **look, choose a small step, do it, and check what happened**. Then Pip can decide what to do next.

That repeating pattern is an **agent loop**.

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 360" role="img" aria-labelledby="pip-title pip-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="pip-title">Pip has a goal, but not yet a sandwich</title>
<desc id="pip-desc">A friendly blue robot looks at two slices of bread and a jar of jam. A speech bubble says: A plan is not a sandwich.</desc>
<rect width="760" height="360" rx="20" fill="#eef6ff"/>
<rect x="265" y="28" width="450" height="76" rx="24" fill="#fff" stroke="#b6c8e4" stroke-width="3"/>
<path d="M300 104l-26 24 58-24" fill="#fff"/>
<text x="490" y="75" text-anchor="middle" font-family="system-ui,sans-serif" font-size="27" font-weight="700" fill="#173452">A plan is not a sandwich.</text>
<path d="M44 282H716" stroke="#8b684c" stroke-width="13" stroke-linecap="round"/>
<rect x="77" y="127" width="140" height="115" rx="27" fill="#559ef5" stroke="#173452" stroke-width="4"/>
<path d="M147 127V100" stroke="#173452" stroke-width="5"/><circle cx="147" cy="91" r="10" fill="#efb943"/>
<circle cx="117" cy="168" r="12" fill="#fff"/><circle cx="177" cy="168" r="12" fill="#fff"/>
<circle cx="120" cy="169" r="5" fill="#173452"/><circle cx="180" cy="169" r="5" fill="#173452"/>
<path d="M121 201Q147 222 173 201M103 242V276M187 242V276M217 213L260 233" fill="none" stroke="#173452" stroke-width="6" stroke-linecap="round"/>
<path d="M328 260V217Q309 186 349 178Q380 168 402 187Q422 175 445 190Q472 205 449 223V260Z" fill="#fbe3ad" stroke="#ae703f" stroke-width="6"/>
<path d="M353 240V212Q389 190 428 212V240Z" fill="#d94877"/>
<path d="M465 263V225Q449 195 483 187Q517 172 547 191Q578 181 590 211L582 263Z" fill="#fbe3ad" stroke="#ae703f" stroke-width="6"/>
<rect x="622" y="191" width="60" height="82" rx="12" fill="#d94877" stroke="#173452" stroke-width="3"/>
<rect x="617" y="181" width="70" height="15" rx="5" fill="#173452"/>
<text x="652" y="239" text-anchor="middle" font-family="system-ui,sans-serif" font-size="17" font-weight="700" fill="#fff">JAM</text>
<text x="147" y="326" text-anchor="middle" font-family="system-ui,sans-serif" font-size="21" fill="#173452">Meet Pip.</text>
<text x="495" y="326" text-anchor="middle" font-family="system-ui,sans-serif" font-size="21" fill="#173452">The goal: one jam sandwich.</text>
</svg>
<figcaption>Pip is our imaginary helper. No actual robots were made sticky while drawing this illustration.</figcaption>
</figure>

## The whole idea, in four little words

**Look. Choose. Act. Check.**

- **Look:** What is happening right now?
- **Choose:** What is one useful thing to do next?
- **Act:** Do that thing.
- **Check:** What actually happened? Are we finished?

If the job is not finished, go around again—with the new information.

A **loop** just means something repeats. An **agent** is a system that can take steps toward a goal, using the tools and permissions it has been given.

Put them together: **an agent loop lets a helper act, see the result, and decide what comes next.**

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 520" role="img" aria-labelledby="loop-title loop-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="loop-title">Look, choose, act, check—and know when to stop</title>
<desc id="loop-desc">A flow diagram runs clockwise from Look to Choose to Act to Check. Check returns to Look when more work is needed. A separate arrow leads from Check to Stop or ask when finished, blocked, or out of budget.</desc>
<defs><marker id="loop-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0L10 5 0 10Z" fill="#4b617e"/></marker></defs>
<rect width="760" height="520" rx="20" fill="#f0f5fb"/>
<g fill="none" stroke="#4b617e" stroke-width="4" marker-end="url(#loop-arrow)"><path d="M298 100H460"/><path d="M586 150V238"/><path d="M464 290H302"/><path d="M176 240V153"/><path d="M176 342V414"/></g>
<g stroke-width="3"><rect x="54" y="48" width="244" height="100" rx="23" fill="#d7eaff" stroke="#3377b9"/><rect x="464" y="48" width="244" height="100" rx="23" fill="#fce9b6" stroke="#9a701b"/><rect x="464" y="242" width="244" height="100" rx="23" fill="#dfd9ff" stroke="#7760b5"/><rect x="54" y="242" width="244" height="100" rx="23" fill="#cff3e4" stroke="#29836a"/><rect x="54" y="419" width="652" height="68" rx="20" fill="#fff" stroke="#4b617e"/></g>
<g font-family="system-ui,sans-serif" text-anchor="middle" fill="#173452"><g font-size="28" font-weight="700"><text x="176" y="90">1. LOOK</text><text x="586" y="90">2. CHOOSE</text><text x="586" y="285">3. ACT</text><text x="176" y="285">4. CHECK</text></g><g font-size="20"><text x="176" y="122">What do I see?</text><text x="586" y="122">What next?</text><text x="586" y="317">Use a tool.</text><text x="176" y="317">What changed?</text><text x="380" y="199">More to do? Go again.</text><text x="428" y="389">Done, blocked, or at the limit?</text><text x="380" y="461" font-size="24" font-weight="700">STOP—or ask a person.</text></g></g>
</svg>
<figcaption>A teaching diagram, not a required software design. Real implementations can combine these stages. The important part is feeding the result back into the next decision.</figcaption>
</figure>

## Back to the very serious sandwich mission

Pip's first small step is to open the jam jar.

**Act:** Turn the lid.

**Check:** The lid did not move.

Here is the interesting bit. Pip should not pretend the jar opened just because opening it was the plan.

And Pip should not keep turning forever until the sun becomes a raisin.

Pip could try a permitted alternative, or say, “Could you help me with this lid?” Asking for help is a useful outcome—not a robot-sized failure.

Once the jar is open, Pip can spread the jam, put the bread together, and check the result against your request.

Two slices? Jam inside? On a plate? Great.

A jar balanced on a loaf? Creative. Not a sandwich.

## Where does the AI part fit?

Our kitchen story is pretend. A software agent's tools might read a file, search a page, edit a document, or run a test instead of handling bread.

In an AI agent, a language model can help choose the next step. The surrounding software runs permitted tool calls and returns their results. The model then gets another turn with that information.

Think of three different jobs:

| Part | Pip's pretend kitchen | Software version |
| --- | --- | --- |
| Goal | Make a jam sandwich | Fix a broken link |
| Decision-maker | Choose the next small step | Model proposes an action |
| Tool | Hands and spoon | File reader, editor, or browser |
| Observation | The lid is still closed | Tool returns an error or result |
| Working notes | Jar open; bread ready | Relevant task history and results |
| Finish check | The requested sandwich is ready | Verify the intended link works |

**A model suggesting an action is not the same as that action happening.** And an action happening is not automatically the same as the goal being met.

“Saved the file” and “saved the correct file with the correct contents” are different claims. The check is where that difference matters.

## A tiny adventure: the missing picture

Suppose you ask a software helper to fix a missing picture on a web page.

A useful loop could look like this:

1. **Look:** Read the page and identify the image path.
2. **Choose:** Check whether the referenced image exists.
3. **Act:** Inspect the relevant files.
4. **Check:** The page requests `cat.png`, but the file is named `cat.jpg`.
5. **Go again:** Update the reference, then check that the page loads the intended picture.
6. **Stop:** Report the change and the checks actually performed.

If the picture still does not appear, “I edited the page” is not enough. The result should guide the next step.

Notice what makes this a loop: **the next action depends on what the previous action revealed.** It is not merely doing the same thing repeatedly.

## Does every lap make things better?

No. More activity does not automatically mean more progress.

Here is a made-up graph for Pip's sandwich mission. We give Pip one point for each completed milestone: jar open, jam spread, sandwich assembled, and the final request checked.

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 450" role="img" aria-labelledby="graph-title graph-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="graph-title">An imaginary sandwich progress graph</title>
<desc id="graph-desc">Across six attempts, completed milestones are zero, zero, one, two, three, and four. The first two attempts make no progress because the jar is stuck. These invented numbers illustrate feedback, not measured agent performance.</desc>
<rect width="760" height="450" rx="20" fill="#f0f5fb"/>
<g font-family="system-ui,sans-serif" fill="#173452"><text x="48" y="42" font-size="23" font-weight="700">Progress is not the same as busyness.</text><text x="48" y="73" font-size="18">Completed milestones · invented example, not a benchmark</text></g>
<g stroke="#c2cedd" stroke-width="1"><path d="M95 335H690M95 280H690M95 225H690M95 170H690M95 115H690"/></g>
<path d="M95 105V345H700" fill="none" stroke="#4b617e" stroke-width="3"/>
<polyline points="115,335 225,335 335,280 445,225 555,170 665,115" fill="none" stroke="#227657" stroke-width="5" stroke-linejoin="round"/>
<g fill="#227657" stroke="#fff" stroke-width="3"><circle cx="115" cy="335" r="8"/><circle cx="225" cy="335" r="8"/><circle cx="335" cy="280" r="8"/><circle cx="445" cy="225" r="8"/><circle cx="555" cy="170" r="8"/><circle cx="665" cy="115" r="8"/></g>
<g font-family="system-ui,sans-serif" font-size="20" fill="#173452" text-anchor="middle"><text x="68" y="341">0</text><text x="68" y="286">1</text><text x="68" y="231">2</text><text x="68" y="176">3</text><text x="68" y="121">4</text><text x="115" y="375">1</text><text x="225" y="375">2</text><text x="335" y="375">3</text><text x="445" y="375">4</text><text x="555" y="375">5</text><text x="665" y="375">6</text><text x="390" y="418">Attempts</text></g>
<g font-family="system-ui,sans-serif" font-size="19" fill="#173452"><text x="116" y="292">Stuck lid!</text><text x="326" y="317">Help worked.</text><text x="586" y="99">Checked!</text></g>
</svg>
<figcaption>Imaginary data: 0, 0, 1, 2, 3, 4 completed milestones. Real work can stall, go backward, or turn out to be impossible with the available tools.</figcaption>
</figure>

The flat bit matters. If nothing changes, the helper needs to notice—not celebrate how many times it has tried.

For grown-ups, that suggests useful questions: Did we learn anything? Did the state change? Are we repeating the same failed action? Is another attempt worth its cost?

For everyone else: **if the door says PULL, pushing harder is not a strategy.**

## Give the helper a fence, not the whole planet

A sensible agent design needs more than a repeat button.

- **A clear finish line.** “Find three pictures of penguins” is easier to check than “make everything amazing.”
- **Appropriate permissions.** Being able to draft an email should not automatically mean being allowed to send it.
- **A stopping budget.** Put limits on attempts, time, or spending. A stuck task must not become an endless task.
- **A way to ask.** Missing information, missing access, or a consequential choice can call for a person.
- **Honest checks.** Use evidence suited to the goal. Do not turn “the tool returned” into “everything is correct.”

These are design principles, not a promise that every product implements them. A loop does not magically make a system safe or reliable.

In Pip's kitchen: make the sandwich, do not order a truck full of jam, and ask before using the grown-up appliances.

## Is an agent loop the same as a script?

Not necessarily—but the boundary is not “scripts are silly, agents are smart.” Scripts can have loops, conditions, and excellent checks too.

The distinction worth watching is **how the next action gets chosen**. In a fixed workflow, the developer has laid out the routes in advance. In a model-driven agent loop, the model can choose among available actions based on the task and the latest observations. Real systems can mix both approaches.

For a predictable job, a small script may be exactly right. You do not need a philosophical robot to ring a bell at noon.

For a task with unknown obstacles, choosing the next step from fresh evidence can be useful. That flexibility also makes limits and verification important.

## The fridge-magnet version

An agent loop is:

> Try a useful step. See what happened. Use what you learned. Repeat only while it makes sense.

It is not magic. It is not a guarantee. It is not “keep going forever.”

It is a way to connect **a goal, an action, and the real result**—again and again, until the helper is finished or needs to stop.

Pip would explain it more simply:

**“Look. Try. Check. And don't say sandwich until there's a sandwich.”**
