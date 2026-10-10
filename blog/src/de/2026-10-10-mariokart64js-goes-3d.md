---
title: MarioKart64JS wird 3D: Wii-Karts, ein 3D-Titelbildschirm und Kameraflüge nach dem Ziel
description: Mario Kart 64 zeichnet seine Fahrer als flache Sprites. Drückt man in MarioKart64JS die 3, wird jedes Kart zu einem 3D-Modell, Lakitu eingeschlossen, mit echten Schatten, einem neu gebauten 3D-Titelbildschirm und einer Kamera, die nach dem Ziel um das eigene Kart fliegt. Hier steht in Screenshots, wie der 3D-Modus entstanden ist.
tags: Showcase, JavaScript
---
<figure style="margin:2rem 0">
<img src="/mk64js-3d-title.jpg" alt="Der 3D-Titelbildschirm von MarioKart64JS: Wario, Bowser, Mario, Peach und Toad fahren in 3D-Karts unter dem Mario-Kart-64-Logo auf die Kamera zu." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Der 3D-Titelbildschirm. Das Original ist ein einziges flaches Gemälde. Hier sind Himmel, Hügel und Straße in Three.js gebaut, und die fünf Fahrer sind 3D-Karts, die auf die Kamera zufahren.</figcaption>
</figure>

Im [letzten MarioKart64JS-Beitrag](/blog/mariokart64js-from-scratch-in-javascript/) ging es darum, Mario Kart 64 so genau wie möglich zu treffen: Streckengeometrie, Sprites und Musik aus dem Modul, und neues JavaScript, das tut, was der C-Code des Originals tut. In diesem geht es um die entgegengesetzte Richtung. Eine Taste, **3**, schaltet einen 3D-Modus ein, den das N64 nie hatte.

## Aus Sprites werden Modelle

Die Fahrer in Mario Kart 64 sind keine Modelle. Jeder Fahrer besteht aus 321 vorgerenderten Frames mit 64×64 Pixeln, und das Spiel wählt den Frame, der zum Kamerawinkel passt. Genau das zeichnet auch MarioKart64JS, und standardmäßig tut es das weiterhin.

Der 3D-Modus ersetzt diese Sprites durch Modelle des Standard-Karts aus Mario Kart Wii, aus Collada-Exporten, die `tools/build-wii-karts.py` ins Projekt übernimmt. Angefangen hat es am Abend des 9. Oktober als einzelner Test: Um 21:22 setzte die Taste 3 ein rotes Standard-Kart mit Mario darin unter den Spieler. Um 22:02 hatten alle acht Fahrer eines, aufgeteilt nach den Gewichtsklassen der Wii: das kleine Kart für Toad, das mittlere für Mario, Luigi, Peach und Yoshi und das große für D.K., Wario und Bowser, jedes mit eigener Lackierung.

Die meiste Arbeit dazwischen bestand aus Kleinigkeiten, die ein Modell-Loader falsch macht:

- **Die Augen.** Jede Augentextur ist ein einzelnes Auge. Auf der Wii verdoppelt eine Texturmatrix es, und der Sampler spiegelt es zu einem Paar. Der ColladaLoader von Three.js verwirft beides, sodass ein einziges Auge über das ganze Gesicht gestreckt war. `kart3d.js` stellt Wiederholung und Spiegelung pro Figur wieder her.
- **Die Reifen.** Die Hinterreifen sind das hochskalierte Mesh des Vorderreifens. Ihre Größe und die Achspositionen werden am zusammengesetzten Menümodell jedes Karts gemessen, wodurch die Hinterreifen 1,29× größer wurden und dort sitzen, wo die Wii sie hat.
- **Die Sitze.** Jeder Fahrer bekommt eine Sitzposition, damit er im zurückgelehnten Sitz sitzt, statt darüber zu schweben.

Agent! kann sich kein Bild ansehen, also prüfte es die Modelle stattdessen mit Zahlen: ASCII-Ansichten jedes Karts von der Seite, von hinten und von oben, Drehteller-Bögen mit 12 Winkeln und gemessene Abstände zwischen den Händen jedes Fahrers und dem Lenkrad.

## Rennen in 3D

<figure style="margin:2rem 0">
<img src="/mk64js-3d-race-mario.jpg" alt="MarioKart64JS im 3D-Modus beim Rennen auf Mario Raceway mit 3D-Karts." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Mario Raceway im 3D-Modus. Jedes Kart im Rennen ist ein 3D-Modell, jedes im Standard-Kart seiner eigenen Figur.</figcaption>
</figure>

Im Rennen tauscht die 3 jedes Kart auf der Strecke aus, nicht nur das eigene, und der nächste Druck bringt die Sprites zurück. Zwei weitere Dinge ändern sich mit.

**Schatten.** Die Sprites haben einen flachen Klecks-Schatten unter sich. Die 3D-Karts werfen echte Shadow-Map-Schatten auf die Strecke. Dafür war ein Trick nötig: Die Strecke wird mit unbeleuchteten Materialien gezeichnet, die keine Schatten empfangen können, also bekommt sie durchsichtige Schattenfänger-Kopien ihrer Oberflächen, die nur dort sichtbar sind, wo ein Schatten hinfällt.

**Lakitu.** Der Schiedsrichter wird zum Lakitu aus Mario Kart Wii (`src/lakitu3d.js`). Seine Arme werden über die eigenen Knochen des Modells positioniert: Einer hält die Angel, der andere schwenkt die Flagge. Startampel, Rundentafeln und Falsche-Richtung-Schild hängen am Haken der Angel, und der Animationsframe des ursprünglichen Sprites bestimmt weiterhin das Timing, sodass der Countdown Rot, Rot, Blau genau dann kommt, wann er immer kam.

Ein 3D-Kart hat außerdem einen Körper, den das Sprite nicht hatte. An Wänden ist es eine Kapsel, ein Kreis über jeder Achse, und es bewegt und dreht sich als starrer Körper. Das hatte Nebenwirkungen. Auf Koopa Troopa Beach erreichte der vordere Kreis die Kante einer Rampe vor dem Mittelpunkt des Karts, und die Rückseite der Kante warf das Kart vom Sprung. Die Lösung prüft jede Achse gegen den Boden darunter. Ein späterer Commit verhinderte, dass Wände das Kart des Spielers bei einem Frontalaufprall drehen, denn in Mario Kart 64 reflektiert eine Wand die Bewegung des Karts und ändert nie seine Blickrichtung.

## Ein 3D-Titelbildschirm

Der Titelhintergrund von Mario Kart 64 ist ein einziges flaches Bild mit 320×240 Pixeln. Himmel, Hügel, Straße und die fünf Fahrer sind alle hineingemalt. Ein Druck auf die 3 im Titel baut ihn neu auf (`src/title3d.js`): Himmel, Hügel und Straße entstehen in Three.js, und die Fahrer sind dieselben 3D-Karts wie in den Rennen.

Die Anordnung folgt dem Gemälde. Wario ist vorne links mit Bowser hinter ihm, Mario vorne rechts mit Peach dahinter, und Toad kommt aus der Rechtskurve. Jedes Kart ist so platziert, dass sein Rahmen auf dem Bildschirm bis auf etwa 10 Pixel genau auf dem Rahmen seines Fahrers in der Originalgrafik liegt. Die Kamera sitzt tief auf der Straße vor ihnen, mit einem weiten 64°-Objektiv, und die Straße scrollt darunter durch, sodass es aussieht, als würden die Karts direkt auf einen zufahren. Die Zielflagge, das Logo, PUSH START und der Copyright-Hinweis sind weiterhin die 2D-Overlays aus dem Originaltitel.

Auch die Menüs dahinter haben passende Hintergründe bekommen. Wer 3D im Titel einschaltet, wechselt außerdem auf die 4×-Texturstufe, und Rennen starten in 3D, bis man erneut die 3 drückt.

<figure style="margin:2rem 0">
<img src="/mk64js-3d-game-select.jpg" alt="Der Spielauswahl-Bildschirm von MarioKart64JS mit seinem Hintergrund im 3D-Modus." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Der Spielauswahl-Bildschirm mit seinem Hintergrund im 3D-Modus.</figcaption>
</figure>

## Kameraflüge nach dem Ziel

Wenn man die Ziellinie überquert, übergibt Mario Kart 64 die Kamera an eine kurze Filmsequenz. MarioKart64JS folgt dafür dem Kamera-Code des Spiels (`PLAYER_CINEMATIC_MODE` und die Funktionen für die Kameraeinstellungen in der Dekompilierung): Die Kamera schwenkt nach vorne vor das Kart und sieht zu, wie es die Linie überquert, dann schneidet sie zwischen Einstellungen hin und her, während der CPU-Fahrer das eigene Kart übernimmt. Die Abfolge wiederholt Bugumkreisung, Straßenrand, hoher Kran, Straßenrand, tiefe Heckeinstellung, Straßenrand. Eine Einschränkung aus den Quellcode-Kommentaren: Die Längen und Abstände der Einstellungen sind nach Augenmaß abgestimmt, nicht aus den Tabellen im ROM übernommen.

Die Verfolgungseinstellungen folgen einer stark geglätteten Kopie der Fahrtrichtung des Karts. Ohne sie ließen die kleinen Lenkkorrekturen der KI die Kamera um das Kart wackeln, und es sah aus, als würde es ruckartig lenken. Mit 3D-Karts zeigen diese Einstellungen die Modelle am meisten, weil die Kamera die Karts endlich von vorne und von der Seite sieht.

<figure style="margin:2rem 0">
<img src="/mk64js-3d-flyover-front.jpg" alt="Kameraflug nach dem Ziel auf Mario Raceway: Die Kamera vor Marios 3D-Kart blickt auf es zurück." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Die Bugeinstellung auf Mario Raceway: Die Kamera kreist von hinter dem Kart nach vorne und fährt vor ihm her.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-3d-flyover-crane.jpg" alt="Kameraflug nach dem Ziel auf Mario Raceway: eine hohe Kranaufnahme, die hinter dem Kart die Straße hinunterblickt." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Die hohe Kranaufnahme, über und hinter dem Kart, mit Blick die Straße hinunter.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-3d-flyover-roadside.jpg" alt="Kameraflug nach dem Ziel auf Royal Raceway: eine Kamera am Straßenrand, während das Kart vorbeifährt." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Eine Straßenrand-Einstellung auf Royal Raceway. Die Kamera steht vorne neben der Straße und hält, bis das Kart vorbeigefahren ist.</figcaption>
</figure>

## Wie die Screenshots entstanden sind

Jedes Bild in diesem Beitrag wurde in Headless Chrome bei 1280×960 aufgenommen. Für die Titel- und Spielauswahl-Aufnahmen wird im Titel die 3 gedrückt, genau wie ein Spieler es tun würde. Die Rennen laufen auf Autopilot mit gespeichertem 3D-Modus, und die Kameraflüge wurden aufgenommen, indem der Spieler auf das letzte Stück der letzten Runde gesetzt und nach dem Ziel alle 0,7 Sekunden ein Frame gespeichert wurde. Agent! wählte die Frames durch Messen aus: Die Position der Kamera relativ zum Kart verriet, welche Einstellung jeder Frame war, und Pixelstatistiken sortierten dunkle oder detailarme Frames aus. Wie beim letzten Beitrag hat es sie sich nicht selbst angesehen.

## Ausprobieren

Klone [AgentiLoop/MarioKart64JS](https://github.com/AgentiLoop/MarioKart64JS), führe `npm install && npm run dev` aus, öffne `http://localhost:5173` und drücke **3** im Titelbildschirm oder in einem Rennen. Der Web-Build enthält ebenfalls die 3D-Karts, Lakitu und den 3D-Titel. Die übernommenen Modelle liegen in `public/wii/`; `tools/build-wii-karts.py` und `tools/build-wii-lakitu.py` sind die Skripte, die sie aus den Collada-Dateien übernommen haben.

*MarioKart64JS ist ein Fan-Forschungsprojekt, um zu testen, wie weit KI beim Duplizieren eines Spiels gehen kann. Mario Kart 64 und Mario Kart Wii sind © Nintendo, und ihre Assets gehören Nintendo. Das Projekt steht in keiner Verbindung zu Nintendo und wird von Nintendo nicht unterstützt.*
