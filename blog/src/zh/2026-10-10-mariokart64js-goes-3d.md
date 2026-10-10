---
title: MarioKart64JS 进入 3D：Wii 卡丁车、3D 标题画面和冲线后的环绕飞行镜头
description: Mario Kart 64 用平面精灵绘制赛车手。在 MarioKart64JS 中按下 3，每辆卡丁车都会变成 3D 模型，Lakitu 也不例外，还带有真实阴影、重建的 3D 标题画面，以及冲线后绕着你的卡丁车飞行的镜头。下面通过截图讲讲 3D 模式是如何搭建起来的。
tags: Showcase, JavaScript
---
<figure style="margin:2rem 0">
<img src="/mk64js-3d-title.jpg" alt="MarioKart64JS 的 3D 标题画面：Wario、Bowser、Mario、Peach 和 Toad 驾驶 3D 卡丁车，在 Mario Kart 64 标志下朝镜头驶来。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>3D 标题画面。原版是一张平面画作。这里的天空、山丘和道路都用 Three.js 构建，五位车手是朝镜头驶来的 3D 卡丁车。</figcaption>
</figure>

[上一篇 MarioKart64JS 文章](/blog/mariokart64js-from-scratch-in-javascript/)讲的是尽可能贴近 Mario Kart 64：赛道几何、精灵和音乐取自卡带，再由全新的 JavaScript 完成原版 C 代码所做的事。这一篇讲的是相反的方向。只需一个按键 **3**，就能开启 N64 从未有过的 3D 模式。

## 精灵变成模型

Mario Kart 64 的赛车手并不是模型。每位车手由 321 帧预渲染的 64×64 图像组成，游戏会挑选与镜头角度相符的那一帧。MarioKart64JS 绘制的也是这些帧，而且默认仍然如此。

3D 模式会把这些精灵换成 Mario Kart Wii 标准卡丁车（Standard Kart）的模型，这些模型来自 Collada 导出文件，由 `tools/build-wii-karts.py` 放入项目中。它始于 10 月 9 日晚上的一个简单测试：21:22，按下 3 键会在玩家下方放上一辆载着 Mario 的红色标准卡丁车。到 22:02，全部八位车手都有了自己的卡丁车，按 Wii 的重量级别划分：Toad 用小型卡丁车，Mario、Luigi、Peach 和 Yoshi 用中型，D.K.、Wario 和 Bowser 用大型，每辆都有自己的涂装。

这期间的大部分工作，都是模型加载器容易弄错的小细节：

- **眼睛。** 每张眼睛纹理只有一只眼睛。在 Wii 上，纹理矩阵会把它重复一次，采样器再把它镜像成一对。Three.js 的 ColladaLoader 把这两者都丢掉了，于是一只眼睛被拉伸到整张脸上。`kart3d.js` 按角色逐一把重复和镜像补了回来。
- **轮胎。** 后轮是放大后的前轮网格。它们的尺寸和车轴位置是从每辆卡丁车组装好的菜单模型中测量得出的，这让后轮变大了 1.29 倍，并放到了 Wii 中的位置上。
- **座位。** 每位车手都有一个座位位置，让他们坐进后倾的座椅里，而不是悬浮在座椅上方。

Agent! 看不了图片，所以它改用数字来检查模型：每辆卡丁车的 ASCII 侧视图、后视图和俯视图，12 个角度的转台图集，以及每位车手双手与方向盘之间的测量间距。

## 3D 赛车

<figure style="margin:2rem 0">
<img src="/mk64js-3d-race-mario.jpg" alt="MarioKart64JS 的 3D 模式，在 Mario Raceway 上用 3D 卡丁车比赛。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>3D 模式下的 Mario Raceway。比赛中的每辆卡丁车都是 3D 模型，各自是对应角色的标准卡丁车。</figcaption>
</figure>

在比赛中，按 3 会替换赛道上的每一辆卡丁车，而不只是你的那辆，再按一次就会换回精灵。随之还有另外两处变化。

**阴影。** 精灵下方是一块扁平的团状阴影。3D 卡丁车则会在赛道上投下真正的阴影贴图阴影。这需要一个技巧：赛道使用的是无光照材质，无法接收阴影，所以赛道会得到其表面的透明"阴影接收"副本，只在有阴影落下的地方显示出来。

**Lakitu。** 裁判变成了 Mario Kart Wii 中的 Lakitu（`src/lakitu3d.js`）。他的手臂通过模型自身的骨骼摆出姿势：一只手握着钓竿，另一只手挥舞旗子。起跑灯、圈数牌和逆行标志都挂在钓竿的钩子上，而原版精灵的动画帧依旧控制着时机，所以红、红、蓝的倒计时仍会在一贯的时刻亮起。

<figure style="margin:2rem 0">
<img src="/mk64js-3d-race-koopa.jpg" alt="MarioKart64JS 的 3D 模式，在 Koopa Troopa Beach 上比赛。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Koopa Troopa Beach，10 月 10 日的大部分时间都花在了这里：3D 卡丁车的车身必须学会冲上的，正是这里的跳台。</figcaption>
</figure>

3D 卡丁车还拥有一个精灵所没有的车身。碰到墙壁时，它是一个胶囊体，每根车轴上方各一个圆，并作为刚体移动和转向。这带来了副作用。在 Koopa Troopa Beach，车头的圆会比卡丁车中心更早碰到坡道的边缘，而边缘的背面会把卡丁车从跳台上弹开。修复方法是让每根车轴分别与其下方的地面进行检测。后来的一个提交让墙壁在正面碰撞时不再改变玩家卡丁车的朝向，因为在 Mario Kart 64 中，墙壁会反弹卡丁车的运动，但从不改变它的朝向。

<figure style="margin:2rem 0">
<img src="/mk64js-3d-race-royal.jpg" alt="MarioKart64JS 的 3D 模式，在 Royal Raceway 上比赛。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>3D 模式下的 Royal Raceway。</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-3d-race-bowser.jpg" alt="MarioKart64JS 的 3D 模式，在 Bowser's Castle 中比赛。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Bowser's Castle，这里宽度为 5 的通道，正是必须防止胶囊体横卡在走廊里的地方。</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-3d-race-rainbow.jpg" alt="MarioKart64JS 的 3D 模式，在 Rainbow Road 上比赛。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>使用 3D 卡丁车的 Rainbow Road。</figcaption>
</figure>

## 3D 标题画面

Mario Kart 64 的标题背景是一张 320×240 的平面图片。天空、山丘、道路和五位车手全都是画上去的。在标题画面按下 3 会把它重建出来（`src/title3d.js`）：天空、山丘和道路用 Three.js 制作，车手则是与比赛中相同的 3D 卡丁车。

布局沿用了原画。Wario 在左前方，Bowser 在他身后；Mario 在右前方，Peach 在他身后；Toad 正从右侧弯道驶出。每辆卡丁车的摆放位置都让它在屏幕上的边框与原画中对应车手的边框相差约 10 像素以内。镜头低低地架在它们前方的路面上，使用 64° 的广角镜头，道路在下方滚动，所以卡丁车看起来就像是径直朝你驶来。方格旗、标志、PUSH START 和版权信息仍然是原版标题中的 2D 叠加层。

它后面的菜单也换上了相配的背景。在标题画面开启 3D 还会切换到 4× 纹理档位，之后的比赛都会以 3D 开始，直到你再次按下 3。

<figure style="margin:2rem 0">
<img src="/mk64js-3d-game-select.jpg" alt="MarioKart64JS 的游戏选择画面，带有 3D 模式背景。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>带有 3D 模式背景的游戏选择画面。</figcaption>
</figure>

## 冲线后的环绕飞行镜头

当你冲过终点线时，Mario Kart 64 会把镜头交给一段简短的过场动画。MarioKart64JS 在这里遵循了游戏的镜头代码（反编译代码中的 `PLAYER_CINEMATIC_MODE` 和各个过场镜头函数）：镜头转到卡丁车前方，看着它冲过终点线，然后在 CPU 车手接管你的卡丁车时于不同镜头之间切换。这个序列依次重复：车头环绕、路边、高空摇臂、路边、低位车尾镜头、路边。源码注释中有一点需要注意：镜头时长和距离是凭肉眼调校的，并非取自 ROM 中的数据表。

跟拍镜头跟随的是卡丁车朝向经过大幅平滑处理后的副本。如果没有这一步，AI 细小的转向修正会让镜头绕着卡丁车晃动，看起来就像它在一顿一顿地转弯。使用 3D 卡丁车时，这些镜头最能展现模型，因为镜头终于能从正面和侧面看到卡丁车了。

<figure style="margin:2rem 0">
<img src="/mk64js-3d-flyover-front.jpg" alt="Mario Raceway 上的冲线环绕飞行镜头：镜头位于 Mario 的 3D 卡丁车前方，回头看着它。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Mario Raceway 上的车头镜头：镜头从卡丁车后方绕到前方，并在它前面随行。</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-3d-flyover-crane.jpg" alt="Mario Raceway 上的冲线环绕飞行镜头：从卡丁车后方高处俯瞰道路的高空摇臂镜头。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>高空摇臂镜头，位于卡丁车的后上方，俯瞰道路。</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-3d-flyover-roadside.jpg" alt="Royal Raceway 上的冲线环绕飞行镜头：卡丁车驶过时，镜头架在路边。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Royal Raceway 上的路边镜头。镜头立在前方的路边，一直停留到卡丁车驶过为止。</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-3d-flyover-low.jpg" alt="Koopa Troopa Beach 上的冲线环绕飞行镜头：位于卡丁车肩侧的低位镜头。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Koopa Troopa Beach 上的低位车尾镜头，位于卡丁车的一侧肩后。</figcaption>
</figure>

## 截图是如何拍摄的

本文中的每张图片都是在无头 Chrome 中以 1280×960 拍摄的。标题和游戏选择画面的截图是在标题画面按下 3 拍到的，和玩家的操作一样。比赛在保存为开启 3D 模式的状态下以自动驾驶运行，而环绕飞行镜头的截取方式是把玩家放到最后一圈的最后一段，并在冲线后每 0.7 秒截取一帧。Agent! 通过测量来挑选画面：镜头相对卡丁车的位置告诉它每一帧属于哪种镜头，像素统计则筛掉了过暗或细节不足的画面。和上一篇文章一样，它自己并没有看这些图片。

## 试一试

克隆 [AgentiLoop/MarioKart64JS](https://github.com/AgentiLoop/MarioKart64JS)，运行 `npm install && npm run dev`，打开 `http://localhost:5173`，然后在标题画面或比赛中按下 **3**。网页版同样包含 3D 卡丁车、Lakitu 和 3D 标题画面。放入项目的模型位于 `public/wii/`；`tools/build-wii-karts.py` 和 `tools/build-wii-lakitu.py` 是从 Collada 文件中把它们放入项目的脚本。

*MarioKart64JS 是一个粉丝研究项目，用于测试 AI 在复制一款游戏上能走多远。Mario Kart 64 和 Mario Kart Wii 均为 © Nintendo，其资源归 Nintendo 所有。本项目与 Nintendo 无关，也未获得 Nintendo 的认可。*
