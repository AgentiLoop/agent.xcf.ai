---
title: Agent! 现已支持 macOS 14.6 和 Intel Mac：我们如何摆脱对 macOS 26 的依赖
description: Agent! 原本围绕 macOS 26 上的 Apple Intelligence 构建。本文介绍我们如何通过一天的 #available 条件判断和包版本升级，让它能够在 Apple Silicon 和 Intel 的 macOS 14.6 上运行。
tags: 发布说明, 工程
---
直到今天，Agent! 都还要求 macOS 26。从今天的预发布版本开始，它可以在**macOS 14.6 或更高版本上运行，同时支持 Apple Silicon 和 Intel**。这覆盖了大量此前被拒之门外、却依然完全好用的 Mac，其中许多根本无法运行 Apple Intelligence。

下面按提交逐一说明，我们在一天之内做了哪些工作。

## 拦路虎：FoundationModels

Agent! 通过 **FoundationModels** 框架使用 Apple 的端侧模型，而该框架仅存在于 macOS 26 上。它并不是主力大脑，那部分由你选择的提供商负责。但它承担着好几项工作：上下文压缩时的快速摘要、端侧 token 计数、启动时预热的会话，以及一些分流处理。

引用了 macOS 26 类型的代码无法针对更早的部署目标进行构建。因此第一步（`ea5ce624`）就是把**所有**对 FoundationModels 的使用都放到 `#available(macOS 26, *)` 之后。这涵盖了 `FoundationModelService`、`AppleIntelligenceMediator`、`AgentApp` 中的预热、`Compression.swift` 中的压缩摘要和 token 计数，以及 `AboutSelf`。

## 技巧：对存储属性进行类型擦除

`#available` 适用于代码路径，却不适用于存储属性。当运行中的系统上不存在 `LanguageModelSession?` 这个类型时，类无法持有该类型的属性。解决办法是将其存储为 `AnyObject?`，并在使用它的地方、在受条件保护的代码中再转换回来：

```swift
/// Type-erased `LanguageModelSession` so the stored property compiles below macOS 26.
private(set) var session: AnyObject?

@available(macOS 26.0, *)
var transcript: Transcript? {
    (session as? LanguageModelSession)?.transcript
}
```

正如提交信息所说，这些存储属性不再“把框架类型拖进类的内存布局中”。

可用性检查也为旧系统给出了坦诚的答案：

```swift
static var unavailabilityReason: String {
    guard #available(macOS 26.0, *) else { return "Apple Intelligence requires macOS 26 or later." }
    ...
}
```

因此在 macOS 14 或 15 上，Apple Intelligence 只会显示为不可用，并附上清晰的原因，其他一切照常运行。在 macOS 26 上，则没有任何变化。

## 长尾工作：十个包

Agent! 由它自己的一系列 Swift 包构建而成，而每个包都声明了各自的最低系统版本。提交 `4d7fca86` 将全部十个包升级到了声明 `.macOS(.v14)` 的版本：

| 包 | 版本 |
|---|---|
| AgentAccess | 2.10.24 |
| AgentAudit | 1.3.9 |
| AgentColorSyntax | 1.2.8 |
| AgentD1F | 1.0.15 |
| AgentEventBridges | 1.1.8 |
| AgentLLM | 1.0.8 |
| AgentMCP | 1.6.10 |
| AgentSwift | 1.1.11 |
| AgentTerminalNeo | 1.37.9 |
| AgentTools | 2.53.19 |

在这样的日子里，掌控所有依赖的好处就体现出来了。无需等待上游维护者，只需打十个标签。

## 意外：26.4

有一个 API 仅靠 26.0 的条件判断还不够。`SystemLanguageModel.tokenCount(for:)` 从 **macOS 26.4** 起才存在，因此它的可用性检查从 26.0 改为了 26.4。否则，运行 26.0 到 26.3 的 Mac 就会尝试调用一个尚不存在的方法。这很好地提醒了我们：“框架可用”和“这个方法可用”并不是同一个问题。

## 在旧款 Mac 上能获得什么

在 macOS 14.6 和 15 上，无论是 Apple Silicon 还是 Intel，Agent! 的工作方式都完全相同：

- 全部 23 个云端和本地 LLM 提供商
- 完整的工具循环：编码、Xcode 构建、git、以你本人或 root 身份运行的 shell、Accessibility、AppleScript、JXA、AgentScript、Safari 自动化以及 MCP
- 上下文压缩，使用模型自身的摘要和提供商的 token 计数，只是没有 Apple Intelligence 这一层

只有端侧 Apple Intelligence 功能需要 macOS 26。

## 立即获取

每个正式版和预发布版都会提供经过签名、公证并装订公证票据的二进制文件。你永远不需要从源码构建：

```sh
brew update && brew install --cask agentiloop-agent
```

或者从 [GitHub Releases](https://github.com/AgentiLoop/Agent/releases) 下载 `.dmg`。如果你一直在等待让旧款 MacBook 或 Intel Mac mini 用上它，那就是今天了。
