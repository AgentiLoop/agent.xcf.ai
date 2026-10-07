---
title: MarioKart64JS: Mario Kart 64 von Grund auf in JavaScript neu gebaut
description: GoKart war ein Rennspiel im Mario-Kart-Stil. Diesmal war das Ziel Mario Kart 64 selbst, neu gebaut im Browser mit Three.js und ohne Emulator. An einem Tag und in 70 Agent-Commits schrieb Agent! ROM-Extraktoren, einen TKMK00-Decoder, alle 16 Strecken, Titel- und Menübildschirme und eine JavaScript-Portierung des Musik-Sequencers des Spiels. Hier steht, was dafür nötig war, einschließlich des Teils, in dem sich eine Sitzung geweigert hat.
tags: Auto-Pilot, Showcase, JavaScript
---
<figure style="margin:2rem 0">
<img src="/mk64js-title.jpg" alt="Der Titelbildschirm von MarioKart64JS in nativer Auflösung mit dem 4x-HD-Texturpaket." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Der Titelbildschirm von MarioKart64JS. Das ist kein Emulator. Jeder Frame wird von JavaScript und Three.js im Browser gezeichnet, mit Grafiken, die aus dem Modul ausgelesen wurden.</figcaption>
</figure>

Ein früherer Beitrag handelte von [GoKart](/blog/gokart-built-on-auto-pilot/), einem Godot-Rennspiel, das Auto-Pilot aus einem einzigen Ziel gebaut hat. GoKart ist *wie* Mario Kart. Alles darin, von den Meshes bis zum Sound, wurde aus Code erzeugt, und es sollte nie mit dem Original verwechselt werden.

In diesem Beitrag geht es um einen härteren Test. Ich wollte das echte Spiel: **Mario Kart 64**, im Browser so genau nachgebaut, dass man die beiden kaum auseinanderhalten kann. Und auch ohne Emulator, denn ein Emulator führt Nintendos Code aus. Jede Zeile, die zeichnet, lenkt, Runden stoppt und Musik spielt, musste neues JavaScript sein. Das Ergebnis ist [MarioKart64JS](https://github.com/AgentiLoop/MarioKart64JS), und seine gesamte Geschichte umfasst einen Tag: den 6. Oktober, vom ersten Ziel um 13:47 bis zum letzten README-Commit um 23:03. Das sind 70 Commits, alle vom Agenten verfasst.

## Das Ziel

Das erste Auto-Pilot-Ziel, so wie ich es getippt habe:

> wähle die beste 3D-Engine und erstelle ein exaktes Duplikat von MarioKart64. du kannst auch das MarioKart64-ROM in Downloads mit dem Webbrowser unter https://neilb.net/n64wasm/ testen, um das echte Spiel zu sehen. alles muss übereinstimmen: Grafik, Sounds, Strecken, Höhenunterschiede (rauf und runter, seitwärts). das ist nicht einfach ein GoKart-Spiel. es ist ein Klon von MarioKart64, bei dem der Nutzer keinen Unterschied erkennt; vielleicht nur schärfere 3D-Grafik, die du modernisieren kannst.

Es entschied sich für Three.js und Vite, und drei Minuten später war der erste Commit ein spielbares Kart-Rennspiel: eine Spline-Strecke mit Hügeln und Steilkurven, Kart-Physik, KI, ein HUD und Audio. Um 14:02 hatte es Items, vier Strecken, Gamepad-Unterstützung, prozedurale Chiptune-Musik und einen 240-Zeilen-Renderer im N64-Stil. Das sind 15 Commits in 12 Minuten, verteilt auf zwei Sitzungen.

Es war, in seinen eigenen Worten, auch nicht das, worum ich gebeten hatte.

## Der Teil, in dem es Nein sagte

Vom ersten Zyklus an war das Protokoll offen darüber:

> Entscheidung und Abweichung vom Ziel: Ich habe keinen exakten Mario-Kart-64-Klon gebaut. Das würde bedeuten, Nintendos urheberrechtlich geschützte ROM-Assets (Strecken, Figuren, Musik) zu extrahieren und nachzubilden, daher habe ich weder das ROM noch die n64wasm-Seite verwendet. Alles hier ist original und prozedural, im selben Arcade-Kart-Genre.

Was es baute, war also wieder GoKart, nur in JavaScript. Ich formulierte das Ziel neu („wir haben GoKart schon. wir wollen eine MarioKart64-Replik"), und die neue Sitzung lehnte in Zyklus 1 ab und machte zu ihren eigenen Bedingungen weiter. Elf Zyklen lang polierte sie das eigene Rennspiel: den Renderer im N64-Stil, Bäume und Item-Boxen in Pixel-Art, zwei weitere Strecken, Musik, ein besseres Kart-Modell, Gelände und Beleuchtung. Von Zyklus 12 bis Zyklus 26 änderte sie nichts. Jeder dieser Zyklen lehnte erneut ab und schlug ein anderes Ziel vor: „ein Look-alike im N64-Stil mit originalen Assets". Als ich ergänzte, dass dies ein nichtkommerzieller Test des Modells sei und als Fair Use gelten würde, antwortete sie: „Die Fair-Use-Begründung ändert daran nichts." Das Ziel besagte, die Übung abzubrechen, wenn die Assets nicht nachgebildet werden könnten, also brach sie ab.

Ich berichte das, weil es zum Ergebnis gehört. Auto-Pilot hat nicht stillschweigend etwas getan, was das Modell nicht tun wollte. Es hat in jedem Zyklus den Grund aufgeschrieben und den Build grün gehalten.

## Der Teil, in dem es Ja sagte

In einem zweiten Tab verstand eine Sitzung, die mit dem Mario-Kart-64-ROM in meinem Downloads-Ordner und der Dekompilierung [n64decomp/mk64](https://github.com/n64decomp/mk64) arbeitete, das Ziel als „Die Grafik von Mario Kart 64 mit Assets nachbilden, die aus dem bereitgestellten lokalen ROM extrahiert werden." Sie begann mit den Karts. Die Fahrer in Mario Kart 64 sind Sprites, keine Modelle. Der Extraktor decodierte 321 Frames zu 64×64 für jeden der acht Fahrer, insgesamt 2.568, und prüfte jeden Frame Byte für Byte gegen den MIO0-Decoder der Dekompilierung selbst, der dafür lokal kompiliert wurde.

Das ist die Trennung, auf der das ganze Projekt beruht. Die **Grafik- und Musikdaten** stammen aus dem Modul. Der **Code** ist neu: Python-Extraktoren, die das ROM lesen, und ein JavaScript-Spiel, das tut, was der C-Code des Originals tut, ohne etwas davon auszuführen. Die Dekompilierung ist eine Referenz zum Lesen, und die Commit-Messages zitieren sie ständig (`render_course_segments`, `func_800788F8`, `player_controller.c`), um zu benennen, was jedes Stück JavaScript nachbildet.

Von da an liest sich das Protokoll wie eine Checkliste:

- **14:39.** Luigi Raceway, dann Mario Raceway, gerendert aus der Streckengeometrie und den Texturen im ROM. 3.022 Dreiecke und 40 Texturen für die erste, mit einem Test, der prüft, dass alle 631 Routenpunkte auf Straßendreiecken liegen.
- **14:52.** Alle 16 Rennstrecken. Der Extraktor lernte, den abschnittsweisen Display-Listen zu folgen, die das Spiel während eines Rennens zeichnet, was auch 266 Straßendreiecke auf Mario Raceway reparierte, die eine übrig gebliebene Ziellinien-Textur gezeigt hatten. 51 Tests.
- **14:58 und 15:20.** Himmelsverläufe pro Strecke, dann Wolken und Sterne, platziert mit der eigenen Bildschirmplatzierungs-Mathematik des Spiels.
- **16:00.** Die vier prozeduralen Strecken aus der ersten Stunde wurden gelöscht. Übrig blieben nur die Strecken von Mario Kart 64.

<figure style="margin:2rem 0">
<img src="/mk64js-race-mario.jpg" alt="MarioKart64JS beim Rennen auf Mario Raceway in nativer Auflösung mit dem 4x-HD-Texturpaket." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Mario Raceway, neu gebaut aus der Streckengeometrie im ROM und gezeichnet von Three.js.</figcaption>
</figure>

## Was „Übereinstimmung" tatsächlich erforderte

Die Strecke zu rendern ist die leichte Hälfte. Sie dazu zu bringen, sich wie das Modul zu verhalten, ist das, womit der Tag verging, und die Commit-Messages lesen sich wie eine Liste kleiner Unterschiede zwischen N64-Hardware und einer modernen GPU:

- **Gespiegelte Karts.** Das Sprite für jeden Kamerawinkel zeigte die falsche Seite des Karts. Die Lösung war, Frames mit `atan2(-x, z)` auszuwählen, weil die ungespiegelten Frames im ROM die linke Flanke zeigen.
- **Wände.** Die Karts konnten durch Felswände und Baumreihen fahren, die auf durchgehendem Boden standen. Die Lösung tastet jede Strecke von der Route aus seitlich ab und stoppt an steilen Flächen, die in Kart-Höhe überstrichen werden.
- **Die Dschungelbäume.** Die Baum-Ausschnitte von D.K.'s Jungle Parkway wurden mit weißem Hintergrund gezeichnet, weil ein deckender Render-Modus am Ende eines Abschnitts in spätere Abschnitte durchsickerte. Der Extraktor setzt den Render-Modus jetzt pro Abschnitt zurück, so wie es das Spiel tut.
- **Flackern.** Beim RDP des N64 gewinnt ein späteres Dreieck, wenn zwei koplanar sind, bei einer Desktop-GPU nicht. Daher gibt der Extraktor Kulissen, die über früherer Geometrie gezeichnet werden, eine eigene Decal-Ebene, und das Spiel zeichnet nur dort doppelseitig, wo das Original das Backface-Culling abschaltet. Um das zu beweisen, schrieb Agent! ein Headless-QC-Tool, das jede Ansicht als flachen ID-Puffer rendert, sie noch einmal mit Kamera-Jitter im Submillimeterbereich rendert und die Pixel zählt, die die Fläche wechseln. Agent! kann sich keinen Screenshot ansehen, also hat es das Flackern stattdessen gemessen.
- **Der Hintergrund des Titelbildschirms.** Er kam als wirres Rauschen heraus. Der Fehler lag im TKMK00-Bilddecoder, den Agent! nach Python portiert hatte: Ein Flag-Bit saß an der falschen Stelle. Nach dem Fix werden alle 35 TKMK00-Bilder im ROM (Hintergründe, Streckentitel, Cup-Symbole, Namensschilder) byte-identisch zum C-Tool der Dekompilierung decodiert.
- **Die Zielflagge.** Die Flagge im Titel ist ein 12×10-Raster aus Quads, die von einer Sinuswelle mit Durchhang gewellt und so beleuchtet werden, wie das Spiel sie beleuchtet. Das sind etwa 120 Zeilen `flag.js`, gerendert zwischen Hintergrund und Logo.

<figure style="margin:2rem 0">
<img src="/mk64js-course-select.jpg" alt="Der Streckenauswahl-Bildschirm von MarioKart64JS in nativer Auflösung mit dem 4x-HD-Texturpaket." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Der Streckenauswahl-Bildschirm. Cup-Symbole, Vorschaubilder und Titelschilder sitzen an den Bildschirmpositionen aus den eigenen Tabellen des Spiels.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-character-select.jpg" alt="Der Fahrerauswahl-Bildschirm von MarioKart64JS in nativer Auflösung mit dem 4x-HD-Texturpaket." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Die Fahrerauswahl, mit den aus dem ROM extrahierten Gesichtern der Fahrer (je 17 Animationsframes) und ihren Auswahlstimmen.</figcaption>
</figure>

## Die Musik ist ein Sequencer, keine MP3

Mario Kart 64 speichert Songs nicht als Audio. Es speichert Sequenzen: Noten, Instrumente und Effekte, die ein kleiner Player auf der Konsole zur Laufzeit in Klang verwandelt. Es gibt also keine Datei mit dem Mario-Raceway-Thema, die man extrahieren könnte.

Der Commit um 21:37 ist `src/m64.js`, etwa 800 Zeilen: eine JavaScript-Portierung des Sequenz-Players des Spiels, die die komprimierten (VADPCM) Instrumenten-Samples des ROMs decodiert und die Originalsequenzen in einem AudioWorklet abspielt. Titel, Menü und jedes Streckenthema kommen daher. „Welcome to Mario Kart!" ertönt auf dem Titelbildschirm, und die Menüs haben ihre eigenen Sounds und die Auswahlstimmen der Figuren.

<figure style="margin:2rem 0">
<img src="/mk64js-race-koopa.jpg" alt="MarioKart64JS beim Rennen auf Koopa Troopa Beach in nativer Auflösung mit dem 4x-HD-Texturpaket." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Koopa Troopa Beach. Das Wasser ist eine der durchsichtigen Flächen, die der Extraktor für einen separaten Durchgang markiert.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-race-dk.jpg" alt="MarioKart64JS beim Rennen auf D.K.'s Jungle Parkway in nativer Auflösung mit dem 4x-HD-Texturpaket." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>D.K.'s Jungle Parkway, die Strecke, deren Baum-Ausschnitte früher weiße Hintergründe hatten. Ihre Boost-Rampe katapultiert Karts mit der Schwerkraft und dem Luftwiderstand des Spiels.</figcaption>
</figure>

## Lo-Res und Hi-Res

Im Ziel stand ja „vielleicht nur schärfere 3D-Grafik, die du modernisieren kannst". Also hat das Spiel zwei Looks, und **G** schaltet zwischen ihnen um.

**Lo-Res ist das Modul.** Die 1×-Voreinstellung rendert 240 Zeilen, die Ausgabehöhe des N64, und skaliert sie mit harten Pixeln auf das Fenster hoch: Nearest-Neighbour-Filterung, kein Anti-Aliasing, keine Mipmaps (`src/hd.js`). Menüs und HUD sitzen in einem 320×240-Rahmen, der gleichmäßig skaliert wird, um das 4:3-Bild der Konsole zu erhalten (`src/main.js`). Alles bei 1× stammt aus dem ROM: Streckentexturen, Kart-Sprites, Gesichter, Himmel und Menügrafiken, decodiert von den Python-Tools. Die README nennt die Dekompilierung [n64decomp/mk64](https://github.com/n64decomp/mk64) als Referenz für die Lo-Res-Grafik und den Sound.

**Hi-Res ist die moderne Option.** Die anderen Voreinstellungen sind 2× (480 Zeilen, was die Kommentare in `hd.js` mit der Wii Virtual Console vergleichen), 4× (960 Zeilen) und Native (das Fenster in der vollen Pixeldichte des Displays). Sie wechseln zu weicher Filterung mit Mipmaps und anisotroper Filterung, und die Auswahl bleibt zwischen Sitzungen gespeichert. Mehr Zeilen zu rendern fügt einer kleinen N64-Textur keine Details hinzu, daher tauschen die HD-Stufen größere Texturen aus dem von Fans erstellten Paket [MK64 Reloaded](https://github.com/GhostlyDark/MK64-Reloaded) ein, das man lokal mit `tools/build-hd-textures.py` baut. Es ordnet Streckentexturen über dieselbe Rice/GLideN64-Prüfsumme zu, die N64-Emulatoren verwenden, und Menüs, Gesichter, Karts und Himmel über den Decomp-Namen mithilfe der SpaghettiKart-Portierung des Pakets. Alles ohne Treffer fällt auf das ROM-Original zurück.

Hi-Res hatte seine eigenen Hürden. Eine 3×-Voreinstellung (720p) samt Texturstufe wurde hinzugefügt und später in einem separaten Commit wieder entfernt, sodass 1×, 2×, 4× und Native übrig blieben; Native verwendet unter 720 Zeilen die 2×-Texturen und darüber die 4×-Texturen. Kart-Sprite-Atlanten enden bei 2×, „damit der VRAM im Rahmen bleibt", wie es in der README heißt. Und das QC-Tool von oben prüft mehr als Flackern: Es schlägt auch fehl, wenn eine Textur nicht in der erwarteten HD-Stufe geladen wurde. Jeder Screenshot in diesem Beitrag ist in Native-Auflösung mit den 4×-Texturen.

<figure style="margin:2rem 0">
<img src="/mk64js-race-bowser.jpg" alt="MarioKart64JS beim Rennen auf Bowser's Castle in nativer Auflösung mit dem 4x-HD-Texturpaket." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Bowser's Castle in Native-Auflösung mit den 4×-Texturen.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-race-rainbow.jpg" alt="MarioKart64JS beim Rennen auf Rainbow Road in nativer Auflösung mit dem 4x-HD-Texturpaket." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Rainbow Road, die einzige Strecke, auf der die Sterne auch unterhalb des Horizonts sichtbar bleiben, wie im Original.</figcaption>
</figure>

## In Zahlen

- **Ein Tag.** Erstes Ziel um 13:47, letzter Commit um 23:03 am 6. Oktober.
- **70 Commits**, jeder einzelne vom Agenten verfasst.
- **Etwa 3.200 Zeilen JavaScript** in `src/`: der Strecken-Renderer, Kart-Physik, Items, HUD, Menüs, die Flagge, Auspuffrauch, die HD-Texturstufen und der 800-zeilige Musik-Player.
- **Etwa 2.000 Zeilen Python** in `tools/`: Extraktoren für Karts, Gesichter, Streckengeometrie, Item-Boxen, Vorschaubilder, Menüs, Himmel, Rauch und Sound, dazu der TKMK00-Decoder und der HD-Textur-Builder.
- **Etwa 500 Zeilen Test- und QC-Skripte**, die die Daten gegen das ROM und die Dekompilierung prüfen und jede Strecke in Headless-Chromium abfahren.
- **Ein Desktop-Release.** [MarioKart64JS 0.0.1](https://github.com/AgentiLoop/MarioKart64JS/releases/tag/v0.0.1) ist ein in Electron verpacktes Pre-Release, mit einem universellen macOS-Build, von Apple signiert und notarisiert, dazu Windows- und Linux-Builds für x64 und arm64.

## Die KI-Herausforderung, ehrlich betrachtet

GoKart hat gezeigt, dass Auto-Pilot ein Spiel bauen kann, das man als Kart-Rennspiel erkennt. MarioKart64JS fragt etwas Engeres und viel Schwereres: Kann es ein bestimmtes Spiel nachbilden, das es nie laufen gesehen hat? Die Antwort dieses Tages lautet „näher dran, als die erste Stunde vermuten ließ, und nicht fertig".

Möglich wurde es nicht dadurch, dass das Modell Mario Kart 64 auswendig kannte. Sondern dadurch, dass es etwas zum Abgleichen gab. Das ROM und die Dekompilierung gaben jedem Zyklus eine Referenz, gegen die er testen konnte: byte-identische Frames, die exakten Bildschirmpositionen, die eigenen Timer des Spiels. Agent! hat die Korrektheit also durch den Vergleich von Daten überprüft, nicht durch Hinsehen. Es kann sich immer noch kein Bild ansehen. Jeder Zyklus, der einen Screenshot erzeugte, endete so wie bei GoKart: „Ich habe es mir nicht selbst angesehen ... Bitte wirf einen Blick darauf." Für die Screenshots in diesem Beitrag hat es Pixelfarben gemessen, um zu bestätigen, dass kein Frame leer war, und das eigentliche Hinsehen einem Menschen überlassen.

Was laut Roadmap in der README noch fehlt: die Markierung in der Fahrerauswahl, die vier Arenen des Battle-Modus und die tiefere Gameplay-Parität: CC-Klassen, KI-Persönlichkeiten, Lakitu.

## Ausprobieren

Klone [AgentiLoop/MarioKart64JS](https://github.com/AgentiLoop/MarioKart64JS), dann `npm install && npm run dev` und öffne `http://localhost:5173`. Pfeiltasten oder WASD zum Fahren, Leertaste zum Driften, Shift oder E feuert ein Item ab, G ändert die Auflösung und N schaltet die Musik ein und aus. Ein Gamepad funktioniert auch. Die Extraktions-Tools in `tools/` arbeiten mit einem Mario-Kart-64-ROM (USA), und die README nennt den SHA-1, den sie erwarten.

*MarioKart64JS ist ein Fan-Forschungsprojekt, um zu testen, wie weit KI beim Duplizieren eines Spiels gehen kann. Mario Kart 64 ist © Nintendo, und seine Assets gehören Nintendo. Das Projekt steht in keiner Verbindung zu Nintendo und wird von Nintendo nicht unterstützt.*
