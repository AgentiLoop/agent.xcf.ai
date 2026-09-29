---
title: Ein Release am Ersten jedes Monats, dazwischen Pre-Releases
description: Agent! erscheint jetzt am 1. jedes Monats als stabiles Release. In täglichen Pre-Releases (bald wöchentlich) werden neue Features und Fixes erprobt, und Release Candidates machen vor dem großen Tag alles fest.
tags: Versionshinweise, Hinter den Kulissen
---
Agent! hat einen neuen Rhythmus. Ab dem **1. Oktober 2026** gibt es am **1. jedes Monats** ein stabiles Release. Dazwischen gibt es Pre-Releases: derzeit etwa eines pro Tag, und wir wollen das auf eines pro Woche verlangsamen. Irgendwann im letzten Abschnitt jedes Monats werden die Pre-Releases zu **Release Candidates**, und der beste Kandidat wird zum Release am 1.

Das ist der ganze Plan. Der Rest dieses Beitrags erzählt, wie es dazu kam, mit ein paar Diagrammen aus unserer eigenen Git-Historie.

## Wo wir herkommen

Agent! 1.0.0 wurde am **13. März 2026** getaggt. Seitdem hat das Repository **188 Versions-Tags** gesammelt. Gleichmäßig verteilt waren sie nicht.

<figure class="chart"><div class="chart-title">Versions-Tags pro Monat, 2026</div><div class="bars"><div class="lbl">Mär</div><div><div class="bar" style="--w:0.738"><span>57</span></div></div><div class="lbl">Apr</div><div><div class="bar" style="--w:0.880"><span>68</span></div></div><div class="lbl">Mai</div><div><div class="bar dim" style="width:3.9%"><span>3</span></div></div><div class="lbl">Jun</div><div><div class="bar dim" style="width:3.9%"><span>3</span></div></div><div class="lbl">Jul</div><div><div class="bar dim" style="width:1.3%"><span>1</span></div></div><div class="lbl">Aug</div><div><div class="bar" style="--w:0.194"><span>15</span></div></div><div class="lbl">Sep</div><div><div class="bar" style="--w:0.531"><span>41</span></div></div></div><figcaption>188 Tags seit 1.0.0 am 13. März. Ein arbeitsreicher Frühling, ein ruhiger Sommer und ein Comeback im September. Quelle: <code>git for-each-ref refs/tags</code>.</figcaption></figure>

März und April waren ein Sprint: 125 Tags in zwei Monaten, manchmal mehrere pro Tag. Dann kam der Sommer. Mai, Juni und Juli brachten zusammen sieben Tags. Ende August zog das Tempo wieder an, und der September hat bisher 41 Tags.

Die stabilen Releases nahmen denselben holprigen Weg. Die Releases-Seite listet vier davon: **1.0.80.170** am 25. April, **1.0.88.182** am 3. Juni, **1.0.89.183** am 26. Juli und **1.1.33.233** am 12. September, das 600-Sterne-Release.

<figure class="chart"><div class="chart-title">Tage zwischen stabilen Releases</div><div class="bars"><div class="lbl">1.0.88</div><div><div class="bar" style="--w:0.648"><span>39 Tage · 25. Apr → 3. Jun</span></div></div><div class="lbl">1.0.89</div><div><div class="bar" style="--w:0.880"><span>53 Tage · 3. Jun → 26. Jul</span></div></div><div class="lbl">1.1.33</div><div><div class="bar" style="--w:0.797"><span>48 Tage · 26. Jul → 12. Sep</span></div></div><div class="lbl">1. Okt</div><div><div class="bar next" style="--w:0.315"><span>19 Tage · 12. Sep → 1. Okt</span></div></div></div><figcaption>Jedes stabile Release auf GitHub, gemessen am vorherigen. Der gestreifte Balken ist das Release vom 1. Oktober, das bereits im Kalender steht. Ab dann beträgt der Abstand einen Monat, jeden Monat.</figcaption></figure>

Abstände von 39, 53 und 48 Tagen sind nicht schlecht, aber man konnte die Uhr nicht danach stellen. Wer wissen wollte, wann das nächste Agent! kommt, bekam ehrlicherweise die Antwort „wenn es fertig ist“. Wir mögen fertig. Wir mögen es aber auch, zu wissen, wann.

## Der Weg zum 1. Oktober

Der neue Zyklus hatte bereits seine Generalprobe. Nachdem 1.1.33 erschienen war, ging es auf `main` weiter. Von v1.1.37.237 am 13. September bis v1.1.77.277 am 28. September war jeder getaggte Build ein Pre-Release, und an den meisten Tagen gab es mindestens einen.

<figure class="chart"><div class="chart-title">Tags pro Tag, 13.–28. September</div><div class="cols"><div style="height:10.6%"><span>1</span></div><div style="height:10.6%"><span>1</span></div><div style="height:10.6%"><span>1</span></div><div style="height:42.5%"><span>4</span></div><div style="height:0.0%"><span></span></div><div style="height:53.1%"><span>5</span></div><div style="height:10.6%"><span>1</span></div><div style="height:10.6%"><span>1</span></div><div style="height:31.9%"><span>3</span></div><div style="height:21.2%"><span>2</span></div><div style="height:10.6%"><span>1</span></div><div style="height:21.2%"><span>2</span></div><div style="height:85.0%"><span>8</span></div><div class="rc" style="height:42.5%"><span>4</span></div><div class="rc" style="height:42.5%"><span>4</span></div><div class="rc" style="height:10.6%"><span>1</span></div></div><div class="cols-x"><span>13</span><span>14</span><span>15</span><span>16</span><span>17</span><span>18</span><span>19</span><span>20</span><span>21</span><span>22</span><span>23</span><span>24</span><span>25</span><span>26</span><span>27</span><span>28</span></div><div class="legend"><span><i></i>Pre-Release-Builds</span><span><i class="rc"></i>RC-Phase (RC1 am 26. → RC6 am 28.)</span></div><figcaption>39 Tags in 16 Tagen. Allein am 25. September erschienen acht Builds, v1.1.61 bis v1.1.68.</figcaption></figure>

Am 26. September bekamen die Builds einen neuen Namen. **v1.1.72.272 wurde zum Release Candidate 1**, mit einer neuen Überschrift in den Release Notes: *Formal Release Date Oct. 1, 2026.* RC2 bis RC5 folgten am 27. September, und RC6 (v1.1.77.277) ging heute online. Die Notes jedes RC bitten Tester, Regressionen gegenüber dem stabilen Release v1.1.33.233 zu melden, damit alle mit derselben Grundlage vergleichen.

Die RCs waren nicht nur eine Umbenennung. Sie enthielten echte Fixes:

- **RC1** hat jedes `Agent*`-Paket in `Package.resolved` auf den neuesten Tag festgelegt, damit Fixes wie AgentTools 2.53.18 tatsächlich im Build landen.
- **RC6** hat das Critic-Review mit neueren Claude-Modellen wieder zum Laufen gebracht, die Erkennung von Kontextüberlauf und max_tokens über alle Provider hinweg korrigiert und den Komprimierungsschwellenwert an das Modell gekoppelt, das man tatsächlich verwendet. (Letzteres hat [einen eigenen Blogbeitrag](/blog/context-compaction-half-the-window/).)

Jedes Pre-Release durchläuft denselben Release-Workflow wie ein stabiles Release: Es wird gebaut und notarisiert, und `.zip` und `.dmg` bekommen ihr Notarisierungsticket angeheftet (Stapling). Ein Pre-Release ist kein Rohschnitt. Es ist ein fertiger Build mit weniger Kilometern auf dem Tacho.

## So läuft ein Monat jetzt

| Wann | Was erscheint | Wofür es da ist |
|---|---|---|
| Der 1. | Stabiles Release | Das, das wir allen empfehlen. Homebrew und das Latest-Abzeichen zeigen hierher. |
| Die meisten Tage (bald wöchentlich) | Pre-Release | Neue Features, Experimente und Bugfixes, früh verfügbar für alle, die sie wollen. |
| Letzter Abschnitt des Monats | Release Candidates | Feature-Freeze. Nur noch Fixes, bis ein RC im besten Sinne langweilig ist. |
| Der nächste 1. | Stabiles Release | Der beste RC, befördert. Dann beginnt die Schleife von vorn. |

<figure class="chart"><div class="chart-title">Ein Monat, zwei Rhythmen</div><div class="month"><span class="lbl">Jetzt</span><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="rc"></b><b class="rc"></b><b class="rc"></b><b class="rc"></b><b class="rc"></b><b class="rc"></b><b class="gold"></b></div><div class="month"><span class="lbl">Bald</span><b></b><b></b><b></b><b></b><b></b><b class="p"></b><b></b><b></b><b></b><b></b><b></b><b></b><b class="p"></b><b></b><b></b><b></b><b></b><b></b><b></b><b class="p"></b><b></b><b></b><b></b><b></b><b class="rc"></b><b></b><b></b><b class="rc"></b><b></b><b></b><b class="gold"></b></div><div class="legend"><span><i></i>Pre-Release</span><span><i class="rc"></i>Release Candidate</span><span><i style="background:#22c55e"></i>stabiles Release am 1.</span></div><figcaption>Eine Illustration, kein Zeitplan: Der Monat läuft von links nach rechts und endet am 1. Heute gibt es an den meisten Tagen ein Pre-Release. Bald eines pro Woche.</figcaption></figure>

**Pre-Releases sind das Labor.** Hier probieren wir Neues aus. Manche Ideen landen in einem Pre-Release, werden im echten Einsatz genutzt und innerhalb von ein, zwei Tagen besser. Manche erweisen sich als schlechte Idee, und das erfährt man viel lieber aus einem Pre-Release als aus dem stabilen Build. Auch Bugfixes landen zuerst hier. Wenn dich also etwas stört, taucht der Fix meist innerhalb weniger Tage in einem Pre-Release auf.

**Release Candidates sind die Ruhe vor dem 1.** Das Ziel jedes Zyklus ist einfach: vor dem Release-Datum einen stabilen RC erreichen und ihn dann ausliefern. Die RC-Serie für Oktober ging in drei Tagen von RC1 bis RC6, und jeder davon drehte sich um Fixes, nicht um Features.

**Der 1. ist für alle.** Wer einfach ein solides Agent! möchte, das sich einmal im Monat aktualisiert, bleibt auf Stable und ist fertig.

## Warum irgendwann wöchentlich

Ein Pre-Release pro Tag ist großartig für den Schwung und für uns. Für Tester ist es aber viel, da mitzuhalten. Sobald sich der Monatszyklus eingespielt hat, werden Pre-Releases **einmal pro Woche** erscheinen. So bekommt jeder Build ein paar Tage echten Einsatz, bevor der nächste kommt, und die Notes jedes Pre-Release lohnen sich von oben bis unten.

Wir kündigen die Umstellung hier und in den Release Notes an, wenn es so weit ist.

## So bleibst du auf dem Laufenden

- **Stable:** `brew update && brew install --cask agentiloop-agent`, oder hol dir den als *Latest* markierten Build von der [Releases-Seite](https://github.com/AgentiLoop/Agent/releases).
- **Pre-Releases und RCs:** Sie liegen auf derselben [Releases-Seite](https://github.com/AgentiLoop/Agent/releases), markiert als *Pre-release*. Installiere eines, nutze es für echte Arbeit und sag uns, was kaputtgegangen ist.
- **Eine Regression gefunden?** Eröffne ein Issue mit deiner macOS-Version, Provider und Modell sowie der relevanten Ausgabe aus dem Activity-Log. Bitte lass deine API-Schlüssel weg.

Trag dir den **1. Oktober** in den Kalender ein, dann den 1. November, dann den 1. Dezember. Wir sehen uns am Ersten.
