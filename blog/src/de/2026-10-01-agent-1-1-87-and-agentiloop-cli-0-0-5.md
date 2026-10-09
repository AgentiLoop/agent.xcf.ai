---
title: Die ganze Familie erscheint: Agent! 1.1.87 und AgentiLoop CLI 0.0.5
description: Agent! für Mac bekommt Auto-Pilot, sechs neue Provider, einen strengeren Kritiker und Unterstützung für macOS 14.6. Die CLIs in Rust und Go bekommen einen größeren Werkzeugkasten: Suche, Web-Abruf, Todos, AGENTS.md, /undo, eigene Befehle und --json.
tags: Ankündigung, Release, Plattformübergreifend
---
<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 380" role="img" aria-labelledby="fam-title fam-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="fam-title">Die AgentiLoop-Familie: eine Mac-App und zwei Terminals</title>
<desc id="fam-desc">In der Mitte steht ein großes Mac-Fenster mit der Beschriftung Agent! 1.1.87. Links davon zeigt ein Terminalfenster eine kleine Krabbe und die Beschriftung Rust 0.0.5, rechts davon zeigt ein Terminalfenster einen kleinen Gopher und die Beschriftung Go 0.0.5. Gepunktete Linien verbinden alle drei mit einem gemeinsamen Schleifensymbol oben.</desc>
<rect width="760" height="380" rx="20" fill="#0f1724"/>
<g fill="#6fb6ff" opacity=".35"><circle cx="60" cy="50" r="2"/><circle cx="700" cy="70" r="2"/><circle cx="640" cy="330" r="2"/><circle cx="110" cy="320" r="2"/><circle cx="380" cy="350" r="2"/><circle cx="520" cy="40" r="2"/><circle cx="230" cy="36" r="2"/></g>
<g fill="none" stroke="#6fb6ff" stroke-width="3" stroke-dasharray="4 8" stroke-linecap="round"><path d="M380 80V112"/><path d="M350 62Q170 70 140 150"/><path d="M410 62Q590 70 620 150"/></g>
<g fill="none" stroke="#9fd2ff" stroke-width="5" stroke-linecap="round"><path d="M380 55C392 39 412 39 412 55C412 71 392 71 380 55C368 39 348 39 348 55C348 71 368 71 380 55Z"/></g>
<rect x="250" y="112" width="260" height="190" rx="16" fill="#1d2a3d" stroke="#6fb6ff" stroke-width="3"/>
<rect x="250" y="112" width="260" height="34" rx="16" fill="#26364d"/><rect x="250" y="130" width="260" height="16" fill="#26364d"/>
<circle cx="272" cy="129" r="6" fill="#ff5f57"/><circle cx="292" cy="129" r="6" fill="#febc2e"/><circle cx="312" cy="129" r="6" fill="#28c840"/>
<rect x="340" y="164" width="80" height="80" rx="20" fill="#2f7bf5"/>
<g fill="#fff"><circle cx="358" cy="186" r="5"/><circle cx="402" cy="186" r="5"/><circle cx="380" cy="204" r="5"/><circle cx="360" cy="226" r="5"/><circle cx="400" cy="226" r="5"/></g>
<g fill="none" stroke="#fff" stroke-width="2" opacity=".8"><path d="M358 186L380 204L402 186M380 204L360 226M380 204L400 226M360 226H400M358 186H402M358 186L360 226M402 186L400 226"/></g>
<text x="380" y="280" text-anchor="middle" font-family="system-ui,sans-serif" font-size="22" font-weight="700" fill="#e8f2ff">Agent! 1.1.87</text>
<rect x="40" y="150" width="190" height="150" rx="12" fill="#121c2a" stroke="#f08a4b" stroke-width="3"/>
<text x="56" y="178" font-family="ui-monospace,monospace" font-size="15" fill="#f08a4b">$ agentiloop</text>
<g fill="#f08a4b" stroke="#0f1724" stroke-width="2"><ellipse cx="135" cy="236" rx="34" ry="22"/><circle cx="92" cy="214" r="10"/><circle cx="178" cy="214" r="10"/></g>
<g stroke="#f08a4b" stroke-width="4" stroke-linecap="round"><path d="M110 256l-10 14M122 258l-6 14M148 258l6 14M160 256l10 14M100 222l8 6M170 222l-8 6"/></g>
<circle cx="124" cy="230" r="4" fill="#0f1724"/><circle cx="146" cy="230" r="4" fill="#0f1724"/>
<text x="135" y="292" text-anchor="middle" font-family="system-ui,sans-serif" font-size="17" font-weight="700" fill="#ffd2b5">Rust 0.0.5</text>
<rect x="530" y="150" width="190" height="150" rx="12" fill="#121c2a" stroke="#4fd1e8" stroke-width="3"/>
<text x="546" y="178" font-family="ui-monospace,monospace" font-size="15" fill="#4fd1e8">$ agentiloop</text>
<g stroke="#0f1724" stroke-width="2"><ellipse cx="625" cy="236" rx="30" ry="36" fill="#4fd1e8"/><circle cx="600" cy="204" r="7" fill="#4fd1e8"/><circle cx="650" cy="204" r="7" fill="#4fd1e8"/></g>
<circle cx="612" cy="222" r="9" fill="#fff"/><circle cx="638" cy="222" r="9" fill="#fff"/><circle cx="612" cy="222" r="4" fill="#0f1724"/><circle cx="638" cy="222" r="4" fill="#0f1724"/>
<text x="625" y="292" text-anchor="middle" font-family="system-ui,sans-serif" font-size="17" font-weight="700" fill="#c8f4fb">Go 0.0.5</text>
<text x="380" y="345" text-anchor="middle" font-family="system-ui,sans-serif" font-size="18" fill="#9fb6d4">Ein Loop. Drei Arten, ihn zu starten.</text>
</svg>
<figcaption>Die AgentiLoop-Familie am 1. Oktober: Agent! für Mac sowie die Kommandozeilen-Editionen in Rust und Go.</figcaption>
</figure>

Heute erscheint die ganze Familie auf einmal. **Agent! 1.1.87** ist das neue Release der Mac-App, und **AgentiLoop CLI 0.0.5** ist sowohl für [Rust](https://github.com/AgentiLoop/AgentiLoopCLI/releases/tag/v0.0.5) als auch für [Go](https://github.com/AgentiLoop/AgentiLoopGo/releases/tag/v0.0.5) verfügbar. Es ist ein vollwertiges Release, keine Vorabversion, und für alle drei der bisher größte Schritt.

Hier ist, was neu ist, direkt aus dem git-Verlauf.

## Agent! 1.1.87 für Mac

Das letzte vollwertige Release der Mac-App war 1.1.33 am 12. September. Seitdem ist viel passiert: 449 Commits sind in 1.1.87 eingeflossen. Das sind die Highlights.

### 🤖 Auto-Pilot: `/auto <goal>`

Das Hauptfeature. Gib Agent! ein Ziel, und `/auto` arbeitet es als Folge unbeaufsichtigter Zyklen innerhalb eines Zeitbudgets ab. Jeder Zyklus arbeitet auf das Ziel hin, prüft, wo er steht, und macht weiter.

- Keine Obergrenze für Zyklen oder Iterationen. Es funktioniert in LLM-Tabs und führt einen Zielverlauf, sodass `/auto last` und `/auto #N` ein früheres Ziel zurückholen.
- Sitzungen überstehen App-Neustarts und laufen im selben Tab weiter.
- **Esc** stoppt nur den aktuellen Zyklus. **Stop All** (oder `/auto stop all`) beendet die Sitzung.

Das ist der Agent-Loop, bei dem der Mensch bewusst einen Schritt zurücktritt: Du legst Ziel und Budget fest, und Agent! fährt.

### 🔌 Sechs neue Provider und weniger Einstellungen zum Herumfummeln

Neu in 1.1.87: **Sidrune AI** (mit Protokolloptionen für OpenAI und Anthropic), **Muse Code** (nutzt dein `muse login`-Abo), **Requesty**, **A2Agent**, **OrcaRouter** und **Qwen Code** im Coding Plan. Dazu kommt ein experimenteller **fm serve**-Provider, der Apple Foundation Models über eine lokale Chat-Completions-API bereitstellt.

Vision-Unterstützung wird jetzt aus den Katalog-Metadaten jedes Providers erkannt, daher wird der Schalter „Force Vision“ nicht mehr gebraucht. Unter der Haube lebt jetzt jeder Provider in einer einzigen Registry, `APIProvider`, statt in einem Dutzend getrennter Codepfade.

### 🧐 Ein Kritiker, der sich nichts ausreden lässt

Agent! hat ein Kritiker-Gate: Ein zweites Modell prüft die Änderung, bevor die Aufgabe als erledigt gilt. In 1.1.87 wird das Review **erzwungen**. Ein unveränderter Diff wird abgelehnt, ein geänderter Diff wird erneut geprüft, und Probleme lassen sich nicht als „außerhalb des Umfangs“ abtun. Der Kritiker läuft jetzt auch mit Codex und Apple Intelligence, und das Log zeigt, welche Probleme er gefunden hat und ob sich der Code danach geändert hat.

Daneben gibt es **Jev**, die TypeSafe-System-One-Entscheidungsschicht, die den Tool-Loop berät. Ihre Einstellungen findest du in den neuen LLM Common Settings.

### 🧠 Klügerer Kontext

Die Kompaktierung wurde sorgfältig überarbeitet. Schwellenwerte richten sich jetzt nach dem *tatsächlich verwendeten* Modell (dem Modell des Tabs oder dem Fallback), und abgerufene Ollama-Kontextfenster werden gespeichert. Das behebt einen Fehler, bei dem manche Modelle schon bei 16K kompaktiert wurden. Das behaltene Ende und Microcompact sind durch Tokens statt durch Nachrichtenanzahlen begrenzt, übergroße Blöcke werden zuerst gekürzt, und Kontextüberlauf- sowie `max_tokens`-Fehler werden bei allen Providern auf dieselbe Weise erkannt.

### 🖥️ Mehr Macs, mehr Sprachen

- **macOS 14.6 Sonoma und neuer**, auf Apple Silicon und Intel. Funktionen von Apple Intelligence (Foundation Models) benötigen macOS 26.
- Die App ist auf Spanisch, Französisch, Deutsch, Chinesisch (vereinfacht), Russisch, Koreanisch und Japanisch lokalisiert.
- Neue Bedienungshilfen-Aktionen: `wait_until_actionable`, `select_text_range` und `observe_start/poll/stop/list`.
- Installation mit Homebrew: `brew update && brew install --cask agentiloop-agent`.

### 🔒 Standardmäßig sicherer

Das rekursive Löschen des aktuellen Projektordners wird jetzt blockiert. Eine App-weite Fehlerjagd hat eine ShellSafety-Umgehung des Nur-Lese-Modus per `&`, ein Hängenbleiben beim Ollama-Streaming und mehrere Abstürze behoben. `task_complete` wird abgelehnt, wenn die Zusammenfassung auf Ausgaben verweist, die nie geschrieben wurden, und lokale Modelle, denen der Speicher ausgeht, stoppen sofort mit einem klaren Grund, statt sich endlos zu drehen.

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 330" role="img" aria-labelledby="box-title box-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="box-title">Ein größerer Werkzeugkasten für die CLI</title>
<desc id="box-desc">Ein offener roter Werkzeugkasten mit der Beschriftung 0.0.5. Werkzeuge steigen auf beschrifteten Schildern daraus empor: glob und grep mit einer Lupe, web_fetch mit einem Globus, todo_write mit einer Checkliste, /undo mit einem gebogenen Pfeil, AGENTS.md mit einem Dokument und --json mit geschweiften Klammern.</desc>
<rect width="760" height="330" rx="20" fill="#fff6ea"/>
<path d="M60 296H700" stroke="#c9a77f" stroke-width="10" stroke-linecap="round"/>
<path d="M240 178L270 140H490L520 178Z" fill="#b8323a" stroke="#5a1418" stroke-width="4" stroke-linejoin="round"/>
<rect x="240" y="178" width="280" height="112" rx="10" fill="#d9444d" stroke="#5a1418" stroke-width="4"/>
<path d="M340 140V120Q340 108 352 108H408Q420 108 420 120V140" fill="none" stroke="#5a1418" stroke-width="8"/>
<rect x="340" y="214" width="80" height="40" rx="8" fill="#fff" stroke="#5a1418" stroke-width="3"/>
<text x="380" y="241" text-anchor="middle" font-family="ui-monospace,monospace" font-size="20" font-weight="700" fill="#5a1418">0.0.5</text>
<g font-family="ui-monospace,monospace" font-size="17" font-weight="700" text-anchor="middle">
<g><rect x="60" y="40" width="150" height="44" rx="12" fill="#d7eaff" stroke="#3377b9" stroke-width="3"/><text x="135" y="68" fill="#173452">glob · grep</text><circle cx="232" cy="102" r="16" fill="none" stroke="#3377b9" stroke-width="5"/><path d="M244 114l14 14" stroke="#3377b9" stroke-width="6" stroke-linecap="round"/></g>
<g><rect x="60" y="120" width="140" height="44" rx="12" fill="#d9f5e4" stroke="#2f8f5b" stroke-width="3"/><text x="130" y="148" fill="#14432a">web_fetch</text><circle cx="222" cy="186" r="16" fill="#bfe9cf" stroke="#2f8f5b" stroke-width="3"/><path d="M206 186H238M222 170Q212 186 222 202Q232 186 222 170" fill="none" stroke="#2f8f5b" stroke-width="2.5"/></g>
<g><rect x="295" y="20" width="170" height="44" rx="12" fill="#fce9b6" stroke="#9a701b" stroke-width="3"/><text x="380" y="48" fill="#4a3608">todo_write</text><path d="M362 76l6 6 10-12M362 94l6 6 10-12" fill="none" stroke="#9a701b" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><path d="M386 78H404M386 96H404" stroke="#9a701b" stroke-width="4" stroke-linecap="round"/></g>
<g><rect x="560" y="40" width="140" height="44" rx="12" fill="#efe1ff" stroke="#7a4bb8" stroke-width="3"/><text x="630" y="68" fill="#341a5a">/undo</text><path d="M548 128Q520 128 520 104Q520 84 546 84" fill="none" stroke="#7a4bb8" stroke-width="5" stroke-linecap="round"/><path d="M538 74l12 10-12 10" fill="none" stroke="#7a4bb8" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></g>
<g><rect x="560" y="120" width="140" height="44" rx="12" fill="#ffe0e6" stroke="#b83a5a" stroke-width="3"/><text x="630" y="148" fill="#5a1426">AGENTS.md</text><path d="M528 172h20l8 8v26h-28z" fill="#fff" stroke="#b83a5a" stroke-width="3" stroke-linejoin="round"/></g>
<g><rect x="560" y="210" width="140" height="44" rx="12" fill="#e2e8f0" stroke="#4b617e" stroke-width="3"/><text x="630" y="238" fill="#173452">--json { }</text></g>
</g>
</svg>
<figcaption>AgentiLoop CLI 0.0.5: derselbe Loop, viel mehr im Kasten.</figcaption>
</figure>

## AgentiLoop CLI 0.0.5: ein größerer Werkzeugkasten

Als wir [den Agent-Loop ins Terminal gebracht haben](/blog/the-terminal-strikes-back/), startete die CLI mit fünf scharfen Tools: Lesen, Auflisten, Schreiben, Bearbeiten und bash. Version 0.0.4 hat ihr beigebracht, sauber anzuhalten. Bei Version 0.0.5 geht es darum, ihr mehr Material zum Arbeiten zu geben. Alles davon ist zuerst in Rust gelandet und wurde Commit für Commit in Go gespiegelt, sodass beide Editionen exakt dieselben Funktionen haben.

### Neue Tools

| Tool | Was es tut | Fragt vorher? |
|---|---|---|
| `glob` | Findet Dateien anhand eines Musters | Nein |
| `grep` | Durchsucht Dateiinhalte, mit 0–5 Zeilen Kontext | Nein |
| `web_fetch` | Ruft eine http(s)-Seite als Text ab, mit Größenbegrenzung | **Ja** |
| `todo_write` | Führt eine Checkliste für mehrstufige Arbeit (anzeigen mit `/todos`) | Nein |

`glob` und `grep` überspringen `.git`, `node_modules`, `target` und Binärdateien und beachten `.gitignore`, einschließlich verschachtelter Dateien, Negation, Verankerung und reiner Verzeichnisregeln. Damit sind sie schneller, als `find` in der Shell aufzurufen, und sicherer, als einen ganzen Verzeichnisbaum in den Kontext zu kippen.

### Sie liest die Anweisungen deines Projekts

Wenn dein Repo eine **`AGENTS.md`** oder **`CLAUDE.md`** hat, lädt die CLI sie in den System-Prompt, zusammen mit einer in `~/.agentiloop` für deine persönlichen Standards. Zeilen wie `@docs/style.md` importieren andere Dateien (verschachtelt und zyklensicher). Noch keine Datei? **`/init`** schreibt eine Start-`AGENTS.md` mit den Build- und Testbefehlen, die es erkennt.

### Undo, Diff und Co.

- **`/undo`**: Jede Änderung durch `write_file`, `edit_file` und `apply_patch` wird pro Prompt protokolliert, sodass du den letzten Zug des Agenten zurückrollen kannst.
- **`/diff`** zeigt den git-Status und den Diff des Arbeitsverzeichnisses.
- **`/export`** speichert die Unterhaltung als Markdown.
- **`/usage`** zeigt die Token-Summen seit dem Start und wie voll der Kontext ist.

### Mach sie zu deiner

- **Eigene Slash-Befehle**: Leg eine Markdown-Datei in `.agentiloop/commands/` ab, etwa `review.md` mit dem Inhalt `Review $1 for bugs`, und `/review main.rs` führt sie aus. `$ARGUMENTS` und `$1`..`$9` werden unterstützt, und `/commands` listet sie auf.
- **MCP-Prompts** von deinen Servern erscheinen als `/mcp__<server>__<prompt>`-Befehle.

### Gebaut für Skripte und CI

- **`--json`** gibt eine One-Shot-Antwort als einzelnes JSON-Objekt aus: result, is_error, session_id, provider, model und usage.
- **`--allow-tool` / `--deny-tool`** legen Berechtigungsregeln nach Tool-Name oder `mcp_*`-Präfix fest. Deny gewinnt immer, sogar gegen `--yes`.
- **`--append-system-prompt`** fügt für einen Lauf Text zum System-Prompt hinzu.
- **Pipes funktionieren einfach**: Ein einzelnes `-` im Prompt wird durch stdin ersetzt, sodass `git diff | agentiloop "review this" -` genau das tut, was draufsteht.

Zusammengenommen ergibt das einen CI-Schritt, der einen Pull Request prüft, die Shell nicht anrührt und maschinenlesbare Ausgabe liefert:

```
git diff origin/main | agentiloop --deny-tool bash --json "review this diff" -
```

## Warum alles zusammen veröffentlichen?

Weil es dieselbe Idee in drei Formen ist. Agent! für Mac ist das Flaggschiff: Es steuert deine Apps, deine Xcode-Builds und deinen ganzen Desktop. Die CLIs tragen denselben Loop in jedes Terminal unter macOS, Windows und Linux. Esc-zum-Abbrechen in der CLI und der Auto-Pilot der Mac-App mit seinem Stop-All-Button beantworten dieselbe Frage von zwei Seiten: *Wie behält ein Mensch die Kontrolle über einen Loop, der von selbst läuft?*

Das ist der Teil, der uns am wichtigsten ist. Kein niedlicher Avatar, keine größere Zahl in einem Benchmark, sondern der Mensch im Loop: Du legst das Ziel fest, du siehst jeden Schritt, und du kannst ihn stoppen. In der CLI macht `/undo` außerdem die letzten Dateiänderungen des Agenten rückgängig. Auto-Pilot lässt sich nicht rückgängig machen, also nutze ihn in einem Projekt, das in git liegt.

## Hol sie dir

- **Agent! 1.1.87 für Mac**: [von GitHub herunterladen](https://github.com/AgentiLoop/Agent/releases/tag/v1.1.87.287) oder `brew update && brew install --cask agentiloop-agent`. macOS 14.6 oder neuer, Apple Silicon oder Intel.
- **AgentiLoop CLI 0.0.5 (Rust)**: [Release auf GitHub](https://github.com/AgentiLoop/AgentiLoopCLI/releases/tag/v0.0.5).
- **AgentiLoopGo 0.0.5 (Go)**: [Release auf GitHub](https://github.com/AgentiLoop/AgentiLoopGo/releases/tag/v0.0.5).

Die macOS-CLI-Binaries sind signiert und notarisiert. Entpacken, `agentiloop` in deinen PATH legen und starten; der Einrichtungsassistent übernimmt den Rest.

Tester sind sehr willkommen. Probier `/undo` nach einer großen Änderung, richte sie auf ein Repo mit einer `AGENTS.md` oder bau `--json` in ein Skript ein, und sag uns dann, was kaputtgegangen ist. Bitte gib dein Betriebssystem, deinen Provider und dein Modell an, und füge niemals API-Schlüssel bei.
