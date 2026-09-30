---
title: Agent! はこうして始まった：3月の3日間
description: 3年分の部品、足りなかったループがひとつ、そして2日足らずで177コミット。git から読み解いた Agent! 本当の誕生物語。
tags: 起源, 歴史
---
<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 380" role="img" aria-labelledby="lego-title lego-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="lego-title">おもちゃのブロックで Mac を組み立てる、やさしいロボット</title>
<desc id="lego-desc">にこにこした青いロボットが、赤・黄・緑・青・オレンジのおもちゃのブロックで半分まで組み立てた Mac の画面の上に、黄色いブロックを持っています。吹き出しには「もうすぐ完成！」と書かれています。</desc>
<rect width="760" height="380" rx="20" fill="#eef6ff"/>
<path d="M40 318H720" stroke="#8b684c" stroke-width="13" stroke-linecap="round"/>
<path d="M190 92l-6 26 40-26" fill="#fff"/>
<rect x="120" y="30" width="230" height="64" rx="22" fill="#fff" stroke="#b6c8e4" stroke-width="3"/>
<text x="235" y="72" text-anchor="middle" font-family="system-ui,sans-serif" font-size="26" font-weight="700" fill="#173452">もうすぐ完成！</text>
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
<text x="190" y="354" text-anchor="middle" font-family="system-ui,sans-serif" font-size="21" fill="#173452">組み立て係。</text>
<text x="540" y="354" text-anchor="middle" font-family="system-ui,sans-serif" font-size="21" fill="#173452">Mac。あとブロック1個。</text>
</svg>
<figcaption>大きなものはみんな、小さなブロックの山から始まります。コツは、次にどのブロックを置くかを知ることです。</figcaption>
</figure>

どんなアプリにも最初の日があります。Agent! の最初の日は水曜日でした。**2026年3月11日、午後3時7分** です。分まで分かるのは、git が書き残してくれたからです。

でも、ブロックはそのずっと前から、あちこちに転がっていました。

## 3年分の部品

Agent! の前にも、いくつものアプリがありました。**ANIE**、**Game Changer**、**BattleScript**、**XCF MCP サーバーとクライアント**、そしてファイルのたくさんの行を一度に書き換えるツール **D1F**。さらに Swift パッケージが8つほど。すべて同じ一人の人が書いたものです。

どれも仕事のひとかけらはこなせました。AI と話せるもの、コードを編集できるもの、Xcode をいじれるもの。でも、いちばん大事なこと、つまり **自分で続けていくこと** は、どれにもできませんでした。

ぜんまいのおもちゃを思い浮かべてください。ぜんまいを巻くと、三歩歩いて止まります。かわいい。でも役には立たない。足りなかったのはループでした。問題を見て、道具を選んで、使って、何が起きたか確かめて、仕事が終わるまでまた繰り返す。（このループには[ロボットとサンドイッチが出てくる専用の記事](/blog/what-is-an-agent-loop/)があります。）

ループが動いた瞬間、古い部品のいいところが、その上にカチッとはまるようになりました。これが誕生の物語を一文で言ったものです。残りは細かい話で、細かい話こそ面白いのです。

## 1日目：頭脳ひとつ、ヘルパーひとつ、そしてキャンセルボタン

最初の本格的なコミットの名前は *「Autonomous Agent with privileged launch daemon.」* です。ファイル20個、Swift で 1,765 行。箱の中身はこうでした。

- やりたいことを打ち込む SwiftUI のウィンドウ。
- 考える役の AI 頭脳、Claude。
- **Launch Daemon**：家じゅうの鍵を持ってバックグラウンドで働く小さなヘルパー。これでエージェントが大人向けのシステム作業をこなせます。
- タスク履歴、スクリーンショット、ペースト。

1時間後、最初のクラッシュ修正が入りました（スクリーンショットを貼り付けると落ちていたのです）。その数分後には、Esc キーに割り当てられた大きな赤い **キャンセル** ボタン。自分で動くものを作ると、停止ボタンは早めにやってきます。

午後5時27分には、2人目のヘルパー **Launch Agent** が登場しました。万能の root ではなく *あなた* としてコマンドを実行するヘルパーです。フォルダの中身を見るためだけにマスターキーを求めるのは、ろうそく1本に火をつけるために消防車を呼ぶようなものです。その6分後、Agent! は2つ目の頭脳を手に入れました。**Ollama** です。これで、あなたの Mac の中に住む AI モデルでも動けるようになりました。

その日が終わる前に、Swift スクリプトを書いて実行すること、Xcode を操作すること、ビジョンモデルで画像を見ること、スプラッシュ画面を出すこともできるようになりました。信号機みたいな小さなステータスドットもつきましたが、緑・黄・赤に落ち着くまでにコミットが十数個かかりました。エージェントループより難しいこともあるのです。

## 2日目：「いいですか？」

3月12日は、Agent! が「Mac は礼儀正しく、しかもそこにとても厳しい」と学んだ日です。

ミュージックや Pages のような別のアプリを操作するとき、macOS はまずこう聞きます。*「Agent! が"ミュージック"を制御しようとしています。許可しますか？」* この小さなウィンドウを実際に出すまでに、夜がまるごとかかりました。だいたい午後8時20分から9時40分までの履歴は、数分おきの試行の山です。この方法で試す、メインスレッドで試す、システム設定を開く、`osascript` を試す、`every window` を頼んでみる、`name` だけで試す。しかも Keynote、Numbers、Pages はバンドル ID が変わっていて、間違った名前でドアをノックしていました。

最後にはうまくいきました。同じ夜、画像や Web ページを自分のログの中にそのまま表示する方法も覚えました。だからアルバムアートを作ると、そのアルバムアートが目の前に見えます。

## 3日目：名前とバージョン番号

3月13日の朝、アプリに名前がつきました。午前9時6分のコミットは *「rename app to Agent!」* です。びっくりマークも、わざとです。

20分後、今でも大事な変更が入りました。スクリプトが別々のプログラムではなくなり、アプリの中に直接読み込まれる **動的ライブラリ** になったのです。だから AgentScripts は、もう一度許可を求めなくても、Agent! と同じ Mac の権限を持てます。

その日のうちに **1.0.0** のタグが打たれました。最初のコミットから数えて、**2日足らずで177コミット** です。1.0.1 から 1.0.16 までは、その後の8日間で続きました。

小さな話をひとつ。初期のコミットの作者名は人ではありません。**「Agent! for MacOS」** です。

## 大きくなる

最初の全力疾走のあと、物語はスピードを上げます。

- **4月6日。** ほぼ1か月分の履歴が、きれいな最初のコミット1つにまとめられました。完全な履歴はバックアップに残してあります。
- **4月7日。** 「コーディングモード」「自動化モード」「標準モード」が[まるごと取り外されました](/blog/why-we-ripped-out-modes/)。エージェントはひとつ、道具は全部、いつでも。
- **4月。** Mac の上で直接、無料で動く頭脳として Apple Intelligence が仲間入りしました。
- **8月31日。** プロジェクトは GitHub の組織 `macOS26` から **AgentiLoop** へ引っ越し、Web サイトは **agentiloop.ai** になりました。
- **最近。** Agent! は [macOS 14.6 と Intel Mac で動くこと](/blog/sonoma-intel-and-the-mac-that-was-not-dead-yet/)を覚え、自分のターミナル版の弟妹づくりも手伝いました。Rust の [AgentiLoopCLI](https://github.com/AgentiLoop/AgentiLoopCLI) と Go の [AgentiLoopGo](https://github.com/AgentiLoop/AgentiLoopGo) です。

始まりは頭脳ひとつでした。今では Apple Intelligence に加えて **23の AI プロバイダー** と一緒に働いています。4月の大掃除以来、メインブランチには 1,300 を超えるコミットが積み重なりました。

## 今の形になった理由

Agent! のちょっと変わったところは、ほとんどが最初の3日間にさかのぼります。

ヘルパーが2つあって、1つはあなた用、1つは root 用なのは、1日目に両方が必要だったからです。100% Swift なのは、材料になった部品が Swift だったからです。65個の NPM パッケージの山ではなく、オリジナルのコードでできています。アクセシビリティと AppleScript で他のアプリを名前で操作するのは、2日目をまるごと使って Mac に礼儀正しくお願いする方法を学んだからです。そして今でも、大きなキャンセルボタンがあります。

大きなものはみんな、小さなブロックの山から始まります。この山は3年かけて積み上がりました。そして3月11日、ついに誰かが、ほかのブロックをまとめてつなぎとめるブロックを見つけました。それがループです。
