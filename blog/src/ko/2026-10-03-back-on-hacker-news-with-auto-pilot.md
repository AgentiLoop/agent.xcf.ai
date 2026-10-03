---
title: 6개월 만에 Auto-Pilot과 함께 다시 Hacker News에
description: Agent!가 Show HN으로 다시 Hacker News에 올라왔습니다. 4월 스레드는 네이티브 Mac 코딩 하네스에 관한 것이었고, 이번에는 목표에 도달할 때까지 사이클을 계속 실행하는 목표 주도 루프인 Auto-Pilot과, 그것이 만들어 온 마리오 카트 스타일 게임에 관한 것입니다. 게시물의 내용, 그 안의 각 주장 뒤에 있는 근거, 그리고 토론에 참여할 수 있는 곳을 소개합니다.
tags: Auto-Pilot, 커뮤니티, Hacker News
---
Agent!가 오늘 Show HN으로 Hacker News에 다시 올라왔습니다: [Show HN: AgentiLoop Agent Mac GUI Agent Loop for macOS 14.6 or Later](https://news.ycombinator.com/item?id=49948810). Hacker News 계정이 있다면, 그 스레드가 질문을 하고, 허점을 찾고, Mac 에이전트에 무엇을 바라는지 말해 줄 수 있는 자리입니다. 이 글은 제출문의 긴 버전으로, 그 안의 모든 주장에 대한 출처를 함께 담았습니다.

## 원문

제출문은 짧으므로, [Hacker News 항목](https://news.ycombinator.com/item?id=49948810)에서 인용한 전문을 여기에 싣습니다:

> Agent!는 지난 4월에 처음 Hacker News에 올라왔습니다. 그 이후로 많은 것이 바뀌었습니다. 최근 Auto-Pilot이라는 새로운 기능이 개발되었습니다. 목표가 주어지면 그 목표에 도달할 때까지 멈추지 않습니다. 강화된 태스크라고 생각하시면 됩니다. Agent가 하는 일은 여러 개의 태스크를 만드는 것입니다. 각 태스크는 Cycle(사이클)이라고 부릅니다. 기본적으로 auto [goal]로 실행된 Auto-Pilot에는 시간 제한이 없습니다. Agent!는 목표에 도달할 때까지 계속 실행하라는 지시를 받습니다. Auto-Pilot에는 킬 스위치인 "Stop All" 버튼이 있습니다. 사용자는 auto stop으로 현재 Cycle만 종료할 수도 있고, auto stop all로 전부 종료할 수도 있습니다. 11월에는 같은 프로젝트에서 여러 개의 Auto-Pilot을 동시에 실행할 수 있게 됩니다. 그리고 Auto-Pilot 탭이 다른 탭을 자동으로 생성할 수 있게 됩니다. 현재 우리는 GoDot 4로 작성한 마리오 카트 유사 클론 "GoKart"를 개발하고 있습니다. 지금까지 게임을 개발하고 개선하는 데 20시간 이상이 기록되었습니다. *(영어 원문 번역)*

아래 내용은 모두 그 글의 한 문장씩을 풀어 쓴 것입니다.

## "Agent!는 지난 4월에 처음 Hacker News에 올라왔습니다"

첫 번째 스레드는 2026년 4월 16일의 [Agent — Native macOS coding IDE/harness](https://news.ycombinator.com/item?id=47787127)로, 83포인트에 댓글 54개였습니다. 당시 앱은 macOS 26.4와 Apple silicon이 필요했고, 17개의 LLM 프로바이더를 지원했으며, 주로 Accessibility API를 통해 Mac 앱도 조작할 수 있는 코딩 하네스로 소개되었습니다. 두 스레드 모두 이 사이트의 [Reviews](/#reviews) 섹션에, 그 사이에 나온 독립적인 리뷰 글들과 함께 실려 있습니다.

4월 이후로: macOS 14.6 및 Intel 지원([그 포팅의 이야기](/blog/sonoma-intel-and-the-mac-that-was-not-dead-yet/)), 23개 프로바이더, [복구할 수 있는 컨텍스트 압축](/blog/context-compaction-half-the-window/), Mac, Windows, Linux용 [Rust 및 Go CLI](/blog/agent-1-1-87-and-agentiloop-cli-0-0-5/), 매월 1일 릴리스, 그리고 이번 제출문이 실제로 다루고 있는 기능이 추가되었습니다.

## "목표가 주어지면 그 목표에 도달할 때까지 멈추지 않습니다"

Auto-Pilot은 Mac용 Agent!의 `/auto` 명령입니다. README의 Auto-pilot 섹션에 따르면: 메인 탭이나 임의의 LLM 탭에서 태스크 루프를 무인 사이클로 실행하며, 목표에 도달하거나, 시간 예산이 소진되거나, Stop을 누를 때까지 계속됩니다. 사이클 수 제한도, 사이클당 반복 횟수 상한도 없습니다. 사이클의 태스크가 끝났는데 목표에 도달하지 못하면, 다음 사이클이 자동으로 시작됩니다.

| 명령 | 동작 |
|---|---|
| `/auto <goal>` | LLM이 도달했다고 보고할 때까지 목표를 향해 작업 |
| `/auto 4h <goal>` | 동일하지만 4시간 후 중지(`30m`, `1.5h`도 가능) |
| `/auto` | 먼저 프로젝트를 검토한 뒤 목표를 물어봄 |
| `/auto history`, `/auto last`, `/auto #N` | 이전 목표 목록 표시, 가장 최근 또는 N번째 목표 재시작 |
| `/auto status` / `/auto stop` | 세션 표시, 또는 현재 사이클이 끝난 뒤 종료 |

"강화된 태스크라고 생각하시면 됩니다"가 올바른 멘탈 모델입니다. 각 사이클은 동일한 도구, 동일한 가드레일(read-before-edit, goal_state 증거, 셸 차단 목록), 동일한 `done()` 계약을 갖는 *그 자체로* 일반적인 Agent! 태스크입니다. Auto-Pilot이 더하는 것은 그 주위를 감싸는 루프입니다. 사이클의 요약이 프로젝트 안의 `.agent/autopilot/progress.md`에 추가되어 다음 사이클의 프롬프트에 공급되므로, 각 사이클은 이전 사이클들이 무엇을 했고, 무엇을 가정했으며, 무엇을 남겨 두었는지 읽는 것으로 시작합니다. 세션은 LLM이 최종 요약을 `AUTOPILOT: GOAL REACHED`로 시작할 때만 끝납니다. 오류나 취소로 요약 없이 끝난 사이클은 세션을 종료하지 않습니다. 다음 사이클이 그저 더 오래 기다릴 뿐입니다. 15초, 그다음 30초, 그다음 60초, 최대 5분까지입니다.

"기본적으로 … 시간 제한이 없습니다"는 말 그대로입니다. 기간 없이 `/auto <goal>`을 실행하면 목표에 도달하거나 사용자가 중지할 때까지 실행됩니다. 상한이 필요하다면 `/auto 4h <goal>`로 지정할 수 있습니다. 활성 세션은 앱 재시작 후에도 유지됩니다. 종료하거나 크래시가 나면 세션이 일시 중지되고, 다음 실행 시 각 세션이 자기 탭에서 다음 사이클로 재개됩니다.

## "Auto-Pilot에는 킬 스위치가 있습니다"

중지하는 방법은 세 가지이며, 각각 하는 일이 다릅니다:

- **Stop All**(모두 중지, 버튼)은 모든 탭의 모든 Auto-Pilot 세션을 종료하고 실행 중인 모든 태스크를 중지합니다. `RunStop.swift`의 주석에 명시되어 있습니다. 단일 태스크 중지(Esc 또는 중지 버튼)는 Auto-Pilot을 계속 실행 상태로 두고, Stop All은 이를 종료합니다.
- **`/auto stop`**은 현재 사이클이 끝난 뒤 세션을 종료하며, 사이클 사이라면 즉시 종료합니다. 현재 사이클은 끝까지 진행하도록 허용됩니다.
- **`/auto stop all`**(`stopall` 또는 `stop-all`도 가능)은 Stop All을 누르는 것과 같으며, 마우스에 손을 뻗고 싶지 않은 사람을 위한 것입니다. `AutoPilot.swift`에서 `/auto stop` 바로 앞에서 처리됩니다.

제출문에서는 `auto stop`이 "현재 Cycle만" 종료한다고 설명합니다. 더 정확히 말하면 현재 사이클이 끝난 뒤 *세션*을 종료하는 것이며, 사이클 자체는 자연스러운 끝까지 실행됩니다. 이것이 진행 로그와 git 히스토리를 깨끗하게 유지하는 비결입니다.

## "11월에는 … 같은 프로젝트에서 여러 개의 Auto-Pilot을 동시에 실행"

이 부분은 제출문에서 이미 출시된 기능이 아니라 로드맵 항목이며, 어느 쪽이 어느 쪽인지 분명히 해 둘 가치가 있습니다. 오늘 기준으로 Agent 저장소의 main 브랜치에는 *Auto-Pilot: multiple tabs per project — per-tab progress, shared registry, auto/forced git worktree isolation, shared memory from worktrees*라는 제목의 커밋이 있습니다. 그것이 기반 작업입니다. 각 탭은 자기만의 진행 로그를 유지하고, 탭들은 서로 등록하며, 두 Auto-Pilot이 같은 파일을 편집하려 할 때는 별도의 git worktree를 받습니다. 아직 릴리스에는 포함되지 않았으며, 1.1.87 태그 이후에 들어갔습니다. 릴리스는 매월 1일에 나오므로, 11월 1일 릴리스가 여러분에게 도달할 수 있는 가장 빠른 시점이며, "다른 탭을 생성하는 탭" 부분은 제출문에 따르면 같은 시기에 계획되어 있습니다.

## "마리오 카트 유사 클론 GoKart"

GoKart는 Auto-Pilot이 그 수명의 대부분을 보낸 프로젝트입니다. [이전 글](/blog/gokart-built-on-auto-pilot/)에서 첫날 오후를 진행 로그 그대로 자세히 다루고 있습니다. 사이클 1에서 Godot 4 설치, 핸들링을 단위 테스트할 수 있도록 `VehicleBody3D` 대신 커스텀 아케이드 물리 선택, 사이클 2에서 드리프트 스파크와 부스트 블러, 사이클 3에서 트랙, 사이클 4에서 아이템, 잘못 들어간 탭 문자로 인한 정체, Stop All, 그리고 모든 셸 실행에 `perl -e 'alarm'` 시간 제한을 걸고 나서 15개의 기능을 연달아 출시한 두 번째 세션.

멈추지 않았습니다. [GoKart 저장소](https://github.com/AgentiLoop/GoKart)는 10월 1일 12:39의 첫 커밋에서 10월 3일 저녁까지 71개의 커밋에 이르렀습니다. 최근 커밋은 마리오 카트 64 체크리스트처럼 읽힙니다. Sunset Speedway의 Toad's Turnpike 스타일 교통, Green Hills의 Moo Moo Farm 스타일 Monty Mole, 라이브 어트랙트 데모가 있는 타이틀 화면, 결과 보드, HUD에 그려진 아이템 창. 각각은 자체 테스트 파일과 `tools/*_check.gd` 스크립트와 함께 들어갑니다. 모델은 여전히 화면을 볼 수 없어서 기능이 존재한다는 것을 다른 방법으로 증명해야 하기 때문입니다. 제출문의 "20시간 이상"은 그 세션들의 실제 경과 시간 합계입니다. 읽기보다 직접 플레이하고 싶다면 [GoKart 0.0.1](https://github.com/AgentiLoop/GoKart/releases/tag/v0.0.1)을 macOS, Windows, Linux용으로 다운로드할 수 있습니다.

## 스레드에서 물어볼 만한 것

Hacker News에서 오셨다면, 우리가 거기서 가장 답하고 싶은 질문들은 다음과 같습니다:

- Auto-Pilot이 목표 도달을 어떻게 판단하는지, 그리고 왜 고정된 지표 대신 모델이 그렇게 말하도록 두는지.
- 사이클이 잘못되면 어떻게 되는지, 그리고 왜 git이 진정한 실행 취소인지.
- 애초에 Mac에서 무인 루프를 돌리는 것이 좋은 생각인지, 그리고 가드레일이 그에 대해 무엇을 하는지.

스레드는 [news.ycombinator.com/item?id=49948810](https://news.ycombinator.com/item?id=49948810)에 있습니다. Auto-Pilot이 포함된 Agent! 1.1.87은 [릴리스 페이지](https://github.com/AgentiLoop/Agent/releases/latest)와 Homebrew에서 받을 수 있습니다: `brew install --cask agentiloop-agent`.
