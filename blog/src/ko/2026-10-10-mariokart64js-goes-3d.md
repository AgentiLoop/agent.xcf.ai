---
title: MarioKart64JS, 3D가 되다: Wii 카트, 3D 타이틀 화면, 그리고 결승 후 플라이오버
description: Mario Kart 64는 레이서를 평면 스프라이트로 그립니다. MarioKart64JS에서 3을 누르면 Lakitu까지 포함해 모든 카트가 3D 모델로 바뀌고, 실제 그림자, 새로 만든 3D 타이틀 화면, 그리고 결승 후 카트 주위를 날아다니는 카메라가 더해집니다. 3D 모드가 어떻게 만들어졌는지 스크린샷과 함께 소개합니다.
tags: Showcase, JavaScript
---
<figure style="margin:2rem 0">
<img src="/mk64js-3d-title.jpg" alt="MarioKart64JS의 3D 타이틀 화면: Mario Kart 64 로고 아래에서 Wario, Bowser, Mario, Peach, Toad가 3D 카트를 타고 카메라를 향해 달려온다." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>3D 타이틀 화면. 원작은 평면 그림 한 장입니다. 여기서는 하늘, 언덕, 도로를 Three.js로 만들었고, 다섯 명의 드라이버는 카메라를 향해 달려오는 3D 카트입니다.</figcaption>
</figure>

[지난 MarioKart64JS 글](/blog/mariokart64js-from-scratch-in-javascript/)은 Mario Kart 64를 최대한 똑같이 재현하는 이야기였습니다. 코스 지오메트리, 스프라이트, 음악은 카트리지에서 가져오고, 원작의 C 코드가 하던 일을 새로운 JavaScript가 하는 것이었죠. 이번 글은 그 반대 방향에 관한 것입니다. 키 하나, **3**을 누르면 N64에는 없었던 3D 모드가 켜집니다.

## 스프라이트가 모델이 되다

Mario Kart 64의 레이서는 모델이 아닙니다. 각 드라이버는 미리 렌더링된 64×64 프레임 321장으로 이루어져 있고, 게임은 카메라 각도에 맞는 프레임을 골라 씁니다. MarioKart64JS도 이 프레임을 그리며, 지금도 기본값은 그렇습니다.

3D 모드는 이 스프라이트를 Mario Kart Wii의 스탠더드 카트(Standard Kart) 모델로 바꿉니다. 모델은 Collada 익스포트 파일에서 가져온 것으로, `tools/build-wii-karts.py`가 프로젝트에 배치합니다. 시작은 10월 9일 저녁의 단순한 테스트 하나였습니다. 21:22에 3 키를 누르면 플레이어 아래에 Mario가 탄 빨간 스탠더드 카트가 놓였습니다. 22:02에는 여덟 명의 드라이버 모두가 카트를 갖게 되었고, Wii의 체급에 따라 나뉘었습니다. Toad는 소형 카트, Mario, Luigi, Peach, Yoshi는 중형, D.K., Wario, Bowser는 대형이며, 각각 고유한 도색을 하고 있습니다.

그 사이 작업의 대부분은 모델 로더가 잘못 처리하는 작은 부분들이었습니다.

- **눈.** 각 눈 텍스처에는 눈이 하나만 있습니다. Wii에서는 텍스처 행렬이 이를 두 번 반복하고, 샘플러가 미러링해 한 쌍으로 만듭니다. Three.js의 ColladaLoader는 둘 다 버리기 때문에 눈 하나가 얼굴 전체에 늘어나 있었습니다. `kart3d.js`가 캐릭터별로 반복과 미러링을 되살립니다.
- **타이어.** 뒷바퀴는 앞바퀴 메시를 확대한 것입니다. 크기와 차축 위치는 각 카트의 조립된 메뉴 모델에서 측정했고, 그 결과 뒷바퀴가 1.29배 커지고 Wii와 같은 위치에 놓였습니다.
- **좌석.** 각 드라이버에게 좌석 위치를 지정해, 좌석 위에 떠 있지 않고 뒤로 젖혀진 좌석에 앉도록 했습니다.

Agent!는 그림을 볼 수 없기 때문에 대신 숫자로 모델을 확인했습니다. 각 카트의 ASCII 측면도, 후면도, 상면도, 12방향 턴테이블 시트, 그리고 각 드라이버의 손과 핸들 사이의 측정 간격을 사용했습니다.

## 3D로 레이스하기

<figure style="margin:2rem 0">
<img src="/mk64js-3d-race-mario.jpg" alt="3D 모드의 MarioKart64JS, 3D 카트로 Mario Raceway를 달리는 모습." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>3D 모드의 Mario Raceway. 레이스의 모든 카트가 3D 모델이며, 각자 자기 캐릭터의 스탠더드 카트를 타고 있습니다.</figcaption>
</figure>

레이스 중에 3을 누르면 내 카트뿐 아니라 트랙 위의 모든 카트가 바뀌고, 다시 누르면 스프라이트로 돌아옵니다. 이와 함께 두 가지가 더 바뀝니다.

**그림자.** 스프라이트 아래에는 납작한 덩어리 그림자가 있습니다. 3D 카트는 코스 위에 진짜 섀도 맵 그림자를 드리웁니다. 여기에는 요령이 필요했습니다. 코스는 그림자를 받을 수 없는 비조명(unlit) 머티리얼로 그려지기 때문에, 코스 표면을 복제한 투명한 섀도 캐처를 만들어 그림자가 떨어지는 곳에만 보이게 했습니다.

**Lakitu.** 심판은 Mario Kart Wii의 Lakitu(`src/lakitu3d.js`)가 됩니다. 팔은 모델 자체의 본을 통해 포즈를 잡습니다. 한 손은 낚싯대를 들고, 다른 손은 깃발을 흔듭니다. 출발 신호등, 랩 보드, 역주행 표지판은 낚싯대 바늘에 매달려 있고, 원작 스프라이트의 애니메이션 프레임이 여전히 타이밍을 제어하기 때문에 빨강, 빨강, 파랑 카운트다운이 늘 그랬던 때에 켜집니다.

<figure style="margin:2rem 0">
<img src="/mk64js-3d-race-koopa.jpg" alt="3D 모드의 MarioKart64JS, Koopa Troopa Beach를 달리는 모습." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>10월 10일 대부분을 보낸 Koopa Troopa Beach. 3D 카트의 차체가 올라타는 법을 배워야 했던 것이 바로 이곳의 점프대입니다.</figcaption>
</figure>

3D 카트에는 스프라이트에 없던 차체도 있습니다. 벽에 대해서는 각 차축 위에 원이 하나씩 있는 캡슐이며, 강체로서 움직이고 회전합니다. 여기에는 부작용이 있었습니다. Koopa Troopa Beach에서는 앞쪽 원이 카트 중심보다 먼저 경사로의 턱에 닿았고, 턱의 뒷면이 카트를 점프대에서 튕겨냈습니다. 수정 방법은 각 차축을 그 아래 지면과 따로 검사하는 것이었습니다. 이후의 커밋에서는 정면 충돌 시 벽이 플레이어 카트의 방향을 돌리지 않도록 했습니다. Mario Kart 64에서 벽은 카트의 움직임을 반사할 뿐, 향하는 방향을 바꾸지는 않기 때문입니다.

<figure style="margin:2rem 0">
<img src="/mk64js-3d-race-royal.jpg" alt="3D 모드의 MarioKart64JS, Royal Raceway를 달리는 모습." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>3D 모드의 Royal Raceway.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-3d-race-bowser.jpg" alt="3D 모드의 MarioKart64JS, Bowser's Castle을 달리는 모습." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Bowser's Castle. 폭이 5인 통로에서 캡슐이 복도를 가로질러 끼지 않도록 막아야 했습니다.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-3d-race-rainbow.jpg" alt="3D 모드의 MarioKart64JS, Rainbow Road를 달리는 모습." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>3D 카트로 달리는 Rainbow Road.</figcaption>
</figure>

## 3D 타이틀 화면

Mario Kart 64의 타이틀 배경은 320×240 크기의 평면 그림 한 장입니다. 하늘, 언덕, 도로, 다섯 명의 드라이버가 모두 그려져 있습니다. 타이틀에서 3을 누르면 이를 새로 만듭니다(`src/title3d.js`). 하늘, 언덕, 도로는 Three.js로 만들고, 드라이버는 레이스와 같은 3D 카트입니다.

배치는 원래 그림을 따릅니다. Wario는 왼쪽 앞, 그 뒤에 Bowser, Mario는 오른쪽 앞, 그 뒤에 Peach가 있고, Toad는 오른쪽 커브를 빠져나오고 있습니다. 각 카트는 화면상의 영역이 원화 속 해당 드라이버의 영역과 약 10픽셀 이내로 맞도록 배치되었습니다. 카메라는 그들 앞의 도로 위에 낮게 자리 잡고 64°의 광각 렌즈를 쓰며, 도로가 아래로 스크롤되기 때문에 카트들이 곧장 나를 향해 달려오는 것처럼 보입니다. 체크무늬 깃발, 로고, PUSH START, 저작권 표기는 여전히 원작 타이틀의 2D 오버레이입니다.

그 뒤의 메뉴에도 어울리는 배경이 생겼습니다. 타이틀에서 3D를 켜면 4× 텍스처 단계로도 전환되고, 다시 3을 누를 때까지 레이스는 3D로 시작합니다.

<figure style="margin:2rem 0">
<img src="/mk64js-3d-game-select.jpg" alt="3D 모드 배경이 적용된 MarioKart64JS 게임 선택 화면." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>3D 모드 배경이 적용된 게임 선택 화면.</figcaption>
</figure>

## 결승 후 플라이오버

결승선을 통과하면 Mario Kart 64는 카메라를 짧은 시네마틱 연출에 넘깁니다. MarioKart64JS는 여기서 게임의 카메라 코드(디컴파일 코드의 `PLAYER_CINEMATIC_MODE`와 시네마틱 샷 함수들)를 따릅니다. 카메라가 카트 앞쪽으로 돌아가 결승선을 통과하는 모습을 지켜본 뒤, CPU 드라이버가 내 카트를 넘겨받는 동안 여러 샷 사이를 전환합니다. 이 시퀀스는 노즈 오빗, 길가, 하이 크레인, 길가, 로우 테일 샷, 길가 순으로 반복됩니다. 소스 주석에 적힌 단서가 하나 있습니다. 샷의 길이와 거리는 ROM의 테이블에서 가져온 것이 아니라 눈대중으로 조정한 값입니다.

추적 샷은 카트 진행 방향을 강하게 평활화한 사본을 따라갑니다. 이것이 없으면 AI의 작은 조향 보정 때문에 카메라가 카트 주위에서 흔들려, 카트가 덜컥거리며 회전하는 것처럼 보였습니다. 3D 카트에서는 이 샷들이 모델을 가장 잘 보여 줍니다. 카메라가 마침내 카트를 정면과 측면에서 보게 되기 때문입니다.

<figure style="margin:2rem 0">
<img src="/mk64js-3d-flyover-front.jpg" alt="Mario Raceway의 결승 플라이오버: Mario의 3D 카트 앞에 있는 카메라가 카트를 돌아보고 있다." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Mario Raceway의 노즈 샷. 카메라가 카트 뒤에서 앞쪽으로 돌아 들어가 카트 앞에서 함께 달립니다.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-3d-flyover-crane.jpg" alt="Mario Raceway의 결승 플라이오버: 카트 뒤쪽 높은 곳에서 도로를 내려다보는 하이 크레인 샷." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>카트의 뒤쪽 위에서 도로를 내려다보는 하이 크레인 샷.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-3d-flyover-roadside.jpg" alt="Royal Raceway의 결승 플라이오버: 카트가 지나가는 동안 길가에 놓인 카메라." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Royal Raceway의 길가 샷. 카메라가 앞쪽 길가에 서서 카트가 지나갈 때까지 머무릅니다.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-3d-flyover-low.jpg" alt="Koopa Troopa Beach의 결승 플라이오버: 카트 어깨 옆의 낮은 카메라." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Koopa Troopa Beach의 로우 테일 샷. 카트의 한쪽 어깨 옆에서 찍었습니다.</figcaption>
</figure>

## 스크린샷은 어떻게 찍었나

이 글의 모든 그림은 헤드리스 Chrome에서 1280×960으로 찍었습니다. 타이틀과 게임 선택 화면은 플레이어와 똑같이 타이틀에서 3을 눌러 찍었습니다. 레이스는 3D 모드를 켠 상태로 저장해 자동 주행으로 진행했고, 플라이오버는 플레이어를 마지막 랩의 마지막 구간에 두고 결승 후 0.7초마다 프레임을 하나씩 찍어 담았습니다. Agent!는 측정을 통해 프레임을 골랐습니다. 카트에 대한 카메라의 위치로 각 프레임이 어떤 샷인지 알아냈고, 픽셀 통계로 어둡거나 디테일이 적은 프레임을 걸러냈습니다. 지난 글과 마찬가지로, 그림을 직접 보지는 않았습니다.

## 직접 해 보기

[AgentiLoop/MarioKart64JS](https://github.com/AgentiLoop/MarioKart64JS)를 클론하고 `npm install && npm run dev`를 실행한 뒤 `http://localhost:5173`을 열고, 타이틀 화면이나 레이스 중에 **3**을 누르세요. 웹 빌드에도 3D 카트, Lakitu, 3D 타이틀이 포함되어 있습니다. 배치된 모델은 `public/wii/`에 있으며, `tools/build-wii-karts.py`와 `tools/build-wii-lakitu.py`가 Collada 파일에서 모델을 배치한 스크립트입니다.

*MarioKart64JS는 AI가 게임을 복제하는 데 어디까지 갈 수 있는지 시험하기 위한 팬 연구 프로젝트입니다. Mario Kart 64와 Mario Kart Wii는 © Nintendo이며, 그 에셋은 Nintendo의 소유입니다. 이 프로젝트는 Nintendo와 제휴하거나 Nintendo의 승인을 받은 것이 아닙니다.*
