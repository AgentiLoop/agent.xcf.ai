---
title: 欢迎来到 Agent! 博客：一个应用，任意 AI，全面掌控你的 Mac
description: AgentiLoop Agent! 是什么、如何构建，以及这个每日更新的博客将涵盖哪些内容——一切都直接来自源代码。
tags: 公告, 架构
---
这里是 **AgentiLoop Agent!** 的官方博客。Agent! 是一款原生 macOS AI 智能体。我们的计划很简单：每天一篇文章，内容主要来自我们最熟悉的东西——代码库本身。你将看到对智能体循环工作原理的深度剖析、某条安全护栏为何如此设计、最新候选版本有哪些变化，偶尔也会放眼更广阔的 AI 智能体世界。

如果你是第一次来，这篇文章就是你的导览图。

## Agent! 是什么

Agent! 是一款 100% 原生的 Swift / SwiftUI 应用。你输入（或说出）想做的事，它就会直接在你的 Mac 上把事情做完，而不只是告诉你该怎么做：

- **真正动手写代码。** 它会读取你的项目，用字符串替换式的 diff 编辑文件，在 Xcode 中构建，读取错误信息并修复，最后用 git 提交。
- **驱动任意 Mac 应用。** 它通过辅助功能（Accessibility）API 操作应用，同时支持 AppleScript、JXA 以及 51 个 ScriptingBridge 应用桥接。
- **以你的身份或 root 身份运行 shell 命令。** 这依靠通过 SMAppService 注册、经由 XPC 访问的 Launch Agent 和 Launch Daemon 实现。
- **对接 23 家 LLM 提供商** ，外加设备端的 Apple Intelligence：Claude、Codex、OpenAI、Gemini、Grok、Mistral、DeepSeek、Qwen、Z.ai、OpenRouter、Ollama、vLLM、LM Studio 等等。
- **它会倾听。** 说出 *"Agent!"* 再加上任务，或者在 iPhone 上通过 iMessage 给它发消息（仅限已批准的发送者）。

README 用一句话概括了它： *Siri 负责回答，Agent! 负责行动。*

## 没有 NPM，没有 Electron

最让人意外的，是 Agent! *没有* 附带的东西：没有 Electron 外壳，没有 Node 运行时，也没有 `node_modules`。它依赖的每一个 Swift 包都出自同一位作者之手，并且各自托管在 [AgentiLoop](https://github.com/AgentiLoop) 组织下的独立仓库中：

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

最终成果是一款内存占用极低的应用，开箱即用地支持 Xcode 自动化、Swift 语法分析、辅助功能、AppleScript、Safari 自动化和 MCP。

## 核心：循环

一切都围绕一个理念展开：一个 **自我验证的任务循环** 。模型进行推理、调用工具、查看真实结果，然后自我纠正。以下几条规则让这个循环值得信赖：

- **工具调用无法伪造。** 每次调用都经过同一个调度器，并返回真实输出。如果模型没有调用工具就声称 *"我点过了"* ，Agent! 会注入一条纠正信息。
- **"完成"需要证据。** 任务只有在其 `goal_state` 标准都被附上证据（例如构建成功或测试通过）标记为完成后，才能宣告结束。
- **先读后改。** 如果模型尚未读取某个文件，或者该文件在读取后已在磁盘上发生变化（通过 SHA-256 校验），对它的编辑都会被拒绝。拒绝时会顺便替模型读取该文件，这样下一次尝试就能使用最新内容。
- **一切皆可撤销。** 每次编辑都会保留一周的快照。你可以回滚单个文件，也可以用 `rewind_task` 让整个任务倒带重来。

我们会在后续文章中逐一拆解这些机制。

## AgentScript：拥有完整权限的 Swift

最具特色的组件之一是 **AgentScript** 。脚本就是普通的 Swift 文件。Agent! 用 SwiftPM 把每个脚本编译成 `.dylib`，再通过 `dlopen` 在进程内加载，因此脚本会继承 Agent! 自身的 macOS 权限：辅助功能、自动化、日历、通讯录、邮件、照片等等。编写一个脚本只需要一个入口点：

```swift
import Foundation
import CalendarBridge   // any `import XBridge` auto-wires, no Package.swift edits

@_cdecl("script_main")
public func scriptMain() -> Int32 {
    print("Hello from AgentScript! 👋")
    return 0
}
```

脚本打印的任何内容都会返回给模型，返回值则作为退出状态。应用内置了大约 35 个示例，包括 `TodayEvents`、`NowPlaying`、`CheckMail` 和 `CreateDmg`。

## 看得见的安全

Agent! 可以以 root 身份运行，所以安全不是演示文稿里的一页幻灯片，而是你可以在 GitHub 上打开阅读的代码。硬编码的 `ShellSafetyService` 会在命令分发之前拒绝灾难性命令，特权守护进程也会在自己这一侧再执行一遍同样的检查。还有一个名为 **Jev** 的可选"第二意见"，用来评估一条命令销毁数据的可能性。我们的 [第一篇深度剖析](/blog/inside-agent-shell-guardrails/) 会详细讲解其工作原理。

## 家族不断壮大

同样的智能体循环如今也能在 macOS、Windows 和 Linux 的终端中运行，形式是两个功能相同的 CLI：用 Rust 编写的 [AgentiLoopCLI](https://github.com/AgentiLoop/AgentiLoopCLI) 和用 Go 编写的 [AgentiLoopGo](https://github.com/AgentiLoop/AgentiLoopGo)。README 里有个有趣的细节：这两个"小兄弟"正是 Mac 版 Agent! 亲手写出来的。

## 你将在这里看到什么

- **内部机制：** 智能体循环、上下文压缩、工具调度、子智能体、记忆与计划。
- **安全：** 安全护栏、XPC 信任模型，以及近期智能体事故给开发者的启示。
- **讲清原因的发布说明：** 每个版本改了什么，以及促成这些改动的 bug。
- **实用指南：** AgentScript 实战技巧、如何在预算内挑选提供商、如何完全本地运行。
- **更广阔的智能体世界：** 新闻与评测，并始终落脚到它对你的 Mac 意味着什么。

Agent! 支持 macOS 14.6 及更高版本，可在 Apple Silicon 和 Intel 上运行，个人使用完全免费。在下方下载，明天记得再来。
