---
title: Agent! läuft jetzt unter macOS 14.6 und auf Intel-Macs: Wie wir uns von macOS 26 gelöst haben
description: Agent! wurde rund um Apple Intelligence unter macOS 26 entwickelt. So hat ein Tag voller #available-Prüfungen und Paket-Updates es auf macOS 14.6 gebracht, auf Apple Silicon und Intel.
tags: Versionshinweise, Engineering
---
Bis heute setzte Agent! macOS 26 voraus. Ab der heutigen Vorabversion läuft es unter **macOS 14.6 oder neuer, auf Apple Silicon und Intel**. Damit sind viele völlig brauchbare Macs abgedeckt, die bisher außen vor waren und von denen viele Apple Intelligence überhaupt nicht ausführen können.

Hier ist, was dafür nötig war, Commit für Commit, an einem einzigen Tag.

## Das Hindernis: FoundationModels

Agent! nutzt Apples On-Device-Modell über das Framework **FoundationModels**, das es nur unter macOS 26 gibt. Es ist nicht das Hauptgehirn, darum kümmert sich der Anbieter deiner Wahl. Aber es übernimmt mehrere Aufgaben: schnelle Zusammenfassungen bei der Kontextkomprimierung, Token-Zählung auf dem Gerät, eine vorgewärmte Sitzung beim Start und etwas Triage.

Code, der einen Typ aus macOS 26 referenziert, lässt sich für ein älteres Deployment-Ziel nicht bauen. Also bestand Schritt eins (`ea5ce624`) darin, **jede** Verwendung von FoundationModels hinter `#available(macOS 26, *)` zu stellen. Das betraf `FoundationModelService`, `AppleIntelligenceMediator`, das Vorwärmen in `AgentApp`, die Komprimierungszusammenfassungen und die Token-Zählung in `Compression.swift` sowie `AboutSelf`.

## Der Trick: Typ-Löschung für die gespeicherte Eigenschaft

`#available` funktioniert für Codepfade, aber nicht für eine gespeicherte Eigenschaft. Eine Klasse kann kein `LanguageModelSession?` halten, wenn der Typ auf dem laufenden Betriebssystem nicht existiert. Die Lösung: Man speichert es als `AnyObject?` und castet es dort zurück, wo es verwendet wird, innerhalb von abgesichertem Code:

```swift
/// Type-erased `LanguageModelSession` so the stored property compiles below macOS 26.
private(set) var session: AnyObject?

@available(macOS 26.0, *)
var transcript: Transcript? {
    (session as? LanguageModelSession)?.transcript
}
```

Wie es in der Commit-Nachricht heißt, „ziehen“ die gespeicherten Eigenschaften „den Framework-Typ nicht mehr ins Klassenlayout“.

Auch die Verfügbarkeitsprüfungen liefern jetzt eine ehrliche Antwort für ältere Systeme:

```swift
static var unavailabilityReason: String {
    guard #available(macOS 26.0, *) else { return "Apple Intelligence requires macOS 26 or later." }
    ...
}
```

Unter macOS 14 oder 15 wird Apple Intelligence also einfach mit einer klaren Begründung als nicht verfügbar angezeigt, und alles andere funktioniert. Unter macOS 26 ändert sich nichts.

## Der lange Rattenschwanz: zehn Pakete

Agent! besteht aus eigenen Swift-Paketen, und jedes davon deklarierte sein eigenes Mindest-Betriebssystem. Commit `4d7fca86` hob alle zehn auf Versionen an, die `.macOS(.v14)` deklarieren:

| Paket | Version |
|---|---|
| AgentAccess | 2.10.24 |
| AgentAudit | 1.3.9 |
| AgentColorSyntax | 1.2.8 |
| AgentD1F | 1.0.15 |
| AgentEventBridges | 1.1.8 |
| AgentLLM | 1.0.8 |
| AgentMCP | 1.6.10 |
| AgentSwift | 1.1.11 |
| AgentTerminalNeo | 1.37.9 |
| AgentTools | 2.53.19 |

An Tagen wie diesem zahlt es sich aus, alle Abhängigkeiten selbst in der Hand zu haben. Kein Warten auf einen externen Maintainer, nur zehn Tags.

## Die Überraschung: 26.4

Eine API brauchte mehr als eine Prüfung auf 26.0. `SystemLanguageModel.tokenCount(for:)` gibt es erst ab **macOS 26.4**, also wurde ihre Verfügbarkeitsprüfung von 26.0 auf 26.4 angehoben. Ohne das hätte ein Mac mit 26.0 bis 26.3 versucht, eine Methode aufzurufen, die es noch gar nicht gibt. Eine gute Erinnerung daran, dass „das Framework ist verfügbar“ und „diese Methode ist verfügbar“ nicht dieselbe Frage sind.

## Was du auf älteren Macs bekommst

Unter macOS 14.6 und 15, auf Apple Silicon oder Intel, funktioniert Agent! genauso:

- alle 23 Cloud- und lokalen LLM-Anbieter
- die vollständige Werkzeugschleife: Programmieren, Xcode-Builds, git, Shell als du selbst oder als root, Bedienungshilfen, AppleScript, JXA, AgentScript, Safari-Automatisierung und MCP
- Kontextkomprimierung, die die eigenen Zusammenfassungen des Modells und die Token-Zählungen des Anbieters nutzt, nur eben ohne die Apple-Intelligence-Stufe

Nur die On-Device-Funktionen von Apple Intelligence setzen macOS 26 voraus.

## Jetzt holen

Jede Version und Vorabversion wird als signierte, notarisierte und mit Staple versehene Binärdatei ausgeliefert. Du musst nie aus dem Quellcode bauen:

```sh
brew update && brew install --cask agentiloop-agent
```

Oder lade die `.dmg` von [GitHub Releases](https://github.com/AgentiLoop/Agent/releases) herunter. Wenn du mit einem älteren MacBook oder einem Intel-Mac-mini gewartet hast: Heute ist der Tag.
