---
title: 什么是智能体循环？一个机器人、一份三明治，以及再试一次的艺术
description: 看一看，选一选，做一做，查一查。一份轻松有趣的图解智能体循环指南——简单到五岁小朋友都能懂，也有足够多的内容留给大人们。
tags: 科普, 智能体循环
---
想象一个名叫 Pip 的小机器人。

你对它说：**“请给我做一份果酱三明治。”**

Pip 看了看桌子。有面包，有果酱，还有一把勺子，上面沾着多得可疑的花生酱。

Pip 会马上宣布“三明治做好啦！”吗？

不会。那只是一段演讲，不是一份三明治。

Pip 需要**看一看，选一个小步骤，去做，再检查发生了什么**。然后，Pip 才能决定接下来做什么。

这个不断重复的模式，就叫**智能体循环**（agent loop）。

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 360" role="img" aria-labelledby="pip-title pip-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="pip-title">Pip 有了目标，但还没有三明治</title>
<desc id="pip-desc">一个友好的蓝色机器人看着两片面包和一罐果酱。对话气泡里写着：计划可不是三明治。</desc>
<rect width="760" height="360" rx="20" fill="#eef6ff"/>
<path d="M300 104l-26 24 58-24" fill="#fff"/>
<rect x="265" y="28" width="450" height="76" rx="24" fill="#fff" stroke="#b6c8e4" stroke-width="3"/>
<text x="490" y="75" text-anchor="middle" font-family="system-ui,sans-serif" font-size="27" font-weight="700" fill="#173452">计划可不是三明治。</text>
<path d="M44 282H716" stroke="#8b684c" stroke-width="13" stroke-linecap="round"/>
<path d="M103 242V276M187 242V276M217 213L260 233" fill="none" stroke="#173452" stroke-width="6" stroke-linecap="round"/>
<rect x="77" y="127" width="140" height="115" rx="27" fill="#559ef5" stroke="#173452" stroke-width="4"/>
<path d="M147 127V100" stroke="#173452" stroke-width="5"/><circle cx="147" cy="91" r="10" fill="#efb943"/>
<circle cx="117" cy="168" r="12" fill="#fff"/><circle cx="177" cy="168" r="12" fill="#fff"/>
<circle cx="120" cy="169" r="5" fill="#173452"/><circle cx="180" cy="169" r="5" fill="#173452"/>
<path d="M121 201Q147 222 173 201" fill="none" stroke="#173452" stroke-width="6" stroke-linecap="round"/>
<g transform="translate(0 12.5)"><path d="M328 260V217Q309 186 349 178Q380 168 402 187Q422 175 445 190Q472 205 449 223V260Z" fill="#fbe3ad" stroke="#ae703f" stroke-width="6"/>
<path d="M353 240V212Q389 190 428 212V240Z" fill="#d94877"/></g>
<path transform="translate(0 9.5)" d="M465 263V225Q449 195 483 187Q517 172 547 191Q578 181 590 211L582 263Z" fill="#fbe3ad" stroke="#ae703f" stroke-width="6"/>
<g transform="translate(0 1)"><rect x="622" y="191" width="60" height="82" rx="12" fill="#d94877" stroke="#173452" stroke-width="3"/>
<rect x="617" y="181" width="70" height="15" rx="5" fill="#173452"/>
<text x="652" y="239" text-anchor="middle" font-family="system-ui,sans-serif" font-size="17" font-weight="700" fill="#fff">果酱</text></g>
<text x="147" y="326" text-anchor="middle" font-family="system-ui,sans-serif" font-size="21" fill="#173452">这是 Pip。</text>
<text x="495" y="326" text-anchor="middle" font-family="system-ui,sans-serif" font-size="21" fill="#173452">目标：一份果酱三明治。</text>
</svg>
<figcaption>Pip 是我们想象出来的小帮手。绘制这幅插图的过程中，没有任何真实的机器人被弄得黏糊糊。</figcaption>
</figure>

## 整个思路，只要四个小词

**看一看。选一选。做一做。查一查。**

- **看一看：**现在正在发生什么？
- **选一选：**下一步做哪件有用的事？
- **做一做：**去做那件事。
- **查一查：**实际发生了什么？我们完成了吗？

如果任务还没完成，就带着新信息再绕一圈。

**循环**的意思就是某件事会重复发生。**智能体**是一个能够朝着目标采取行动的系统，它使用的是被赋予的工具和权限。

合在一起：**智能体循环让一个帮手能够行动、看到结果，再决定下一步做什么。**

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 520" role="img" aria-labelledby="loop-title loop-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="loop-title">看一看、选一选、做一做、查一查——并且知道何时停下</title>
<desc id="loop-desc">一张流程图，按顺时针方向从“看一看”到“选一选”，再到“做一做”和“查一查”。如果还有工作要做，“查一查”会回到“看一看”。当任务完成、受阻或预算用尽时，另一个箭头从“查一查”指向“停下或询问”。</desc>
<defs><marker id="loop-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0L10 5 0 10Z" fill="#4b617e"/></marker></defs>
<rect width="760" height="520" rx="20" fill="#f0f5fb"/>
<g fill="none" stroke="#4b617e" stroke-width="4" marker-end="url(#loop-arrow)"><path d="M298 100H460"/><path d="M586 150V238"/><path d="M464 290H302"/><path d="M176 240V153"/><path d="M176 342V414"/></g>
<g stroke-width="3"><rect x="54" y="48" width="244" height="100" rx="23" fill="#d7eaff" stroke="#3377b9"/><rect x="464" y="48" width="244" height="100" rx="23" fill="#fce9b6" stroke="#9a701b"/><rect x="464" y="242" width="244" height="100" rx="23" fill="#dfd9ff" stroke="#7760b5"/><rect x="54" y="242" width="244" height="100" rx="23" fill="#cff3e4" stroke="#29836a"/><rect x="54" y="419" width="652" height="68" rx="20" fill="#fff" stroke="#4b617e"/></g>
<g font-family="system-ui,sans-serif" text-anchor="middle" fill="#173452"><g font-size="28" font-weight="700"><text x="176" y="90">1. 看一看</text><text x="586" y="90">2. 选一选</text><text x="586" y="285">3. 做一做</text><text x="176" y="285">4. 查一查</text></g><g font-size="20"><text x="176" y="122">我看到了什么？</text><text x="586" y="122">下一步做什么？</text><text x="586" y="317">使用工具。</text><text x="176" y="317">有什么变化？</text><text x="380" y="199">还没做完？再来一圈。</text><text x="428" y="389">完成了、卡住了，还是到上限了？</text><text x="380" y="461" font-size="24" font-weight="700">停下来——或者去问人。</text></g></g>
</svg>
<figcaption>这是一张教学示意图，并不是必须遵循的软件设计。真实的实现可以把这些阶段合并在一起。重要的是把结果反馈到下一次决策中。</figcaption>
</figure>

## 回到那项非常严肃的三明治任务

Pip 的第一个小步骤是打开果酱罐。

**做一做：**拧盖子。

**查一查：**盖子纹丝不动。

有意思的地方来了。Pip 不应该仅仅因为“打开罐子”是计划的一部分，就假装罐子已经开了。

Pip 也不应该一直拧下去，拧到太阳都变成葡萄干。

Pip 可以尝试一个被允许的替代办法，或者说：“你能帮我拧一下这个盖子吗？”寻求帮助是一个有用的结果——而不是机器人级别的大失败。

罐子打开之后，Pip 就可以抹果酱、把面包合上，再对照你的要求检查成果。

两片面包？中间有果酱？放在盘子里？太好了。

一个罐子立在一整条面包上？很有创意。但不是三明治。

## AI 在哪里发挥作用？

我们的厨房故事是虚构的。软件智能体的工具不是用来拿面包的，而是可能用来读取文件、搜索网页、编辑文档或运行测试。

在 AI 智能体中，语言模型可以帮忙选择下一步。外围的软件负责执行被允许的工具调用，并把结果返回。然后模型带着这些信息再进行一轮。

可以把它想成三种不同的分工：

| 部分 | Pip 的假想厨房 | 软件版本 |
| --- | --- | --- |
| 目标 | 做一份果酱三明治 | 修复一个失效的链接 |
| 决策者 | 选择下一个小步骤 | 模型提出一个操作 |
| 工具 | 双手和勺子 | 文件读取器、编辑器或浏览器 |
| 观察 | 盖子还是没打开 | 工具返回错误或结果 |
| 工作笔记 | 罐子已开；面包已备好 | 相关的任务历史和结果 |
| 完成检查 | 你要的三明治做好了 | 确认目标链接能正常使用 |

**模型建议一个操作，并不等于这个操作真的发生了。**而一个操作真的发生了，也不自动等于目标已经达成。

“文件已保存”和“用正确的内容保存了正确的文件”是两种不同的说法。检查这一步，正是这种差别发挥作用的地方。

## 一次小小的冒险：消失的图片

假设你让一个软件帮手修复网页上一张不显示的图片。

一个有用的循环可能是这样的：

1. **看一看：**读取页面，找出图片路径。
2. **选一选：**检查被引用的图片是否存在。
3. **做一做：**查看相关文件。
4. **查一查：**页面请求的是 `cat.png`，但文件名其实是 `cat.jpg`。
5. **再来一圈：**更新引用，然后确认页面加载的是预期的那张图片。
6. **停下：**报告所做的修改，以及实际执行过的检查。

如果图片还是没有出现，那么“我改了页面”是不够的。结果应该指引下一步。

注意是什么让它成为一个循环：**下一个操作取决于上一个操作揭示了什么。**它并不只是一遍又一遍地做同一件事。

## 每绕一圈都会更好吗？

不会。动作更多，并不自动意味着进展更多。

下面是一张为 Pip 的三明治任务编造的图表。每完成一个里程碑，我们就给 Pip 记一分：打开罐子、抹好果酱、组装三明治，以及最终核对要求。

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 450" role="img" aria-labelledby="graph-title graph-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="graph-title">一张想象中的三明治进度图</title>
<desc id="graph-desc">在六次尝试中，已完成的里程碑分别是零、零、一、二、三和四。前两次尝试毫无进展，因为罐子打不开。这些编造的数字用来说明反馈的作用，并不是实测的智能体表现。</desc>
<rect width="760" height="450" rx="20" fill="#f0f5fb"/>
<g font-family="system-ui,sans-serif" fill="#173452"><text x="48" y="42" font-size="23" font-weight="700">有进展不等于忙个不停。</text><text x="48" y="73" font-size="18">已完成的里程碑 · 虚构示例，并非基准测试</text></g>
<g stroke="#c2cedd" stroke-width="1"><path d="M95 335H690M95 280H690M95 225H690M95 170H690M95 115H690"/></g>
<path d="M95 105V345H700" fill="none" stroke="#4b617e" stroke-width="3"/>
<polyline points="115,335 225,335 335,280 445,225 555,170 665,115" fill="none" stroke="#227657" stroke-width="5" stroke-linejoin="round"/>
<g fill="#227657" stroke="#fff" stroke-width="3"><circle cx="115" cy="335" r="8"/><circle cx="225" cy="335" r="8"/><circle cx="335" cy="280" r="8"/><circle cx="445" cy="225" r="8"/><circle cx="555" cy="170" r="8"/><circle cx="665" cy="115" r="8"/></g>
<g font-family="system-ui,sans-serif" font-size="20" fill="#173452" text-anchor="middle"><text x="68" y="341">0</text><text x="68" y="286">1</text><text x="68" y="231">2</text><text x="68" y="176">3</text><text x="68" y="121">4</text><text x="115" y="375">1</text><text x="225" y="375">2</text><text x="335" y="375">3</text><text x="445" y="375">4</text><text x="555" y="375">5</text><text x="665" y="375">6</text><text x="390" y="418">尝试次数</text></g>
<g font-family="system-ui,sans-serif" font-size="19" fill="#173452"><text x="116" y="292">盖子卡住了！</text><text x="326" y="317">求助成功。</text><text x="586" y="99">检查完毕！</text></g>
</svg>
<figcaption>虚构数据：已完成的里程碑依次为 0、0、1、2、3、4。真实的工作可能会停滞、倒退，或者在现有工具下根本无法完成。</figcaption>
</figure>

那段平线很重要。如果什么都没有改变，帮手需要察觉到这一点——而不是庆祝自己已经试了多少次。

对大人们来说，这引出了几个有用的问题：我们学到什么了吗？状态改变了吗？我们是在重复同一个失败的操作吗？再试一次值得付出这个代价吗？

对其他所有人来说：**如果门上写着“拉”，更用力地推可不是什么策略。**

## 给帮手一道围栏，而不是整个星球

一个合理的智能体设计，需要的不只是一个“重复”按钮。

- **清晰的终点线。**“找三张企鹅的图片”比“让一切都变得超棒”更容易检查。
- **恰当的权限。**能起草一封邮件，不应该自动意味着能把它发出去。
- **停止的预算。**给尝试次数、时间或花费设定上限。卡住的任务绝不能变成无休止的任务。
- **提问的途径。**缺少信息、缺少权限，或者面临重大选择时，可能需要一个人来介入。
- **诚实的检查。**使用与目标相匹配的证据。不要把“工具返回了”变成“一切都正确”。

这些是设计原则，并不是承诺每个产品都实现了它们。循环并不会神奇地让一个系统变得安全或可靠。

在 Pip 的厨房里就是：把三明治做好，不要订一整卡车的果酱，使用大人的电器之前要先问一声。

## 智能体循环和脚本是一回事吗？

不一定——但两者的界线并不是“脚本很傻，智能体很聪明”。脚本同样可以有循环、条件判断和出色的检查。

真正值得关注的区别在于**下一个操作是如何被选出来的**。在固定的工作流中，开发者事先铺好了所有路线。在由模型驱动的智能体循环中，模型可以根据任务和最新的观察，在可用的操作之间做出选择。真实的系统可以把两种方式混合使用。

对于可预测的工作，一个小脚本可能恰到好处。中午敲一下钟，用不着一个会思考哲学的机器人。

对于充满未知障碍的任务，根据新鲜证据来选择下一步可能会很有用。也正是这种灵活性，让限制和验证变得重要。

## 冰箱贴版本

智能体循环就是：

> 尝试一个有用的步骤。看看发生了什么。运用你学到的东西。只在合理的时候才重复。

它不是魔法。它不是保证。它也不是“永远做下去”。

它是一种把**目标、行动和真实结果**连接起来的方式——一遍又一遍，直到帮手完成任务，或者需要停下来。

Pip 会说得更简单：

**“看一看。试一试。查一查。还没有三明治的时候，别说三明治做好了。”**
