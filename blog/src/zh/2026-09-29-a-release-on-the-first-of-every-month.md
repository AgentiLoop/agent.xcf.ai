---
title: 每月 1 日发布，中间穿插预发布
description: Agent! 现在于每月 1 日发布稳定版。每日预发布(之后改为每周)用来试验新功能和修复，候选版本则在发布日之前把一切定下来。
tags: 发布说明, 幕后
---
Agent! 有了新的节奏。从 **2026 年 10 月 1 日**起，**每月 1 日**发布一个稳定版。两次发布之间会有预发布版本：目前大约每天一个，我们计划放慢到每周一个。在每个月的最后阶段，预发布会变成**候选版本(RC)**，其中最好的一个会成为 1 日的正式发布。

这就是全部计划。本文剩下的部分讲讲我们是怎么走到这一步的，并附上几张来自我们自己 git 历史的图表。

## 我们走过的路

Agent! 1.0.0 于 **2026 年 3 月 13 日**打上标签。从那以后，仓库累计了 **188 个版本标签**。它们来得并不均匀。

<figure class="chart"><div class="chart-title">2026 年每月版本标签数</div><div class="bars"><div class="lbl">3月</div><div><div class="bar" style="--w:0.738"><span>57</span></div></div><div class="lbl">4月</div><div><div class="bar" style="--w:0.880"><span>68</span></div></div><div class="lbl">5月</div><div><div class="bar dim" style="width:3.9%"><span>3</span></div></div><div class="lbl">6月</div><div><div class="bar dim" style="width:3.9%"><span>3</span></div></div><div class="lbl">7月</div><div><div class="bar dim" style="width:1.3%"><span>1</span></div></div><div class="lbl">8月</div><div><div class="bar" style="--w:0.194"><span>15</span></div></div><div class="lbl">9月</div><div><div class="bar" style="--w:0.531"><span>41</span></div></div></div><figcaption>自 3 月 13 日的 1.0.0 以来共 188 个标签。忙碌的春天，安静的夏天，以及九月的回归。来源：<code>git for-each-ref refs/tags</code>。</figcaption></figure>

三月和四月是一场冲刺：两个月 125 个标签，有时一天好几个。然后夏天来了。五月、六月和七月加起来只有七个标签。八月下旬节奏重新加快，九月到目前为止已有 41 个。

稳定版也走过同样坎坷的路。Releases 页面列出了四个：4 月 25 日的 **1.0.80.170**、6 月 3 日的 **1.0.88.182**、7 月 26 日的 **1.0.89.183**，以及 9 月 12 日的 **1.1.33.233**，也就是 600 星纪念版。

<figure class="chart"><div class="chart-title">稳定版之间的天数</div><div class="bars"><div class="lbl">1.0.88</div><div><div class="bar" style="--w:0.648"><span>39 天 · 4/25 → 6/3</span></div></div><div class="lbl">1.0.89</div><div><div class="bar" style="--w:0.880"><span>53 天 · 6/3 → 7/26</span></div></div><div class="lbl">1.1.33</div><div><div class="bar" style="--w:0.797"><span>48 天 · 7/26 → 9/12</span></div></div><div class="lbl">10/1</div><div><div class="bar next" style="--w:0.315"><span>19 天 · 9/12 → 10/1</span></div></div></div><figcaption>GitHub 上的每个稳定版，从上一个版本算起。条纹柱是已经排上日程的 10 月 1 日发布。从那以后，间隔就是一个月，每个月都是。</figcaption></figure>

39、53 和 48 天的间隔不算差，但没法拿来对表。如果你想知道下一个 Agent! 什么时候来，老实的回答是"准备好的时候"。我们喜欢准备好。我们也喜欢知道是什么时候。

## 通往 10 月 1 日之路

新周期已经完成了彩排。1.1.33 发布之后，`main` 一直在推进。从 9 月 13 日的 v1.1.37.237 到 9 月 28 日的 v1.1.77.277，每个标签都是预发布构建，而且大多数日子里至少有一个。

<figure class="chart"><div class="chart-title">每日标签数，9 月 13–28 日</div><div class="cols"><div style="height:10.6%"><span>1</span></div><div style="height:10.6%"><span>1</span></div><div style="height:10.6%"><span>1</span></div><div style="height:42.5%"><span>4</span></div><div style="height:0.0%"><span></span></div><div style="height:53.1%"><span>5</span></div><div style="height:10.6%"><span>1</span></div><div style="height:10.6%"><span>1</span></div><div style="height:31.9%"><span>3</span></div><div style="height:21.2%"><span>2</span></div><div style="height:10.6%"><span>1</span></div><div style="height:21.2%"><span>2</span></div><div style="height:85.0%"><span>8</span></div><div class="rc" style="height:42.5%"><span>4</span></div><div class="rc" style="height:42.5%"><span>4</span></div><div class="rc" style="height:10.6%"><span>1</span></div></div><div class="cols-x"><span>13</span><span>14</span><span>15</span><span>16</span><span>17</span><span>18</span><span>19</span><span>20</span><span>21</span><span>22</span><span>23</span><span>24</span><span>25</span><span>26</span><span>27</span><span>28</span></div><div class="legend"><span><i></i>预发布构建</span><span><i class="rc"></i>RC 阶段(26 日 RC1 → 28 日 RC6)</span></div><figcaption>16 天 39 个标签。仅 9 月 25 日一天就发布了八个构建，从 v1.1.61 到 v1.1.68。</figcaption></figure>

9 月 26 日，构建换了名字。**v1.1.72.272 成为候选版本 1(RC1)**，发布说明里多了一个新标题：*Formal Release Date Oct. 1, 2026.* RC2 到 RC5 在 9 月 27 日相继发布，RC6(v1.1.77.277)于 9 月 28 日上线。每个 RC 的发布说明都请测试者以稳定版 v1.1.33.233 为基准报告回归问题，这样大家都在同一个基准上比较。

RC 不只是改了个名字。它们带来了实实在在的修复：

- **RC1** 把 `Package.resolved` 中每个 `Agent*` 包都固定到最新标签，确保像 AgentTools 2.53.18 这样的修复真正进入构建。
- **RC6** 让评审(critic)功能在较新的 Claude 模型上重新工作，修复了所有提供商的上下文溢出和 max_tokens 检测，并让压缩阈值跟随你实际使用的模型。(最后这一点有[单独的博客文章](/blog/context-compaction-half-the-window/)。)

每个预发布都和稳定版走同样的 Release 工作流：构建、公证，并把票据装订(staple)到 `.zip` 和 `.dmg` 上。预发布不是半成品。它是一个完整的构建，只是里程少一些。

## 现在一个月是这样的

| 时间 | 发布什么 | 用途 |
|---|---|---|
| 1 日 | 稳定版 | 我们推荐给所有人的版本。Homebrew 和 Latest 徽章都指向这里。 |
| 大多数日子(之后每周) | 预发布 | 新功能、实验和错误修复，提前提供给想要的人。 |
| 月底最后阶段 | 候选版本 | 功能冻结。只做修复，直到某个 RC 变得"无聊"(褒义)。 |
| 下一个 1 日 | 稳定版 | 最好的 RC 转正。然后循环重新开始。 |

<figure class="chart"><div class="chart-title">一个月，两种节奏</div><div class="month"><span class="lbl">现在</span><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="rc"></b><b class="rc"></b><b class="rc"></b><b class="rc"></b><b class="rc"></b><b class="rc"></b><b class="gold"></b></div><div class="month"><span class="lbl">之后</span><b></b><b></b><b></b><b></b><b></b><b class="p"></b><b></b><b></b><b></b><b></b><b></b><b></b><b class="p"></b><b></b><b></b><b></b><b></b><b></b><b></b><b class="p"></b><b></b><b></b><b></b><b></b><b class="rc"></b><b></b><b></b><b class="rc"></b><b></b><b></b><b class="gold"></b></div><div class="legend"><span><i></i>预发布</span><span><i class="rc"></i>候选版本</span><span><i style="background:#22c55e"></i>1 日的稳定版</span></div><figcaption>这是示意图，不是日程表：一个月从左到右推进，在 1 日结束。现在几乎每天都有预发布。之后改为每周一个。</figcaption></figure>

**预发布是实验室。** 我们在这里尝试新东西。有些想法进入预发布，在真实使用中一两天内就变得更好。有些想法被证明是坏主意，而从预发布中发现这一点，要比从稳定版中发现好得多。错误修复也会先出现在这里，所以如果有什么让你困扰，修复通常几天内就会出现在预发布中。

**候选版本是 1 日前的平静。** 每个周期的目标很简单：在发布日之前得到一个稳定的 RC，然后发布它。十月的 RC 系列三天内从 RC1 走到 RC6，每一个都是关于修复，而不是新功能。

**1 日属于所有人。** 如果你只想要一个每月更新一次的可靠 Agent!，留在稳定版就行了。

## 为什么之后改为每周

每天一个预发布对保持势头很好，对我们也很好。但对测试者来说，要跟上可不容易。等月度周期稳定下来，预发布会改为**每周一次**。这样每个构建在下一个到来之前都能经过几天的真实使用，每个预发布的说明也值得从头读到尾。

切换时我们会在这里和发布说明中公告。

## 如何跟进

- **稳定版：** 运行 `brew update && brew install --cask agentiloop-agent`，或者在 [Releases 页面](https://github.com/AgentiLoop/Agent/releases)下载标记为 *Latest* 的构建。
- **预发布和 RC：** 它们在同一个 [Releases 页面](https://github.com/AgentiLoop/Agent/releases)上，标记为 *Pre-release*。安装一个，用它做真实的工作，然后告诉我们哪里坏了。
- **发现回归问题？** 提交一个 issue，附上你的 macOS 版本、提供商和模型，以及相关的活动日志输出。请不要附上你的 API 密钥。

在日历上记下 **10 月 1 日**，然后是 11 月 1 日，然后是 12 月 1 日。1 日见。
