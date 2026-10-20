---
title: AgentiLoop Racing, Prototype III: 브라우저에서 즐기는 F1 시뮬레이터
description: AgentiLoop Racing은 Agent!가 Three.js로 만든, 브라우저에서 실행되는 오픈휠 레이싱 시뮬레이터입니다. 240 Hz 물리 엔진, 18개의 실제 서킷, AI 드라이버, 피트 스톱, 타이어 컴파운드, 연료, ERS, DRS를 갖추고 있습니다. f1.gokart.games에서 플레이할 수 있습니다.
tags: Showcase, JavaScript
---
<figure style="margin:2rem 0">
<img src="/agentiloop-racing-og.jpg" alt="AgentiLoop Racing: 브라우저 시뮬레이터에서 트랙을 달리는 오픈휠 레이스카." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>AgentiLoop Racing, Prototype III. 그리드 위의 모든 차는 2026년형 RB22 모델이며, 각자의 컬러와 스폰서 이름으로 다시 도색되어 있습니다.</figcaption>
</figure>

**지금 바로 플레이: [f1.gokart.games](https://f1.gokart.games).** 다운로드도, 설치도 필요 없습니다. WebGL을 지원하는 브라우저만 있으면 되고, 키보드나 Xbox(또는 기타 표준) 컨트롤러로 플레이할 수 있습니다.

AgentiLoop Racing은 순수 JavaScript와 Three.js로 작성된 F1 스타일의 레이싱 시뮬레이터입니다. 첫 커밋은 결정론적인 4륜 차량 모델로, 10월 16일 저녁에 들어갔습니다. 그로부터 3일, 109개의 커밋이 지난 지금은 18개의 실제 서킷에서 AI 풀 필드와 레이스를 펼칩니다. 피트 스톱, 타이어 컴파운드, 연료, ERS와 DRS, 물리 엔진으로 만들어 내는 엔진 사운드, 그리고 미러에 뒤따르는 차들이 비치는 콕핏 카메라도 있습니다. 이 모든 것을 Agent!가 작고 테스트된 커밋을 하나씩 쌓아 가며 작성했습니다.

먼저 솔직한 꼬리표를 하나 붙여 둡니다. README에 적힌 것과 같은 내용입니다. 이것은 **프로토타입이며, 검증된 Formula 1 시뮬레이터가 아닙니다**. 차량의 파라미터는 설명을 위한 가정일 뿐, 실제로 측정한 F1 데이터가 아닙니다.

## 물리가 먼저

이 프로젝트는 물리 테스트베드로 시작했고, 3D는 그다음이었습니다. `physics.mjs`는 차량을 고정된 **240 Hz**로 진행시킵니다. 각 바퀴는 고유한 관성과 슬립을 가지며, 각 타이어에는 최대 그립에서 미끄러짐까지 이어지는 그립 특성, 슬립 앵글 완화, 온도, 마모가 있습니다. 서스펜션 위의 차체는 공기역학적 하중을 받아 롤, 피치, 스쿼트를 하며, 이는 3D 차량에서도 눈으로 확인할 수 있습니다. 기어박스는 자동 또는 패들 시프트이며, 벽을 마주 보고 멈춰 버렸을 때를 위한 보호 장치가 있는 후진 기어도 있습니다.

파워 유닛도 모델링되어 있습니다. 연료는 실제 질량으로 실려 있어서, 연료를 태울수록 차가 가벼워집니다. 하이브리드는 100 km/h 이상에서 최대 120 kW를 랩당 4 MJ 한도 안에서 방출하고, 제동 시에 에너지를 회수합니다.

테스트 스위트는 Node에 내장된 테스트 러너만 사용합니다. 현재 `node --test`는 158개의 테스트를 실행하며, 모두 통과합니다. 풀 스로틀 상태의 차가 절대로 벽을 뚫고 지나가지 않는지, 3D 모델이 타이어와 플랭크로만 지면에 닿는지 같은 것들을 확인합니다.

## 18개의 실제 서킷

<figure style="margin:2rem 0">
<img src="/agentiloop-racing-monza.jpg" alt="AgentiLoop Racing: 몬차에서 AI 필드와 펼치는 레이스." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>몬차에서의 레이스. 타이밍 박스, 순위표, 미니맵이 레이스 중 실시간으로 표시됩니다.</figcaption>
</figure>

가상의 스타디움 테스트 트랙 외에도 바레인부터 마이애미까지, 몬차, 실버스톤, 스파, 모나코를 포함한 18개의 실제 서킷이 있으며, 레이아웃은 실제 차량의 위치 데이터로 만들었습니다. 나머지는 실제 데이터로 조정했습니다.

- **DRS 존**은 2024년 레이스 텔레메트리(OpenF1)에서 가져왔습니다. 드라이버들이 실제로 플랩을 열고 닫은 위치입니다. 모나코는 피트 스트레이트에 존이 하나뿐입니다.
- **그립은 실제 코너 속도에 맞춰 보정했습니다.** 18개 서킷 전체에서 오토파일럿의 랩과 실제 레이스 최고 랩 사이의 차이가 17.9%에서 5.8%로 줄었습니다. 모나코에서는 오토파일럿의 랩이 84.2초에서 74.4초가 되었고, 실제 기록은 73.9초입니다.
- **좁은 코너는 넓혀서** 최소 반경을 15 m로 만들어, 차들이 모나코의 생 드보트를 돌아 나갈 수 있게 했습니다.
- **모든 서킷에 피트 레인이 있습니다.** 스타트/피니시 스트레이트 옆에 있으며, 제한 속도는 80 km/h이고 차마다 피트 박스가 있습니다.

<figure style="margin:2rem 0">
<img src="/agentiloop-racing-monaco.jpg" alt="AgentiLoop Racing: 모나코에서의 레이스." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>AI 필드와 함께 달리는 모나코.</figcaption>
</figure>

## AI와 레이스

실제 서킷은 솔로 타임 트라이얼로 시작합니다. **O**를 누르거나 URL에 `?race`를 붙이면 필드와 레이스를 할 수 있습니다. 스타트는 다섯 개의 빨간 신호등이 1초에 하나씩 켜지고, 무작위로 잠시 기다린 뒤 꺼집니다. 0.5 m 넘게 일찍 움직이면 5초 부정 출발 페널티입니다. 신호등이 켜져 있는 동안 **1–5** 키를 누르면 해당 그리드 위치의 차에 탈 수 있습니다.

AI 차들은 레이싱 라인을 따라 달리고, 스트레이트에서는 서로 슬립스트림을 타다가 빠져나오며, 감지 지점에서 1초 이내에 있으면 DRS를 쓰고, 제동 구간에서는 안쪽으로 파고듭니다. 추월을 조정한 커밋에서는 18개 서킷 전체의 3랩 레이스에서 추월이 16회에서 34회로 늘었고, 접촉은 8회에서 0회가 되었습니다. 배리어에 걸려 꼼짝 못 하게 된 차는 후진 기어를 넣고, 다른 차와 벽을 확인한 경로를 따라 빠져나온 다음 다시 레이스에 합류합니다.

레이스 규칙도 적용됩니다. 완주자는 모두 두 가지 타이어 컴파운드를 사용해야 하므로, 한 번은 피트에 들어가지 않으면 실격입니다. **B**를 누르면 크루에게 소프트, 미디엄, 하드를 요청할 수 있습니다. 피트 레인에서 과속하면 +5초입니다.

모든 세션은 오토파일럿으로 시작하므로, 직접 조작을 넘겨받기 전까지는 차가 알아서 달립니다. **P**를 누르거나, 게임패드를 건드리거나, 기어를 바꾸면 그때부터는 당신의 차입니다.

## 차량과 콕핏

그리드 위의 모든 차는 Tyler_Dave가 만든 2026년형 RB22 모델(CC BY 4.0, Sketchfab 출처)을 사용합니다. 로드 시점에 `rb22.mjs`가 각 차의 컬러로 다시 도색하고, 프로젝트의 스폰서 이름과 레이스 번호를 차체에 투영합니다. 가까이에서는 모델의 각 부분이 세분화되고 부드럽게 처리되며, 멀리 있을 때는 디테일이 낮은 버전이 쓰입니다.

**C**를 누르면 콕핏 시점이 됩니다. 드라이버의 눈은 서스펜션 위의 차체에 실려 있어서 롤, 피치, 상하 움직임에 따라 시야가 움직이고, 머리도 G-포스에 따라 조금씩 움직입니다. 미러는 각 유리에 반사된 장면을 렌더링하며, 자신의 뒷타이어는 제외되어 트랙과 뒤따르는 차들이 보입니다.

사운드 역시 물리 엔진에서 합성됩니다. 회전수를 따라가는 V6 점화음, 터보의 휘파람 소리, 슬립에서 나오는 타이어 스키드음, 그리고 속도가 올라갈수록 커지는 바람 소리입니다.

<figure style="margin:2rem 0">
<img src="/agentiloop-racing-spa.jpg" alt="AgentiLoop Racing: 스파-프랑코샹에서의 타임 트라이얼." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>스파 타임 트라이얼.</figcaption>
</figure>

## 영상으로 보기

<figure style="margin:2rem 0">
<div style="position:relative;padding-top:56.25%;border-radius:20px;overflow:hidden">
<iframe src="https://www.youtube-nocookie.com/embed/2RluAIH3iQw?rel=0&amp;modestbranding=1&amp;color=white" title="AgentiLoop Racing — F1 simulator built with AgentiLoop.ai in Three.js" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="position:absolute;inset:0;width:100%;height:100%;border:0"></iframe>
</div>
</figure>

## 직접 해 보기

- [몬차에서의 레이스](https://f1.gokart.games/?track=monza&race)
- [스파 타임 트라이얼](https://f1.gokart.games/?track=spa)
- [소프트 타이어로 달리는 스파 5랩 레이스](https://f1.gokart.games/?track=spa&race&laps=5&tyre=soft)

소스는 [AgentiLoop/F1](https://github.com/AgentiLoop/F1)에 있습니다. npm 의존성도 번들러도 없습니다. Three.js가 저장소에 포함되어 있으므로, 폴더에서 `python3 -m http.server`만 실행하면 로컬에서 돌려 볼 수 있습니다. 사이트 자체는 저장소를 정적 파일로 제공하는 Cloudflare Worker입니다.

*AgentiLoop Racing은 독립 프로젝트이며, Formula 1, FIA 또는 어떤 팀과도 관련이 없습니다. 3D 모델은 각자의 라이선스를 따릅니다. 저장소의 `models/CREDITS.md`를 참고하세요.*
