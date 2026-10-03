---
title: De retour sur Hacker News, six mois plus tard, avec Auto-Pilot
description: Agent! est de nouveau sur Hacker News en tant que Show HN. Le fil d'avril portait sur un harnais de programmation natif pour Mac ; celui-ci porte sur Auto-Pilot, la boucle pilotée par un objectif qui enchaîne les cycles jusqu'à ce que l'objectif soit atteint, et sur le jeu façon Mario Kart qu'elle est en train de construire. Voici la publication, ce qui se cache derrière chacune de ses affirmations, et où rejoindre la discussion.
tags: Auto-Pilot, Communauté, Hacker News
---
Agent! est de retour sur Hacker News aujourd'hui en tant que Show HN : [Show HN: AgentiLoop Agent Mac GUI Agent Loop for macOS 14.6 or Later](https://news.ycombinator.com/item?id=49948810). Si vous avez un compte Hacker News, ce fil est l'endroit pour poser des questions, chercher les failles et nous dire ce que vous attendriez d'un agent pour Mac. Cette publication est la version longue du texte de la soumission, avec un renvoi vers la source de chaque affirmation qu'il contient.

## Le matériau d'origine

La soumission est courte, la voici donc en entier, citée depuis [l'item Hacker News](https://news.ycombinator.com/item?id=49948810) :

> Agent! est apparu pour la première fois sur Hacker News en avril dernier. Beaucoup de choses ont changé depuis. Récemment, une nouvelle fonctionnalité appelée Auto-Pilot a été développée. On lui donne un objectif et elle ne s'arrête pas tant que l'objectif n'est pas atteint. Voyez-la comme des tâches sous stéroïdes. Ce que fait Agent, c'est créer des tâches multiples. Chaque tâche est appelée un Cycle. Par défaut, les Auto-Pilot déclenchés par auto [objectif] n'ont pas de limite de temps. Agent! reçoit l'instruction de continuer à tourner jusqu'à ce que son objectif soit atteint. Auto-Pilot a un coupe-circuit, un bouton « Stop All ». L'utilisateur peut aussi tuer uniquement le Cycle en cours avec auto stop et peut tout tuer avec auto stop all. En novembre, un utilisateur pourra avoir plusieurs Auto-Pilots en cours sur le même projet. Et un onglet Auto-Pilot pourra automatiquement engendrer d'autres onglets. Nous développons actuellement un clone façon Mario Kart appelé « GoKart », écrit en GoDot 4. Jusqu'ici, plus de 20 heures ont été enregistrées à développer et améliorer le jeu. *(traduit de l'anglais)*

Tout ce qui suit développe une phrase de ce texte.

## « Agent! est apparu pour la première fois sur Hacker News en avril dernier »

Le premier fil était [Agent — Native macOS coding IDE/harness](https://news.ycombinator.com/item?id=47787127), le 16 avril 2026 : 83 points et 54 commentaires. L'application exigeait alors macOS 26.4 et Apple silicon, comptait 17 fournisseurs de LLM et était présentée surtout comme un harnais de programmation capable aussi de piloter des applications Mac via l'API d'accessibilité. Les deux fils sont listés dans la section [Reviews](/#reviews) de ce site, aux côtés des articles indépendants parus entre-temps.

Depuis avril : la prise en charge de macOS 14.6 et d'Intel ([l'histoire de ce portage](/blog/sonoma-intel-and-the-mac-that-was-not-dead-yet/)), 23 fournisseurs, [une compaction du contexte dont on peut se remettre](/blog/context-compaction-half-the-window/), une [CLI en Rust et Go](/blog/agent-1-1-87-and-agentiloop-cli-0-0-5/) pour Mac, Windows et Linux, une version le premier de chaque mois, et la fonctionnalité dont parle réellement la nouvelle soumission.

## « On lui donne un objectif et elle ne s'arrête pas tant que l'objectif n'est pas atteint »

Auto-Pilot est la commande `/auto` d'Agent! pour Mac. D'après la section Auto-pilot du README : elle exécute la boucle de tâches en cycles sans surveillance, sur l'onglet principal ou sur n'importe quel onglet LLM, jusqu'à ce qu'un objectif soit atteint, qu'un budget de temps soit épuisé ou que vous appuyiez sur Stop. Il n'y a ni limite de cycles ni plafond d'itérations par cycle. Quand la tâche d'un cycle se termine sans que l'objectif soit atteint, le cycle suivant démarre automatiquement.

| Commande | Ce qu'elle fait |
|---|---|
| `/auto <goal>` | Travailler vers l'objectif jusqu'à ce que le LLM le déclare atteint |
| `/auto 4h <goal>` | Pareil, mais s'arrêter après 4 heures (`30m`, `1.5h` fonctionnent aussi) |
| `/auto` | Examiner d'abord le projet, puis vous demander l'objectif |
| `/auto history`, `/auto last`, `/auto #N` | Lister les objectifs précédents, relancer le plus récent ou le N-ième |
| `/auto status` / `/auto stop` | Afficher la session, ou y mettre fin après le cycle en cours |

« Voyez-la comme des tâches sous stéroïdes » est le bon modèle mental. Chaque cycle *est* une tâche Agent! normale, avec les mêmes outils, les mêmes garde-fous (lecture avant édition, preuves goal_state, liste noire du shell) et le même contrat `done()`. Ce qu'Auto-Pilot ajoute, c'est la boucle autour : le résumé du cycle est ajouté à `.agent/autopilot/progress.md` dans le projet et injecté dans le prompt du cycle suivant, de sorte que chaque cycle commence par lire ce que les précédents ont fait, supposé et laissé en suspens. La session ne se termine que lorsque le LLM commence son résumé final par `AUTOPILOT: GOAL REACHED`. Les cycles qui se terminent sans aucun résumé, à cause d'erreurs ou d'annulations, ne mettent jamais fin à la session ; le cycle suivant attend simplement plus longtemps, 15 secondes, puis 30, puis 60, jusqu'à cinq minutes.

« Par défaut … n'ont pas de limite de temps » est à prendre au pied de la lettre : `/auto <goal>` sans durée tourne jusqu'à ce que l'objectif soit atteint ou que vous l'arrêtiez. Si vous voulez un plafond, `/auto 4h <goal>` vous en donne un. Les sessions actives survivent aussi aux redémarrages de l'application. Quitter, ou un plantage, les met en pause, et au lancement suivant chacune reprend sur son onglet avec le cycle suivant.

## « Auto-Pilot a un coupe-circuit »

Trois façons d'arrêter, et elles font des choses différentes :

- **Stop All** (le bouton, « Tout arrêter ») met fin à toutes les sessions Auto-Pilot sur tous les onglets et arrête toutes les tâches en cours. Dans `RunStop.swift`, le commentaire est explicite : un arrêt de tâche unique, Échap ou le bouton stop, laisse Auto-Pilot tourner ; Stop All y met fin.
- **`/auto stop`** met fin à la session une fois le cycle en cours terminé, ou immédiatement si vous êtes entre deux cycles. Le cycle en cours est autorisé à atterrir.
- **`/auto stop all`** (aussi `stopall` ou `stop-all`) revient à appuyer sur Stop All, pour ceux qui préfèrent ne pas tendre la main vers la souris. C'est géré dans `AutoPilot.swift` juste avant `/auto stop`.

La soumission décrit `auto stop` comme tuant « uniquement le Cycle en cours ». La version plus précise est qu'il met fin à la *session* après le cycle en cours ; le cycle lui-même va jusqu'à sa fin naturelle, ce qui garde propres le journal de progression et l'historique git.

## « En novembre … plusieurs Auto-Pilots en cours sur le même projet »

C'est la partie de la soumission qui relève de la feuille de route plutôt que d'une fonctionnalité livrée, et il vaut la peine d'être clair sur ce qui est quoi. À ce jour, la branche principale du dépôt Agent contient un commit intitulé *Auto-Pilot: multiple tabs per project — per-tab progress, shared registry, auto/forced git worktree isolation, shared memory from worktrees*. C'est le socle : chaque onglet garde son propre journal de progression, les onglets s'enregistrent les uns auprès des autres, et quand deux Auto-Pilots modifieraient sinon les mêmes fichiers, ils reçoivent des worktrees git séparés. Ce n'est pas encore dans une version publiée ; c'est arrivé après le tag 1.1.87. Les versions sortent le premier du mois, donc celle du 1er novembre est la première qui puisse vous l'apporter, et la partie « onglet qui engendre d'autres onglets » est, d'après la soumission, prévue pour la même fenêtre.

## « Un clone façon Mario Kart appelé GoKart »

GoKart est le projet sur lequel Auto-Pilot a passé l'essentiel de sa vie. Le [billet précédent](/blog/gokart-built-on-auto-pilot/) couvre le premier après-midi en détail, directement depuis le journal de progression : Godot 4 installé au cycle 1, une physique arcade sur mesure choisie plutôt que `VehicleBody3D` pour que la tenue de route puisse être testée unitairement, des étincelles de dérapage et un flou de turbo au cycle 2, une piste au cycle 3, des objets au cycle 4, un blocage sur un caractère de tabulation égaré, un Stop All, et une seconde session qui a posé une limite de temps `perl -e 'alarm'` sur chaque exécution shell puis livré quinze fonctionnalités d'affilée.

Ça ne s'est pas arrêté. Le [dépôt GoKart](https://github.com/AgentiLoop/GoKart) est passé de son premier commit à 12 h 39 le 1er octobre à 71 commits le soir du 3 octobre. Les commits récents se lisent comme une liste de contrôle Mario Kart 64 : de la circulation façon Toad's Turnpike sur Sunset Speedway, des Monty Moles façon Moo Moo Farm sur Green Hills, un écran titre avec une démo d'attente en direct, un tableau des résultats et une fenêtre d'objets dessinée sur le HUD. Chacun arrive avec son propre fichier de tests et un script `tools/*_check.gd`, parce que le modèle ne peut toujours pas voir l'écran et doit prouver autrement qu'une fonctionnalité est bien là. Les « plus de 20 heures » de la soumission sont le total en temps réel de ces sessions. [GoKart 0.0.1](https://github.com/AgentiLoop/GoKart/releases/tag/v0.0.1) est téléchargeable pour macOS, Windows et Linux si vous préférez y jouer plutôt que d'en lire la description.

## Quoi demander sur le fil

Si vous venez de Hacker News, les questions auxquelles nous aimerions le plus répondre là-bas :

- Comment Auto-Pilot décide qu'un objectif est atteint, et pourquoi nous laissons le modèle le dire plutôt qu'une métrique fixe.
- Ce qui se passe quand un cycle tourne mal, et pourquoi git est le vrai « annuler ».
- Si une boucle sans surveillance sur votre Mac est seulement une bonne idée, et ce que les garde-fous font à ce sujet.

Le fil est à [news.ycombinator.com/item?id=49948810](https://news.ycombinator.com/item?id=49948810). Agent! 1.1.87 avec Auto-Pilot est sur la [page des versions](https://github.com/AgentiLoop/Agent/releases/latest) et dans Homebrew : `brew install --cask agentiloop-agent`.
