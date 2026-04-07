---
title: Warum wir den Coding-Modus rausgeworfen haben: Das Modell soll seine Werkzeuge selbst wählen
description: Agent! hat früher geraten, ob du programmieren oder automatisieren willst, und passend dazu Werkzeuge ausgeblendet. Eine gescheiterte Photo-Booth-Aufgabe hat gezeigt, warum das Harness aufhören sollte, das Modell zu bevormunden.
tags: Architektur, Design
---
Frühe Versionen von Agent! hatten **Modi**: Coding, Automatisierung und Standard. Die Idee klang vernünftig. Eine Programmieraufgabe braucht das Bedienungshilfen-Werkzeug nicht, und eine Aufgabe wie „Klick auf diesen Button“ braucht kein Xcode. Blendet man aus, was nicht relevant ist, sieht das Modell eine kürzere Werkzeugliste, verbraucht weniger Tokens und trifft seltener die falsche Wahl.

Am 7. April 2026 hat der Commit `7ea44c0d` das gesamte System gelöscht. Hier ist der Bug, der dazu geführt hat, und das Prinzip, das davon geblieben ist.

## Wie die Modi funktionierten

Im zweiten Durchgang einer Aufgabe prüfte das Harness, worum du gebeten hattest, und glich es mit zwei Schlüsselwortlisten ab. Wörter wie `build`, `compile`, `edit`, `fix` und `refactor` bedeuteten Coding. Wörter wie `click`, `button`, `window`, `photo` und `accessibility` bedeuteten Automatisierung. Dann setzte es ein Flag, `codingModeEnabled` oder `automationModeEnabled`, und beschränkte die für das Modell sichtbaren Werkzeuge auf die Gruppen dieses Modus. Das Modell konnte den Modus auch selbst über ein `mode`-Werkzeug wechseln.

## Der Bug: Photo Booth im Coding-Modus

Die Meldung lautete schlicht: „Bedienungshilfen sind kaputt.“ Die Ursache, in den Worten der Commit-Nachricht: Der automatische Wechsel stufte `open -a Photo Booth` als unbekanntes Signal ein und **fiel standardmäßig auf den Coding-Modus zurück**. Der Coding-Modus schloss die Auto-Gruppe aus, und genau in der Auto-Gruppe liegt das `accessibility`-Werkzeug.

Das Modell sollte also ein Foto aufnehmen, und das einzige Werkzeug, das zum Drücken des Auslösers gebaut war, war mitten in der Aufgabe verschwunden. Es tat, was ein fähiges Modell mit den verbliebenen Werkzeugen tut: Es wich auf `osascript` über die Shell aus, das immer wieder mit *„Symbolleiste 1 von Fenster 1 kann nicht abgerufen werden.“* scheiterte.

Mit dem Modell war alles in Ordnung, und mit dem Bedienungshilfen-Werkzeug auch. Das Harness hatte die Absicht falsch erraten und die richtige Antwort stillschweigend entfernt.

## Die Lösung, die keine war

Der naheliegende Patch wäre gewesen, `open -a` zu den Automatisierungs-Schlüsselwörtern hinzuzufügen. Die Commit-Nachricht spricht das direkt an: Das wäre „ein weiteres Pflaster in einer langen Reihe“ gewesen. Absichtserkennung per Schlüsselwort ist ein aussichtsloses Spiel. Jede neue App, jede Formulierung und jede Sprache reißt ein weiteres Loch, und jeder Fehlgriff scheitert auf die verwirrendste Weise: mit einem Modell, das plötzlich etwas nicht mehr kann, was es einen Durchgang vorher noch konnte.

## Was an seine Stelle trat: nichts

Das gesamte Modussystem flog raus: 13 Dateien, 141 Zeilen gelöscht und 39 hinzugefügt. Dazu gehörten:

- die Flags `codingModeEnabled` und `automationModeEnabled` samt ihren Werkzeuggruppen-Listen
- der automatische Wechsel im zweiten Durchgang, sowohl in der Haupt-Aufgabenschleife als auch in Tab-Aufgaben
- `predictToolGroups()`, die Funktion, die Werkzeuggruppen aus deinem Prompt erriet
- die Einschränkung der Werkzeugliste für lokale Endpunkte in den Claude- und OpenAI-kompatiblen Diensten
- die Aliase `coding` und `automation` für Sub-Agenten (stattdessen übergibst du echte Gruppennamen)

Werkzeuge werden jetzt **ausschließlich durch deine eigenen Schalter** in den Einstellungen gefiltert (`ToolPreferencesService`). Jedes Werkzeug, das du aktiviert hast, steht in jedem Durchgang zur Verfügung, und das Modell wählt, was es braucht.

Zwei kleine Details zeigen, mit wie viel Sorgfalt eine solche Löschung verbunden ist. Das `mode`-Werkzeug wurde nicht komplett entfernt. Es wurde zu einer Operation ohne Wirkung, die mit *„Der Moduswechsel wurde entfernt“* antwortet, denn ein Modell mit einer alten Unterhaltung im Kontext könnte es noch aufrufen, und eine klare Antwort ist besser als ein Fehler wegen eines unbekannten Werkzeugs. Außerdem stieg die Revision des System-Prompts von 71 auf 72, sodass jeder auf der Festplatte gespeicherte Prompt, der Modi erwähnte, neu synchronisiert wird.

## Das Ergebnis

Kein Log-Spam mehr mit *„Coding-Modus automatisch aktiviert“*. Keine Werkzeuge mehr, die mitten in der Aufgabe verschwinden. Keine Werkzeugliste mehr, die von einem Durchgang zum nächsten hin- und herspringt.

## Das Prinzip

Diese Entscheidung hat vieles von dem geprägt, was danach kam, deshalb lohnt es sich, sie klar zu formulieren:

> Das Harness sollte **Sicherheit** durchsetzen, nicht **Absichten** erraten.

Agent! ist dort streng, wo Strenge objektiv ist. Es verweigert katastrophale Shell-Befehle, Änderungen an Dateien, die das Modell nicht gelesen hat, und ein „Fertig“ ohne Nachweis. Das sind Fakten, die es überprüfen kann. Welches Werkzeug eine Aufgabe braucht, ist eine Ermessensfrage, und darin ist das Modell besser als eine Schlüsselwortliste. Wenn das Harness das Modell in einer Ermessensfrage überstimmt, scheitert es still und verwirrend. Wenn es eine überprüfbare Regel durchsetzt, scheitert es laut und mit Begründung.

Wenn du einen Agenten baust, ist es verlockend, dem Modell zu „helfen“, indem du seine Auswahl beschneidest. Miss zuerst. Eine etwas längere Werkzeugliste kostet ein paar Tokens. Ein fehlendes Werkzeug kann dich die ganze Aufgabe kosten.
