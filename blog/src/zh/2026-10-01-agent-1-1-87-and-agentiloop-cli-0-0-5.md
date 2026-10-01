---
title: 全家齐发：Agent! 1.1.87 与 AgentiLoop CLI 0.0.5
description: Mac 版 Agent! 迎来自动驾驶（Auto-Pilot）、六个新提供商、更严格的评审器以及对 macOS 14.6 的支持。Rust 和 Go 两个 CLI 获得了更大的工具箱：搜索、网页抓取、待办清单、AGENTS.md、/undo、自定义命令和 --json。
tags: 公告, 发布, 跨平台
---
<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 380" role="img" aria-labelledby="fam-title fam-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="fam-title">AgentiLoop 家族：一个 Mac 应用和两个终端</title>
<desc id="fam-desc">中间是一个标有 Agent! 1.1.87 的大 Mac 窗口。左边的终端窗口里有一只小螃蟹，标签为 Rust 0.0.5；右边的终端窗口里有一只小地鼠，标签为 Go 0.0.5。虚线将三者连接到顶部一个共享的循环符号。</desc>
<rect width="760" height="380" rx="20" fill="#0f1724"/>
<g fill="#6fb6ff" opacity=".35"><circle cx="60" cy="50" r="2"/><circle cx="700" cy="70" r="2"/><circle cx="640" cy="330" r="2"/><circle cx="110" cy="320" r="2"/><circle cx="380" cy="350" r="2"/><circle cx="520" cy="40" r="2"/><circle cx="230" cy="36" r="2"/></g>
<g fill="none" stroke="#6fb6ff" stroke-width="3" stroke-dasharray="4 8" stroke-linecap="round"><path d="M380 80V112"/><path d="M350 62Q170 70 140 150"/><path d="M410 62Q590 70 620 150"/></g>
<g fill="none" stroke="#9fd2ff" stroke-width="5" stroke-linecap="round"><path d="M380 55C392 39 412 39 412 55C412 71 392 71 380 55C368 39 348 39 348 55C348 71 368 71 380 55Z"/></g>
<rect x="250" y="112" width="260" height="190" rx="16" fill="#1d2a3d" stroke="#6fb6ff" stroke-width="3"/>
<rect x="250" y="112" width="260" height="34" rx="16" fill="#26364d"/><rect x="250" y="130" width="260" height="16" fill="#26364d"/>
<circle cx="272" cy="129" r="6" fill="#ff5f57"/><circle cx="292" cy="129" r="6" fill="#febc2e"/><circle cx="312" cy="129" r="6" fill="#28c840"/>
<rect x="340" y="164" width="80" height="80" rx="20" fill="#2f7bf5"/>
<g fill="#fff"><circle cx="358" cy="186" r="5"/><circle cx="402" cy="186" r="5"/><circle cx="380" cy="204" r="5"/><circle cx="360" cy="226" r="5"/><circle cx="400" cy="226" r="5"/></g>
<g fill="none" stroke="#fff" stroke-width="2" opacity=".8"><path d="M358 186L380 204L402 186M380 204L360 226M380 204L400 226M360 226H400M358 186H402M358 186L360 226M402 186L400 226"/></g>
<text x="380" y="280" text-anchor="middle" font-family="system-ui,sans-serif" font-size="22" font-weight="700" fill="#e8f2ff">Agent! 1.1.87</text>
<rect x="40" y="150" width="190" height="150" rx="12" fill="#121c2a" stroke="#f08a4b" stroke-width="3"/>
<text x="56" y="178" font-family="ui-monospace,monospace" font-size="15" fill="#f08a4b">$ agentiloop</text>
<g fill="#f08a4b" stroke="#0f1724" stroke-width="2"><ellipse cx="135" cy="236" rx="34" ry="22"/><circle cx="92" cy="214" r="10"/><circle cx="178" cy="214" r="10"/></g>
<g stroke="#f08a4b" stroke-width="4" stroke-linecap="round"><path d="M110 256l-10 14M122 258l-6 14M148 258l6 14M160 256l10 14M100 222l8 6M170 222l-8 6"/></g>
<circle cx="124" cy="230" r="4" fill="#0f1724"/><circle cx="146" cy="230" r="4" fill="#0f1724"/>
<text x="135" y="292" text-anchor="middle" font-family="system-ui,sans-serif" font-size="17" font-weight="700" fill="#ffd2b5">Rust 0.0.5</text>
<rect x="530" y="150" width="190" height="150" rx="12" fill="#121c2a" stroke="#4fd1e8" stroke-width="3"/>
<text x="546" y="178" font-family="ui-monospace,monospace" font-size="15" fill="#4fd1e8">$ agentiloop</text>
<g stroke="#0f1724" stroke-width="2"><ellipse cx="625" cy="236" rx="30" ry="36" fill="#4fd1e8"/><circle cx="600" cy="204" r="7" fill="#4fd1e8"/><circle cx="650" cy="204" r="7" fill="#4fd1e8"/></g>
<circle cx="612" cy="222" r="9" fill="#fff"/><circle cx="638" cy="222" r="9" fill="#fff"/><circle cx="612" cy="222" r="4" fill="#0f1724"/><circle cx="638" cy="222" r="4" fill="#0f1724"/>
<text x="625" y="292" text-anchor="middle" font-family="system-ui,sans-serif" font-size="17" font-weight="700" fill="#c8f4fb">Go 0.0.5</text>
<text x="380" y="345" text-anchor="middle" font-family="system-ui,sans-serif" font-size="18" fill="#9fb6d4">一个循环，三种运行方式。</text>
</svg>
<figcaption>10 月 1 日的 AgentiLoop 家族：Mac 版 Agent!，以及 Rust 和 Go 两个命令行版本。</figcaption>
</figure>

今天，整个家族同时发布。**Agent! 1.1.87** 是 Mac 应用的新版本，**AgentiLoop CLI 0.0.5** 的 [Rust](https://github.com/AgentiLoop/AgentiLoopCLI/releases/tag/v0.0.5) 版和 [Go](https://github.com/AgentiLoop/AgentiLoopGo/releases/tag/v0.0.5) 版也同步推出。这是正式版，而不是预发布版，也是三者迄今为止最大的一步。

以下是新内容，直接取自 git 历史。

## Mac 版 Agent! 1.1.87

Mac 应用的上一个正式版是 9 月 12 日发布的 1.1.33。此后发生了很多事：1.1.87 共包含 449 次提交。以下是重点内容。

### 🤖 自动驾驶：`/auto <goal>`

这是本次的头号功能。给 Agent! 一个目标，`/auto` 就会在时间预算内以一系列无人值守的周期来执行它。每个周期都朝目标推进，检查当前进展，然后继续。

- 没有周期或迭代次数上限。它适用于 LLM 标签页，并保留目标历史，因此 `/auto last` 和 `/auto #N` 可以调回之前的目标。
- 会话在应用重启后依然保留，并在同一个标签页中恢复。
- **Esc** 只会停止当前周期。**Stop All**（或 `/auto stop all`）会结束整个会话。

这就是人类有意退后一步的智能体循环：你设定目的地和预算，由 Agent! 来驾驶。

### 🔌 六个新提供商，需要折腾的设置更少了

1.1.87 新增：**Fluxion AI**（提供 OpenAI 和 Anthropic 协议选项）、**Muse Code**（复用你的 `muse login` 订阅）、**Requesty**、**A2Agent**、**OrcaRouter**，以及 Coding Plan 上的 **Qwen Code**。此外还有一个实验性的 **fm serve** 提供商，通过本地 Chat Completions API 提供 Apple Foundation Models。

视觉支持现在根据每个提供商的目录元数据自动检测，因此不再需要 Force Vision 开关。在底层，所有提供商现在都位于同一个注册表 `APIProvider` 中，而不是分散在十几条独立的代码路径里。

### 🧐 无法被说服放水的评审器

Agent! 有一道评审关卡：在任务被标记为完成之前，由第二个模型审查改动。在 1.1.87 中，这项审查是**强制执行**的。未改变的 diff 会被拒绝，改变后的 diff 会被再次审查，问题也不能以"超出范围"为由被搪塞过去。评审器现在也可在 Codex 和 Apple Intelligence 上运行，日志会显示它发现了哪些问题，以及代码随后是否有所修改。

与之配套的是 **Jev**，这是 TypeSafe System One 决策层，为工具循环提供建议。它的设置位于新的 LLM 通用设置（LLM Common Settings）中。

### 🧠 更聪明的上下文

压缩功能经过了一轮细致打磨。阈值现在根据*实际使用中*的模型（标签页的模型或后备模型）来确定，并且会记住获取到的 Ollama 上下文窗口大小。这修复了某些模型在 16K 时就被压缩的错误。保留的尾部和微压缩以 token 而非消息数量为界，超大块会优先被截断，上下文溢出和 `max_tokens` 错误在各提供商之间采用相同的方式检测。

### 🖥️ 更多 Mac，更多语言

- **macOS 14.6 Sonoma 及更高版本**，支持 Apple Silicon 和 Intel。Apple Intelligence（Foundation Models）功能需要 macOS 26。
- 应用已本地化为西班牙语、法语、德语、简体中文、俄语、韩语和日语。
- 新的辅助功能操作：`wait_until_actionable`、`select_text_range` 和 `observe_start/poll/stop/list`。
- 通过 Homebrew 安装：`brew update && brew install --cask agentiloop-agent`。

### 🔒 默认更安全

递归删除当前项目文件夹的操作现在会被阻止。一次全应用范围的错误排查修复了 ShellSafety 的 `&` 只读绕过漏洞、Ollama 流式传输卡顿以及若干崩溃问题。当摘要指向从未写入的输出时，`task_complete` 会被拒绝；内存耗尽的本地模型会立即停止并给出明确原因，而不是原地空转。

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 330" role="img" aria-labelledby="box-title box-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="box-title">CLI 的更大工具箱</title>
<desc id="box-desc">一个打开的红色工具箱，标有 0.0.5。各种工具带着标签从中升起：带放大镜的 glob 和 grep、带地球的 web_fetch、带清单的 todo_write、带弯曲箭头的 /undo、带文档的 AGENTS.md，以及带花括号的 --json。</desc>
<rect width="760" height="330" rx="20" fill="#fff6ea"/>
<path d="M60 296H700" stroke="#c9a77f" stroke-width="10" stroke-linecap="round"/>
<path d="M240 178L270 140H490L520 178Z" fill="#b8323a" stroke="#5a1418" stroke-width="4" stroke-linejoin="round"/>
<rect x="240" y="178" width="280" height="112" rx="10" fill="#d9444d" stroke="#5a1418" stroke-width="4"/>
<path d="M340 140V120Q340 108 352 108H408Q420 108 420 120V140" fill="none" stroke="#5a1418" stroke-width="8"/>
<rect x="340" y="214" width="80" height="40" rx="8" fill="#fff" stroke="#5a1418" stroke-width="3"/>
<text x="380" y="241" text-anchor="middle" font-family="ui-monospace,monospace" font-size="20" font-weight="700" fill="#5a1418">0.0.5</text>
<g font-family="ui-monospace,monospace" font-size="17" font-weight="700" text-anchor="middle">
<g><rect x="60" y="40" width="150" height="44" rx="12" fill="#d7eaff" stroke="#3377b9" stroke-width="3"/><text x="135" y="68" fill="#173452">glob · grep</text><circle cx="232" cy="102" r="16" fill="none" stroke="#3377b9" stroke-width="5"/><path d="M244 114l14 14" stroke="#3377b9" stroke-width="6" stroke-linecap="round"/></g>
<g><rect x="60" y="120" width="140" height="44" rx="12" fill="#d9f5e4" stroke="#2f8f5b" stroke-width="3"/><text x="130" y="148" fill="#14432a">web_fetch</text><circle cx="222" cy="186" r="16" fill="#bfe9cf" stroke="#2f8f5b" stroke-width="3"/><path d="M206 186H238M222 170Q212 186 222 202Q232 186 222 170" fill="none" stroke="#2f8f5b" stroke-width="2.5"/></g>
<g><rect x="295" y="20" width="170" height="44" rx="12" fill="#fce9b6" stroke="#9a701b" stroke-width="3"/><text x="380" y="48" fill="#4a3608">todo_write</text><path d="M362 76l6 6 10-12M362 94l6 6 10-12" fill="none" stroke="#9a701b" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><path d="M386 78H404M386 96H404" stroke="#9a701b" stroke-width="4" stroke-linecap="round"/></g>
<g><rect x="560" y="40" width="140" height="44" rx="12" fill="#efe1ff" stroke="#7a4bb8" stroke-width="3"/><text x="630" y="68" fill="#341a5a">/undo</text><path d="M548 128Q520 128 520 104Q520 84 546 84" fill="none" stroke="#7a4bb8" stroke-width="5" stroke-linecap="round"/><path d="M538 74l12 10-12 10" fill="none" stroke="#7a4bb8" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></g>
<g><rect x="560" y="120" width="140" height="44" rx="12" fill="#ffe0e6" stroke="#b83a5a" stroke-width="3"/><text x="630" y="148" fill="#5a1426">AGENTS.md</text><path d="M528 172h20l8 8v26h-28z" fill="#fff" stroke="#b83a5a" stroke-width="3" stroke-linejoin="round"/></g>
<g><rect x="560" y="210" width="140" height="44" rx="12" fill="#e2e8f0" stroke="#4b617e" stroke-width="3"/><text x="630" y="238" fill="#173452">--json { }</text></g>
</g>
</svg>
<figcaption>AgentiLoop CLI 0.0.5：同样的循环，箱子里的东西多了很多。</figcaption>
</figure>

## AgentiLoop CLI 0.0.5：更大的工具箱

当我们[把智能体循环带到终端](/blog/the-terminal-strikes-back/)时，CLI 从五个锋利的工具起步：read、list、write、edit 和 bash。0.0.4 版教会了它干净利落地停下来。0.0.5 版则是为了让它有更多东西可用。所有功能都先在 Rust 版中落地，然后逐个提交地镜像到 Go 版，因此两个版本的功能完全相同。

### 新工具

| 工具 | 功能 | 需要先询问？ |
|---|---|---|
| `glob` | 按模式查找文件 | 否 |
| `grep` | 搜索文件内容，可附带 0–5 行上下文 | 否 |
| `web_fetch` | 以文本形式获取 http(s) 页面，有大小上限 | **是** |
| `todo_write` | 为多步骤工作维护一份清单（用 `/todos` 查看） | 否 |

`glob` 和 `grep` 会跳过 `.git`、`node_modules`、`target` 和二进制文件，并遵循 `.gitignore`，包括嵌套文件、否定、锚定和仅限目录的规则。这使它们比调用 shell 里的 `find` 更快，也比把整个目录树倒进上下文更安全。

### 它会读取你项目的说明

如果你的仓库中有 **`AGENTS.md`** 或 **`CLAUDE.md`**，CLI 会把它加载到系统提示中，同时还会加载 `~/.agentiloop` 中的一份，用于你的个人默认设置。像 `@docs/style.md` 这样的行会导入其他文件（支持嵌套且防循环）。还没有这个文件？**`/init`** 会写入一份入门 `AGENTS.md`，其中包含它检测到的构建和测试命令。

### 撤销、diff 及其他

- **`/undo`**：`write_file`、`edit_file` 和 `apply_patch` 所做的每一处改动都按提示记录日志，因此你可以回滚智能体的上一轮操作。
- **`/diff`** 显示工作树的 git 状态和 diff。
- **`/export`** 将对话保存为 Markdown。
- **`/usage`** 显示自启动以来的 token 总量以及上下文的占用程度。

### 打造专属于你的工具

- **自定义斜杠命令**：将一个 Markdown 文件放入 `.agentiloop/commands/`，比如内容为 `Review $1 for bugs` 的 `review.md`，然后 `/review main.rs` 就会运行它。支持 `$ARGUMENTS` 和 `$1`..`$9`，`/commands` 会列出所有命令。
- 来自你的服务器的 **MCP 提示** 会显示为 `/mcp__<server>__<prompt>` 命令。

### 为脚本和 CI 而生

- **`--json`** 将单次回答输出为一个 JSON 对象：result、is_error、session_id、provider、model 和 usage。
- **`--allow-tool` / `--deny-tool`** 按工具名称或 `mcp_*` 前缀设置权限规则。拒绝规则始终优先，即使面对 `--yes` 也是如此。
- **`--append-system-prompt`** 为单次运行向系统提示追加文本。
- **管道直接可用**：提示中单独的 `-` 会被替换为 stdin，因此 `git diff | agentiloop "review this" -` 正如其字面意思那样工作。

把这些组合起来，就是一个能审查拉取请求、拒绝动用 shell 并返回机器可读输出的 CI 步骤：

```
git diff origin/main | agentiloop --deny-tool bash --json "review this diff" -
```

## 为什么一起发布？

因为它们是同一个理念的三种形态。Mac 版 Agent! 是旗舰：它操控你的应用、你的 Xcode 构建以及整个桌面。CLI 则把同样的循环带到 macOS、Windows 和 Linux 上的每一个终端。CLI 的按 Esc 取消，以及 Mac 应用带 Stop All 按钮的自动驾驶，从两个方向回答了同一个问题：*一个人如何掌控一个自行运转的循环？*

这是我们最在意的部分。不是可爱的头像，也不是基准测试上更高的分数，而是人在回路中：你设定目标，你看到每一步，你可以停止它，也可以撤销它。

## 获取方式

- **Mac 版 Agent! 1.1.87**：[从 GitHub 下载](https://github.com/AgentiLoop/Agent/releases/tag/v1.1.87.287)或运行 `brew update && brew install --cask agentiloop-agent`。需要 macOS 14.6 或更高版本，Apple Silicon 或 Intel。
- **AgentiLoop CLI 0.0.5 (Rust)**：[GitHub 上的发布页](https://github.com/AgentiLoop/AgentiLoopCLI/releases/tag/v0.0.5)。
- **AgentiLoopGo 0.0.5 (Go)**：[GitHub 上的发布页](https://github.com/AgentiLoop/AgentiLoopGo/releases/tag/v0.0.5)。

macOS 版 CLI 二进制文件已签名并经过公证。解压后，将 `agentiloop` 放入你的 PATH 并运行它，设置向导会引导你完成剩下的步骤。

非常欢迎测试者参与。试试在一次大改动后使用 `/undo`，把它指向一个带有 `AGENTS.md` 的仓库，或者把 `--json` 接入脚本，然后告诉我们哪里出了问题。请附上你的操作系统、提供商和模型，并且千万不要附上 API 密钥。
