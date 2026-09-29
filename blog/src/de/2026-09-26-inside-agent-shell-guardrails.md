---
title: Bevor das Modell mitreden darf: So funktionieren die Shell-Schutzmechanismen von Agent!
description: Wie ShellSafetyService, die zweite Prüfung im Daemon und die Zweitmeinung von Jev verhindern, dass ein KI-Agent deinen Mac löscht – erklärt anhand des echten Swift-Codes.
tags: Sicherheit, Interna
---
Diese Woche berichtete TechRadar, dass ein Coding-Agent in kurzer Zeit rund 48,000 Dateien gelöscht und sich anschließend entschuldigt hat. Die Entschuldigung änderte nichts. Die Dateien waren weg.

Agent! kann Shell-Befehle über einen Launch Agent als du ausführen und über einen Launch Daemon als **root**. Genau das macht es nützlich: Es kann eine SD-Karte flashen, Berechtigungen reparieren oder einen Build-Ordner aufräumen. Es bedeutet aber auch, dass „das Modell wird schon vorsichtig sein“ kein Sicherheitskonzept ist. Deshalb bittet Agent! das Modell gar nicht erst um Vorsicht. Es prüft jeden Befehl im Code, bevor irgendetwas ausgeführt wird – in drei Schichten.

## Schicht 1: ein fest verdrahteter Schutz, den das Modell nicht wegdiskutieren kann

`ShellSafetyService` ist ein schlichtes Swift-`enum` in `Agent/Services/ShellSafetyService.swift`. Der Doc-Kommentar ganz oben gibt den Ton vor: Er läuft *vor jeder Ausführungsschnittstelle* und weist katastrophale Befehle ab, *ohne sie überhaupt abzuschicken*. System-Prompts werden als das bezeichnet, was sie sind: ein zusätzliches Auffangnetz, nicht die Durchsetzungsschicht.

Der Einstiegspunkt erhält den Befehl, den Kontext, in dem er laufen soll, und den Projektordner des Tabs:

```swift
static func check(_ command: String,
                  context: Context = .userAgent,
                  projectFolder: String = "") -> Verdict
```

Ein `Verdict` besteht aus `allowed`, einem menschenlesbaren `reason` und einer kurzen `rule`-ID für das Audit-Log. Die Begründung ist für das Modell geschrieben: Sie geht als Tool-Ergebnis zurück, damit das LLM versteht, *warum* der Befehl abgelehnt wurde, und es nicht einfach erneut versucht.

### Es liest zusammengesetzte Befehle so, wie eine Shell es tut

Ein naiver Filter prüft nur den Anfang des Strings. Angreifer und verwirrte Modelle halten sich nicht daran. `check` zerlegt den Befehl an `;`, `&&`, `||`, `|` und Zeilenumbrüchen und prüft dann **jedes Segment**. Dadurch wird `ls; rm -rf /` blockiert, obwohl die erste Hälfte harmlos ist.

Es gibt eine bewusste Ausnahme von dieser Reihenfolge. Die klassische Fork-Bomb `:(){ :|:& };:` *ist angewiesen* auf `;` und `|` – genau die Zeichen, an denen der Splitter trennt. Deshalb läuft die Fork-Bomb-Prüfung vor dem Zerlegen auf dem gesamten Befehl.

### Es reißt die Verkleidung herunter

Bevor nach `rm` gesucht wird, entfernt eine Hilfsfunktion namens `stripPrefixWrappers` alle Wrapper, die an der Wirkung eines Befehls nichts ändern: `sudo`, `exec`, `command`, `builtin`, `eval` und `doas`. Auch vorangestellte Umgebungszuweisungen wie `FOO=bar` werden entfernt. So greift bei `sudo rm -rf ~` und `FOO=1 exec rm -rf ~` dieselbe Regel wie beim nackten Befehl.

Auch Flags werden geparst statt per Muster abgeglichen. `-rf`, `-fr`, `-Rf`, `-r -f` und `--recursive --force` zählen alle, denn der Parser sucht in jeder Gruppe kurzer Flags nach einem `r` und einem `f` und berücksichtigt zusätzlich die Langformen.

### Was es ablehnt

Das sind die Regel-IDs, die im Quellcode vorkommen:

| Regel | Was sie verhindert |
|---|---|
| `rm.catastrophic` | `rm -rf` auf `/`, einen nackten Glob wie `*` oder `./*` oder dein Home-Verzeichnis in beliebiger Schreibweise (`~`, `~/*`, `$HOME`, `${HOME}/*` oder den ausgeschriebenen Home-Pfad) |
| `rm.no-preserve-root` | `--no-preserve-root`, die explizite Umgehung des Schutzes für `/` |
| `rm.project-folder` | Das rekursive Löschen des Projektordners, in dem der Agent arbeitet, oder das Löschen seines gesamten Inhalts per Glob. Das Löschen eines benannten Unterordners bleibt erlaubt. |
| `rm.dangerous-target` | Weitere gefährliche `rm`-Ziele auf dem Benutzerebenen-Pfad |
| `fork-bomb` | Sich selbst replizierende Prozessbomben |
| `mv.to-devnull` | Das „Löschen“ von Dateien durch Verschieben nach `/dev/null` |
| `find.delete-broad-root` | `find … -delete` ab einem zu weit gefassten Wurzelverzeichnis |
| `perms.recursive-on-root` | Rekursive Rechteänderungen an Pfaden auf Root-Ebene |

Die Projektordner-Regel verdient einen genaueren Blick. Sie entspricht am direktesten dem eingangs geschilderten Vorfall: Ein Agent sollte niemals genau das Projekt löschen, an dem er arbeiten soll – ganz gleich, wie die Anfrage formuliert ist.

### Root wird bewusst anders behandelt

Man könnte erwarten, dass der Root-Daemon die *strengsten* Regeln bekommt. Er bekommt die engsten. Der Kommentar erklärt, warum: Der Daemon existiert für Arbeit auf Systemebene, etwa das Klonen von Datenträgern oder `mkfs`, und er „sollte uns nicht im Weg stehen“. Im Kontext `.rootDaemon` springt `check` daher direkt zu `checkCatastrophicRm`, das nur die drei nicht wiedergutzumachenden Muster blockiert (`/`, nackte Globs und das Home-Verzeichnis) sowie `--no-preserve-root` und das Löschen des Projektordners. Alles andere liegt in der Verantwortung des Operators.

Diese Designentscheidung ist es wert, übernommen zu werden. Ein Schutz, der legitime Admin-Arbeit blockiert, wird irgendwann abgeschaltet. Ein Schutz, der nur nicht wiedergutzumachende Fehler blockiert, bleibt aktiv.

## Schicht 2: Der Daemon prüft noch einmal

Die App führt `ShellSafetyService.check` aus, bevor sie irgendetwas abschickt. Die Helper verlassen sich nicht einfach darauf. In `Shared/DaemonCore.swift` führt der Daemon direkt nach dem Schreiben des Audit-Log-Eintrags **dieselbe Prüfung** auf seiner Seite aus:

```swift
// Defense-in-depth: the app already runs this same check before
// dispatching, but any same-team-signed client can reach the mach
// service directly.
let verdict = ShellSafetyService.check(
    script,
    context: auditCategory == .launchDaemon ? .rootDaemon : .userAgent,
    projectFolder: workingDirectory
)
```

Ein blockierter Befehl wird mit seiner Regel-ID als abgelehnt protokolliert und erhält den Exit-Status 126. Er erreicht `/bin/zsh` nie. Das ist wichtig, weil die XPC-Listener jeden Client akzeptieren, der vom selben Team signiert ist. Verbindet sich etwas anderes, das von diesem Team signiert ist, direkt mit dem Mach-Service, stößt es trotzdem auf den Schutz.

## Schicht 3: Jev, eine Zweitmeinung für das, was Muster übersehen

Musterregeln sind präzise, kennen aber nur die Muster, die man aufgeschrieben hat. Viele zerstörerische Befehle sehen nicht aus wie `rm -rf /`: ein `truncate` auf die falsche Datei, ein SQL-`DROP`, das per Pipe an eine CLI geht, ein `dd` in die falsche Richtung.

Hier kommt **Jev** ins Spiel, eine optionale beratende Schicht in `JevAdvisor.swift`. Jeder Befehl, der `ShellSafetyService` bereits *passiert* hat, geht an Jev, das bewertet, wie wahrscheinlich er Daten unwiderruflich zerstört. Liegt der Wert über deinem Schwellenwert, lehnt Agent! mit einer klaren Meldung ab:

```text
Refused: Jev rated this command 85% likely to irreversibly destroy data.
Command: …
Narrow the target or run it yourself if this is intentional.
```

Einige Details zeigen, wie sorgfältig der Einsatzbereich abgesteckt wurde:

- **Es ergänzt, ersetzt aber nie.** Der Code-Kommentar ist eindeutig: `ShellSafetyService` ist die Durchsetzungsschicht, und Jev fängt nur ab, was den Musterregeln entgeht. Deshalb ist der Schwellenwert bewusst hoch. Standardmäßig liegt er bei **70%**, und du kannst ihn in den Einstellungen in 10%-Schritten zwischen 0 und 100% anpassen.
- **Im Fehlerfall lässt es durch – aber nicht stillschweigend.** Kein Schlüssel, deaktivierter Schalter oder ein Netzwerkausfall bedeuten „keine Meinung“, sodass ein wackeliger Dienst deine Aufgabe nie ausbremsen kann. Der Fehler wird trotzdem protokolliert (`⚠️ Jev check failed, command allowed`), damit ein abgelaufener Schlüssel nie mit „Jev hält es für sicher“ verwechselt wird.
- **Abbrechen heißt abbrechen.** Stoppst du eine Aufgabe, während Jev noch überlegt, wird der Befehl nicht ausgeführt.
- **Jedes Urteil ist sichtbar.** Jede Prüfung protokolliert den Risikoprozentsatz, ob der Befehl erlaubt oder abgelehnt wurde, welches Modell geantwortet hat und die Token-Zahlen.

## Getestet, nicht angenommen

`AgentTests/ShellSafetyServiceTests.swift` enthält 30 Tests für den Schutzmechanismus. Und weil jeder Helper-Befehl vor seiner Ausführung ins Audit-Log geschrieben wird, lässt sich jederzeit nachvollziehen, was der Agent versucht hat – auch das, was er nicht durfte.

## Die Lehre für alle, die Agenten bauen

1. **Im Code durchsetzen, nicht im Prompt.** Prompts sind Vorschläge. Ein Swift-`enum` ist es nicht.
2. **So parsen, wie die Shell parst.** Zusammengesetzte Befehle zerlegen, Wrapper entfernen und Flags normalisieren.
3. **An der privilegierten Grenze erneut prüfen.** Nicht darauf vertrauen, dass der eigene Client der einzige Aufrufer ist.
4. **Das Unwiderrufliche blockieren, nicht das Ungewöhnliche.** Enge Regeln bleiben bestehen, lärmende werden abgeschaltet.
5. **Urteilsvermögen obendrauf setzen – und Ausfälle sichtbar machen.** Eine Zweitmeinung ist nur dann wertvoll, wenn man erkennt, wann sie nicht geantwortet hat.

All das ist offen auf [GitHub](https://github.com/AgentiLoop/Agent) einsehbar. Lies es, such nach Schwachstellen und eröffne ein Issue, wenn du einen Befehl findest, der hätte gestoppt werden müssen.
