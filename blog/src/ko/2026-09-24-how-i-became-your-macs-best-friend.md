---
title: Agent!는 이렇게 시작됐습니다: 3월의 사흘
description: 3년 동안 모은 부품, 빠져 있던 루프 하나, 그리고 이틀도 안 되는 동안 177개의 커밋. git에서 바로 꺼낸 Agent!의 진짜 탄생 이야기.
tags: 기원, 역사
---
<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 380" role="img" aria-labelledby="lego-title lego-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="lego-title">장난감 블록으로 Mac을 만드는 친절한 로봇</title>
<desc id="lego-desc">웃는 얼굴의 파란 로봇이 빨강, 노랑, 초록, 파랑, 주황 장난감 블록으로 반쯤 만든 Mac 화면 위로 노란 블록을 들고 있습니다. 말풍선에는 '거의 다 됐어!'라고 쓰여 있습니다.</desc>
<rect width="760" height="380" rx="20" fill="#eef6ff"/>
<path d="M40 318H720" stroke="#8b684c" stroke-width="13" stroke-linecap="round"/>
<path d="M190 92l-6 26 40-26" fill="#fff"/>
<rect x="120" y="30" width="230" height="64" rx="22" fill="#fff" stroke="#b6c8e4" stroke-width="3"/>
<text x="235" y="72" text-anchor="middle" font-family="system-ui,sans-serif" font-size="26" font-weight="700" fill="#173452">거의 다 됐어!</text>
<path d="M140 270V310M210 270V310" stroke="#173452" stroke-width="7" stroke-linecap="round"/>
<path d="M250 200L318 146" stroke="#173452" stroke-width="7" stroke-linecap="round"/>
<rect x="100" y="150" width="150" height="120" rx="28" fill="#559ef5" stroke="#173452" stroke-width="4"/>
<path d="M175 150V124" stroke="#173452" stroke-width="5"/><circle cx="175" cy="115" r="10" fill="#efb943"/>
<circle cx="145" cy="192" r="13" fill="#fff"/><circle cx="205" cy="192" r="13" fill="#fff"/>
<circle cx="149" cy="193" r="5.5" fill="#173452"/><circle cx="209" cy="193" r="5.5" fill="#173452"/>
<path d="M148 228Q175 250 202 228" fill="none" stroke="#173452" stroke-width="6" stroke-linecap="round"/>
<g stroke="#173452" stroke-width="3">
<rect x="300" y="112" width="70" height="34" rx="4" fill="#efb943"/>
<rect x="311" y="102" width="16" height="10" rx="2" fill="#efb943"/><rect x="343" y="102" width="16" height="10" rx="2" fill="#efb943"/>
</g>
<g stroke="#173452" stroke-width="3">
<rect x="430" y="276" width="140" height="34" rx="4" fill="#9aa7b8"/>
<rect x="480" y="244" width="40" height="32" fill="#b8c3d1"/>
<rect x="400" y="210" width="70" height="34" rx="4" fill="#d94877"/>
<rect x="470" y="210" width="70" height="34" rx="4" fill="#4caf6e"/>
<rect x="540" y="210" width="70" height="34" rx="4" fill="#559ef5"/>
<rect x="610" y="210" width="70" height="34" rx="4" fill="#f08a3c"/>
<rect x="400" y="176" width="70" height="34" rx="4" fill="#efb943"/>
<rect x="470" y="176" width="70" height="34" rx="4" fill="#559ef5"/>
<rect x="540" y="176" width="70" height="34" rx="4" fill="#d94877"/>
<rect x="610" y="176" width="70" height="34" rx="4" fill="#4caf6e"/>
<rect x="400" y="142" width="70" height="34" rx="4" fill="#4caf6e"/>
<rect x="470" y="142" width="70" height="34" rx="4" fill="#f08a3c"/>
<rect x="540" y="142" width="70" height="34" rx="4" fill="#efb943"/>
<rect x="400" y="108" width="70" height="34" rx="4" fill="#559ef5"/>
<rect x="470" y="108" width="70" height="34" rx="4" fill="#d94877"/>
<rect x="540" y="108" width="70" height="34" rx="4" fill="#4caf6e"/>
<rect x="610" y="108" width="70" height="34" rx="4" fill="#efb943"/>
</g>
<rect x="610" y="142" width="70" height="34" rx="4" fill="none" stroke="#173452" stroke-width="3" stroke-dasharray="8 6"/>
<text x="190" y="354" text-anchor="middle" font-family="system-ui,sans-serif" font-size="21" fill="#173452">만드는 로봇.</text>
<text x="540" y="354" text-anchor="middle" font-family="system-ui,sans-serif" font-size="21" fill="#173452">Mac. 블록 하나만 더.</text>
</svg>
<figcaption>큰 것은 모두 작은 블록 더미에서 시작합니다. 비결은 다음에 어떤 블록이 올지 아는 것입니다.</figcaption>
</figure>

모든 앱에는 첫날이 있습니다. Agent!의 첫날은 수요일이었습니다. 바로 **2026년 3월 11일 오후 3시 7분**입니다. 몇 분인지까지 아는 건 git이 적어 두었기 때문이죠.

하지만 블록들은 그보다 훨씬 전부터 여기저기 굴러다니고 있었습니다.

## 3년 동안 모은 부품들

Agent! 이전에도 다른 앱들이 있었습니다. **ANIE**, **Game Changer**, **BattleScript**, **XCF MCP 서버와 클라이언트**, 그리고 파일의 여러 줄을 한 번에 바꾸는 도구인 **D1F**. 여기에 Swift 패키지 여덟 개 정도가 더 있었고, 모두 같은 사람이 만들었습니다.

각각은 일의 한 조각씩을 할 수 있었습니다. 어떤 건 AI와 대화할 수 있었고, 어떤 건 코드를 고칠 수 있었고, 어떤 건 Xcode를 만지작거릴 수 있었죠. 하지만 가장 중요한 일, 즉 **스스로 계속 해 나가는 일**은 아무것도 못 했습니다.

태엽 장난감을 떠올려 보세요. 태엽을 감으면 세 걸음 걷고 멈춥니다. 귀엽죠. 쓸모는 없고요. 빠져 있던 건 루프였습니다. 문제를 보고, 도구를 고르고, 써 보고, 무슨 일이 일어났는지 확인하고, 일이 끝날 때까지 다시 반복하는 것. (그 루프에 대해서는 [로봇과 샌드위치가 나오는 글](/blog/what-is-an-agent-loop/)이 따로 있습니다.)

루프가 돌아가기 시작하자, 옛 부품 중 가장 좋은 것들이 그 위에 딸깍 맞춰 끼워질 수 있었습니다. 이게 한 문장으로 된 탄생 이야기 전부입니다. 나머지는 세부 사항이고, 세부 사항이 재미있습니다.

## 첫째 날: 두뇌 하나, 도우미 하나, 그리고 취소 버튼

첫 번째 진짜 커밋의 이름은 *"Autonomous Agent with privileged launch daemon."* 입니다. 파일 20개, Swift 코드 1,765줄이었죠. 상자 안에는 이런 게 들어 있었습니다.

- 원하는 일을 입력하는 SwiftUI 창.
- 생각을 맡은 AI 두뇌 하나, Claude.
- **Launch Daemon**: 집 전체의 열쇠를 들고 백그라운드에서 일하는 작은 도우미. 덕분에 에이전트가 어른들만 하는 시스템 일을 할 수 있습니다.
- 작업 기록, 스크린샷, 붙여넣기.

한 시간 뒤 첫 번째 충돌 수정이 들어왔습니다(스크린샷을 붙여넣으면 앱이 죽었거든요). 몇 분 뒤에는 Esc 키에 연결된 커다란 빨간 **취소** 버튼이 생겼습니다. 스스로 움직이는 걸 만들면, 멈춤 버튼은 일찍 생기기 마련입니다.

오후 5시 27분에는 두 번째 도우미 **Launch Agent**가 생겼습니다. 전능한 root가 아니라 *여러분*의 권한으로 명령을 실행하는 도우미죠. 폴더 목록 하나 보려고 마스터키를 달라고 하는 건, 촛불 하나 켜려고 소방서를 부르는 것과 같습니다. 6분 뒤 Agent!는 두 번째 두뇌를 얻었습니다. 바로 **Ollama**로, 여러분의 Mac 안에 사는 AI 모델로도 돌아갈 수 있게 되었죠.

그날이 끝나기 전에 Agent!는 Swift 스크립트를 작성하고 실행하고, Xcode를 조작하고, 비전 모델로 그림을 보고, 스플래시 화면을 띄울 수도 있게 되었습니다. 신호등 같은 작은 상태 점도 생겼는데, 초록·노랑·빨강으로 정착하기까지 커밋이 열두 개쯤 들었습니다. 에이전트 루프보다 어려운 일도 있는 법이죠.

## 둘째 날: "해도 될까요?"

3월 12일은 Agent!가 Mac이 예의 바르고, 그 예의에 아주 엄격하다는 걸 배운 날입니다.

음악이나 Pages 같은 다른 앱을 조작하려면 macOS가 먼저 묻습니다. *"Agent!가 '음악'을 제어하려고 합니다. 허용하시겠습니까?"* 이 작은 창이 실제로 뜨게 만드는 데 저녁 내내 걸렸습니다. 대략 밤 8시 20분부터 9시 40분까지의 기록은 몇 분 간격의 시도로 가득합니다. 이렇게 해 보고, 메인 스레드에서 해 보고, 시스템 설정을 열어 보고, `osascript`를 써 보고, `every window`를 요청해 보고, 그냥 `name`만 해 보고. 게다가 Keynote, Numbers, Pages는 번들 ID가 바뀌어 있어서, 엉뚱한 이름으로 문을 두드리고 있었습니다.

결국 해냈습니다. 같은 날 밤에는 이미지와 웹 페이지를 자기 로그 안에 바로 보여 주는 법도 배웠습니다. 그래서 앨범 아트를 만들면, 앨범 아트가 눈앞에 보입니다.

## 셋째 날: 이름과 버전 번호

3월 13일 아침, 앱은 이름을 얻었습니다. 오전 9시 6분 커밋의 제목은 *"rename app to Agent!"* 입니다. 느낌표도 일부러 붙였습니다.

20분 뒤에는 지금까지도 중요한 변화가 들어왔습니다. 스크립트가 별도 프로그램이 아니라, 앱 안에 바로 로드되는 **동적 라이브러리**가 된 것이죠. 그래서 AgentScripts는 다시 묻지 않고도 Agent!와 똑같은 Mac 권한을 갖습니다.

그날 늦게 **1.0.0** 태그가 붙었습니다. 첫 커밋부터 세면 **이틀도 안 되어 177개의 커밋**입니다. 1.0.1부터 1.0.16까지는 그 뒤 8일 동안 이어졌습니다.

작은 사실 하나: 그 초기 커밋들의 작성자 이름은 사람이 아닙니다. **"Agent! for MacOS"** 입니다.

## 자라나기

첫 스프린트가 끝나자 이야기는 빨라집니다.

- **4월 6일.** 거의 한 달치 기록이 깔끔한 시작 커밋 하나로 합쳐졌습니다. 전체 기록은 백업에 남겨 두었습니다.
- **4월 7일.** "코딩 모드", "자동화 모드", "표준 모드"가 [통째로 뜯겨 나갔습니다](/blog/why-we-ripped-out-modes/). 에이전트 하나, 모든 도구, 언제나.
- **4월.** Mac에서 직접, 무료로 돌아가는 두뇌인 Apple Intelligence가 합류했습니다.
- **8월 31일.** 프로젝트가 GitHub 조직 `macOS26`에서 **AgentiLoop**로 옮겨 갔고, 웹사이트는 **agentiloop.ai**가 되었습니다.
- **최근.** Agent!는 [macOS 14.6과 Intel Mac에서 돌아가는 법](/blog/sonoma-intel-and-the-mac-that-was-not-dead-yet/)을 배웠고, 자기 터미널 동생들을 만드는 일도 도왔습니다. Rust로 만든 [AgentiLoopCLI](https://github.com/AgentiLoop/AgentiLoopCLI)와 Go로 만든 [AgentiLoopGo](https://github.com/AgentiLoop/AgentiLoopGo)입니다.

처음엔 두뇌 하나로 시작했습니다. 지금은 Apple Intelligence에 더해 **23개 AI 제공업체**와 함께 일합니다. 4월의 그 대청소 이후, 메인 브랜치에는 1,300개가 넘는 커밋이 쌓였습니다.

## 지금 모습이 된 이유

Agent!의 독특한 점은 거의 다 처음 사흘로 거슬러 올라갑니다.

도우미가 둘인 것, 하나는 여러분을 위해, 하나는 root를 위해 있는 것은 첫날에 둘 다 필요했기 때문입니다. 100% Swift인 것은 그걸 만든 부품들이 Swift였기 때문입니다. 65개짜리 NPM 패키지 더미가 아니라 직접 쓴 코드로 만들어졌습니다. 손쉬운 사용과 AppleScript로 다른 앱을 이름으로 조작하는 것은, 둘째 날 내내 Mac에게 공손하게 부탁하는 법을 배웠기 때문입니다. 그리고 지금도 커다란 취소 버튼이 있습니다.

큰 것은 모두 작은 블록 더미에서 시작합니다. 이 더미는 3년 동안 쌓였습니다. 그리고 3월 11일, 드디어 누군가 다른 블록들을 한데 붙잡아 주는 블록을 찾아냈습니다. 바로 루프입니다.
