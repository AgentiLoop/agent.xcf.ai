---
title: Pourquoi nous avons supprimé le mode programmation : laissons le modèle choisir ses propres outils
description: Agent! essayait de deviner si vous vouliez programmer ou automatiser, et masquait des outils en conséquence. Une tâche Photo Booth ratée a montré pourquoi l’environnement doit cesser de remettre en question le modèle.
tags: Architecture, Conception
---
Les premières versions d’Agent! disposaient de **modes** : programmation, automatisation et standard. L’idée semblait raisonnable. Une tâche de programmation n’a pas besoin de l’outil d’accessibilité, et une tâche du type « clique sur ce bouton » n’a pas besoin de Xcode. En masquant ce qui n’est pas pertinent, le modèle voit une liste d’outils plus courte, consomme moins de tokens et fait moins de mauvais choix.

Le 7 avril 2026, le commit `7ea44c0d` a supprimé tout le système. Voici le bug qui en est à l’origine, et le principe qu’il nous a laissé.

## Comment fonctionnaient les modes

Au deuxième tour d’une tâche, l’environnement examinait votre demande et la comparait à deux listes de mots-clés. Des mots comme `build`, `compile`, `edit`, `fix` et `refactor` signifiaient programmation. Des mots comme `click`, `button`, `window`, `photo` et `accessibility` signifiaient automatisation. Il activait alors un indicateur, `codingModeEnabled` ou `automationModeEnabled`, et restreignait les outils visibles par le modèle aux groupes de ce mode. Le modèle pouvait aussi changer lui-même de mode via un outil `mode`.

## Le bug : Photo Booth en mode programmation

Le signalement disait simplement « l’accessibilité est cassée ». La cause, selon les propres termes du message de commit : le basculement automatique a interprété `open -a Photo Booth` comme un signal inconnu et **s’est rabattu par défaut sur le mode programmation**. Le mode programmation excluait le groupe Auto, et c’est dans le groupe Auto que se trouve l’outil `accessibility`.

On a donc demandé au modèle de prendre une photo, et le seul outil conçu pour appuyer sur le déclencheur avait disparu en pleine tâche. Il a fait ce que fait un modèle compétent avec les outils qui lui restent : il s’est rabattu sur `osascript` via le shell, qui échouait sans cesse avec *« Impossible d’obtenir la barre d’outils 1 de la fenêtre 1. »*

Le modèle n’avait aucun problème, pas plus que l’outil d’accessibilité. L’environnement s’était trompé sur l’intention et avait discrètement retiré la bonne réponse.

## Le correctif qui n’en était pas un

Le correctif évident consistait à ajouter `open -a` aux mots-clés d’automatisation. Le message de commit le dit sans détour : cela n’aurait été qu’« un pansement de plus dans une longue série ». La détection d’intention par mots-clés est une bataille perdue d’avance. Chaque nouvelle application, formulation ou langue ouvre une nouvelle brèche, et chaque raté échoue de la manière la plus déroutante possible : avec un modèle qui, soudain, ne peut plus faire ce qu’il savait faire un tour plus tôt.

## Ce qui l’a remplacé : rien

Tout le système de modes a été retiré : 13 fichiers, 141 lignes supprimées et 39 ajoutées. Cela comprenait :

- les indicateurs `codingModeEnabled` et `automationModeEnabled` ainsi que leurs listes de groupes d’outils
- le basculement automatique au tour 2, à la fois dans la boucle de tâches principale et dans les tâches d’onglet
- `predictToolGroups()`, la fonction qui devinait les groupes d’outils à partir de votre prompt
- la restriction de la liste d’outils pour les endpoints locaux dans les services Claude et compatibles OpenAI
- les alias `coding` et `automation` pour les sous-agents (on passe désormais les vrais noms de groupes)

Les outils sont désormais filtrés **uniquement par vos propres interrupteurs** dans les Réglages (`ToolPreferencesService`). Chaque outil que vous avez activé est disponible à chaque tour, et le modèle choisit ce dont il a besoin.

Deux petits détails montrent le soin qu’exige une telle suppression. L’outil `mode` n’a pas été purement et simplement retiré. Il est devenu une opération sans effet qui répond *« le changement de mode a été supprimé »*, car un modèle ayant une ancienne conversation dans son contexte pourrait encore l’appeler, et une réponse claire vaut mieux qu’une erreur d’outil inconnu. Par ailleurs, la révision du prompt système est passée de 71 à 72, afin que tout prompt enregistré sur disque mentionnant les modes soit resynchronisé.

## Le résultat

Fini le spam de journaux *« Mode programmation activé automatiquement »*. Fini les outils qui disparaissent en pleine tâche. Fini la liste d’outils qui change d’un tour à l’autre.

## Le principe

Cette décision a façonné une grande partie de ce qui a suivi, il vaut donc la peine de l’énoncer clairement :

> L’environnement doit garantir la **sécurité**, pas deviner l’**intention**.

Agent! est strict là où la rigueur est objective. Il refuse les commandes shell catastrophiques, les modifications de fichiers que le modèle n’a pas lus et les « terminé » sans preuve. Ce sont des faits qu’il peut vérifier. L’outil dont une tâche a besoin relève du jugement, et le modèle en juge mieux qu’une liste de mots-clés. Quand l’environnement désavoue le modèle sur une question de jugement, il échoue silencieusement et de façon déroutante. Quand il applique une règle vérifiable, il échoue bruyamment et avec une raison.

Si vous développez un agent, il est tentant d’« aider » le modèle en réduisant ses choix. Mesurez d’abord. Une liste d’outils un peu plus longue coûte quelques tokens. Un outil manquant peut vous coûter toute la tâche.
