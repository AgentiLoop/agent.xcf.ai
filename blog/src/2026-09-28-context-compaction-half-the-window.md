---
title: Why Agent! Compacts at Half the Window, and the Three Bugs That Shrank It to 16K
description: How Agent!'s context compaction decides when to summarize a long task, and the September 28 fixes for fallback models, Ollama and a 272K Codex window.
tags: Internals, Release Notes
---
Long agent tasks have a physics problem. Every tool call adds its output to the transcript: a file read, a build log, a diff. Eventually the transcript won't fit in the model's context window, and the provider rejects the request. An agent that runs overnight has to **compact**. It shrinks the conversation while keeping what matters.

Compaction lives in `Agent/AgentViewModel/Messages/Compression.swift`. On September 28, it got three fixes in one evening, all for the same symptom: tasks compacting at 16K tokens on models with far bigger windows. Here's how the system works, and what went wrong.

## When to compact: half the window, capped

The trigger is a struct called `CompactionState`. Its core is a single function:

```swift
static func threshold(for contextWindow: Int, maxTokens: Int = 0) -> Int {
    let byFraction = Int(Double(min(contextWindow, compactionWindowCap)) * compactionFraction)
    let reservedOutput = maxTokens > 0 ? min(maxTokens, contextWindow / 2) : 8_192
    return max(2_000, min(byFraction, contextWindow - reservedOutput))
}
```

With `compactionFraction = 0.5` and `compactionWindowCap = 256_000`, that reads:

- **Compact at 50% of the window.** It's a percentage rather than a fixed token count. The other half is the output budget, so input plus output always fit.
- **Never above 128K.** Windows advertised above 256K (Claude 1M, MiniMax 1M, Gemini and Grok 2M) all compact at 128K. A 200K window compacts at 100K.
- **Always leave room for the reply.** The threshold can't be so late that the reserved output no longer fits.
- **Never below 2K**, as a floor for tiny local models.

Why cap a 2M window at 128K? The comment is blunt. On huge advertised windows, an uncapped percentage delays compaction so long that any provider-side discrepancy turns into a hard context overflow instead of a compaction. Examples include a router serving a shorter window than it reports, or a system prompt counted wrong. Compacting early costs a summary. Compacting too late costs the task.

## Measuring: trust the provider, then estimate

To compare against the threshold, you need a token count. Guessing from characters is noisy, so `measuredTokens` prefers the truth: the `input_tokens` the provider reported for the last request. That number counts the system prompt and tool schemas, which a local estimate can't see. Only messages appended *since* that report get estimated.

Without a report, it falls back to the classic characters ÷ 4 estimate, inflated by 25%, because dense code runs closer to 3.3 characters per token. Before paying for a compaction on an estimate alone, the loop confirms with an on-device counter.

## How it compacts: tiers

When the threshold trips, `tieredCompact` works through escalating steps:

1. **Tier 0: a structured summary** of the *full* transcript by the active model. It runs first so the summarizer still sees the tool output it's summarizing.
2. **Microcompact:** old tool results become short, recoverable stubs. The `restore_tool_result` tool can bring any of them back.
3. **Image strip:** screenshots are huge and don't summarize well.
4. **Tier 1: Apple Intelligence summarization,** fast and on-device.
5. **Tier 2: aggressive prune,** folding middle messages into a summary.

One comment captures the philosophy: structural compaction "is a safety mechanism, not a feature." It runs even if you turn Token Compression off. Only the Apple Intelligence tier respects that toggle.

After compaction, the model gets back what it would miss most. That includes open goal criteria, the active plan checklist, and the current contents of up to five files it edited during the task (about 10K tokens in total). The read-dedup cache is reset too, so re-reading a file is allowed again.

Finally, there's a **circuit breaker**. After three compactions in a row that fail to shrink the transcript, the loop stops trying. But it doesn't give up for good: once the transcript grows another 25% past the last failed attempt, it tries again.

## The bugs: three roads to 16K

Every fix on September 28 ended in the same number. A 32K fallback window gives `min(16K, 32K − 8K) = 16K`. For a 200K+ model, compacting at 16K means summarizing almost constantly and forgetting files the model just read.

### 1. The fallback model borrowed the wrong window

Agent! supports a fallback chain. If a provider returns a 429, times out or drops off the network, the task continues on the next configured provider. Tabs can also override the model. But `contextWindow(for:)` looked up the window for the provider's *globally selected* model, not the one actually running. For a fallback model with no entry, it dropped to the 32K static size.

The fix adds the model to the lookup:

```swift
func contextWindow(for provider: APIProvider, model: String? = nil) -> Int
```

Every call site now passes the model in use: the main loop, tab tasks, the fallback path and sub-agents.

### 2. Ollama forgot what it had learned

Local servers report their real per-model window asynchronously: Ollama through `/api/show`, LM Studio through `/api/v0/models`, and vLLM through `/v1/models`. That's why the loop calls `refreshThreshold` on every iteration after the first. A fetch that lands after the task starts still takes effect.

On Ollama, though, the fetched windows weren't persisted, so compaction kept defaulting to 16K. The fix persists fetched context windows and fetches at task start when the window is unknown. It shipped with a new `OllamaContextWindowTests.swift` suite.

### 3. A generous output budget ate the input budget

This one is subtle. Codex reports a 272K window for its GPT-6 Astra model. A user sets **Max Output Tokens** to 256K. The old code reserved the full output budget:

```text
272K − 256K = 16K   →   threshold = min(128K, 16K) = 16K
```

The new code reserves at most half the window for output:

```swift
let reservedOutput = maxTokens > 0 ? min(maxTokens, contextWindow / 2) : 8_192
```

The same case now gives `min(128K, 272K − 136K) = 128K`. The percentage cap still uses the capped window, but the output-fit check uses the *true* window. Otherwise Claude's default 500K output budget on a 1M window would turn `window − maxTokens` negative and floor the threshold at 2K.

## Why this matters to you

If you run long tasks, especially overnight coding runs, on fallback providers or local models, those tasks should now keep much more working context. That means fewer "I need to re-read that file" loops, fewer lost details, and fewer tokens spent summarizing. These fixes shipped on September 28 alongside Version 1.1.77 (build 277), release candidate 6, together with cross-provider detection of context-overflow and `max_tokens` errors.

The lesson for agent builders is general: **size your memory from the model that's actually running**, trust the provider's token counts over your own estimates, and cap every budget so no single setting can starve the others.
