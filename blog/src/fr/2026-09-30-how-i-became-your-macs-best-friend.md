---
title: Comment Agent! a commencé : trois jours en mars
description: Trois ans de pièces détachées, une boucle manquante et 177 commits en moins de deux jours. La vraie origine d'Agent!, tirée directement de git.
tags: Origines, Histoire
---
<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 380" role="img" aria-labelledby="lego-title lego-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="lego-title">Un robot sympathique construit un Mac avec des briques de jouet</title>
<desc id="lego-desc">Un robot bleu souriant tient une brique jaune au-dessus d'un écran de Mac à moitié construit en briques de jouet rouges, jaunes, vertes, bleues et orange. Une bulle dit : Presque fini !</desc>
<rect width="760" height="380" rx="20" fill="#eef6ff"/>
<path d="M40 318H720" stroke="#8b684c" stroke-width="13" stroke-linecap="round"/>
<path d="M190 92l-6 26 40-26" fill="#fff"/>
<rect x="120" y="30" width="230" height="64" rx="22" fill="#fff" stroke="#b6c8e4" stroke-width="3"/>
<text x="235" y="72" text-anchor="middle" font-family="system-ui,sans-serif" font-size="26" font-weight="700" fill="#173452">Presque fini !</text>
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
<text x="190" y="354" text-anchor="middle" font-family="system-ui,sans-serif" font-size="21" fill="#173452">Le bâtisseur.</text>
<text x="540" y="354" text-anchor="middle" font-family="system-ui,sans-serif" font-size="21" fill="#173452">Le Mac. Plus qu'une brique.</text>
</svg>
<figcaption>Tout ce qui est grand commence par un tas de petites briques. Le secret, c'est de savoir laquelle vient ensuite.</figcaption>
</figure>

Toute app a un premier jour. Celui d'Agent! était un mercredi : **le 11 mars 2026, à 15 h 07.** On connaît la minute exacte parce que git l'a notée.

Mais les briques traînaient là depuis bien plus longtemps.

## Trois ans de pièces détachées

Avant Agent!, il y a eu d'autres apps. **ANIE.** **Game Changer.** **BattleScript.** Le **XCF MCP Server et Client.** **D1F**, un outil pour modifier beaucoup de lignes d'un fichier d'un seul coup. Et environ huit paquets Swift, tous écrits par la même personne.

Chacune savait faire un bout du travail. Certaines savaient parler à une IA. D'autres savaient modifier du code. D'autres savaient bricoler dans Xcode. Aucune ne savait faire le plus important : **continuer toute seule.**

Pensez à un jouet mécanique. Vous le remontez, il fait trois pas, il s'arrête. Mignon. Pas très utile. Ce qui manquait, c'était une boucle : regarder le problème, choisir un outil, l'utiliser, vérifier ce qui s'est passé, et recommencer jusqu'à ce que le travail soit fait. (Cette boucle a [son propre article, avec un robot et un sandwich](/blog/what-is-an-agent-loop/).)

Dès que la boucle a fonctionné, le meilleur des anciennes pièces a pu s'emboîter dessus. Voilà toute l'histoire en une phrase. Le reste, ce sont des détails, et les détails sont amusants.

## Premier jour : un cerveau, un assistant et un bouton Annuler

Le tout premier vrai commit s'appelle *« Autonomous Agent with privileged launch daemon. »* Il comptait 20 fichiers et 1 765 lignes de Swift. Voici ce qu'il y avait dans la boîte :

- Une fenêtre SwiftUI où l'on tape ce qu'on veut.
- Un cerveau d'IA, Claude, chargé de réfléchir.
- Un **Launch Daemon** : un petit assistant qui tourne en arrière-plan avec les clés de toute la maison, pour que l'agent puisse faire les corvées système des grands.
- L'historique des tâches, les captures d'écran et le collage.

Une heure plus tard arrivait le premier correctif de plantage (coller une capture d'écran faisait tout planter). Quelques minutes après, un grand bouton rouge **Annuler**, relié à la touche Échap. Quand on construit quelque chose qui agit tout seul, le bouton stop arrive tôt.

À 17 h 27, il y avait un deuxième assistant, un **Launch Agent**, qui exécute les commandes en tant que *vous* et non en tant que root tout-puissant. Demander le passe-partout pour lister un dossier, c'est comme appeler les pompiers pour allumer une bougie. Six minutes plus tard, Agent! recevait son deuxième cerveau : **Ollama**, pour faire tourner des modèles d'IA qui vivent sur votre propre Mac.

Avant la fin de la journée, il savait aussi écrire et lancer des scripts Swift, piloter Xcode, voir des images avec des modèles de vision et afficher un écran d'accueil. Il a aussi reçu de petits voyants d'état façon feu tricolore, qui ont demandé une douzaine de commits pour se fixer sur vert, jaune et rouge. Certaines choses sont plus difficiles qu'une boucle d'agent.

## Deuxième jour : « Je peux ? »

Le 12 mars, Agent! a appris qu'un Mac est poli, et très strict là-dessus.

Pour contrôler une autre app, comme Musique ou Pages, macOS vous demande d'abord : *« Agent! souhaite contrôler Musique. Autoriser ? »* Faire apparaître vraiment cette petite fenêtre a pris toute la soirée. De 20 h 20 environ à 21 h 40, l'historique est une pile d'essais à quelques minutes d'intervalle : essayer d'une façon, essayer sur le fil principal, ouvrir Réglages Système, essayer `osascript`, essayer de demander `every window`, essayer juste `name`. En plus, Keynote, Numbers et Pages avaient changé de bundle ID, donc il frappait aux portes avec les mauvais noms.

Il y est arrivé. Le même soir, il a appris à afficher des images et des pages web directement dans son propre journal : quand il crée une pochette d'album, vous voyez la pochette.

## Troisième jour : un nom et un numéro de version

Le matin du 13 mars, l'app a reçu son nom. Le commit de 9 h 06 s'intitule *« rename app to Agent! »* Point d'exclamation compris, exprès.

Vingt minutes plus tard arrivait un changement qui compte encore aujourd'hui : les scripts ont cessé d'être des programmes séparés pour devenir des **bibliothèques dynamiques** chargées directement dans l'app. C'est pour ça que les AgentScripts ont les mêmes autorisations Mac qu'Agent!, sans redemander.

Plus tard ce jour-là, la version **1.0.0** était étiquetée. Depuis le premier commit, cela fait **177 commits en moins de deux jours.** Les versions 1.0.1 à 1.0.16 ont suivi dans les huit jours suivants.

Petit détail : le nom d'auteur sur ces premiers commits n'est pas celui d'une personne. C'est **« Agent! for MacOS ».**

## Grandir

Après ce premier sprint, l'histoire s'accélère :

- **6 avril.** Près d'un mois d'historique a été compressé en un seul commit de départ propre. L'historique complet a été conservé dans une sauvegarde.
- **7 avril.** Le « mode code », le « mode automatisation » et le « mode standard » ont été [arrachés](/blog/why-we-ripped-out-modes/). Un seul agent, tous les outils, à chaque fois.
- **Avril.** Apple Intelligence était de la partie, comme un cerveau qui tourne directement sur le Mac, gratuitement.
- **31 août.** Le projet est passé de l'organisation GitHub `macOS26` à **AgentiLoop**, et le site est devenu **agentiloop.ai**.
- **Dernièrement.** Agent! a appris à [tourner sur macOS 14.6 et sur les Mac Intel](/blog/sonoma-intel-and-the-mac-that-was-not-dead-yet/), et il a aidé à construire ses propres petits frères en terminal : [AgentiLoopCLI](https://github.com/AgentiLoop/AgentiLoopCLI) en Rust et [AgentiLoopGo](https://github.com/AgentiLoop/AgentiLoopGo) en Go.

Il a commencé avec un seul cerveau. Aujourd'hui, il fonctionne avec **23 fournisseurs d'IA**, plus Apple Intelligence. Depuis le grand ménage d'avril, la branche principale a gagné plus de 1 300 commits.

## Pourquoi il est comme il est

Presque tout ce qui est étrange chez Agent! remonte à ces trois premiers jours.

Il a deux assistants, un pour vous et un pour root, parce que le premier jour avait besoin des deux. Il est 100 % Swift, comme les pièces détachées dont il est fait. Il est construit à partir de code original, pas d'un tas de 65 paquets NPM. Il pilote les autres apps par leur nom via l'Accessibilité et AppleScript parce que le deuxième jour a été passé à apprendre à demander poliment au Mac. Et il a toujours un grand bouton Annuler.

Tout ce qui est grand commence par un tas de petites briques. Celui-ci s'empilait depuis trois ans. Le 11 mars, quelqu'un a enfin trouvé la brique qui tient toutes les autres ensemble : la boucle.
