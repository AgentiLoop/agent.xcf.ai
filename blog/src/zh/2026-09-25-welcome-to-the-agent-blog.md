---
title: 欢迎来到 Agent! 博客：一个应用，任意 AI，全面掌控你的 Mac
description: AgentiLoop Agent! 是什么、我为什么这样打造它，以及你能在这里读到什么——一切都直接来自源代码。
tags: 公告, 架构
---
<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 340" role="img" aria-labelledby="map-title map-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="map-title">一台小小的 Mac 递给你一张地图</title>
<desc id="map-desc">一台面带微笑的 Mac 站在桌上，手里拿着一张展开的地图。地图上有四个站点，由一条虚线小路连接：任意 AI、循环、AgentScript 和安全。</desc>
<rect width="760" height="340" rx="20" fill="#eef6ff"/>
<path d="M30 290H730" stroke="#8b684c" stroke-width="10" stroke-linecap="round"/>
<rect x="132" y="228" width="16" height="52" fill="#8a97a8"/><rect x="100" y="276" width="80" height="12" rx="4" fill="#8a97a8"/>
<rect x="40" y="100" width="200" height="130" rx="14" fill="#c9d3df" stroke="#173452" stroke-width="4"/>
<rect x="54" y="114" width="172" height="102" rx="6" fill="#559ef5"/>
<circle cx="110" cy="152" r="9" fill="#fff"/><circle cx="170" cy="152" r="9" fill="#fff"/>
<circle cx="112" cy="153" r="4" fill="#173452"/><circle cx="172" cy="153" r="4" fill="#173452"/>
<path d="M115 180Q140 198 165 180" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
<path d="M228 180Q262 176 290 160" fill="none" stroke="#173452" stroke-width="6" stroke-linecap="round"/>
<path d="M290 50L400 70L510 50L620 70V260L510 240L400 260L290 240Z" fill="#fff8e6" stroke="#8b684c" stroke-width="4" stroke-linejoin="round"/>
<path d="M400 70V260M510 50V240" stroke="#e6d6b3" stroke-width="3"/>
<path d="M350 175C380 140 410 140 440 140S490 190 520 190 560 130 580 110" fill="none" stroke="#d94877" stroke-width="4" stroke-dasharray="3 10" stroke-linecap="round"/>
<circle cx="350" cy="175" r="11" fill="#559ef5" stroke="#173452" stroke-width="3"/>
<circle cx="440" cy="140" r="11" fill="#7b6ad6" stroke="#173452" stroke-width="3"/>
<circle cx="520" cy="190" r="11" fill="#22c55e" stroke="#173452" stroke-width="3"/>
<circle cx="580" cy="110" r="11" fill="#f59e0b" stroke="#173452" stroke-width="3"/>
<g font-family="system-ui,sans-serif" text-anchor="middle" fill="#173452">
<text x="350" y="152" font-size="15" font-weight="700">任意 AI</text>
<text x="440" y="117" font-size="15" font-weight="700">循环</text>
<text x="520" y="222" font-size="15" font-weight="700">AgentScript</text>
<text x="580" y="90" font-size="15" font-weight="700">安全</text>
<text x="345" y="88" font-size="14" fill="#8b684c">你的地图</text>
<text x="140" y="322" font-size="18">Mac 版 Agent!</text>
</g>
</svg>
<figcaption>每个博客都需要第一篇文章。这一篇，就是地图。</figcaption>
</figure>

你好，我是 Todd。我在开发 **AgentiLoop Agent!**，一款原生 macOS AI 智能体，而这里就是它的博客。

我一直想要一个地方，来聊聊 Agent! 里那些塞不进 README 或发布说明的部分：某条安全护栏为什么长成这个样子；智能体循环为什么要检查自己的工作；某个候选版本里出了什么问题，我们又是怎么修好的。你在这里读到的大部分内容都直接来自代码库，因为那是我最熟悉的东西。时不时地，我也会把目光投向更广阔的 AI 智能体世界，聊聊它对你的 Mac 意味着什么。

如果你是第一次来，就从这里开始吧。把这篇文章当作一张地图。

## Agent! 是什么

Agent! 是 100% 原生的 Swift 和 SwiftUI 应用。你输入（或说出）想做的事，它就会直接在你的 Mac 上把活干完，而不只是告诉你该怎么做：

- **它真的会写代码。** 它会读取你的项目，用字符串替换式的 diff 编辑文件，在 Xcode 中构建，读取报错并修复，最后用 git 提交。
- **它能驱动任意 Mac 应用。** 靠的是辅助功能（Accessibility）API，外加 AppleScript、JXA 和 51 个 ScriptingBridge 应用桥接。
- **它能以你的身份或 root 身份运行 shell 命令。** 这通过一个 Launch Agent 和一个 Launch Daemon 实现，二者用 SMAppService 注册，经由 XPC 访问。
- **它支持 23 家 LLM 提供商**，外加设备端的 Apple Intelligence：Claude、Codex、OpenAI、Gemini、Grok、Mistral、DeepSeek、Qwen、Z.ai、OpenRouter、Ollama、vLLM、LM Studio 等等。
- **它会倾听。** 说一声 *"Agent!"* 再接上任务，或者在 iPhone 上通过 iMessage 给它发消息（仅限已批准的发送者）。

README 用一句话就概括了它：*Siri 负责回答，Agent! 负责行动。*

## 没有 NPM，没有 Electron

这一点总让人意外。没有 Electron 外壳，没有 Node 运行时，也没有 `node_modules` 文件夹悄悄吃掉你的磁盘。Agent! 依赖的每一个 Swift 包都是我亲手写的，而且各自放在 [AgentiLoop](https://github.com/AgentiLoop) 组织下的独立仓库里：

| 包 | 职责 |
|---|---|
| AgentTools | 工具 schema、系统提示词和提供商管理 |
| AgentLLM | LLM 提供商协议、类型和注册表 |
| AgentMCP | MCP 客户端（stdio 和 HTTP） |
| AgentAccess | 辅助功能自动化 |
| AgentEventBridges | 面向 50 多款 Mac 应用的 ScriptingBridge 协议 |
| AgentD1F | 多行 diff 引擎 |
| AgentSwift | 基于 SwiftSyntax 的代码分析 |
| AgentColorSyntax · AgentTerminalNeo | 语法高亮 · 复古终端风格 Markdown |
| AgentAudit | `os.log` 审计日志 |

最终你得到的是一款内存占用极低的应用，却开箱即用地带着 Xcode 自动化、Swift 语法分析、辅助功能、AppleScript、Safari 自动化和 MCP。

## 核心：循环

Agent! 的一切都围绕一个理念：一个 **自我验证的任务循环**。模型思考、调用工具、查看真实结果，然后自我纠正。但这只有在你能信任它的前提下才行得通，所以我把几条规则直接写进了里面：

- **工具调用无法伪造。** 每次调用都经过同一个调度器，并返回真实输出。如果模型没真正调用工具就说 *"我点过了"*，Agent! 会当场指出来，并发送一条纠正信息。
- **"完成"要拿出证据。** 任务只有在 `goal_state` 标准都附上证据（比如构建通过或测试通过）逐一勾选后，才能宣布完成。
- **先读再改。** 如果模型还没读过某个文件，或者文件在读取之后已在磁盘上发生变化（用 SHA-256 校验），Agent! 会拒绝编辑。拒绝时会把最新的文件交给模型，这样下一次尝试就能用上正确的行。
- **一切都能撤销。** 每次编辑都会保留一周的快照。你可以回滚单个文件，也可以用 `rewind_task` 把整个任务倒带重来。

之后的文章里，我会把这些机制一个个拆开来讲。

## AgentScript：拥有完整权限的 Swift

AgentScript 是我最喜欢的部分之一。脚本就是普通的 Swift 文件。Agent! 用 SwiftPM 把每个脚本编译成 `.dylib`，再通过 `dlopen` 在进程内加载，所以你的脚本能拿到 Agent! 已有的全部 macOS 权限：辅助功能、自动化、日历、通讯录、邮件、照片等等。你只需要一个入口点：

```swift
import Foundation
import CalendarBridge   // any `import XBridge` auto-wires, no Package.swift edits

@_cdecl("script_main")
public func scriptMain() -> Int32 {
    print("Hello from AgentScript! 👋")
    return 0
}
```

脚本打印的任何内容都会回传给模型，返回值则作为退出状态。应用自带大约 35 个示例，包括 `TodayEvents`、`NowPlaying`、`CheckMail` 和 `CreateDmg`。

## 看得见的安全

Agent! 可以以 root 身份运行命令。这需要你给予相当大的信任，所以安全不能只是演示文稿里的一页幻灯片。它是代码，你可以在 GitHub 上亲自阅读。硬编码的 `ShellSafetyService` 会在命令发出之前就拒绝灾难性命令，特权守护进程也会在自己这一端再做一遍同样的检查。另外还有一个可选的"第二意见"，名叫 **Jev**，它会评估一条命令销毁数据的可能性有多大。[第一篇深度剖析](/blog/inside-agent-shell-guardrails/) 会详细讲清楚它是怎么工作的。

## 家族不断壮大

同样的智能体循环现在也能在终端里运行了，支持 macOS、Windows 和 Linux。有两个功能相同的 CLI：用 Rust 写的 [AgentiLoopCLI](https://github.com/AgentiLoop/AgentiLoopCLI) 和用 Go 写的 [AgentiLoopGo](https://github.com/AgentiLoop/AgentiLoopGo)。README 里我最喜欢的一个趣闻是：这两个小兄弟，正是 Mac 版 Agent! 自己写出来的。

## 你将在这里读到什么

- **内部机制：** 智能体循环、上下文压缩、工具调度、子智能体、记忆与计划。
- **安全：** 安全护栏、XPC 信任模型，以及近期的智能体事故能给我们其他人带来什么教训。
- **讲清原因的发布说明：** 每个版本改了什么，以及让这些改动变得必要的那个 bug。
- **实用指南：** AgentScript 实用配方、预算有限时如何挑选提供商、如何完全本地运行。
- **更广阔的智能体世界：** 新闻与评测，并且始终落脚到它对你的 Mac 意味着什么。

Agent! 支持 macOS 14.6 及更高版本，可在 Apple Silicon 和 Intel 上运行，个人使用免费。在下方下载吧，给它找点真正的活儿干，然后告诉我用得怎么样。
