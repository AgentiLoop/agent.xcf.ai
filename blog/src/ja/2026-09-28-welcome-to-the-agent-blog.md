---
title: Agent! ブログへようこそ：ひとつのアプリで、あらゆる AI を使い、Mac を完全に操る
description: AgentiLoop Agent! とは何か、どのように作られているのか、そしてこの毎日更新のブログで何を取り上げていくのかを、ソースコードから直接お伝えします。
tags: お知らせ, アーキテクチャ
---
ここは、ネイティブ macOS AI エージェント **AgentiLoop Agent!** の公式ブログです。方針はシンプルで、1 日 1 本の記事を、私たちが最もよく知っているもの、つまりコードベースそのものを題材に書いていきます。エージェントループの仕組み、各ガードレールがなぜその形になっているのか、最新のリリース候補で何が変わったのかといった掘り下げに加え、ときには AI エージェントを取り巻くより広い世界にも目を向けます。

初めての方にとって、この最初の記事が道案内になります。

## Agent! とは

Agent! は 100% ネイティブの Swift / SwiftUI アプリです。やりたいことを入力する（または話しかける）と、やり方を説明するだけでなく、Mac 上で実際に作業をこなします。

- **本当にコードを書きます。** プロジェクトを読み込み、文字列置換方式の diff でファイルを編集し、Xcode でビルドし、エラーを読んで修正し、git でコミットします。
- **あらゆる Mac アプリを操作します。** アクセシビリティ API に加え、AppleScript、JXA、そして 51 個の ScriptingBridge アプリブリッジを利用します。
- **ユーザーとして、あるいは root としてシェルコマンドを実行します。** SMAppService で登録され、XPC 経由でアクセスする Launch Agent と Launch Daemon を通じて実行します。
- **23 の LLM プロバイダーと連携します。** さらにオンデバイスの Apple Intelligence にも対応。Claude、Codex、OpenAI、Gemini、Grok、Mistral、DeepSeek、Qwen、Z.ai、OpenRouter、Ollama、vLLM、LM Studio などが使えます。
- **声を聞き取ります。** *"Agent!"* と呼びかけてからタスクを伝えるか、iPhone から iMessage でメッセージを送ってください（承認済みの送信者のみ）。

README ではこれを一言で表しています。 *Siri は答える。Agent! は動く。*

## NPM も Electron も使わない

多くの人が最も驚くのは、Agent! に *含まれていない* ものです。Electron のシェルも、Node ランタイムも、`node_modules` もありません。依存している Swift パッケージはすべて同じ作者が書いたもので、それぞれが [AgentiLoop](https://github.com/AgentiLoop) organization 配下の独立したリポジトリで管理されています。

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

その結果、メモリ使用量がごくわずかでありながら、Xcode の自動化、Swift の構文解析、アクセシビリティ、AppleScript、Safari の自動化、MCP をすぐに使えるアプリになりました。

## 中心にあるループ

すべては 1 つの考え方から成り立っています。それが **自己検証型のタスクループ** です。モデルが推論し、ツールを呼び出し、実際の結果を確認して、自ら軌道修正します。このループを信頼できるものにしているのが、いくつかのルールです。

- **ツール呼び出しは偽装できません。** すべての呼び出しは単一のディスパッチャーを経由し、実際の出力を返します。モデルがツールを呼び出さずに *「クリックしました」* と主張した場合、Agent! は訂正を差し込みます。
- **「完了」には証拠が必要です。** タスクは、`goal_state` の基準がビルド成功やテスト合格といった証拠とともに完了とマークされるまで、終了を宣言できません。
- **編集の前に読む。** モデルがまだ読んでいないファイルや、読んだ後にディスク上で変更されたファイル（SHA-256 で確認）への編集は拒否されます。拒否の際にはモデルの代わりにファイルを読み込むので、次の試行では最新の内容が使われます。
- **すべて元に戻せます。** すべての編集は 1 週間スナップショットとして保存されます。1 つのファイルだけをロールバックすることも、`rewind_task` でタスク全体を巻き戻すこともできます。

これらについては、今後の記事で 1 つずつ詳しく解説していきます。

## AgentScript：フル権限を持つ Swift

特に際立った仕組みの 1 つが **AgentScript** です。スクリプトはただの Swift ファイルです。Agent! は SwiftPM で各スクリプトを `.dylib` にコンパイルし、`dlopen` でプロセス内にロードします。そのためスクリプトは、アクセシビリティ、オートメーション、カレンダー、連絡先、メール、写真など、Agent! 自身の macOS 権限をそのまま引き継ぎます。書くのに必要なのはエントリーポイント 1 つだけです。

```swift
import Foundation
import CalendarBridge   // any `import XBridge` auto-wires, no Package.swift edits

@_cdecl("script_main")
public func scriptMain() -> Int32 {
    print("Hello from AgentScript! 👋")
    return 0
}
```

スクリプトが出力した内容はすべてモデルに返され、戻り値は終了ステータスになります。アプリには `TodayEvents`、`NowPlaying`、`CheckMail`、`CreateDmg` など、約 35 個のサンプルが同梱されています。

## 読んで確かめられる安全性

Agent! は root として実行できるため、安全性はプレゼン資料の 1 枚のスライドではありません。GitHub で開いて読めるコードです。ハードコードされた `ShellSafetyService` が、壊滅的なコマンドをディスパッチ前に拒否し、特権デーモン側でも同じチェックがもう一度実行されます。さらに、オプションのセカンドオピニオンである **Jev** が、コマンドがデータを破壊する可能性を評価します。その仕組みは [最初の詳細解説記事](/blog/inside-agent-shell-guardrails/) で詳しく紹介しています。

## 広がり続けるファミリー

同じエージェントループが、今では macOS、Windows、Linux のターミナルでも動作します。同じ機能を持つ 2 つの CLI として、Rust 製の [AgentiLoopCLI](https://github.com/AgentiLoop/AgentiLoopCLI) と Go 製の [AgentiLoopGo](https://github.com/AgentiLoop/AgentiLoopGo) があります。README に載っている面白い話として、この小さな弟妹たちは Mac 版 Agent! 自身が書き上げたものです。

## このブログで扱う内容

- **内部構造：** エージェントループ、コンテキスト圧縮、ツールのディスパッチ、サブエージェント、メモリ、プラン。
- **セキュリティ：** ガードレール、XPC の信頼モデル、そして最近のエージェント関連インシデントが開発者に教えてくれること。
- **理由まで伝えるリリースノート：** 各ビルドで何が変わったのか、そしてそのきっかけとなったバグ。
- **ハウツー：** AgentScript のレシピ、予算に合わせたプロバイダーの選び方、完全ローカルでの実行方法。
- **エージェントを取り巻く広い世界：** ニュースやレビューを、常に「あなたの Mac にとって何を意味するか」という視点で。

Agent! は macOS 14.6 以降で動作し、Apple Silicon と Intel の両方に対応、個人利用は無料です。下のリンクから入手して、また明日お越しください。
