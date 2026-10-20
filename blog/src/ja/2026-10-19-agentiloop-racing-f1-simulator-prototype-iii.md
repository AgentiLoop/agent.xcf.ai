---
title: AgentiLoop Racing, Prototype III：ブラウザで動く F1 シミュレーター
description: AgentiLoop Racing は、Agent! が Three.js で作った、ブラウザで動くオープンホイールのレーシングシミュレーターです。240 Hz の物理演算、18 の実在サーキット、AI ドライバー、ピットストップ、タイヤコンパウンド、燃料、ERS、DRS を備えています。f1.gokart.games でプレイできます。
tags: Showcase, JavaScript
---
<figure style="margin:2rem 0">
<img src="/agentiloop-racing-og.jpg" alt="AgentiLoop Racing：ブラウザのシミュレーターでコースを走るオープンホイールのレースカー。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>AgentiLoop Racing, Prototype III。グリッド上のすべてのマシンは 2026 年型 RB22 のモデルで、それぞれ専用のカラーとスポンサー名で塗り直されています。</figcaption>
</figure>

**今すぐプレイ：[f1.gokart.games](https://f1.gokart.games)。** ダウンロードもインストールも不要です。WebGL 対応のブラウザが必要で、キーボードか Xbox（またはその他の標準的な）コントローラーで遊べます。

AgentiLoop Racing は、素の JavaScript と Three.js で書かれた F1 スタイルのレーシングシミュレーターです。最初のコミットは決定論的な四輪の車両モデルで、10 月 16 日の夜に入りました。それから 3 日と 109 コミットを経て、今では 18 の実在サーキットで AI のフルフィールドとレースができます。ピットストップ、タイヤコンパウンド、燃料、ERS、DRS、物理演算から作られるエンジン音、そしてミラーに後続車が映るコックピットカメラも備えています。書いたのは Agent! で、小さくテスト済みのコミットをひとつずつ積み重ねていきました。

最初に正直なラベルをひとつ。README に書かれているものと同じです。これは**プロトタイプであり、検証済みの Formula 1 シミュレーターではありません**。マシンのパラメーターは説明用の仮定であり、F1 の実測データではありません。

## まずは物理演算

このプロジェクトは物理演算のテストベッドとして始まり、3D は後から加わりました。`physics.mjs` はマシンを固定の **240 Hz** で進めます。各ホイールはそれぞれ独自の慣性とスリップを持ち、各タイヤにはピークグリップからスライドに至るグリップ特性、スリップアングルの緩和、温度、摩耗があります。サスペンションに支えられた車体は空力荷重を受けてロール、ピッチ、スクワットし、それは 3D のマシンでも目に見えます。ギアボックスはオートマチックかパドルシフトで、壁に向かって止まってしまったときのために、安全策付きのリバースギアもあります。

パワーユニットもモデル化されています。燃料は実際の質量として積まれているので、燃えるにつれてマシンは軽くなります。ハイブリッドは 100 km/h 以上で最大 120 kW を、1 周あたり 4 MJ の範囲で放出し、ブレーキング時に回生します。

テストスイートは Node 組み込みのテストランナーだけを使っています。現在 `node --test` は 158 のテストを実行し、すべてパスしています。全開のマシンが壁をすり抜けないこと、3D モデルがタイヤとプランクだけで地面に触れていることなどを確認しています。

## 18 の実在サーキット

<figure style="margin:2rem 0">
<img src="/agentiloop-racing-monza.jpg" alt="AgentiLoop Racing：モンツァで AI ドライバーたちとレース。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>モンツァでのレース。タイミングボックス、順位表、ミニマップはレース中リアルタイムで更新されます。</figcaption>
</figure>

架空のスタジアムのテストコースのほかに、バーレーンからマイアミまで、モンツァ、シルバーストーン、スパ、モナコを含む 18 の実在サーキットがあり、レイアウトは実際のマシンの位置データから作られています。残りの調整には実データを使いました。

- **DRS ゾーン**は 2024 年のレーステレメトリー（OpenF1）から取っています。ドライバーが実際にフラップを開け閉めした場所です。モナコはピットストレートの 1 ゾーンだけです。
- **グリップは実際のコーナー速度に合わせて調整しました。** 18 サーキット全体で、オートパイロットのラップと実際のレースの最速ラップとの差は 17.9% から 5.8% に縮まりました。モナコでは、オートパイロットのラップが 84.2 秒から 74.4 秒になりました。実際のタイムは 73.9 秒です。
- **タイトなコーナーは広げて**最小半径を 15 m にし、マシンがモナコのサント・デボーテを曲がれるようにしました。
- **すべてのサーキットにピットレーンがあります。** スタート／フィニッシュストレートの横にあり、制限速度は 80 km/h で、マシンごとにピットボックスがあります。

<figure style="margin:2rem 0">
<img src="/agentiloop-racing-monaco.jpg" alt="AgentiLoop Racing：モナコでのレース。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>AI ドライバーたちと走るモナコ。</figcaption>
</figure>

## AI とレース

実在サーキットはソロのタイムトライアルとして始まります。**O** を押すか、URL に `?race` を付けると、フィールドとレースできます。スタートは 5 つのレッドシグナルが 1 秒ごとに点灯し、ランダムな待ち時間のあとに消えます。0.5 m 以上早く動くと、5 秒のフライングペナルティです。シグナルが点灯している間、キー **1–5** でそのグリッド位置のマシンに乗れます。

AI のマシンはレーシングラインをたどり、ストレートでは互いにスリップストリームを使い、そこから抜け出し、検知ポイントで 1 秒以内にいれば DRS を使い、ブレーキングでインに飛び込みます。オーバーテイクを調整したコミットでは、18 サーキットすべてでの 3 周レースで、追い抜きが 16 回から 34 回に増え、接触は 8 回からゼロになりました。バリアに引っかかって動けなくなったマシンは、リバースに入れ、交通と壁を確認した経路に沿って後退し、コースに復帰します。

レースルールも適用されます。完走者は全員 2 種類のタイヤコンパウンドを使わなければならないので、1 回はピットに入らないと失格になります。**B** でクルーにソフト、ミディアム、ハードを頼めます。ピットレーンでスピード違反をすると +5 秒です。

どのセッションもオートパイロットで始まるので、操作を引き継ぐまではマシンが自動で走ります。**P** を押すか、ゲームパッドに触れるか、ギアを変えれば、あなたの番です。

## マシンとコックピット

グリッド上のすべてのマシンは、Tyler_Dave による 2026 年型 RB22 のモデル（CC BY 4.0、Sketchfab より）を使っています。読み込み時に `rb22.mjs` がそれを各マシンのカラーで塗り直し、プロジェクトのスポンサー名とカーナンバーを投影します。近くでは、モデルの各パーツが細分化されて滑らかになり、遠くではより低ディテールのバージョンが使われます。

**C** を押すとコックピットになります。ドライバーの目線はサスペンションに支えられた車体に乗っているので、ロール、ピッチ、上下動で視界が動き、頭も G に合わせて少し動きます。ミラーは各ガラス越しに反射したシーンを描画し、自分の後輪は除外しているので、コースと後続車が見えます。

サウンドも物理演算から合成されています。回転数に追従する V6 の爆発音、ターボの唸り、スリップから生まれるタイヤのスキール音、そして速度とともに大きくなる風切り音です。

<figure style="margin:2rem 0">
<img src="/agentiloop-racing-spa.jpg" alt="AgentiLoop Racing：スパ・フランコルシャンでのタイムトライアル。" style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>スパのタイムトライアル。</figcaption>
</figure>

## 動画で見る

<figure style="margin:2rem 0">
<div style="position:relative;padding-top:56.25%;border-radius:20px;overflow:hidden">
<iframe src="https://www.youtube-nocookie.com/embed/2RluAIH3iQw?rel=0&amp;modestbranding=1&amp;color=white" title="AgentiLoop Racing — F1 simulator built with AgentiLoop.ai in Three.js" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="position:absolute;inset:0;width:100%;height:100%;border:0"></iframe>
</div>
</figure>

## 試してみる

- [モンツァでのレース](https://f1.gokart.games/?track=monza&race)
- [スパのタイムトライアル](https://f1.gokart.games/?track=spa)
- [ソフトタイヤでのスパ 5 周レース](https://f1.gokart.games/?track=spa&race&laps=5&tyre=soft)

ソースは [AgentiLoop/F1](https://github.com/AgentiLoop/F1) にあります。npm の依存関係もバンドラーもありません。Three.js は同梱されているので、フォルダ内で `python3 -m http.server` を実行するだけでローカルで動かせます。サイト自体は、リポジトリを静的ファイルとして配信する Cloudflare Worker です。

*AgentiLoop Racing は独立したプロジェクトであり、Formula 1、FIA、いずれのチームとも提携していません。3D モデルにはそれぞれ独自のライセンスがあります。リポジトリの `models/CREDITS.md` を参照してください。*
