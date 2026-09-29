---
title: Das Terminal schlägt zurück: Der Agent-Loop wird plattformübergreifend in Rust und Go
description: Agent! ist eine Mac-App, aber ein Coding-Agent gehört dorthin, wo Entwickler arbeiten. So wurden aus dem Agent-Loop zwei CLIs, eine in Rust und eine in Go, mit einer Vollbild-TUI unter macOS, Windows und Linux.
tags: Ankündigung, Plattformübergreifend, Engineering
---
Die meiste Zeit seines Bestehens war Agent! eine stolze Mac-App: natives Swift und SwiftUI, tiefe Anbindung an AppleScript und Bedienungshilfen und ein Launch Daemon für root. Das ist nach wie vor das Flaggschiff. Doch in den letzten Tagen hat sich etwas daran geändert, wie wir über Coding-Agents denken, und heute erscheint es.

**Der Agent-Loop läuft jetzt in deinem Terminal, unter macOS, Windows und Linux.** Es gibt ihn in zwei Editionen mit denselben Fähigkeiten: [AgentiLoopCLI](https://github.com/AgentiLoop/AgentiLoopCLI) in Rust und [AgentiLoopGo](https://github.com/AgentiLoop/AgentiLoopGo) in Go. Und ja, Agent! für Mac hat einen Großteil seiner eigenen kleinen Geschwister selbst geschrieben.

## Der Paradigmenwechsel: zurück ins Terminal

Die erste Welle von KI-Coding-Tools lebte in Editoren und Chatfenstern. Die Welle, die sich gerade durchsetzt, lebt im **Terminal**. Dafür gibt es gute Gründe:

- **Im Terminal findet die Arbeit ohnehin statt.** Builds, Tests, git, Paketmanager und SSH-Sitzungen leben alle dort. Ein Agent im Terminal braucht nicht für alles eine eigene Integration; er hat `bash`.
- **Es läuft überall.** Eine CLI läuft auf einer Linux-Build-Maschine, in einem Container, per SSH auf einem Raspberry Pi oder in einer Windows-Entwicklungs-VM. Eine Mac-App läuft auf einem Mac.
- **Es lässt sich kombinieren.** Der One-Shot-Modus (`agentiloop "explain this project"`) passt direkt in Skripte und CI.
- **Es ist ehrlich darüber, was es tut.** Jeder Tool-Aufruf, jeder Diff und jede Berechtigungsabfrage läuft als Klartext durch.

Die Superkräfte der Mac-App, etwa Photo Booth über Bedienungshilfen zu steuern oder Mail mit ScriptingBridge zu automatisieren, gibt es tatsächlich nur auf dem Mac. Der **Agent-Loop** dagegen ist nicht an den Mac gebunden. Nachdenken, ein Tool aufrufen, das echte Ergebnis lesen, korrigieren und wiederholen: Das funktioniert auf jedem Betriebssystem mit einer Shell und einem Dateisystem. Also haben wir den Loop herausgelöst.

## Warum zwei Sprachen?

Wir hätten uns für eine entscheiden können. Stattdessen haben wir dasselbe Design zweimal portiert, und zwar mit Absicht.

**Rust (AgentiLoopCLI)** kam zuerst. Der Workspace wurde am 20. September mit einem Kern-Loop, dem Anthropic-Provider, eingebauten Tools und der CLI aufgesetzt. Er ist in fünf Crates aufgeteilt: `agentiloop-core` (der Loop, Nachrichten, Sitzungen und Berechtigungen), `agentiloop-provider`, `agentiloop-tools`, `agentiloop-mcp` und `agentiloop-cli`. Er läuft auf `tokio`, nutzt `reqwest` mit `rustls`, sodass man sich unter Windows nicht mit OpenSSL herumschlagen muss, und zeichnet seine TUI mit `ratatui`. Markdown läuft durch `pulldown-cmark`, und Code bekommt Syntaxhervorhebung von `syntect`.

**Go (AgentiLoopGo)** ist heute in einer Reihe von Commits gelandet: der Kern (Nachrichten, Agent-Loop, Kompaktierung, Sitzungen und Berechtigungen) mit Tests, dann die Provider, dann der MCP-Client, dann die CLI mit REPL, TUI, Markdown, Syntaxhervorhebung, Sitzungen und Slash-Befehlen. Sie zeichnet die TUI mit `tcell`, rendert Markdown mit `goldmark`, hebt Syntax mit `chroma` hervor und übernimmt die Zeilenbearbeitung mit `liner`. Ihr Release-Workflow zielt auf dieselben fünf Plattformen wie die Rust-Edition.

Es zweimal zu machen, ist das beste Design-Review, das es gibt. Alles, was eigentlich ein Rust-Ismus oder ein Go-Ismus war, fällt sofort auf, und was übrig bleibt, ist die eigentliche Architektur. Es gibt auch einen praktischen Vorteil: Wähl die Toolchain, der dein Team bereits vertraut. Und dann sag uns, welche es besser macht. 🦀 vs 🐹

## Derselbe Loop, weniger Angriffsfläche

Beide CLIs starten bewusst mit einem kleinen, scharfen Werkzeugsatz:

| Tool | Was es tut | Fragt vorher? |
|---|---|---|
| `read_file` | Liest eine Datei mit Zeilennummern | Nein |
| `list_dir` | Listet einen Ordner auf | Nein |
| `write_file` | Erstellt oder überschreibt eine Datei | **Ja** |
| `edit_file` | Ersetzt ein exaktes Textstück | **Ja** |
| `bash` | Führt einen Befehl aus (`sh -c` auf Mac und Linux, `cmd /C` unter Windows) | **Ja** |

Mehr gewünscht? Beide Editionen enthalten einen MCP-Client, portiert vom hauseigenen AgentMCP von Agent!, der stdio, Streamable HTTP und das ältere HTTP+SSE unterstützt, sodass sich die Tools jedes MCP-Servers direkt einbinden lassen.

Berechtigungen sind Teil des Kerns und nicht nachträglich an die Oberfläche angeflanscht. In Rust entscheidet ein `PermissionPolicy`-Trait, ob ein Aufruf ausgeführt werden darf, basierend auf dem Tool-Namen, darauf, ob er etwas verändert, und auf seiner Eingabe. Die Antwort lautet `Allow`, `Deny` oder `Cancel`. Diese dritte Option gibt es wegen eines echten Ärgernisses: Ein Druck auf **Esc** bei einer Berechtigungsabfrage sollte *nur diesen einen Aufruf* überspringen, nicht die gesamte Aufgabe beenden. Die CLI liefert eine interaktive Richtlinie, Tests und CI verwenden `AllowAll`.

## Plattformübergreifend steckt im Detail

„Läuft unter Windows“ ist leicht behauptet und schwer eingelöst. Einiges davon, was dafür nötig war:

- **Einen außer Kontrolle geratenen Befehl wirklich beenden.** Wenn `bash` in ein Timeout läuft, reicht es nicht, die Shell zu beenden, falls die Shell Kindprozesse gestartet hat. Die Go-Edition beendet den gesamten Prozessbaum: eine Prozessgruppe unter Unix und `taskkill /T` unter Windows. Der Code ist auf `proc_unix.go` und `proc_windows.go` aufgeteilt.
- **CI auf allen drei Betriebssystemen.** Das Go-Repo führt CI unter macOS, Linux und Windows aus, und der Rust-Release-Workflow baut fünf Binaries: macOS arm64 und x86_64, Linux x86_64 und arm64 sowie Windows x86_64.
- **Signierte Mac-Binaries.** Der Release-Workflow kann die macOS-Builds signieren und notarisieren, damit Gatekeeper sie nicht blockiert.
- **Keine Konfigurationsdatei-Archäologie.** Die CLI merkt sich, wie du sie gestartet hast: Provider, Modell, TUI-Modus und Sitzung. Nach dem ersten Start macht ein bloßes `agentiloop` genau dort weiter, wo du aufgehört hast.

## Eine TUI, die sich wie eine App anfühlt

Es gibt drei Möglichkeiten, sie zu starten: die Vollbild-**TUI** (`agentiloop --tui`), einen zeilenweisen **Chat**-Modus für einfache Terminals und **One-Shot** für Skripte. Die TUI hatte ein paar arbeitsreiche Tage:

- eine animierte Aktivitätsanzeige im Eingabefeld, mit Spinner, aktueller Tätigkeit und verstrichener Zeit
- Messung der Tokens pro Sekunde
- anklickbare Links
- ein Prompt-Verlauf, der über Neustarts hinweg erhalten bleibt
- fortgesetzte Sitzungen, die die vorherige Unterhaltung anzeigen, damit du nicht auf einen leeren Bildschirm starrst
- `/model`, gestützt auf die Live-Modellliste des Providers

Und wenn ein API-Schlüssel fehlt oder falsch ist, sagt sie das in klaren Worten und nennt den tatsächlichen Provider, statt einfach einen 401 auszuspucken.

## Provider

Vom ersten Tag an funktioniert sie mit Claude (API-Schlüssel oder Claude-Code-OAuth-Token in derselben Zugangsangabe, wobei das Authentifizierungsschema automatisch erkannt wird), OpenAI und jedem OpenAI-kompatiblen Server, lokalen Modellen über Ollama oder LM Studio sowie **oMLX** auf Apple Silicon. Adresse und Schlüssel von oMLX liest sie automatisch aus `~/.omlx/settings.json`.

## Probier die Vorabversion aus

Heute veröffentlichen wir **v0.0.1** als Vorabversion. Sie ist noch früh dran und entwickelt sich schnell, und wir wollen dein Feedback jetzt, solange Änderungen noch wenig kosten. Hol dir ein Binary von den [Rust-Releases](https://github.com/AgentiLoop/AgentiLoopCLI/releases) oder baue die Go-Edition aus dem [Quellcode](https://github.com/AgentiLoop/AgentiLoopGo).

Die Mac-App bleibt. Wenn du einen Mac nutzt, kann Agent! weiterhin Dinge, die kein Terminal kann. Aber wenn du dir schon immer denselben Agenten auf dem Linux-Server, dem Windows-Laptop und dem Raspberry Pi gewünscht hast: Hier ist er.
