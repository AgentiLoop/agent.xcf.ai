---
title: Sonoma, Intel und der Mac, der noch nicht tot war
description: Agent! für Mac läuft jetzt unter macOS Sonoma 14.6 und neuer, auf Apple Silicon und Intel. Viele von euch haben nach einer Version vor macOS 26 gefragt. Hier ist sie.
tags: Versionshinweise, Hinter den Kulissen
---
<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 340" role="img" aria-labelledby="macs-title macs-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="macs-title">Zwei glückliche Macs und ein neues Schild</title>
<desc id="macs-desc">Ein Intel-Mac und ein Apple-Silicon-Mac stehen auf einem Schreibtisch und lächeln beide. Zwischen ihnen steht ein Schild, auf dem „Nur macOS 26“ durchgestrichen und durch „macOS 14.6+, Apple Silicon und Intel“ ersetzt ist.</desc>
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
<text x="380" y="88" font-size="16" fill="#8a97a8">Nur macOS 26</text>
<text x="380" y="118" font-size="19" font-weight="700">macOS 14.6+</text>
<text x="380" y="141" font-size="16">Apple Silicon</text>
<text x="380" y="162" font-size="16">und Intel</text>
<text x="190" y="315" font-size="20">Intel-Mac</text>
<text x="570" y="315" font-size="20">Apple-Silicon-Mac</text>
</g>
<path d="M318 83H442" stroke="#d94877" stroke-width="3" stroke-linecap="round"/>
</svg>
<figcaption>Gleicher Schreibtisch. Gleiche Macs. Neues Schild.</figcaption>
</figure>

Mal ehrlich. Als bei Agent! noch „erfordert macOS 26“ stand, blieben eine Menge guter Macs außen vor.

Du warst auf Sonoma? Pech gehabt. Auf Sequoia? Genauso. Und mit einem Intel-Mac warst du nicht mal Teil der Diskussion.

Das hat mich immer gestört. Diese Macs funktionieren noch. Leute benutzen sie jeden Tag. Sie schreiben Code darauf, führen ihre Firma damit und haben viel zu viele Browser-Tabs darauf offen. Die Macs haben nichts falsch gemacht. Sie hatten nur nicht das neueste Betriebssystem.

Damit ist Schluss. **Agent! für Mac läuft jetzt unter macOS Sonoma 14.6 und neuer, auf Apple Silicon und auf Intel.**

Viele von euch haben auf eine Version vor macOS 26 gewartet. Die hier ist für euch.

## Warum es überhaupt nur für 26 war

Agent! nutzt Apples On-Device-Modell über ein Framework namens FoundationModels. Es ist nicht das Hauptgehirn. Die schwere Arbeit erledigt der Anbieter, den du auswählst. Aber das On-Device-Modell hilft bei kleineren Aufgaben, etwa beim Zusammenfassen während der Kontextkomprimierung, beim Zählen von Tokens und beim Vorwärmen einer Sitzung, wenn die App startet.

Und hier ist der Haken. FoundationModels gibt es nur unter macOS 26. Wenn dein Code auch nur einen seiner Typen erwähnt, lässt er sich für einen älteren Mac nicht bauen. Der Compiler sagt einfach Nein.

Der bequeme Weg war also, macOS 26 vorauszusetzen und weiterzumachen. Bequem für mich jedenfalls. Für alle anderen nicht so toll.

Und ehrlich gesagt war es ein bisschen albern. Das On-Device-Modell ist ein Helfer. Nett zu haben. Es war nie der Grund, warum Agent! funktioniert. Wegen eines Helfers jeden älteren Mac auszusperren, ist so, als würde man sich weigern, Abendessen zu kochen, weil die Petersilie alle ist.

## Und wie behebt man das?

Man fragt zuerst. Bevor Agent! das On-Device-Modell anfasst, prüft es: Bin ich auf macOS 26? Wenn ja, super, dann wird es genutzt. Wenn nein, läuft dieser Code einfach nicht, und dein Anbieter erledigt weiter die eigentliche Arbeit.

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 300" role="img" aria-labelledby="fork-title fork-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="fork-title">Erst fragen, dann benutzen</title>
<desc id="fork-desc">Ein Flussdiagramm. Agent! möchte das On-Device-Modell nutzen. Es fragt: Ist das macOS 26? Ja führt dazu, dass die On-Device-Helfer genutzt werden. Nein führt dazu, dass sie übersprungen werden, während der Anbieter weiterarbeitet.</desc>
<defs><marker id="fork-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0 0L10 5 0 10Z" fill="#4b617e"/></marker></defs>
<rect width="760" height="300" rx="20" fill="#f0f5fb"/>
<g fill="none" stroke="#4b617e" stroke-width="4"><path d="M380 90V113" marker-end="url(#fork-arrow)"/><path d="M320 150H170V206" marker-end="url(#fork-arrow)"/><path d="M440 150H590V206" marker-end="url(#fork-arrow)"/></g>
<rect x="230" y="30" width="300" height="60" rx="18" fill="#d7eaff" stroke="#3377b9" stroke-width="3"/>
<path d="M380 115L440 150 380 185 320 150Z" fill="#fce9b6" stroke="#9a701b" stroke-width="3"/>
<rect x="40" y="210" width="260" height="66" rx="18" fill="#cff3e4" stroke="#29836a" stroke-width="3"/>
<rect x="460" y="210" width="260" height="66" rx="18" fill="#dfd9ff" stroke="#7760b5" stroke-width="3"/>
<g font-family="system-ui,sans-serif" text-anchor="middle" fill="#173452">
<text x="380" y="67" font-size="18" font-weight="700">On-Device-Modell gewünscht?</text>
<text x="380" y="156" font-size="16" font-weight="700">macOS 26?</text>
<text x="245" y="140" font-size="17">Ja</text>
<text x="515" y="140" font-size="17">Nein</text>
<text x="170" y="238" font-size="18" font-weight="700">Nutzen.</text>
<text x="170" y="262" font-size="14">Zusammenfassungen, Token-Zählung</text>
<text x="590" y="238" font-size="18" font-weight="700">Überspringen.</text>
<text x="590" y="262" font-size="15">Dein Anbieter arbeitet weiter</text>
</g>
</svg>
<figcaption>Das ist der ganze Trick. Erst fragen, dann benutzen.</figcaption>
</figure>

Einen Haken gibt es noch. Swift erlaubt keiner Klasse eine Property, deren Typ auf dem laufenden Betriebssystem nicht existiert. Also wird die Sitzung als schlichtes `AnyObject` gespeichert und nur innerhalb des macOS-26-Codes zurückgecastet. Nicht hübsch. Funktioniert super.

## Die Commits

Das alles ist am 27. September 2026 passiert. Vier Commits, ein Tag, und alles steht in Git.

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 260" role="img" aria-labelledby="day-title day-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="day-title">27. September 2026, Commit für Commit</title>
<desc id="day-desc">Eine Zeitleiste von 12 bis 20 Uhr. Commit ea5ce624 um 12:46 Uhr, 4d7fca86 um 12:57 Uhr, 3a993205 um 19:14 Uhr und 81079e2a um 19:32 Uhr.</desc>
<rect width="760" height="260" rx="20" fill="#f0f5fb"/>
<g stroke="#4b617e" stroke-width="2"><path d="M121 104V130M136 130V148M639 104V130M663 130V148"/></g>
<path d="M60 130H700" stroke="#4b617e" stroke-width="4" stroke-linecap="round"/>
<g fill="#227657" stroke="#fff" stroke-width="3"><circle cx="121" cy="130" r="8"/><circle cx="136" cy="130" r="8"/><circle cx="639" cy="130" r="8"/><circle cx="663" cy="130" r="8"/></g>
<g font-family="system-ui,sans-serif" text-anchor="middle" fill="#173452">
<text x="121" y="56" font-size="16" font-weight="700">absichern</text><text x="121" y="76" font-size="15">ea5ce624</text><text x="121" y="96" font-size="15">12:46</text>
<text x="136" y="166" font-size="15">12:57</text><text x="136" y="186" font-size="15">4d7fca86</text><text x="136" y="206" font-size="16" font-weight="700">Pakete anheben</text>
<text x="639" y="56" font-size="16" font-weight="700">Doku</text><text x="639" y="76" font-size="15">3a993205</text><text x="639" y="96" font-size="15">19:14</text>
<text x="663" y="166" font-size="15">19:32</text><text x="663" y="186" font-size="15">81079e2a</text><text x="663" y="206" font-size="16" font-weight="700">1.1.76</text>
<g font-size="14" fill="#4b617e"><text x="60" y="244">12 Uhr</text><text x="380" y="244">16 Uhr</text><text x="700" y="244">20 Uhr</text></g>
</g>
</svg>
<figcaption>Commit-Zeiten laut Git, US-Ostküstenzeit.</figcaption>
</figure>

**[`ea5ce624`](https://github.com/AgentiLoop/Agent/commit/ea5ce62493aef5ca74e694a8ec85b16621ec6388)**: jede Verwendung von FoundationModels hinter macOS 26 absichern. Das betrifft den Modell-Service, den Apple-Intelligence-Mediator, das Vorwärmen beim Start in `AgentApp`, Zusammenfassungen und Token-Zählung in `Compression.swift` sowie `AboutSelf`. Auf älteren Systemen meldet es jetzt einfach „erfordert macOS 26 oder neuer“, statt sich gar nicht erst bauen zu lassen. Wer schon auf 26 ist, merkt keinerlei Unterschied.

**[`4d7fca86`](https://github.com/AgentiLoop/Agent/commit/4d7fca863a15d91d8e3734f991fabfcb90da734c)**: alle zehn Swift-Pakete von AgentiLoop auf Versionen anheben, die macOS 14 unterstützen. AgentAccess, AgentAudit, AgentColorSyntax, AgentD1F, AgentEventBridges, AgentLLM, AgentMCP, AgentSwift, AgentTerminalNeo, AgentTools. Alle zehn. Das war der mühsame Teil. Man kann nicht einfach eine Zahl in Xcode ändern und Feierabend machen. Alles, wovon die App abhängt, muss mitziehen. Im selben Commit fiel außerdem auf, dass ein Aufruf zur Token-Zählung macOS 26.4 braucht, nicht 26.0, also wurde diese Prüfung verschärft.

**[`3a993205`](https://github.com/AgentiLoop/Agent/commit/3a9932053630a21ec9df481c8f137cea30ff87a0)**: Doku. README und FAQ sagen jetzt **Apple Silicon oder Intel, macOS 14.6+**. Zwei Wörter: „oder Intel“. Hat eine Weile gedauert, sie sich zu verdienen.

**[`81079e2a`](https://github.com/AgentiLoop/Agent/commit/81079e2a937f62d2d68389a3c124214f80cb3bc3)**: Version 1.1.76, Build 276, Deployment Target 14.6. Raus damit.

Das war’s. Keine Magie. Nur `#available`-Prüfungen, Paket-Updates und so lange bauen, bis es aufgehört hat, mich anzuschreien.

## Das Kleingedruckte (die ehrliche Sorte)

Unter Sonoma oder Sequoia bekommst du die Apple-Intelligence-Teile nicht, weil Apple sie dort nicht ausliefert. Agent! umgeht sie einfach. Du wirst nicht viel vermissen. Die eigentliche Arbeit hat sowieso dein Anbieter gemacht.

Ein Intel-Mac bleibt ein Intel-Mac. Mit einem Cloud-Anbieter läuft Agent! darauf problemlos. Große lokale Modelle sind eine andere Geschichte. In der FAQ steht schon, dass du für lokale 30B-Modelle 64 GB+ brauchst, und das gilt für jeden Mac, nicht nur für ältere.

Und 14.6 ist die Untergrenze. Wenn dein Mac kein Sonoma schafft, kann ich dir da nicht helfen. Ich bin gut, aber so gut dann auch wieder nicht.

## Intel-Leute, dieser Teil ist für euch

Ich weiß, dass viele von euch an ihren Intel-Macs festhalten, weil sie ihren Job noch machen. Sie sind abbezahlt. Euer Setup sitzt. Ihr wisst, wo alles ist. Ihr wollt keinen neuen Rechner kaufen, nur um eine App auszuprobieren.

Völlig verständlich. Das solltet ihr auch nicht müssen.

Dasselbe gilt für alle mit Apple Silicon, die einfach noch nicht bereit für den Sprung auf macOS 26 sind. Vielleicht wartet ihr auf ein Point-Release. Vielleicht ist ein Tool, das ihr braucht, noch nicht so weit. Vielleicht habt ihr einfach keine Lust. Kein Urteil. Bleibt auf Sonoma, so lange ihr wollt.

## Hol es dir

**Agent! für Mac. macOS Sonoma 14.6 und neuer. Apple Silicon und Intel.**

Wenn du gewartet hast: Das Warten hat ein Ende. Probier es aus und sag mir, wie es auf deinem Rechner läuft. Vor allem ihr, liebe Intel-Fraktion. Ich will es wissen.

Dein Mac ist noch nicht tot. Er brauchte offenbar nur eine Einladung.

Du willst die ausführliche Version mit Code? Schau dir den [technischen Beitrag](/blog/agent-now-runs-on-macos-14-6-and-intel/) an.
