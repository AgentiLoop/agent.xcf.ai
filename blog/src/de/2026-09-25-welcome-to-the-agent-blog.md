---
title: Willkommen im Agent!-Blog: Eine App, jede KI, volle Kontrolle über deinen Mac
description: Was AgentiLoop Agent! ist, warum ich es so gebaut habe, wie es ist, und was dich hier erwartet – direkt aus dem Quellcode.
tags: Ankündigung, Architektur
---
<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 340" role="img" aria-labelledby="map-title map-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="map-title">Ein kleiner Mac reicht dir die Landkarte</title>
<desc id="map-desc">Ein lächelnder Mac steht auf einem Schreibtisch und hält eine aufgefaltete Landkarte. Die Karte hat vier Stationen, verbunden durch einen gepunkteten Pfad: Jede KI, Die Schleife, AgentScript und Sicherheit.</desc>
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
<text x="350" y="152" font-size="15" font-weight="700">Jede KI</text>
<text x="440" y="117" font-size="15" font-weight="700">Die Schleife</text>
<text x="520" y="222" font-size="15" font-weight="700">AgentScript</text>
<text x="580" y="90" font-size="15" font-weight="700">Sicherheit</text>
<text x="345" y="88" font-size="14" fill="#8b684c">Deine Karte</text>
<text x="140" y="322" font-size="18">Agent! für den Mac</text>
</g>
</svg>
<figcaption>Jeder Blog braucht einen ersten Beitrag. Dieser hier ist die Landkarte.</figcaption>
</figure>

Hi, ich bin Todd. Ich entwickle **AgentiLoop Agent!**, einen nativen KI-Agenten für macOS, und das hier ist sein Blog.

Ich wollte einen Ort, an dem ich die Teile von Agent! erklären kann, die in keine README und keine Release Notes passen. Warum eine Schutzmaßnahme genau so aussieht, wie sie aussieht. Warum die Agent-Schleife ihre eigene Arbeit überprüft. Was in einem Release Candidate kaputtgegangen ist und wie wir es repariert haben. Das meiste, was du hier liest, kommt direkt aus der Codebasis, denn die kenne ich am besten. Ab und zu schaue ich mir auch die größere Welt der KI-Agenten an und was sie für deinen Mac bedeutet.

Wenn du neu hier bist, fang hier an. Betrachte diesen Beitrag als Landkarte.

## Was Agent! ist

Agent! ist zu 100 % natives Swift und SwiftUI. Du tippst (oder sagst), was du willst, und es erledigt die Arbeit tatsächlich auf deinem Mac, statt dir nur zu erklären, wie es geht:

- **Es schreibt echten Code.** Es liest dein Projekt, bearbeitet Dateien per String-Replace-Diffs, baut in Xcode, liest die Fehler, behebt sie und committet mit git.
- **Es steuert jede Mac-App** über die Accessibility-API sowie über AppleScript, JXA und 51 ScriptingBridge-App-Bridges.
- **Es führt Shell-Befehle als du oder als root aus** – über einen Launch Agent und einen Launch Daemon, die mit SMAppService registriert und per XPC angesprochen werden.
- **Es arbeitet mit 23 LLM-Anbietern** plus Apple Intelligence auf dem Gerät: Claude, Codex, OpenAI, Gemini, Grok, Mistral, DeepSeek, Qwen, Z.ai, OpenRouter, Ollama, vLLM, LM Studio und weiteren.
- **Es hört zu.** Sag *„Agent!“*, gefolgt von einer Aufgabe, oder schreib ihm von deinem iPhone per iMessage (nur freigegebene Absender).

Die README bringt es in vier Wörtern auf den Punkt: *Siri antwortet. Agent! handelt.*

## Kein NPM, kein Electron

Das ist der Teil, der die Leute überrascht. Es gibt keine Electron-Hülle. Keine Node-Runtime. Keinen `node_modules`-Ordner, der still und leise deine Festplatte auffrisst. Jedes Swift-Paket, von dem Agent! abhängt, habe ich selbst geschrieben, und jedes liegt in einem eigenen Repository in der Organisation [AgentiLoop](https://github.com/AgentiLoop):

| Paket | Aufgabe |
|---|---|
| AgentTools | Tool-Schemas, System-Prompts und Anbieterverwaltung |
| AgentLLM | Protokolle, Typen und Registry für LLM-Anbieter |
| AgentMCP | MCP-Client (stdio und HTTP) |
| AgentAccess | Accessibility-Automatisierung |
| AgentEventBridges | ScriptingBridge-Protokolle für über 50 Mac-Apps |
| AgentD1F | Mehrzeilige Diff-Engine |
| AgentSwift | Codeanalyse mit SwiftSyntax |
| AgentColorSyntax · AgentTerminalNeo | Syntaxhervorhebung · Retro-Terminal-Markdown |
| AgentAudit | Audit-Logging über `os.log` |

Heraus kommt eine App, die kaum RAM braucht und trotzdem Xcode-Automatisierung, Swift-Syntaxanalyse, Accessibility, AppleScript, Safari-Automatisierung und MCP direkt ab Werk mitbringt.

## Die Schleife im Zentrum

Bei Agent! hängt alles an einer Idee: einer **selbstprüfenden Aufgabenschleife**. Das Modell denkt nach, ruft ein Tool auf, schaut sich das echte Ergebnis an und korrigiert sich selbst. Das funktioniert nur, wenn man sich darauf verlassen kann, deshalb sind ein paar Regeln fest eingebaut:

- **Tools lassen sich nicht vortäuschen.** Jeder Aufruf läuft über einen einzigen Dispatcher und liefert echte Ausgabe. Behauptet das Modell *„Ich habe es angeklickt“*, ohne tatsächlich ein Tool aufgerufen zu haben, spricht Agent! das an und schickt eine Korrektur.
- **„Fertig“ braucht Belege.** Eine Aufgabe kann sich erst für abgeschlossen erklären, wenn ihre `goal_state`-Kriterien mit Nachweis abgehakt sind – etwa mit einem grünen Build oder einem bestandenen Test.
- **Erst lesen, dann bearbeiten.** Agent! weigert sich, eine Datei zu bearbeiten, die das Modell nicht gelesen hat oder die sich seit dem Lesen auf der Festplatte geändert hat (geprüft per SHA-256). Mit der Ablehnung bekommt das Modell gleich die aktuelle Datei, sodass der nächste Versuch die richtigen Zeilen verwendet.
- **Alles lässt sich rückgängig machen.** Jede Änderung wird eine Woche lang als Snapshot gesichert. Setz eine einzelne Datei zurück oder spul mit `rewind_task` eine ganze Aufgabe zurück.

Jede dieser Regeln nehme ich in kommenden Beiträgen auseinander.

## AgentScript: Swift mit vollen Berechtigungen

AgentScript gehört zu meinen Lieblingsbausteinen. Skripte sind ganz normale Swift-Dateien. Agent! kompiliert jedes davon mit SwiftPM zu einer `.dylib` und lädt sie per `dlopen` in den eigenen Prozess. So bekommt dein Skript dieselben macOS-Berechtigungen, die Agent! bereits hat: Accessibility, Automatisierung, Kalender, Kontakte, Mail, Fotos und den Rest. Du brauchst nur einen einzigen Einstiegspunkt:

```swift
import Foundation
import CalendarBridge   // any `import XBridge` auto-wires, no Package.swift edits

@_cdecl("script_main")
public func scriptMain() -> Int32 {
    print("Hello from AgentScript! 👋")
    return 0
}
```

Alles, was das Skript ausgibt, geht zurück an das Modell, und der Rückgabewert ist der Exit-Status. Rund 35 Beispiele werden mit der App ausgeliefert, darunter `TodayEvents`, `NowPlaying`, `CheckMail` und `CreateDmg`.

## Sicherheit zum Nachlesen

Agent! kann Befehle als root ausführen. Das ist eine Menge Vertrauen, um das ich da bitte, also darf Sicherheit nicht nur eine Folie in einer Präsentation sein. Sie ist Code, und du kannst ihn auf GitHub lesen. Ein fest einprogrammierter `ShellSafetyService` weist katastrophale Befehle ab, bevor sie überhaupt abgeschickt werden, und der privilegierte Daemon führt dieselbe Prüfung auf seiner Seite noch einmal durch. Außerdem gibt es eine optionale Zweitmeinung namens **Jev**, die bewertet, wie wahrscheinlich ein Befehl Daten zerstört. Der [erste Deep Dive](/blog/inside-agent-shell-guardrails/) zeigt genau, wie das funktioniert.

## Die Familie wächst

Dieselbe Agent-Schleife läuft inzwischen auch im Terminal, unter macOS, Windows und Linux. Es gibt zwei CLIs mit denselben Fähigkeiten: [AgentiLoopCLI](https://github.com/AgentiLoop/AgentiLoopCLI) in Rust und [AgentiLoopGo](https://github.com/AgentiLoop/AgentiLoopGo) in Go. Mein liebster Fun Fact aus der README: Agent! für den Mac hat seine kleinen Geschwister selbst geschrieben.

## Was dich hier erwartet

- **Interna:** die Agent-Schleife, Kontextkomprimierung, Tool-Dispatch, Sub-Agents, Gedächtnis und Pläne.
- **Sicherheit:** Schutzmechanismen, das XPC-Vertrauensmodell und was jüngste Agent-Vorfälle uns allen beibringen.
- **Release Notes mit dem Warum:** was sich in jedem Build geändert hat – und der Bug, der es nötig gemacht hat.
- **Anleitungen:** AgentScript-Rezepte, die Wahl eines Anbieters mit kleinem Budget und ein komplett lokaler Betrieb.
- **Die weitere Agent-Welt:** News und Reviews, immer zurückgeführt auf das, was sie für deinen Mac bedeuten.

Agent! läuft ab macOS 14.6 auf Apple Silicon und Intel und ist für die private Nutzung kostenlos. Hol es dir unten, gib ihm eine echte Aufgabe und erzähl mir, wie es gelaufen ist.
