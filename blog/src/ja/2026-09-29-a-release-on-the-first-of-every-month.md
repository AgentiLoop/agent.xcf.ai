---
title: 毎月 1 日にリリース、その間はプレリリース
description: Agent! は毎月 1 日に安定版をリリースするようになりました。毎日のプレリリース(いずれ毎週に移行)で新機能や修正を試し、リリース候補で本番前に仕上げます。
tags: リリースノート, 舞台裏
---
Agent! に新しいリズムができました。**2026 年 10 月 1 日**から、**毎月 1 日**に安定版をリリースします。その間にはプレリリースがあります。今はおよそ 1 日 1 回ですが、週 1 回まで落とす予定です。毎月の終盤のどこかでプレリリースは**リリース候補(RC)**になり、いちばん良い候補が 1 日のリリースになります。

計画はこれだけです。この記事の残りでは、ここに至るまでの経緯を、私たち自身の git 履歴から作ったグラフと一緒に紹介します。

## これまでの歩み

Agent! 1.0.0 は **2026 年 3 月 13 日**にタグ付けされました。それ以来、リポジトリには **188 個のバージョンタグ**が付いています。ただし、均等に付いたわけではありません。

<figure class="chart"><div class="chart-title">月ごとのバージョンタグ数(2026 年)</div><div class="bars"><div class="lbl">3月</div><div><div class="bar" style="--w:0.738"><span>57</span></div></div><div class="lbl">4月</div><div><div class="bar" style="--w:0.880"><span>68</span></div></div><div class="lbl">5月</div><div><div class="bar dim" style="width:3.9%"><span>3</span></div></div><div class="lbl">6月</div><div><div class="bar dim" style="width:3.9%"><span>3</span></div></div><div class="lbl">7月</div><div><div class="bar dim" style="width:1.3%"><span>1</span></div></div><div class="lbl">8月</div><div><div class="bar" style="--w:0.194"><span>15</span></div></div><div class="lbl">9月</div><div><div class="bar" style="--w:0.531"><span>41</span></div></div></div><figcaption>3 月 13 日の 1.0.0 以降のタグは 188 個。忙しい春、静かな夏、そして 9 月の復活。出典: <code>git for-each-ref refs/tags</code>。</figcaption></figure>

3 月と 4 月は全力疾走でした。2 か月で 125 個のタグ、1 日に何個も付く日もありました。そして夏が来ました。5 月、6 月、7 月を合わせても 7 個です。8 月下旬にペースが戻り、9 月はここまでで 41 個です。

安定版も同じようにでこぼこの道をたどりました。Releases ページには 4 つが並んでいます。4 月 25 日の **1.0.80.170**、6 月 3 日の **1.0.88.182**、7 月 26 日の **1.0.89.183**、そして 9 月 12 日の **1.1.33.233**、スター 600 達成のリリースです。

<figure class="chart"><div class="chart-title">安定版リリースの間隔(日数)</div><div class="bars"><div class="lbl">1.0.88</div><div><div class="bar" style="--w:0.648"><span>39 日 · 4/25 → 6/3</span></div></div><div class="lbl">1.0.89</div><div><div class="bar" style="--w:0.880"><span>53 日 · 6/3 → 7/26</span></div></div><div class="lbl">1.1.33</div><div><div class="bar" style="--w:0.797"><span>48 日 · 7/26 → 9/12</span></div></div><div class="lbl">10/1</div><div><div class="bar next" style="--w:0.315"><span>19 日 · 9/12 → 10/1</span></div></div></div><figcaption>GitHub 上の各安定版を、ひとつ前のリリースからの日数で示しています。縞模様のバーは、すでに予定が決まっている 10 月 1 日のリリースです。そこから先は、毎月、間隔は 1 か月です。</figcaption></figure>

39 日、53 日、48 日という間隔は悪くありませんが、それで時計を合わせることはできませんでした。次の Agent! がいつ出るのか聞かれたら、正直な答えは「準備ができたら」でした。準備ができていることは大事です。いつなのかがわかることも大事です。

## 10 月 1 日への道

新しいサイクルはすでにリハーサルを終えています。1.1.33 のリリース後も `main` は動き続けました。9 月 13 日の v1.1.37.237 から 9 月 28 日の v1.1.77.277 まで、すべてのタグがプレリリースのビルドで、ほとんどの日に少なくとも 1 つはありました。

<figure class="chart"><div class="chart-title">1 日あたりのタグ数(9 月 13〜28 日)</div><div class="cols"><div style="height:10.6%"><span>1</span></div><div style="height:10.6%"><span>1</span></div><div style="height:10.6%"><span>1</span></div><div style="height:42.5%"><span>4</span></div><div style="height:0.0%"><span></span></div><div style="height:53.1%"><span>5</span></div><div style="height:10.6%"><span>1</span></div><div style="height:10.6%"><span>1</span></div><div style="height:31.9%"><span>3</span></div><div style="height:21.2%"><span>2</span></div><div style="height:10.6%"><span>1</span></div><div style="height:21.2%"><span>2</span></div><div style="height:85.0%"><span>8</span></div><div class="rc" style="height:42.5%"><span>4</span></div><div class="rc" style="height:42.5%"><span>4</span></div><div class="rc" style="height:10.6%"><span>1</span></div></div><div class="cols-x"><span>13</span><span>14</span><span>15</span><span>16</span><span>17</span><span>18</span><span>19</span><span>20</span><span>21</span><span>22</span><span>23</span><span>24</span><span>25</span><span>26</span><span>27</span><span>28</span></div><div class="legend"><span><i></i>プレリリースのビルド</span><span><i class="rc"></i>RC 期間(26 日の RC1 → 28 日の RC6)</span></div><figcaption>16 日間で 39 個のタグ。9 月 25 日だけで v1.1.61 から v1.1.68 まで 8 つのビルドが出ました。</figcaption></figure>

9 月 26 日、ビルドの呼び名が変わりました。**v1.1.72.272 がリリース候補 1(RC1)になり**、リリースノートに新しい見出し *Formal Release Date Oct. 1, 2026.* が加わりました。RC2 から RC5 は 9 月 27 日に続き、RC6(v1.1.77.277)は今日公開されました。各 RC のリリースノートでは、安定版 v1.1.33.233 と比べたリグレッションを報告するようテスターにお願いしています。全員が同じ基準で比べられるようにするためです。

RC は名前を変えただけではありません。実際の修正が入っています。

- **RC1** は `Package.resolved` 内のすべての `Agent*` パッケージを最新タグに固定し、AgentTools 2.53.18 などの修正が確実にビルドに入るようにしました。
- **RC6** は新しい Claude モデルでクリティックレビューが再び動くようにし、全プロバイダーでコンテキストあふれと max_tokens の検出を修正し、圧縮のしきい値が実際に使っているモデルに合わせて決まるようにしました。(最後の件は[専用のブログ記事](/blog/context-compaction-half-the-window/)があります。)

プレリリースはすべて、安定版と同じ Release ワークフローを通ります。ビルドし、公証し、`.zip` と `.dmg` にチケットをステープルします。プレリリースは試作品ではありません。走行距離が少ないだけの完成したビルドです。

## これからの 1 か月の流れ

| いつ | 何が出るか | 何のためか |
|---|---|---|
| 1 日 | 安定版 | すべての人におすすめするバージョン。Homebrew と Latest バッジはこれを指します。 |
| ほぼ毎日(いずれ毎週) | プレリリース | 新機能、実験、バグ修正。欲しい人に早めに届けます。 |
| 月の終盤 | リリース候補 | 機能は凍結。いい意味で退屈な RC になるまで、修正だけを行います。 |
| 翌月 1 日 | 安定版 | いちばん良い RC を昇格。そしてまたループが始まります。 |

<figure class="chart"><div class="chart-title">1 か月、2 つのリズム</div><div class="month"><span class="lbl">現在</span><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="rc"></b><b class="rc"></b><b class="rc"></b><b class="rc"></b><b class="rc"></b><b class="rc"></b><b class="gold"></b></div><div class="month"><span class="lbl">今後</span><b></b><b></b><b></b><b></b><b></b><b class="p"></b><b></b><b></b><b></b><b></b><b></b><b></b><b class="p"></b><b></b><b></b><b></b><b></b><b></b><b></b><b class="p"></b><b></b><b></b><b></b><b></b><b class="rc"></b><b></b><b></b><b class="rc"></b><b></b><b></b><b class="gold"></b></div><div class="legend"><span><i></i>プレリリース</span><span><i class="rc"></i>リリース候補</span><span><i style="background:#22c55e"></i>1 日の安定版</span></div><figcaption>予定表ではなくイメージ図です。1 か月は左から右へ進み、1 日で終わります。現在はほぼ毎日プレリリースがあります。今後は週 1 回になります。</figcaption></figure>

**プレリリースは実験室です。** 新しいことを試す場所です。プレリリースに入ったアイデアが実際に使われ、1〜2 日で良くなることもあります。悪いアイデアだとわかることもありますが、それは安定版よりプレリリースで知るほうがずっといいのです。バグ修正もまずここに入ります。気になることがあれば、たいてい数日以内にプレリリースで修正が届きます。

**リリース候補は 1 日前の静けさです。** 各サイクルの目標はシンプルです。リリース日までに安定した RC にたどり着き、それを出荷すること。10 月の RC は 3 日間で RC1 から RC6 まで進み、どれも機能追加ではなく修正のためのものでした。

**1 日はすべての人のためにあります。** 月に 1 回アップデートされる安定した Agent! が欲しいだけなら、安定版を使い続ければそれで十分です。

## いずれ毎週にする理由

毎日のプレリリースは勢いが出ますし、私たちにとっては最高です。でもテスターにとっては追いかけるのが大変です。月次サイクルが落ち着いたら、プレリリースは**週 1 回**に移行します。そうすれば、各ビルドが次のビルドが来るまでに数日間しっかり使われ、プレリリースごとのノートも最初から最後まで読む価値のあるものになります。

切り替えのときは、このブログとリリースノートでお知らせします。

## 追いかける方法

- **安定版:** `brew update && brew install --cask agentiloop-agent` を実行するか、[Releases ページ](https://github.com/AgentiLoop/Agent/releases)で *Latest* と表示されたビルドをダウンロードしてください。
- **プレリリースと RC:** 同じ [Releases ページ](https://github.com/AgentiLoop/Agent/releases)に *Pre-release* として並んでいます。インストールして実際の作業に使い、何が壊れたか教えてください。
- **リグレッションを見つけたら:** macOS のバージョン、プロバイダーとモデル、関連するアクティビティログの出力を添えて Issue を作成してください。API キーは含めないでください。

カレンダーに **10 月 1 日**を書き込んでください。次は 11 月 1 日、その次は 12 月 1 日です。1 日にお会いしましょう。
