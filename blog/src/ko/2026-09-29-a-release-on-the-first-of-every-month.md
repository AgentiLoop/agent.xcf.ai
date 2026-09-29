---
title: 매달 1일에 릴리스, 그 사이에는 프리릴리스
description: Agent!는 이제 매달 1일에 안정 버전을 출시합니다. 매일 나오는 프리릴리스(곧 매주로 전환)에서 새 기능과 수정 사항을 시험하고, 릴리스 후보로 출시일 전에 모든 것을 확정합니다.
tags: 릴리스 노트, 비하인드
---
Agent!에 새로운 리듬이 생겼습니다. **2026년 10월 1일**부터 **매달 1일**에 안정 버전이 나옵니다. 그 사이에는 프리릴리스가 있습니다. 지금은 대략 하루에 하나씩이고, 앞으로 일주일에 하나로 줄일 계획입니다. 매달 막바지 어딘가에서 프리릴리스는 **릴리스 후보(RC)**가 되고, 가장 좋은 후보가 1일의 릴리스가 됩니다.

계획은 이게 전부입니다. 이 글의 나머지는 우리가 여기까지 오게 된 과정을, 우리 git 기록에서 뽑은 차트와 함께 소개합니다.

## 지금까지의 여정

Agent! 1.0.0은 **2026년 3월 13일**에 태그되었습니다. 그 이후 저장소에는 **188개의 버전 태그**가 쌓였습니다. 고르게 쌓이지는 않았습니다.

<figure class="chart"><div class="chart-title">월별 버전 태그 수, 2026년</div><div class="bars"><div class="lbl">3월</div><div><div class="bar" style="--w:0.738"><span>57</span></div></div><div class="lbl">4월</div><div><div class="bar" style="--w:0.880"><span>68</span></div></div><div class="lbl">5월</div><div><div class="bar dim" style="width:3.9%"><span>3</span></div></div><div class="lbl">6월</div><div><div class="bar dim" style="width:3.9%"><span>3</span></div></div><div class="lbl">7월</div><div><div class="bar dim" style="width:1.3%"><span>1</span></div></div><div class="lbl">8월</div><div><div class="bar" style="--w:0.194"><span>15</span></div></div><div class="lbl">9월</div><div><div class="bar" style="--w:0.531"><span>41</span></div></div></div><figcaption>3월 13일 1.0.0 이후 188개의 태그. 바빴던 봄, 조용했던 여름, 그리고 9월의 귀환. 출처: <code>git for-each-ref refs/tags</code>.</figcaption></figure>

3월과 4월은 전력 질주였습니다. 두 달 동안 태그 125개, 하루에 여러 개가 붙은 날도 있었습니다. 그러고 나서 여름이 왔습니다. 5월, 6월, 7월을 다 합쳐도 태그는 7개였습니다. 8월 말에 다시 속도가 붙었고, 9월은 지금까지 41개입니다.

안정 버전도 똑같이 울퉁불퉁한 길을 걸었습니다. Releases 페이지에는 네 개가 있습니다. 4월 25일 **1.0.80.170**, 6월 3일 **1.0.88.182**, 7월 26일 **1.0.89.183**, 그리고 9월 12일 **1.1.33.233**, 스타 600개 기념 릴리스입니다.

<figure class="chart"><div class="chart-title">안정 버전 사이의 일수</div><div class="bars"><div class="lbl">1.0.88</div><div><div class="bar" style="--w:0.648"><span>39일 · 4/25 → 6/3</span></div></div><div class="lbl">1.0.89</div><div><div class="bar" style="--w:0.880"><span>53일 · 6/3 → 7/26</span></div></div><div class="lbl">1.1.33</div><div><div class="bar" style="--w:0.797"><span>48일 · 7/26 → 9/12</span></div></div><div class="lbl">10/1</div><div><div class="bar next" style="--w:0.315"><span>19일 · 9/12 → 10/1</span></div></div></div><figcaption>GitHub의 각 안정 버전을 직전 버전으로부터의 간격으로 나타냈습니다. 줄무늬 막대는 이미 일정이 잡힌 10월 1일 릴리스입니다. 그 이후로는 매달, 간격이 한 달입니다.</figcaption></figure>

39일, 53일, 48일이라는 간격은 나쁘지 않지만, 그걸로 시계를 맞출 수는 없었습니다. 다음 Agent!가 언제 나오느냐고 물으면 솔직한 답은 "준비되면"이었습니다. 준비된 것은 좋습니다. 언제인지 아는 것도 좋습니다.

## 10월 1일로 가는 길

새 주기는 이미 리허설을 마쳤습니다. 1.1.33이 나온 뒤에도 `main`은 계속 움직였습니다. 9월 13일 v1.1.37.237부터 9월 28일 v1.1.77.277까지 모든 태그가 프리릴리스 빌드였고, 대부분의 날에 적어도 하나씩은 있었습니다.

<figure class="chart"><div class="chart-title">일별 태그 수, 9월 13–28일</div><div class="cols"><div style="height:10.6%"><span>1</span></div><div style="height:10.6%"><span>1</span></div><div style="height:10.6%"><span>1</span></div><div style="height:42.5%"><span>4</span></div><div style="height:0.0%"><span></span></div><div style="height:53.1%"><span>5</span></div><div style="height:10.6%"><span>1</span></div><div style="height:10.6%"><span>1</span></div><div style="height:31.9%"><span>3</span></div><div style="height:21.2%"><span>2</span></div><div style="height:10.6%"><span>1</span></div><div style="height:21.2%"><span>2</span></div><div style="height:85.0%"><span>8</span></div><div class="rc" style="height:42.5%"><span>4</span></div><div class="rc" style="height:42.5%"><span>4</span></div><div class="rc" style="height:10.6%"><span>1</span></div></div><div class="cols-x"><span>13</span><span>14</span><span>15</span><span>16</span><span>17</span><span>18</span><span>19</span><span>20</span><span>21</span><span>22</span><span>23</span><span>24</span><span>25</span><span>26</span><span>27</span><span>28</span></div><div class="legend"><span><i></i>프리릴리스 빌드</span><span><i class="rc"></i>RC 기간(26일 RC1 → 28일 RC6)</span></div><figcaption>16일 동안 태그 39개. 9월 25일 하루에만 v1.1.61부터 v1.1.68까지 빌드 8개가 나왔습니다.</figcaption></figure>

9월 26일, 빌드의 이름이 바뀌었습니다. **v1.1.72.272가 릴리스 후보 1이 되었고**, 릴리스 노트에 새 제목이 붙었습니다: *Formal Release Date Oct. 1, 2026.* RC2부터 RC5까지는 9월 27일에 나왔고, RC6(v1.1.77.277)은 오늘 올라왔습니다. 각 RC의 릴리스 노트는 테스터들에게 안정 버전 v1.1.33.233과 비교한 회귀를 보고해 달라고 요청합니다. 모두가 같은 기준으로 비교하기 위해서입니다.

RC는 이름만 바꾼 것이 아니었습니다. 실제 수정이 들어 있었습니다.

- **RC1**은 `Package.resolved`의 모든 `Agent*` 패키지를 최신 태그로 고정해, AgentTools 2.53.18 같은 수정이 실제로 빌드에 들어가도록 했습니다.
- **RC6**은 최신 Claude 모델에서 크리틱 리뷰가 다시 작동하도록 고치고, 모든 프로바이더에서 컨텍스트 초과와 max_tokens 감지를 수정했으며, 압축 임계값이 실제로 사용하는 모델을 따르도록 했습니다. (마지막 항목은 [별도의 블로그 글](/blog/context-compaction-half-the-window/)이 있습니다.)

모든 프리릴리스는 안정 버전과 같은 Release 워크플로를 거칩니다. 빌드하고, 공증하고, `.zip`과 `.dmg`에 티켓을 스테이플합니다. 프리릴리스는 초안이 아닙니다. 주행 거리가 조금 짧을 뿐인 완성된 빌드입니다.

## 이제 한 달은 이렇게 돌아갑니다

| 언제 | 무엇이 나오나 | 무엇을 위한 것인가 |
|---|---|---|
| 1일 | 안정 버전 | 모두에게 권장하는 버전입니다. Homebrew와 Latest 배지가 이 버전을 가리킵니다. |
| 대부분의 날(곧 매주) | 프리릴리스 | 새 기능, 실험, 버그 수정을 원하는 사람에게 먼저 제공합니다. |
| 월말 막바지 | 릴리스 후보 | 기능 동결. 좋은 의미로 지루한 RC가 될 때까지 수정만 합니다. |
| 다음 달 1일 | 안정 버전 | 가장 좋은 RC를 승격합니다. 그리고 다시 반복됩니다. |

<figure class="chart"><div class="chart-title">한 달, 두 가지 리듬</div><div class="month"><span class="lbl">지금</span><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="rc"></b><b class="rc"></b><b class="rc"></b><b class="rc"></b><b class="rc"></b><b class="rc"></b><b class="gold"></b></div><div class="month"><span class="lbl">곧</span><b></b><b></b><b></b><b></b><b></b><b class="p"></b><b></b><b></b><b></b><b></b><b></b><b></b><b class="p"></b><b></b><b></b><b></b><b></b><b></b><b></b><b class="p"></b><b></b><b></b><b></b><b></b><b class="rc"></b><b></b><b></b><b class="rc"></b><b></b><b></b><b class="gold"></b></div><div class="legend"><span><i></i>프리릴리스</span><span><i class="rc"></i>릴리스 후보</span><span><i style="background:#22c55e"></i>1일의 안정 버전</span></div><figcaption>일정표가 아니라 그림입니다. 한 달은 왼쪽에서 오른쪽으로 흐르고 1일에 끝납니다. 지금은 거의 매일 프리릴리스가 있습니다. 곧 일주일에 하나가 됩니다.</figcaption></figure>

**프리릴리스는 실험실입니다.** 새로운 것을 시도하는 곳입니다. 어떤 아이디어는 프리릴리스에 들어가 실제로 쓰이면서 하루이틀 만에 더 좋아집니다. 어떤 아이디어는 나쁜 생각으로 판명되는데, 그걸 안정 버전보다 프리릴리스에서 알게 되는 편이 훨씬 낫습니다. 버그 수정도 먼저 여기에 들어갑니다. 그러니 뭔가 거슬린다면, 보통 며칠 안에 프리릴리스에서 수정이 나옵니다.

**릴리스 후보는 1일 전의 고요함입니다.** 각 주기의 목표는 간단합니다. 출시일 전에 안정적인 RC에 도달하고, 그것을 출시하는 것입니다. 10월 RC 시리즈는 사흘 만에 RC1에서 RC6까지 갔고, 모두 기능이 아니라 수정에 관한 것이었습니다.

**1일은 모두를 위한 날입니다.** 한 달에 한 번 업데이트되는 탄탄한 Agent!만 원한다면, 안정 버전을 쓰면 그걸로 끝입니다.

## 왜 나중에는 매주인가

매일 나오는 프리릴리스는 추진력 면에서, 그리고 우리에게는 아주 좋습니다. 하지만 테스터에게는 따라가기 벅찹니다. 월간 주기가 자리를 잡으면 프리릴리스는 **일주일에 한 번**으로 바뀝니다. 그러면 각 빌드가 다음 빌드가 나오기 전에 며칠 동안 실제로 쓰이고, 프리릴리스마다 노트를 처음부터 끝까지 읽을 가치가 생깁니다.

전환할 때는 이 블로그와 릴리스 노트로 알려 드리겠습니다.

## 따라오는 방법

- **안정 버전:** `brew update && brew install --cask agentiloop-agent`를 실행하거나, [Releases 페이지](https://github.com/AgentiLoop/Agent/releases)에서 *Latest*로 표시된 빌드를 받으세요.
- **프리릴리스와 RC:** 같은 [Releases 페이지](https://github.com/AgentiLoop/Agent/releases)에 *Pre-release*로 표시되어 있습니다. 하나를 설치해 실제 작업에 써 보고, 무엇이 깨졌는지 알려 주세요.
- **회귀를 발견했나요?** macOS 버전, 프로바이더와 모델, 관련 활동 로그 출력을 담아 이슈를 열어 주세요. API 키는 빼 주세요.

달력에 **10월 1일**을 적어 두세요. 그다음은 11월 1일, 그다음은 12월 1일입니다. 1일에 만나요.
