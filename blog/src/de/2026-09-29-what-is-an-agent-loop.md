---
title: Was ist ein Agent-Loop? Ein Roboter, ein Sandwich und die Kunst, es noch einmal zu versuchen
description: Schauen, wählen, handeln, prüfen. Ein verspielter, illustrierter Leitfaden zu Agent-Loops – einfach genug für Fünfjährige und mit reichlich Stoff für die Großen.
tags: Erklärt, Agent-Loops
---
<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 360" role="img" aria-labelledby="pip-title pip-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="pip-title">Pip hat ein Ziel, aber noch kein Sandwich</title>
<desc id="pip-desc">Ein freundlicher blauer Roboter betrachtet zwei Scheiben Brot und ein Glas Marmelade. In einer Sprechblase steht: Ein Plan ist kein Sandwich.</desc>
<rect width="760" height="360" rx="20" fill="#eef6ff"/>
<path d="M300 104l-26 24 58-24" fill="#fff"/>
<rect x="265" y="28" width="450" height="76" rx="24" fill="#fff" stroke="#b6c8e4" stroke-width="3"/>
<text x="490" y="75" text-anchor="middle" font-family="system-ui,sans-serif" font-size="27" font-weight="700" fill="#173452">Ein Plan ist kein Sandwich.</text>
<path d="M44 282H716" stroke="#8b684c" stroke-width="13" stroke-linecap="round"/>
<path d="M103 242V276M187 242V276M217 213L260 233" fill="none" stroke="#173452" stroke-width="6" stroke-linecap="round"/>
<rect x="77" y="127" width="140" height="115" rx="27" fill="#559ef5" stroke="#173452" stroke-width="4"/>
<path d="M147 127V100" stroke="#173452" stroke-width="5"/><circle cx="147" cy="91" r="10" fill="#efb943"/>
<circle cx="117" cy="168" r="12" fill="#fff"/><circle cx="177" cy="168" r="12" fill="#fff"/>
<circle cx="120" cy="169" r="5" fill="#173452"/><circle cx="180" cy="169" r="5" fill="#173452"/>
<path d="M121 201Q147 222 173 201" fill="none" stroke="#173452" stroke-width="6" stroke-linecap="round"/>
<g transform="translate(0 12.5)"><path d="M328 260V217Q309 186 349 178Q380 168 402 187Q422 175 445 190Q472 205 449 223V260Z" fill="#fbe3ad" stroke="#ae703f" stroke-width="6"/>
<path d="M353 240V212Q389 190 428 212V240Z" fill="#d94877"/></g>
<path transform="translate(0 9.5)" d="M465 263V225Q449 195 483 187Q517 172 547 191Q578 181 590 211L582 263Z" fill="#fbe3ad" stroke="#ae703f" stroke-width="6"/>
<g transform="translate(0 1)"><rect x="622" y="191" width="60" height="82" rx="12" fill="#d94877" stroke="#173452" stroke-width="3"/>
<rect x="617" y="181" width="70" height="15" rx="5" fill="#173452"/>
<text x="652" y="239" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" font-weight="700" fill="#fff">MARMELADE</text></g>
<text x="147" y="326" text-anchor="middle" font-family="system-ui,sans-serif" font-size="21" fill="#173452">Das ist Pip.</text>
<text x="495" y="326" text-anchor="middle" font-family="system-ui,sans-serif" font-size="21" fill="#173452">Das Ziel: ein Marmeladen-Sandwich.</text>
</svg>
<figcaption>Pip ist unser erfundener Helfer. Beim Zeichnen dieser Illustration wurden keine echten Roboter klebrig gemacht.</figcaption>
</figure>

Stell dir einen kleinen Roboter namens Pip vor.

Du sagst: **„Mach mir bitte ein Marmeladen-Sandwich.“**

Pip schaut auf den Tisch. Da ist Brot. Da ist Marmelade. Da ist ein Löffel mit einer verdächtig großen Menge Erdnussbutter.

Verkündet Pip jetzt: „Sandwich fertig!“?

Nein. Das wäre eine Rede, kein Sandwich.

Pip muss **schauen, einen kleinen Schritt wählen, ihn ausführen und prüfen, was passiert ist**. Dann kann Pip entscheiden, was als Nächstes kommt.

Dieses sich wiederholende Muster ist ein **Agent-Loop**.

## Die ganze Idee in vier kleinen Wörtern

**Schauen. Wählen. Handeln. Prüfen.**

- **Schauen:** Was passiert gerade?
- **Wählen:** Was ist eine sinnvolle nächste Sache?
- **Handeln:** Genau diese Sache tun.
- **Prüfen:** Was ist tatsächlich passiert? Sind wir fertig?

Ist die Aufgabe nicht erledigt, geht es noch eine Runde weiter – mit den neuen Informationen.

Ein **Loop** (eine Schleife) bedeutet einfach, dass sich etwas wiederholt. Ein **Agent** ist ein System, das mit den Werkzeugen und Berechtigungen, die man ihm gegeben hat, Schritte in Richtung eines Ziels unternehmen kann.

Zusammen ergibt das: **Ein Agent-Loop lässt einen Helfer handeln, das Ergebnis sehen und entscheiden, was als Nächstes kommt.**

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 520" role="img" aria-labelledby="loop-title loop-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="loop-title">Schauen, wählen, handeln, prüfen – und wissen, wann Schluss ist</title>
<desc id="loop-desc">Ein Flussdiagramm läuft im Uhrzeigersinn von Schauen über Wählen und Handeln zu Prüfen. Von Prüfen geht es zurück zu Schauen, wenn noch Arbeit ansteht. Ein separater Pfeil führt von Prüfen zu Aufhören oder fragen, wenn die Aufgabe erledigt oder blockiert oder das Budget aufgebraucht ist.</desc>
<defs><marker id="loop-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0L10 5 0 10Z" fill="#4b617e"/></marker></defs>
<rect width="760" height="520" rx="20" fill="#f0f5fb"/>
<g fill="none" stroke="#4b617e" stroke-width="4" marker-end="url(#loop-arrow)"><path d="M298 100H460"/><path d="M586 150V238"/><path d="M464 290H302"/><path d="M176 240V153"/><path d="M176 342V414"/></g>
<g stroke-width="3"><rect x="54" y="48" width="244" height="100" rx="23" fill="#d7eaff" stroke="#3377b9"/><rect x="464" y="48" width="244" height="100" rx="23" fill="#fce9b6" stroke="#9a701b"/><rect x="464" y="242" width="244" height="100" rx="23" fill="#dfd9ff" stroke="#7760b5"/><rect x="54" y="242" width="244" height="100" rx="23" fill="#cff3e4" stroke="#29836a"/><rect x="54" y="419" width="652" height="68" rx="20" fill="#fff" stroke="#4b617e"/></g>
<g font-family="system-ui,sans-serif" text-anchor="middle" fill="#173452"><g font-size="28" font-weight="700"><text x="176" y="90">1. SCHAUEN</text><text x="586" y="90">2. WÄHLEN</text><text x="586" y="285">3. HANDELN</text><text x="176" y="285">4. PRÜFEN</text></g><g font-size="20"><text x="176" y="122">Was sehe ich?</text><text x="586" y="122">Was als Nächstes?</text><text x="586" y="317">Ein Werkzeug nutzen.</text><text x="176" y="317" font-size="19">Was hat sich geändert?</text><text x="380" y="199">Noch was zu tun? Nächste Runde.</text><text x="428" y="389">Fertig, blockiert oder am Limit?</text><text x="380" y="461" font-size="24" font-weight="700">STOPP – oder einen Menschen fragen.</text></g></g>
</svg>
<figcaption>Ein Lehrdiagramm, kein vorgeschriebenes Software-Design. Echte Implementierungen können diese Phasen zusammenfassen. Entscheidend ist, dass das Ergebnis in die nächste Entscheidung einfließt.</figcaption>
</figure>

## Zurück zur hochernsten Sandwich-Mission

Pips erster kleiner Schritt: das Marmeladenglas öffnen.

**Handeln:** Den Deckel drehen.

**Prüfen:** Der Deckel hat sich nicht bewegt.

Jetzt wird es spannend. Pip sollte nicht so tun, als wäre das Glas offen, nur weil das Öffnen der Plan war.

Und Pip sollte auch nicht ewig weiterdrehen, bis die Sonne zur Rosine geworden ist.

Pip könnte eine erlaubte Alternative versuchen oder sagen: „Kannst du mir mit dem Deckel helfen?“ Um Hilfe zu bitten ist ein nützliches Ergebnis – kein Scheitern in Robotergröße.

Sobald das Glas offen ist, kann Pip die Marmelade verstreichen, das Brot zusammenlegen und das Ergebnis mit deiner Bitte abgleichen.

Zwei Scheiben? Marmelade dazwischen? Auf einem Teller? Super.

Ein Glas, das auf einem Brotlaib balanciert? Kreativ. Aber kein Sandwich.

## Wo kommt die KI ins Spiel?

Unsere Küchengeschichte ist nur ausgedacht. Statt mit Brot zu hantieren, könnten die Werkzeuge eines Software-Agenten eine Datei lesen, eine Seite durchsuchen, ein Dokument bearbeiten oder einen Test ausführen.

In einem KI-Agenten kann ein Sprachmodell dabei helfen, den nächsten Schritt zu wählen. Die umgebende Software führt die erlaubten Werkzeugaufrufe aus und liefert deren Ergebnisse zurück. Dann ist das Modell mit diesen Informationen wieder am Zug.

Denk an drei verschiedene Aufgaben:

| Teil | Pips ausgedachte Küche | Software-Version |
| --- | --- | --- |
| Ziel | Ein Marmeladen-Sandwich machen | Einen kaputten Link reparieren |
| Entscheider | Den nächsten kleinen Schritt wählen | Das Modell schlägt eine Aktion vor |
| Werkzeug | Hände und Löffel | Dateileser, Editor oder Browser |
| Beobachtung | Der Deckel ist immer noch zu | Das Werkzeug liefert einen Fehler oder ein Ergebnis |
| Arbeitsnotizen | Glas offen; Brot bereit | Relevanter Aufgabenverlauf und Ergebnisse |
| Abschlussprüfung | Das gewünschte Sandwich ist fertig | Prüfen, ob der gewünschte Link funktioniert |

**Dass ein Modell eine Aktion vorschlägt, heißt nicht, dass diese Aktion auch passiert.** Und dass eine Aktion passiert, heißt nicht automatisch, dass das Ziel erreicht ist.

„Datei gespeichert“ und „die richtige Datei mit dem richtigen Inhalt gespeichert“ sind zwei verschiedene Aussagen. Bei der Prüfung zeigt sich, worin der Unterschied liegt.

## Ein kleines Abenteuer: das verschwundene Bild

Angenommen, du bittest einen Software-Helfer, ein fehlendes Bild auf einer Webseite zu reparieren.

Ein sinnvoller Loop könnte so aussehen:

1. **Schauen:** Die Seite lesen und den Bildpfad ermitteln.
2. **Wählen:** Prüfen, ob das referenzierte Bild existiert.
3. **Handeln:** Die relevanten Dateien untersuchen.
4. **Prüfen:** Die Seite fordert `cat.png` an, die Datei heißt aber `cat.jpg`.
5. **Nächste Runde:** Die Referenz anpassen und dann prüfen, ob die Seite das richtige Bild lädt.
6. **Aufhören:** Die Änderung und die tatsächlich durchgeführten Prüfungen melden.

Wenn das Bild immer noch nicht erscheint, reicht „Ich habe die Seite bearbeitet“ nicht. Das Ergebnis sollte den nächsten Schritt bestimmen.

Achte darauf, was das Ganze zu einem Loop macht: **Die nächste Aktion hängt davon ab, was die vorherige ans Licht gebracht hat.** Es geht nicht bloß darum, immer wieder dasselbe zu tun.

## Wird es mit jeder Runde besser?

Nein. Mehr Aktivität bedeutet nicht automatisch mehr Fortschritt.

Hier ist ein ausgedachtes Diagramm für Pips Sandwich-Mission. Pip bekommt einen Punkt für jeden erreichten Meilenstein: Glas offen, Marmelade verstrichen, Sandwich zusammengesetzt und die ursprüngliche Bitte geprüft.

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 450" role="img" aria-labelledby="graph-title graph-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="graph-title">Ein ausgedachtes Sandwich-Fortschrittsdiagramm</title>
<desc id="graph-desc">Über sechs Versuche hinweg liegen die erreichten Meilensteine bei null, null, eins, zwei, drei und vier. Die ersten beiden Versuche bringen keinen Fortschritt, weil das Glas klemmt. Diese erfundenen Zahlen veranschaulichen Feedback, keine gemessene Agent-Leistung.</desc>
<rect width="760" height="450" rx="20" fill="#f0f5fb"/>
<g font-family="system-ui,sans-serif" fill="#173452"><text x="48" y="42" font-size="23" font-weight="700">Fortschritt ist nicht dasselbe wie Beschäftigung.</text><text x="48" y="73" font-size="18">Erreichte Meilensteine · erfundenes Beispiel, kein Benchmark</text></g>
<g stroke="#c2cedd" stroke-width="1"><path d="M95 335H690M95 280H690M95 225H690M95 170H690M95 115H690"/></g>
<path d="M95 105V345H700" fill="none" stroke="#4b617e" stroke-width="3"/>
<polyline points="115,335 225,335 335,280 445,225 555,170 665,115" fill="none" stroke="#227657" stroke-width="5" stroke-linejoin="round"/>
<g fill="#227657" stroke="#fff" stroke-width="3"><circle cx="115" cy="335" r="8"/><circle cx="225" cy="335" r="8"/><circle cx="335" cy="280" r="8"/><circle cx="445" cy="225" r="8"/><circle cx="555" cy="170" r="8"/><circle cx="665" cy="115" r="8"/></g>
<g font-family="system-ui,sans-serif" font-size="20" fill="#173452" text-anchor="middle"><text x="68" y="341">0</text><text x="68" y="286">1</text><text x="68" y="231">2</text><text x="68" y="176">3</text><text x="68" y="121">4</text><text x="115" y="375">1</text><text x="225" y="375">2</text><text x="335" y="375">3</text><text x="445" y="375">4</text><text x="555" y="375">5</text><text x="665" y="375">6</text><text x="390" y="418">Versuche</text></g>
<g font-family="system-ui,sans-serif" font-size="19" fill="#173452"><text x="116" y="292">Deckel klemmt!</text><text x="326" y="317">Hilfe hat geklappt.</text><text x="586" y="99">Geprüft!</text></g>
</svg>
<figcaption>Erfundene Daten: 0, 0, 1, 2, 3, 4 erreichte Meilensteine. Echte Arbeit kann ins Stocken geraten, Rückschritte machen oder sich mit den verfügbaren Werkzeugen als unmöglich erweisen.</figcaption>
</figure>

Das flache Stück ist wichtig. Wenn sich nichts ändert, muss der Helfer das bemerken – statt zu feiern, wie oft er es schon versucht hat.

Für die Großen ergeben sich daraus nützliche Fragen: Haben wir etwas gelernt? Hat sich der Zustand geändert? Wiederholen wir dieselbe gescheiterte Aktion? Ist ein weiterer Versuch seinen Preis wert?

Für alle anderen: **Wenn an der Tür ZIEHEN steht, ist fester drücken keine Strategie.**

## Gib dem Helfer einen Zaun, nicht den ganzen Planeten

Ein vernünftiges Agent-Design braucht mehr als einen Wiederholen-Knopf.

- **Eine klare Ziellinie.** „Finde drei Pinguinbilder“ lässt sich leichter prüfen als „Mach alles großartig“.
- **Passende Berechtigungen.** Eine E-Mail entwerfen zu dürfen, sollte nicht automatisch heißen, sie auch senden zu dürfen.
- **Ein Budget fürs Aufhören.** Begrenze Versuche, Zeit oder Ausgaben. Eine festgefahrene Aufgabe darf keine endlose Aufgabe werden.
- **Eine Möglichkeit zu fragen.** Fehlende Informationen, fehlender Zugriff oder eine folgenreiche Entscheidung können einen Menschen erfordern.
- **Ehrliche Prüfungen.** Nutze Belege, die zum Ziel passen. Mach aus „Das Werkzeug hat geantwortet“ nicht „Alles ist korrekt“.

Das sind Designprinzipien, kein Versprechen, dass jedes Produkt sie umsetzt. Ein Loop macht ein System nicht auf magische Weise sicher oder zuverlässig.

In Pips Küche heißt das: das Sandwich machen, keinen Lastwagen voller Marmelade bestellen und fragen, bevor die Geräte der Großen benutzt werden.

## Ist ein Agent-Loop dasselbe wie ein Skript?

Nicht unbedingt – aber die Grenze verläuft nicht bei „Skripte sind dumm, Agenten sind schlau“. Auch Skripte können Schleifen, Bedingungen und hervorragende Prüfungen haben.

Der Unterschied, auf den es ankommt, ist, **wie die nächste Aktion gewählt wird**. In einem festen Workflow hat die Entwicklerin oder der Entwickler die Wege im Voraus festgelegt. In einem modellgesteuerten Agent-Loop kann das Modell anhand der Aufgabe und der neuesten Beobachtungen unter den verfügbaren Aktionen wählen. Echte Systeme können beide Ansätze mischen.

Für eine vorhersehbare Aufgabe kann ein kleines Skript genau das Richtige sein. Man braucht keinen philosophierenden Roboter, um mittags eine Glocke zu läuten.

Für eine Aufgabe mit unbekannten Hindernissen kann es nützlich sein, den nächsten Schritt anhand frischer Belege zu wählen. Genau diese Flexibilität macht Grenzen und Überprüfung aber auch so wichtig.

## Die Version für den Kühlschrankmagneten

Ein Agent-Loop heißt:

> Probier einen sinnvollen Schritt. Schau, was passiert ist. Nutze, was du gelernt hast. Wiederhole das nur, solange es Sinn ergibt.

Es ist keine Magie. Es ist keine Garantie. Es ist nicht „einfach ewig weitermachen“.

Es ist eine Art, **ein Ziel, eine Aktion und das echte Ergebnis** miteinander zu verbinden – immer wieder, bis der Helfer fertig ist oder aufhören muss.

Pip würde es einfacher erklären:

**„Schauen. Probieren. Prüfen. Und nicht Sandwich sagen, bevor da ein Sandwich ist.“**
