---
title: 终端反击：用 Rust 和 Go 将智能体循环带向跨平台
description: Agent! 是一款 Mac 应用，但编程智能体应该出现在开发者工作的任何地方。本文介绍智能体循环如何变成两个 CLI（一个用 Rust，一个用 Go），并在 macOS、Windows 和 Linux 上提供全屏 TUI。
tags: 公告, 跨平台, 工程
---
在过去的大部分时间里，Agent! 一直是一款引以为傲的 Mac 应用：原生 Swift 和 SwiftUI，深度集成 AppleScript 与辅助功能（Accessibility），并通过 Launch Daemon 获得 root 权限。它依然是我们的旗舰产品。但在过去几天里，我们对编程智能体的看法发生了变化，而今天，这一变化正式发布。

**智能体循环现在可以在你的终端中运行，支持 macOS、Windows 和 Linux**。它有两个功能相同的版本：用 Rust 编写的 [AgentiLoopCLI](https://github.com/AgentiLoop/AgentiLoopCLI)，以及用 Go 编写的 [AgentiLoopGo](https://github.com/AgentiLoop/AgentiLoopGo)。没错，这两个小兄弟的大部分代码都是 Mac 版 Agent! 亲手写的。

## 范式转移：回归终端

第一波 AI 编程工具存在于编辑器和聊天窗口中。而正在胜出的这一波，存在于**终端**之中。这背后有充分的理由：

- **终端本来就是干活的地方**。构建、测试、git、包管理器和 SSH 会话都在这里。终端里的智能体不需要为每样东西单独做集成，它有 `bash`。
- **它无处不在**。CLI 可以运行在 Linux 构建机上、容器里、通过 SSH 连接的 Raspberry Pi 上，或者 Windows 开发虚拟机中。而 Mac 应用只能运行在 Mac 上。
- **它可以组合**。单次模式（`agentiloop "explain this project"`）可以直接嵌入脚本和 CI。
- **它对自己的所作所为坦诚透明**。每一次工具调用、每一个 diff 和每一个权限提示都以纯文本形式滚动显示。

Mac 应用的超能力，比如通过辅助功能操控 Photo Booth，或用 ScriptingBridge 编写 Mail 脚本，确实只属于 Mac。但**智能体循环**不是。推理、调用工具、读取真实结果、修正，然后重复：这在任何拥有 shell 和文件系统的操作系统上都行得通。所以我们把这个循环单独抽了出来。

## 为什么用两种语言？

我们本可以只选一种。但我们刻意将同一套设计移植了两次。

**Rust (AgentiLoopCLI)** 最先完成。工作区于 9 月 20 日搭建完成，包含核心循环、Anthropic 提供商、内置工具和 CLI。它被拆分为五个 crate：`agentiloop-core`（循环、消息、会话和权限）、`agentiloop-provider`、`agentiloop-tools`、`agentiloop-mcp` 和 `agentiloop-cli`。它运行在 `tokio` 上，使用搭配 `rustls` 的 `reqwest`，因此在 Windows 上无需折腾 OpenSSL，并使用 `ratatui` 绘制 TUI。Markdown 由 `pulldown-cmark` 处理，代码的语法高亮则来自 `syntect`。

**Go (AgentiLoopGo)** 在 9 月 23 日通过一连串提交落地：先是带测试的核心（消息、智能体循环、压缩、会话和权限），然后是提供商，接着是 MCP 客户端，最后是 CLI，包括 REPL、TUI、Markdown、语法高亮、会话和斜杠命令。它用 `tcell` 绘制 TUI，用 `goldmark` 渲染 Markdown，用 `chroma` 进行高亮，并用 `liner` 处理行编辑。它的发布工作流与 Rust 版本面向相同的五个平台。

实现两遍就是最好的设计评审。任何真正属于 Rust 特有或 Go 特有的写法都会立刻暴露出来，剩下的才是真正的架构。这还有一个实际的好处：选择你的团队已经信任的工具链就好。然后告诉我们哪个做得更好。🦀 vs 🐹

## 同样的循环，更小的表面

两个 CLI 都刻意从一套小而精的工具集起步：

| 工具 | 功能 | 需要先询问？ |
|---|---|---|
| `read_file` | 读取文件并显示行号 | 否 |
| `list_dir` | 列出文件夹内容 | 否 |
| `write_file` | 创建或覆盖文件 | **是** |
| `edit_file` | 替换一段精确匹配的文本 | **是** |
| `bash` | 运行命令（在 Mac 和 Linux 上使用 `sh -c`，在 Windows 上使用 `cmd /C`） | **是** |

想要更多？两个版本都包含一个从 Agent! 自己的 AgentMCP 移植而来的 MCP 客户端，支持 stdio、Streamable HTTP 以及旧版 HTTP+SSE，因此任何 MCP 服务器的工具都可以直接接入。

权限是核心的一部分，而不是硬塞进 UI 的附加功能。在 Rust 中，由一个 `PermissionPolicy` trait 根据工具名称、是否会修改内容以及输入，来决定每次调用能否执行。结果是 `Allow`、`Deny` 或 `Cancel`。第三个选项的存在源于一个真实的烦恼：在权限提示时按下 **Esc**，应该只跳过*那一次调用*，而不是终止整个任务。CLI 提供交互式策略，而测试和 CI 使用 `AllowAll`。

## 跨平台体现在细节中

"支持 Windows"说起来容易，做到名副其实却很难。我们为此做了这些事：

- **真正终止失控的命令**。当 `bash` 超时时，如果 shell 已经派生出子进程，仅仅终止 shell 是不够的。Go 版本会终止整个进程树：在 Unix 上使用进程组，在 Windows 上使用 `taskkill /T`。代码被拆分为 `proc_unix.go` 和 `proc_windows.go`。
- **三大操作系统上的 CI**。Go 仓库在 macOS、Linux 和 Windows 上运行 CI，而 Rust 的发布工作流会构建五个二进制文件：macOS arm64 和 x86_64、Linux x86_64 和 arm64，以及 Windows x86_64。
- **已签名的 Mac 二进制文件**。发布工作流可以对 macOS 构建进行签名和公证，这样 Gatekeeper 就不会拦截它们。
- **无需考古配置文件**。CLI 会记住你的启动方式：提供商、模型、TUI 模式和会话。首次运行之后，只需输入 `agentiloop` 就能精确地从上次中断的地方继续。

## 用起来像应用的 TUI

它有三种运行方式：全屏 **TUI**（`agentiloop --tui`）、适用于简单终端的逐行**聊天**模式，以及用于脚本的**单次**模式。TUI 在过去几天里进展飞快：

- 提示框中的动画忙碌指示器，包含旋转图标、当前活动和已用时间
- 每秒 token 数统计
- 可点击的链接
- 在多次启动之间保留的提示历史
- 恢复会话时显示之前的对话，让你不必面对一片空白的屏幕
- 由提供商实时模型列表支持的 `/model`

当 API 密钥缺失或错误时，它会用通俗的语言说明问题并指出真正的提供商，而不是直接甩给你一个 401。

## 提供商

从第一天起，它就支持 Claude（API 密钥或 Claude Code OAuth 令牌均可放在同一个凭据中，认证方式会自动识别）、OpenAI 及任何兼容 OpenAI 的服务器、通过 Ollama 或 LM Studio 运行的本地模型，以及 Apple Silicon 上的 **oMLX**。它会自动从 `~/.omlx/settings.json` 读取 oMLX 的地址和密钥。

## 试用正式版

今天我们发布了 **v0.0.4** 正式版。它还处于早期阶段，迭代很快，我们希望现在就听到你的反馈，趁改动成本还低。你可以从 [Rust releases](https://github.com/AgentiLoop/AgentiLoopCLI/releases) 下载二进制文件，或者从[源码](https://github.com/AgentiLoop/AgentiLoopGo)构建 Go 版本。

Mac 应用不会消失。如果你用的是 Mac，Agent! 依然能做到任何终端都做不到的事。但如果你曾希望在 Linux 服务器、Windows 笔记本和 Raspberry Pi 上使用同一个智能体，它现在来了。
