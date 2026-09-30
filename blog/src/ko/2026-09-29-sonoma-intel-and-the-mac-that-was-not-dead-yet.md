---
title: Sonoma, Intel, 그리고 아직 끝나지 않은 Mac
description: 이제 Mac용 Agent!가 Apple Silicon과 Intel의 macOS Sonoma 14.6 이상에서 실행됩니다. macOS 26 이전 버전을 원하신 분이 많았죠. 여기 있습니다.
tags: 릴리스 노트, 비하인드
---
<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 340" role="img" aria-labelledby="macs-title macs-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="macs-title">행복한 Mac 두 대와 새 표지판</title>
<desc id="macs-desc">Intel Mac과 Apple Silicon Mac이 책상 위에서 나란히 웃고 있습니다. 둘 사이의 표지판에는 "macOS 26 전용"이 줄로 지워지고 "macOS 14.6+, Apple Silicon 및 Intel"로 바뀌어 있습니다.</desc>
<rect width="760" height="340" rx="20" fill="#eef6ff"/>
<rect x="182" y="215" width="16" height="50" fill="#8a97a8"/><rect x="150" y="263" width="80" height="12" rx="4" fill="#8a97a8"/>
<rect x="562" y="215" width="16" height="50" fill="#8a97a8"/><rect x="530" y="263" width="80" height="12" rx="4" fill="#8a97a8"/>
<rect x="374" y="170" width="12" height="105" fill="#8b684c"/>
<path d="M30 280H730" stroke="#8b684c" stroke-width="10" stroke-linecap="round"/>
<rect x="90" y="100" width="200" height="125" rx="14" fill="#c9d3df" stroke="#173452" stroke-width="4"/>
<rect x="104" y="114" width="172" height="97" rx="6" fill="#559ef5"/>
<circle cx="160" cy="150" r="9" fill="#fff"/><circle cx="220" cy="150" r="9" fill="#fff"/>
<circle cx="162" cy="151" r="4" fill="#173452"/><circle cx="222" cy="151" r="4" fill="#173452"/>
<path d="M165 178Q190 196 215 178" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
<rect x="470" y="100" width="200" height="125" rx="14" fill="#e7e2f7" stroke="#173452" stroke-width="4"/>
<rect x="484" y="114" width="172" height="97" rx="6" fill="#7b6ad6"/>
<circle cx="540" cy="150" r="9" fill="#fff"/><circle cx="600" cy="150" r="9" fill="#fff"/>
<circle cx="542" cy="151" r="4" fill="#173452"/><circle cx="602" cy="151" r="4" fill="#173452"/>
<path d="M545 178Q570 196 595 178" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
<rect x="303" y="60" width="154" height="115" rx="10" fill="#fff" stroke="#8b684c" stroke-width="4"/>
<g font-family="system-ui,sans-serif" text-anchor="middle" fill="#173452">
<text x="380" y="88" font-size="16" fill="#8a97a8">macOS 26 전용</text>
<text x="380" y="118" font-size="19" font-weight="700">macOS 14.6+</text>
<text x="380" y="141" font-size="16">Apple Silicon</text>
<text x="380" y="162" font-size="16">및 Intel</text>
<text x="190" y="315" font-size="20">Intel Mac</text>
<text x="570" y="315" font-size="20">Apple Silicon Mac</text>
</g>
<path d="M318 83H442" stroke="#d94877" stroke-width="3" stroke-linecap="round"/>
</svg>
<figcaption>같은 책상. 같은 Mac. 새 표지판.</figcaption>
</figure>

솔직히 말해 봅시다. Agent!에 "macOS 26 필요"라고 적혀 있을 때, 좋은 Mac들이 꽤 많이 소외됐습니다.

Sonoma를 쓰고 있다면 운이 없었죠. Sequoia도 마찬가지. Intel Mac이라면 아예 대화에 끼지도 못했고요.

그게 늘 마음에 걸렸습니다. 그 Mac들은 아직 멀쩡히 돌아갑니다. 사람들이 매일 씁니다. 거기서 코드를 짜고, 사업을 굴리고, 브라우저 탭을 지나치게 많이 열어 둡니다. 잘못한 건 하나도 없어요. 그냥 최신 OS가 아니었을 뿐이죠.

이제는 아닙니다. **Mac용 Agent!가 이제 macOS Sonoma 14.6 이상, Apple Silicon과 Intel 모두에서 실행됩니다.**

macOS 26 이전 버전을 기다려 온 분이 많았죠. 이번 버전은 여러분을 위한 겁니다.

## 애초에 왜 26 전용이었나

Agent!는 FoundationModels라는 프레임워크를 통해 Apple의 온디바이스 모델을 씁니다. 메인 두뇌는 아닙니다. 힘든 일은 여러분이 고른 공급자가 다 합니다. 하지만 온디바이스 모델은 컨텍스트 압축 중 요약, 토큰 세기, 앱 실행 시 세션 예열 같은 작은 일들을 거들어 줍니다.

문제는 여기 있습니다. FoundationModels는 macOS 26에만 있습니다. 코드에서 그 타입을 하나라도 언급하면 구형 Mac용으로는 빌드가 안 됩니다. 컴파일러가 그냥 안 된다고 해요.

그래서 제일 쉬운 길은 macOS 26을 요구하고 넘어가는 거였습니다. 적어도 저한테는 쉬웠죠. 다른 모두에게는 별로였고요.

솔직히 좀 우스운 일이었습니다. 온디바이스 모델은 도우미예요. 있으면 좋은 것. Agent!가 돌아가는 이유였던 적은 한 번도 없습니다. 도우미 하나 때문에 구형 Mac을 전부 막는 건, 파슬리가 떨어졌다고 저녁을 안 하는 것과 같아요.

## 그럼 어떻게 고치냐고요?

먼저 물어봅니다. 온디바이스 모델을 건드리기 전에 Agent!가 확인합니다. 나 지금 macOS 26이야? 그렇다면 좋아요, 씁니다. 아니라면 그 코드는 그냥 실행되지 않고, 공급자가 계속 진짜 일을 합니다.

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 300" role="img" aria-labelledby="fork-title fork-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="fork-title">쓰기 전에 물어보기</title>
<desc id="fork-desc">순서도. Agent!가 온디바이스 모델을 쓰려고 합니다. macOS 26인지 묻습니다. 예라면 온디바이스 도우미를 사용합니다. 아니요라면 건너뛰고, 공급자는 계속 작동합니다.</desc>
<defs><marker id="fork-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0 0L10 5 0 10Z" fill="#4b617e"/></marker></defs>
<rect width="760" height="300" rx="20" fill="#f0f5fb"/>
<g fill="none" stroke="#4b617e" stroke-width="4"><path d="M380 90V113" marker-end="url(#fork-arrow)"/><path d="M320 150H170V206" marker-end="url(#fork-arrow)"/><path d="M440 150H590V206" marker-end="url(#fork-arrow)"/></g>
<rect x="230" y="30" width="300" height="60" rx="18" fill="#d7eaff" stroke="#3377b9" stroke-width="3"/>
<path d="M380 115L440 150 380 185 320 150Z" fill="#fce9b6" stroke="#9a701b" stroke-width="3"/>
<rect x="40" y="210" width="260" height="66" rx="18" fill="#cff3e4" stroke="#29836a" stroke-width="3"/>
<rect x="460" y="210" width="260" height="66" rx="18" fill="#dfd9ff" stroke="#7760b5" stroke-width="3"/>
<g font-family="system-ui,sans-serif" text-anchor="middle" fill="#173452">
<text x="380" y="67" font-size="18" font-weight="700">온디바이스 모델을 쓸까요?</text>
<text x="380" y="156" font-size="16" font-weight="700">macOS 26?</text>
<text x="245" y="140" font-size="17">예</text>
<text x="515" y="140" font-size="17">아니요</text>
<text x="170" y="238" font-size="18" font-weight="700">사용한다.</text>
<text x="170" y="262" font-size="15">요약, 토큰 계산</text>
<text x="590" y="238" font-size="18" font-weight="700">건너뛴다.</text>
<text x="590" y="262" font-size="15">공급자는 계속 작동</text>
</g>
</svg>
<figcaption>이게 비결의 전부입니다. 쓰기 전에 물어보기.</figcaption>
</figure>

한 가지 걸림돌이 더 있습니다. Swift는 실행 중인 OS에 존재하지 않는 타입의 프로퍼티를 클래스가 갖지 못하게 합니다. 그래서 세션은 평범한 `AnyObject`로 저장하고, macOS 26 코드 안에서만 다시 캐스팅합니다. 예쁘진 않아요. 그래도 아주 잘 돌아갑니다.

## 커밋들

모든 일은 2026년 9월 27일에 일어났습니다. 커밋 네 개, 하루, 전부 Git에 남아 있습니다.

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 260" role="img" aria-labelledby="day-title day-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="day-title">2026년 9월 27일, 커밋 하나하나</title>
<desc id="day-desc">정오부터 오후 8시까지의 타임라인. 오후 12:46에 커밋 ea5ce624, 오후 12:57에 4d7fca86, 오후 7:14에 3a993205, 오후 7:32에 81079e2a.</desc>
<rect width="760" height="260" rx="20" fill="#f0f5fb"/>
<g stroke="#4b617e" stroke-width="2"><path d="M121 104V130M136 130V148M639 104V130M663 130V148"/></g>
<path d="M60 130H700" stroke="#4b617e" stroke-width="4" stroke-linecap="round"/>
<g fill="#227657" stroke="#fff" stroke-width="3"><circle cx="121" cy="130" r="8"/><circle cx="136" cy="130" r="8"/><circle cx="639" cy="130" r="8"/><circle cx="663" cy="130" r="8"/></g>
<g font-family="system-ui,sans-serif" text-anchor="middle" fill="#173452">
<text x="121" y="56" font-size="16" font-weight="700">게이트 추가</text><text x="121" y="76" font-size="15">ea5ce624</text><text x="121" y="96" font-size="15">오후 12:46</text>
<text x="136" y="166" font-size="15">오후 12:57</text><text x="136" y="186" font-size="15">4d7fca86</text><text x="136" y="206" font-size="16" font-weight="700">패키지 업데이트</text>
<text x="639" y="56" font-size="16" font-weight="700">문서</text><text x="639" y="76" font-size="15">3a993205</text><text x="639" y="96" font-size="15">오후 7:14</text>
<text x="663" y="166" font-size="15">오후 7:32</text><text x="663" y="186" font-size="15">81079e2a</text><text x="663" y="206" font-size="16" font-weight="700">1.1.76</text>
<g font-size="14" fill="#4b617e"><text x="60" y="244">정오</text><text x="380" y="244">오후 4시</text><text x="700" y="244">오후 8시</text></g>
</g>
</svg>
<figcaption>Git의 커밋 시각, 미국 동부 시간 기준.</figcaption>
</figure>

**[`ea5ce624`](https://github.com/AgentiLoop/Agent/commit/ea5ce62493aef5ca74e694a8ec85b16621ec6388)**: FoundationModels를 쓰는 모든 곳을 macOS 26 게이트 뒤로 옮겼습니다. 모델 서비스, Apple Intelligence 중재자, `AgentApp`의 실행 시 예열, `Compression.swift`의 요약과 토큰 계산, 그리고 `AboutSelf`까지요. 구형 시스템에서는 이제 빌드를 거부하는 대신 "macOS 26 이상 필요"라고 알려 줄 뿐입니다. 이미 26을 쓰고 있다면 달라지는 건 전혀 없습니다.

**[`4d7fca86`](https://github.com/AgentiLoop/Agent/commit/4d7fca863a15d91d8e3734f991fabfcb90da734c)**: AgentiLoop Swift 패키지 열 개를 전부 macOS 14를 지원하는 릴리스로 올렸습니다. AgentAccess, AgentAudit, AgentColorSyntax, AgentD1F, AgentEventBridges, AgentLLM, AgentMCP, AgentSwift, AgentTerminalNeo, AgentTools. 열 개 전부요. 이게 지루한 부분이었습니다. Xcode에서 숫자 하나 바꾸고 끝낼 수는 없어요. 앱이 의존하는 모든 게 같이 따라와야 합니다. 같은 커밋에서 토큰 계산 호출 하나가 26.0이 아니라 macOS 26.4를 필요로 한다는 것도 잡아내서, 그 확인을 더 엄격하게 바꿨습니다.

**[`3a993205`](https://github.com/AgentiLoop/Agent/commit/3a9932053630a21ec9df481c8f137cea30ff87a0)**: 문서. 이제 README와 FAQ에 **Apple Silicon 또는 Intel, macOS 14.6+** 라고 적혀 있습니다. "또는 Intel", 이 몇 글자를 얻기까지 시간이 좀 걸렸네요.

**[`81079e2a`](https://github.com/AgentiLoop/Agent/commit/81079e2a937f62d2d68389a3c124214f80cb3bc3)**: 버전 1.1.76, 빌드 276, 배포 대상 14.6. 출시.

그게 전부입니다. 마법 같은 건 없어요. `#available` 확인, 패키지 업데이트, 그리고 컴파일러가 저한테 소리 지르는 걸 멈출 때까지 빌드하기.

## 작은 글씨 (정직한 버전)

Sonoma나 Sequoia에서는 Apple Intelligence 기능을 쓸 수 없습니다. Apple이 거기에 제공하지 않으니까요. Agent!는 그냥 그 부분을 비켜 갑니다. 아쉬울 건 별로 없어요. 진짜 일은 어차피 공급자가 하고 있었으니까요.

Intel Mac은 여전히 Intel Mac입니다. 클라우드 공급자와 함께라면 Agent!는 잘 돌아갑니다. 큰 로컬 모델은 얘기가 다릅니다. FAQ에 이미 30B 로컬 모델에는 64GB+가 필요하다고 적혀 있고, 이건 구형 Mac만이 아니라 모든 Mac에 해당합니다.

그리고 14.6이 하한선입니다. 여러분의 Mac이 Sonoma를 못 돌린다면, 거기까지는 제가 도와드릴 수 없어요. 제가 꽤 괜찮긴 하지만, 그 정도는 아닙니다.

## Intel 사용자 여러분, 이건 여러분 얘기예요

아직 제 몫을 하니까 Intel Mac을 계속 쓰고 계신 분이 많다는 거 압니다. 할부도 다 끝났고. 세팅도 딱 맞춰 뒀고. 뭐가 어디 있는지 다 알고요. 앱 하나 써 보자고 새 기계를 사고 싶지는 않죠.

완전히 맞는 말입니다. 그럴 필요 없어야죠.

아직 macOS 26으로 넘어갈 준비가 안 된 Apple Silicon 사용자분들도 마찬가지입니다. 포인트 릴리스를 기다리는 중일 수도 있고, 필요한 도구가 아직 준비되지 않았을 수도 있고, 그냥 내키지 않을 수도 있죠. 뭐라 하지 않습니다. 원하는 만큼 Sonoma에 머무르세요.

## 받아 가세요

**Mac용 Agent!. macOS Sonoma 14.6 이상. Apple Silicon과 Intel.**

기다려 오셨다면, 기다림은 끝났습니다. 한번 써 보시고 여러분 기기에서 어떻게 돌아가는지 알려 주세요. 특히 Intel 사용자 여러분. 꼭 듣고 싶어요.

여러분의 Mac은 아직 끝나지 않았습니다. 알고 보니 초대장이 필요했을 뿐이었어요.

코드까지 담긴 자세한 버전이 궁금하다면 [엔지니어링 글](/blog/agent-now-runs-on-macos-14-6-and-intel/)을 확인해 보세요.
