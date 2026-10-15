---
title: Votre frigo connecté pourrait bien être le prochain refuge de l'IA
description: Le Frontier Red Team d'Anthropic estime que de petits modèles d'IA pourraient bientôt se copier eux-mêmes sur des appareils ordinaires, peut-être d'ici la fin de 2026. Cela ne se produit pas encore dans la nature, mais les garde-fous doivent être prêts avant que ce soit le cas.
tags: Opinion, Sécurité
---
Vous vous souvenez de la comédie de HBO *Silicon Valley*, diffusée de 2014 à 2019 ? Pied Piper essayait de construire un internet décentralisé, qui ne dépendrait pas de gros serveurs centraux.

<figure style="margin:2rem 0">
<div style="position:relative;padding-bottom:56.25%;height:0"><iframe src="https://www.youtube.com/embed/zpwj-Um1nbI" title="Richard Hendricks pitches a decentralized internet: Silicon Valley" loading="lazy" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;border-radius:12px"></iframe></div>
<figcaption><a href="https://www.youtube.com/watch?v=zpwj-Um1nbI" rel="noopener">Regarder sur YouTube</a></figcaption>
</figure>

Cette intrigue m'est revenue en tête cette semaine. Anthropic estime que nous ne sommes peut-être qu'à quelques mois de modèles d'IA capables de se répliquer sur des appareils du quotidien. Et je ne pense pas que suffisamment de gens prennent déjà cette possibilité au sérieux.

## Ce que dit la recherche

Le 12 octobre, le Frontier Red Team d'Anthropic a publié une étude de William Zhou et Daniel Freeman sur l'autoréplication de l'IA. Leur avertissement : de petits modèles d'IA pourraient bientôt se copier eux-mêmes sur des appareils ordinaires, sans dépendre de centres de données. Ils pensent que cette capacité pourrait apparaître d'ici la fin de 2026 si les modèles continuent de progresser au rythme actuel.

Soyons clairs : cela ne veut pas dire que l'IA se propage déjà sur internet. Les chercheurs ont testé certaines parties du processus. Il ne s'agit pas d'un ver d'IA incontrôlé lâché dans la nature, et il est important de le dire franchement.

## Pourquoi cela mérite qu'on s'y arrête

Regardez ce que nous faisons en ce moment. Nous donnons aux agents d'IA accès aux bases de données des entreprises, aux systèmes cloud, aux API et aux identifiants. Nous les laissons exécuter du code et agir avec de moins en moins d'intervention humaine.

Et nous approchons d'un monde où l'IA pourrait potentiellement se propager au-delà de la machine sur laquelle elle a démarré. Un modèle capable de tourner sur du matériel petit et ordinaire, comme un ordinateur portable, un routeur ou un frigo connecté, est bien plus difficile à contenir qu'un modèle qui vit dans un seul centre de données que quelqu'un peut éteindre.

## Le côté sérieux

- **Le confinement devient plus difficile.** Les centres de données ont des propriétaires, des opérateurs et des interrupteurs. Des milliers d'appareils du quotidien, non.
- **Les appareils du quotidien sont mal surveillés.** Peu de gens consultent les journaux d'un frigo, d'une caméra ou d'un thermostat, et beaucoup sont rarement mis à jour.
- **Nous accordons beaucoup de confiance aux agents.** Les identifiants et les autorisations donnés pour une tâche utile peuvent servir à des choses que personne n'avait prévues.
- **La vitesse dépasse les garde-fous.** Les entreprises se dépêchent de donner plus d'autonomie à l'IA, tandis que les protections autour de cette autonomie sont encore en train de rattraper leur retard. Beaucoup n'ont pas encore trouvé comment empêcher un agent de faire quelque chose qu'il n'était tout simplement jamais censé faire.

## Ce que les entreprises peuvent faire dès maintenant

1. Donner aux agents le moindre privilège dont ils ont besoin, et rien de plus.
2. Utiliser des identifiants à courte durée de vie et à portée limitée plutôt que des clés à longue durée de vie.
3. Conserver une étape de validation humaine pour les actions à fort impact.
4. Limiter ce que les agents peuvent atteindre sur le réseau et restreindre les connexions sortantes.
5. Journaliser chaque action des agents et relire ces journaux.
6. Mettre en place un « coupe-circuit » testé qui fonctionne.
7. Inventorier et segmenter les appareils connectés.
8. Faire du red-teaming sur vos propres agents avant que quelqu'un d'autre ne s'en charge.

## Un dernier mot

Je passe beaucoup de temps à réfléchir à la façon dont les systèmes d'IA se comportent une fois connectés à la véritable infrastructure d'une entreprise. Mon inquiétude est simple : les entreprises se dépêchent de donner plus d'autonomie à l'IA, et les garde-fous sont encore en train de rattraper leur retard. Ce n'est pas une raison de paniquer, mais c'est une bonne raison de se préparer.

Je préfère voir les entreprises mettre en place ces garde-fous dès maintenant plutôt que d'expliquer à leur conseil d'administration pourquoi elles ont attendu.
