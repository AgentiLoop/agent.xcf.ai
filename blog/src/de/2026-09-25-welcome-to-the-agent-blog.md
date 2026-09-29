---
title: Willkommen im Agent!-Blog: Eine App, jede KI, volle Kontrolle über deinen Mac
description: Was AgentiLoop Agent! ist, wie es aufgebaut ist und worum es in diesem täglichen Blog gehen wird – direkt aus dem Quellcode.
tags: Ankündigung, Architektur
---
Dies ist der offizielle Blog von **AgentiLoop Agent!**, dem nativen KI-Agenten für macOS. Der Plan ist einfach: ein Beitrag pro Tag, geschrieben vor allem auf Basis dessen, was wir am besten kennen – der Codebasis selbst. Freu dich auf tiefe Einblicke in die Funktionsweise der Agent-Schleife, darauf, warum eine Schutzmaßnahme genau so gestaltet ist, was sich im neuesten Release Candidate geändert hat, und gelegentlich auf einen Blick in die größere Welt der KI-Agenten.

Wenn du neu hier bist, ist dieser erste Beitrag deine Landkarte.

## Was Agent! ist

Agent! ist eine zu 100 % native Swift-/SwiftUI-App. Du tippst (oder sagst), was du willst, und es erledigt die Arbeit auf deinem Mac, statt sie nur zu beschreiben:

- **Es programmiert wirklich.** Es liest dein Projekt, bearbeitet Dateien per String-Replace-Diffs, baut in Xcode, liest die Fehler, behebt sie und committet mit git.
- **Es steuert jede Mac-App** über die Accessibility-API sowie über AppleScript, JXA und 51 ScriptingBridge-App-Bridges.
- **Es führt Shell-Befehle als du oder als root aus** – über einen Launch Agent und einen Launch Daemon, die mit SMAppService registriert und per XPC angesprochen werden.
- **Es spricht mit 23 LLM-Anbietern** plus Apple Intelligence auf dem Gerät: Claude, Codex, OpenAI, Gemini, Grok, Mistral, DeepSeek, Qwen, Z.ai, OpenRouter, Ollama, vLLM, LM Studio und weitere.
- **Es hört zu.** Sag *„Agent!“*, gefolgt von einer Aufgabe, oder schreib ihm von deinem iPhone per iMessage (nur freigegebene Absender).

Die README bringt es in einer Zeile auf den Punkt: *Siri antwortet. Agent! handelt.*

## Kein NPM, kein Electron

Am meisten überrascht, was Agent! *nicht* mitbringt. Keine Electron-Hülle, keine Node-Runtime und kein `node_modules`. Jedes Swift-Paket, von dem es abhängt, stammt vom selben Autor, und jedes liegt in einem eigenen Repository in der Organisation [AgentiLoop](https://github.com/AgentiLoop):

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

Das Ergebnis ist eine App, die sehr wenig RAM braucht und Xcode-Automatisierung, Swift-Syntaxanalyse, Accessibility, AppleScript, Safari-Automatisierung und MCP direkt mitbringt.

## Die Schleife im Zentrum

Alles hängt an einer Idee: einer **selbstprüfenden Aufgabenschleife**. Das Modell denkt nach, ruft ein Tool auf, sieht das echte Ergebnis und korrigiert sich selbst. Ein paar Regeln machen diese Schleife vertrauenswürdig:

- **Tools lassen sich nicht vortäuschen.** Jeder Aufruf läuft über einen einzigen Dispatcher und liefert echte Ausgabe. Behauptet das Modell *„Ich habe es angeklickt“*, ohne ein Tool aufzurufen, schleust Agent! eine Korrektur ein.
- **„Fertig“ braucht Belege.** Eine Aufgabe kann sich erst für abgeschlossen erklären, wenn ihre `goal_state`-Kriterien mit Nachweis als erledigt markiert sind – etwa mit einem grünen Build oder einem bestandenen Test.
- **Erst lesen, dann bearbeiten.** Änderungen an einer Datei, die das Modell nicht gelesen hat oder die sich seit dem Lesen auf der Festplatte geändert hat (geprüft per SHA-256), werden abgelehnt. Die Ablehnung liest die Datei gleich für das Modell ein, sodass der nächste Versuch mit aktuellen Zeilen arbeitet.
- **Alles ist umkehrbar.** Jede Änderung wird eine Woche lang als Snapshot gesichert. Du kannst eine einzelne Datei zurücksetzen oder mit `rewind_task` eine ganze Aufgabe zurückspulen.

Jede dieser Regeln nehmen wir in kommenden Beiträgen auseinander.

## AgentScript: Swift mit vollen Berechtigungen

Einer der markantesten Bausteine ist **AgentScript**. Skripte sind ganz normale Swift-Dateien. Agent! kompiliert jedes davon mit SwiftPM zu einer `.dylib` und lädt sie per `dlopen` in den eigenen Prozess. So erbt das Skript die macOS-Berechtigungen von Agent!: Accessibility, Automatisierung, Kalender, Kontakte, Mail, Fotos und so weiter. Zum Schreiben genügt ein einziger Einstiegspunkt:

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

Agent! kann als root laufen – Sicherheit ist hier also keine Folie in einer Präsentation, sondern Code, den du auf GitHub öffnen kannst. Ein fest einprogrammierter `ShellSafetyService` weist katastrophale Befehle ab, bevor sie überhaupt abgeschickt werden, und der privilegierte Daemon führt dieselbe Prüfung auf seiner Seite noch einmal durch. Eine optionale Zweitmeinung namens **Jev** bewertet, wie wahrscheinlich ein Befehl Daten zerstört. Unser [erster Deep Dive](/blog/inside-agent-shell-guardrails/) zeigt genau, wie das funktioniert.

## Die Familie wächst

Dieselbe Agent-Schleife läuft inzwischen auch im Terminal unter macOS, Windows und Linux – als zwei CLIs mit denselben Fähigkeiten: [AgentiLoopCLI](https://github.com/AgentiLoop/AgentiLoopCLI) in Rust und [AgentiLoopGo](https://github.com/AgentiLoop/AgentiLoopGo) in Go. Kleiner Fun Fact aus der README: Agent! für den Mac hat seine kleinen Geschwister selbst geschrieben.

## Was dich hier erwartet

- **Interna:** die Agent-Schleife, Kontextkomprimierung, Tool-Dispatch, Sub-Agents, Gedächtnis und Pläne.
- **Sicherheit:** Schutzmechanismen, das XPC-Vertrauensmodell und was jüngste Agent-Vorfälle Entwicklern lehren.
- **Release Notes mit dem Warum:** was sich in jedem Build geändert hat – und welcher Bug der Auslöser war.
- **Anleitungen:** AgentScript-Rezepte, die Wahl eines Anbieters mit kleinem Budget und ein komplett lokaler Betrieb.
- **Die weitere Agent-Welt:** News und Reviews, immer mit Blick darauf, was sie für deinen Mac bedeuten.

Agent! läuft ab macOS 14.6 auf Apple Silicon und Intel und ist für die private Nutzung kostenlos. Hol es dir unten und schau morgen wieder vorbei.
