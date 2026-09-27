---
title: Agent! が macOS 14.6 と Intel Mac で動作するように：macOS 26 依存からの脱却
description: Agent! は macOS 26 の Apple Intelligence を前提に構築されていました。1日がかりの #available ゲートとパッケージの更新で、Apple Silicon と Intel の macOS 14.6 に対応させた方法を紹介します。
tags: リリースノート, エンジニアリング
---
これまで Agent! には macOS 26 が必要でした。本日のプレリリースから、**macOS 14.6 以降の Apple Silicon と Intel の両方**で動作するようになりました。これにより、これまで対象外だったものの十分に現役で使える多くの Mac がカバーされます。その多くは Apple Intelligence をまったく実行できないマシンです。

ここでは、1日で行った作業をコミットごとに紹介します。

## 障壁：FoundationModels

Agent! は **FoundationModels** フレームワークを通じて Apple のオンデバイスモデルを利用していますが、このフレームワークは macOS 26 にしか存在しません。メインの頭脳ではなく、その役割はユーザーが選んだプロバイダーが担います。それでも、コンテキスト圧縮時の高速な要約、オンデバイスでのトークンカウント、起動時にプリウォームされるセッション、一部のトリアージなど、いくつかの役割を担っています。

macOS 26 の型を参照するコードは、それより古いデプロイメントターゲット向けにはビルドできません。そこで最初のステップ（`ea5ce624`）として、FoundationModels の**すべて**の利用箇所を `#available(macOS 26, *)` の内側に移しました。対象は `FoundationModelService`、`AppleIntelligenceMediator`、`AgentApp` 内のプリウォーム、`Compression.swift` 内の圧縮用要約とトークンカウント、そして `AboutSelf` です。

## 工夫：保存プロパティの型消去

`#available` はコードパスには使えますが、保存プロパティには使えません。実行中の OS に `LanguageModelSession?` という型が存在しない場合、クラスはその型のプロパティを保持できません。解決策は、`AnyObject?` として保存し、使用する箇所のゲートされたコード内でキャストし直すことです。

```swift
/// Type-erased `LanguageModelSession` so the stored property compiles below macOS 26.
private(set) var session: AnyObject?

@available(macOS 26.0, *)
var transcript: Transcript? {
    (session as? LanguageModelSession)?.transcript
}
```

コミットメッセージにあるとおり、保存プロパティが「フレームワークの型をクラスのレイアウトに引きずり込む」ことはなくなりました。

可用性チェックも、古いシステムに対して正直な答えを返すようになりました。

```swift
static var unavailabilityReason: String {
    guard #available(macOS 26.0, *) else { return "Apple Intelligence requires macOS 26 or later." }
    ...
}
```

そのため macOS 14 や 15 では、Apple Intelligence は明確な理由とともに利用不可と表示されるだけで、それ以外はすべて動作します。macOS 26 では何も変わりません。

## 地道な作業：10個のパッケージ

Agent! は独自の Swift パッケージ群で構成されており、それぞれが独自に最小 OS バージョンを宣言していました。コミット `4d7fca86` で、10個すべてを `.macOS(.v14)` を宣言するリリースに更新しました。

| パッケージ | バージョン |
|---|---|
| AgentAccess | 2.10.24 |
| AgentAudit | 1.3.9 |
| AgentColorSyntax | 1.2.8 |
| AgentD1F | 1.0.15 |
| AgentEventBridges | 1.1.8 |
| AgentLLM | 1.0.8 |
| AgentMCP | 1.6.10 |
| AgentSwift | 1.1.11 |
| AgentTerminalNeo | 1.37.9 |
| AgentTools | 2.53.19 |

すべての依存関係を自分たちで管理していることが、こういう日に報われます。上流のメンテナーを待つ必要はなく、タグを10個打つだけで済みました。

## 想定外：26.4

ある API は、26.0 のゲートだけでは不十分でした。`SystemLanguageModel.tokenCount(for:)` は **macOS 26.4** 以降にしか存在しないため、その可用性チェックを 26.0 から 26.4 に変更しました。これがなければ、26.0 から 26.3 の Mac がまだ存在しないメソッドを呼び出そうとしていたはずです。「フレームワークが利用可能か」と「このメソッドが利用可能か」は別の問題だということを改めて思い出させてくれる出来事でした。

## 古い Mac で使える機能

macOS 14.6 と 15 では、Apple Silicon でも Intel でも、Agent! は同じように動作します。

- 23のクラウドおよびローカル LLM プロバイダーすべて
- 完全なツールループ：コーディング、Xcode ビルド、git、ユーザー権限または root 権限でのシェル、Accessibility、AppleScript、JXA、AgentScript、Safari の自動化、MCP
- コンテキスト圧縮。モデル自身の要約とプロバイダーのトークンカウントを使用します（Apple Intelligence の層がないだけです）

macOS 26 が必要なのは、オンデバイスの Apple Intelligence 機能だけです。

## 入手方法

すべてのリリースとプレリリースで、署名、公証、ステープル済みのバイナリを提供しています。ソースからビルドする必要はまったくありません。

```sh
brew update && brew install --cask agentiloop-agent
```

または、[GitHub Releases](https://github.com/AgentiLoop/Agent/releases) から `.dmg` をダウンロードしてください。古い MacBook や Intel Mac mini で使える日を待っていたなら、今日がその日です。
