---
title: 六个月后，带着 Auto-Pilot 重返 Hacker News
description: Agent! 再次以 Show HN 的形式登上 Hacker News。四月那条帖子讲的是一个原生 Mac 编码工具；这一条讲的是 Auto-Pilot——一个以目标驱动、在目标达成之前持续运行周期的循环，以及它一直在开发的马里奥赛车风格游戏。这里是帖子全文、其中每一项说法背后的依据，以及参与讨论的入口。
tags: Auto-Pilot, 社区, Hacker News
---
Agent! 今天以 Show HN 的形式重返 Hacker News：[Show HN: AgentiLoop Agent Mac GUI Agent Loop for macOS 14.6 or Later](https://news.ycombinator.com/item?id=49948810)。如果你有 Hacker News 账号，那个帖子就是提问、挑刺、告诉我们你想从一个 Mac 代理那里得到什么的地方。本文是提交文字的加长版，并为其中的每一项说法附上了出处。

## 原始材料

提交内容很短，所以这里全文引用自[那条 Hacker News 条目](https://news.ycombinator.com/item?id=49948810)：

> Agent! 最初于去年四月出现在 Hacker News 上。从那以后变化很大。最近开发了一个名为 Auto-Pilot 的新功能。给它一个目标，它在目标达成之前不会停止。可以把它看作加强版的任务。Agent 做的事情是创建多个任务。每个任务被称为一个周期（Cycle）。默认情况下，由 auto [目标] 触发的 Auto-Pilot 没有时间限制。Agent! 被告知要一直运行，直到目标达成。Auto-Pilot 有一个紧急停止开关，即"Stop All"按钮。用户也可以用 auto stop 只终止当前周期，或者用 auto stop all 终止全部。到十一月，用户将能够在同一个项目上运行多个 Auto-Pilot。而且一个 Auto-Pilot 标签页将能够自动生成其他标签页。目前我们正在用 GoDot 4 开发一个类似马里奥赛车的克隆游戏，叫"GoKart"。到目前为止，已记录了超过 20 小时的游戏开发和改进时间。 *（译自英文）*

下面的每一节都展开了其中的一句话。

## "Agent! 最初于去年四月出现在 Hacker News 上"

第一条帖子是 2026 年 4 月 16 日的 [Agent — Native macOS coding IDE/harness](https://news.ycombinator.com/item?id=47787127)：83 分、54 条评论。当时的应用要求 macOS 26.4 和 Apple silicon，有 17 家 LLM 提供商，定位主要是一个编码工具，同时也能通过辅助功能 API 驱动 Mac 应用。两条帖子都列在本站的[评价](/#reviews)部分，与期间出现的独立评测并列。

四月以来：支持 macOS 14.6 和 Intel（[那次移植的故事](/blog/sonoma-intel-and-the-mac-that-was-not-dead-yet/)）、23 家提供商、[可以恢复的上下文压缩](/blog/context-compaction-half-the-window/)、面向 Mac、Windows 和 Linux 的 [Rust 与 Go CLI](/blog/agent-1-1-87-and-agentiloop-cli-0-0-5/)、每月一号发布一个版本，以及这次新提交真正要讲的功能。

## "给它一个目标，它在目标达成之前不会停止"

Auto-Pilot 就是 Agent! for Mac 中的 `/auto` 命令。按照 README 的 Auto-pilot 一节：它在主标签页或任意 LLM 标签页上以无人值守的周期运行任务循环，直到目标达成、时间预算用尽，或者你按下 Stop。没有周期数上限，也没有每周期的迭代上限。当一个周期的任务结束而目标尚未达成时，下一个周期会自动开始。

| 命令 | 作用 |
|---|---|
| `/auto <goal>` | 朝目标推进，直到 LLM 报告目标已达成 |
| `/auto 4h <goal>` | 同上，但 4 小时后停止（`30m`、`1.5h` 也可用） |
| `/auto` | 先审阅项目，再向你询问目标 |
| `/auto history`、`/auto last`、`/auto #N` | 列出以往的目标，重启最近一个或第 N 个 |
| `/auto status` / `/auto stop` | 显示当前会话，或在当前周期结束后终止它 |

"可以把它看作加强版的任务"是正确的思维模型。每个周期*就是*一个普通的 Agent! 任务，用同样的工具、同样的护栏（先读后改、goal_state 证据、shell 黑名单）和同样的 `done()` 约定。Auto-Pilot 增加的是围绕它的循环：周期的总结会追加到项目内的 `.agent/autopilot/progress.md`，并被送入下一个周期的提示中，因此每个周期一开始就会读到前面的周期做了什么、假设了什么、还有什么没做完。只有当 LLM 的最终总结以 `AUTOPILOT: GOAL REACHED` 开头时，会话才会结束。因错误或取消而完全没有总结的周期，永远不会结束会话；下一个周期只是等待更久——15 秒，然后 30 秒，然后 60 秒，最多五分钟。

"默认情况下……没有时间限制"是字面意思：不带时长的 `/auto <goal>` 会一直运行，直到目标达成或你停止它。如果想要一个上限，`/auto 4h <goal>` 就能给你一个。活动中的会话还能在应用重启后存活。退出或崩溃会暂停它们，下次启动时，每个会话都会在各自的标签页上以下一个周期恢复。

## "Auto-Pilot 有一个紧急停止开关"

有三种停止方式，它们的作用各不相同：

- **Stop All**（全部停止，即那个按钮）会结束所有标签页上的所有 Auto-Pilot 会话，并停止所有正在运行的任务。`RunStop.swift` 中的注释写得很明确：单任务停止（Esc 或停止按钮）会让 Auto-Pilot 继续运行；Stop All 则会结束它。
- **`/auto stop`** 在当前周期完成后结束会话，如果你正处于两个周期之间，则立即结束。当前周期被允许落地。
- **`/auto stop all`**（也可写作 `stopall` 或 `stop-all`）与按下 Stop All 相同，为不想伸手去拿鼠标的人准备。它在 `AutoPilot.swift` 中紧挨着 `/auto stop` 之前处理。

提交中把 `auto stop` 描述为"只终止当前周期"。更精确的说法是，它在当前周期之后结束*会话*；周期本身会运行到自然结束，正是这一点让进度日志和 git 历史保持干净。

## "到十一月……在同一个项目上运行多个 Auto-Pilot"

这是提交中属于路线图而非已发布功能的部分，值得把两者分清楚。截至今天，Agent 仓库的 main 分支上有一个提交，标题为 *Auto-Pilot: multiple tabs per project — per-tab progress, shared registry, auto/forced git worktree isolation, shared memory from worktrees*。那是基础工作：每个标签页保留自己的进度日志，标签页之间相互注册，当两个 Auto-Pilot 原本会编辑相同文件时，它们会获得各自独立的 git worktree。它尚未进入任何发布版本；它是在 1.1.87 标签之后合入的。版本在每月一号发布，所以 11 月 1 日的版本是它最早能到你手上的时间，而"能生成其他标签页的标签页"这部分，按提交所说，计划在同一时间窗口内完成。

## "一个类似马里奥赛车的克隆游戏，叫 GoKart"

GoKart 是 Auto-Pilot 大部分时间都在投入的项目。[之前的文章](/blog/gokart-built-on-auto-pilot/)直接根据进度日志，详细记录了第一个下午：第 1 周期装好 Godot 4，选择自定义街机物理而非 `VehicleBody3D` 以便对操控进行单元测试，第 2 周期做出漂移火花和加速模糊，第 3 周期做出一条赛道，第 4 周期做出道具，一次因多余的制表符而卡住，一次 Stop All，以及第二个会话为每次 shell 运行加上 `perl -e 'alarm'` 时间限制，随后一口气交付了十五项功能。

它没有停下来。[GoKart 仓库](https://github.com/AgentiLoop/GoKart)从 10 月 1 日 12:39 的第一次提交，到 10 月 3 日晚上已有 71 次提交。最近的提交读起来就像一份马里奥赛车 64 的清单：Sunset Speedway 上的奇诺比奥高速公路式车流、Green Hills 上的哞哞牧场式鼹鼠、带实时演示的标题画面、成绩板，以及 HUD 上绘制的道具窗口。每一项都附带自己的测试文件和一个 `tools/*_check.gd` 脚本，因为模型仍然看不到屏幕，必须用其他方式证明功能确实存在。提交中的"超过 20 小时"就是这些会话的挂钟总时长。如果你更想玩而不是读，[GoKart 0.0.1](https://github.com/AgentiLoop/GoKart/releases/tag/v0.0.1) 可供 macOS、Windows 和 Linux 下载。

## 可以在帖子里问什么

如果你是从 Hacker News 过来的，我们最希望在那里回答的问题是：

- Auto-Pilot 如何判定目标已达成，以及我们为什么让模型来宣布，而不是用固定指标。
- 当一个周期出错时会发生什么，以及为什么 git 才是真正的撤销。
- 在你的 Mac 上跑一个无人值守的循环到底是不是个好主意，以及护栏对此做了什么。

帖子地址是 [news.ycombinator.com/item?id=49948810](https://news.ycombinator.com/item?id=49948810)。带有 Auto-Pilot 的 Agent! 1.1.87 在[发布页面](https://github.com/AgentiLoop/Agent/releases/latest)和 Homebrew 上均可获取：`brew install --cask agentiloop-agent`。
