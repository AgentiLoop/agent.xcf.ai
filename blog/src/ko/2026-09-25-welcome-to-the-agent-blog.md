---
title: Agent! 블로그에 오신 것을 환영합니다: 하나의 앱, 어떤 AI든, Mac을 완벽하게 제어
description: AgentiLoop Agent!가 무엇인지, 어떻게 만들어졌는지, 그리고 이 데일리 블로그에서 무엇을 다룰지 소스 코드를 바탕으로 직접 소개합니다.
tags: 공지, 아키텍처
---
이곳은 네이티브 macOS AI 에이전트인 **AgentiLoop Agent!** 의 공식 블로그입니다. 계획은 간단합니다. 하루에 한 편씩, 주로 저희가 가장 잘 아는 것, 즉 코드베이스 자체를 바탕으로 글을 씁니다. 에이전트 루프가 어떻게 동작하는지, 특정 가드레일이 왜 그런 형태를 갖게 되었는지, 최신 릴리스 후보에서 무엇이 바뀌었는지를 깊이 파고들고, 가끔은 더 넓은 AI 에이전트 생태계도 살펴볼 예정입니다.

처음 오셨다면 이 첫 글이 지도가 되어 드릴 것입니다.

## Agent!란 무엇인가

Agent!는 100% 네이티브 Swift / SwiftUI 앱입니다. 원하는 작업을 입력하거나 말하기만 하면, 방법을 설명하는 데 그치지 않고 Mac에서 직접 작업을 수행합니다.

- **실제로 코드를 작성합니다.** 프로젝트를 읽고, 문자열 치환 방식의 diff로 파일을 편집하고, Xcode에서 빌드하고, 오류를 읽고 수정한 뒤 git으로 커밋합니다.
- **어떤 Mac 앱이든 조작합니다.** Accessibility API는 물론 AppleScript, JXA, 그리고 51개의 ScriptingBridge 앱 브리지를 활용합니다.
- **사용자 권한 또는 root 권한으로 셸 명령을 실행합니다.** SMAppService로 등록되고 XPC로 연결되는 Launch Agent와 Launch Daemon을 통해서입니다.
- **23개의 LLM 제공업체와 연동됩니다.** 온디바이스 Apple Intelligence도 지원하며, Claude, Codex, OpenAI, Gemini, Grok, Mistral, DeepSeek, Qwen, Z.ai, OpenRouter, Ollama, vLLM, LM Studio 등을 사용할 수 있습니다.
- **귀 기울여 듣습니다.** *"Agent!"* 라고 부른 뒤 작업을 말하거나, iPhone에서 iMessage로 메시지를 보내면 됩니다(승인된 발신자만 가능).

README는 이를 한 줄로 요약합니다. *Siri는 대답하고, Agent!는 행동합니다.*

## NPM도, Electron도 없다

사람들이 가장 놀라는 부분은 Agent!에 *포함되지 않은* 것들입니다. Electron 셸도, Node 런타임도, `node_modules`도 없습니다. 의존하는 모든 Swift 패키지는 같은 개발자가 직접 작성했으며, 각각 [AgentiLoop](https://github.com/AgentiLoop) 조직 아래 별도의 저장소에 있습니다.

| 패키지 | 역할 |
|---|---|
| AgentTools | 도구 스키마, 시스템 프롬프트, 제공업체 관리 |
| AgentLLM | LLM 제공업체 프로토콜, 타입, 레지스트리 |
| AgentMCP | MCP 클라이언트(stdio 및 HTTP) |
| AgentAccess | 손쉬운 사용(Accessibility) 자동화 |
| AgentEventBridges | 50개 이상의 Mac 앱을 위한 ScriptingBridge 프로토콜 |
| AgentD1F | 여러 줄 diff 엔진 |
| AgentSwift | SwiftSyntax 기반 코드 분석 |
| AgentColorSyntax · AgentTerminalNeo | 구문 강조 · 레트로 터미널 마크다운 |
| AgentAudit | `os.log` 감사 로깅 |

그 결과 RAM을 아주 적게 사용하면서도 Xcode 자동화, Swift 구문 분석, 손쉬운 사용, AppleScript, Safari 자동화, MCP를 기본으로 갖춘 앱이 탄생했습니다.

## 모든 것의 중심에 있는 루프

모든 것은 하나의 아이디어, 즉 **스스로 검증하는 작업 루프** 에서 출발합니다. 모델이 추론하고, 도구를 호출하고, 실제 결과를 확인한 뒤 스스로 바로잡습니다. 몇 가지 규칙이 이 루프를 신뢰할 수 있게 만듭니다.

- **도구 사용은 위장할 수 없습니다.** 모든 호출은 단일 디스패처를 거쳐 실제 출력을 반환합니다. 모델이 도구 호출 없이 *"클릭했습니다"* 라고 주장하면 Agent!가 교정 메시지를 삽입합니다.
- **"완료"에는 증거가 필요합니다.** 작업은 `goal_state` 기준이 빌드 성공이나 테스트 통과 같은 증거와 함께 완료로 표시되기 전까지 스스로 완료를 선언할 수 없습니다.
- **편집하기 전에 먼저 읽어야 합니다.** 모델이 읽지 않은 파일이나, 읽은 뒤 디스크에서 변경된 파일(SHA-256으로 확인)에 대한 편집은 거부됩니다. 거부될 때 파일을 모델 대신 읽어 주므로 다음 시도는 최신 내용을 바탕으로 이루어집니다.
- **모든 것은 되돌릴 수 있습니다.** 모든 편집은 일주일 동안 스냅숏으로 보관됩니다. 파일 하나만 롤백할 수도 있고, `rewind_task`로 작업 전체를 되감을 수도 있습니다.

이 규칙들은 앞으로의 글에서 하나씩 자세히 뜯어볼 예정입니다.

## AgentScript: 모든 권한을 갖춘 Swift

가장 독특한 구성 요소 중 하나는 **AgentScript** 입니다. 스크립트는 평범한 Swift 파일입니다. Agent!는 각 스크립트를 SwiftPM으로 `.dylib`로 컴파일한 뒤 `dlopen`으로 프로세스 안에 로드합니다. 그래서 스크립트는 Agent! 자체의 macOS 권한, 즉 손쉬운 사용, 자동화, 캘린더, 연락처, 메일, 사진 등을 그대로 물려받습니다. 스크립트를 작성하는 데는 진입점 하나면 충분합니다.

```swift
import Foundation
import CalendarBridge   // any `import XBridge` auto-wires, no Package.swift edits

@_cdecl("script_main")
public func scriptMain() -> Int32 {
    print("Hello from AgentScript! 👋")
    return 0
}
```

스크립트가 출력하는 내용은 모두 모델에게 전달되고, 반환값은 종료 상태가 됩니다. 앱에는 `TodayEvents`, `NowPlaying`, `CheckMail`, `CreateDmg` 등 약 35개의 예제가 함께 제공됩니다.

## 직접 읽어 볼 수 있는 안전성

Agent!는 root 권한으로 실행될 수 있으므로, 안전성은 발표 자료 속 슬라이드 한 장이 아닙니다. GitHub에서 직접 열어 볼 수 있는 코드입니다. 하드코딩된 `ShellSafetyService`가 치명적인 명령을 전달되기 전에 거부하고, 권한을 가진 데몬도 자기 쪽에서 같은 검사를 다시 수행합니다. 선택 사항인 두 번째 의견 **Jev** 는 명령이 데이터를 파괴할 가능성을 평가합니다. 이것이 정확히 어떻게 동작하는지는 [첫 번째 심층 분석](/blog/inside-agent-shell-guardrails/)에서 다룹니다.

## 계속 늘어나는 가족

같은 에이전트 루프가 이제 macOS, Windows, Linux의 터미널에서도 동작합니다. 동일한 기능을 갖춘 두 개의 CLI, Rust로 작성된 [AgentiLoopCLI](https://github.com/AgentiLoop/AgentiLoopCLI)와 Go로 작성된 [AgentiLoopGo](https://github.com/AgentiLoop/AgentiLoopGo)입니다. README에 실린 재미있는 사실 하나: 이 작은 동생들은 Mac용 Agent!가 직접 작성했습니다.

## 앞으로 다룰 내용

- **내부 구조:** 에이전트 루프, 컨텍스트 압축, 도구 디스패치, 하위 에이전트, 메모리와 플랜.
- **보안:** 가드레일, XPC 신뢰 모델, 그리고 최근의 에이전트 사고가 개발자에게 주는 교훈.
- **이유까지 담은 릴리스 노트:** 빌드마다 무엇이 바뀌었는지, 그리고 그 원인이 된 버그.
- **사용 가이드:** AgentScript 레시피, 예산에 맞는 제공업체 고르기, 완전한 로컬 실행.
- **더 넓은 에이전트 세계:** 뉴스와 리뷰를 다루되, 항상 여러분의 Mac에 어떤 의미가 있는지와 연결합니다.

Agent!는 macOS 14.6 이상, Apple Silicon과 Intel에서 실행되며 개인 용도로는 무료입니다. 아래에서 내려받으시고, 내일 다시 찾아 주세요.
