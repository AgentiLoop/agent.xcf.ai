---
title: ファミリーそろってリリース：Agent! 1.1.87 と AgentiLoop CLI 0.0.5
description: Mac 版 Agent! にオートパイロット（Auto-Pilot）、6 つの新しいプロバイダ、より厳格なクリティック、macOS 14.6 サポートが加わりました。Rust 版と Go 版の CLI は、検索、Web 取得、ToDo、AGENTS.md、/undo、カスタムコマンド、--json と、より大きなツールボックスを手に入れました。
tags: お知らせ, リリース, クロスプラットフォーム
---
<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 380" role="img" aria-labelledby="fam-title fam-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="fam-title">AgentiLoop ファミリー：1 つの Mac アプリと 2 つのターミナル</title>
<desc id="fam-desc">中央に Agent! 1.1.87 と書かれた大きな Mac のウィンドウがあります。左側のターミナルウィンドウには小さなカニと Rust 0.0.5 のラベル、右側のターミナルウィンドウには小さなゴーファーと Go 0.0.5 のラベルが表示されています。点線が 3 つすべてを上部の共有ループ記号につないでいます。</desc>
<rect width="760" height="380" rx="20" fill="#0f1724"/>
<g fill="#6fb6ff" opacity=".35"><circle cx="60" cy="50" r="2"/><circle cx="700" cy="70" r="2"/><circle cx="640" cy="330" r="2"/><circle cx="110" cy="320" r="2"/><circle cx="380" cy="350" r="2"/><circle cx="520" cy="40" r="2"/><circle cx="230" cy="36" r="2"/></g>
<g fill="none" stroke="#6fb6ff" stroke-width="3" stroke-dasharray="4 8" stroke-linecap="round"><path d="M380 80V112"/><path d="M350 62Q170 70 140 150"/><path d="M410 62Q590 70 620 150"/></g>
<g fill="none" stroke="#9fd2ff" stroke-width="5" stroke-linecap="round"><path d="M380 55C392 39 412 39 412 55C412 71 392 71 380 55C368 39 348 39 348 55C348 71 368 71 380 55Z"/></g>
<rect x="250" y="112" width="260" height="190" rx="16" fill="#1d2a3d" stroke="#6fb6ff" stroke-width="3"/>
<rect x="250" y="112" width="260" height="34" rx="16" fill="#26364d"/><rect x="250" y="130" width="260" height="16" fill="#26364d"/>
<circle cx="272" cy="129" r="6" fill="#ff5f57"/><circle cx="292" cy="129" r="6" fill="#febc2e"/><circle cx="312" cy="129" r="6" fill="#28c840"/>
<rect x="340" y="164" width="80" height="80" rx="20" fill="#2f7bf5"/>
<g fill="#fff"><circle cx="358" cy="186" r="5"/><circle cx="402" cy="186" r="5"/><circle cx="380" cy="204" r="5"/><circle cx="360" cy="226" r="5"/><circle cx="400" cy="226" r="5"/></g>
<g fill="none" stroke="#fff" stroke-width="2" opacity=".8"><path d="M358 186L380 204L402 186M380 204L360 226M380 204L400 226M360 226H400M358 186H402M358 186L360 226M402 186L400 226"/></g>
<text x="380" y="280" text-anchor="middle" font-family="system-ui,sans-serif" font-size="22" font-weight="700" fill="#e8f2ff">Agent! 1.1.87</text>
<rect x="40" y="150" width="190" height="150" rx="12" fill="#121c2a" stroke="#f08a4b" stroke-width="3"/>
<text x="56" y="178" font-family="ui-monospace,monospace" font-size="15" fill="#f08a4b">$ agentiloop</text>
<g fill="#f08a4b" stroke="#0f1724" stroke-width="2"><ellipse cx="135" cy="236" rx="34" ry="22"/><circle cx="92" cy="214" r="10"/><circle cx="178" cy="214" r="10"/></g>
<g stroke="#f08a4b" stroke-width="4" stroke-linecap="round"><path d="M110 256l-10 14M122 258l-6 14M148 258l6 14M160 256l10 14M100 222l8 6M170 222l-8 6"/></g>
<circle cx="124" cy="230" r="4" fill="#0f1724"/><circle cx="146" cy="230" r="4" fill="#0f1724"/>
<text x="135" y="292" text-anchor="middle" font-family="system-ui,sans-serif" font-size="17" font-weight="700" fill="#ffd2b5">Rust 0.0.5</text>
<rect x="530" y="150" width="190" height="150" rx="12" fill="#121c2a" stroke="#4fd1e8" stroke-width="3"/>
<text x="546" y="178" font-family="ui-monospace,monospace" font-size="15" fill="#4fd1e8">$ agentiloop</text>
<g stroke="#0f1724" stroke-width="2"><ellipse cx="625" cy="236" rx="30" ry="36" fill="#4fd1e8"/><circle cx="600" cy="204" r="7" fill="#4fd1e8"/><circle cx="650" cy="204" r="7" fill="#4fd1e8"/></g>
<circle cx="612" cy="222" r="9" fill="#fff"/><circle cx="638" cy="222" r="9" fill="#fff"/><circle cx="612" cy="222" r="4" fill="#0f1724"/><circle cx="638" cy="222" r="4" fill="#0f1724"/>
<text x="625" y="292" text-anchor="middle" font-family="system-ui,sans-serif" font-size="17" font-weight="700" fill="#c8f4fb">Go 0.0.5</text>
<text x="380" y="345" text-anchor="middle" font-family="system-ui,sans-serif" font-size="18" fill="#9fb6d4">1 つのループ。3 通りの動かし方。</text>
</svg>
<figcaption>10 月 1 日の AgentiLoop ファミリー：Mac 版 Agent! と、Rust 版・Go 版のコマンドラインエディション。</figcaption>
</figure>

今日、ファミリー全員が一斉にリリースされます。**Agent! 1.1.87** は Mac アプリの新しいリリースで、**AgentiLoop CLI 0.0.5** は [Rust](https://github.com/AgentiLoop/AgentiLoopCLI/releases/tag/v0.0.5) 版と [Go](https://github.com/AgentiLoop/AgentiLoopGo/releases/tag/v0.0.5) 版の両方で公開されました。プレリリースではなく正式リリースであり、3 つすべてにとってこれまでで最大の一歩です。

git の履歴から直接拾った新機能を紹介します。

## Mac 版 Agent! 1.1.87

Mac アプリの前回の正式リリースは、9 月 12 日の 1.1.33 でした。それ以来さまざまなことがあり、1.1.87 には 449 件のコミットが入っています。主なハイライトは次のとおりです。

### 🤖 オートパイロット：`/auto <goal>`

今回の目玉機能です。Agent! に目標を与えると、`/auto` が時間予算の範囲内で、無人のサイクルを連続して実行します。各サイクルは目標に向けて作業し、現在の状況を確認して、さらに進みます。

- サイクル数や反復回数の上限はありません。LLM タブで動作し、目標の履歴を保持するので、`/auto last` や `/auto #N` で以前の目標を呼び戻せます。
- セッションはアプリを再起動しても残り、同じタブで再開されます。
- **Esc** は現在のサイクルだけを止めます。**Stop All**（または `/auto stop all`）はセッション全体を終了します。

これは、人間があえて一歩引いたエージェントループです。あなたが目的地と予算を決め、運転するのは Agent! です。

### 🔌 6 つの新プロバイダと、いじる設定の削減

1.1.87 の新顔：**Sidrune AI**（OpenAI と Anthropic のプロトコルオプション付き）、**Muse Code**（`muse login` のサブスクリプションを再利用）、**Requesty**、**A2Agent**、**OrcaRouter**、そして Coding Plan 上の **Qwen Code**。さらに、ローカルの Chat Completions API 経由で Apple Foundation Models を公開する実験的な **fm serve** プロバイダもあります。

ビジョン対応は各プロバイダのカタログのメタデータから検出されるようになったため、Force Vision のトグルはもう不要です。内部的には、すべてのプロバイダが十数本の別々のコードパスではなく、1 つのレジストリ `APIProvider` に集約されました。

### 🧐 言いくるめられないクリティック

Agent! にはクリティックゲートがあります。タスクが完了扱いになる前に、2 つ目のモデルが変更をレビューします。1.1.87 ではこのレビューが**強制**されます。変更のない diff は拒否され、変更された diff は再レビューされ、問題を「スコープ外」として片付けることはできません。クリティックは Codex と Apple Intelligence でも動作するようになり、ログにはどんな問題を見つけたか、その後コードが変更されたかどうかが表示されます。

あわせて登場したのが **Jev** です。ツールループに助言する TypeSafe System One の意思決定レイヤーで、設定は新しい LLM 共通設定（LLM Common Settings）にあります。

### 🧠 よりスマートなコンテキスト

コンパクションを入念に見直しました。しきい値は*実際に使用中の*モデル（タブのモデルまたはフォールバック）に基づいて決まるようになり、取得した Ollama のコンテキストウィンドウも記憶されます。これにより、一部のモデルが 16K でコンパクションされてしまうバグが修正されました。保持される末尾部分とマイクロコンパクトはメッセージ数ではなくトークン数で制限され、大きすぎるブロックが最初に切り詰められ、コンテキストのオーバーフローや `max_tokens` エラーはすべてのプロバイダで同じ方法で検出されます。

### 🖥️ より多くの Mac、より多くの言語

- **macOS 14.6 Sonoma 以降**、Apple Silicon と Intel に対応。Apple Intelligence（Foundation Models）の機能には macOS 26 が必要です。
- アプリはスペイン語、フランス語、ドイツ語、中国語（簡体字）、ロシア語、韓国語、日本語にローカライズされました。
- 新しいアクセシビリティアクション：`wait_until_actionable`、`select_text_range`、`observe_start/poll/stop/list`。
- Homebrew でインストール：`brew update && brew install --cask agentiloop-agent`。

### 🔒 デフォルトでより安全に

現在のプロジェクトフォルダの再帰的な削除はブロックされるようになりました。アプリ全体のバグハントで、ShellSafety の `&` による読み取り専用の回避、Ollama のストリーミング停止、いくつかのクラッシュが修正されました。要約が一度も書き込まれていない出力を指している場合は `task_complete` が拒否され、メモリ不足になったローカルモデルは空回りせず、明確な理由とともに即座に停止します。

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 330" role="img" aria-labelledby="box-title box-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="box-title">CLI のための、より大きなツールボックス</title>
<desc id="box-desc">0.0.5 と書かれた、開いた赤いツールボックス。ラベル付きのタグを付けたツールがそこから飛び出しています。虫眼鏡付きの glob と grep、地球儀付きの web_fetch、チェックリスト付きの todo_write、曲がった矢印付きの /undo、ドキュメント付きの AGENTS.md、波かっこ付きの --json。</desc>
<rect width="760" height="330" rx="20" fill="#fff6ea"/>
<path d="M60 296H700" stroke="#c9a77f" stroke-width="10" stroke-linecap="round"/>
<path d="M240 178L270 140H490L520 178Z" fill="#b8323a" stroke="#5a1418" stroke-width="4" stroke-linejoin="round"/>
<rect x="240" y="178" width="280" height="112" rx="10" fill="#d9444d" stroke="#5a1418" stroke-width="4"/>
<path d="M340 140V120Q340 108 352 108H408Q420 108 420 120V140" fill="none" stroke="#5a1418" stroke-width="8"/>
<rect x="340" y="214" width="80" height="40" rx="8" fill="#fff" stroke="#5a1418" stroke-width="3"/>
<text x="380" y="241" text-anchor="middle" font-family="ui-monospace,monospace" font-size="20" font-weight="700" fill="#5a1418">0.0.5</text>
<g font-family="ui-monospace,monospace" font-size="17" font-weight="700" text-anchor="middle">
<g><rect x="60" y="40" width="150" height="44" rx="12" fill="#d7eaff" stroke="#3377b9" stroke-width="3"/><text x="135" y="68" fill="#173452">glob · grep</text><circle cx="232" cy="102" r="16" fill="none" stroke="#3377b9" stroke-width="5"/><path d="M244 114l14 14" stroke="#3377b9" stroke-width="6" stroke-linecap="round"/></g>
<g><rect x="60" y="120" width="140" height="44" rx="12" fill="#d9f5e4" stroke="#2f8f5b" stroke-width="3"/><text x="130" y="148" fill="#14432a">web_fetch</text><circle cx="222" cy="186" r="16" fill="#bfe9cf" stroke="#2f8f5b" stroke-width="3"/><path d="M206 186H238M222 170Q212 186 222 202Q232 186 222 170" fill="none" stroke="#2f8f5b" stroke-width="2.5"/></g>
<g><rect x="295" y="20" width="170" height="44" rx="12" fill="#fce9b6" stroke="#9a701b" stroke-width="3"/><text x="380" y="48" fill="#4a3608">todo_write</text><path d="M362 76l6 6 10-12M362 94l6 6 10-12" fill="none" stroke="#9a701b" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><path d="M386 78H404M386 96H404" stroke="#9a701b" stroke-width="4" stroke-linecap="round"/></g>
<g><rect x="560" y="40" width="140" height="44" rx="12" fill="#efe1ff" stroke="#7a4bb8" stroke-width="3"/><text x="630" y="68" fill="#341a5a">/undo</text><path d="M548 128Q520 128 520 104Q520 84 546 84" fill="none" stroke="#7a4bb8" stroke-width="5" stroke-linecap="round"/><path d="M538 74l12 10-12 10" fill="none" stroke="#7a4bb8" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></g>
<g><rect x="560" y="120" width="140" height="44" rx="12" fill="#ffe0e6" stroke="#b83a5a" stroke-width="3"/><text x="630" y="148" fill="#5a1426">AGENTS.md</text><path d="M528 172h20l8 8v26h-28z" fill="#fff" stroke="#b83a5a" stroke-width="3" stroke-linejoin="round"/></g>
<g><rect x="560" y="210" width="140" height="44" rx="12" fill="#e2e8f0" stroke="#4b617e" stroke-width="3"/><text x="630" y="238" fill="#173452">--json { }</text></g>
</g>
</svg>
<figcaption>AgentiLoop CLI 0.0.5：同じループに、ずっと多くの中身を。</figcaption>
</figure>

## AgentiLoop CLI 0.0.5：より大きなツールボックス

私たちが[エージェントループをターミナルに持ち込んだ](/blog/the-terminal-strikes-back/)とき、CLI は read、list、write、edit、bash という 5 つの鋭いツールから始まりました。バージョン 0.0.4 では、きれいに止まることを覚えました。バージョン 0.0.5 は、扱えるものを増やすためのリリースです。すべての機能はまず Rust 版に入り、コミット単位でそのまま Go 版にミラーされたため、両エディションの機能はまったく同じです。

### 新しいツール

| ツール | 機能 | 事前に確認？ |
|---|---|---|
| `glob` | パターンでファイルを検索する | いいえ |
| `grep` | 0〜5 行のコンテキスト付きでファイルの内容を検索する | いいえ |
| `web_fetch` | http(s) のページをサイズ上限付きでテキストとして取得する | **はい** |
| `todo_write` | 複数ステップの作業用にチェックリストを管理する（`/todos` で確認） | いいえ |

`glob` と `grep` は `.git`、`node_modules`、`target`、バイナリファイルをスキップし、ネストしたファイル、否定、アンカー、ディレクトリ限定のルールを含め `.gitignore` に従います。そのため、シェルで `find` を呼び出すより速く、ツリー全体をコンテキストに流し込むより安全です。

### プロジェクトの指示を読み込みます

リポジトリに **`AGENTS.md`** または **`CLAUDE.md`** があれば、CLI はそれをシステムプロンプトに読み込みます。あわせて、個人のデフォルト設定用に `~/.agentiloop` にあるものも読み込みます。`@docs/style.md` のような行は他のファイルをインポートします（ネスト可能、循環にも安全）。まだファイルがない？ **`/init`** が、検出したビルドコマンドとテストコマンドを含むスターター `AGENTS.md` を書き出します。

### 元に戻す、diff、その仲間たち

- **`/undo`**：`write_file`、`edit_file`、`apply_patch` による変更はすべてプロンプトごとに記録されるため、エージェントの直前のターンを巻き戻せます。
- **`/diff`** は作業ツリーの git ステータスと diff を表示します。
- **`/export`** は会話を Markdown として保存します。
- **`/usage`** は起動以降のトークン合計と、コンテキストがどれだけ埋まっているかを表示します。

### 自分好みにカスタマイズ

- **カスタムスラッシュコマンド**：`.agentiloop/commands/` に Markdown ファイルを置きます。たとえば `Review $1 for bugs` と書いた `review.md` を置けば、`/review main.rs` でそれが実行されます。`$ARGUMENTS` と `$1`..`$9` に対応し、`/commands` で一覧を表示できます。
- サーバーからの **MCP プロンプト**は `/mcp__<server>__<prompt>` コマンドとして表示されます。

### スクリプトと CI のために

- **`--json`** はワンショットの回答を 1 つの JSON オブジェクトとして出力します：result、is_error、session_id、provider、model、usage。
- **`--allow-tool` / `--deny-tool`** はツール名または `mcp_*` プレフィックスで権限ルールを設定します。拒否は常に優先され、`--yes` よりも優先されます。
- **`--append-system-prompt`** は 1 回の実行に限り、システムプロンプトにテキストを追加します。
- **パイプがそのまま使えます**：プロンプト内の単独の `-` は stdin に置き換えられるので、`git diff | agentiloop "review this" -` は書いてあるとおりに動きます。

これらを組み合わせると、プルリクエストをレビューし、シェルには触れず、機械可読な出力を返す CI ステップになります。

```
git diff origin/main | agentiloop --deny-tool bash --json "review this diff" -
```

## なぜ一緒にリリースするのか？

それらは同じアイデアの 3 つの形だからです。Mac 版 Agent! はフラッグシップで、あなたのアプリ、Xcode のビルド、デスクトップ全体を操作します。CLI は同じループを macOS・Windows・Linux のあらゆるターミナルに届けます。CLI の Esc によるキャンセルと、Stop All ボタンを備えた Mac アプリのオートパイロットは、同じ問いに両側から答えています。*自律的に回るループを、人はどうやって掌握し続けるのか？*

それこそが、私たちが最も大切にしている部分です。かわいいアバターでも、ベンチマークの大きな数字でもなく、ループの中にいる人間です。あなたが目標を決め、すべてのステップを見て、止めることができます。CLI では、`/undo` でエージェントの直前のファイル編集を元に戻すこともできます。Auto-Pilot には元に戻す機能がないため、git で管理しているプロジェクトで実行してください。

## 入手方法

- **Mac 版 Agent! 1.1.87**：[GitHub からダウンロード](https://github.com/AgentiLoop/Agent/releases/tag/v1.1.87.287)、または `brew update && brew install --cask agentiloop-agent`。macOS 14.6 以降、Apple Silicon または Intel。
- **AgentiLoop CLI 0.0.5 (Rust)**：[GitHub のリリース](https://github.com/AgentiLoop/AgentiLoopCLI/releases/tag/v0.0.5)。
- **AgentiLoopGo 0.0.5 (Go)**：[GitHub のリリース](https://github.com/AgentiLoop/AgentiLoopGo/releases/tag/v0.0.5)。

macOS 版の CLI バイナリは署名と公証が済んでいます。展開して `agentiloop` を PATH に置き、実行するだけ。あとはセットアップウィザードが案内します。

テスターは大歓迎です。大きな編集のあとに `/undo` を試したり、`AGENTS.md` のあるリポジトリを指定したり、`--json` をスクリプトに組み込んだりして、何が壊れたか教えてください。OS、プロバイダ、モデルを添えていただき、API キーは決して含めないでください。
