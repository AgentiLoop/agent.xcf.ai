---
title: Agent! ブログへようこそ：ひとつのアプリで、あらゆる AI を使い、Mac を完全に操る
description: AgentiLoop Agent! とは何か、なぜこういう作りにしたのか、そしてここで何を読めるのかを、ソースコードから直接お伝えします。
tags: お知らせ, アーキテクチャ
---
<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 340" role="img" aria-labelledby="map-title map-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="map-title">小さな Mac があなたに地図を手渡す</title>
<desc id="map-desc">にっこり笑った Mac が机の上に立ち、広げた地図を手にしています。地図には点線の道でつながった 4 つの地点があります：あらゆる AI、ループ、AgentScript、安全性。</desc>
<rect width="760" height="340" rx="20" fill="#eef6ff"/>
<path d="M30 290H730" stroke="#8b684c" stroke-width="10" stroke-linecap="round"/>
<rect x="132" y="228" width="16" height="52" fill="#8a97a8"/><rect x="100" y="276" width="80" height="12" rx="4" fill="#8a97a8"/>
<rect x="40" y="100" width="200" height="130" rx="14" fill="#c9d3df" stroke="#173452" stroke-width="4"/>
<rect x="54" y="114" width="172" height="102" rx="6" fill="#559ef5"/>
<circle cx="110" cy="152" r="9" fill="#fff"/><circle cx="170" cy="152" r="9" fill="#fff"/>
<circle cx="112" cy="153" r="4" fill="#173452"/><circle cx="172" cy="153" r="4" fill="#173452"/>
<path d="M115 180Q140 198 165 180" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
<path d="M228 180Q262 176 290 160" fill="none" stroke="#173452" stroke-width="6" stroke-linecap="round"/>
<path d="M290 50L400 70L510 50L620 70V260L510 240L400 260L290 240Z" fill="#fff8e6" stroke="#8b684c" stroke-width="4" stroke-linejoin="round"/>
<path d="M400 70V260M510 50V240" stroke="#e6d6b3" stroke-width="3"/>
<path d="M350 175C380 140 410 140 440 140S490 190 520 190 560 130 580 110" fill="none" stroke="#d94877" stroke-width="4" stroke-dasharray="3 10" stroke-linecap="round"/>
<circle cx="350" cy="175" r="11" fill="#559ef5" stroke="#173452" stroke-width="3"/>
<circle cx="440" cy="140" r="11" fill="#7b6ad6" stroke="#173452" stroke-width="3"/>
<circle cx="520" cy="190" r="11" fill="#22c55e" stroke="#173452" stroke-width="3"/>
<circle cx="580" cy="110" r="11" fill="#f59e0b" stroke="#173452" stroke-width="3"/>
<g font-family="system-ui,sans-serif" text-anchor="middle" fill="#173452">
<text x="350" y="152" font-size="15" font-weight="700">あらゆる AI</text>
<text x="440" y="117" font-size="15" font-weight="700">ループ</text>
<text x="520" y="222" font-size="15" font-weight="700">AgentScript</text>
<text x="580" y="90" font-size="15" font-weight="700">安全性</text>
<text x="345" y="88" font-size="14" fill="#8b684c">あなたの地図</text>
<text x="140" y="322" font-size="18">Agent! for Mac</text>
</g>
</svg>
<figcaption>どんなブログにも最初の記事が必要です。この記事は、その地図です。</figcaption>
</figure>

こんにちは、Todd です。ネイティブ macOS AI エージェント **AgentiLoop Agent!** を作っていて、ここはそのブログです。

README やリリースノートには収まりきらない Agent! の話をする場所が欲しかったんです。あるガードレールがなぜその形になっているのか。エージェントループがなぜ自分の仕事をチェックするのか。リリース候補で何が壊れて、どうやって直したのか。ここで読める内容の多くは、コードベースから直接持ってきたものです。それが私の一番よく知っているものだからです。ときどきは、AI エージェントを取り巻くもっと広い世界にも目を向けて、それがあなたの Mac にとってどんな意味を持つのかも考えていきます。

初めての方は、ここから始めてください。この記事を地図だと思ってもらえればと思います。

## Agent! とは

Agent! は 100% ネイティブの Swift と SwiftUI で作られています。やりたいことを入力する（あるいは話しかける）と、やり方を説明するのではなく、あなたの Mac 上で実際に作業をこなしてくれます。

- **本物のコードを書きます。** プロジェクトを読み込み、文字列置換方式の diff でファイルを編集し、Xcode でビルドし、エラーを読んで直し、git でコミットします。
- **あらゆる Mac アプリを操作します。** アクセシビリティ API に加えて、AppleScript、JXA、51 個の ScriptingBridge アプリブリッジを使います。
- **あなたとして、あるいは root としてシェルコマンドを実行します。** SMAppService で登録し、XPC 経由でアクセスする Launch Agent と Launch Daemon を通して動きます。
- **23 の LLM プロバイダーに対応しています。** さらにオンデバイスの Apple Intelligence も。Claude、Codex、OpenAI、Gemini、Grok、Mistral、DeepSeek、Qwen、Z.ai、OpenRouter、Ollama、vLLM、LM Studio などが使えます。
- **ちゃんと聞いています。** *"Agent!"* と呼びかけてからタスクを伝えるか、iPhone から iMessage で送ってください（承認済みの送信者のみ）。

README ではひとことでこうまとめています。*Siri は答える。Agent! は動く。*

## NPM も Electron もなし

ここはよく驚かれるところです。Electron のシェルはありません。Node ランタイムもありません。いつの間にかディスクを食いつぶしていく `node_modules` フォルダもありません。Agent! が依存している Swift パッケージはすべて私が書いたもので、それぞれ [AgentiLoop](https://github.com/AgentiLoop) organization の下にある独立したリポジトリに置いてあります。

| パッケージ | 役割 |
|---|---|
| AgentTools | ツールスキーマ、システムプロンプト、プロバイダー管理 |
| AgentLLM | LLM プロバイダーのプロトコル、型、レジストリ |
| AgentMCP | MCP クライアント（stdio と HTTP） |
| AgentAccess | アクセシビリティによる自動化 |
| AgentEventBridges | 50 以上の Mac アプリ向け ScriptingBridge プロトコル |
| AgentD1F | 複数行 diff エンジン |
| AgentSwift | SwiftSyntax によるコード解析 |
| AgentColorSyntax · AgentTerminalNeo | シンタックスハイライト · レトロなターミナル風 Markdown |
| AgentAudit | `os.log` による監査ログ |

その結果、メモリはほんの少ししか使わないのに、Xcode の自動化、Swift の構文解析、アクセシビリティ、AppleScript、Safari の自動化、MCP が最初から全部そろったアプリになりました。

## 中心にあるループ

Agent! のすべては、ひとつの考え方から成り立っています。**自己検証型のタスクループ** です。モデルが考え、ツールを呼び出し、実際の結果を見て、自分で軌道修正する。これは信頼できてこそ意味があるので、いくつかのルールを最初から組み込んであります。

- **ツール呼び出しはごまかせません。** すべての呼び出しは単一のディスパッチャーを通り、実際の出力を返します。モデルが実際にはツールを呼ばずに *「クリックしました」* と言ったら、Agent! はそれを指摘して訂正を送ります。
- **「完了」には証拠が必要です。** `goal_state` の基準が、ビルド成功やテスト合格といった証拠つきでチェックされるまで、タスクは自分で完了を名乗れません。
- **編集の前に読む。** モデルがまだ読んでいないファイルや、読んだ後にディスク上で変わったファイル（SHA-256 で確認）への編集は、Agent! が拒否します。拒否するときに最新のファイルをモデルに渡すので、次の試行では正しい行が使われます。
- **何でも元に戻せます。** すべての編集は 1 週間スナップショットとして残ります。1 つのファイルだけロールバックすることも、`rewind_task` でタスク全体を巻き戻すこともできます。

これらは今後の記事で 1 つずつ分解して解説していきます。

## AgentScript：フル権限を持つ Swift

AgentScript は、私のお気に入りの部分のひとつです。スクリプトはただの Swift ファイルです。Agent! は SwiftPM で各スクリプトを `.dylib` にコンパイルし、`dlopen` でプロセス内にロードします。だからあなたのスクリプトは、Agent! がすでに持っている macOS の権限をそのまま使えます。アクセシビリティ、オートメーション、カレンダー、連絡先、メール、写真などです。必要なのはエントリーポイント 1 つだけ。

```swift
import Foundation
import CalendarBridge   // any `import XBridge` auto-wires, no Package.swift edits

@_cdecl("script_main")
public func scriptMain() -> Int32 {
    print("Hello from AgentScript! 👋")
    return 0
}
```

スクリプトが出力したものはすべてモデルに返り、戻り値が終了ステータスになります。アプリには `TodayEvents`、`NowPlaying`、`CheckMail`、`CreateDmg` など、約 35 個のサンプルが付属しています。

## 読んで確かめられる安全性

Agent! は root としてコマンドを実行できます。これはかなりの信頼をお願いすることなので、安全性をプレゼン資料の 1 枚のスライドで済ませるわけにはいきません。安全性はコードであり、GitHub で実際に読めます。ハードコードされた `ShellSafetyService` が、壊滅的なコマンドを送信される前に拒否し、特権デーモンの側でも同じチェックをもう一度行います。さらに、**Jev** というオプションのセカンドオピニオンがあり、コマンドがデータを破壊する可能性がどれくらいあるかを評価します。その仕組みは [最初の詳細解説](/blog/inside-agent-shell-guardrails/) でじっくり紹介しています。

## 広がり続けるファミリー

同じエージェントループが、今ではターミナルでも、macOS、Windows、Linux で動きます。同じ機能を持つ CLI が 2 つあって、Rust 製の [AgentiLoopCLI](https://github.com/AgentiLoop/AgentiLoopCLI) と Go 製の [AgentiLoopGo](https://github.com/AgentiLoop/AgentiLoopGo) です。README の中で私が一番好きな小ネタは、この小さな弟妹たちを Mac 版 Agent! が自分で書いた、という話です。

## ここで読めること

- **内部構造：** エージェントループ、コンテキスト圧縮、ツールのディスパッチ、サブエージェント、メモリ、プラン。
- **セキュリティ：** ガードレール、XPC の信頼モデル、そして最近のエージェント関連のインシデントから私たちみんなが学べること。
- **「なぜ」まで伝えるリリースノート：** 各ビルドで何が変わったのか、そしてそれを必要にしたバグ。
- **ハウツー：** AgentScript のレシピ、予算に合わせたプロバイダーの選び方、完全ローカルでの動かし方。
- **エージェントを取り巻く広い世界：** ニュースやレビューを、いつも「あなたの Mac にとってどういう意味があるか」に引き戻してお届けします。

Agent! は macOS 14.6 以降で、Apple Silicon と Intel の両方で動き、個人利用は無料です。下から入手して、何か本当にやりたいことを任せてみてください。どうだったか、ぜひ教えてくださいね。
