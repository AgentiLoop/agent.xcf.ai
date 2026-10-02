---
title: GoKart：自动驾驶在一个下午做出的马里奥赛车风格竞速游戏
description: 给 Agent! 的自动驾驶（Auto-Pilot）一个目标——"创建一个名为 GoKart 的马里奥赛车克隆"——回来时就得到了一款 Godot 4 竞速游戏：三条赛道、八种道具、AI 对手，以及 3,344 项通过的测试检查。下面是日志记录的真实经过，包括它卡住的那些部分。
tags: Auto-Pilot, 案例展示, Godot
---
<figure style="margin:2rem 0">
<img src="/gokart-green-hills-drift.png" alt="GoKart 的 Green Hills 赛道：追尾视角，玩家卡丁车正在灰色路面上漂移，路边是红白条纹的护墙，绿色地面，蓝天。HUD 显示第 1 名、圈数和计时器，左下角是赛道小地图。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Green Hills，第 1 圈，以第一名的身份漂移中。这一帧里的每个网格、着色器和声音都是由代码生成的。</figcaption>
</figure>

昨天的文章介绍了[自动驾驶（Auto-Pilot）](/blog/agent-1-1-87-and-agentiloop-cli-0-0-5/)：在 Mac 版 Agent! 中输入 `/auto <目标>`，它就会朝着这个目标无人值守地一轮轮运行，直到你按下 Stop All。这篇文章讲的是，当我把它对准一款游戏时，另一头产出了什么。

目标，基本按我当时输入的原样粘贴：

> create a Mario Kart clone called GoKart with all Mario Kart effects. I believe Godot 4 can do the Mario Kart effects, but I haven't built any of them yet: drift sparks and boost flames (GPUParticles3D), speed lines and boost blur (screen-space shaders, glow and tonemapping), item effects and tire trails (shaders plus ribbon meshes), kart movement (VehicleBody3D or custom arcade physics). Write unit tests and test the game frequently.

预算：不限时间，不限轮数。第一个提交落地于 12:39。同一天下午 16:32，仓库已有 33 个提交。如今它有 47 个 GDScript 文件，约 5,500 行 GDScript 和着色器代码，以及一套能通过 3,344 项检查的单元测试。整个项目在 GitHub 上：[AgentiLoop/GoKart](https://github.com/AgentiLoop/GoKart)。

## 自动驾驶做了什么，一轮接一轮

自动驾驶在项目内的 `.agent/autopilot/progress.md` 保存着一份持续的日志，每一轮都会追加它做了什么、假设了什么、还剩什么，以及有没有东西卡住它。下面的所有内容都来自这份日志。我引用日志而不是凭记忆，因为日志比我诚实。

**第 1 轮**时机器上没有 Godot。它运行了 `brew install --cask godot`，给可执行文件建了软链接，执行了 `git init`，并把 `kart_physics.gd` 写成一个不依赖场景的纯模型：加速、刹车、倒车、摩擦、转向、锁定在起始方向上的漂移，以及三级小型加速。它刻意选择了自定义街机物理而不是 `VehicleBody3D`，并说明了原因："这样马里奥赛车式的操控就容易做单元测试。"11 个测试，17 项检查，第一个提交。

**第 2 轮**加入了我点名要的效果：按小型加速等级着色的 GPUParticles3D 漂移火花、排气火焰、带状网格的轮胎拖痕，以及一个用于径向加速模糊、速度线和暗角的屏幕空间着色器。43 项检查。

**第 3 轮**搭了一条赛道。一条每 3 米重采样一次的 Catmull-Rom 闭环、一条路面带、带碰撞体的红白条纹护墙、带滚动箭头着色器的加速板、八个有序检查点，以及一个拒绝计算抄近路和逆行圈数的圈数追踪器。新测试中有一个追踪机器人，它用真实物理模型完整跑了三圈。用时 1:02.5。90 项检查。

**第 4 轮**加入了带彩虹菲涅尔着色器的道具箱、一个转盘，以及头三种道具：蘑菇、香蕉，还有会在护墙间弹射的绿龟壳。被击中后卡丁车会打转 1.2 秒。235 项检查。

然后它卡住了。

## 它卡住的那部分

下一轮开始添加 AI 卡丁车和一场无头冒烟赛，然后再也没回来。原因在下一次会话中找到了：`main.gd` 第 115 行多了一个制表符——一个解析错误，让冒烟脚本永无止境地刷错误，而运行它的 shell 命令又没有时间限制。

我按下了 **Stop All**，用同样的目标开了一个新会话，外加一段我不会全文照录的大写备注。大意是：*你在测试冒烟运行时卡住了，不要卡住，给 shell 加时间限制。*

第二次会话的第一轮修好了那个制表符，把 AI 的前瞻从 10 个路面采样减到 6 个，让 AI 不再切弯撞上内侧护墙，加了弯道限速器，并把每次 shell 运行包在 `perl -e 'alarm 100; exec @ARGV'` 里，因为 macOS 自带的系统里没有 `timeout` 命令。从那以后，几乎每一轮的结尾日志都写着"所有运行都在 perl alarm 限制之下"。它从目标文本中学到了教训，并一直贯彻。

那次会话在大约一小时一刻钟里跑了 15 轮，每一轮都是一个功能：带起步倒计时，油门时机踩得准就有火箭起步加速；小型加速升级时的爆开效果和屏幕边缘闪光；小地图；追踪红龟壳和无敌星；一个程序化卡丁车模型，轮子会转、前轮会转向、车手会扭头；让所有对手缩小的闪电；环绕卡丁车的三连龟壳；沿着道路追杀领先者的蓝色尖刺龟壳；带积分的结算画面；完全合成、没有任何音频文件的音效，从引擎循环到冲线小曲；带第二条赛道的标题菜单；圈数选项；第三条赛道；以及每辆 AI 卡丁车上的 3D 定位引擎嗡鸣。

<figure style="margin:2rem 0">
<img src="/gokart-sunset-speedway.png" alt="GoKart 的 Sunset Speedway 赛道：玩家卡丁车在橙到紫的日落天空下，全速驰骋在沙质赛道上。HUD 显示第 4 名、第 1 圈，以及小地图上一条带发夹弯的长赛道轮廓。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Sunset Speedway，第二条赛道，在第 12 轮与标题菜单一起加入。比 Green Hills 更长，有一个发夹弯和一个减速弯。</figcaption>
</figure>

## 它诚实的那部分

日志里我最喜欢的是那种反复坦白的模式。Agent! 看不了 PNG，而它一轮又一轮地这么说：

> 窗口模式的截图运行没有记录错误，但我无法查看图片，所以我没有看过赛道或 HUD 渲染成什么样。

> 我没有听过那些声音，也没有运行冒烟赛或截图工具。

> 我的工具无法查看图片，所以这项审查需要一个人来做。

于是它测试它能测的：无头场景检查，实例化真实场景并对状态做断言。放闪电，确认三个对手缩放为 0.5 并在打转，之后闪电被清理干净。朝挤在一起的起跑格发射蓝龟壳，确认第 12 帧爆炸、两辆卡丁车打转。强制玩家冲线，确认自动驾驶把卡丁车交给 `AiDriver`，并且结算面板显示"1st YOU"。

第三次会话以同样的方式停滞了，这次是卡在一个宽松得离谱的 240 秒 alarm 后面，我跑了一轮就停掉了。然后一个人看了看。那个人是我，第四次会话的目标就是我的试玩笔记，稍微整理了一下：

> the UI needs to scale with the window. the UI should not be prone to the screen speed effects and blurry. Should be able to use cursor keys. it's not clear when power ups are released. the tops of the walls flicker. Little too hard to steer the kart. hard to keep up with the computer AI karts. maybe have AI difficulty levels Easy Medium and Hard.

一轮之后：canvas-items 拉伸模式让 UI 随窗口缩放，HUD 移到了速度特效叠加层之上的画布层，方向键、Enter 和 Ctrl 用于道具并附带屏幕提示，转向加入了渐入缓动，护墙条纹的 z-fighting 修复（相邻的红白段在争抢同一批像素，于是白色段被稍微放大了一点），4x MSAA，以及把 AI 最高速度分别缩放到 0.72、0.85 和 1.0 的简单 / 中等 / 困难难度。测试从 2,156 项增加到 3,344 项检查，部分原因是它顺带找到并修复了 `tests/test_items.gd` 里一个早已存在、导致整套测试无法加载的解析错误。

## 它自己停下来的那部分

最后一次会话的第 2 到第 8 轮没有做任何代码改动。每一轮都重新读了仓库、重跑了测试套件，然后写下同一段话的某个变体：

> 我无法在屏幕上看到结果，所以我不宣布目标已达成。还有四项需要人在游戏里亲自试一试。

这是正确的行为。目标是"转向手感不好"和"护墙闪烁"，没有任何无头测试能关闭这样的目标。自动驾驶没有迭代上限，所以它本可以永远检查下去。会话在第 8 轮后结束，GoKart 接下来需要的是一次试玩，而不是再来一轮。

<figure style="margin:2rem 0">
<img src="/gokart-frosty-peaks.png" alt="GoKart 的 Frosty Peaks 赛道：玩家卡丁车在深蓝色的暮色天空下，全速驰骋在雪白的赛道上。HUD 显示第 2 名、第 1 圈、以 km/h 计的速度和小地图。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Frosty Peaks，在第 14 轮作为赛道库的新条目加入。按赛道运行的测试自动把它纳入了进来。</figcaption>
</figure>

## 关于这些截图

截图是 Agent! 拍的，不是我，也不是手动拍的。我要了三张随机驾驶的截图，它写了一个 70 行的 `tools/random_drive.gd`：带着游走的车道偏移沿路行驶，随机插入漂移冲刺，在随机时刻发射手里拿着的道具，然后每隔几百个物理帧保存一帧。每条赛道跑了一次，上面三张就是各取一帧。它们也在 [GoKart 的 README](https://github.com/AgentiLoop/GoKart#screenshots) 里。

## 在你试之前我想说的

- **在 git 里运行它。** 自动驾驶没有撤销。GoKart 的日志之所以可读，是因为每一轮都以一次提交结束，而唯一一次某轮跑偏时，什么都没丢。
- **把操作规则写进目标里。** "给 shell 加时间限制"作为目标的一部分比作为一条临时消息更有效，因为每一个新的轮次都会重新读取目标。
- **预期它会要求人眼。** 凡是视觉或手感方面的事，这个循环会诚实地停下来而不是撒谎。在会话之间安排一次试玩，把你的笔记作为下一个目标喂回去。
- **Stop All 是工作流的一部分**，不是失败。GoKart 的前三次会话全都是这样结束的。

带自动驾驶的 Agent! 1.1.87 已在[发布页面](https://github.com/AgentiLoop/Agent/releases/latest)和 Homebrew 上提供。GoKart 需要 Godot 4.4 或更高版本：`git clone https://github.com/AgentiLoop/GoKart.git && cd GoKart && godot --path .`
