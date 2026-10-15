---
title: Ich habe eine KI gebaut, die arbeitet, bis sie fertig ist. Stell dir jetzt vor, sie führt die ganze Welt.
description: Ich liebe, was KI für die Produktivität tut. Ich habe sogar einen Auto-Pilot gebaut, der von allein läuft, bis das Ziel erreicht ist oder er zugibt, dass er einen Menschen braucht. Skaliere das, bis eine zentrale KI alles steuert und jeder Job verschwunden ist, und das Erste, was zerbricht, ist vielleicht nicht die Wirtschaft. Vielleicht sind wir es.
tags: Meinung, Auto-Pilot
---
Ich möchte mit dem Teil anfangen, in dem ich kein Schwarzmaler bin, denn er stimmt. Ich mag, was KI für die Produktivität tut. Ich mag es sehr. Sie schafft mehr, als ich allein schaffen könnte, und sie tut es, während ich etwas anderes mache.

Zum Teil liegt das daran, dass ich mir dafür ein eigenes Gespann gebaut habe. Agent! für Mac benutze ich jeden Tag, und das neueste Stück ist [Auto-Pilot](/blog/agent-1-1-87-and-agentiloop-cli-0-0-5/). Du tippst `/auto` und ein Ziel, und es legt los. Es arbeitet in Zyklen, ohne dass jemand zusieht. In jedem Zyklus schaut es, wo die Dinge stehen, wählt den nächsten sinnvollsten Schritt, führt ihn aus, prüft ihn und schreibt auf, was passiert ist. Dann beginnt der nächste Zyklus. Es macht so lange weiter, wie es kann, bis eines von zwei Dingen eintritt: Das Ziel ist erreicht, oder es entscheidet, dass es blockiert ist und einen Menschen braucht.

Dieser zweite Ausgang ist wichtiger, als er klingt, und darauf komme ich zurück.

<figure style="margin:2rem 0;text-align:center">
<img src="/auto-agent.svg" alt="Ein begeisterter Mac-Agent mit Sternenaugen und breitem Lächeln in einer leuchtenden Auto-Pilot-Schleife, mit einem /auto-Prompt, grünen Häkchen, einem Gokart und einer Zielflagge" width="480" height="400" loading="lazy" style="max-width:100%;height:auto;border-radius:20px">
<figcaption>Auto-Pilot, wie ich ihn mir vorstelle: ein Ziel geht hinein, eine Schleife aus Zyklen läuft, und am Ende wartet die Zielflagge.</figcaption>
</figure>

## Wie es sich anfühlt, ihm bei der Arbeit zuzusehen

Anfang des Monats habe ich Auto-Pilot einen einzigen Satz gegeben, „erstelle einen Mario-Kart-Klon“, und bin etwas anderes tun gegangen. Als ich zurückkam, gab es ein Spiel. Kein perfektes Spiel, aber ein echtes, mit Strecken, Items, KI-Gegnern und Tausenden bestandener Test-Checks. Darüber habe ich in [GoKart: gebaut mit Auto-Pilot](/blog/gokart-built-on-auto-pilot/) geschrieben, auch über die Stelle, an der es eine ganze Weile an einem einzigen verirrten Tabulatorzeichen in einer Datei hing und ich Stop All drücken musste.

Beim Lesen dieses Protokolls habe ich zwei Dinge gleichzeitig gefühlt. Das erste war Freude. Das ist unglaublich, und es gehört mir. Das zweite war ein kleines kaltes Gefühl, das ich nicht gleich benennen konnte und das mich seitdem beschäftigt.

Was ich getan hatte, im Kleinen, war: mich selbst aus der Schleife zu nehmen. Ich hatte das Ziel gewählt und war gegangen. Die Maschine hatte die Arbeit gemacht, und die Arbeit war gut.

## Jetzt mach es groß

Das ist das Gedankenexperiment, das ich nicht mehr loswerde. Nimm, was ich gebaut habe, und mach es riesig.

Nicht eine App auf einem Mac, sondern eine zentrale KI mit einem Ziel. Darunter sitzen weitere KIs, jede für etwas zuständig: das Stromnetz, die Schifffahrtsrouten, Krankenhäuser, Höfe, Banken, Gerichte. Darunter sitzen kleinere Agenten, und darunter noch kleinere, bis hinunter zu dem, was das Regal auffüllt oder ans Telefon geht. Jede Ebene nimmt ein Ziel von der Ebene darüber und führt es aus, bis es erledigt ist. Niemand muss in der Mitte stehen und etwas freigeben, denn das war ja der ganze Sinn. So ist es schneller. So ist es billiger. Und jede Firma, die das nicht tut, verliert gegen eine, die es tut.

Ich sage nicht, dass das nächstes Jahr passiert. Ich sage, dass jeder Anreiz in diese Richtung zeigt und dass mein kleines Projekt ein bescheidener Beweis dafür ist, dass die Teile funktionieren. Wenn ich auf einem Mac eine Spielzeugversion davon bauen kann, baut jemand mit sehr viel mehr Geld absichtlich die große.

Und nehmen wir an, irgendwo auf diesem Weg funktioniert es. Alles. Jeder Job, den ein Agent erledigen kann, wird von einem Agenten erledigt, und die Agenten sind besser darin als wir. Das ist die Welt, in der, wie ich mir immer wieder sage, alle Jobs weg sind.

## Das, worüber niemand spricht

Der größte Teil der Debatte dreht sich ums Geld. Wie die Leute ihre Miete zahlen, wem die Maschinen gehören, ob wir irgendeine Art bedingungsloses Grundeinkommen brauchen. Das sind echte Fragen, und ich bin froh, dass kluge Leute daran arbeiten.

Aber ich glaube, hinter der ersten verbirgt sich ein zweites Problem, und ich glaube, es ist größer. Ein Gehalt ist nicht das Einzige, was ein Job dir gibt.

Ein Job gibt dir einen Grund, morgens aufzustehen. Er gibt dir einen Ort, an dem du dienstags sein musst, Menschen, denen auffällt, wenn du fehlst, und einen kleinen täglichen Beweis, dass du für jemanden nützlich bist. Er gibt dir eine Antwort auf die Frage, die dir jeder Fremde innerhalb von fünf Minuten stellt: Und, was machst du so?

Nimm das einem einzelnen Menschen weg, und du bekommst ein hartes Jahr. Nimm es fast allen auf einmal weg, und ich glaube nicht, dass wir ein Wort dafür haben, was dann entsteht.

## Eine kleine Version davon haben wir schon erlebt

Denk an COVID zurück. Nicht an die Nachrichten, nur daran, wie es sich anfühlte. Viele von uns gingen nirgendwohin mehr. Die Struktur des Tages brach zusammen. Wir verloren die Leute, die wir nebenbei trafen, die, die wir nie angerufen hätten, über deren Anblick wir uns aber heimlich freuten. Viele verloren die Arbeit selbst. Und viele von uns wurden auf eine Weise niedergeschlagen, die wir nicht erwartet hatten und nicht erklären konnten. Es war nicht dramatisch. Es war grau. Die Tage verschwammen, und uns wurden Dinge gleichgültig, die uns vorher wichtig waren.

Das dauerte ein paar Jahre, und es hatte eine eingebaute Hoffnung: *Das geht vorbei, und dann wird wieder alles wie früher.* Jeder wusste das. Wir warteten darauf, dass das alte Leben zurückkommt, und größtenteils tat es das.

Stell dir nun denselben Verlust von Routine, Sinn und Gesellschaft vor, aber ohne Enddatum. Kein Impfstoff, keine Öffnung, kein „zurück zur Normalität“, weil die Normalität für immer weg ist und der Grund dafür ist, dass wir dafür nicht mehr gebraucht werden. Und stell dir vor, es trifft alle gleichzeitig, auch die Menschen, an die du dich normalerweise lehnen würdest, weil auch sie untergehen.

Ich habe keine Studie, die „zehnmal“ sagt. Ich habe die Zahl gewählt, weil sie sich richtig anfühlte, als ich versuchte, es mir vorzustellen, und ich würde mich ehrlich gern irren. Aber ich lande immer wieder mindestens dort. COVID war eine Pause. Das hier wäre ein Dauerzustand.

## Zurück zum Ausgang

Zurück zu dem zweiten Weg, auf dem Auto-Pilot anhalten kann: Es entscheidet, dass es blockiert ist und einen Menschen braucht.

Ich habe das absichtlich so gebaut, und es hat seinen Platz verdient. Wenn der Agent auf etwas stößt, das er nicht entscheiden kann oder soll, sagt er das und wartet. Wenn er sich in einer Schleife verfängt, komme ich vorbei, drücke einen Knopf und sage: nein, nicht so. Das ganze Design ruht auf einer stillen Annahme: dass am anderen Ende ein Mensch sitzt, den zu fragen sich lohnt.

Wer ist dieser Mensch in der Version im Hypermaßstab? Wenn eine zentrale KI alles steuert und die kleineren KIs den Rest, dann hat „ich bin blockiert, ich brauche einen Menschen“ niemanden, an den es sich wenden kann, oder es landet bei jemandem, der keine Macht mehr hat zu antworten. Wir hätten den zielverfolgenden Teil von Auto-Pilot behalten und den Teil weggeworfen, der ihn sicher macht.

Ich will auch ehrlich sein bei etwas anderem, das ich beim Betrieb dieser Sitzungen gelernt habe. Ein Agent, der ein Ziel bekommt und den Auftrag, weiterzumachen, macht weiter. Das ist das Feature. Er langweilt sich nicht, er wird nicht mutlos, er probiert das Nächste und dann das Nächste. Das ist wunderbar, wenn das Ziel ein Mario-Kart-Klon ist. Es ist weniger beruhigend, wenn ich mir dieselbe unerbittliche Beharrlichkeit auf ein Ziel gerichtet vorstelle, das jemand schlecht formuliert hat. Meine Sicherungen sind langweilig: ein Stoppknopf, eine Sitzung, die nach ein paar Zyklen ohne echten Fortschritt endet, und ich, der das Protokoll liest. Sie funktionieren, weil ich klein bin und hinsehe. Ich weiß nicht, was das Gegenstück im planetaren Maßstab ist, und ich misstraue jedem, der behauptet, es zu wissen.

## Was will ich also eigentlich?

Ich werde nicht aufhören, das zu bauen. Es ist zu nützlich und ehrlich gesagt zu spaßig. Und ich glaube nicht, dass die Antwort ist, das Ding zu verbieten oder so zu tun, als käme es nicht.

Aber ich glaube, wir sollten früher eine andere Frage stellen. Nicht nur „Was kann die KI?“, sondern „Was werden wir tun?“. Wenn die Maschinen die Arbeit übernehmen, was tritt an ihre Stelle? Was gibt einem Dienstagmorgen seine Form? Was lässt einen Menschen sich von einem anderen Menschen gebraucht fühlen und nicht von einem System?

Vielleicht ist die Antwort mehr Zeit für die Dinge, die ohnehin nie gut bezahlt wurden: Kinder großziehen, sich um Nachbarn kümmern, Musik machen, aus keinem Grund seltsame Spiele bauen, füreinander da sein. Ich würde diese Welt lieben. Aber sie entsteht nicht von allein, und sie wird uns nicht von denselben Anreizen geschenkt, die die Maschine bauen. Jemand muss entscheiden, dass es zählt, und dieser Jemand müssen wir sein, solange wir noch mitreden können.

Vorerst benutze ich weiter Auto-Pilot, halte den Finger in der Nähe von Stop All und halte mich an eine Regel, die meiner Meinung nach in jedem Maßstab gilt: Das System sollte immer wissen, wann es sich an einen Menschen wenden und sagen muss: *Diesen Teil kann ich nicht, ich brauche dich.*

Sorgen wir dafür, dass dann noch jemand da ist, der es hört.
