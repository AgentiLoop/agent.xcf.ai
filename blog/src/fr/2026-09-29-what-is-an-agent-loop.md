---
title: Qu’est-ce qu’une boucle d’agent ? Un robot, un sandwich et l’art de réessayer
description: Observer, choisir, agir, vérifier. Un guide illustré et ludique des boucles d’agent, assez simple pour un enfant de cinq ans, avec de quoi réfléchir pour les grands.
tags: Explications, Boucles d’agent
---
Imaginez un petit robot nommé Pip.

Vous lui dites : **« S’il te plaît, fais-moi un sandwich à la confiture. »**

Pip regarde la table. Il y a du pain. Il y a de la confiture. Il y a une cuillère couverte d’une quantité suspecte de beurre de cacahuète.

Pip annonce-t-il : « Sandwich terminé ! » ?

Non. Ce serait un discours, pas un sandwich.

Pip doit **observer, choisir une petite étape, l’accomplir et vérifier ce qui s’est passé**. Ensuite seulement, Pip peut décider de la suite.

Ce schéma qui se répète, c’est une **boucle d’agent**.

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 360" role="img" aria-labelledby="pip-title pip-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="pip-title">Pip a un objectif, mais pas encore de sandwich</title>
<desc id="pip-desc">Un sympathique robot bleu regarde deux tranches de pain et un pot de confiture. Une bulle dit : Un plan n’est pas un sandwich.</desc>
<rect width="760" height="360" rx="20" fill="#eef6ff"/>
<path d="M300 104l-26 24 58-24" fill="#fff"/>
<rect x="265" y="28" width="450" height="76" rx="24" fill="#fff" stroke="#b6c8e4" stroke-width="3"/>
<text x="490" y="75" text-anchor="middle" font-family="system-ui,sans-serif" font-size="25" font-weight="700" fill="#173452">Un plan n’est pas un sandwich.</text>
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
<text x="652" y="239" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" font-weight="700" fill="#fff">CONFITURE</text></g>
<text x="147" y="326" text-anchor="middle" font-family="system-ui,sans-serif" font-size="21" fill="#173452">Voici Pip.</text>
<text x="495" y="326" text-anchor="middle" font-family="system-ui,sans-serif" font-size="21" fill="#173452">L’objectif : un sandwich à la confiture.</text>
</svg>
<figcaption>Pip est notre assistant imaginaire. Aucun vrai robot n’a été rendu collant pendant la réalisation de cette illustration.</figcaption>
</figure>

## Toute l’idée, en quatre petits mots

**Observer. Choisir. Agir. Vérifier.**

- **Observer :** Que se passe-t-il en ce moment ?
- **Choisir :** Quelle est la prochaine chose utile à faire ?
- **Agir :** Faire cette chose.
- **Vérifier :** Que s’est-il réellement passé ? A-t-on terminé ?

Si le travail n’est pas terminé, on refait un tour, avec les nouvelles informations.

Une **boucle**, c’est simplement quelque chose qui se répète. Un **agent** est un système capable d’avancer vers un objectif en utilisant les outils et les autorisations qu’on lui a donnés.

Mettez les deux ensemble : **une boucle d’agent permet à un assistant d’agir, de voir le résultat et de décider de la suite.**

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 520" role="img" aria-labelledby="loop-title loop-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="loop-title">Observer, choisir, agir, vérifier, et savoir quand s’arrêter</title>
<desc id="loop-desc">Un diagramme de flux tourne dans le sens des aiguilles d’une montre : Observer, Choisir, Agir, Vérifier. Vérifier revient à Observer quand il reste du travail. Une autre flèche mène de Vérifier à S’arrêter ou demander quand la tâche est finie, bloquée ou que le budget est épuisé.</desc>
<defs><marker id="loop-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0L10 5 0 10Z" fill="#4b617e"/></marker></defs>
<rect width="760" height="520" rx="20" fill="#f0f5fb"/>
<g fill="none" stroke="#4b617e" stroke-width="4" marker-end="url(#loop-arrow)"><path d="M298 100H460"/><path d="M586 150V238"/><path d="M464 290H302"/><path d="M176 240V153"/><path d="M176 342V414"/></g>
<g stroke-width="3"><rect x="54" y="48" width="244" height="100" rx="23" fill="#d7eaff" stroke="#3377b9"/><rect x="464" y="48" width="244" height="100" rx="23" fill="#fce9b6" stroke="#9a701b"/><rect x="464" y="242" width="244" height="100" rx="23" fill="#dfd9ff" stroke="#7760b5"/><rect x="54" y="242" width="244" height="100" rx="23" fill="#cff3e4" stroke="#29836a"/><rect x="54" y="419" width="652" height="68" rx="20" fill="#fff" stroke="#4b617e"/></g>
<g font-family="system-ui,sans-serif" text-anchor="middle" fill="#173452"><g font-size="28" font-weight="700"><text x="176" y="90">1. OBSERVER</text><text x="586" y="90">2. CHOISIR</text><text x="586" y="285">3. AGIR</text><text x="176" y="285">4. VÉRIFIER</text></g><g font-size="20"><text x="176" y="122">Que vois-je ?</text><text x="586" y="122">Et ensuite ?</text><text x="586" y="317">Utiliser un outil.</text><text x="176" y="317">Qu’est-ce qui a changé ?</text><text x="380" y="199">Encore du travail ? On repart.</text><text x="428" y="389">Fini, bloqué ou à la limite ?</text><text x="380" y="461" font-size="24" font-weight="700">STOP, ou demander à quelqu’un.</text></g></g>
</svg>
<figcaption>Un schéma pédagogique, pas une architecture logicielle imposée. Les implémentations réelles peuvent fusionner ces étapes. L’essentiel est de réinjecter le résultat dans la décision suivante.</figcaption>
</figure>

## Retour à la très sérieuse mission sandwich

La première petite étape de Pip consiste à ouvrir le pot de confiture.

**Agir :** Tourner le couvercle.

**Vérifier :** Le couvercle n’a pas bougé.

C’est là que ça devient intéressant. Pip ne doit pas faire comme si le pot était ouvert simplement parce que l’ouvrir faisait partie du plan.

Et Pip ne doit pas non plus continuer à tourner jusqu’à ce que le soleil devienne un raisin sec.

Pip pourrait essayer une autre solution autorisée, ou dire : « Tu peux m’aider avec ce couvercle ? » Demander de l’aide est un résultat utile, pas un échec à la taille d’un robot.

Une fois le pot ouvert, Pip peut étaler la confiture, assembler le pain et comparer le résultat à votre demande.

Deux tranches ? De la confiture dedans ? Dans une assiette ? Parfait.

Un pot en équilibre sur une miche de pain ? Créatif. Mais ce n’est pas un sandwich.

## Et l’IA, dans tout ça ?

Notre histoire de cuisine est pour de faux. Au lieu de manipuler du pain, les outils d’un agent logiciel peuvent lire un fichier, chercher dans une page, modifier un document ou lancer un test.

Dans un agent d’IA, un modèle de langage peut aider à choisir l’étape suivante. Le logiciel qui l’entoure exécute les appels d’outils autorisés et renvoie leurs résultats. Le modèle a ensuite un nouveau tour avec ces informations.

Pensez à trois rôles différents :

| Élément | La cuisine imaginaire de Pip | Version logicielle |
| --- | --- | --- |
| Objectif | Faire un sandwich à la confiture | Réparer un lien cassé |
| Décideur | Choisir la prochaine petite étape | Le modèle propose une action |
| Outil | Mains et cuillère | Lecteur de fichiers, éditeur ou navigateur |
| Observation | Le couvercle est toujours fermé | L’outil renvoie une erreur ou un résultat |
| Notes de travail | Pot ouvert ; pain prêt | Historique et résultats pertinents de la tâche |
| Vérification finale | Le sandwich demandé est prêt | Vérifier que le lien visé fonctionne |

**Qu’un modèle suggère une action ne veut pas dire que cette action a lieu.** Et qu’une action ait lieu ne veut pas automatiquement dire que l’objectif est atteint.

« J’ai enregistré le fichier » et « j’ai enregistré le bon fichier avec le bon contenu » sont deux affirmations différentes. C’est à l’étape de vérification que cette différence compte.

## Une petite aventure : l’image manquante

Imaginons que vous demandiez à un assistant logiciel de réparer une image manquante sur une page web.

Une boucle utile pourrait ressembler à ceci :

1. **Observer :** Lire la page et repérer le chemin de l’image.
2. **Choisir :** Vérifier si l’image référencée existe.
3. **Agir :** Examiner les fichiers concernés.
4. **Vérifier :** La page demande `cat.png`, mais le fichier s’appelle `cat.jpg`.
5. **Refaire un tour :** Mettre à jour la référence, puis vérifier que la page charge bien l’image voulue.
6. **S’arrêter :** Rendre compte de la modification et des vérifications réellement effectuées.

Si l’image n’apparaît toujours pas, « j’ai modifié la page » ne suffit pas. Le résultat doit guider l’étape suivante.

Remarquez ce qui en fait une boucle : **la prochaine action dépend de ce que l’action précédente a révélé.** Il ne s’agit pas simplement de refaire la même chose en boucle.

## Chaque tour améliore-t-il les choses ?

Non. Plus d’activité ne signifie pas automatiquement plus de progrès.

Voici un graphique inventé pour la mission sandwich de Pip. On donne à Pip un point par étape franchie : pot ouvert, confiture étalée, sandwich assemblé et demande finale vérifiée.

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 450" role="img" aria-labelledby="graph-title graph-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="graph-title">Un graphique imaginaire de progression du sandwich</title>
<desc id="graph-desc">Sur six tentatives, les étapes franchies sont zéro, zéro, un, deux, trois et quatre. Les deux premières tentatives n’avancent pas, car le pot est coincé. Ces chiffres inventés illustrent la boucle de rétroaction, pas une performance mesurée d’agent.</desc>
<rect width="760" height="450" rx="20" fill="#f0f5fb"/>
<g font-family="system-ui,sans-serif" fill="#173452"><text x="48" y="42" font-size="23" font-weight="700">Progresser, ce n’est pas s’agiter.</text><text x="48" y="73" font-size="18">Étapes franchies · exemple inventé, pas un benchmark</text></g>
<g stroke="#c2cedd" stroke-width="1"><path d="M95 335H690M95 280H690M95 225H690M95 170H690M95 115H690"/></g>
<path d="M95 105V345H700" fill="none" stroke="#4b617e" stroke-width="3"/>
<polyline points="115,335 225,335 335,280 445,225 555,170 665,115" fill="none" stroke="#227657" stroke-width="5" stroke-linejoin="round"/>
<g fill="#227657" stroke="#fff" stroke-width="3"><circle cx="115" cy="335" r="8"/><circle cx="225" cy="335" r="8"/><circle cx="335" cy="280" r="8"/><circle cx="445" cy="225" r="8"/><circle cx="555" cy="170" r="8"/><circle cx="665" cy="115" r="8"/></g>
<g font-family="system-ui,sans-serif" font-size="20" fill="#173452" text-anchor="middle"><text x="68" y="341">0</text><text x="68" y="286">1</text><text x="68" y="231">2</text><text x="68" y="176">3</text><text x="68" y="121">4</text><text x="115" y="375">1</text><text x="225" y="375">2</text><text x="335" y="375">3</text><text x="445" y="375">4</text><text x="555" y="375">5</text><text x="665" y="375">6</text><text x="390" y="418">Tentatives</text></g>
<g font-family="system-ui,sans-serif" font-size="19" fill="#173452"><text x="116" y="292">Couvercle coincé !</text><text x="326" y="317">L’aide a marché.</text><text x="586" y="99">Vérifié !</text></g>
</svg>
<figcaption>Données imaginaires : 0, 0, 1, 2, 3, 4 étapes franchies. Le travail réel peut stagner, reculer ou se révéler impossible avec les outils disponibles.</figcaption>
</figure>

Le palier plat compte. Si rien ne change, l’assistant doit le remarquer, et non se féliciter du nombre de fois où il a essayé.

Pour les grands, cela soulève des questions utiles : A-t-on appris quelque chose ? L’état a-t-il changé ? Répète-t-on la même action ratée ? Une nouvelle tentative vaut-elle ce qu’elle coûte ?

Pour tous les autres : **si la porte dit TIREZ, pousser plus fort n’est pas une stratégie.**

## Donnez à l’assistant une clôture, pas la planète entière

Une conception d’agent raisonnable demande plus qu’un bouton « recommencer ».

- **Une ligne d’arrivée claire.** « Trouve trois photos de manchots » est plus facile à vérifier que « rends tout génial ».
- **Des autorisations adaptées.** Pouvoir rédiger un e-mail ne devrait pas automatiquement vouloir dire pouvoir l’envoyer.
- **Un budget d’arrêt.** Limitez les tentatives, le temps ou les dépenses. Une tâche bloquée ne doit pas devenir une tâche sans fin.
- **Un moyen de demander.** Une information manquante, un accès manquant ou un choix lourd de conséquences peuvent nécessiter une personne.
- **Des vérifications honnêtes.** Utilisez des preuves adaptées à l’objectif. Ne transformez pas « l’outil a répondu » en « tout est correct ».

Ce sont des principes de conception, pas la promesse que chaque produit les applique. Une boucle ne rend pas un système sûr ou fiable par magie.

Dans la cuisine de Pip : faire le sandwich, ne pas commander un camion rempli de confiture, et demander avant d’utiliser les appareils des grands.

## Une boucle d’agent, est-ce la même chose qu’un script ?

Pas forcément, mais la frontière n’est pas « les scripts sont bêtes, les agents sont malins ». Les scripts peuvent eux aussi avoir des boucles, des conditions et d’excellentes vérifications.

La distinction à surveiller, c’est **la manière dont l’action suivante est choisie**. Dans un flux de travail figé, le développeur a tracé les chemins à l’avance. Dans une boucle d’agent pilotée par un modèle, le modèle peut choisir parmi les actions disponibles en fonction de la tâche et des dernières observations. Les systèmes réels peuvent mélanger les deux approches.

Pour une tâche prévisible, un petit script peut être exactement ce qu’il faut. Pas besoin d’un robot philosophe pour sonner une cloche à midi.

Pour une tâche aux obstacles inconnus, choisir l’étape suivante à partir d’éléments tout frais peut être utile. Cette souplesse rend aussi les limites et la vérification indispensables.

## La version aimant de frigo

Une boucle d’agent, c’est :

> Essayer une étape utile. Voir ce qui s’est passé. Tirer parti de ce qu’on a appris. Recommencer seulement tant que ça a du sens.

Ce n’est pas de la magie. Ce n’est pas une garantie. Ce n’est pas « continuer indéfiniment ».

C’est une façon de relier **un objectif, une action et le résultat réel**, encore et encore, jusqu’à ce que l’assistant ait terminé ou doive s’arrêter.

Pip l’expliquerait plus simplement :

**« Regarde. Essaie. Vérifie. Et ne dis pas sandwich tant qu’il n’y a pas de sandwich. »**
