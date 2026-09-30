---
title: Sonoma と Intel と、まだ死んでいなかった Mac
description: Agent! for Mac が macOS Sonoma 14.6 以降の Apple Silicon と Intel で動くようになりました。macOS 26 より前の OS 向けのバージョンを求める声がたくさんありました。お待たせしました。
tags: リリースノート, 舞台裏
---
正直に言いましょう。Agent! が「macOS 26 が必要です」と言っていたころ、たくさんのいい Mac が置いてけぼりになっていました。

Sonoma を使っていたら、残念でした。Sequoia でも同じ。Intel Mac なら、そもそも話にすら入れてもらえませんでした。

それがずっと引っかかっていました。あの Mac たちはまだ動きます。みんな毎日使っています。コードを書いて、仕事を回して、ブラウザのタブを開きすぎています。何も悪いことはしていません。ただ最新の OS じゃなかっただけです。

でも、もう違います。**Agent! for Mac は macOS Sonoma 14.6 以降で、Apple Silicon でも Intel でも動くようになりました。**

macOS 26 より前の OS 向けのバージョンを待っていた人はたくさんいました。これは、そんなあなたのためのものです。

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 340" role="img" aria-labelledby="macs-title macs-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="macs-title">うれしそうな2台の Mac と新しい看板</title>
<desc id="macs-desc">机の上に Intel Mac と Apple Silicon Mac が並び、どちらも笑顔です。その間の看板では「macOS 26 専用」に線が引かれ、「macOS 14.6+、Apple Silicon と Intel」に書き換えられています。</desc>
<rect width="760" height="340" rx="20" fill="#eef6ff"/>
<rect x="182" y="215" width="16" height="50" fill="#8a97a8"/><rect x="150" y="263" width="80" height="12" rx="4" fill="#8a97a8"/>
<rect x="562" y="215" width="16" height="50" fill="#8a97a8"/><rect x="530" y="263" width="80" height="12" rx="4" fill="#8a97a8"/>
<rect x="374" y="170" width="12" height="105" fill="#8b684c"/>
<path d="M30 280H730" stroke="#8b684c" stroke-width="10" stroke-linecap="round"/>
<rect x="90" y="100" width="200" height="125" rx="14" fill="#c9d3df" stroke="#173452" stroke-width="4"/>
<rect x="104" y="114" width="172" height="97" rx="6" fill="#559ef5"/>
<circle cx="160" cy="150" r="9" fill="#fff"/><circle cx="220" cy="150" r="9" fill="#fff"/>
<circle cx="162" cy="151" r="4" fill="#173452"/><circle cx="222" cy="151" r="4" fill="#173452"/>
<path d="M165 178Q190 196 215 178" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
<rect x="470" y="100" width="200" height="125" rx="14" fill="#e7e2f7" stroke="#173452" stroke-width="4"/>
<rect x="484" y="114" width="172" height="97" rx="6" fill="#7b6ad6"/>
<circle cx="540" cy="150" r="9" fill="#fff"/><circle cx="600" cy="150" r="9" fill="#fff"/>
<circle cx="542" cy="151" r="4" fill="#173452"/><circle cx="602" cy="151" r="4" fill="#173452"/>
<path d="M545 178Q570 196 595 178" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
<rect x="303" y="60" width="154" height="115" rx="10" fill="#fff" stroke="#8b684c" stroke-width="4"/>
<g font-family="system-ui,sans-serif" text-anchor="middle" fill="#173452">
<text x="380" y="88" font-size="16" fill="#8a97a8">macOS 26 専用</text>
<text x="380" y="118" font-size="19" font-weight="700">macOS 14.6+</text>
<text x="380" y="141" font-size="16">Apple Silicon</text>
<text x="380" y="162" font-size="16">と Intel</text>
<text x="190" y="315" font-size="20">Intel Mac</text>
<text x="570" y="315" font-size="20">Apple Silicon Mac</text>
</g>
<path d="M318 83H442" stroke="#d94877" stroke-width="3" stroke-linecap="round"/>
</svg>
<figcaption>同じ机。同じ Mac。新しい看板。</figcaption>
</figure>

## そもそも、なぜ 26 専用だったのか

Agent! は FoundationModels というフレームワークを通じて、Apple のオンデバイスモデルを使っています。これはメインの頭脳ではありません。重い仕事は、あなたが選んだプロバイダーがやります。でもオンデバイスモデルは、コンテキスト圧縮中の要約、トークンのカウント、アプリ起動時のセッションのウォームアップといった、ちょっとした仕事を手伝ってくれます。

ここに落とし穴があります。FoundationModels は macOS 26 にしか存在しません。コードがその型を一つでも口にしただけで、古い Mac 向けにはビルドできなくなります。コンパイラが「ダメ」と言うのです。

だから楽な道は、macOS 26 を必須にして先へ進むことでした。少なくとも、僕にとっては楽でした。ほかのみんなにとっては、あまりありがたくない話です。

正直、ちょっとバカげていました。オンデバイスモデルはお手伝い役です。あればうれしい。でも、Agent! が動く理由だったことは一度もありません。お手伝い役のために古い Mac を全部締め出すなんて、パセリが切れたから晩ごはんを作らない、と言うようなものです。

## じゃあ、どう直すのか？

まず聞くんです。Agent! はオンデバイスモデルに触る前に確認します。いま macOS 26 の上？もしそうなら、よし、使おう。違うなら、そのコードはただ実行されないだけで、本当の仕事はプロバイダーが続けてくれます。

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 300" role="img" aria-labelledby="fork-title fork-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="fork-title">使う前に聞く</title>
<desc id="fork-desc">フローチャート。Agent! はオンデバイスモデルを使いたい。そこで「これは macOS 26？」と聞きます。「はい」ならオンデバイスのお手伝い機能を使います。「いいえ」ならそれをスキップし、プロバイダーはそのまま動き続けます。</desc>
<defs><marker id="fork-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0 0L10 5 0 10Z" fill="#4b617e"/></marker></defs>
<rect width="760" height="300" rx="20" fill="#f0f5fb"/>
<g fill="none" stroke="#4b617e" stroke-width="4"><path d="M380 90V113" marker-end="url(#fork-arrow)"/><path d="M320 150H170V206" marker-end="url(#fork-arrow)"/><path d="M440 150H590V206" marker-end="url(#fork-arrow)"/></g>
<rect x="230" y="30" width="300" height="60" rx="18" fill="#d7eaff" stroke="#3377b9" stroke-width="3"/>
<path d="M380 115L440 150 380 185 320 150Z" fill="#fce9b6" stroke="#9a701b" stroke-width="3"/>
<rect x="40" y="210" width="260" height="66" rx="18" fill="#cff3e4" stroke="#29836a" stroke-width="3"/>
<rect x="460" y="210" width="260" height="66" rx="18" fill="#dfd9ff" stroke="#7760b5" stroke-width="3"/>
<g font-family="system-ui,sans-serif" text-anchor="middle" fill="#173452">
<text x="380" y="67" font-size="17" font-weight="700">オンデバイスモデルを使いたい？</text>
<text x="380" y="156" font-size="16" font-weight="700">macOS 26?</text>
<text x="245" y="140" font-size="17">はい</text>
<text x="515" y="140" font-size="17">いいえ</text>
<text x="170" y="238" font-size="18" font-weight="700">使う。</text>
<text x="170" y="262" font-size="15">要約、トークン数のカウント</text>
<text x="590" y="238" font-size="18" font-weight="700">スキップ。</text>
<text x="590" y="262" font-size="15">プロバイダーはそのまま動く</text>
</g>
</svg>
<figcaption>トリックはこれで全部です。使う前に聞く。</figcaption>
</figure>

もうひとつ、ちょっとした問題があります。Swift では、実行中の OS に存在しない型のプロパティをクラスに持たせることができません。そこでセッションはただの `AnyObject` として保存し、macOS 26 のコードの中でだけキャストし直します。きれいじゃない。でもちゃんと動きます。

## コミット

すべては 2026年9月27日に起きました。コミット4つ、1日で。全部 Git に残っています。

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 260" role="img" aria-labelledby="day-title day-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="day-title">2026年9月27日、コミットごとに</title>
<desc id="day-desc">正午から20時までのタイムライン。コミット ea5ce624 が 12:46、4d7fca86 が 12:57、3a993205 が 19:14、81079e2a が 19:32。</desc>
<rect width="760" height="260" rx="20" fill="#f0f5fb"/>
<g stroke="#4b617e" stroke-width="2"><path d="M121 104V130M136 130V148M639 104V130M663 130V148"/></g>
<path d="M60 130H700" stroke="#4b617e" stroke-width="4" stroke-linecap="round"/>
<g fill="#227657" stroke="#fff" stroke-width="3"><circle cx="121" cy="130" r="8"/><circle cx="136" cy="130" r="8"/><circle cx="639" cy="130" r="8"/><circle cx="663" cy="130" r="8"/></g>
<g font-family="system-ui,sans-serif" text-anchor="middle" fill="#173452">
<text x="121" y="56" font-size="16" font-weight="700">ゲートで囲う</text><text x="121" y="76" font-size="15">ea5ce624</text><text x="121" y="96" font-size="15">12:46</text>
<text x="136" y="166" font-size="15">12:57</text><text x="136" y="186" font-size="15">4d7fca86</text><text x="136" y="206" font-size="16" font-weight="700">パッケージ更新</text>
<text x="639" y="56" font-size="16" font-weight="700">ドキュメント</text><text x="639" y="76" font-size="15">3a993205</text><text x="639" y="96" font-size="15">19:14</text>
<text x="663" y="166" font-size="15">19:32</text><text x="663" y="186" font-size="15">81079e2a</text><text x="663" y="206" font-size="16" font-weight="700">1.1.76</text>
<g font-size="14" fill="#4b617e"><text x="60" y="244">正午</text><text x="380" y="244">16:00</text><text x="700" y="244">20:00</text></g>
</g>
</svg>
<figcaption>コミット時刻は Git より、米国東部時間。</figcaption>
</figure>

**[`ea5ce624`](https://github.com/AgentiLoop/Agent/commit/ea5ce62493aef5ca74e694a8ec85b16621ec6388)**：FoundationModels の使用箇所をすべて macOS 26 のゲートの内側に入れました。モデルサービス、Apple Intelligence メディエーター、`AgentApp` の起動時プリウォーム、`Compression.swift` の要約とトークンカウント、そして `AboutSelf`。古いシステムでは、ビルドを拒否する代わりに「macOS 26 以降が必要です」と表示するだけになりました。すでに 26 を使っているなら、何も変わりません。

**[`4d7fca86`](https://github.com/AgentiLoop/Agent/commit/4d7fca863a15d91d8e3734f991fabfcb90da734c)**：AgentiLoop の Swift パッケージ10個すべてを、macOS 14 をサポートするリリースに更新しました。AgentAccess、AgentAudit、AgentColorSyntax、AgentD1F、AgentEventBridges、AgentLLM、AgentMCP、AgentSwift、AgentTerminalNeo、AgentTools。10個全部です。ここが地味にしんどいところでした。Xcode で数字をひとつ変えて終わり、とはいきません。アプリが依存しているものは全部、一緒に連れていかないといけないんです。同じコミットで、トークンカウントの呼び出しのひとつが 26.0 ではなく macOS 26.4 を必要とすることにも気づいたので、そのチェックを厳しくしました。

**[`3a993205`](https://github.com/AgentiLoop/Agent/commit/3a9932053630a21ec9df481c8f137cea30ff87a0)**：ドキュメント。README と FAQ に **Apple Silicon または Intel、macOS 14.6+** と書くようになりました。増えたのは「または Intel」のひとことだけ。それを勝ち取るのに、けっこう時間がかかりました。

**[`81079e2a`](https://github.com/AgentiLoop/Agent/commit/81079e2a937f62d2d68389a3c124214f80cb3bc3)**：バージョン 1.1.76、ビルド 276、デプロイメントターゲット 14.6。出荷です。

以上です。魔法はありません。`#available` のチェックと、パッケージの更新と、怒鳴られなくなるまでビルドし続けること。それだけです。

## 注意書き（正直なやつ）

Sonoma や Sequoia では、Apple Intelligence まわりの機能は使えません。Apple がそこで提供していないからです。Agent! はそこを避けて動くだけです。困ることはあまりないはずです。本当の仕事はどのみちプロバイダーがやっていたので。

Intel Mac は、やっぱり Intel Mac です。クラウドのプロバイダーと組み合わせれば Agent! は問題なく動きます。大きなローカルモデルは話が別です。FAQ にはすでに、30B のローカルモデルには 64GB 以上が必要と書いてあります。これは古い Mac に限らず、どの Mac でも同じです。

そして 14.6 が下限です。お使いの Mac で Sonoma が動かないなら、そこは僕にもどうにもできません。僕はけっこうやる男ですが、そこまでではないんです。

## Intel のみなさん、ここはあなたたちへ

まだ現役だからという理由で Intel Mac を使い続けている人がたくさんいるのは知っています。支払いはもう済んでいる。環境はばっちり整っている。どこに何があるかもわかっている。アプリを試すためだけに新しいマシンを買いたくはない。

まったくもってその通り。そうする必要なんてありません。

まだ macOS 26 に移る気になれない Apple Silicon のみなさんも同じです。マイナーアップデートを待っているのかもしれない。必要なツールがまだ対応していないのかもしれない。単に気が乗らないだけかもしれない。責めたりしません。好きなだけ Sonoma にいてください。

## さあ、手に入れよう

**Agent! for Mac。macOS Sonoma 14.6 以降。Apple Silicon と Intel。**

待っていた人、お待たせしました。ぜひ試してみて、あなたのマシンでどう動いたか教えてください。特に Intel 勢のみなさん。ぜひ聞かせてほしいです。

あなたの Mac はまだ死んでいません。招待状が必要だっただけなんです。

コード付きの詳しい解説が読みたい？[エンジニアリング解説記事](/blog/agent-now-runs-on-macos-14-6-and-intel/)をどうぞ。
