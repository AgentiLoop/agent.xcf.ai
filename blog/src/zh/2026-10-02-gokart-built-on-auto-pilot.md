---
title: GoKart：自动驾驶在一个下午做出的马里奥赛车风格竞速游戏
description: 给 Agent! 的自动驾驶（Auto-Pilot）一个目标——"创建一个名为 GoKart 的马里奥赛车克隆"——回来时就得到了一款 Godot 4 竞速游戏：三条赛道、八种道具、AI 对手，以及 3,344 项通过的测试检查。两天和 87 个代理提交之后，它成了 GoKart 0.0.2：四条赛道、对战模式、计时赛、Mario Kart 64 风格的菜单，以及 14,134 项通过的检查。下面是日志记录的真实经过，包括它卡住的那些部分。
tags: Auto-Pilot, 案例展示, Godot
updated: 2026-10-04
---
<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-title.png" alt="GoKart 0.0.2 的标题画面：GOKART 一词以黄到红渐变的大字排成拱形，带海军蓝的块状侧面和柔和阴影，叠在 CPU 卡丁车绕赛道行驶的实时演示画面之上，下方是 PRESS ENTER。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>GoKart 0.0.2 的标题画面。Logo 飞入并弹跳停下，背后是巡游各条赛道的实时演示。每个网格、着色器、字体排版和声音都是由代码生成的。</figcaption>
</figure>

*10 月 4 日更新：这篇文章现在涵盖了第一个下午之后的两天、在同一个仓库里同时运行的两个自动驾驶会话，以及 [GoKart 0.0.2](#gokart-0-0-2) 版本的发布。截图已从 0.0.2 标签重新拍摄。*

昨天的文章介绍了[自动驾驶（Auto-Pilot）](/blog/agent-1-1-87-and-agentiloop-cli-0-0-5/)：在 Mac 版 Agent! 中输入 `/auto <目标>`，它就会朝着这个目标无人值守地一轮轮运行，直到你按下 Stop All。这篇文章讲的是，当我把它对准一款游戏时，另一头产出了什么。

目标，基本按我当时输入的原样粘贴：

> create a Mario Kart clone called GoKart with all Mario Kart effects. I believe Godot 4 can do the Mario Kart effects, but I haven't built any of them yet: drift sparks and boost flames (GPUParticles3D), speed lines and boost blur (screen-space shaders, glow and tonemapping), item effects and tire trails (shaders plus ribbon meshes), kart movement (VehicleBody3D or custom arcade physics). Write unit tests and test the game frequently.

预算：不限时间，不限轮数。每一轮 Agent! 内部使用的模型都是 Claude Sonnet 5.5。第一个提交落地于 12:39。同一天下午 16:32，仓库已有 33 个提交、47 个 GDScript 文件、约 5,500 行 GDScript 和着色器代码，以及一套能通过 3,344 项检查的单元测试。两天后，在 0.0.2 标签处，它是 126 个提交、150 个 GDScript 文件、约 24,500 行代码和 14,134 项检查，而且每一个提交的作者都是代理。整个项目在 GitHub 上：[AgentiLoop/GoKart](https://github.com/AgentiLoop/GoKart)。

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
<img src="/gokart-0-0-2-sunset-speedway.png" alt="GoKart 0.0.2 的 Sunset Speedway 赛道：玩家卡丁车在日落天空下漂移，第 1 圈、8 辆中第 3 名，配有 Mario Kart 64 风格的 HUD：左下角是半透明的赛道地图，名次、圈数和速度以圆润的金色与奶油色字体显示。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>0.0.2 中的 Sunset Speedway：一个随机驾驶机器人正在漂移，8 辆中第 3 名。第二条赛道在第一天的第 12 轮与标题菜单一起加入。车流、护墙外的建筑和 HUD 是两天后才有的。</figcaption>
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

这是正确的行为。目标是"转向手感不好"和"护墙闪烁"，没有任何无头测试能关闭这样的目标。自动驾驶没有迭代上限，所以它本可以永远检查下去。会话在第 8 轮后结束，GoKart 接下来需要的是一次试玩，而不是再来一轮。那天晚上，仓库被打上了 0.0.1 标签，并导出了 macOS、Windows 和 Linux 版本。

## 两天后：一个仓库里的两个自动驾驶

10 月 3 日，我带着一种不同类型的目标回来了。不是功能清单，而是一个参照物：

> keep building GoKart to resemble Mario Kart Nintendo 64 version. search Mario Kart N64 or Mario Kart Nintendo 64 and keep improving, iterating, making GoKart better

第五次会话从 14:19 开始，跑了 28 轮，几乎每一轮都是代理查到并做出来的一样 Mario Kart 64 的东西：两列起跑格上的 8 车阵容、按难度区分的橡皮筋机制、50cc / 100cc / 150cc 以及镜像的 Extra 级别、会互相推挤的轻型 / 中型 / 重型卡丁车、采用 9/6/3/1 积分制和淘汰规则的大奖赛、带幽灵车的计时赛、在 Big Donut、Block Fort 和 Skyscraper 中进行的气球对战模式、三连蘑菇和金蘑菇、假道具箱、香蕉串、Boo、三连红龟壳、龟壳格挡、抢跑、举着起跑信号和圈数牌的 Lakitu、名为 Dusty Canyon 的第四条赛道、带平交道口的 Kalimari Desert 火车、Toad's Turnpike 车流、Monty Mole 鼹鼠、雪人、企鹅、Sherbet Land 冰面、每种主题各自的路边景物、尾流、跳台、起跳切换式的动力滑行，以及用代码中的音序模式渲染出来的每条赛道的芯片音乐循环。

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-train.png" alt="GoKart 0.0.2 的 Dusty Canyon 赛道：玩家卡丁车在平交道口等候，一列蒸汽火车正驶过道路，铁轨旁有交叉警示牌，天空是沙漠的天色。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>第四条赛道 Dusty Canyon，以及它的 Kalimari Desert 风格火车。CPU 卡丁车会在被挡住的道口停车等候；不停的卡丁车会被抛上天。</figcaption>
</figure>

四小时后，18:25，我打开第二个标签页，在同一个仓库上启动了第二个自动驾驶，目标更窄：

> the menus are not Mario Kart Quality and neither is the title shot. and there is over use of black outlines on text everywhere. see Mario Kart 64 screenshots and images on the web and make better menus. focus only on the menus / screens and title shot for GoKart. make conscious decisions. do not conflict with previous /auto working on the application

于是从 18:25 到午夜，两个代理同时往同一个工作树里提交。菜单会话重做了标题画面，用上了会飞入并弹跳的拱形渐变 Logo；一个每条赛道旁都配图的选择画面；所选赛道的实时飞越镜头；带点亮横条的选项行；会旋转的卡丁车肖像和金色光标；赛道开场飞越；暂停画面；一块行与行依次滑入的结算板；以及一套圆润的金色与奶油色带投影文字的共享配色，取代了游戏里所有 8 像素的黑色描边。它跑了 23 轮，于 23:54 宣布目标达成。

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-select.png" alt="GoKart 0.0.2 的选择画面：顶部是 GOKART Logo，左侧是赛道列表，每个赛道名旁有一张小图，选中的一行被点亮；右侧是赛道的实时画面，角落里有地图轮廓；下面是圈数、CPU、引擎级别、卡丁车重量和模式的一排排选项胶囊，还有玩家的卡丁车在小肖像窗口里旋转，整体叠在变暗的演示画面之上。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>菜单会话之后的选择画面。赛道图片、赛道的实时飞越、每个选项都列为一排胶囊并点亮选中项，以及在肖像窗口里旋转的卡丁车。</figcaption>
</figure>

"do not conflict"这一句真的起了作用。日志里满是两个会话互相绕开对方的记录：菜单会话从 HEAD 处的干净 `git worktree` 进行验证，好让"另一个会话正在进行的企鹅工作"不进入它的测试运行；在我要求时，一个会话完成了另一个会话做了一半的功能；提交时逐个文件暂存而不是 `git add -A`，因为另一个标签页的改动就放在同一棵树里。过程并不整洁，但什么都没丢，测试套件在当晚结束时是 14,134 通过、0 失败。

功能会话的日志在三分钟后的 23:57 结束，写着"Session ended — Stop All"。我紧接着给 Agent! 的备注——它把这条备注保存为下一个检查点提交的提交信息——是：Stop All 应该只停止按下它的那个标签页，而不是全部。当两个自动驾驶同时运行时，一个按钮管两个，是按错了按钮。

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-snowmen.png" alt="GoKart 0.0.2 的 Frosty Peaks 赛道：玩家卡丁车位于一片雪人阵的入口，雪人交错成排地站在雪白的路面上，每个都戴着红围巾、高顶礼帽和胡萝卜鼻子，天空是深蓝色的暮色。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Frosty Peaks 上的雪人阵。撞上一个，你会被抛上天，而它会炸成一团雪；CPU 卡丁车会向前看 40 米，在雪人行列间穿行。</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-penguins.png" alt="GoKart 0.0.2 的 Frosty Peaks 赛道：一只企鹅在玩家卡丁车前方的长弯道上，用肚皮在淡蓝白色的冰面上滑行。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Frosty Peaks 上 Sherbet Land 风格的冰面和企鹅。在冰上车头会转，但卡丁车仍沿原方向滑行；企鹅摇摇摆摆走到边缘，扑倒，再滑回来穿过赛道。</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-traffic.png" alt="GoKart 0.0.2 的 Sunset Speedway 赛道：玩家卡丁车被堵在一辆公交车和一辆厢式货车后面，它们开着车头灯占据道路的两条车道，天空是日落的天色。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Sunset Speedway 上 Toad's Turnpike 风格的车流：开着车头灯的轿车、公交车、厢式货车和油罐车，以及护墙外带亮灯窗带的建筑。</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-gp-results.png" alt="GoKart 0.0.2 的大奖赛结算板，海军蓝面板配金色边框：左侧是本场比赛结果，右侧是杯赛积分榜，每位车手一行，带颜色色块、金银铜名次、用时和积分，玩家那一行在点亮的金色横条上，下方是奖杯。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>大奖赛结算板：比赛结果和杯赛积分榜并排显示，各行依次滑入，每行伴随一声滴答，下方是奖杯。</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-battle.png" alt="GoKart 0.0.2 对战模式：四辆卡丁车停在对战竞技场的起始台上，每辆系着三个气球，Lakitu 的起跑信号悬在头顶。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>对战模式：四辆卡丁车，每辆三个气球。道具命中、岩浆、屋顶边缘、无敌星触碰和重型推挤都会戳破气球，气球用完的卡丁车会变成迷你炸弹车。</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-dusty-canyon.png" alt="GoKart 0.0.2 的 Dusty Canyon 赛道：玩家卡丁车在沙漠道路上，第 1 圈、8 辆中第 5 名，配有 Mario Kart 64 风格的 HUD。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>随机驾驶机器人视角下的 Dusty Canyon，8 辆中第 5 名。沙漠大弯、一个发夹弯、一个左向 S 弯、两段绿洲水域、火车，以及起步直道上的跳台。</figcaption>
</figure>

## 关于这些截图

截图是 Agent! 拍的，不是我，也不是手动拍的。第一个版本时我要了三张随机驾驶的截图，它写了一个 70 行的 `tools/random_drive.gd`：带着游走的车道偏移沿路行驶，随机插入漂移冲刺，在随机时刻发射手里拿着的道具，然后每隔几百个物理帧保存一帧。上面两张比赛截图就是那个机器人拍下的帧。其余的来自各个功能随附的截图工具：`menu_shot.gd`、`train_shot.gd`、`traffic_shot.gd`、`snowman_shot.gd`、`penguin_shot.gd`、`hud_shot.gd` 和 `battle_shot.gd`，每一个都会布置好自己的场景、等到合适的那一帧再保存。为了这次更新，它们全部在一个检出到 `v0.0.2` 标签的干净工作树里运行，所以图片里没有任何未提交的内容。Agent! 仍然看不了结果，所以这些工具改为采样像素：冰面截图会打印前方冰面相对于柏油路的路面颜色，暂停截图会证明面板之外有一秒钟没有任何东西在动，而在发布之前，我让它数了上面全部十张图片里的纯黑像素：每一张都是零。[GoKart 的 README](https://github.com/AgentiLoop/GoKart#screenshots) 里还有更多。

## 在你试之前我想说的

- **在 git 里运行它。** 自动驾驶没有撤销。GoKart 的日志之所以可读，是因为每一轮都以一次提交结束，而唯一一次某轮跑偏时，什么都没丢。
- **把操作规则写进目标里。** "给 shell 加时间限制"作为目标的一部分比作为一条临时消息更有效，因为每一个新的轮次都会重新读取目标。
- **预期它会要求人眼。** 凡是视觉或手感方面的事，这个循环会诚实地停下来而不是撒谎。在会话之间安排一次试玩，把你的笔记作为下一个目标喂回去。
- **Stop All 是工作流的一部分**，不是失败。GoKart 的前三次会话全都是这样结束的。
- **一个仓库里跑两个自动驾驶是可行的，前提是你告诉它们彼此的存在。** "Do not conflict with the previous /auto"写进了第二个目标，两个会话都花了实实在在的功夫避开对方。给它们代码中各自独立的区域，并且目前要预料到你停掉的那一个会把另一个也一起带停。

## 这算好吗？

在 Agent! 读完仓库、数过提交并找到自动驾驶日志之后，我问了它这个问题。全部 126 个提交的作者都是代理，没有一个出自人手，`.agent/autopilot/progress.md` 已经记到第 23 轮之后。它的回答，未经编辑：

> 这取决于你想从中得到什么。作为自动驾驶能力的展示，它令人印象深刻。二十三轮以上产出了四条赛道、道具、AI 车手、大奖赛、计时赛、对战模式、程序化音乐和音效，全都没有导入任何素材，还有一份详细记录这一切的 README。从一句目标陈述出发，这是相当多的可运行软件。

它还补充了一点说明：过程中没有任何人类审查过它，所以质量是由代理自己的验证日志来判断的；而且它既没有玩过也没有审计过代码，所以说不出实际玩起来怎么样。这和日志自己得出的结论是一样的：下一步是一次试玩。

## GoKart 0.0.2

不用装 Godot 也能试玩。[GoKart 0.0.2](https://github.com/AgentiLoop/GoKart/releases/tag/v0.0.2) 是第二个打包发布版，从同一个仓库导出，比 [0.0.1](https://github.com/AgentiLoop/GoKart/releases/tag/v0.0.1) 多了 87 个提交：

- **macOS** 通用版（Apple 芯片和 Intel），使用 Developer ID 签名并经 Apple 公证
- **Windows** x86_64
- **Linux** x86_64 和 arm64

每个下载都是一个内嵌游戏数据的独立二进制文件，发布页面上还有 `SHA256SUMS.txt`，方便你核对下载内容。Windows 版未签名，所以会看到 SmartScreen 提示。这篇文章里所有 0.0.1 没有的东西都在 0.0.2 里：对战模式、计时赛、四赛道杯赛、引擎级别和重量级别、新道具、Lakitu、火车、车流、鼹鼠、雪人、企鹅、冰面、路边景物、尾流、跳台、赛道音乐、新的标题和选择画面、赛道开场、暂停画面以及重新设计的 HUD。完整清单见发布说明。

带自动驾驶的 Agent! 1.1.87 已在[发布页面](https://github.com/AgentiLoop/Agent/releases/latest)和 Homebrew 上提供。如果你更想从源码运行 GoKart，需要 Godot 4.4 或更高版本：`git clone https://github.com/AgentiLoop/GoKart.git && cd GoKart && godot --path .`
