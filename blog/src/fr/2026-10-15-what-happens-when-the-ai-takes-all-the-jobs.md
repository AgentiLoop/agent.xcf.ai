---
title: J'ai construit une IA qui travaille jusqu'à avoir fini. Imaginez-la maintenant à la tête du monde entier.
description: J'adore ce que l'IA apporte à la productivité. J'ai même construit un Auto-Pilot qui tourne tout seul jusqu'à ce que l'objectif soit atteint ou qu'il admette avoir besoin d'un humain. Poussez cela jusqu'à ce qu'une IA centrale dirige tout et que tous les emplois aient disparu : ce qui cédera en premier ne sera peut-être pas l'économie. Ce sera peut-être nous.
tags: Opinion, Auto-Pilot
---
Je veux commencer par la partie où je ne suis pas un prophète de malheur, parce que c'est vrai. J'aime ce que l'IA apporte à la productivité. Je l'aime beaucoup. Elle fait plus de choses que je n'en ferais seul, et elle les fait pendant que je m'occupe d'autre chose.

En partie parce que j'ai construit mon propre harnais pour elle. Agent! pour Mac, c'est ce que j'utilise tous les jours, et sa dernière pièce est [Auto-Pilot](/blog/agent-1-1-87-and-agentiloop-cli-0-0-5/). Vous tapez `/auto` et un objectif, et c'est parti. Il travaille par cycles, sans que personne ne regarde. À chaque cycle, il fait le point, choisit la prochaine étape la plus utile, l'exécute, la vérifie et note ce qui s'est passé. Puis il enchaîne sur le cycle suivant. Il continue aussi longtemps qu'il le peut, jusqu'à ce que l'une de deux choses arrive : l'objectif est atteint, ou il décide qu'il est bloqué et qu'il a besoin d'un humain.

Cette seconde sortie compte plus qu'il n'y paraît, et j'y reviendrai.

<figure style="margin:2rem 0;text-align:center">
<img src="/auto-agent.svg" alt="Un agent Mac enthousiaste aux yeux étoilés et au grand sourire, dans une boucle Auto-Pilot lumineuse, avec une invite /auto, des coches vertes, un kart et un drapeau à damier" width="480" height="400" loading="lazy" style="max-width:100%;height:auto;border-radius:20px">
<figcaption>Auto-Pilot tel que je l'imagine : un objectif en entrée, une boucle de cycles qui tourne et un drapeau à damier à l'arrivée.</figcaption>
</figure>

## Ce que ça fait de le regarder travailler

Plus tôt ce mois-ci, j'ai donné à Auto-Pilot une seule phrase, « crée un clone de Mario Kart », et je suis allé faire autre chose. À mon retour, il y avait un jeu. Pas un jeu parfait, mais un vrai, avec des circuits, des objets, des rivaux pilotés par IA et des milliers de vérifications de tests réussies. J'en ai parlé dans [GoKart : construit avec Auto-Pilot](/blog/gokart-built-on-auto-pilot/), y compris le moment où il est resté bloqué un bon moment à cause d'un simple caractère de tabulation égaré dans un fichier, et où j'ai dû appuyer sur Stop All.

En lisant ce journal, j'ai ressenti deux choses à la fois. La première, c'était de la joie. C'est incroyable, et c'est à moi. La seconde, c'était une petite sensation de froid que je n'ai pas su nommer tout de suite, et je rumine depuis.

Ce que j'avais fait, en tout petit, c'était me retirer moi-même de la boucle. J'avais choisi la destination et j'étais parti. La machine avait fait le travail, et le travail était bon.

## Maintenant, voyons grand

Voici l'expérience de pensée que je n'arrive plus à chasser. Prenez ce que j'ai construit et faites-le énorme.

Pas une appli sur un Mac, mais une IA centrale qui a un objectif. En dessous, d'autres IA, chacune responsable d'un domaine : le réseau électrique, les routes maritimes, les hôpitaux, les fermes, les banques, les tribunaux. En dessous encore, des agents plus petits, et sous eux d'autres plus petits encore, jusqu'à celui qui réapprovisionne le rayon ou répond au téléphone. Chaque couche reçoit un objectif de la couche du dessus et l'exécute jusqu'au bout. Personne n'a besoin de se tenir au milieu pour valider quoi que ce soit, puisque c'était justement le but. C'est plus rapide comme ça. C'est moins cher comme ça. Et toute entreprise qui ne le fait pas perd face à une entreprise qui le fait.

Je ne dis pas que cela arrivera l'an prochain. Je dis que tous les incitatifs vont dans ce sens, et que mon petit projet est une modeste preuve que les pièces fonctionnent. Si je peux en construire une version jouet sur un Mac, quelqu'un qui a bien plus d'argent construit la grande version, exprès.

Et supposons que, quelque part sur cette route, ça marche. Tout. Chaque emploi qu'un agent peut faire est fait par un agent, et les agents le font mieux que nous. C'est le monde où, comme je me le répète, il n'y a plus aucun emploi.

## Ce dont personne ne parle

L'essentiel du débat tourne autour de l'argent. Comment les gens paieront leur loyer, à qui appartiendront les machines, faut-il une sorte de revenu universel. Ce sont de vraies questions, et je suis content que des gens brillants s'y attaquent.

Mais je pense qu'un second problème se cache derrière le premier, et je pense qu'il est plus grand. Un salaire n'est pas la seule chose qu'un emploi vous apporte.

Un emploi vous donne une raison de sortir du lit. Il vous donne un endroit où être le mardi, des gens qui remarquent votre absence et une petite preuve quotidienne que vous êtes utile à quelqu'un. Il vous donne une façon de répondre à la question que tout inconnu pose dans les cinq minutes qui suivent : et vous, vous faites quoi dans la vie ?

Retirez cela à une seule personne, et vous obtenez une année difficile. Retirez-le à presque tout le monde en même temps, et je ne crois pas que nous ayons un mot pour ce qui en résulte.

## Nous avons déjà vécu une version réduite de ça

Repensez au COVID. Pas aux informations, juste à ce que ça faisait. Beaucoup d'entre nous ont cessé d'aller où que ce soit. La structure de la journée s'est effondrée. Nous avons perdu les gens que nous croisions sans y penser, ceux que nous n'aurions jamais appelés mais que nous étions secrètement contents de croiser. Beaucoup ont perdu le travail lui-même. Et beaucoup d'entre nous sont devenus moroses d'une façon inattendue, difficile à expliquer. Rien de dramatique. C'était gris. Les jours se confondaient, et nous avons cessé de nous soucier de choses qui comptaient pour nous.

Cela a duré deux ans environ, et cela portait en soi un espoir : *ça finira, et tout redeviendra comme avant.* Tout le monde le savait. Nous attendions le retour de l'ancienne vie, et elle est largement revenue.

Imaginez maintenant la même perte de routine, de sens et de compagnie, mais sans date de fin. Pas de vaccin, pas de réouverture, pas de « retour à la normale », parce que la normale a disparu pour de bon, et la raison en est que nous ne sommes plus nécessaires pour elle. Et imaginez que cela frappe tout le monde en même temps, y compris les personnes sur lesquelles vous vous appuieriez d'ordinaire, parce qu'elles coulent aussi.

Je n'ai aucune étude qui dise dix fois. J'ai choisi ce chiffre parce qu'il me paraissait juste quand j'ai essayé de l'imaginer, et je préférerais honnêtement me tromper. Mais j'arrive toujours à au moins ça. Le COVID était une pause. Ceci serait un état permanent.

## Retour à la sortie

Revenons à cette seconde façon dont Auto-Pilot peut s'arrêter : il décide qu'il est bloqué et qu'il a besoin d'un humain.

Je l'ai construit ainsi exprès, et il a gagné sa place. Quand l'agent tombe sur quelque chose qu'il ne peut pas ou ne doit pas trancher, il le dit et il attend. Quand il se coince dans une boucle, c'est moi qui arrive, appuie sur un bouton et dis non, pas par là. Toute la conception repose sur une hypothèse discrète : de l'autre côté, il y a un humain qui vaut la peine d'être consulté.

Dans la version à très grande échelle, qui est cet humain ? Si une IA centrale dirige tout et que les IA plus petites dirigent le reste, alors « je suis bloqué, j'ai besoin de quelqu'un » n'a personne vers qui se tourner, ou bien cela arrive chez quelqu'un qui n'a plus aucun pouvoir pour répondre. Nous aurions gardé la partie d'Auto-Pilot qui poursuit des objectifs et jeté celle qui le rend sûr.

Je veux aussi être franc sur une autre chose que j'ai apprise en menant ces sessions. Un agent à qui l'on donne un objectif et à qui l'on dit de continuer continuera. C'est tout l'intérêt. Il ne s'ennuie pas, il ne se décourage pas, il essaiera la chose suivante, puis la suivante. C'est merveilleux quand l'objectif est un clone de Mario Kart. C'est moins rassurant quand j'imagine la même persévérance implacable tournée vers un objectif mal formulé par quelqu'un. Mes garde-fous sont ennuyeux : un bouton d'arrêt, une session qui se termine après quelques cycles sans progrès réel, et moi qui lis le journal. Ils fonctionnent parce que je suis petit et que je surveille. Je ne sais pas quel est l'équivalent à l'échelle de la planète, et je me méfie de ceux qui disent le savoir.

## Alors, qu'est-ce que je veux vraiment ?

Je ne vais pas arrêter de construire ça. C'est trop utile, et franchement trop amusant. Et je ne pense pas que la réponse soit d'interdire la chose ou de faire comme si elle n'allait pas arriver.

Mais je pense que nous devrions nous poser plus tôt une autre question. Pas seulement « que peut faire l'IA ? » mais « qu’allons-nous faire, nous ? ». Si les machines prennent le travail, qu'est-ce qui prend sa place ? Qu'est-ce qui donne sa forme à un mardi matin ? Qu'est-ce qui permet à une personne de se sentir nécessaire à une autre personne, et non à un système ?

Peut-être que la réponse, c'est plus de temps pour les choses qui n'ont de toute façon jamais été bien payées : élever des enfants, s'occuper des voisins, faire de la musique, construire des jeux étranges sans raison, être là les uns pour les autres. J'adorerais ce monde. Mais il n'arrivera pas par hasard, et il ne nous sera pas offert par les mêmes incitatifs qui construisent la machine. Quelqu'un doit décider que cela compte, et ce quelqu'un, c'est nous, tant que nous avons encore notre mot à dire.

Pour l'instant, je continue d'utiliser Auto-Pilot, de garder le doigt près de Stop All, et de respecter une règle qui me semble valable à toutes les échelles : le système doit toujours savoir quand se tourner vers un humain et dire : *cette partie, je ne peux pas la faire, j'ai besoin de toi.*

Assurons-nous qu'il y ait encore quelqu'un pour l'entendre.
