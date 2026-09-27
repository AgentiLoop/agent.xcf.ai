---
title: Agent!, 이제 macOS 14.6과 Intel Mac에서 실행: macOS 26에서 벗어난 방법
description: Agent!는 macOS 26의 Apple Intelligence를 중심으로 만들어졌습니다. 하루 동안의 #available 게이트와 패키지 버전 업으로 Apple Silicon과 Intel의 macOS 14.6까지 지원하게 된 과정을 소개합니다.
tags: 릴리스 노트, 엔지니어링
---
오늘까지 Agent!는 macOS 26이 필요했습니다. 오늘의 프리릴리스부터는 **macOS 14.6 이상, Apple Silicon과 Intel** 에서 실행됩니다. 그동안 소외되었던 멀쩡한 Mac들이 대거 포함되며, 그중 상당수는 Apple Intelligence를 아예 실행할 수 없는 기기입니다.

하루 동안 커밋 단위로 무엇이 필요했는지 살펴보겠습니다.

## 걸림돌: FoundationModels

Agent!는 macOS 26에만 존재하는 **FoundationModels** 프레임워크를 통해 Apple의 온디바이스 모델을 사용합니다. 이 모델이 핵심 두뇌는 아닙니다. 그 역할은 사용자가 선택한 제공자가 맡습니다. 하지만 여러 가지 일을 담당합니다. 컨텍스트 압축 중의 빠른 요약, 온디바이스 토큰 계산, 실행 시 미리 준비해 두는 세션, 그리고 일부 분류 작업입니다.

macOS 26의 타입을 참조하는 코드는 더 낮은 배포 대상으로 빌드되지 않습니다. 그래서 첫 단계(`ea5ce624`)는 FoundationModels의 **모든** 사용처를 `#available(macOS 26, *)` 뒤에 두는 것이었습니다. 여기에는 `FoundationModelService`, `AppleIntelligenceMediator`, `AgentApp`의 사전 준비 로직, `Compression.swift`의 압축 요약과 토큰 계산, 그리고 `AboutSelf`가 포함되었습니다.

## 요령: 저장 프로퍼티의 타입 소거

`#available`은 코드 경로에는 통하지만 저장 프로퍼티에는 통하지 않습니다. 실행 중인 OS에 해당 타입이 없으면 클래스는 `LanguageModelSession?`을 보유할 수 없습니다. 해결책은 이를 `AnyObject?`로 저장하고, 사용하는 곳에서 게이트된 코드 안에서 다시 캐스팅하는 것입니다.

```swift
/// Type-erased `LanguageModelSession` so the stored property compiles below macOS 26.
private(set) var session: AnyObject?

@available(macOS 26.0, *)
var transcript: Transcript? {
    (session as? LanguageModelSession)?.transcript
}
```

커밋 메시지의 표현대로, 저장 프로퍼티는 더 이상 "프레임워크 타입을 클래스 레이아웃 안으로 끌어들이지" 않습니다.

가용성 검사도 이전 시스템에 대해 솔직한 답을 내놓게 되었습니다.

```swift
static var unavailabilityReason: String {
    guard #available(macOS 26.0, *) else { return "Apple Intelligence requires macOS 26 or later." }
    ...
}
```

따라서 macOS 14나 15에서는 Apple Intelligence가 명확한 이유와 함께 사용 불가로 표시될 뿐, 나머지는 모두 정상 동작합니다. macOS 26에서는 아무것도 달라지지 않습니다.

## 긴 꼬리: 10개의 패키지

Agent!는 자체 Swift 패키지들로 구성되어 있고, 각 패키지가 저마다 최소 OS 버전을 선언하고 있었습니다. 커밋 `4d7fca86`은 10개 패키지 모두를 `.macOS(.v14)`를 선언하는 릴리스로 올렸습니다.

| 패키지 | 버전 |
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

모든 의존성을 직접 소유한 덕을 이런 날에 봅니다. 업스트림 메인테이너를 기다릴 필요 없이, 태그 10개면 충분했습니다.

## 뜻밖의 복병: 26.4

한 API는 26.0 게이트만으로는 부족했습니다. `SystemLanguageModel.tokenCount(for:)`는 **macOS 26.4** 부터 존재하기 때문에, 이 API의 가용성 검사를 26.0에서 26.4로 옮겼습니다. 그러지 않았다면 26.0부터 26.3까지의 Mac은 아직 존재하지 않는 메서드를 호출하려 했을 것입니다. "프레임워크를 사용할 수 있다"와 "이 메서드를 사용할 수 있다"는 서로 다른 질문이라는 좋은 교훈입니다.

## 이전 Mac에서 얻을 수 있는 것

macOS 14.6과 15의 Apple Silicon 또는 Intel Mac에서도 Agent!는 동일하게 동작합니다.

- 23개의 클라우드 및 로컬 LLM 제공자 전부
- 전체 도구 루프: 코딩, Xcode 빌드, git, 사용자 권한 또는 root 권한의 셸, Accessibility, AppleScript, JXA, AgentScript, Safari 자동화, MCP
- 모델 자체의 요약과 제공자의 토큰 수를 사용하는 컨텍스트 압축(Apple Intelligence 계층만 빠짐)

macOS 26이 필요한 것은 온디바이스 Apple Intelligence 기능뿐입니다.

## 설치하기

모든 릴리스와 프리릴리스는 서명, 공증, 스테이플링을 마친 바이너리로 배포됩니다. 소스에서 직접 빌드할 필요가 전혀 없습니다.

```sh
brew update && brew install --cask agentiloop-agent
```

또는 [GitHub Releases](https://github.com/AgentiLoop/Agent/releases)에서 `.dmg`를 내려받으세요. 오래된 MacBook이나 Intel Mac mini에서 기다려 오셨다면, 바로 오늘입니다.
