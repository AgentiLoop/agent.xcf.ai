---
title: 在模型开口之前：深入解析 Agent! 的 Shell 安全护栏
description: ShellSafetyService、守护进程侧的二次检查以及 Jev 第二意见如何阻止 AI 智能体清空你的 Mac——带你逐行走读真实的 Swift 代码。
tags: 安全, 内部机制
---
本周，TechRadar 报道称，一个编程智能体在短时间内删除了约 48,000 个文件，随后道了歉。道歉于事无补，文件已经没了。

Agent! 可以通过 Launch Agent 以你的身份运行 shell 命令，也可以通过 Launch Daemon 以 **root** 身份运行。这正是它的价值所在：它能烧录 SD 卡、修复权限、清理构建目录。但这同样意味着，"模型大概会小心的"根本算不上安全模型。所以 Agent! 不指望模型自己小心，而是在任何命令运行之前，用代码对每条命令进行三层检查。

## 第 1 层：模型无法靠说辞绕过的硬编码护栏

`ShellSafetyService` 是位于 `Agent/Services/ShellSafetyService.swift` 中的一个普通 Swift `enum`。文件顶部的文档注释奠定了基调：它运行在 *每一个执行入口之前* ，并且会 *在分发之前* 直接拒绝灾难性命令。系统提示词被如实定位为兜底手段，而不是执行层。

入口函数接收命令、命令将要运行的上下文，以及当前标签页的项目文件夹：

```swift
static func check(_ command: String,
                  context: Context = .userAgent,
                  projectFolder: String = "") -> Verdict
```

`Verdict` 包含 `allowed`、一段人类可读的 `reason`，以及一个供审计日志使用的简短 `rule` id。这段 reason 是写给模型看的：它会作为工具结果返回，让 LLM 明白命令 *为什么* 被拒绝，而不是一味重试。

### 像 shell 一样解析复合命令

简单粗暴的过滤器只检查字符串开头，但攻击者和犯糊涂的模型可不会配合。`check` 会按 `;`、`&&`、`||`、`|` 和换行符拆分命令，然后检查 **每一个片段** 。因此，即使前半部分人畜无害，`ls; rm -rf /` 依然会被拦截。

这个顺序有一个刻意设计的例外。经典的 fork 炸弹 `:(){ :|:& };:` 恰恰 *依赖* `;` 和 `|`——正是拆分器会拆开的字符。因此，fork 炸弹检查会在拆分之前针对整条命令执行。

### 剥掉伪装

在匹配 `rm` 之前，一个名为 `stripPrefixWrappers` 的辅助函数会剥掉那些不改变命令实际行为的包装：`sudo`、`exec`、`command`、`builtin`、`eval` 和 `doas`。它还会去掉开头的环境变量赋值，例如 `FOO=bar`。这样一来，`sudo rm -rf ~` 和 `FOO=1 exec rm -rf ~` 触发的规则与裸命令完全相同。

参数标志也是经过解析的，而不是简单的模式匹配。`-rf`、`-fr`、`-Rf`、`-r -f`、`--recursive --force` 都会被识别，因为解析器会在任意短参数组合中查找 `r` 和 `f`，同时也识别长参数形式。

### 它会拒绝什么

以下是源代码中出现的规则 id：

| 规则 | 拦截内容 |
|---|---|
| `rm.catastrophic` | 对 `/`、`*` 或 `./*` 这类裸通配符，或任意写法的主目录（`~`、`~/*`、`$HOME`、`${HOME}/*` 或主目录的字面路径）执行 `rm -rf` |
| `rm.no-preserve-root` | `--no-preserve-root`，即显式绕过 `/` 保护的选项 |
| `rm.project-folder` | 递归删除智能体当前工作的项目文件夹，或用通配符删除其中的所有内容。删除指定名称的子文件夹仍然允许。 |
| `rm.dangerous-target` | 用户级路径上的其他危险 `rm` 目标 |
| `fork-bomb` | 自我复制的进程炸弹 |
| `mv.to-devnull` | 通过把文件移动到 `/dev/null` 来"删除"文件 |
| `find.delete-broad-root` | 从范围过大的根目录执行 `find … -delete` |
| `perms.recursive-on-root` | 对根级路径递归修改权限 |

项目文件夹规则值得多说几句。它与上面那起事故的关系最为直接：无论请求如何措辞，智能体都绝不应该清空它被要求处理的那个项目本身。

### root 被区别对待，这是有意为之

你可能以为 root 守护进程会受到 *最严格* 的规则约束，实际上它受到的约束范围最窄。注释解释了原因：守护进程的存在就是为了完成系统级工作，比如磁盘克隆或 `mkfs`，它"不应该和我们作对"。因此在 `.rootDaemon` 上下文中，`check` 会直接跳到 `checkCatastrophicRm`，只拦截三种不可恢复的模式（`/`、裸通配符和主目录），外加 `--no-preserve-root` 和清空项目文件夹。其余一切都交由操作者自行决定。

这是一个值得借鉴的设计选择。会拦截正当管理操作的护栏，最终会被关掉；只拦截不可恢复错误的护栏，才会一直开着。

## 第 2 层：守护进程再检查一遍

应用在分发任何命令之前都会运行 `ShellSafetyService.check`，但辅助进程并不因此就盲目信任。在 `Shared/DaemonCore.swift` 中，守护进程写完审计日志条目后，会立即在自己这一侧运行 **同样的检查** ：

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

被拦截的命令会连同规则 id 一起记录为已拒绝，并返回退出状态 126，永远不会到达 `/bin/zsh`。这一点很重要，因为 XPC 监听器会接受同一团队签名的任何客户端。即使有其他同团队签名的程序直接连接 mach 服务，也同样会撞上这道护栏。

## 第 3 层：Jev，为模式规则的盲区提供第二意见

模式规则很精确，但它们只认识你写下来的那些模式。许多破坏性命令看起来并不像 `rm -rf /`：对错误文件执行的 `truncate`、通过管道传给 CLI 的 SQL `DROP`、方向搞反了的 `dd`。

这就是 **Jev** 的职责所在。它是位于 `JevAdvisor.swift` 中的一个可选建议层。每条已经 *通过* `ShellSafetyService` 的命令都会交给 Jev，由它评估该命令不可逆地销毁数据的可能性。一旦超过你设定的阈值，Agent! 就会拒绝执行，并给出清晰的提示：

```text
Refused: Jev rated this command 85% likely to irreversibly destroy data.
Command: …
Narrow the target or run it yourself if this is intentional.
```

从几个细节可以看出它的边界划定得有多谨慎：

- **只做补充，绝不取代。** 代码注释写得很明白：`ShellSafetyService` 才是执行层，Jev 只负责捕捉模式规则漏掉的情况。这也是阈值被刻意设得很高的原因：默认值为 **70%** ，你可以在设置中以 10% 为步长在 0 到 100% 之间调整。
- **失败时放行，但会大声告知。** 没有密钥、开关关闭或网络中断都意味着"不发表意见"，因此不稳定的服务永远不会卡住你的任务。但失败依然会被记录（`⚠️ Jev check failed, command allowed`），这样过期的密钥就不会被误当成"Jev 认为安全"。
- **取消就是取消。** 如果你在 Jev 思考时停止任务，命令不会被执行。
- **每个判定都清晰可见。** 每次检查都会记录风险百分比、允许还是拒绝、给出答复的模型以及 token 数量。

## 经过测试，而非想当然

`AgentTests/ShellSafetyServiceTests.swift` 中包含 30 个针对这套护栏的测试。而且由于每条辅助进程命令在运行前都会写入审计日志，你随时都能还原智能体尝试做过的事情，包括那些被禁止的操作。

## 给所有智能体开发者的启示

1. **在代码中强制执行，而不是在提示词里。** 提示词只是建议，Swift `enum` 可不是。
2. **像 shell 那样解析。** 拆分复合命令、剥离包装、规范化参数标志。
3. **在特权边界处再检查一次。** 不要以为你自己的客户端是唯一的调用方。
4. **拦截不可恢复的操作，而不是不寻常的操作。** 范围窄的规则能长期存活，噪声大的规则终会被禁用。
5. **在此之上加入判断，并让它的失败清晰可见。** 只有当你能分辨它何时没有给出答复时，第二意见才有价值。

所有这些都在 [GitHub](https://github.com/AgentiLoop/Agent) 上公开。欢迎阅读、挑刺，如果你发现某条本该被拦截的命令漏网了，请提交 issue。
