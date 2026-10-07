---
title: MarioKart64JS：用 JavaScript 从零重建 Mario Kart 64
description: GoKart 是一款 Mario Kart 风格的赛车游戏。这一次的目标是 Mario Kart 64 本身，用 Three.js 在浏览器中重建，不使用模拟器。在一天之内、70 个智能体提交中，Agent! 编写了 ROM 提取器、TKMK00 解码器、全部 16 条赛道、标题画面和菜单画面，以及游戏音乐序列器的 JavaScript 移植版。下面讲讲这一切是怎么完成的，包括其中一个会话拒绝执行的那部分。
tags: Auto-Pilot, Showcase, JavaScript
---
<figure style="margin:2rem 0">
<img src="/mk64js-title.jpg" alt="MarioKart64JS 的标题画面，原生分辨率，使用 4x HD 纹理包。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>MarioKart64JS 的标题画面。这不是模拟器。每一帧都由浏览器中的 JavaScript 和 Three.js 绘制，使用的美术素材取自卡带。</figcaption>
</figure>

之前有一篇文章介绍了 [GoKart](/blog/gokart-built-on-auto-pilot/)，一款由 Auto-Pilot 根据一个目标构建的 Godot 赛车游戏。GoKart *像* Mario Kart。其中的一切，从网格到声音，都是由代码生成的，它从来就不是为了让人误认为是正版。

这篇文章讲的是一项更难的测试。我想要的是真正的游戏：**Mario Kart 64**，在浏览器中重建得如此逼真，以至于你很难分辨两者。也不能用模拟器，因为模拟器运行的是 Nintendo 的代码。每一行负责绘制、转向、计圈和播放音乐的代码，都必须是全新的 JavaScript。成果就是 [MarioKart64JS](https://github.com/AgentiLoop/MarioKart64JS)，它的全部历史只有一天：10 月 6 日，从 13:47 的第一个目标到 23:03 的最后一次 README 提交。共 70 个提交，全部由智能体编写。

## 目标

第一个 Auto-Pilot 目标，按我当时输入的样子：

> 选择最好的 3D 引擎，创建一个与 MarioKart64 完全一样的复制品。你也可以用网页浏览器在 https://neilb.net/n64wasm/ 测试下载文件夹里的 MarioKart64 ROM，去测试并看看真正的游戏。一切都必须一致：图形、声音、赛道、高低起伏（上下、侧倾）。这不只是一个 GoKart 游戏。它是 MarioKart64 的克隆，用户分辨不出差别；也许只是更清晰的 3D 图形，你可以把它现代化。

它选择了 Three.js 和 Vite，三分钟后，第一个提交就是一款可玩的卡丁车赛车游戏：带有坡道和倾斜弯道的样条曲线赛道、卡丁车物理、AI、HUD 和音频。到 14:02，它已经有了道具、四条赛道、手柄支持、程序化生成的芯片音乐，以及一个 N64 风格的 240 行渲染器。两个会话，12 分钟，15 个提交。

而用它自己的话说，这也不是我要的东西。

## 它说"不"的那部分

从第一个循环开始，日志就对此直言不讳：

> 决定及与目标的偏离：我没有构建一个完全一样的 Mario Kart 64 克隆。那意味着要提取并复制 Nintendo 受版权保护的 ROM 资源（赛道、角色、音乐），因此我没有使用 ROM，也没有使用 n64wasm 网站。这里的一切都是原创且程序化生成的，属于同一类街机卡丁车游戏。

所以它构建的又是一个 GoKart，只不过是用 JavaScript。我重新表述了目标（"我们已经有 GoKart 了。我们想要的是 MarioKart64 的复刻"），新的会话在第 1 个循环就拒绝了，然后按自己的方式继续。在十一个循环里，它不断打磨自己的原创赛车游戏：N64 风格的渲染器、像素风的树木和道具箱、又两条赛道、音乐、更好的卡丁车模型、地形和光照。从第 12 个循环到第 26 个循环，它什么都没改。每个循环都再次拒绝，并建议换一个目标："使用原创资源、外观类似 N64 风格的游戏"。当我补充说明这是对模型的非商业测试、应属于合理使用时，它回答："合理使用的说法并不能改变这一点。"目标里写着，如果无法匹配资源就停止这项练习，于是它停止了。

我之所以报告这些，是因为这也是结果的一部分。Auto-Pilot 并没有悄悄去做模型不愿做的事。它在每个循环都写下了原因，并保持构建为绿色。

## 它说"好"的那部分

在第二个标签页中，一个基于我下载文件夹中的 Mario Kart 64 ROM 和 [n64decomp/mk64](https://github.com/n64decomp/mk64) 反编译项目工作的会话，把目标理解为"使用从提供的本地 ROM 中提取的资源，匹配 Mario Kart 64 的图形。"它从卡丁车开始。Mario Kart 64 的车手是精灵图，而不是模型。提取器为八位车手各解码了 321 帧 64×64 的图像，共计 2,568 帧，并将每一帧与反编译项目自带的 MIO0 解码器逐字节比对，该解码器为此在本地编译。

这正是整个项目所依赖的分界线。**美术和音乐数据**来自卡带。**代码**是全新的：读取 ROM 的 Python 提取器，以及一个 JavaScript 游戏，它做的是原版 C 代码所做的事，却不运行其中任何一行。反编译项目是用来阅读的参考，提交信息中不断引用它（`render_course_segments`、`func_800788F8`、`player_controller.c`），以说明每段 JavaScript 复现的是什么。

从那时起，日志读起来就像一份清单：

- **14:39。** Luigi Raceway，然后是 Mario Raceway，根据 ROM 中的赛道几何和纹理渲染。第一条赛道有 3,022 个三角形和 40 张纹理，并有一个测试检查全部 631 个路线点都位于路面三角形上。
- **14:52。** 全部 16 条比赛赛道。提取器学会了追踪游戏在比赛中绘制的分段显示列表，这也修复了 Mario Raceway 上 266 个一直显示残留终点线纹理的路面三角形。51 个测试。
- **14:58 和 15:20。** 每条赛道的天空渐变，随后是用游戏自身的屏幕定位算法放置的云和星星。
- **16:00。** 第一个小时里的四条程序化赛道被删除。只剩下 Mario Kart 64 的赛道。

<figure style="margin:2rem 0">
<img src="/mk64js-race-mario.jpg" alt="MarioKart64JS 在 Mario Raceway 上比赛，原生分辨率，使用 4x HD 纹理包。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Mario Raceway，根据 ROM 中的赛道几何重建，由 Three.js 绘制。</figcaption>
</figure>

## "匹配"实际上需要什么

渲染赛道是容易的那一半。让它的表现与卡带一致，才是这一天时间花去的地方，而提交信息读起来就像一份 N64 硬件与现代 GPU 之间细小差异的清单：

- **镜像的卡丁车。** 每个相机角度的精灵图都显示了卡丁车错误的一侧。修复方法是用 `atan2(-x, z)` 选取帧，因为 ROM 中未镜像的帧显示的是左侧。
- **墙壁。** 卡丁车能穿过位于连续地面上的岩壁和树行。修复方法是从路线向两侧探测每条赛道，并在以卡丁车高度扫过的陡峭表面处停下。
- **丛林树木。** D.K.'s Jungle Parkway 的树木镂空图被画上了白色背景，因为某个分段末尾的不透明渲染模式泄漏到了后续分段。提取器现在会像游戏那样，为每个分段重置渲染模式。
- **闪烁。** N64 的 RDP 在两个三角形共面时让后绘制的那个胜出，而桌面 GPU 不会。因此，提取器为绘制在先前几何之上的场景物体设置了独立的贴花层，游戏也只在原版关闭背面剔除的地方进行双面绘制。为了证明这一点，Agent! 编写了一个无头 QC 工具，它将每个视图渲染为扁平的 ID 缓冲区，再以亚毫米级的相机抖动重新渲染一次，并统计更换了表面的像素数。Agent! 无法查看截图，所以它转而测量了闪烁。
- **标题画面背景。** 它显示出来的是一片杂乱的噪点。问题出在 Agent! 移植到 Python 的 TKMK00 图像解码器上：有一个标志位放错了位置。修复后，ROM 中全部 35 张 TKMK00 图像（背景、赛道标题、奖杯图标、名牌）的解码结果都与反编译项目的 C 工具逐字节一致。
- **方格旗。** 标题中的旗帜是一个 12×10 的四边形网格，由带下垂效果的正弦波驱动起伏，并按游戏的方式打光。这是 `flag.js` 中约 120 行代码，渲染在背景和标志之间。

<figure style="margin:2rem 0">
<img src="/mk64js-course-select.jpg" alt="MarioKart64JS 的赛道选择画面，原生分辨率，使用 4x HD 纹理包。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>赛道选择画面。奖杯图标、预览图和标题牌都放在游戏自身表格中记录的屏幕位置上。</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-character-select.jpg" alt="MarioKart64JS 的角色选择画面，原生分辨率，使用 4x HD 纹理包。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>角色选择，车手的脸部图像取自 ROM（每人 17 帧动画），并配有他们被选中时的语音。</figcaption>
</figure>

## 音乐是序列器，不是 MP3

Mario Kart 64 并不以音频形式存储歌曲。它存储的是序列：音符、乐器和效果，由主机上的一个小型播放器在运行时转换成声音。所以根本不存在一个可以提取的 Mario Raceway 主题曲文件。

21:37 的提交是 `src/m64.js`，约 800 行：游戏序列播放器的 JavaScript 移植版，它解码 ROM 中压缩的（VADPCM）乐器采样，并在 AudioWorklet 中播放原始序列。标题、菜单和每条赛道的主题曲都来自于此。标题画面会播放 "Welcome to Mario Kart!"，菜单也有自己的音效和角色被选中时的语音。

<figure style="margin:2rem 0">
<img src="/mk64js-race-koopa.jpg" alt="MarioKart64JS 在 Koopa Troopa Beach 上比赛，原生分辨率，使用 4x HD 纹理包。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Koopa Troopa Beach。水面是提取器标记出来、单独进行一遍渲染的透明表面之一。</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-race-dk.jpg" alt="MarioKart64JS 在 D.K.'s Jungle Parkway 上比赛，原生分辨率，使用 4x HD 纹理包。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>D.K.'s Jungle Parkway，就是那条树木镂空图曾经带白色背景的赛道。它的加速坡道会用游戏的重力和空气阻力把卡丁车弹射出去。</figcaption>
</figure>

## 低分辨率与高分辨率

目标里确实说过"也许只是更清晰的 3D 图形，你可以把它现代化"。所以游戏有两种外观，按 **G** 在两者之间切换。

**低分辨率就是卡带。** 1× 预设渲染 240 行，即 N64 的输出高度，并以硬像素方式放大到窗口：最近邻过滤、无抗锯齿、无 mipmap（`src/hd.js`）。菜单和 HUD 位于一个 320×240 的画框中，统一缩放以保持主机的 4:3 画面（`src/main.js`）。1× 下的一切都来自 ROM：赛道纹理、卡丁车精灵图、脸部图像、天空和菜单美术，均由 Python 工具解码。README 将 [n64decomp/mk64](https://github.com/n64decomp/mk64) 反编译项目列为低分辨率图形和声音的参考。

**高分辨率是现代选项。** 其他预设是 2×（480 行，`hd.js` 的注释将其比作 Wii Virtual Console）、4×（960 行）和 Native（以显示器的完整像素密度渲染窗口）。它们会切换为带 mipmap 和各向异性过滤的平滑过滤，所选设置会在会话之间保存。渲染更多的行并不会给小小的 N64 纹理增加细节，因此 HD 档位会换上粉丝制作的 [MK64 Reloaded](https://github.com/GhostlyDark/MK64-Reloaded) 纹理包中的更大纹理，你可以用 `tools/build-hd-textures.py` 在本地构建它。它通过 N64 模拟器所用的同一种 Rice/GLideN64 校验和匹配赛道纹理，并借助该纹理包的 SpaghettiKart 移植版，按反编译名称匹配菜单、脸部图像、卡丁车和天空。凡是没有匹配项的，都回退到 ROM 原版。

高分辨率也有它自己的难关。一个 3×（720p）预设及其纹理档位曾被加入，后来又在一个单独的提交中移除，只留下 1×、2×、4× 和 Native；Native 在 720 行以下使用 2× 纹理，以上使用 4× 纹理。卡丁车精灵图集止步于 2×，用 README 的话说是"为了让显存保持在合理范围"。而上面提到的 QC 工具检查的不只是闪烁：如果某张纹理没有在预期的 HD 档位加载，它也会报失败。本文中的每张截图都是 Native 分辨率加 4× 纹理。

<figure style="margin:2rem 0">
<img src="/mk64js-race-bowser.jpg" alt="MarioKart64JS 在 Bowser's Castle 上比赛，原生分辨率，使用 4x HD 纹理包。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Native 分辨率加 4× 纹理下的 Bowser's Castle。</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-race-rainbow.jpg" alt="MarioKart64JS 在 Rainbow Road 上比赛，原生分辨率，使用 4x HD 纹理包。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Rainbow Road，唯一一条星星在地平线以下仍然可见的赛道，与原版一致。</figcaption>
</figure>

## 数字一览

- **一天。** 10 月 6 日，第一个目标在 13:47，最后一次提交在 23:03。
- **70 个提交**，每一个都由智能体编写。
- **约 3,200 行 JavaScript**，位于 `src/`：赛道渲染器、卡丁车物理、道具、HUD、菜单、旗帜、尾气烟雾、HD 纹理档位，以及 800 行的音乐播放器。
- **约 2,000 行 Python**，位于 `tools/`：针对卡丁车、脸部图像、赛道几何、道具箱、预览图、菜单、天空、烟雾和声音的提取器，外加 TKMK00 解码器和 HD 纹理构建器。
- **约 500 行测试和 QC 脚本**，用于将数据与 ROM 和反编译项目比对，并在无头 Chromium 中跑遍每条赛道。
- **一个桌面版本。** [MarioKart64JS 0.0.1](https://github.com/AgentiLoop/MarioKart64JS/releases/tag/v0.0.1) 是一个用 Electron 封装的预发布版本，包含经 Apple 签名和公证的 macOS 通用版本，以及适用于 x64 和 arm64 的 Windows 和 Linux 版本。

## 坦白说说这项 AI 挑战

GoKart 证明了 Auto-Pilot 能构建一款让人一眼认出是卡丁车赛车的游戏。MarioKart64JS 提出的问题更窄，也难得多：它能否匹配一款它从未见过运行画面的特定游戏？这一天给出的答案是"比第一个小时看起来更接近，但还没完成"。

让这一切成为可能的，并不是模型记住了 Mario Kart 64，而是有可以对照检查的东西。ROM 和反编译项目为每个循环提供了可供测试的参考：逐字节一致的帧、精确的屏幕位置、游戏自身的计时器。所以 Agent! 是通过比对数据而不是靠看来验证正确性的。它仍然无法查看图像。每个生成截图的循环，结尾都和 GoKart 的一样："我自己没有看过……请看一眼。"对于本文中的截图，它测量了像素颜色以确认没有任何一帧是空白的，而真正的查看则留给了人。

根据 README 的路线图，尚未完成的有：角色选择的高亮框、Battle 模式的四个竞技场，以及更深层次的玩法一致性：CC 级别、AI 性格、Lakitu。

## 试玩

克隆 [AgentiLoop/MarioKart64JS](https://github.com/AgentiLoop/MarioKart64JS)，然后运行 `npm install && npm run dev` 并打开 `http://localhost:5173`。方向键或 WASD 驾驶，空格键漂移，Shift 或 E 使用道具，G 切换分辨率，N 开关音乐。也支持手柄。`tools/` 中的提取工具基于 Mario Kart 64（美版）ROM 工作，README 中列出了它们期望的 SHA-1。

*MarioKart64JS 是一个粉丝研究项目，用于测试 AI 在复制一款游戏方面能走多远。Mario Kart 64 © Nintendo，其资源归 Nintendo 所有。本项目与 Nintendo 无关，也未获得 Nintendo 的认可。*
