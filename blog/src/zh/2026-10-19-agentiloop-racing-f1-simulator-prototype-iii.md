---
title: AgentiLoop Racing, Prototype III：在浏览器中运行的 F1 模拟器
description: AgentiLoop Racing 是一款在浏览器中运行的开轮赛车模拟器，由 Agent! 使用 Three.js 打造。它拥有 240 Hz 物理引擎、18 条真实赛道、AI 车手、进站、轮胎配方、燃油、ERS 和 DRS。可在 f1.gokart.games 上游玩。
tags: Showcase, JavaScript
---
<figure style="margin:2rem 0">
<img src="/agentiloop-racing-og.jpg" alt="AgentiLoop Racing：浏览器模拟器中赛道上的一辆开轮赛车。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>AgentiLoop Racing, Prototype III。发车格上的每辆赛车都是 2026 款 RB22 模型，并重新涂装了各自的配色和赞助商名称。</figcaption>
</figure>

**立即游玩：[f1.gokart.games](https://f1.gokart.games)。** 无需下载，无需安装。只需一个支持 WebGL 的浏览器，可以用键盘或 Xbox（或其他标准）手柄来玩。

AgentiLoop Racing 是一款用纯 JavaScript 和 Three.js 编写的 F1 风格赛车模拟器。第一次提交是一个确定性的四轮车辆模型，于 10 月 16 日晚上提交。三天、109 次提交之后，它已经能在 18 条真实赛道上与完整的 AI 车阵比赛，具备进站、轮胎配方、燃油、ERS 和 DRS，由物理引擎生成的引擎声，以及后视镜中能看到身后赛车的座舱视角。这一切都由 Agent! 编写，每次一个经过测试的小提交。

先给出一个诚实的说明，和 README 里写的一样：这是一个**原型，而不是经过验证的 Formula 1 模拟器**。赛车的参数是用于演示的假设值，并非实测的 F1 数据。

## 物理优先

这个项目最初是一个物理测试平台，3D 是后来才加上的。`physics.mjs` 以固定的 **240 Hz** 推进赛车。每个车轮都有自己的惯性和滑移，每条轮胎都有一条从峰值抓地到滑动的抓地特性曲线，以及侧偏角松弛、温度和磨损。簧上车身会在空气动力载荷下侧倾、俯仰和下蹲，这在 3D 赛车上也能看到。变速箱可选自动或拨片换挡，还有一个带保护的倒挡，供你车头对着墙时使用。

动力单元也做了建模。燃油作为真实质量装载，所以赛车会随着燃油消耗而变轻。混合动力系统在 100 km/h 以上最多释放 120 kW，每圈上限 4 MJ，并在制动时回收能量。

测试套件只使用 Node 内置的测试运行器：`node --test` 目前运行 158 个测试，全部通过。它们会检查诸如全油门的赛车永远不会穿墙而过，以及 3D 模型只用轮胎和底板接触地面之类的事情。

## 18 条真实赛道

<figure style="margin:2rem 0">
<img src="/agentiloop-racing-monza.jpg" alt="AgentiLoop Racing：在蒙扎与 AI 车阵比赛。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>蒙扎的一场比赛。计时框、排名和小地图在比赛中实时更新。</figcaption>
</figure>

除了一条虚构的体育场测试赛道之外，还有 18 条真实赛道，从巴林到迈阿密，包括蒙扎、银石、斯帕和摩纳哥，赛道布局由真实赛车的位置数据构建而成。其余部分则用真实数据调校：

- **DRS 区**来自 2024 年的比赛遥测数据（OpenF1）：也就是车手实际打开和关闭襟翼的位置。摩纳哥只有一个区，位于维修区直道。
- **抓地力根据真实弯道速度进行了校准。** 在 18 条赛道上，自动驾驶的圈速与真实比赛最快圈速之间的差距从 17.9% 缩小到 5.8%。在摩纳哥，自动驾驶的圈速从 84.2 秒提升到 74.4 秒，而真实圈速为 73.9 秒。
- **急弯被放宽**到最小半径 15 m，让赛车能过得了摩纳哥的圣迪沃特弯。
- **每条赛道都有维修区通道**，位于起终点直道旁，限速 80 km/h，每辆赛车都有一个维修位。

<figure style="margin:2rem 0">
<img src="/agentiloop-racing-monaco.jpg" alt="AgentiLoop Racing：摩纳哥的一场比赛。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>与 AI 车阵一起比赛的摩纳哥。</figcaption>
</figure>

## 与 AI 比赛

真实赛道默认以单人计时赛开始；按 **O**，或在 URL 后加上 `?race`，即可与车阵比赛。起步时五盏红灯每秒亮起一盏，随后经过一段随机的等待才熄灭。提前移动超过半米，就会被判 5 秒抢跑罚时。红灯亮着时，按 **1–5** 键可以进入对应发车位上的赛车。

AI 赛车会沿着赛车线行驶，在直道上相互尾流牵引，从尾流中切出，在检测点处相距一秒以内时使用 DRS，并在制动时从内线突入。在调校超车的那次提交中，18 条赛道上的 3 圈比赛，超车次数从 16 次增加到 34 次，碰撞从 8 次降为零。卡在护栏上的赛车会挂上倒挡，沿着一条已检查过车流和墙壁的路径倒出来，然后重新回到赛道。

比赛规则同样适用。每位完赛车手都必须使用两种轮胎配方，所以你必须至少进站一次，否则将被取消资格。按 **B** 可以让技师换上软胎、中性胎或硬胎。在维修区通道超速则罚 +5 秒。

每个环节都以自动驾驶开始，所以在你接管之前赛车会自己行驶。按 **P**、碰一下手柄或换挡，赛车就交给你了。

## 赛车与座舱

发车格上的每辆赛车都使用 Tyler_Dave 制作的 2026 款 RB22 模型（CC BY 4.0，来自 Sketchfab）。加载时，`rb22.mjs` 会用每辆车的配色重新涂装，并把项目的赞助商名称和车号投影到车身上。近距离时，模型的每个部件都会被细分和平滑处理，远处则使用细节较低的版本。

按 **C** 进入座舱视角。车手的视点随簧上车身移动，所以侧倾、俯仰和上下起伏都会带动视野，头部也会随 G 力轻微移动。后视镜会渲染透过每块镜面反射的场景，并排除你自己的后轮，让你看到赛道和身后的赛车。

声音同样由物理引擎合成：随转速变化的 V6 点火声、涡轮啸叫、由滑移产生的轮胎尖啸，以及随速度增大的风噪。

<figure style="margin:2rem 0">
<img src="/agentiloop-racing-spa.jpg" alt="AgentiLoop Racing：斯帕-弗朗科尔尚的计时赛。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>斯帕计时赛。</figcaption>
</figure>

## 观看视频

<figure style="margin:2rem 0">
<div style="position:relative;padding-top:56.25%;border-radius:20px;overflow:hidden">
<iframe src="https://www.youtube-nocookie.com/embed/2RluAIH3iQw?rel=0&amp;modestbranding=1&amp;color=white" title="AgentiLoop Racing — F1 simulator built with AgentiLoop.ai in Three.js" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="position:absolute;inset:0;width:100%;height:100%;border:0"></iframe>
</div>
</figure>

## 试一试

- [蒙扎的一场比赛](https://f1.gokart.games/?track=monza&race)
- [斯帕计时赛](https://f1.gokart.games/?track=spa)
- [斯帕 5 圈软胎比赛](https://f1.gokart.games/?track=spa&race&laps=5&tyre=soft)

源代码位于 [AgentiLoop/F1](https://github.com/AgentiLoop/F1)。它没有 npm 依赖，也没有打包工具：Three.js 已内置在仓库中，所以在该文件夹中运行 `python3 -m http.server` 就足以在本地运行。网站本身是一个 Cloudflare Worker，以静态文件的形式提供仓库内容。

*AgentiLoop Racing 是一个独立项目，与 Formula 1、FIA 或任何车队均无关联。3D 模型保留各自的许可证；详见仓库中的 `models/CREDITS.md`。*
