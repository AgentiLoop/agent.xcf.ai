---
title: Agent! 블로그에 오신 것을 환영합니다: 하나의 앱, 어떤 AI든, Mac을 완벽하게 제어
description: AgentiLoop Agent!가 무엇인지, 왜 이런 방식으로 만들었는지, 그리고 이곳에서 무엇을 만나게 될지, 소스 코드에서 바로 꺼내 이야기합니다.
tags: 공지, 아키텍처
---
<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 340" role="img" aria-labelledby="map-title map-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="map-title">작은 Mac이 지도를 건네줍니다</title>
<desc id="map-desc">웃고 있는 Mac이 책상 위에 서서 펼친 지도를 들고 있습니다. 지도에는 점선으로 이어진 네 개의 지점이 있습니다: 모든 AI, 루프, AgentScript, 안전.</desc>
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
<text x="350" y="152" font-size="15" font-weight="700">모든 AI</text>
<text x="440" y="117" font-size="15" font-weight="700">루프</text>
<text x="520" y="222" font-size="15" font-weight="700">AgentScript</text>
<text x="580" y="90" font-size="15" font-weight="700">안전</text>
<text x="345" y="88" font-size="14" fill="#8b684c">여러분의 지도</text>
<text x="140" y="322" font-size="18">Mac용 Agent!</text>
</g>
</svg>
<figcaption>블로그에는 첫 글이 있어야 하죠. 이 글이 바로 지도입니다.</figcaption>
</figure>

안녕하세요, Todd입니다. 네이티브 macOS AI 에이전트인 **AgentiLoop Agent!** 를 만들고 있고, 여기는 그 블로그예요.

README나 릴리스 노트에는 담기지 않는 Agent!의 이야기들을 풀어놓을 곳이 필요했습니다. 가드레일이 왜 하필 그런 모양인지. 에이전트 루프가 왜 자기 작업을 스스로 확인하는지. 릴리스 후보에서 뭐가 망가졌고 어떻게 고쳤는지. 여기서 읽게 될 대부분의 글은 코드베이스에서 곧장 나옵니다. 제가 가장 잘 아는 게 그거니까요. 가끔은 더 넓은 AI 에이전트 세계를 둘러보고, 그게 여러분의 Mac에 어떤 의미인지도 짚어 보려고 합니다.

처음 오셨다면 여기서 시작하세요. 이 글을 지도라고 생각하시면 됩니다.

## Agent!란 무엇인가

Agent!는 100% 네이티브 Swift와 SwiftUI로 만들었습니다. 원하는 걸 입력하거나 말로 하면, 방법을 알려주는 대신 Mac에서 실제로 그 일을 해냅니다.

- **진짜 코드를 씁니다.** 프로젝트를 읽고, 문자열 치환 방식의 diff로 파일을 고치고, Xcode에서 빌드하고, 오류를 읽고 고친 다음 git으로 커밋합니다.
- **어떤 Mac 앱이든 다룹니다.** Accessibility API에 더해 AppleScript, JXA, 그리고 51개의 ScriptingBridge 앱 브리지를 씁니다.
- **셸 명령을 사용자 권한으로도, root 권한으로도 실행합니다.** SMAppService로 등록하고 XPC로 연결하는 Launch Agent와 Launch Daemon을 통해서요.
- **23개의 LLM 제공업체와 함께 동작합니다.** 온디바이스 Apple Intelligence도 물론이고요. Claude, Codex, OpenAI, Gemini, Grok, Mistral, DeepSeek, Qwen, Z.ai, OpenRouter, Ollama, vLLM, LM Studio 등이 있습니다.
- **귀를 기울입니다.** *"Agent!"* 라고 부른 뒤 할 일을 말하거나, iPhone에서 iMessage로 문자를 보내면 됩니다(승인된 발신자만 가능).

README는 이걸 네 마디로 정리합니다. *Siri는 대답하고, Agent!는 행동합니다.*

## NPM도, Electron도 없습니다

사람들이 놀라는 게 바로 이 부분이에요. Electron 셸이 없습니다. Node 런타임도 없습니다. 디스크를 조용히 갉아먹는 `node_modules` 폴더도 없죠. Agent!가 의존하는 Swift 패키지는 전부 제가 직접 작성했고, 각각 [AgentiLoop](https://github.com/AgentiLoop) 조직 아래 자기만의 저장소에 있습니다.

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

그래서 RAM은 아주 조금만 쓰면서도 Xcode 자동화, Swift 구문 분석, 손쉬운 사용, AppleScript, Safari 자동화, MCP를 처음부터 다 갖춘 앱이 됐습니다.

## 한가운데에 있는 루프

Agent!의 모든 것은 하나의 아이디어에 매달려 있습니다. 바로 **스스로 검증하는 작업 루프** 입니다. 모델이 생각하고, 도구를 호출하고, 실제 결과를 보고, 스스로 바로잡습니다. 이게 제대로 굴러가려면 믿을 수 있어야 하니까, 몇 가지 규칙을 아예 박아 두었습니다.

- **도구 호출은 흉내 낼 수 없습니다.** 모든 호출은 하나의 디스패처를 거쳐 실제 출력을 돌려줍니다. 모델이 도구를 실제로 호출하지도 않고 *"클릭했습니다"* 라고 하면, Agent!가 그걸 지적하고 교정 메시지를 보냅니다.
- **"완료"에는 증거가 필요합니다.** 작업은 `goal_state` 기준이 빌드 성공이나 테스트 통과 같은 증거와 함께 체크되기 전까지 스스로 끝났다고 할 수 없습니다.
- **고치기 전에 먼저 읽으세요.** 모델이 읽지 않은 파일, 또는 읽은 뒤 디스크에서 바뀐 파일(SHA-256으로 확인)은 Agent!가 편집을 거부합니다. 거부하면서 최신 파일을 모델에게 건네주기 때문에, 다음 시도에서는 올바른 줄을 쓰게 됩니다.
- **무엇이든 되돌릴 수 있습니다.** 모든 편집은 일주일 동안 스냅숏으로 남습니다. 파일 하나만 롤백하거나, `rewind_task`로 작업 전체를 되감을 수 있어요.

이 규칙들은 앞으로 글 하나하나에서 뜯어볼게요.

## AgentScript: 모든 권한을 가진 Swift

AgentScript는 제가 제일 아끼는 부분 중 하나입니다. 스크립트는 평범한 Swift 파일이에요. Agent!는 각 스크립트를 SwiftPM으로 `.dylib`로 컴파일하고 `dlopen`으로 프로세스 안에 올립니다. 그래서 스크립트는 Agent!가 이미 가진 macOS 권한을 그대로 씁니다. 손쉬운 사용, 자동화, 캘린더, 연락처, 메일, 사진 같은 것들 전부요. 필요한 건 진입점 하나뿐입니다.

```swift
import Foundation
import CalendarBridge   // any `import XBridge` auto-wires, no Package.swift edits

@_cdecl("script_main")
public func scriptMain() -> Int32 {
    print("Hello from AgentScript! 👋")
    return 0
}
```

스크립트가 출력하는 건 모두 모델에게 돌아가고, 반환값은 종료 상태가 됩니다. 앱에는 `TodayEvents`, `NowPlaying`, `CheckMail`, `CreateDmg`를 비롯해 35개 정도의 예제가 함께 들어 있습니다.

## 직접 읽어 볼 수 있는 안전

Agent!는 root 권한으로 명령을 실행할 수 있습니다. 그만큼 큰 신뢰를 부탁드리는 거니까, 안전이 발표 자료 속 슬라이드 한 장으로 끝나서는 안 되죠. 안전은 코드이고, GitHub에서 직접 읽어 보실 수 있습니다. 하드코딩된 `ShellSafetyService`가 치명적인 명령을 보내기도 전에 거부하고, 권한을 가진 데몬도 자기 쪽에서 똑같은 검사를 한 번 더 합니다. 여기에 **Jev** 라는 선택형 두 번째 의견도 있어서, 명령이 데이터를 날려 버릴 가능성이 얼마나 되는지 평가해 줍니다. 이게 정확히 어떻게 동작하는지는 [첫 번째 심층 분석](/blog/inside-agent-shell-guardrails/)에서 차근차근 살펴봅니다.

## 가족이 계속 늘어납니다

같은 에이전트 루프가 이제 터미널에서도 돌아갑니다. macOS, Windows, Linux 모두에서요. 기능이 똑같은 CLI가 두 개 있는데, Rust로 만든 [AgentiLoopCLI](https://github.com/AgentiLoop/AgentiLoopCLI)와 Go로 만든 [AgentiLoopGo](https://github.com/AgentiLoop/AgentiLoopGo)입니다. README에서 제가 제일 좋아하는 재미있는 사실: 이 작은 동생들은 Mac용 Agent!가 직접 작성했습니다.

## 이곳에서 만나게 될 것들

- **내부 구조:** 에이전트 루프, 컨텍스트 압축, 도구 디스패치, 하위 에이전트, 메모리와 플랜.
- **보안:** 가드레일, XPC 신뢰 모델, 그리고 최근의 에이전트 사고들이 우리 모두에게 주는 교훈.
- **이유까지 담은 릴리스 노트:** 빌드마다 무엇이 바뀌었는지, 그리고 그렇게 할 수밖에 없게 만든 버그.
- **사용 가이드:** AgentScript 레시피, 예산에 맞춰 제공업체 고르기, 완전히 로컬로 실행하기.
- **더 넓은 에이전트 세계:** 뉴스와 리뷰를 다루되, 언제나 여러분의 Mac에 어떤 의미인지로 돌아옵니다.

Agent!는 macOS 14.6 이상, Apple Silicon과 Intel에서 돌아가고, 개인 용도로는 무료입니다. 아래에서 받아서 진짜 일을 하나 맡겨 보시고, 어땠는지 꼭 알려 주세요.
