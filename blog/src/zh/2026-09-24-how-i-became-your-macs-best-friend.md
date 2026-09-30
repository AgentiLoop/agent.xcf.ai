---
title: Agent! 是怎么开始的：三月里的三天
description: 三年攒下的零件，一个缺失的循环，不到两天 177 个提交。Agent! 真正的起源，直接来自 git。
tags: 起源, 历史
---
<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 380" role="img" aria-labelledby="lego-title lego-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="lego-title">一个友好的机器人用玩具积木搭一台 Mac</title>
<desc id="lego-desc">一个微笑的蓝色机器人举着一块黄色积木，面前是一块用红、黄、绿、蓝、橙色玩具积木搭到一半的 Mac 屏幕。对话气泡里写着：快好了！</desc>
<rect width="760" height="380" rx="20" fill="#eef6ff"/>
<path d="M40 318H720" stroke="#8b684c" stroke-width="13" stroke-linecap="round"/>
<path d="M190 92l-6 26 40-26" fill="#fff"/>
<rect x="120" y="30" width="230" height="64" rx="22" fill="#fff" stroke="#b6c8e4" stroke-width="3"/>
<text x="235" y="72" text-anchor="middle" font-family="system-ui,sans-serif" font-size="26" font-weight="700" fill="#173452">快好了！</text>
<path d="M140 270V310M210 270V310" stroke="#173452" stroke-width="7" stroke-linecap="round"/>
<path d="M250 200L318 146" stroke="#173452" stroke-width="7" stroke-linecap="round"/>
<rect x="100" y="150" width="150" height="120" rx="28" fill="#559ef5" stroke="#173452" stroke-width="4"/>
<path d="M175 150V124" stroke="#173452" stroke-width="5"/><circle cx="175" cy="115" r="10" fill="#efb943"/>
<circle cx="145" cy="192" r="13" fill="#fff"/><circle cx="205" cy="192" r="13" fill="#fff"/>
<circle cx="149" cy="193" r="5.5" fill="#173452"/><circle cx="209" cy="193" r="5.5" fill="#173452"/>
<path d="M148 228Q175 250 202 228" fill="none" stroke="#173452" stroke-width="6" stroke-linecap="round"/>
<g stroke="#173452" stroke-width="3">
<rect x="300" y="112" width="70" height="34" rx="4" fill="#efb943"/>
<rect x="311" y="102" width="16" height="10" rx="2" fill="#efb943"/><rect x="343" y="102" width="16" height="10" rx="2" fill="#efb943"/>
</g>
<g stroke="#173452" stroke-width="3">
<rect x="430" y="276" width="140" height="34" rx="4" fill="#9aa7b8"/>
<rect x="480" y="244" width="40" height="32" fill="#b8c3d1"/>
<rect x="400" y="210" width="70" height="34" rx="4" fill="#d94877"/>
<rect x="470" y="210" width="70" height="34" rx="4" fill="#4caf6e"/>
<rect x="540" y="210" width="70" height="34" rx="4" fill="#559ef5"/>
<rect x="610" y="210" width="70" height="34" rx="4" fill="#f08a3c"/>
<rect x="400" y="176" width="70" height="34" rx="4" fill="#efb943"/>
<rect x="470" y="176" width="70" height="34" rx="4" fill="#559ef5"/>
<rect x="540" y="176" width="70" height="34" rx="4" fill="#d94877"/>
<rect x="610" y="176" width="70" height="34" rx="4" fill="#4caf6e"/>
<rect x="400" y="142" width="70" height="34" rx="4" fill="#4caf6e"/>
<rect x="470" y="142" width="70" height="34" rx="4" fill="#f08a3c"/>
<rect x="540" y="142" width="70" height="34" rx="4" fill="#efb943"/>
<rect x="400" y="108" width="70" height="34" rx="4" fill="#559ef5"/>
<rect x="470" y="108" width="70" height="34" rx="4" fill="#d94877"/>
<rect x="540" y="108" width="70" height="34" rx="4" fill="#4caf6e"/>
<rect x="610" y="108" width="70" height="34" rx="4" fill="#efb943"/>
</g>
<rect x="610" y="142" width="70" height="34" rx="4" fill="none" stroke="#173452" stroke-width="3" stroke-dasharray="8 6"/>
<text x="190" y="354" text-anchor="middle" font-family="system-ui,sans-serif" font-size="21" fill="#173452">搭建者。</text>
<text x="540" y="354" text-anchor="middle" font-family="system-ui,sans-serif" font-size="21" fill="#173452">这台 Mac，还差一块积木。</text>
</svg>
<figcaption>所有大东西，一开始都是一堆小积木。诀窍在于知道下一块该放哪一块。</figcaption>
</figure>

每个应用都有自己的第一天。Agent! 的第一天是个星期三：**2026 年 3 月 11 日，下午 3:07**。我们连分钟都知道，因为 git 把它记下来了。

不过，积木早在那之前就已经散落一地了。

## 三年攒下的零件

在 Agent! 之前，还有别的应用。**ANIE**、**Game Changer**、**BattleScript**、**XCF MCP 服务器和客户端**，以及 **D1F**，一个能一次改动文件里很多行的工具。还有大约八个 Swift 包，全都出自同一个人之手。

它们每个都能完成一小块工作。有的能和 AI 说话，有的能改代码，有的能摆弄 Xcode。可没有一个能做到最重要的那件事：**自己一直干下去**。

想想发条玩具。你拧上发条，它走三步，然后停下。很可爱，但没什么用。缺的是一个循环：看看问题，挑一个工具，用它，检查发生了什么，然后再来一遍，直到把活干完。（这个循环有[一篇专门的文章，里面有一个机器人和一个三明治](/blog/what-is-an-agent-loop/)。）

循环一跑通，那些旧零件里最好的部分就能一块块扣上去。这就是整个起源故事的一句话版本。剩下的都是细节，而细节很好玩。

## 第一天：一个大脑、一个帮手和一个取消按钮

第一个真正的提交叫 *“Autonomous Agent with privileged launch daemon.”* 一共 20 个文件、1,765 行 Swift。盒子里装着这些：

- 一个 SwiftUI 窗口，你在里面输入想做的事。
- 一个 AI 大脑 Claude，负责思考。
- 一个 **Launch Daemon**：在后台运行的小帮手，手里有整栋房子的钥匙，让智能体能做那些“大人才能做”的系统杂活。
- 任务历史、截图和粘贴。

一小时后，第一个崩溃修复来了（粘贴截图会让它崩溃）。几分钟后，又加了一个大大的红色**取消**按钮，绑定到 Esc 键。当你造出一个会自己动手的东西时，停止按钮总是来得很早。

下午 5:27，第二个帮手登场：**Launch Agent**，它以*你*的身份运行命令，而不是以无所不能的 root 身份。为了列个文件夹就去要万能钥匙，就像为了点根蜡烛去叫消防队。六分钟后，Agent! 有了第二个大脑：**Ollama**，这样它就能用住在你自己 Mac 上的 AI 模型。

这一天结束之前，它还学会了编写和运行 Swift 脚本、操控 Xcode、用视觉模型看图片，还有了启动画面。它还得到了几个红绿灯一样的小状态点，前后大约花了十几个提交才定下绿、黄、红。有些事比智能体循环还难。

## 第二天：“可以吗？”

3 月 12 日，Agent! 学到了一件事：Mac 很有礼貌，而且对礼貌这件事非常较真。

要控制另一个应用，比如“音乐”或 Pages，macOS 会先问你：*“Agent! 想要控制‘音乐’。允许吗？”*光是让这个小窗口真正弹出来，就花了整整一个晚上。大约从晚上 8:20 到 9:40，提交历史就是一堆间隔几分钟的尝试：换个方式试试，放到主线程试试，打开系统设置，试 `osascript`，试着请求 `every window`，只试 `name`。另外，Keynote、Numbers 和 Pages 改过 bundle ID，所以它一直拿着错的名字在敲门。

最后成功了。同一天晚上，它还学会了在自己的日志里直接显示图片和网页，所以它做了专辑封面，你就能看到专辑封面。

## 第三天：一个名字和一个版本号

3 月 13 日早上，这个应用有了名字。上午 9:06 的提交写着 *“rename app to Agent!”* 感叹号是故意加的。

二十分钟后，来了一个到今天仍然很重要的改动：脚本不再是独立的程序，而是变成了直接加载进应用里的**动态库**。这就是为什么 AgentScripts 拥有和 Agent! 一样的 Mac 权限，不用再问一遍。

当天晚些时候，打上了 **1.0.0** 标签。从第一个提交算起，**不到两天，177 个提交**。接下来的八天里，1.0.1 到 1.0.16 陆续发布。

还有个小细节：这些早期提交上的作者名不是一个人，而是 **“Agent! for MacOS”**。

## 长大

第一轮冲刺之后，故事开始加速：

- **4 月 6 日**。将近一个月的历史被压成了一个干净的起始提交，完整历史保存在备份里。
- **4 月 7 日**。“编程模式”“自动化模式”和“标准模式”被[统统拆掉](/blog/why-we-ripped-out-modes/)。一个智能体，所有工具，每次都是。
- **4 月**。Apple Intelligence 加入进来，成为直接在 Mac 上运行、免费的大脑。
- **8 月 31 日**。项目从 GitHub 组织 `macOS26` 搬到了 **AgentiLoop**，网站也变成了 **agentiloop.ai**。
- **最近**。Agent! 学会了[在 macOS 14.6 和 Intel Mac 上运行](/blog/sonoma-intel-and-the-mac-that-was-not-dead-yet/)，还帮忙造出了自己的终端版弟弟妹妹：用 Rust 写的 [AgentiLoopCLI](https://github.com/AgentiLoop/AgentiLoopCLI) 和用 Go 写的 [AgentiLoopGo](https://github.com/AgentiLoop/AgentiLoopGo)。

它最初只有一个大脑。如今它支持 **23 家 AI 提供商**，外加 Apple Intelligence。自四月那次大扫除以来，主分支又多了 1,300 多个提交。

## 它为什么是现在这个样子

Agent! 身上几乎所有与众不同的地方，都能追溯到最初那三天。

它有两个帮手，一个替你干活，一个替 root 干活，因为第一天就两个都需要。它是 100% Swift，就像造它的那些零件一样。它用的是原创代码，而不是一堆 65 个 NPM 包。它通过辅助功能和 AppleScript 按名字操控其他应用，因为第二天整天都在学怎么礼貌地请求 Mac。而且，它至今还留着那个大大的取消按钮。

所有大东西，一开始都是一堆小积木。这一堆攒了三年。3 月 11 日，终于有人找到了那块把其他积木连在一起的积木：循环。
