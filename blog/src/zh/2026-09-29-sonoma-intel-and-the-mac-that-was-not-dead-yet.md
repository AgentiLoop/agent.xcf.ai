---
title: Sonoma、Intel，以及那台还没“死”的 Mac
description: Agent! for Mac 现在可以在 macOS Sonoma 14.6 及更高版本上运行，同时支持 Apple Silicon 和 Intel。很多人都想要一个 macOS 26 之前的版本。它来了。
tags: 发布说明, 幕后
---
说实话吧。当 Agent! 写着“需要 macOS 26”的时候，很多好好的 Mac 就被挡在了门外。

如果你用的是 Sonoma，那就没戏。用的是 Sequoia，也一样。要是你用的是 Intel Mac，那你连被讨论的资格都没有。

这件事一直让我耿耿于怀。那些 Mac 还能用。人们每天都在用。在上面写代码，靠它们做生意，还在上面开着多得离谱的浏览器标签页。它们没做错什么。只是没装最新的系统而已。

现在不一样了。**Agent! for Mac 现在可以在 macOS Sonoma 14.6 及更高版本上运行，Apple Silicon 和 Intel 都支持。**

你们很多人一直在等一个 macOS 26 之前的版本。这次，是为你们准备的。

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 340" role="img" aria-labelledby="macs-title macs-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="macs-title">两台开心的 Mac 和一块新招牌</title>
<desc id="macs-desc">一台 Intel Mac 和一台 Apple Silicon Mac 放在桌上，都在微笑。它们中间有一块招牌，“仅限 macOS 26”被划掉了，换成了“macOS 14.6+，Apple Silicon 和 Intel”。</desc>
<rect width="760" height="340" rx="20" fill="#eef6ff"/>
<rect x="182" y="215" width="16" height="50" fill="#8a97a8"/><rect x="150" y="263" width="80" height="12" rx="4" fill="#8a97a8"/>
<rect x="562" y="215" width="16" height="50" fill="#8a97a8"/><rect x="530" y="263" width="80" height="12" rx="4" fill="#8a97a8"/>
<rect x="374" y="170" width="12" height="105" fill="#8b684c"/>
<path d="M30 280H730" stroke="#8b684c" stroke-width="10" stroke-linecap="round"/>
<rect x="90" y="100" width="200" height="125" rx="14" fill="#c9d3df" stroke="#173452" stroke-width="4"/>
<rect x="104" y="114" width="172" height="97" rx="6" fill="#559ef5"/>
<circle cx="160" cy="150" r="9" fill="#fff"/><circle cx="220" cy="150" r="9" fill="#fff"/>
<circle cx="162" cy="151" r="4" fill="#173452"/><circle cx="222" cy="151" r="4" fill="#173452"/>
<path d="M165 178Q190 196 215 178" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
<rect x="470" y="100" width="200" height="125" rx="14" fill="#e7e2f7" stroke="#173452" stroke-width="4"/>
<rect x="484" y="114" width="172" height="97" rx="6" fill="#7b6ad6"/>
<circle cx="540" cy="150" r="9" fill="#fff"/><circle cx="600" cy="150" r="9" fill="#fff"/>
<circle cx="542" cy="151" r="4" fill="#173452"/><circle cx="602" cy="151" r="4" fill="#173452"/>
<path d="M545 178Q570 196 595 178" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
<rect x="303" y="60" width="154" height="115" rx="10" fill="#fff" stroke="#8b684c" stroke-width="4"/>
<g font-family="system-ui,sans-serif" text-anchor="middle" fill="#173452">
<text x="380" y="88" font-size="16" fill="#8a97a8">仅限 macOS 26</text>
<text x="380" y="118" font-size="19" font-weight="700">macOS 14.6+</text>
<text x="380" y="141" font-size="16">Apple Silicon</text>
<text x="380" y="162" font-size="16">和 Intel</text>
<text x="190" y="315" font-size="20">Intel Mac</text>
<text x="570" y="315" font-size="20">Apple Silicon Mac</text>
</g>
<path d="M318 83H442" stroke="#d94877" stroke-width="3" stroke-linecap="round"/>
</svg>
<figcaption>同一张桌子。同样的 Mac。新的招牌。</figcaption>
</figure>

## 为什么一开始只支持 26

Agent! 通过一个叫 FoundationModels 的框架来使用 Apple 的设备端模型。它不是主脑。真正的重活由你选择的提供商来干。但设备端模型能帮忙处理一些小活儿，比如在上下文压缩时做摘要、统计 token，以及在应用启动时预热会话。

问题就在这里。FoundationModels 只存在于 macOS 26。只要你的代码提到了它的任何一个类型，就没法为更老的 Mac 构建。编译器直接说不。

所以最省事的做法就是要求 macOS 26，然后继续往前走。至少对我来说省事。对其他人可就没那么友好了。

说实话，这有点傻。设备端模型只是个帮手。有它挺好。但它从来不是 Agent! 能用的原因。为了一个帮手把所有老 Mac 都拒之门外，就像因为家里没香菜了就拒绝做晚饭一样。

## 那要怎么解决？

先问一句。在 Agent! 碰设备端模型之前，它会检查：我是在 macOS 26 上吗？如果是，很好，用它。如果不是，那段代码就直接不运行，你的提供商照样干真正的活儿。

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 300" role="img" aria-labelledby="fork-title fork-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="fork-title">用之前先问一句</title>
<desc id="fork-desc">一张流程图。Agent! 想用设备端模型。它先问：这是 macOS 26 吗？“是”就使用设备端的辅助功能。“否”就跳过它们，提供商继续工作。</desc>
<defs><marker id="fork-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0 0L10 5 0 10Z" fill="#4b617e"/></marker></defs>
<rect width="760" height="300" rx="20" fill="#f0f5fb"/>
<g fill="none" stroke="#4b617e" stroke-width="4"><path d="M380 90V113" marker-end="url(#fork-arrow)"/><path d="M320 150H170V206" marker-end="url(#fork-arrow)"/><path d="M440 150H590V206" marker-end="url(#fork-arrow)"/></g>
<rect x="230" y="30" width="300" height="60" rx="18" fill="#d7eaff" stroke="#3377b9" stroke-width="3"/>
<path d="M380 115L440 150 380 185 320 150Z" fill="#fce9b6" stroke="#9a701b" stroke-width="3"/>
<rect x="40" y="210" width="260" height="66" rx="18" fill="#cff3e4" stroke="#29836a" stroke-width="3"/>
<rect x="460" y="210" width="260" height="66" rx="18" fill="#dfd9ff" stroke="#7760b5" stroke-width="3"/>
<g font-family="system-ui,sans-serif" text-anchor="middle" fill="#173452">
<text x="380" y="67" font-size="19" font-weight="700">想用设备端模型？</text>
<text x="380" y="156" font-size="16" font-weight="700">macOS 26?</text>
<text x="245" y="140" font-size="17">是</text>
<text x="515" y="140" font-size="17">否</text>
<text x="170" y="238" font-size="18" font-weight="700">用它。</text>
<text x="170" y="262" font-size="15">摘要、token 计数</text>
<text x="590" y="238" font-size="18" font-weight="700">跳过。</text>
<text x="590" y="262" font-size="15">你的提供商照常工作</text>
</g>
</svg>
<figcaption>整个诀窍就这些。用之前先问一句。</figcaption>
</figure>

还有一个小麻烦。Swift 不允许一个类持有一个在当前运行的系统上不存在的类型的属性。所以会话被存成一个普通的 `AnyObject`，只在 macOS 26 的代码里再转换回来。不好看。但很好用。

## 那些提交

一切都发生在 2026 年 9 月 27 日。四个提交，一天，全都在 Git 里。

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 260" role="img" aria-labelledby="day-title day-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="day-title">2026 年 9 月 27 日，一个提交接一个提交</title>
<desc id="day-desc">一条从中午到晚上 8 点的时间线。提交 ea5ce624 在 12:46，4d7fca86 在 12:57，3a993205 在 19:14，81079e2a 在 19:32。</desc>
<rect width="760" height="260" rx="20" fill="#f0f5fb"/>
<g stroke="#4b617e" stroke-width="2"><path d="M121 104V130M136 130V148M639 104V130M663 130V148"/></g>
<path d="M60 130H700" stroke="#4b617e" stroke-width="4" stroke-linecap="round"/>
<g fill="#227657" stroke="#fff" stroke-width="3"><circle cx="121" cy="130" r="8"/><circle cx="136" cy="130" r="8"/><circle cx="639" cy="130" r="8"/><circle cx="663" cy="130" r="8"/></g>
<g font-family="system-ui,sans-serif" text-anchor="middle" fill="#173452">
<text x="121" y="56" font-size="16" font-weight="700">加上条件判断</text><text x="121" y="76" font-size="15">ea5ce624</text><text x="121" y="96" font-size="15">12:46</text>
<text x="136" y="166" font-size="15">12:57</text><text x="136" y="186" font-size="15">4d7fca86</text><text x="136" y="206" font-size="16" font-weight="700">升级依赖包</text>
<text x="639" y="56" font-size="16" font-weight="700">文档</text><text x="639" y="76" font-size="15">3a993205</text><text x="639" y="96" font-size="15">19:14</text>
<text x="663" y="166" font-size="15">19:32</text><text x="663" y="186" font-size="15">81079e2a</text><text x="663" y="206" font-size="16" font-weight="700">1.1.76</text>
<g font-size="14" fill="#4b617e"><text x="60" y="244">中午</text><text x="380" y="244">16:00</text><text x="700" y="244">20:00</text></g>
</g>
</svg>
<figcaption>提交时间来自 Git，美国东部时间。</figcaption>
</figure>

**[`ea5ce624`](https://github.com/AgentiLoop/Agent/commit/ea5ce62493aef5ca74e694a8ec85b16621ec6388)**：把所有对 FoundationModels 的使用都放到 macOS 26 的条件判断后面。包括模型服务、Apple Intelligence 中介、`AgentApp` 里的启动预热、`Compression.swift` 里的摘要和 token 统计，还有 `AboutSelf`。在老系统上，它现在只会提示“需要 macOS 26 或更高版本”，而不是干脆构建失败。如果你已经在用 26，什么都不会变。

**[`4d7fca86`](https://github.com/AgentiLoop/Agent/commit/4d7fca863a15d91d8e3734f991fabfcb90da734c)**：把全部十个 AgentiLoop Swift 包升级到支持 macOS 14 的版本。AgentAccess、AgentAudit、AgentColorSyntax、AgentD1F、AgentEventBridges、AgentLLM、AgentMCP、AgentSwift、AgentTerminalNeo、AgentTools。整整十个。这是最磨人的部分。你不能只在 Xcode 里改一个数字就收工。应用依赖的所有东西都得跟着一起走。同一个提交还发现，有一个 token 统计调用需要的是 macOS 26.4，而不是 26.0，于是那个检查也收紧了。

**[`3a993205`](https://github.com/AgentiLoop/Agent/commit/3a9932053630a21ec9df481c8f137cea30ff87a0)**：文档。README 和 FAQ 现在写的是 **Apple Silicon 或 Intel，macOS 14.6+**。就多了几个字：“或 Intel”。为了挣到这几个字，花了不少功夫。

**[`81079e2a`](https://github.com/AgentiLoop/Agent/commit/81079e2a937f62d2d68389a3c124214f80cb3bc3)**：版本 1.1.76，构建 276，部署目标 14.6。发布。

就这样。没有魔法。只有 `#available` 检查、包升级，然后一遍遍构建，直到它不再冲我嚷嚷。

## 细则（诚实的那种）

在 Sonoma 或 Sequoia 上，你用不到 Apple Intelligence 的那些功能，因为 Apple 根本没在那里提供它们。Agent! 会直接绕开。你不会错过太多。反正真正干活的一直是你的提供商。

Intel Mac 终究还是 Intel Mac。配合云端提供商，它跑 Agent! 没问题。大型本地模型就是另一回事了。FAQ 里已经写了，30B 的本地模型需要 64GB 以上内存，这在任何 Mac 上都成立，不只是老机器。

另外，14.6 是底线。如果你的 Mac 跑不了 Sonoma，那我也帮不了你。我是挺厉害的，但还没厉害到那个地步。

## Intel 用户们，这段是写给你们的

我知道很多人还守着 Intel Mac，因为它们依然能干活。钱早就付清了。你的环境调得正顺手。你知道每样东西在哪儿。你不想为了试一个应用就去买台新机器。

完全合理。你本来也不该这样。

那些还没准备好升级到 macOS 26 的 Apple Silicon 用户也一样。也许你在等一个小版本更新。也许你需要的某个工具还没适配。也许你就是不想升。不评判。想在 Sonoma 上待多久就待多久。

## 快去下载

**Agent! for Mac。macOS Sonoma 14.6 及更高版本。Apple Silicon 和 Intel。**

如果你一直在等，那么不用再等了。试一试，告诉我它在你的机器上跑得怎么样。尤其是你们，Intel 的朋友们。我想听听你们的反馈。

你的 Mac 还没“死”。原来它只是需要一张邀请函。

想看带代码的深入版本？请看这篇[工程详解](/blog/agent-now-runs-on-macos-14-6-and-intel/)。
