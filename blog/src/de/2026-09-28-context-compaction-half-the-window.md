---
title: Warum Agent! bei halbem Kontextfenster komprimiert – und die drei Bugs, die es auf 16K schrumpfen ließen
description: Wie die Kontextkomprimierung von Agent! entscheidet, wann eine lange Aufgabe zusammengefasst wird, und die Fixes vom 28. September für Fallback-Modelle, Ollama und ein 272K-Fenster bei Codex.
tags: Interna, Release Notes
---
Lange Agent-Aufgaben haben ein physikalisches Problem. Jeder Tool-Aufruf hängt seine Ausgabe an das Transkript an: eine gelesene Datei, ein Build-Log, ein Diff. Irgendwann passt das Transkript nicht mehr ins Kontextfenster des Modells, und der Anbieter lehnt die Anfrage ab. Ein Agent, der die ganze Nacht durchläuft, muss deshalb **komprimieren**: Er verkleinert die Unterhaltung und behält dabei das, worauf es ankommt.

Die Komprimierung steckt in `Agent/AgentViewModel/Messages/Compression.swift`. Am 28. September bekam sie an einem einzigen Abend drei Fixes, alle für dasselbe Symptom: Aufgaben, die bei 16K Tokens komprimiert wurden, obwohl die Modelle weit größere Fenster haben. So funktioniert das System – und das ist schiefgelaufen.

## Wann komprimiert wird: bei halbem Fenster, mit Obergrenze

Auslöser ist ein Struct namens `CompactionState`. Sein Kern ist eine einzige Funktion:

```swift
static func threshold(for contextWindow: Int, maxTokens: Int = 0) -> Int {
    let byFraction = Int(Double(min(contextWindow, compactionWindowCap)) * compactionFraction)
    let reservedOutput = maxTokens > 0 ? min(maxTokens, contextWindow / 2) : 8_192
    return max(2_000, min(byFraction, contextWindow - reservedOutput))
}
```

Mit `compactionFraction = 0.5` und `compactionWindowCap = 256_000` bedeutet das:

- **Komprimieren bei 50% des Fensters.** Es ist ein Prozentsatz statt einer festen Token-Zahl. Die andere Hälfte ist das Ausgabebudget, sodass Eingabe und Ausgabe immer zusammen hineinpassen.
- **Nie über 128K.** Fenster, die mit mehr als 256K beworben werden (Claude 1M, MiniMax 1M, Gemini und Grok 2M), komprimieren alle bei 128K. Ein 200K-Fenster komprimiert bei 100K.
- **Immer Platz für die Antwort lassen.** Der Schwellenwert darf nie so spät liegen, dass die reservierte Ausgabe nicht mehr hineinpasst.
- **Nie unter 2K** – als Untergrenze für winzige lokale Modelle.

Warum ein 2M-Fenster bei 128K deckeln? Der Kommentar ist unmissverständlich. Bei riesigen beworbenen Fenstern verzögert ein ungedeckelter Prozentsatz die Komprimierung so lange, dass jede Abweichung auf Anbieterseite zu einem harten Kontextüberlauf statt zu einer Komprimierung führt. Beispiele sind ein Router, der ein kleineres Fenster ausliefert, als er meldet, oder ein falsch gezählter System-Prompt. Früh zu komprimieren kostet eine Zusammenfassung. Zu spät zu komprimieren kostet die Aufgabe.

## Messen: erst dem Anbieter vertrauen, dann schätzen

Um mit dem Schwellenwert zu vergleichen, braucht man eine Token-Zahl. Aus Zeichen zu raten ist ungenau, deshalb bevorzugt `measuredTokens` den echten Wert: die `input_tokens`, die der Anbieter für die letzte Anfrage gemeldet hat. Diese Zahl berücksichtigt den System-Prompt und die Tool-Schemas, die eine lokale Schätzung nicht sehen kann. Nur Nachrichten, die *seit* dieser Meldung hinzugekommen sind, werden geschätzt.

Ohne Meldung greift die klassische Schätzung Zeichen ÷ 4, aufgeschlagen um 25%, weil dichter Code eher bei 3.3 Zeichen pro Token liegt. Bevor die Schleife allein auf Basis einer Schätzung für eine Komprimierung bezahlt, bestätigt sie diese mit einem Zähler auf dem Gerät.

## Wie komprimiert wird: in Stufen

Wird der Schwellenwert überschritten, arbeitet `tieredCompact` eine Reihe zunehmend drastischer Schritte ab:

1. **Stufe 0: eine strukturierte Zusammenfassung** des *gesamten* Transkripts durch das aktive Modell. Sie läuft zuerst, damit das zusammenfassende Modell die Tool-Ausgaben, die es zusammenfasst, noch sieht.
2. **Mikrokomprimierung:** Alte Tool-Ergebnisse werden zu kurzen, wiederherstellbaren Platzhaltern. Das Tool `restore_tool_result` kann jeden davon zurückholen.
3. **Bilder entfernen:** Screenshots sind riesig und lassen sich schlecht zusammenfassen.
4. **Stufe 1: Zusammenfassung mit Apple Intelligence,** schnell und auf dem Gerät.
5. **Stufe 2: aggressives Beschneiden,** bei dem mittlere Nachrichten zu einer Zusammenfassung verdichtet werden.

Ein Kommentar fasst die Philosophie zusammen: Die strukturelle Komprimierung „ist ein Sicherheitsmechanismus, kein Feature“. Sie läuft selbst dann, wenn du Token Compression ausschaltest. Nur die Apple-Intelligence-Stufe respektiert diesen Schalter.

Nach der Komprimierung bekommt das Modell zurück, was ihm am meisten fehlen würde: offene Zielkriterien, die Checkliste des aktiven Plans und den aktuellen Inhalt von bis zu fünf Dateien, die es während der Aufgabe bearbeitet hat (insgesamt etwa 10K Tokens). Auch der Deduplizierungs-Cache für Lesezugriffe wird zurückgesetzt, sodass eine Datei wieder erneut gelesen werden darf.

Schließlich gibt es einen **Circuit Breaker**. Nach drei Komprimierungen in Folge, die das Transkript nicht verkleinern, hört die Schleife auf, es zu versuchen. Endgültig gibt sie aber nicht auf: Sobald das Transkript um weitere 25% über den letzten fehlgeschlagenen Versuch hinaus gewachsen ist, probiert sie es erneut.

## Die Bugs: drei Wege zu 16K

Jeder Fix vom 28. September lief auf dieselbe Zahl hinaus. Ein Fallback-Fenster von 32K ergibt `min(16K, 32K − 8K) = 16K`. Für ein Modell mit 200K+ bedeutet Komprimieren bei 16K, dass fast ununterbrochen zusammengefasst wird und Dateien vergessen werden, die das Modell gerade erst gelesen hat.

### 1. Das Fallback-Modell lieh sich das falsche Fenster

Agent! unterstützt eine Fallback-Kette. Liefert ein Anbieter einen 429 zurück, läuft in ein Timeout oder fällt aus dem Netz, geht die Aufgabe beim nächsten konfigurierten Anbieter weiter. Tabs können zudem das Modell überschreiben. `contextWindow(for:)` suchte jedoch das Fenster des *global ausgewählten* Modells des Anbieters heraus, nicht das des tatsächlich laufenden. Bei einem Fallback-Modell ohne eigenen Eintrag fiel es auf die statische Größe von 32K zurück.

Der Fix nimmt das Modell in die Abfrage auf:

```swift
func contextWindow(for provider: APIProvider, model: String? = nil) -> Int
```

Jede Aufrufstelle übergibt jetzt das verwendete Modell: die Hauptschleife, Tab-Aufgaben, der Fallback-Pfad und Sub-Agents.

### 2. Ollama vergaß, was es gelernt hatte

Lokale Server melden ihr echtes Fenster pro Modell asynchron: Ollama über `/api/show`, LM Studio über `/api/v0/models` und vLLM über `/v1/models`. Deshalb ruft die Schleife ab der zweiten Iteration bei jedem Durchlauf `refreshThreshold` auf. Ein Abruf, der erst nach dem Start der Aufgabe eintrifft, wirkt sich so trotzdem aus.

Bei Ollama wurden die abgerufenen Fenster allerdings nicht gespeichert, sodass die Komprimierung immer wieder auf den Standardwert von 16K zurückfiel. Der Fix speichert abgerufene Kontextfenster dauerhaft und fragt sie beim Start der Aufgabe ab, wenn das Fenster unbekannt ist. Er kam zusammen mit einer neuen Testsuite, `OllamaContextWindowTests.swift`.

### 3. Ein großzügiges Ausgabebudget fraß das Eingabebudget auf

Dieser Fall ist subtil. Codex meldet für sein Modell GPT-6 Astra ein Fenster von 272K. Ein Nutzer setzt **Max Output Tokens** auf 256K. Der alte Code reservierte das komplette Ausgabebudget:

```text
272K − 256K = 16K   →   threshold = min(128K, 16K) = 16K
```

Der neue Code reserviert höchstens die Hälfte des Fensters für die Ausgabe:

```swift
let reservedOutput = maxTokens > 0 ? min(maxTokens, contextWindow / 2) : 8_192
```

Derselbe Fall ergibt jetzt `min(128K, 272K − 136K) = 128K`. Die prozentuale Obergrenze verwendet weiterhin das gedeckelte Fenster, die Prüfung, ob die Ausgabe hineinpasst, aber das *tatsächliche* Fenster. Andernfalls würde Claudes Standard-Ausgabebudget von 500K bei einem 1M-Fenster `window − maxTokens` negativ machen und den Schwellenwert auf die Untergrenze von 2K drücken.

## Warum das für dich wichtig ist

Wenn du lange Aufgaben ausführst – vor allem nächtliche Coding-Sessions – und dabei Fallback-Anbieter oder lokale Modelle nutzt, sollten diese Aufgaben jetzt deutlich mehr Arbeitskontext behalten. Das heißt weniger „Ich muss diese Datei noch einmal lesen“-Schleifen, weniger verlorene Details und weniger Tokens, die für Zusammenfassungen draufgehen. Diese Fixes wurden am 28. September zusammen mit Version 1.1.77 (Build 277), Release Candidate 6, ausgeliefert – gemeinsam mit einer anbieterübergreifenden Erkennung von Kontextüberlauf- und `max_tokens`-Fehlern.

Die Lehre für alle, die Agenten bauen, ist allgemeingültig: **Bemiss dein Gedächtnis am Modell, das tatsächlich läuft**, vertraue den Token-Zahlen des Anbieters mehr als deinen eigenen Schätzungen und deckle jedes Budget, damit keine einzelne Einstellung die anderen aushungern kann.
