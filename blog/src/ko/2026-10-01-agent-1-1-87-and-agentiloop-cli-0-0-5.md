---
title: 온 가족이 함께 출시합니다: Agent! 1.1.87과 AgentiLoop CLI 0.0.5
description: Mac용 Agent! 에 오토파일럿(Auto-Pilot), 여섯 개의 새 프로바이더, 더 엄격한 크리틱, macOS 14.6 지원이 추가되었습니다. Rust와 Go CLI는 더 커진 도구 상자를 갖추게 되었습니다. 검색, 웹 가져오기, 할 일 목록, AGENTS.md, /undo, 사용자 정의 명령, --json까지.
tags: 공지, 릴리스, 크로스 플랫폼
---
<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 380" role="img" aria-labelledby="fam-title fam-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="fam-title">AgentiLoop 가족: Mac 앱 하나와 터미널 둘</title>
<desc id="fam-desc">가운데에 Agent! 1.1.87이라고 표시된 큰 Mac 창이 있습니다. 왼쪽 터미널 창에는 작은 게와 Rust 0.0.5라는 라벨이, 오른쪽 터미널 창에는 작은 고퍼와 Go 0.0.5라는 라벨이 보입니다. 점선이 세 창을 모두 위쪽의 공유 루프 기호와 연결합니다.</desc>
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
<text x="380" y="345" text-anchor="middle" font-family="system-ui,sans-serif" font-size="18" fill="#9fb6d4">하나의 루프. 세 가지 실행 방식.</text>
</svg>
<figcaption>10월 1일의 AgentiLoop 가족: Mac용 Agent! 와 Rust 및 Go 커맨드라인 에디션.</figcaption>
</figure>

오늘 온 가족이 한꺼번에 출시됩니다. **Agent! 1.1.87** 은 Mac 앱의 새 릴리스이고, **AgentiLoop CLI 0.0.5** 는 [Rust](https://github.com/AgentiLoop/AgentiLoopCLI/releases/tag/v0.0.5)와 [Go](https://github.com/AgentiLoop/AgentiLoopGo/releases/tag/v0.0.5) 양쪽으로 나왔습니다. 프리릴리스가 아닌 정식 릴리스이며, 세 제품 모두에게 지금까지 가장 큰 도약입니다.

git 기록에서 바로 가져온 새로운 내용을 소개합니다.

## Mac용 Agent! 1.1.87

Mac 앱의 마지막 정식 릴리스는 9월 12일의 1.1.33이었습니다. 그 이후로 많은 일이 있었습니다. 1.1.87에는 449개의 커밋이 들어갔습니다. 주요 내용은 다음과 같습니다.

### 🤖 오토파일럿: `/auto <goal>`

이번 릴리스의 대표 기능입니다. Agent! 에게 목표를 주면, `/auto` 가 시간 예산 안에서 무인 사이클을 연달아 실행합니다. 각 사이클은 목표를 향해 작업하고, 현재 상황을 점검한 뒤 계속 진행합니다.

- 사이클이나 반복 횟수 제한이 없습니다. LLM 탭에서 동작하며 목표 기록을 유지하므로, `/auto last` 와 `/auto #N` 으로 이전 목표를 다시 불러올 수 있습니다.
- 세션은 앱을 재시작해도 유지되며 같은 탭에서 이어집니다.
- **Esc** 는 현재 사이클만 멈춥니다. **Stop All**(또는 `/auto stop all`)은 세션 전체를 종료합니다.

이것은 사람이 의도적으로 한 발 물러선 에이전트 루프입니다. 여러분이 목적지와 예산을 정하면, 운전은 Agent! 가 합니다.

### 🔌 여섯 개의 새 프로바이더, 그리고 만질 설정은 더 적게

1.1.87의 새 프로바이더: **Fluxion AI**(OpenAI 및 Anthropic 프로토콜 옵션 포함), **Muse Code**(`muse login` 구독을 재사용), **Requesty**, **A2Agent**, **OrcaRouter**, 그리고 Coding Plan의 **Qwen Code**. 로컬 Chat Completions API를 통해 Apple Foundation Models를 제공하는 실험적인 **fm serve** 프로바이더도 있습니다.

이제 비전 지원은 각 프로바이더의 카탈로그 메타데이터로 감지되므로, Force Vision 토글이 더 이상 필요 없습니다. 내부적으로는 모든 프로바이더가 십여 개의 개별 코드 경로 대신 하나의 레지스트리 `APIProvider` 에 모여 있습니다.

### 🧐 말로 구슬릴 수 없는 크리틱

Agent! 에는 크리틱 게이트가 있습니다. 작업이 완료로 처리되기 전에 두 번째 모델이 변경 사항을 검토합니다. 1.1.87에서는 이 검토가 **강제** 됩니다. 바뀌지 않은 diff는 거부되고, 바뀐 diff는 다시 검토되며, 문제를 "범위 밖"이라며 넘겨 버릴 수 없습니다. 크리틱은 이제 Codex와 Apple Intelligence에서도 실행되며, 로그에는 어떤 문제를 발견했는지와 그 후 코드가 변경되었는지가 표시됩니다.

함께 등장한 것이 **Jev** 로, 도구 루프에 조언하는 TypeSafe System One 의사 결정 계층입니다. 설정은 새로운 LLM 공통 설정(LLM Common Settings)에 있습니다.

### 🧠 더 똑똑한 컨텍스트

컨텍스트 압축을 꼼꼼히 손봤습니다. 이제 임계값은 *실제로 사용 중인* 모델(탭의 모델 또는 대체 모델)을 기준으로 정해지며, 가져온 Ollama 컨텍스트 창 크기를 기억합니다. 이로써 일부 모델이 16K에서 압축되던 버그가 수정되었습니다. 유지되는 꼬리 부분과 마이크로 압축은 메시지 수가 아닌 토큰 수로 제한되고, 지나치게 큰 블록이 먼저 잘리며, 컨텍스트 초과와 `max_tokens` 오류는 모든 프로바이더에서 같은 방식으로 감지됩니다.

### 🖥️ 더 많은 Mac, 더 많은 언어

- **macOS 14.6 Sonoma 이상**, Apple Silicon과 Intel 모두 지원합니다. Apple Intelligence(Foundation Models) 기능은 macOS 26이 필요합니다.
- 앱이 스페인어, 프랑스어, 독일어, 중국어(간체), 러시아어, 한국어, 일본어로 현지화되었습니다.
- 새로운 Accessibility 액션: `wait_until_actionable`, `select_text_range`, `observe_start/poll/stop/list`.
- Homebrew로 설치: `brew update && brew install --cask agentiloop-agent`.

### 🔒 기본적으로 더 안전하게

현재 프로젝트 폴더를 재귀적으로 삭제하는 작업이 이제 차단됩니다. 앱 전반에 걸친 버그 사냥으로 ShellSafety의 `&` 읽기 전용 우회, Ollama 스트리밍 멈춤, 여러 크래시가 수정되었습니다. 요약이 실제로 작성된 적 없는 출력을 가리키면 `task_complete` 가 거부되며, 메모리가 부족한 로컬 모델은 헛돌지 않고 명확한 이유와 함께 즉시 멈춥니다.

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 330" role="img" aria-labelledby="box-title box-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="box-title">CLI를 위한 더 커진 도구 상자</title>
<desc id="box-desc">0.0.5라고 표시된 열린 빨간 도구 상자. 라벨이 붙은 도구들이 상자에서 솟아오릅니다. 돋보기와 함께 있는 glob과 grep, 지구본과 함께 있는 web_fetch, 체크리스트와 함께 있는 todo_write, 휘어진 화살표와 함께 있는 /undo, 문서와 함께 있는 AGENTS.md, 중괄호와 함께 있는 --json.</desc>
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
<figcaption>AgentiLoop CLI 0.0.5: 같은 루프, 상자 안에는 훨씬 더 많은 것.</figcaption>
</figure>

## AgentiLoop CLI 0.0.5: 더 커진 도구 상자

우리가 [에이전트 루프를 터미널로 가져왔을](/blog/the-terminal-strikes-back/) 때, CLI는 read, list, write, edit, bash라는 다섯 개의 날카로운 도구로 시작했습니다. 0.0.4 버전에서는 깔끔하게 멈추는 법을 배웠습니다. 0.0.5 버전은 더 많은 것을 다룰 수 있게 하는 데 초점을 맞췄습니다. 모든 기능이 Rust에 먼저 들어갔고 Go에 커밋 단위로 그대로 반영되었기 때문에, 두 에디션의 기능은 완전히 같습니다.

### 새로운 도구

| 도구 | 하는 일 | 먼저 묻나요? |
|---|---|---|
| `glob` | 패턴으로 파일을 찾습니다 | 아니요 |
| `grep` | 0–5줄의 컨텍스트와 함께 파일 내용을 검색합니다 | 아니요 |
| `web_fetch` | http(s) 페이지를 크기 제한과 함께 텍스트로 가져옵니다 | **예** |
| `todo_write` | 여러 단계 작업을 위한 체크리스트를 유지합니다 (`/todos` 로 확인) | 아니요 |

`glob` 과 `grep` 은 `.git`, `node_modules`, `target`, 바이너리 파일을 건너뛰며, 중첩 파일, 부정, 앵커링, 디렉터리 전용 규칙을 포함해 `.gitignore` 를 따릅니다. 덕분에 셸에서 `find` 를 호출하는 것보다 빠르고, 트리 전체를 컨텍스트에 쏟아붓는 것보다 안전합니다.

### 프로젝트의 지침을 읽습니다

저장소에 **`AGENTS.md`** 또는 **`CLAUDE.md`** 가 있으면 CLI가 이를 시스템 프롬프트에 불러오며, 개인 기본값을 위해 `~/.agentiloop` 에 있는 파일도 함께 불러옵니다. `@docs/style.md` 같은 줄은 다른 파일을 가져옵니다(중첩 가능, 순환 방지). 아직 파일이 없나요? **`/init`** 이 감지한 빌드 및 테스트 명령을 담은 기본 `AGENTS.md` 를 작성해 줍니다.

### 실행 취소, diff, 그리고 친구들

- **`/undo`**: `write_file`, `edit_file`, `apply_patch` 로 이루어진 모든 변경이 프롬프트별로 기록되므로, 에이전트의 마지막 턴을 되돌릴 수 있습니다.
- **`/diff`** 는 작업 트리의 git 상태와 diff를 보여줍니다.
- **`/export`** 는 대화를 Markdown으로 저장합니다.
- **`/usage`** 는 시작 이후의 토큰 합계와 컨텍스트가 얼마나 찼는지를 보여줍니다.

### 나만의 것으로 만들기

- **사용자 정의 슬래시 명령**: `.agentiloop/commands/` 에 Markdown 파일을 넣으세요. 예를 들어 `Review $1 for bugs` 를 담은 `review.md` 를 넣으면 `/review main.rs` 가 이를 실행합니다. `$ARGUMENTS` 와 `$1`..`$9` 를 지원하며, `/commands` 가 목록을 보여줍니다.
- 서버의 **MCP 프롬프트** 는 `/mcp__<server>__<prompt>` 명령으로 나타납니다.

### 스크립트와 CI를 위해

- **`--json`** 은 원샷 응답을 하나의 JSON 객체로 출력합니다: result, is_error, session_id, provider, model, usage.
- **`--allow-tool` / `--deny-tool`** 은 도구 이름이나 `mcp_*` 접두사로 권한 규칙을 설정합니다. 거부가 항상 우선하며, `--yes` 보다도 우선합니다.
- **`--append-system-prompt`** 는 한 번의 실행에 한해 시스템 프롬프트에 텍스트를 추가합니다.
- **파이프가 그냥 동작합니다**: 프롬프트에 단독으로 있는 `-` 는 stdin으로 대체되므로, `git diff | agentiloop "review this" -` 는 말 그대로 동작합니다.

이를 모두 합치면, 풀 리퀘스트를 검토하고, 셸은 건드리지 않으며, 기계가 읽을 수 있는 출력을 반환하는 CI 단계가 됩니다.

```
git diff origin/main | agentiloop --deny-tool bash --json "review this diff" -
```

## 왜 함께 출시하나요?

세 가지 모습을 한 같은 아이디어이기 때문입니다. Mac용 Agent! 는 플래그십으로, 여러분의 앱과 Xcode 빌드, 데스크톱 전체를 조작합니다. CLI는 같은 루프를 macOS, Windows, Linux의 모든 터미널로 가져갑니다. CLI의 Esc로 취소하기와 Stop All 버튼이 있는 Mac 앱의 오토파일럿은 같은 질문에 양쪽에서 답합니다. *스스로 돌아가는 루프를 사람이 어떻게 계속 통제할 수 있을까?*

이것이 우리가 가장 중요하게 여기는 부분입니다. 귀여운 아바타도, 벤치마크의 더 높은 숫자도 아닌, 루프 속의 사람입니다. 여러분이 목표를 정하고, 모든 단계를 보고, 멈출 수 있고, 되돌릴 수 있습니다.

## 다운로드

- **Mac용 Agent! 1.1.87**: [GitHub에서 다운로드](https://github.com/AgentiLoop/Agent/releases/tag/v1.1.87.287)하거나 `brew update && brew install --cask agentiloop-agent`. macOS 14.6 이상, Apple Silicon 또는 Intel.
- **AgentiLoop CLI 0.0.5 (Rust)**: [GitHub 릴리스](https://github.com/AgentiLoop/AgentiLoopCLI/releases/tag/v0.0.5).
- **AgentiLoopGo 0.0.5 (Go)**: [GitHub 릴리스](https://github.com/AgentiLoop/AgentiLoopGo/releases/tag/v0.0.5).

macOS용 CLI 바이너리는 서명 및 공증되어 있습니다. 압축을 풀고 `agentiloop` 을 PATH에 넣은 뒤 실행하면, 나머지는 설정 마법사가 안내합니다.

테스터는 언제나 환영합니다. 큰 수정 후에 `/undo` 를 써 보거나, `AGENTS.md` 가 있는 저장소를 지정해 보거나, `--json` 을 스크립트에 연결해 본 뒤 무엇이 깨졌는지 알려주세요. OS, 프로바이더, 모델을 함께 적어 주시고, API 키는 절대 포함하지 마세요.
