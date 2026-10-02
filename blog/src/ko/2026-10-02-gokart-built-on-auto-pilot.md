---
title: GoKart: 오토파일럿이 오후 한나절 만에 만든 마리오 카트 스타일 레이싱 게임
description: Agent! 의 오토파일럿(Auto-Pilot)에 목표 하나 - "GoKart라는 이름의 마리오 카트 클론을 만들어라" - 를 주고 돌아오면, 트랙 세 개, 아이템 여덟 개, AI 라이벌, 그리고 3,344개의 테스트 검사를 통과하는 Godot 4 레이싱 게임이 기다리고 있습니다. 막혔던 부분까지 포함해, 로그가 말하는 실제로 일어난 일을 정리했습니다.
tags: Auto-Pilot, 쇼케이스, Godot
---
<figure style="margin:2rem 0">
<img src="/gokart-green-hills-drift.png" alt="GoKart의 Green Hills 트랙: 추적 카메라 시점으로, 빨간색과 흰색 줄무늬 벽, 초록색 지면, 파란 하늘 아래 회색 도로에서 플레이어 카트가 드리프트 중입니다. HUD에는 1위, 랩과 시간 카운터, 그리고 왼쪽 아래 구석에 트랙 미니맵이 표시됩니다." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Green Hills, 1랩, 1위로 드리프트 중. 이 프레임의 모든 메시, 셰이더, 사운드는 코드에서 생성되었습니다.</figcaption>
</figure>

어제 글에서 [오토파일럿(Auto-Pilot)](/blog/agent-1-1-87-and-agentiloop-cli-0-0-5/)을 소개했습니다. Mac용 Agent! 에 `/auto <목표>`를 입력하면 Stop All을 누를 때까지 그 목표를 향해 무인 사이클을 반복합니다. 이 글은 제가 그것을 게임에 겨눴을 때 반대편에서 무엇이 나왔는지에 관한 이야기입니다.

목표는 제가 입력한 거의 그대로입니다:

> create a Mario Kart clone called GoKart with all Mario Kart effects. I believe Godot 4 can do the Mario Kart effects, but I haven't built any of them yet: drift sparks and boost flames (GPUParticles3D), speed lines and boost blur (screen-space shaders, glow and tonemapping), item effects and tire trails (shaders plus ribbon meshes), kart movement (VehicleBody3D or custom arcade physics). Write unit tests and test the game frequently.

예산: 시간 제한 없음, 사이클 무제한. 모든 사이클에서 Agent! 안의 모델은 Claude Sonnet 5.5였습니다. 첫 커밋은 12:39에 들어왔습니다. 같은 날 오후 16:32에는 저장소에 커밋이 33개 쌓여 있었습니다. 오늘 기준으로 GDScript 파일 47개, GDScript와 셰이더 코드 약 5,500줄, 그리고 3,344개의 검사를 통과하는 유닛 테스트 스위트가 있습니다. 전체는 GitHub의 [AgentiLoop/GoKart](https://github.com/AgentiLoop/GoKart)에 있습니다.

## 오토파일럿이 하는 일, 한 사이클씩

오토파일럿은 프로젝트 안의 `.agent/autopilot/progress.md`에 진행 로그를 계속 기록하고, 매 사이클마다 무엇을 했는지, 무엇을 가정했는지, 무엇이 남았는지, 무언가에 막혔는지를 덧붙입니다. 아래 내용은 전부 그 로그가 출처입니다. 제 기억 대신 로그를 인용하는 이유는, 로그가 저보다 정직하기 때문입니다.

**사이클 1**에는 머신에 Godot이 없었습니다. `brew install --cask godot`을 실행하고, 바이너리에 심볼릭 링크를 걸고, `git init`을 한 뒤, `kart_physics.gd`를 씬 의존성이 없는 순수 모델로 작성했습니다. 가속, 제동, 후진, 마찰, 조향, 시작한 방향으로 고정되는 드리프트, 그리고 미니터보 3단계. `VehicleBody3D` 대신 커스텀 아케이드 물리를 의도적으로 선택했고, 이유도 밝혔습니다. "마리오 카트식 조작감을 유닛 테스트하기 쉽도록." 테스트 11개, 검사 17개, 첫 커밋.

**사이클 2**는 제가 이름을 짚어 요청한 효과들을 추가했습니다. 미니터보 단계에 따라 색이 바뀌는 GPUParticles3D 드리프트 스파크, 배기 화염, 리본 메시 타이어 자국, 그리고 방사형 부스트 블러, 스피드 라인, 비네트를 위한 스크린 스페이스 셰이더. 검사 43개.

**사이클 3**은 트랙을 만들었습니다. 3미터마다 리샘플링한 Catmull-Rom 루프, 도로 리본, 콜라이더가 달린 빨강-흰색 줄무늬 벽, 스크롤하는 셰브런 셰이더가 붙은 부스트 패드, 순서가 정해진 체크포인트 8개, 그리고 지름길이나 역주행 랩은 세지 않는 랩 트래커. 새 테스트 중 하나는 실제 물리 모델로 세 바퀴를 완주하는 추적 봇입니다. 1:02.5에 들어왔습니다. 검사 90개.

**사이클 4**는 무지개 프레넬 셰이더가 적용된 아이템 박스, 룰렛, 그리고 첫 세 가지 아이템을 추가했습니다. 버섯, 바나나, 벽에 튕기는 초록 등껍질. 맞으면 카트가 1.2초 동안 스핀합니다. 검사 235개.

그러고 나서 막혔습니다.

## 막혔던 부분

다음 사이클은 AI 카트와 헤드리스 스모크 레이스를 추가하기 시작했고, 다시는 돌아오지 않았습니다. 다음 세션에서 찾아낸 원인은 `main.gd` 115번째 줄에 잘못 들어간 탭 하나였습니다. 파싱 오류 때문에 스모크 스크립트가 끝없이 에러를 뿜어냈는데, 그것을 실행하던 셸 명령에는 시간 제한이 없었습니다.

저는 **Stop All**을 누르고, 같은 목표에 대문자로 쓴 메모를 덧붙여 새 세션을 시작했습니다. 전문을 옮기지는 않겠지만 요지는 이렇습니다. *스모크 실행을 테스트하다 막혔다, 막히지 마라, 셸에 시간 제한을 걸어라.*

두 번째 세션의 첫 사이클은 탭을 고치고, AI가 안쪽 벽으로 코너를 파고들지 않도록 AI의 전방 주시를 도로 샘플 10개에서 6개로 줄이고, 코너 속도 제한기를 추가하고, macOS에는 `timeout` 명령이 없기 때문에 모든 셸 실행을 `perl -e 'alarm 100; exec @ARGV'`로 감쌌습니다. 그때부터 거의 모든 사이클 끝에 로그에는 "모든 실행은 perl alarm 제한 아래에서 이루어졌다"고 적혀 있습니다. 목표 텍스트에서 교훈을 배우고 계속 적용한 것입니다.

그 세션은 약 1시간 15분 동안 15사이클을 돌았고, 각 사이클이 기능 하나입니다. 타이밍 좋게 가속하면 로켓 스타트 부스트가 붙는 출발 카운트다운; 미니터보 단계 상승 팝과 화면 가장자리 플래시; 미니맵; 유도 빨간 등껍질과 스타; 바퀴가 돌고 앞바퀴가 조향되며 드라이버가 고개를 돌리는 절차적 카트 모델; 모든 라이벌을 작게 만드는 번개; 카트 주위를 도는 트리플 등껍질; 도로를 따라 선두를 추격하는 파란 가시 등껍질; 점수가 있는 결과 화면; 엔진 루프부터 피니시 징글까지 오디오 파일 하나 없이 완전히 합성된 사운드; 두 번째 트랙이 있는 타이틀 메뉴; 랩 수 옵션; 세 번째 트랙; 그리고 각 AI 카트의 3D 위치 기반 엔진 소리.

<figure style="margin:2rem 0">
<img src="/gokart-sunset-speedway.png" alt="GoKart의 Sunset Speedway 트랙: 주황색에서 보라색으로 물드는 노을 하늘 아래, 모래 서킷을 전속력으로 달리는 플레이어 카트. HUD에는 4위, 1랩, 그리고 헤어핀이 있는 긴 트랙의 미니맵 윤곽이 표시됩니다." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Sunset Speedway, 두 번째 트랙. 사이클 12에서 타이틀 메뉴와 함께 추가되었습니다. Green Hills보다 길고, 헤어핀과 시케인이 있습니다.</figcaption>
</figure>

## 정직했던 부분

로그에서 제가 가장 좋아하는 것은 반복되는 고백의 패턴입니다. Agent! 는 PNG를 볼 수 없고, 사이클마다 그렇게 말했습니다:

> 창 모드 스크린샷 실행에서 오류는 기록되지 않았지만, 저는 이미지를 볼 수 없어서 트랙이나 HUD가 어떻게 렌더링되는지는 확인하지 못했습니다.

> 사운드는 들어보지 못했고, 스모크 레이스나 스크린샷 도구도 실행하지 않았습니다.

> 제 도구로는 이미지를 볼 수 없으니, 그 검토는 사람이 해야 합니다.

그래서 할 수 있는 것을 테스트했습니다. 실제 씬을 인스턴스화하고 상태를 검증하는 헤드리스 씬 검사입니다. 번개를 발사하고, 라이벌 셋이 0.5 스케일로 스핀 중인지, 그리고 번개가 이후 정리되는지 확인. 뭉쳐 있는 출발 그리드에 파란 등껍질을 쏘고, 12프레임째 폭발과 카트 두 대의 스핀을 확인. 플레이어를 강제로 완주시키고, 오토파일럿이 카트를 `AiDriver`에 넘기며 결과 패널에 "1st YOU"가 표시되는지 확인.

세 번째 세션도 같은 방식으로 멈췄습니다. 이번에는 지나치게 후한 240초 alarm 뒤에서였고, 한 사이클 만에 제가 중단했습니다. 그다음에는 사람이 봤습니다. 그 사람은 저였고, 네 번째 세션의 목표는 제 플레이테스트 메모를 살짝 다듬은 것이었습니다:

> the UI needs to scale with the window. the UI should not be prone to the screen speed effects and blurry. Should be able to use cursor keys. it's not clear when power ups are released. the tops of the walls flicker. Little too hard to steer the kart. hard to keep up with the computer AI karts. maybe have AI difficulty levels Easy Medium and Hard.

한 사이클 뒤: UI가 창 크기에 맞춰 스케일되도록 canvas-items 스트레치, HUD를 속도 효과 오버레이 위의 캔버스 레이어로 이동, 화살표 키와 아이템용 Enter 및 Ctrl에 화면 힌트 추가, 부드럽게 들어가는 조향, 벽 줄무늬의 z-fighting 수정(이웃한 빨간 세그먼트와 흰 세그먼트가 같은 픽셀을 두고 다투고 있어서 흰 것을 아주 살짝 키웠습니다), 4x MSAA, 그리고 AI 최고 속도를 0.72, 0.85, 1.0으로 조정하는 쉬움 / 보통 / 어려움 난이도. 테스트는 2,156개에서 3,344개 검사로 늘었는데, 스위트가 로드되지 않게 만들던 `tests/test_items.gd`의 기존 파싱 오류까지 찾아서 고친 덕이 큽니다.

## 스스로 멈춘 부분

그 마지막 세션의 사이클 2부터 8까지는 코드 변경이 없었습니다. 매 사이클 저장소를 다시 읽고, 스위트를 다시 돌리고, 같은 문단의 변형을 썼습니다:

> 화면에서 결과를 볼 수 없었으므로 목표가 달성되었다고 선언하지 않습니다. 네 가지 항목은 여전히 사람이 게임에서 직접 해봐야 합니다.

이것이 올바른 동작입니다. 목표는 "조향감이 나쁘다"와 "벽이 깜빡인다"였고, 어떤 헤드리스 테스트도 그 목표를 닫을 수 없습니다. 오토파일럿에는 반복 상한이 없어서, 영원히 확인만 계속했을 것입니다. 세션은 사이클 8 이후 끝났고, GoKart에 다음으로 필요한 것은 또 한 번의 사이클이 아니라 플레이테스트였습니다.

<figure style="margin:2rem 0">
<img src="/gokart-frosty-peaks.png" alt="GoKart의 Frosty Peaks 트랙: 짙은 남색 황혼 하늘 아래, 눈처럼 하얀 서킷을 전속력으로 달리는 플레이어 카트. HUD에는 2위, 1랩, km/h 단위 속도, 미니맵이 표시됩니다." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Frosty Peaks, 사이클 14에서 트랙 라이브러리의 새 항목으로 추가되었습니다. 트랙별 테스트가 자동으로 집어 올렸습니다.</figcaption>
</figure>

## 이 스크린샷에 대하여

찍은 것은 Agent! 이고, 제가 아니며, 손으로 찍은 것도 아닙니다. 무작위 주행 스크린샷 세 장을 요청했더니, 70줄짜리 `tools/random_drive.gd`를 작성했습니다. 흔들리는 차선 오프셋으로 도로를 따라가고, 무작위로 드리프트를 터뜨리고, 들고 있는 아이템을 무작위 순간에 발사한 뒤, 물리 프레임 몇백 개마다 한 프레임을 저장합니다. 트랙마다 한 번씩 실행했고, 위의 세 장은 각각에서 한 프레임씩 고른 것입니다. [GoKart README](https://github.com/AgentiLoop/GoKart#screenshots)에도 있습니다.

## 직접 해보기 전에 드리고 싶은 말

- **git 안에서 실행하세요.** 오토파일럿에는 되돌리기가 없습니다. GoKart의 로그를 읽을 수 있는 이유는 모든 사이클이 커밋으로 끝났기 때문이고, 사이클이 한 번 엇나갔을 때도 잃은 것은 없었습니다.
- **운영 규칙을 목표에 넣으세요.** "셸에 시간 제한을 걸어라"는 일회성 메시지보다 목표의 일부일 때 더 잘 작동했습니다. 새 사이클은 매번 목표를 다시 읽기 때문입니다.
- **눈을 요청할 것을 예상하세요.** 시각적이거나 느낌에 관한 것이라면, 루프는 거짓말하는 대신 정직하게 멈춥니다. 세션 사이에 플레이테스트 시간을 잡고, 메모를 다음 목표로 다시 넣어주세요.
- **Stop All은 워크플로의 일부**이지 실패가 아닙니다. GoKart의 첫 세 세션은 모두 그렇게 끝났습니다.

## GoKart 0.0.1

이제 Godot 없이도 바로 해볼 수 있습니다. [GoKart 0.0.1](https://github.com/AgentiLoop/GoKart/releases/tag/v0.0.1)은 같은 저장소에서 내보낸 첫 번째 패키지 릴리스입니다:

- **macOS** 유니버설 (Apple Silicon 및 Intel), Developer ID로 서명하고 Apple에서 공증
- **Windows** x86_64
- **Linux** x86_64 및 arm64

각 다운로드는 게임 데이터가 내장된 단일 독립 실행 바이너리이며, 받은 파일을 확인하고 싶다면 릴리스 페이지에 `SHA256SUMS.txt`가 있습니다. Windows 빌드는 서명되지 않았으므로 SmartScreen 경고가 뜰 수 있습니다.

오토파일럿이 포함된 Agent! 1.1.87은 [릴리스 페이지](https://github.com/AgentiLoop/Agent/releases/latest)와 Homebrew에 있습니다. 소스에서 GoKart를 실행하고 싶다면 Godot 4.4 이상이 필요합니다: `git clone https://github.com/AgentiLoop/GoKart.git && cd GoKart && godot --path .`
