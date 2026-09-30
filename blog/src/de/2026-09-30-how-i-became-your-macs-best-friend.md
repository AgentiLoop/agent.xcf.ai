---
title: Wie Agent! anfing: drei Tage im März
description: Drei Jahre Ersatzteile, eine fehlende Schleife und 177 Commits in weniger als zwei Tagen. Die echte Entstehung von Agent!, direkt aus git.
tags: Ursprünge, Geschichte
---
<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 380" role="img" aria-labelledby="lego-title lego-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="lego-title">Ein freundlicher Roboter baut einen Mac aus Spielzeugsteinen</title>
<desc id="lego-desc">Ein lächelnder blauer Roboter hält einen gelben Baustein über einen halb fertigen Mac-Bildschirm aus roten, gelben, grünen, blauen und orangefarbenen Spielzeugsteinen. In einer Sprechblase steht: Fast fertig!</desc>
<rect width="760" height="380" rx="20" fill="#eef6ff"/>
<path d="M40 318H720" stroke="#8b684c" stroke-width="13" stroke-linecap="round"/>
<path d="M190 92l-6 26 40-26" fill="#fff"/>
<rect x="120" y="30" width="230" height="64" rx="22" fill="#fff" stroke="#b6c8e4" stroke-width="3"/>
<text x="235" y="72" text-anchor="middle" font-family="system-ui,sans-serif" font-size="26" font-weight="700" fill="#173452">Fast fertig!</text>
<path d="M140 270V310M210 270V310" stroke="#173452" stroke-width="7" stroke-linecap="round"/>
<path d="M250 200L318 146" stroke="#173452" stroke-width="7" stroke-linecap="round"/>
<rect x="100" y="150" width="150" height="120" rx="28" fill="#559ef5" stroke="#173452" stroke-width="4"/>
<path d="M175 150V124" stroke="#173452" stroke-width="5"/><circle cx="175" cy="115" r="10" fill="#efb943"/>
<circle cx="145" cy="192" r="13" fill="#fff"/><circle cx="205" cy="192" r="13" fill="#fff"/>
<circle cx="149" cy="193" r="5.5" fill="#173452"/><circle cx="209" cy="193" r="5.5" fill="#173452"/>
<path d="M148 228Q175 250 202 228" fill="none" stroke="#173452" stroke-width="6" stroke-linecap="round"/>
<g stroke="#173452" stroke-width="3">
<rect x="300" y="112" width="70" height="34" rx="4" fill="#efb943"/>
<rect x="311" y="102" width="16" height="10" rx="2" fill="#efb943"/><rect x="343" y="102" width="16" height="10" rx="2" fill="#efb943"/>
</g>
<g stroke="#173452" stroke-width="3">
<rect x="430" y="276" width="140" height="34" rx="4" fill="#9aa7b8"/>
<rect x="480" y="244" width="40" height="32" fill="#b8c3d1"/>
<rect x="400" y="210" width="70" height="34" rx="4" fill="#d94877"/>
<rect x="470" y="210" width="70" height="34" rx="4" fill="#4caf6e"/>
<rect x="540" y="210" width="70" height="34" rx="4" fill="#559ef5"/>
<rect x="610" y="210" width="70" height="34" rx="4" fill="#f08a3c"/>
<rect x="400" y="176" width="70" height="34" rx="4" fill="#efb943"/>
<rect x="470" y="176" width="70" height="34" rx="4" fill="#559ef5"/>
<rect x="540" y="176" width="70" height="34" rx="4" fill="#d94877"/>
<rect x="610" y="176" width="70" height="34" rx="4" fill="#4caf6e"/>
<rect x="400" y="142" width="70" height="34" rx="4" fill="#4caf6e"/>
<rect x="470" y="142" width="70" height="34" rx="4" fill="#f08a3c"/>
<rect x="540" y="142" width="70" height="34" rx="4" fill="#efb943"/>
<rect x="400" y="108" width="70" height="34" rx="4" fill="#559ef5"/>
<rect x="470" y="108" width="70" height="34" rx="4" fill="#d94877"/>
<rect x="540" y="108" width="70" height="34" rx="4" fill="#4caf6e"/>
<rect x="610" y="108" width="70" height="34" rx="4" fill="#efb943"/>
</g>
<rect x="610" y="142" width="70" height="34" rx="4" fill="none" stroke="#173452" stroke-width="3" stroke-dasharray="8 6"/>
<text x="190" y="354" text-anchor="middle" font-family="system-ui,sans-serif" font-size="21" fill="#173452">Der Baumeister.</text>
<text x="540" y="354" text-anchor="middle" font-family="system-ui,sans-serif" font-size="21" fill="#173452">Der Mac. Ein Stein fehlt noch.</text>
</svg>
<figcaption>Alles Große beginnt als Haufen kleiner Bausteine. Der Trick ist zu wissen, welcher als Nächstes kommt.</figcaption>
</figure>

Jede App hat einen ersten Tag. Der erste Tag von Agent! war ein Mittwoch: **der 11. März 2026, um 15:07 Uhr.** Wir kennen die Minute, weil git sie aufgeschrieben hat.

Aber die Bausteine lagen schon lange vorher herum.

## Drei Jahre Ersatzteile

Vor Agent! gab es andere Apps. **ANIE.** **Game Changer.** **BattleScript.** Den **XCF MCP Server und Client.** **D1F**, ein Werkzeug, um viele Zeilen einer Datei auf einmal zu ändern. Und etwa acht Swift-Pakete, alle von derselben Person geschrieben.

Jede davon konnte ein Stück der Arbeit. Manche konnten mit einer KI reden. Manche konnten Code bearbeiten. Manche konnten in Xcode herumstochern. Keine konnte das Wichtigste: **von allein weitermachen.**

Denk an ein Aufziehspielzeug. Du ziehst es auf, es macht drei Schritte, dann bleibt es stehen. Süß. Nicht hilfreich. Was fehlte, war eine Schleife: das Problem ansehen, ein Werkzeug wählen, es benutzen, prüfen, was passiert ist, und wieder von vorn, bis die Arbeit erledigt ist. (Diese Schleife hat [einen eigenen Beitrag, mit einem Roboter und einem Sandwich](/blog/what-is-an-agent-loop/).)

Sobald die Schleife funktionierte, konnten die besten alten Teile darauf einrasten. Das ist die ganze Entstehungsgeschichte in einem Satz. Der Rest sind Details, und die Details machen Spaß.

## Tag eins: ein Gehirn, ein Helfer und ein Abbrechen-Knopf

Der allererste echte Commit heißt *„Autonomous Agent with privileged launch daemon.“* Er umfasste 20 Dateien und 1.765 Zeilen Swift. Das war in der Kiste:

- Ein SwiftUI-Fenster, in das du tippst, was du willst.
- Ein KI-Gehirn, Claude, das das Denken übernimmt.
- Ein **Launch Daemon**: ein kleiner Helfer, der im Hintergrund läuft und die Schlüssel zum ganzen Haus hat, damit der Agent erwachsene System-Aufgaben erledigen kann.
- Aufgabenverlauf, Bildschirmfotos und Einfügen.

Eine Stunde später kam die erste Absturz-Reparatur (das Einfügen eines Bildschirmfotos ließ alles abstürzen). Minuten danach ein großer roter **Abbrechen**-Knopf, auf die Escape-Taste gelegt. Wenn man etwas baut, das selbst handelt, kommt der Stopp-Knopf früh.

Um 17:27 Uhr gab es einen zweiten Helfer, einen **Launch Agent**, der Befehle als *du* ausführt statt als allmächtiger root. Den Generalschlüssel zu verlangen, nur um einen Ordner aufzulisten, ist wie die Feuerwehr zu rufen, um eine Kerze anzuzünden. Sechs Minuten später bekam Agent! sein zweites Gehirn: **Ollama**, damit es mit KI-Modellen laufen kann, die auf deinem eigenen Mac wohnen.

Noch bevor der Tag vorbei war, konnte es außerdem Swift-Skripte schreiben und ausführen, Xcode steuern, mit Vision-Modellen Bilder sehen und einen Startbildschirm zeigen. Es bekam auch kleine Status-Punkte im Ampel-Stil, die ungefähr ein Dutzend Commits brauchten, bis Grün, Gelb und Rot feststanden. Manche Dinge sind schwieriger als eine Agent-Schleife.

## Tag zwei: „Darf ich?“

Am 12. März lernte Agent!, dass ein Mac höflich ist, und dabei sehr streng.

Um eine andere App wie Musik oder Pages zu steuern, fragt macOS dich zuerst: *„Agent! möchte Musik steuern. Erlauben?“* Dieses kleine Fenster wirklich zum Erscheinen zu bringen, hat den ganzen Abend gedauert. Von etwa 20:20 bis 21:40 Uhr ist der Verlauf ein Haufen Versuche im Abstand weniger Minuten: so probieren, auf dem Hauptthread probieren, Systemeinstellungen öffnen, `osascript` probieren, nach `every window` fragen, nur `name` probieren. Außerdem hatten Keynote, Numbers und Pages ihre Bundle-IDs geändert, also klopfte es mit den falschen Namen an die Türen.

Es hat geklappt. Am selben Abend lernte es, Bilder und Webseiten direkt in seinem eigenen Protokoll anzuzeigen. Wenn es also ein Album-Cover macht, siehst du das Album-Cover.

## Tag drei: ein Name und eine Versionsnummer

Am Morgen des 13. März bekam die App ihren Namen. Der Commit um 9:06 Uhr heißt *„rename app to Agent!“* Ausrufezeichen inklusive, mit Absicht.

Zwanzig Minuten später kam eine Änderung, die bis heute zählt: Skripte waren keine eigenen Programme mehr, sondern **dynamische Bibliotheken**, die direkt in der App geladen werden. Deshalb haben AgentScripts dieselben Mac-Berechtigungen wie Agent!, ohne erneut zu fragen.

Später an diesem Tag wurde **1.0.0** getaggt. Vom ersten Commit an gezählt sind das **177 Commits in weniger als zwei Tagen.** Die Versionen 1.0.1 bis 1.0.16 folgten in den nächsten acht Tagen.

Ein kleines Detail: Der Autorenname auf diesen frühen Commits ist keine Person. Er lautet **„Agent! for MacOS“.**

## Erwachsen werden

Nach dem ersten Sprint wird die Geschichte schneller:

- **6. April.** Fast ein Monat Verlauf wurde zu einem einzigen sauberen Start-Commit zusammengefasst. Der vollständige Verlauf blieb in einem Backup erhalten.
- **7. April.** „Coding-Modus“, „Automatisierungs-Modus“ und „Standard-Modus“ wurden [herausgerissen](/blog/why-we-ripped-out-modes/). Ein Agent, alle Werkzeuge, jedes Mal.
- **April.** Apple Intelligence war an Bord, als Gehirn, das direkt auf dem Mac läuft, kostenlos.
- **31. August.** Das Projekt zog von der GitHub-Organisation `macOS26` zu **AgentiLoop** um, und die Website wurde zu **agentiloop.ai**.
- **Zuletzt.** Agent! lernte, [auf macOS 14.6 und auf Intel-Macs zu laufen](/blog/sonoma-intel-and-the-mac-that-was-not-dead-yet/), und half beim Bau seiner eigenen Terminal-Geschwister: [AgentiLoopCLI](https://github.com/AgentiLoop/AgentiLoopCLI) in Rust und [AgentiLoopGo](https://github.com/AgentiLoop/AgentiLoopGo) in Go.

Es begann mit einem Gehirn. Heute arbeitet es mit **23 KI-Anbietern**, dazu Apple Intelligence. Seit dem Aufräumen im April hat der Hauptzweig mehr als 1.300 Commits dazubekommen.

## Warum es so ist, wie es ist

Fast alles Eigenartige an Agent! geht auf diese ersten drei Tage zurück.

Es hat zwei Helfer, einen für dich und einen für root, weil Tag eins beide brauchte. Es ist zu 100 % Swift, wie die Ersatzteile, aus denen es gebaut wurde. Es besteht aus eigenem Code, nicht aus einem Haufen von 65 NPM-Paketen. Es steuert andere Apps über ihren Namen per Bedienungshilfen und AppleScript, weil Tag zwei damit verbracht wurde zu lernen, wie man den Mac höflich fragt. Und es hat immer noch einen großen Abbrechen-Knopf.

Alles Große beginnt als Haufen kleiner Bausteine. Dieser Haufen ist drei Jahre lang gewachsen. Am 11. März hat endlich jemand den Baustein gefunden, der alle anderen zusammenhält: die Schleife.
