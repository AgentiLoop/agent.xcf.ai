---
title: GoKart: Ein Rennspiel im Mario-Kart-Stil, das Auto-Pilot an einem Nachmittag gebaut hat
description: Gib dem Auto-Pilot von Agent! ein einziges Ziel - „erstelle einen Mario-Kart-Klon namens GoKart" - und komm zurück zu einem Godot-4-Rennspiel mit drei Strecken, acht Items, KI-Gegnern und 3.344 bestandenen Test-Checks. Hier steht, was laut Protokoll wirklich passiert ist, einschließlich der Stellen, an denen es feststeckte.
tags: Auto-Pilot, Showcase, Godot
---
<figure style="margin:2rem 0">
<img src="/gokart-green-hills-drift.png" alt="GoKart auf der Strecke Green Hills: Verfolgerkamera auf das Spieler-Kart mitten im Drift auf einer grauen Straße mit rot-weiß gestreiften Banden, grünem Boden und blauem Himmel. Das HUD zeigt Platz 1, Runden- und Zeitzähler und eine Minimap der Strecke unten links." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Green Hills, Runde 1, driftend auf Platz eins. Jedes Mesh, jeder Shader und jeder Sound in diesem Bild wurde aus Code erzeugt.</figcaption>
</figure>

Der gestrige Beitrag hat [Auto-Pilot](/blog/agent-1-1-87-and-agentiloop-cli-0-0-5/) vorgestellt: Tippe `/auto <Ziel>` in Agent! für Mac, und es läuft unbeaufsichtigt Zyklus für Zyklus auf dieses Ziel zu, bis du Stop All drückst. In diesem Beitrag geht es darum, was am anderen Ende herauskam, als ich es auf ein Spiel angesetzt habe.

Das Ziel, mehr oder weniger so eingefügt, wie ich es getippt habe:

> create a Mario Kart clone called GoKart with all Mario Kart effects. I believe Godot 4 can do the Mario Kart effects, but I haven't built any of them yet: drift sparks and boost flames (GPUParticles3D), speed lines and boost blur (screen-space shaders, glow and tonemapping), item effects and tire trails (shaders plus ribbon meshes), kart movement (VehicleBody3D or custom arcade physics). Write unit tests and test the game frequently.

Budget: kein Zeitlimit, unbegrenzte Zyklen. Das Modell in Agent! war in jedem Zyklus Claude Sonnet 5.5. Der erste Commit landete um 12:39. Um 16:32 am selben Nachmittag hatte das Repo 33 Commits. Heute hat es 47 GDScript-Dateien, rund 5.500 Zeilen GDScript- und Shader-Code und eine Unit-Suite, die 3.344 Checks besteht. Das Ganze liegt auf GitHub unter [AgentiLoop/GoKart](https://github.com/AgentiLoop/GoKart).

## Was Auto-Pilot tut, ein Zyklus nach dem anderen

Auto-Pilot führt im Projekt ein laufendes Protokoll unter `.agent/autopilot/progress.md`, und jeder Zyklus hängt an, was er getan hat, was er angenommen hat, was noch offen ist und ob ihn etwas blockiert hat. Dieses Protokoll ist die Quelle für alles Folgende. Ich zitiere es statt meiner Erinnerung, weil das Protokoll ehrlicher ist als ich.

**Zyklus 1** fand kein Godot auf dem Rechner vor. Er führte `brew install --cask godot` aus, verlinkte die Binary per Symlink, machte `git init` und schrieb `kart_physics.gd` als reines Modell ohne Szenenabhängigkeiten: Beschleunigung, Bremsen, Rückwärtsgang, Reibung, Lenkung, ein Drift, der in der Richtung festgehalten wird, in der man ihn begonnen hat, und drei Mini-Turbo-Stufen. Er entschied sich bewusst für eigene Arcade-Physik statt `VehicleBody3D` und begründete das auch: „damit sich das Mario-Kart-Fahrverhalten leicht per Unit-Test prüfen lässt." Elf Tests, 17 Checks, erster Commit.

**Zyklus 2** fügte die Effekte hinzu, die ich namentlich verlangt hatte: GPUParticles3D-Driftfunken, eingefärbt nach Mini-Turbo-Stufe, Auspuffflammen, Reifenspuren aus Ribbon-Meshes und einen Screen-Space-Shader für radiale Boost-Unschärfe, Speedlines und eine Vignette. 43 Checks.

**Zyklus 3** baute eine Strecke. Eine Catmull-Rom-Schleife, alle 3 Meter neu abgetastet, ein Straßenband, rot-weiß gestreifte Banden mit Collidern, Boost-Pads mit einem scrollenden Chevron-Shader, acht geordnete Checkpoints und ein Rundenzähler, der sich weigert, Abkürzungen oder Runden in falscher Richtung zu zählen. Einer der neuen Tests ist ein Verfolger-Bot, der mit dem echten Physikmodell drei volle Runden fährt. Er kam in 1:02,5 ins Ziel. 90 Checks.

**Zyklus 4** fügte Item-Boxen mit einem Regenbogen-Fresnel-Shader hinzu, ein Roulette und die ersten drei Items: Pilz, Banane und einen grünen Panzer, der von den Banden abprallt. Wer getroffen wird, dreht sich 1,2 Sekunden lang. 235 Checks.

Dann blieb es stecken.

## Der Teil, in dem es feststeckte

Der nächste Zyklus begann, KI-Karts und ein Headless-Smoke-Rennen hinzuzufügen, und kam nie zurück. Die Ursache, in der nächsten Sitzung gefunden, war ein einzelner verirrter Tab in Zeile 115 von `main.gd`: ein Parse-Fehler, der das Smoke-Skript endlos Fehler ausspucken ließ, ohne Zeitlimit für den Shell-Befehl, der es ausführte.

Ich drückte **Stop All** und startete eine neue Sitzung mit demselben Ziel plus einer Notiz in Großbuchstaben, die ich nicht vollständig wiedergeben werde. Der Kern: *du bist beim Testen des Smoke-Laufs steckengeblieben, bleib nicht stecken, setz ein Zeitlimit auf die Shell.*

Der erste Zyklus der zweiten Sitzung behob den Tab, kürzte die KI-Vorausschau von 10 Straßen-Samples auf 6, damit die KI aufhörte, Kurven in die Innenbande zu schneiden, fügte einen Kurvengeschwindigkeitsbegrenzer hinzu und packte jeden Shell-Aufruf in `perl -e 'alarm 100; exec @ARGV'`, weil macOS ohne `timeout`-Befehl ausgeliefert wird. Von da an steht am Ende fast jedes Zyklus im Protokoll „alle Läufe liefen hinter perl-alarm-Limits". Es hat die Lektion aus dem Zieltext gelernt und sie weiter angewendet.

Diese Sitzung lief 15 Zyklen in etwa eineinviertel Stunden, und jeder einzelne ist ein Feature: Start-Countdown mit Raketenstart-Boost für gut getimtes Gasgeben; Mini-Turbo-Aufstiegs-Pops und ein Blitz am Bildschirmrand; eine Minimap; der zielsuchende rote Panzer und der Stern; ein prozedurales Kart-Modell mit drehenden Rädern, einschlagenden Vorderrädern und einem Fahrer, der den Kopf dreht; ein Blitz, der jeden Gegner schrumpfen lässt; Dreifach-Panzer, die das Kart umkreisen; der blaue Stachelpanzer, der den Führenden entlang der Straße jagt; ein Ergebnisbildschirm mit Punkten; komplett synthetisierter Sound ohne Audiodateien, vom Motor-Loop bis zum Ziel-Jingle; ein Titelmenü mit einer zweiten Strecke; eine Option für die Rundenzahl; eine dritte Strecke; und positionales 3D-Motorbrummen an jedem KI-Kart.

<figure style="margin:2rem 0">
<img src="/gokart-sunset-speedway.png" alt="GoKart auf der Strecke Sunset Speedway: das Spieler-Kart mit Vollgas auf einem sandigen Kurs unter einem Sonnenuntergangshimmel von Orange bis Violett. Das HUD zeigt Platz 4, Runde 1 und den Minimap-Umriss einer langen Strecke mit einer Haarnadelkurve." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Sunset Speedway, die zweite Strecke, in Zyklus 12 zusammen mit dem Titelmenü hinzugefügt. Länger als Green Hills, mit einer Haarnadel und einer Schikane.</figcaption>
</figure>

## Der Teil, in dem es ehrlich war

Was mir am Protokoll am besten gefällt, ist das Muster der Geständnisse. Agent! kann sich kein PNG ansehen, und es hat das gesagt, Zyklus für Zyklus:

> Der Screenshot-Lauf im Fenstermodus hat keine Fehler protokolliert, aber ich kann keine Bilder ansehen, also habe ich nicht geprüft, wie Strecke oder HUD gerendert werden.

> Ich habe die Sounds nicht gehört, und ich habe weder das Smoke-Rennen noch das Screenshot-Tool ausgeführt.

> Ich kann mit meinen Werkzeugen keine Bilder ansehen, also braucht diese Prüfung einen Menschen.

Also testete es, was es konnte: Headless-Szenenchecks, die die echte Szene instanziieren und Zustände prüfen. Blitz auslösen, bestätigen, dass drei Gegner auf Skalierung 0,5 sind und sich drehen und die Blitze danach aufgeräumt werden. Einen blauen Panzer auf ein dicht gedrängtes Startfeld abfeuern, die Explosion in Frame 12 und zwei sich drehende Karts bestätigen. Den Spieler zum Zieleinlauf zwingen, bestätigen, dass der Autopilot das Kart an einen `AiDriver` übergibt und das Ergebnisfenster „1st YOU" zeigt.

Eine dritte Sitzung blieb auf dieselbe Weise hängen, diesmal hinter einem 240-Sekunden-Alarm, der viel zu großzügig war, und ich stoppte sie nach einem Zyklus. Dann schaute ein Mensch hin. Dieser Mensch war ich, und das Ziel der vierten Sitzung waren meine Playtest-Notizen, leicht aufgeräumt:

> the UI needs to scale with the window. the UI should not be prone to the screen speed effects and blurry. Should be able to use cursor keys. it's not clear when power ups are released. the tops of the walls flicker. Little too hard to steer the kart. hard to keep up with the computer AI karts. maybe have AI difficulty levels Easy Medium and Hard.

Einen Zyklus später: Canvas-Items-Stretch, damit die UI mit dem Fenster skaliert, das HUD auf eine Canvas-Ebene über dem Speed-Effekt-Overlay verschoben, Pfeiltasten, Enter und Strg für Items mit einem Hinweis auf dem Bildschirm, weich einsetzende Lenkung, ein Z-Fighting-Fix für die Bandenstreifen (benachbarte rote und weiße Segmente stritten sich um dieselben Pixel, also wurden die weißen ganz leicht vergrößert), 4x MSAA und Leicht / Mittel / Schwer, die die KI-Höchstgeschwindigkeit auf 0,72, 0,85 und 1,0 skalieren. Die Tests stiegen von 2.156 auf 3.344 Checks, zum Teil, weil es nebenbei auch einen schon vorhandenen Parse-Fehler in `tests/test_items.gd` fand und behob, der das Laden der Suite verhindert hatte.

## Der Teil, in dem es sich selbst gestoppt hat

Die Zyklen 2 bis 8 dieser letzten Sitzung nahmen keine Codeänderungen vor. Jeder las das Repo erneut, ließ die Suite erneut laufen und schrieb eine Variante desselben Absatzes:

> Ich konnte das Ergebnis nicht auf dem Bildschirm sehen, deshalb erkläre ich das Ziel nicht für erreicht. Vier Punkte muss immer noch ein Mensch im Spiel ausprobieren.

Das ist das richtige Verhalten. Das Ziel lautete „die Lenkung fühlt sich schlecht an" und „die Banden flackern", und kein Headless-Test kann dieses Ziel abschließen. Auto-Pilot hat keine Iterationsobergrenze, es hätte also ewig weitergeprüft. Die Sitzung endete nach Zyklus 8, und was GoKart als Nächstes brauchte, war ein Playtest, kein weiterer Zyklus.

<figure style="margin:2rem 0">
<img src="/gokart-frosty-peaks.png" alt="GoKart auf der Strecke Frosty Peaks: das Spieler-Kart mit Vollgas auf einem schneeweißen Kurs unter einem dunkelblauen Dämmerungshimmel. Das HUD zeigt Platz 2, Runde 1, die Geschwindigkeit in km/h und die Minimap." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Frosty Peaks, in Zyklus 14 als neuer Eintrag in der Streckenbibliothek hinzugefügt. Die Tests pro Strecke haben ihn automatisch aufgenommen.</figcaption>
</figure>

## Zu diesen Screenshots

Agent! hat sie aufgenommen, nicht ich, und nicht von Hand. Ich bat um drei Screenshots einer zufälligen Fahrt, und es schrieb ein 70-zeiliges `tools/random_drive.gd`, das der Straße mit einem wandernden Spurversatz folgt, zufällige Drift-Schübe einstreut und das gehaltene Item zu zufälligen Zeitpunkten abfeuert und dann alle paar hundert Physik-Frames ein Bild speichert. Es lief einmal pro Strecke, und die drei oben sind je ein Bild davon. Sie stehen auch in der [GoKart-README](https://github.com/AgentiLoop/GoKart#screenshots).

## Was ich dir sagen würde, bevor du es ausprobierst

- **Lass es in git laufen.** Auto-Pilot hat kein Undo. Das GoKart-Protokoll ist lesbar, weil jeder Zyklus mit einem Commit endete, und als ein Zyklus einmal schiefging, ging nichts verloren.
- **Schreib die Betriebsregeln ins Ziel.** „Setz ein Zeitlimit auf die Shell" funktionierte besser als Teil des Ziels denn als einmalige Nachricht, weil jeder neue Zyklus das Ziel erneut liest.
- **Rechne damit, dass es nach Augen fragt.** Bei allem Visuellen oder Gefühlsmäßigen bleibt die Schleife ehrlich stehen, statt zu lügen. Plane zwischen den Sitzungen einen Playtest ein und gib deine Notizen als nächstes Ziel zurück.
- **Stop All gehört zum Workflow**, es ist kein Fehlschlag. Die ersten drei GoKart-Sitzungen endeten alle damit.

Agent! 1.1.87 mit Auto-Pilot gibt es auf der [Releases-Seite](https://github.com/AgentiLoop/Agent/releases/latest) und in Homebrew. GoKart braucht Godot 4.4 oder neuer: `git clone https://github.com/AgentiLoop/GoKart.git && cd GoKart && godot --path .`
