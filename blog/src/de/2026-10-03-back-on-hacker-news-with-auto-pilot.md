---
title: Zurück auf Hacker News, sechs Monate später, mit Auto-Pilot
description: Agent! ist wieder auf Hacker News, als Show HN. Der Thread im April drehte sich um ein natives Coding-Harness für den Mac; dieser dreht sich um Auto-Pilot, die zielgesteuerte Schleife, die so lange Zyklen ausführt, bis das Ziel erreicht ist, und um das Spiel im Stil von Mario Kart, das sie seitdem baut. Hier ist der Beitrag, was hinter jeder Behauptung darin steckt und wo man in die Diskussion einsteigen kann.
tags: Auto-Pilot, Community, Hacker News
---
Agent! ist heute wieder auf Hacker News, als Show HN: [Show HN: AgentiLoop Agent Mac GUI Agent Loop for macOS 14.6 or Later](https://news.ycombinator.com/item?id=49948810). Wenn ihr ein Hacker-News-Konto habt, ist dieser Thread der Ort, um Fragen zu stellen, Schwachstellen zu suchen und uns zu sagen, was ihr euch von einem Mac-Agenten wünscht. Dieser Beitrag ist die lange Fassung des Einreichungstextes, mit einem Verweis auf die Quelle jeder darin enthaltenen Behauptung.

## Das Ausgangsmaterial

Die Einreichung ist kurz, hier ist sie also vollständig, zitiert aus [dem Hacker-News-Eintrag](https://news.ycombinator.com/item?id=49948810):

> Agent! erschien ursprünglich im vergangenen April auf Hacker News. Seitdem hat sich viel verändert. Kürzlich wurde eine neue Funktion namens Auto-Pilot entwickelt. Sie bekommt ein Ziel und hört nicht auf, bis das Ziel erreicht ist. Man kann es sich als Tasks auf Steroiden vorstellen. Was Agent macht, ist, mehrere Tasks zu erstellen. Jeder Task wird als Zyklus bezeichnet. Standardmäßig haben Auto-Pilots, die mit auto [Ziel] gestartet werden, keinen Zeitrahmen. Agent! wird angewiesen weiterzulaufen, bis sein Ziel erreicht ist. Auto-Pilot hat einen Notausschalter, einen „Stop All“-Button. Der Nutzer kann mit auto stop auch nur den aktuellen Zyklus beenden und mit auto stop all alles beenden. Im November wird ein Nutzer mehrere Auto-Pilots im selben Projekt laufen lassen können. Und ein Auto-Pilot-Tab wird automatisch weitere Tabs erzeugen können. Derzeit entwickeln wir einen Mario-Kart-ähnlichen Klon namens „GoKart“, geschrieben in GoDot 4. Bisher wurden über 20 Stunden Entwicklung und Verbesserung des Spiels aufgezeichnet. *(aus dem Englischen übersetzt)*

Alles Weitere unten baut auf jeweils einem Satz davon auf.

## „Agent! erschien ursprünglich im vergangenen April auf Hacker News“

Der erste Thread war [Agent — Native macOS coding IDE/harness](https://news.ycombinator.com/item?id=47787127) am 16. April 2026: 83 Punkte und 54 Kommentare. Die App setzte damals macOS 26.4 und Apple Silicon voraus, hatte 17 LLM-Anbieter und wurde vor allem als Coding-Harness vorgestellt, das über die Accessibility-API auch Mac-Apps steuern konnte. Beide Threads sind im Abschnitt [Reviews](/#reviews) dieser Seite aufgeführt, zusammen mit den unabhängigen Artikeln, die dazwischen erschienen sind.

Seit April: Unterstützung für macOS 14.6 und Intel ([die Geschichte dieser Portierung](/blog/sonoma-intel-and-the-mac-that-was-not-dead-yet/)), 23 Anbieter, [Kontextkompaktierung, von der man sich erholen kann](/blog/context-compaction-half-the-window/), eine [CLI in Rust und Go](/blog/agent-1-1-87-and-agentiloop-cli-0-0-5/) für Mac, Windows und Linux, ein Release am Ersten jedes Monats und die Funktion, um die es in der neuen Einreichung eigentlich geht.

## „Sie bekommt ein Ziel und hört nicht auf, bis das Ziel erreicht ist“

Auto-Pilot ist der Befehl `/auto` in Agent! für Mac. Aus dem Abschnitt Auto-pilot der README: Er führt die Task-Schleife in unbeaufsichtigten Zyklen aus, im Haupt-Tab oder in jedem beliebigen LLM-Tab, bis ein Ziel erreicht ist, ein Zeitbudget aufgebraucht ist oder ihr auf Stop drückt. Es gibt kein Zyklenlimit und keine Obergrenze für Iterationen pro Zyklus. Wenn der Task eines Zyklus endet und das Ziel nicht erreicht ist, startet der nächste Zyklus automatisch.

| Befehl | Was er tut |
|---|---|
| `/auto <goal>` | Auf das Ziel hinarbeiten, bis das LLM meldet, dass es erreicht ist |
| `/auto 4h <goal>` | Dasselbe, aber nach 4 Stunden stoppen (`30m`, `1.5h` funktionieren auch) |
| `/auto` | Erst das Projekt sichten, dann euch nach dem Ziel fragen |
| `/auto history`, `/auto last`, `/auto #N` | Frühere Ziele auflisten, das jüngste oder das N-te neu starten |
| `/auto status` / `/auto stop` | Die Sitzung anzeigen oder sie nach dem aktuellen Zyklus beenden |

„Man kann es sich als Tasks auf Steroiden vorstellen“ ist das richtige mentale Modell. Jeder Zyklus *ist* ein normaler Agent!-Task, mit denselben Werkzeugen, denselben Leitplanken (Lesen vor dem Bearbeiten, goal_state-Nachweise, Shell-Sperrliste) und demselben `done()`-Vertrag. Was Auto-Pilot hinzufügt, ist die Schleife drumherum: Die Zusammenfassung des Zyklus wird an `.agent/autopilot/progress.md` im Projekt angehängt und in den Prompt des nächsten Zyklus eingespeist, sodass jeder Zyklus damit beginnt zu lesen, was die vorherigen getan, angenommen und offen gelassen haben. Die Sitzung endet erst, wenn das LLM seine abschließende Zusammenfassung mit `AUTOPILOT: GOAL REACHED` beginnt. Zyklen, die ohne jede Zusammenfassung enden, durch Fehler oder Abbrüche, beenden die Sitzung nie; der nächste Zyklus wartet einfach länger, 15 Sekunden, dann 30, dann 60, bis zu fünf Minuten.

„Standardmäßig … keinen Zeitrahmen“ ist wörtlich gemeint: `/auto <goal>` ohne Dauer läuft, bis das Ziel erreicht ist oder ihr es stoppt. Wenn ihr eine Obergrenze wollt, gibt `/auto 4h <goal>` euch eine. Aktive Sitzungen überleben auch App-Neustarts. Beenden, oder ein Absturz, pausiert sie, und beim nächsten Start setzt jede in ihrem Tab mit dem nächsten Zyklus fort.

## „Auto-Pilot hat einen Notausschalter“

Drei Wege zum Anhalten, und sie tun unterschiedliche Dinge:

- **Stop All** (der Button, „Alles stoppen“) beendet jede Auto-Pilot-Sitzung in jedem Tab und stoppt alle laufenden Tasks. In `RunStop.swift` ist der Kommentar eindeutig: Ein Stopp eines einzelnen Tasks, Esc oder der Stop-Button, lässt Auto-Pilot weiterlaufen; Stop All beendet ihn.
- **`/auto stop`** beendet die Sitzung, nachdem der aktuelle Zyklus abgeschlossen ist, oder sofort, wenn ihr zwischen zwei Zyklen seid. Der aktuelle Zyklus darf landen.
- **`/auto stop all`** (auch `stopall` oder `stop-all`) ist dasselbe wie das Drücken von Stop All, für Leute, die lieber nicht zur Maus greifen. Es wird in `AutoPilot.swift` direkt vor `/auto stop` behandelt.

Die Einreichung beschreibt `auto stop` so, dass es „nur den aktuellen Zyklus“ beendet. Die genauere Fassung ist, dass es die *Sitzung* nach dem aktuellen Zyklus beendet; der Zyklus selbst läuft bis zu seinem natürlichen Ende, und genau das hält das Fortschrittsprotokoll und die Git-Historie sauber.

## „Im November … mehrere Auto-Pilots im selben Projekt“

Das ist der Teil der Einreichung, der ein Roadmap-Punkt und keine ausgelieferte Funktion ist, und es lohnt sich, klar zu sagen, was was ist. Stand heute hat der Hauptbranch des Agent-Repos einen Commit mit dem Titel *Auto-Pilot: multiple tabs per project — per-tab progress, shared registry, auto/forced git worktree isolation, shared memory from worktrees*. Das ist die Grundlage: Jeder Tab führt sein eigenes Fortschrittsprotokoll, die Tabs registrieren sich gegenseitig, und wenn zwei Auto-Pilots sonst dieselben Dateien bearbeiten würden, bekommen sie getrennte Git-Worktrees. Es ist noch in keinem Release; es kam nach dem Tag 1.1.87 herein. Releases erscheinen am Ersten des Monats, das Release vom 1. November ist also das früheste, das es zu euch bringen kann, und der Teil mit dem „Tab, der weitere Tabs erzeugt“ ist laut Einreichung für dasselbe Zeitfenster geplant.

## „Ein Mario-Kart-ähnlicher Klon namens GoKart“

GoKart ist das Projekt, mit dem Auto-Pilot den größten Teil seines Lebens verbracht hat. Der [frühere Beitrag](/blog/gokart-built-on-auto-pilot/) behandelt den ersten Nachmittag im Detail, direkt aus dem Fortschrittsprotokoll: Godot 4 in Zyklus 1 installiert, eine eigene Arcade-Physik statt `VehicleBody3D` gewählt, damit sich das Fahrverhalten per Unit-Tests prüfen lässt, Drift-Funken und Boost-Unschärfe in Zyklus 2, eine Strecke in Zyklus 3, Items in Zyklus 4, ein Hänger wegen eines verirrten Tabulatorzeichens, ein Stop All und eine zweite Sitzung, die jedem Shell-Aufruf ein `perl -e 'alarm'`-Zeitlimit verpasste und dann fünfzehn Funktionen in Folge auslieferte.

Es hat nicht aufgehört. Das [GoKart-Repository](https://github.com/AgentiLoop/GoKart) ging von seinem ersten Commit um 12:39 Uhr am 1. Oktober auf 71 Commits am Abend des 3. Oktober. Die jüngsten Commits lesen sich wie eine Mario-Kart-64-Checkliste: Verkehr im Stil von Toad's Turnpike auf Sunset Speedway, Monty Moles im Stil von Moo Moo Farm auf Green Hills, ein Titelbildschirm mit einer laufenden Attract-Demo, eine Ergebnistafel und ein gezeichnetes Item-Fenster im HUD. Jeder landet mit seiner eigenen Testdatei und einem `tools/*_check.gd`-Skript, weil das Modell den Bildschirm nach wie vor nicht sehen kann und auf anderem Weg beweisen muss, dass eine Funktion da ist. Die „über 20 Stunden“ in der Einreichung sind die Gesamtlaufzeit dieser Sitzungen in Echtzeit. [GoKart 0.0.1](https://github.com/AgentiLoop/GoKart/releases/tag/v0.0.1) ist für macOS, Windows und Linux herunterladbar, falls ihr lieber spielt als darüber lest.

## Was man im Thread fragen sollte

Wenn ihr von Hacker News kommt, die Fragen, die wir dort am liebsten beantworten würden:

- Wie Auto-Pilot entscheidet, dass ein Ziel erreicht ist, und warum wir das Modell das sagen lassen statt einer festen Metrik.
- Was passiert, wenn ein Zyklus schiefgeht, und warum Git das eigentliche Rückgängig ist.
- Ob eine unbeaufsichtigte Schleife auf eurem Mac überhaupt eine gute Idee ist, und was die Leitplanken dagegen tun.

Der Thread ist unter [news.ycombinator.com/item?id=49948810](https://news.ycombinator.com/item?id=49948810). Agent! 1.1.87 mit Auto-Pilot gibt es auf der [Releases-Seite](https://github.com/AgentiLoop/Agent/releases/latest) und in Homebrew: `brew install --cask agentiloop-agent`.
