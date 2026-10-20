---
title: AgentiLoop Racing, Prototype III: ein F1-Simulator im Browser
description: AgentiLoop Racing ist ein Formelsport-Rennsimulator, der im Browser läuft, gebaut mit Agent! in Three.js. Er hat 240-Hz-Physik, 18 echte Strecken, ein KI-Feld, Boxenstopps, Reifenmischungen, Kraftstoff, ERS und DRS. Spielbar unter f1.gokart.games.
tags: Showcase, JavaScript
---
<figure style="margin:2rem 0">
<img src="/agentiloop-racing-og.jpg" alt="AgentiLoop Racing: ein Formelrennwagen auf der Strecke im Browser-Simulator." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>AgentiLoop Racing, Prototype III. Jedes Auto im Feld ist ein RB22-Modell von 2026, neu lackiert in eigenen Farben und mit eigenen Sponsorennamen.</figcaption>
</figure>

**Jetzt spielen: [f1.gokart.games](https://f1.gokart.games).** Kein Download, keine Installation. Nötig ist ein Browser mit WebGL, gespielt wird mit Tastatur oder einem Xbox-Controller (oder einem anderen Standard-Controller).

AgentiLoop Racing ist ein Rennsimulator im F1-Stil, geschrieben in reinem JavaScript und Three.js. Der erste Commit, ein deterministisches Vierrad-Fahrzeugmodell, ging am Abend des 16. Oktober ein. Drei Tage und 109 Commits später fährt er mit einem kompletten KI-Feld auf 18 echten Strecken, mit Boxenstopps, Reifenmischungen, Kraftstoff, ERS und DRS, einem aus der Physik erzeugten Motorsound und einer Cockpitkamera, deren Spiegel die Autos hinter einem zeigen. Agent! hat ihn geschrieben, einen kleinen, getesteten Commit nach dem anderen.

Vorab eine ehrliche Einordnung, dieselbe, die auch in der README steht: Es ist ein **Prototyp, kein validierter Formel-1-Simulator**. Die Parameter des Autos sind anschauliche Annahmen, keine gemessenen F1-Daten.

## Zuerst die Physik

Das Projekt begann als Physik-Testumgebung, das 3D kam erst danach. `physics.mjs` berechnet das Auto in festen Schritten mit **240 Hz**. Jedes Rad hat seine eigene Trägheit und seinen eigenen Schlupf, und jeder Reifen hat eine Grip-Kurve, die von maximalem Grip bis zum Rutschen reicht, dazu Schräglaufwinkel-Relaxation, Temperatur und Verschleiß. Die gefederte Karosserie rollt, nickt und senkt sich unter Abtrieb ab, und das sieht man am 3D-Auto. Das Getriebe schaltet automatisch oder per Schaltwippen, und es gibt einen abgesicherten Rückwärtsgang für den Fall, dass man vor einer Mauer landet.

Auch die Antriebseinheit ist modelliert. Der Kraftstoff wird als echte Masse mitgeführt, sodass das Auto leichter wird, während er verbrennt. Das Hybridsystem gibt oberhalb von 100 km/h bis zu 120 kW ab, innerhalb von 4 MJ pro Runde, und gewinnt beim Bremsen Energie zurück.

Die Testsuite ist der eingebaute Test-Runner von Node und sonst nichts: `node --test` führt heute 158 Tests aus, alle bestanden. Sie prüfen etwa, dass ein Auto bei Vollgas nie durch eine Mauer tunnelt und dass das 3D-Modell den Boden nur mit Reifen und Unterbodenplanke berührt.

## 18 echte Strecken

<figure style="margin:2rem 0">
<img src="/agentiloop-racing-monza.jpg" alt="AgentiLoop Racing: ein Rennen in Monza gegen das KI-Feld." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Ein Rennen in Monza. Die Zeitenanzeige, der Rennstand und die Minikarte laufen während des Rennens live mit.</figcaption>
</figure>

Neben einer fiktiven Stadion-Teststrecke gibt es 18 echte Strecken, von Bahrain bis Miami, darunter Monza, Silverstone, Spa und Monaco, mit Layouts, die aus echten Fahrzeugpositionen erstellt wurden. Den Rest haben echte Daten abgestimmt:

- **DRS-Zonen** stammen aus Renntelemetrie von 2024 (OpenF1): wo die Fahrer die Klappe tatsächlich geöffnet und geschlossen haben. Monaco bekommt eine Zone, auf der Start-Ziel-Geraden.
- **Der Grip wurde an echten Kurvengeschwindigkeiten kalibriert.** Über die 18 Strecken sank der Abstand zwischen den Runden des Autopiloten und den schnellsten echten Rennrunden von 17,9 % auf 5,8 %. In Monaco sank die Runde des Autopiloten von 84,2 s auf 74,4 s, gegenüber echten 73,9 s.
- **Enge Kurven wurden aufgeweitet**, auf einen Mindestradius von 15 m, damit die Autos durch Monacos Ste Devote kommen.
- **Jede Strecke hat eine Boxengasse** neben der Start-Ziel-Geraden, mit einem Tempolimit von 80 km/h und einer Box für jedes Auto.

<figure style="margin:2rem 0">
<img src="/agentiloop-racing-monaco.jpg" alt="AgentiLoop Racing: ein Rennen in Monaco." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Monaco, gefahren mit dem KI-Feld.</figcaption>
</figure>

## Rennen gegen die KI

Eine echte Strecke startet als Solo-Zeitfahren; drückt man **O** oder hängt `?race` an die URL, fährt man gegen das Feld. Der Start besteht aus fünf roten Lichtern, eines pro Sekunde, dann einer zufälligen Pause, bevor sie ausgehen. Wer sich vorher mehr als einen halben Meter bewegt, bekommt eine 5-Sekunden-Strafe für einen Frühstart. Solange die Lichter leuchten, setzen einen die Tasten **1–5** in das Auto auf dem jeweiligen Startplatz.

Die KI-Autos folgen der Ideallinie, ziehen sich gegenseitig im Windschatten die Geraden hinunter, scheren aus dem Windschatten aus, nutzen DRS, wenn sie am Messpunkt weniger als eine Sekunde zurückliegen, und stechen beim Bremsen innen hinein. In dem Commit, der das Überholen abgestimmt hat, stieg die Zahl der Überholmanöver in 3-Runden-Rennen auf allen 18 Strecken von 16 auf 34, und die Kontakte sanken von 8 auf null. Ein Auto, das an einer Barriere festhängt, legt den Rückwärtsgang ein, setzt auf einem auf Verkehr und Mauern geprüften Weg zurück und fährt wieder ein.

Es gelten Rennregeln. Jeder, der ins Ziel kommt, muss zwei Reifenmischungen fahren, man muss also einmal stoppen oder wird disqualifiziert. Mit **B** bestellt man bei der Crew Soft, Medium oder Hard. Wer in der Boxengasse zu schnell fährt, bekommt +5 s.

Jede Session beginnt mit Autopilot, das Auto fährt also selbst, bis man übernimmt. Drückt man **P**, berührt das Gamepad oder schaltet einen Gang, gehört es einem.

## Das Auto und das Cockpit

Jedes Auto im Feld verwendet ein RB22-Modell von 2026 von Tyler_Dave (CC BY 4.0, von Sketchfab). Beim Laden lackiert `rb22.mjs` es in den Farben des jeweiligen Autos um und projiziert die Sponsorennamen des Projekts und eine Startnummer darauf. Aus der Nähe wird jedes Teil des Modells unterteilt und geglättet, weiter entfernt kommen Versionen mit weniger Details zum Einsatz.

Mit **C** geht es ins Cockpit. Das Auge des Fahrers sitzt auf der gefederten Karosserie, sodass Rollen, Nicken und Heben die Sicht bewegen, und der Kopf bewegt sich mit den G-Kräften ein wenig mit. Die Spiegel rendern die Szene gespiegelt durch jedes Glas, wobei die eigenen Hinterreifen weggelassen werden, damit man die Strecke und die Autos dahinter sieht.

Auch der Sound wird aus der Physik synthetisiert: ein V6-Zündton, der der Drehzahl folgt, Turbo-Pfeifen, Reifenquietschen aus dem Schlupf und Windgeräusche, die mit der Geschwindigkeit zunehmen.

<figure style="margin:2rem 0">
<img src="/agentiloop-racing-spa.jpg" alt="AgentiLoop Racing: ein Zeitfahren in Spa-Francorchamps." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Das Zeitfahren in Spa.</figcaption>
</figure>

## Ansehen

<figure style="margin:2rem 0">
<div style="position:relative;padding-top:56.25%;border-radius:20px;overflow:hidden">
<iframe src="https://www.youtube-nocookie.com/embed/2RluAIH3iQw?rel=0&amp;modestbranding=1&amp;color=white" title="AgentiLoop Racing — F1 simulator built with AgentiLoop.ai in Three.js" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="position:absolute;inset:0;width:100%;height:100%;border:0"></iframe>
</div>
</figure>

## Ausprobieren

- [Ein Rennen in Monza](https://f1.gokart.games/?track=monza&race)
- [Das Zeitfahren in Spa](https://f1.gokart.games/?track=spa)
- [Ein 5-Runden-Rennen in Spa auf Soft-Reifen](https://f1.gokart.games/?track=spa&race&laps=5&tyre=soft)

Der Quellcode liegt unter [AgentiLoop/F1](https://github.com/AgentiLoop/F1). Er hat keine npm-Abhängigkeiten und keinen Bundler: Three.js ist mit im Repository, daher reicht `python3 -m http.server` im Ordner, um es lokal laufen zu lassen. Die Website selbst ist ein Cloudflare Worker, der das Repository als statische Dateien ausliefert.

*AgentiLoop Racing ist ein unabhängiges Projekt und steht in keiner Verbindung zur Formel 1, zur FIA oder zu einem Team. Die 3D-Modelle behalten ihre eigenen Lizenzen; siehe `models/CREDITS.md` im Repository.*
