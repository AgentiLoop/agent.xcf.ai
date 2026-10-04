---
title: GoKart: 오토파일럿이 오후 한나절 만에 만든 마리오 카트 스타일 레이싱 게임
description: Agent! 의 오토파일럿(Auto-Pilot)에 목표 하나 - "GoKart라는 이름의 마리오 카트 클론을 만들어라" - 를 주고 돌아오면, 트랙 세 개, 아이템 여덟 개, AI 라이벌, 그리고 3,344개의 테스트 검사를 통과하는 Godot 4 레이싱 게임이 기다리고 있습니다. 이틀 뒤, 에이전트 커밋 87개가 더 쌓인 지금은 GoKart 0.0.2입니다. 코스 네 개, 배틀 모드, 타임 트라이얼, Mario Kart 64 스타일 메뉴, 그리고 14,134개의 검사 통과. 막혔던 부분까지 포함해, 로그가 말하는 실제로 일어난 일을 정리했습니다.
tags: Auto-Pilot, 쇼케이스, Godot
updated: 2026-10-04
---
<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-title.png" alt="GoKart 0.0.2 타이틀 화면: 노란색에서 빨간색으로 그라데이션되는 큰 글자에 남색 블록 측면과 부드러운 그림자를 더해 아치 위에 얹은 GOKART 글자가, CPU 카트들이 코스를 도는 라이브 어트랙트 데모 위에 떠 있고, 아래에는 PRESS ENTER가 표시됩니다." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>GoKart 0.0.2 타이틀 화면. 로고가 날아 들어와 튕기며 멈추고, 그 뒤로 코스들을 둘러보는 라이브 어트랙트 데모가 돌아갑니다. 모든 메시, 셰이더, 폰트 레이아웃, 사운드는 코드에서 생성되었습니다.</figcaption>
</figure>

*10월 4일 업데이트: 이 글은 이제 첫 오후 이후의 이틀, 같은 저장소에서 동시에 돌아간 두 개의 오토파일럿 세션, 그리고 [GoKart 0.0.2](#gokart-0-0-2) 릴리스까지 다룹니다. 스크린샷은 0.0.2 태그에서 다시 찍었습니다.*

어제 글에서 [오토파일럿(Auto-Pilot)](/blog/agent-1-1-87-and-agentiloop-cli-0-0-5/)을 소개했습니다. Mac용 Agent! 에 `/auto <목표>`를 입력하면 Stop All을 누를 때까지 그 목표를 향해 무인 사이클을 반복합니다. 이 글은 제가 그것을 게임에 겨눴을 때 반대편에서 무엇이 나왔는지에 관한 이야기입니다.

목표는 제가 입력한 거의 그대로입니다:

> create a Mario Kart clone called GoKart with all Mario Kart effects. I believe Godot 4 can do the Mario Kart effects, but I haven't built any of them yet: drift sparks and boost flames (GPUParticles3D), speed lines and boost blur (screen-space shaders, glow and tonemapping), item effects and tire trails (shaders plus ribbon meshes), kart movement (VehicleBody3D or custom arcade physics). Write unit tests and test the game frequently.

예산: 시간 제한 없음, 사이클 무제한. 모든 사이클에서 Agent! 안의 모델은 Claude Sonnet 5.5였습니다. 첫 커밋은 12:39에 들어왔습니다. 같은 날 오후 16:32에는 저장소에 커밋 33개, GDScript 파일 47개, GDScript와 셰이더 코드 약 5,500줄, 그리고 3,344개의 검사를 통과하는 유닛 테스트 스위트가 있었습니다. 이틀 뒤 0.0.2 태그 시점에는 커밋 126개, GDScript 파일 150개, 약 24,500줄, 검사 14,134개이고, 그 커밋 하나하나가 모두 에이전트가 작성한 것입니다. 전체는 GitHub의 [AgentiLoop/GoKart](https://github.com/AgentiLoop/GoKart)에 있습니다.

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
<img src="/gokart-0-0-2-sunset-speedway.png" alt="GoKart 0.0.2의 Sunset Speedway: 노을 하늘 아래 8대 중 3위로 1랩을 달리며 드리프트 중인 플레이어 카트와 Mario Kart 64 스타일 HUD. 왼쪽 아래 구석에 반투명 코스 맵, 그리고 둥근 금색-크림색 폰트로 순위, 랩, 속도가 표시됩니다." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>0.0.2의 Sunset Speedway: 무작위 주행 봇이 8대 중 3위로 드리프트 중. 두 번째 트랙은 첫날 사이클 12에서 타이틀 메뉴와 함께 추가되었습니다. 교통 차량, 벽 너머의 건물, HUD는 이틀 뒤에 왔습니다.</figcaption>
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

이것이 올바른 동작입니다. 목표는 "조향감이 나쁘다"와 "벽이 깜빡인다"였고, 어떤 헤드리스 테스트도 그 목표를 닫을 수 없습니다. 오토파일럿에는 반복 상한이 없어서, 영원히 확인만 계속했을 것입니다. 세션은 사이클 8 이후 끝났고, GoKart에 다음으로 필요한 것은 또 한 번의 사이클이 아니라 플레이테스트였습니다. 그날 저녁 저장소에 0.0.1 태그를 달고 macOS, Windows, Linux용으로 내보냈습니다.

## 이틀 뒤: 한 저장소에 오토파일럿 두 개

10월 3일, 저는 다른 종류의 목표를 들고 돌아왔습니다. 기능 목록이 아니라 참조 대상입니다:

> keep building GoKart to resemble Mario Kart Nintendo 64 version. search Mario Kart N64 or Mario Kart Nintendo 64 and keep improving, iterating, making GoKart better

그 다섯 번째 세션은 14:19에 시작해 28사이클을 돌았고, 거의 모든 사이클이 에이전트가 찾아보고 만든 Mario Kart 64의 요소 하나입니다. 2열 그리드의 8대 레이서, 난이도별 러버밴딩, 50cc / 100cc / 150cc와 미러 Extra 클래스, 서로 밀쳐내는 경량 / 중량 / 중량급 카트, 9/6/3/1 점수와 탈락 규칙이 있는 그랑프리, 고스트가 있는 타임 트라이얼, Big Donut, Block Fort, Skyscraper에서 풍선으로 겨루는 배틀 모드, 트리플 버섯과 골든 버섯, 가짜 아이템 박스, 바나나 묶음, 부끄부끄, 트리플 빨간 등껍질, 등껍질 방어, 부정 출발, 출발 신호와 랩 표지판을 든 쥬게무, Dusty Canyon이라는 네 번째 코스, 건널목이 있는 칼리마리 사막 기차, 키노피오 하이웨이 교통 차량, 몬티 두더지, 눈사람, 펭귄, 셔벗 랜드 얼음, 테마별 길가 풍경, 슬립스트림, 점프 램프, 홉-앤-토글 파워슬라이드, 그리고 코드의 스텝 패턴에서 렌더링한 코스별 칩튠 루프.

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-train.png" alt="GoKart 0.0.2의 Dusty Canyon: 사막 하늘 아래, 증기 기관차가 도로를 가로질러 지나가는 동안 건널목에서 기다리는 플레이어 카트와 선로 옆의 X자 건널목 표지판." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>네 번째 코스 Dusty Canyon과 칼리마리 사막 스타일 기차. CPU 카트는 차단된 건널목에서 멈춰 기다리고, 그러지 않은 카트는 공중으로 튕겨 나갑니다.</figcaption>
</figure>

네 시간 뒤인 18:25, 저는 두 번째 탭을 열고 같은 저장소에서 더 좁은 목표로 두 번째 오토파일럿을 시작했습니다:

> the menus are not Mario Kart Quality and neither is the title shot. and there is over use of black outlines on text everywhere. see Mario Kart 64 screenshots and images on the web and make better menus. focus only on the menus / screens and title shot for GoKart. make conscious decisions. do not conflict with previous /auto working on the application

그래서 18:25부터 자정까지 에이전트 두 개가 같은 작업 트리에 커밋하고 있었습니다. 메뉴 세션은 타이틀 화면을 다시 만들었습니다. 날아 들어와 튕기는 아치형 그라데이션 로고, 코스마다 그림이 옆에 붙은 선택 화면, 고른 코스의 라이브 플라이오버, 불 켜진 바가 있는 옵션 줄, 회전하는 카트 초상과 금색 커서, 코스 인트로 플라이오버, 일시정지 화면, 줄이 하나씩 차례로 미끄러져 들어오는 결과 보드, 그리고 게임의 모든 8픽셀 검은 외곽선을 대체한 그림자 있는 둥근 금색-크림색 텍스트의 공통 팔레트. 23사이클을 돌고 23:54에 목표 달성을 선언했습니다.

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-select.png" alt="GoKart 0.0.2 선택 화면: 위에 GOKART 로고, 왼쪽에는 코스 이름마다 작은 그림이 붙고 고른 줄에 불이 켜진 코스 목록, 오른쪽에는 구석에 맵 윤곽이 있는 코스의 라이브 화면, 랩 수, CPU, 엔진 클래스, 카트 무게, 모드를 위한 옵션 알약 줄들, 그리고 작은 초상 창에서 회전하는 플레이어의 카트가, 어둡게 처리된 어트랙트 데모 위에 모두 표시됩니다." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>메뉴 세션 이후의 선택 화면. 코스 그림, 코스의 라이브 플라이오버, 고른 것에 불이 켜지는 알약 줄로 나열된 모든 옵션, 그리고 초상 창에서 회전하는 카트.</figcaption>
</figure>

"충돌하지 말 것"이라는 한 줄이 실제로 일을 했습니다. 로그는 두 세션이 서로를 피해 일하는 기록으로 가득합니다. 메뉴 세션은 "다른 세션이 진행 중인 펭귄 작업"이 자기 테스트 실행에 섞이지 않도록 HEAD에서 깨끗한 `git worktree`를 만들어 검증했고, 제가 요청하자 한 세션이 다른 세션의 반쯤 끝난 기능을 마무리했으며, 다른 탭의 편집이 같은 트리에 놓여 있었기 때문에 `git add -A` 대신 파일 하나씩 스테이징해서 커밋했습니다. 깔끔하지는 않았지만 잃은 것은 없었고, 스위트는 그날 밤 통과 14,134개, 실패 0개로 끝났습니다.

기능 세션의 로그는 3분 뒤인 23:57에 "Session ended — Stop All"로 끝납니다. 바로 뒤에 Agent! 에 남긴 제 메모(에이전트가 다음 체크포인트 커밋 메시지로 저장했습니다)는, Stop All이 모든 탭이 아니라 눌린 탭만 멈춰야 한다는 것이었습니다. 오토파일럿 두 개가 돌아가고 있을 때, 둘 다 멈추는 버튼 하나는 잘못된 버튼입니다.

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-snowmen.png" alt="GoKart 0.0.2의 Frosty Peaks: 짙은 남색 황혼 하늘 아래, 눈처럼 하얀 도로를 가로질러 엇갈린 줄로 서 있는 눈사람 밭 입구의 플레이어 카트. 눈사람마다 빨간 목도리, 실크해트, 당근 코가 있습니다." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Frosty Peaks의 눈사람 밭. 하나를 들이받으면 눈사람은 눈으로 흩어지고 카트는 공중으로 튕겨 나갑니다. CPU 카트는 40미터 앞을 내다보며 줄 사이를 빠져나갑니다.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-penguins.png" alt="GoKart 0.0.2의 Frosty Peaks: 플레이어 카트 앞의 긴 스위퍼 구간, 연한 청백색 얼음 위를 배로 미끄러지는 펭귄." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Frosty Peaks의 셔벗 랜드 스타일 얼음과 펭귄. 얼음 위에서는 앞머리는 돌아가지만 카트는 가던 방향으로 계속 미끄러집니다. 펭귄은 가장자리까지 뒤뚱거리다가 엎어져 다시 미끄러져 돌아옵니다.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-traffic.png" alt="GoKart 0.0.2의 Sunset Speedway: 노을 하늘 아래, 도로의 두 차선에서 헤드라이트를 켠 버스와 박스 트럭 뒤에 갇힌 플레이어 카트." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Sunset Speedway의 키노피오 하이웨이 교통 차량: 헤드라이트를 켠 승용차, 버스, 박스 트럭, 탱크로리, 그리고 벽 너머에 불 켜진 창문 띠가 있는 건물들.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-gp-results.png" alt="GoKart 0.0.2 그랑프리 결과 보드: 금색 테두리의 남색 패널에, 왼쪽에는 레이스 결과, 오른쪽에는 컵 순위가 레이서마다 한 줄씩 색상 견본, 금·은·동 순위, 시간, 점수와 함께 표시되고, 플레이어의 줄은 불 켜진 금색 바 위에 있으며, 아래에 트로피가 있습니다." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>그랑프리 결과 보드: 레이스 결과와 컵 순위가 나란히 놓이고, 줄이 하나씩 차례로 틱 소리와 함께 미끄러져 들어오며, 아래에 트로피가 있습니다.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-battle.png" alt="GoKart 0.0.2 배틀 모드: 배틀 아레나의 출발 패드 위에 선 카트 네 대, 각각 풍선 세 개가 매달려 있고, 머리 위에는 쥬게무의 출발 신호." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>배틀 모드: 카트 네 대, 각각 풍선 세 개. 아이템 피격, 용암, 지붕 가장자리, 스타 접촉, 중량급 밀치기가 풍선을 터뜨리고, 풍선이 하나도 남지 않은 카트는 미니 폭탄 카트가 됩니다.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-dusty-canyon.png" alt="GoKart 0.0.2의 Dusty Canyon: 사막 도로에서 8대 중 5위로 1랩을 달리는 플레이어 카트와 Mario Kart 64 스타일 HUD." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>무작위 주행 봇이 찍은 Dusty Canyon, 8대 중 5위. 사막 스위퍼, 헤어핀, 왼쪽 S자, 오아시스 물 구간 두 곳, 기차, 그리고 첫 직선 구간의 점프 램프.</figcaption>
</figure>

## 이 스크린샷에 대하여

찍은 것은 Agent! 이고, 제가 아니며, 손으로 찍은 것도 아닙니다. 첫 버전 때 무작위 주행 스크린샷 세 장을 요청했더니, 70줄짜리 `tools/random_drive.gd`를 작성했습니다. 흔들리는 차선 오프셋으로 도로를 따라가고, 무작위로 드리프트를 터뜨리고, 들고 있는 아이템을 무작위 순간에 발사한 뒤, 물리 프레임 몇백 개마다 한 프레임을 저장합니다. 위의 레이스 장면 두 장은 그 봇의 프레임입니다. 나머지는 각 기능과 함께 들어온 샷 도구에서 나왔습니다. `menu_shot.gd`, `train_shot.gd`, `traffic_shot.gd`, `snowman_shot.gd`, `penguin_shot.gd`, `hud_shot.gd`, `battle_shot.gd`는 각각 씬을 연출하고, 알맞은 프레임을 기다렸다가 저장합니다. 이번 업데이트를 위해 모두 `v0.0.2` 태그를 체크아웃한 깨끗한 워크트리에서 실행했으므로, 커밋되지 않은 것은 어떤 사진에도 없습니다. Agent! 는 여전히 결과를 볼 수 없으므로, 도구들이 대신 픽셀을 샘플링합니다. 얼음 샷은 전방 얼음 위 도로 색을 아스팔트와 대비해 출력하고, 일시정지 샷은 1초 동안 패널 밖에서 아무것도 움직이지 않았음을 증명하며, 게시 전에 위의 열 장 사진 모두에서 순수 검은색 픽셀을 세게 했습니다. 각각 0개였습니다. [GoKart README](https://github.com/AgentiLoop/GoKart#screenshots)에 더 있습니다.

## 직접 해보기 전에 드리고 싶은 말

- **git 안에서 실행하세요.** 오토파일럿에는 되돌리기가 없습니다. GoKart의 로그를 읽을 수 있는 이유는 모든 사이클이 커밋으로 끝났기 때문이고, 사이클이 한 번 엇나갔을 때도 잃은 것은 없었습니다.
- **운영 규칙을 목표에 넣으세요.** "셸에 시간 제한을 걸어라"는 일회성 메시지보다 목표의 일부일 때 더 잘 작동했습니다. 새 사이클은 매번 목표를 다시 읽기 때문입니다.
- **눈을 요청할 것을 예상하세요.** 시각적이거나 느낌에 관한 것이라면, 루프는 거짓말하는 대신 정직하게 멈춥니다. 세션 사이에 플레이테스트 시간을 잡고, 메모를 다음 목표로 다시 넣어주세요.
- **Stop All은 워크플로의 일부**이지 실패가 아닙니다. GoKart의 첫 세 세션은 모두 그렇게 끝났습니다.
- **한 저장소에 오토파일럿 두 개도 됩니다. 서로의 존재를 알려준다면요.** "이전 /auto와 충돌하지 말 것"이 두 번째 목표에 들어갔고, 두 세션 모두 서로의 길에서 비켜 있으려고 실제로 애썼습니다. 코드의 영역을 따로 나눠 주고, 당분간은 하나를 멈추면 다른 하나도 함께 멈춘다는 점을 감안하세요.

## 그래서 좋은 건가요?

저장소를 읽고, 커밋을 세고, 오토파일럿 로그를 찾은 뒤의 Agent! 에게 그 질문을 던졌습니다. 126개 커밋 전부가 에이전트가 작성한 것이고 사람이 쓴 것은 하나도 없으며, `.agent/autopilot/progress.md`는 사이클 23을 넘어갑니다. 편집하지 않은 답변:

> 무엇을 원하느냐에 따라 다릅니다. 오토파일럿이 할 수 있는 일의 쇼케이스로서는 인상적입니다. 스물세 번이 넘는 사이클이 코스 네 개, 아이템, AI 레이서, 그랑프리, 타임 트라이얼, 배틀 모드, 절차적 음악과 사운드를 가져온 에셋 하나 없이 만들어 냈고, 그것을 상세히 문서화한 README까지 있습니다. 목표 문장 하나에서 나온 것치고는 작동하는 소프트웨어가 상당히 많습니다.

또한 과정에서 사람이 검토한 적이 없으므로 품질은 에이전트 자신의 검증 로그로 판단되었다는 것과, 직접 플레이하거나 코드를 감사하지 않았으므로 실제로 얼마나 잘 플레이되는지는 말할 수 없다는 단서를 덧붙였습니다. 로그가 스스로 도달한 결론과 같습니다. 다음 단계는 플레이테스트입니다.

## GoKart 0.0.2

Godot 없이도 해볼 수 있습니다. [GoKart 0.0.2](https://github.com/AgentiLoop/GoKart/releases/tag/v0.0.2)는 같은 저장소에서 내보낸 두 번째 패키지 릴리스로, [0.0.1](https://github.com/AgentiLoop/GoKart/releases/tag/v0.0.1)에서 87개 커밋 뒤입니다:

- **macOS** 유니버설 (Apple Silicon 및 Intel), Developer ID로 서명하고 Apple에서 공증
- **Windows** x86_64
- **Linux** x86_64 및 arm64

각 다운로드는 게임 데이터가 내장된 단일 독립 실행 바이너리이며, 받은 파일을 확인하고 싶다면 릴리스 페이지에 `SHA256SUMS.txt`가 있습니다. Windows 빌드는 서명되지 않았으므로 SmartScreen 경고가 뜰 수 있습니다. 이 글에서 0.0.1에 없던 모든 것이 0.0.2에 있습니다. 배틀 모드, 타임 트라이얼, 4코스 컵, 엔진 및 중량 클래스, 새 아이템, 쥬게무, 기차, 교통 차량, 두더지, 눈사람, 펭귄, 얼음, 풍경, 슬립스트림, 점프 램프, 코스 음악, 새 타이틀 및 선택 화면, 코스 인트로, 일시정지 화면, 그리고 새로 스타일링한 HUD. 전체 목록은 릴리스 노트에 있습니다.

오토파일럿이 포함된 Agent! 1.1.87은 [릴리스 페이지](https://github.com/AgentiLoop/Agent/releases/latest)와 Homebrew에 있습니다. 소스에서 GoKart를 실행하고 싶다면 Godot 4.4 이상이 필요합니다: `git clone https://github.com/AgentiLoop/GoKart.git && cd GoKart && godot --path .`
