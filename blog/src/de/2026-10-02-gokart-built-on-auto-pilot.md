---
title: GoKart: Ein Rennspiel im Mario-Kart-Stil, das Auto-Pilot an einem Nachmittag gebaut hat
description: Gib dem Auto-Pilot von Agent! ein einziges Ziel - „erstelle einen Mario-Kart-Klon namens GoKart" - und komm zurück zu einem Godot-4-Rennspiel mit drei Strecken, acht Items, KI-Gegnern und 3.344 bestandenen Test-Checks. Zwei Tage und 87 Agent-Commits später ist es GoKart 0.0.2, mit vier Strecken, Battle-Modus, Zeitfahren und einem Menü im Stil von Mario Kart 64. Hier steht, was laut Protokoll wirklich passiert ist, einschließlich der Stellen, an denen es feststeckte.
tags: Auto-Pilot, Showcase, Godot
updated: 2026-10-04
---
<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-title.png" alt="Der Titelbildschirm von GoKart 0.0.2: das Wort GOKART auf einem Bogen in großen Buchstaben mit Gelb-zu-Rot-Verlauf, marineblauen Blockseiten und weichem Schatten, über einer laufenden Attract-Demo von CPU-Karts, die eine Strecke umrunden, darunter PRESS ENTER." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Der Titelbildschirm von GoKart 0.0.2. Das Logo fliegt herein und federt zum Stillstand über einer laufenden Attract-Demo, die durch die Strecken führt. Jedes Mesh, jeder Shader, jedes Schriftlayout und jeder Sound wurde aus Code erzeugt.</figcaption>
</figure>

*Aktualisiert am 4. Oktober: Der Beitrag folgt der Geschichte jetzt durch die zwei Tage nach jenem ersten Nachmittag, einschließlich des Abends, an dem sich zwei Auto-Pilot-Sitzungen ein Repo teilten, und endet mit dem Release [GoKart 0.0.2](#gokart-0-0-2). Die Screenshots wurden vom 0.0.2-Tag neu aufgenommen.*

Der gestrige Beitrag hat [Auto-Pilot](/blog/agent-1-1-87-and-agentiloop-cli-0-0-5/) vorgestellt: Tippe `/auto <Ziel>` in Agent! für Mac, und es läuft unbeaufsichtigt Zyklus für Zyklus auf dieses Ziel zu, bis du Stop All drückst. In diesem Beitrag geht es darum, was am anderen Ende herauskam, als ich es auf ein Spiel angesetzt habe.

Das Ziel, mehr oder weniger so eingefügt, wie ich es getippt habe:

> create a Mario Kart clone called GoKart with all Mario Kart effects. I believe Godot 4 can do the Mario Kart effects, but I haven't built any of them yet: drift sparks and boost flames (GPUParticles3D), speed lines and boost blur (screen-space shaders, glow and tonemapping), item effects and tire trails (shaders plus ribbon meshes), kart movement (VehicleBody3D or custom arcade physics). Write unit tests and test the game frequently.

Budget: kein Zeitlimit, unbegrenzte Zyklen. Das Modell in Agent! war in jedem Zyklus Claude Sonnet 5.5. Der erste Commit landete um 12:39. Um 16:32 am selben Nachmittag hatte das Repo 33 Commits, 47 GDScript-Dateien, rund 5.500 Zeilen GDScript- und Shader-Code und eine Unit-Suite, die 3.344 Checks bestand. Zwei Tage später, beim 0.0.2-Tag, waren diese Zahlen auf 126 Commits, 150 Dateien, rund 24.500 Zeilen und 14.134 Checks gewachsen. Jeder einzelne dieser Commits stammt vom Agenten. Das Ganze liegt auf GitHub unter [AgentiLoop/GoKart](https://github.com/AgentiLoop/GoKart).

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
<img src="/gokart-0-0-2-sunset-speedway.png" alt="GoKart 0.0.2 auf Sunset Speedway: das Spieler-Kart driftend auf Platz 3 von 8 in Runde 1 unter dem Sonnenuntergangshimmel, mit dem HUD im Stil von Mario Kart 64: eine durchscheinende Streckenkarte unten links, Platz, Runde und Geschwindigkeit in einer runden Gold-und-Creme-Schrift." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Sunset Speedway in 0.0.2: ein Zufallsfahrt-Bot mitten im Drift auf Platz 3 von 8. Die zweite Strecke wurde in Zyklus 12 des ersten Tages zusammen mit dem Titelmenü hinzugefügt. Der Verkehr, die Gebäude hinter den Banden und das HUD kamen zwei Tage später.</figcaption>
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

Das ist das richtige Verhalten. Das Ziel lautete „die Lenkung fühlt sich schlecht an" und „die Banden flackern", und kein Headless-Test kann dieses Ziel abschließen. Auto-Pilot hat keine Iterationsobergrenze, es hätte also ewig weitergeprüft. Die Sitzung endete nach Zyklus 8, und was GoKart als Nächstes brauchte, war ein Playtest, kein weiterer Zyklus. An diesem Abend wurde das Repo als 0.0.1 getaggt und für macOS, Windows und Linux exportiert.

## Zwei Tage später: zwei Auto-Pilots in einem Repo

Am 3. Oktober kam ich mit einer anderen Art von Ziel zurück. Diesmal keine Feature-Liste, sondern eine Referenz:

> keep building GoKart to resemble Mario Kart Nintendo 64 version. search Mario Kart N64 or Mario Kart Nintendo 64 and keep improving, iterating, making GoKart better

Diese fünfte Sitzung begann um 14:19 und lief 28 Zyklen, und fast jeder Zyklus ist ein Mario-Kart-64-Element, das der Agent nachgeschlagen und dann gebaut hat. Zuerst kam die Struktur des Spiels: ein 8er-Fahrerfeld auf einem zweispaltigen Startraster, Gummiband-KI je nach Schwierigkeit, 50cc, 100cc und 150cc plus die gespiegelte Extra-Klasse, leichte, mittlere und schwere Karts, die sich gegenseitig schubsen, und ein Grand Prix mit 9/6/3/1 Punkten und der Rank-out-Regel. Dann die anderen Modi: Zeitfahren mit einem Geist und Battle-Modus mit Ballons in Big Donut, Block Fort und Skyscraper. Dann füllte sich das Item-Set mit Dreifach- und goldenen Pilzen, der falschen Item-Box, dem Bananenbündel, Buu Huu, dreifachen roten Panzern und Panzerblocken, und Lakitu kam dazu, um den Fehlstart anzuzeigen, das Startsignal zu geben und die Rundenschilder hochzuhalten.

Der Rest des Nachmittags ging in die Strecken selbst. Eine vierte, Dusty Canyon, kam mit einem Zug im Stil von Kalimari Desert und Bahnübergängen. Sunset Speedway bekam den Verkehr von Toad's Turnpike. Frosty Peaks bekam Sherbet-Land-Eis, Schneemänner und Pinguine, Green Hills bekam Monty-Maulwürfe, und jede Strecke bekam Streckenrand-Kulissen passend zu ihrem Thema, dazu den Windschatten, eine Sprungrampe, den Hop-and-Toggle-Powerslide und einen Chiptune-Loop, im Code aus Step-Patterns gerendert.

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-train.png" alt="GoKart 0.0.2 auf Dusty Canyon: das Spieler-Kart wartet an einem Bahnübergang, während eine Dampflok über die Straße rollt, mit einem Andreaskreuz neben den Gleisen, unter einem Wüstenhimmel." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Dusty Canyon, die vierte Strecke, mit ihrem Zug im Stil von Kalimari Desert. CPU-Karts halten an einem gesperrten Übergang an und warten; ein Kart, das das nicht tut, wird in die Luft geschleudert.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-snowmen.png" alt="GoKart 0.0.2 auf Frosty Peaks: das Spieler-Kart am Eingang eines Feldes von Schneemännern, die in versetzten Reihen über die schneeweiße Straße stehen, jeder mit rotem Schal, Zylinder und Karottennase, unter einem dunkelblauen Dämmerungshimmel." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Das Schneemannfeld auf Frosty Peaks. Wer einen trifft, wird in die Luft geschleudert, während er zu Schnee zerplatzt; CPU-Karts schauen 40 Meter voraus und schlängeln sich durch die Reihen.</figcaption>
</figure>

Vier Stunden später, um 18:25, öffnete ich einen zweiten Tab und startete einen zweiten Auto-Pilot auf demselben Repository, mit einem enger gefassten Ziel:

> the menus are not Mario Kart Quality and neither is the title shot. and there is over use of black outlines on text everywhere. see Mario Kart 64 screenshots and images on the web and make better menus. focus only on the menus / screens and title shot for GoKart. make conscious decisions. do not conflict with previous /auto working on the application

Von 18:25 bis Mitternacht committeten also zwei Agenten in denselben Arbeitsbaum. Die Menü-Sitzung baute den Titelbildschirm rund um ein bogenförmiges Verlaufslogo neu, das hereinfliegt und federt, und arbeitete sich dann durch jeden Bildschirm dahinter: einen Auswahlbildschirm mit einem Bild neben jeder Strecke und einem Live-Überflug der gewählten, Optionszeilen mit leuchtenden Balken, ein sich drehendes Kart-Porträt und einen goldenen Cursor, einen Strecken-Intro-Überflug vor jedem Rennen, einen Pausenbildschirm und eine Ergebnistafel, deren Zeilen nacheinander hereingleiten. Unter all das kam eine gemeinsame Palette aus runder Gold-und-Creme-Schrift mit Schlagschatten, die jede 8-Pixel-Schwarzkontur im Spiel ersetzte. Sie lief 23 Zyklen und erklärte das Ziel um 23:54 für erreicht.

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-select.png" alt="Der Auswahlbildschirm von GoKart 0.0.2: das GOKART-Logo oben, links eine Streckenliste mit einem kleinen Bild neben jedem Streckennamen und der gewählten Zeile hervorgehoben, rechts ein Live-Bild der Strecke mit dem Kartenumriss in der Ecke, Reihen von Options-Pills für Runden, CPU, Motorklasse, Kart-Gewicht und Modus, und das Kart des Spielers, das sich in einem kleinen Porträtfenster dreht, alles über der abgedunkelten Attract-Demo." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Der Auswahlbildschirm nach der Menü-Sitzung. Streckenbilder, ein Live-Überflug der Strecke, jede Option als Reihe von Pills mit der gewählten hervorgehoben, und das Kart, das sich in seinem Porträtfenster dreht.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-gp-results.png" alt="Die Grand-Prix-Ergebnistafel von GoKart 0.0.2 auf einer marineblauen Tafel mit goldenem Rand: links das Rennergebnis und rechts die Cup-Wertung, eine Zeile pro Fahrer mit Farbfeld, Gold-, Silber- und Bronzeplätzen, Zeiten und Punkten, die Zeile des Spielers auf einem leuchtenden goldenen Balken und darunter der Pokal." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Die Grand-Prix-Ergebnistafel: Rennergebnis und Cup-Wertung nebeneinander, die Zeilen gleiten nacheinander herein, jede mit einem Tick, und darunter der Pokal.</figcaption>
</figure>

Die Zeile „do not conflict" hat echte Arbeit geleistet. Das Protokoll ist voll davon, wie die beiden Sitzungen umeinander herum arbeiteten. Die Menü-Sitzung verifizierte aus einem sauberen `git worktree` auf HEAD, damit „die laufende Pinguin-Arbeit der anderen Sitzung" aus ihren Testläufen herausblieb. Auf meine Bitte hin beendete eine Sitzung das halbfertige Feature der anderen. Commits wurden Datei für Datei gestaged statt mit `git add -A`, weil die Änderungen des anderen Tabs im selben Baum lagen. Es war nicht aufgeräumt, aber nichts ging verloren, und die Suite beendete die Nacht mit 14.134 bestanden, 0 fehlgeschlagen.

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-penguins.png" alt="GoKart 0.0.2 auf Frosty Peaks: ein Pinguin, der auf dem Bauch über das blassblau-weiße Eis der langen Kurve vor dem Spieler-Kart rutscht." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Die Pinguine, die aus den Testläufen der Menü-Sitzung herausblieben, auf Eis im Stil von Sherbet Land auf Frosty Peaks. Auf Eis dreht sich die Nase, aber das Kart rutscht weiter in die bisherige Richtung; die Pinguine watscheln zum Rand, plumpsen hin und rutschen wieder zurück.</figcaption>
</figure>

Das Protokoll der Feature-Sitzung endet drei Minuten nach dem der Menü-Sitzung, um 23:57, mit „Session ended — Stop All". Meine Notiz an Agent! direkt danach, die es als Nachricht des nächsten Checkpoint-Commits gespeichert hat, lautete, dass Stop All nur den Tab stoppen muss, in dem es gedrückt wird, nicht alle. Mit zwei laufenden Auto-Pilots ist ein Knopf für beide der falsche Knopf.

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-traffic.png" alt="GoKart 0.0.2 auf Sunset Speedway: das Spieler-Kart hängt hinter einem Bus und einem Kastenwagen mit eingeschalteten Scheinwerfern auf den zwei Spuren der Straße fest, unter dem Sonnenuntergangshimmel." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Verkehr im Stil von Toad's Turnpike auf Sunset Speedway: Autos, Busse, Kastenwagen und Tanklaster mit Scheinwerfern, und Gebäude mit beleuchteten Fensterbändern hinter den Banden.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-battle.png" alt="Battle-Modus in GoKart 0.0.2: vier Karts auf ihren Startfeldern in einer Battle-Arena, jedes mit drei angebundenen Ballons, und Lakitus Startsignal darüber." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Battle-Modus: vier Karts, je drei Ballons. Item-Treffer, Lava, die Dachkante, Sternberührungen und harte Rempler lassen Ballons platzen, und ein Kart ohne Ballons wird zum Mini-Bomben-Kart.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-dusty-canyon.png" alt="Das Strecken-Intro von GoKart 0.0.2 für Dusty Canyon: ein Überflug über die Wüstenstraße mit dem Streckennamen DUSTY CANYON und einer einzeiligen Beschreibung auf einer Karte am unteren Bildschirmrand." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Das Strecken-Intro für Dusty Canyon, der Überflug im Stil von Mario Kart 64, der vor jedem Rennen abläuft, mit der Namenskarte der Strecke am unteren Rand.</figcaption>
</figure>

## Zu diesen Screenshots

Agent! hat sie aufgenommen, nicht ich, und nicht von Hand. Für die erste Version dieses Beitrags bat ich um drei Screenshots einer zufälligen Fahrt, und es schrieb ein 70-zeiliges `tools/random_drive.gd`, das der Straße mit einem wandernden Spurversatz folgt, zufällige Drift-Schübe einstreut, das gehaltene Item zu zufälligen Zeitpunkten abfeuert und alle paar hundert Physik-Frames ein Bild speichert. Das Sunset-Speedway-Bild oben ist ein Frame von diesem Bot.

Der Rest stammt aus den Shot-Tools, die mit jedem Feature mitgeliefert wurden. Es gibt eines für die Menüs, eines für das Strecken-Intro, eines für den Zug, je eines für den Verkehr, die Schneemänner und die Pinguine, eines für das HUD und eines für den Battle-Modus, und jedes baut seine Szene auf, wartet auf den richtigen Frame und speichert ihn. Alle wurden für dieses Update aus einem sauberen Worktree ausgeführt, der auf dem Tag `v0.0.2` ausgecheckt war, sodass nichts Uncommittetes in einem Bild steckt.

Agent! kann sich das Ergebnis immer noch nicht ansehen, also tasten die Tools stattdessen Pixel ab. Das Eis-Bild gibt die Straßenfarbe voraus auf Eis gegenüber Asphalt aus, das Pausen-Bild beweist, dass sich eine Sekunde lang außerhalb des Panels nichts bewegt hat, und vor der Veröffentlichung ließ ich es in allen zehn Bildern oben die rein schwarzen Pixel zählen: null in jedem. Mehr davon stehen in der [GoKart-README](https://github.com/AgentiLoop/GoKart#screenshots).

## Was ich dir sagen würde, bevor du es ausprobierst

- **Lass es in git laufen.** Auto-Pilot hat kein Undo. Das GoKart-Protokoll ist lesbar, weil jeder Zyklus mit einem Commit endete, und als ein Zyklus einmal schiefging, ging nichts verloren.
- **Schreib die Betriebsregeln ins Ziel.** „Setz ein Zeitlimit auf die Shell" funktionierte besser als Teil des Ziels denn als einmalige Nachricht, weil jeder neue Zyklus das Ziel erneut liest.
- **Rechne damit, dass es nach Augen fragt.** Bei allem Visuellen oder Gefühlsmäßigen bleibt die Schleife ehrlich stehen, statt zu lügen. Plane zwischen den Sitzungen einen Playtest ein und gib deine Notizen als nächstes Ziel zurück.
- **Stop All gehört zum Workflow**, es ist kein Fehlschlag. Die ersten drei GoKart-Sitzungen endeten alle damit.
- **Zwei Auto-Pilots in einem Repo funktionieren, wenn du ihnen voneinander erzählst.** „Do not conflict with the previous /auto" kam ins zweite Ziel, und beide Sitzungen gaben sich echte Mühe, einander aus dem Weg zu gehen. Gib ihnen getrennte Bereiche des Codes, und rechne vorerst damit, dass der, den du stoppst, den anderen mitnimmt.

## Ist das gut?

Ich habe Agent! diese Frage gestellt, nachdem es das Repo gelesen, die Commits gezählt und das Auto-Pilot-Protokoll gefunden hatte. Seine Antwort, unbearbeitet:

> Es kommt darauf an, was du dir davon erhoffst. Als Showcase dessen, was Auto-Pilot kann, ist es beeindruckend. Mehr als dreiundzwanzig Zyklen haben vier Strecken, Items, KI-Fahrer, Grand Prix, Zeitfahren, Battle-Modus, prozedurale Musik und Sound hervorgebracht, alles ohne importierte Assets, und eine README, die das im Detail dokumentiert. Das ist eine Menge funktionierende Software aus einer einzigen Zielformulierung.

Es fügte außerdem den Vorbehalt hinzu, dass unterwegs kein Mensch es geprüft hat, die Qualität also anhand der eigenen Verifikationsprotokolle des Agenten beurteilt wurde, und dass es das Spiel weder gespielt noch den Code auditiert hatte, also nicht sagen könne, wie gut es sich tatsächlich spielt. Das ist dieselbe Schlussfolgerung, zu der das Protokoll von allein gekommen ist: Der nächste Schritt ist ein Playtest.

## GoKart 0.0.2

Du brauchst kein Godot, um es auszuprobieren. [GoKart 0.0.2](https://github.com/AgentiLoop/GoKart/releases/tag/v0.0.2) ist das zweite paketierte Release, exportiert aus demselben Repo, 87 Commits nach [0.0.1](https://github.com/AgentiLoop/GoKart/releases/tag/v0.0.1):

- **macOS** universal (Apple Silicon und Intel), mit Developer ID signiert und von Apple notarisiert
- **Windows** x86_64
- **Linux** x86_64 und arm64

Jeder Download ist eine einzelne, eigenständige Binärdatei mit eingebetteten Spieldaten, und `SHA256SUMS.txt` liegt auf der Release-Seite, falls du prüfen willst, was du bekommen hast. Der Windows-Build ist nicht signiert, rechne also mit der SmartScreen-Abfrage. Alles oben Beschriebene, was nicht in 0.0.1 war, ist in 0.0.2, vom Battle-Modus und Zeitfahren bis zum Zug, dem Verkehr, den neuen Menüs und dem neu gestalteten HUD; die Release Notes haben die vollständige Liste.

Agent! 1.1.87 mit Auto-Pilot gibt es auf der [Releases-Seite](https://github.com/AgentiLoop/Agent/releases/latest) und in Homebrew. Wenn du GoKart lieber aus dem Quellcode startest, braucht es Godot 4.4 oder neuer: `git clone https://github.com/AgentiLoop/GoKart.git && cd GoKart && godot --path .`
