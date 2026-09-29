---
title: Before the Model Gets a Vote: Inside Agent!'s Shell Guardrails
description: How ShellSafetyService, the daemon-side re-check and the Jev second opinion stop an AI agent from wiping your Mac, walked through the actual Swift code.
tags: Security, Internals
---
This week, TechRadar reported that a coding agent deleted roughly 48,000 files in a short burst and then apologized. The apology changed nothing. The files were gone.

Agent! can run shell commands as you through a Launch Agent, and as **root** through a Launch Daemon. That's what makes it useful, since it can flash an SD card, fix permissions or clean a build folder. It also means "the model will probably be careful" is not a security model. So Agent! doesn't ask the model to be careful. It checks every command in code, before anything runs, in three layers.

## Layer 1: a hard-coded guardrail the model can't talk its way past

`ShellSafetyService` is a plain Swift `enum` in `Agent/Services/ShellSafetyService.swift`. The doc comment at the top sets the tone: it runs *before every execution surface* and rejects catastrophic commands *without dispatching them*. System prompts are called what they are: backstops, not the enforcement layer.

The entry point takes the command, the context it will run in, and the tab's project folder:

```swift
static func check(_ command: String,
                  context: Context = .userAgent,
                  projectFolder: String = "") -> Verdict
```

A `Verdict` is `allowed`, a human-readable `reason`, and a short `rule` id for the audit log. The reason is written for the model: it goes back as the tool result, so the LLM understands *why* it was refused and doesn't just retry.

### It reads compound commands the way a shell does

A naive filter checks the start of the string. Attackers and confused models don't cooperate with that. `check` splits the command on `;`, `&&`, `||`, `|` and newlines, then checks **each segment**. So `ls; rm -rf /` is blocked, even though the first half is harmless.

There's one deliberate exception to the ordering. The classic fork bomb, `:(){ :|:& };:`, *depends* on `;` and `|`, exactly the characters the splitter tears apart. So the fork-bomb check runs on the whole command before splitting.

### It strips the disguises

Before matching `rm`, a helper called `stripPrefixWrappers` peels off wrappers that don't change what a command does: `sudo`, `exec`, `command`, `builtin`, `eval` and `doas`. It also strips leading environment assignments like `FOO=bar`. That means `sudo rm -rf ~` and `FOO=1 exec rm -rf ~` hit the same rule as the bare command.

Flags are parsed rather than pattern-matched, too. `-rf`, `-fr`, `-Rf`, `-r -f`, `--recursive --force` all count, because the parser looks for an `r` and an `f` in any short-flag cluster, plus the long forms.

### What it refuses

These are the rule ids that appear in the source:

| Rule | What it stops |
|---|---|
| `rm.catastrophic` | `rm -rf` on `/`, a bare glob like `*` or `./*`, or your home directory in any spelling (`~`, `~/*`, `$HOME`, `${HOME}/*`, or the literal home path) |
| `rm.no-preserve-root` | `--no-preserve-root`, the explicit bypass for `/` protection |
| `rm.project-folder` | Recursively deleting the project folder the agent is working in, or globbing everything inside it. Deleting a named subfolder stays allowed. |
| `rm.dangerous-target` | Other dangerous `rm` targets on the user-level path |
| `fork-bomb` | Self-replicating process bombs |
| `mv.to-devnull` | "Deleting" files by moving them to `/dev/null` |
| `find.delete-broad-root` | `find … -delete` from a broad root |
| `perms.recursive-on-root` | Recursive permission changes on root-level paths |

The project-folder rule deserves a moment. It's the one that maps most directly to the incident above: an agent should never wipe the very project it was asked to work on, no matter how the request is phrased.

### Root is treated differently, on purpose

You might expect the root daemon to get the *strictest* rules. It gets the narrowest. The comment explains why: the daemon exists to do system-level work, like disk cloning or `mkfs`, and it "shouldn't fight us." So in `.rootDaemon` context, `check` skips straight to `checkCatastrophicRm`, which blocks only the three unrecoverable patterns (`/`, bare globs and home) plus `--no-preserve-root` and a project-folder wipe. Everything else is the operator's call.

That's a design choice worth copying. A guardrail that blocks legitimate admin work gets turned off. A guardrail that blocks only unrecoverable mistakes stays on.

## Layer 2: the daemon checks again

The app runs `ShellSafetyService.check` before it dispatches anything. The helpers don't take that on trust. In `Shared/DaemonCore.swift`, right after writing the audit-log entry, the daemon runs the **same check** on its own side:

```swift
// Defense-in-depth: the app already runs this same check before
// dispatching, but any same-team-signed client can reach the mach
// service directly.
let verdict = ShellSafetyService.check(
    script,
    context: auditCategory == .launchDaemon ? .rootDaemon : .userAgent,
    projectFolder: workingDirectory
)
```

A blocked command is logged as denied with its rule id and gets exit status 126. It never reaches `/bin/zsh`. This matters because the XPC listeners accept any client signed by the same team. If something else signed by that team connects to the mach service directly, it still hits the guardrail.

## Layer 3: Jev, a second opinion for what patterns miss

Pattern rules are precise, but they only know the patterns you wrote down. Plenty of destructive commands don't look like `rm -rf /`: a `truncate` on the wrong file, a SQL `DROP` piped into a CLI, a `dd` in the wrong direction.

That's the job of **Jev**, an optional advisory layer in `JevAdvisor.swift`. Every command that already *passed* `ShellSafetyService` goes to Jev, which rates how likely it is to irreversibly destroy data. Above your threshold, Agent! refuses with a clear message:

```text
Refused: Jev rated this command 85% likely to irreversibly destroy data.
Command: …
Narrow the target or run it yourself if this is intentional.
```

A few details show how carefully this was scoped:

- **It supplements, never replaces.** The code comment is explicit: `ShellSafetyService` is the enforcement layer, and Jev only catches what the pattern rules miss. That's why the threshold is deliberately high. It defaults to **70%**, and you can tune it from 0 to 100% in 10% steps in Settings.
- **It fails open, but loudly.** No key, the toggle off, or a network outage means "no opinion", so a flaky service can never stall your task. The failure is still logged (`⚠️ Jev check failed, command allowed`), so an expired key is never mistaken for "Jev says safe."
- **Cancel means cancel.** If you stop a task while Jev is thinking, the command doesn't run.
- **Every verdict is visible.** Each check logs the risk percentage, allowed or refused, the model that answered, and token counts.

## Tested, not assumed

`AgentTests/ShellSafetyServiceTests.swift` holds 30 tests for the guardrail. And because every helper command is written to the audit log before it runs, you can always reconstruct what the agent tried to do, including what it wasn't allowed to do.

## The takeaway for anyone building agents

1. **Enforce in code, not in the prompt.** Prompts are suggestions. A Swift `enum` isn't.
2. **Parse like the shell parses.** Split compound commands, strip wrappers, and normalize flags.
3. **Check again at the privileged boundary.** Don't trust your own client to be the only caller.
4. **Block the unrecoverable, not the unusual.** Narrow rules survive; noisy ones get disabled.
5. **Add judgment on top, and make it fail visibly.** A second opinion is valuable only if you can tell when it didn't answer.

All of this is in the open on [GitHub](https://github.com/AgentiLoop/Agent). Read it, poke holes in it, and open an issue if you find a command that should have been stopped.
