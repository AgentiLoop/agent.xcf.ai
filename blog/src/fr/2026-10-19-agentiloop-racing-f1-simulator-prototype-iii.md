---
title: AgentiLoop Racing, Prototype III : un simulateur de F1 dans votre navigateur
description: AgentiLoop Racing est un simulateur de course de monoplaces qui tourne dans le navigateur, créé avec Agent! en Three.js. Il offre une physique à 240 Hz, 18 circuits réels, un plateau de concurrents pilotés par l'IA, des arrêts aux stands, des gommes de pneus, du carburant, l'ERS et le DRS. Jouez sur f1.gokart.games.
tags: Showcase, JavaScript
---
<figure style="margin:2rem 0">
<img src="/agentiloop-racing-og.jpg" alt="AgentiLoop Racing : une monoplace en piste dans le simulateur du navigateur." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>AgentiLoop Racing, Prototype III. Chaque voiture de la grille est un modèle RB22 de 2026, repeint à ses propres couleurs et aux noms de ses sponsors.</figcaption>
</figure>

**Jouez dès maintenant : [f1.gokart.games](https://f1.gokart.games).** Pas de téléchargement, pas d'installation. Il faut un navigateur compatible WebGL, et on joue au clavier ou avec une manette Xbox (ou une autre manette standard).

AgentiLoop Racing est un simulateur de course façon F1 écrit en JavaScript pur et Three.js. Le premier commit, un modèle de véhicule déterministe à quatre roues, a été poussé le soir du 16 octobre. Trois jours et 109 commits plus tard, il fait courir un plateau complet d'IA sur 18 circuits réels, avec arrêts aux stands, gommes de pneus, carburant, ERS et DRS, un son moteur généré à partir de la physique et une caméra cockpit dont les rétroviseurs montrent les voitures derrière vous. C'est Agent! qui l'a écrit, un petit commit testé à la fois.

Une précision honnête d'emblée, la même que dans le README : c'est un **prototype, pas un simulateur de Formule 1 validé**. Les paramètres de la voiture sont des hypothèses illustratives, pas des données de F1 mesurées.

## La physique d'abord

Le projet a commencé comme un banc d'essai physique, et la 3D est venue ensuite. `physics.mjs` fait avancer la voiture à une fréquence fixe de **240 Hz**. Chaque roue a sa propre inertie et son propre glissement, et chaque pneu a une enveloppe d'adhérence qui va de l'adhérence maximale à la glisse, avec relaxation de l'angle de dérive, température et usure. La caisse suspendue prend du roulis, du tangage et s'écrase sous la charge aérodynamique, et on le voit sur la voiture 3D. La boîte de vitesses est automatique ou à palettes, et il y a une marche arrière sécurisée pour quand vous vous retrouvez face à un mur.

Le groupe propulseur est lui aussi modélisé. Le carburant est embarqué comme une vraie masse, si bien que la voiture s'allège à mesure qu'elle le brûle. L'hybride délivre jusqu'à 120 kW au-dessus de 100 km/h, dans la limite de 4 MJ par tour, et récupère de l'énergie au freinage.

La suite de tests repose sur le test runner intégré de Node et rien d'autre : `node --test` exécute aujourd'hui 158 tests, tous réussis. Ils vérifient par exemple qu'une voiture à pleins gaz ne traverse jamais un mur, et que le modèle 3D ne touche le sol qu'avec ses pneus et son patin.

## 18 circuits réels

<figure style="margin:2rem 0">
<img src="/agentiloop-racing-monza.jpg" alt="AgentiLoop Racing : une course à Monza contre le plateau de l'IA." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Une course à Monza. Le panneau de chronométrage, le classement et la mini-carte sont mis à jour en direct pendant la course.</figcaption>
</figure>

En plus d'un circuit d'essai fictif dans un stade, il y a 18 circuits réels, de Bahrain à Miami, dont Monza, Silverstone, Spa et Monaco, avec des tracés construits à partir de positions réelles des voitures. Les données réelles ont réglé le reste :

- **Les zones de DRS** proviennent de la télémétrie de course 2024 (OpenF1) : là où les pilotes ouvraient et fermaient réellement le volet. Monaco n'a qu'une zone, sur la ligne droite des stands.
- **L'adhérence a été calibrée sur des vitesses réelles en virage.** Sur les 18 circuits, l'écart entre les tours du pilote automatique et les meilleurs tours réels en course est passé de 17,9 % à 5,8 %. À Monaco, le tour du pilote automatique est passé de 84,2 s à 74,4 s, contre 73,9 s en réalité.
- **Les virages serrés ont été élargis** jusqu'à un rayon minimal de 15 m, pour que les voitures puissent passer Ste Devote à Monaco.
- **Chaque circuit a une voie des stands** le long de la ligne droite de départ et d'arrivée, avec une limite de 80 km/h et un stand pour chaque voiture.

<figure style="margin:2rem 0">
<img src="/agentiloop-racing-monaco.jpg" alt="AgentiLoop Racing : une course à Monaco." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Monaco, en course contre le plateau de l'IA.</figcaption>
</figure>

## Courir contre l'IA

Un circuit réel s'ouvre en contre-la-montre en solo ; appuyez sur **O**, ou ajoutez `?race` à l'URL, pour affronter le plateau. Le départ, ce sont cinq feux rouges, un par seconde, puis une attente aléatoire avant qu'ils s'éteignent. Bougez de plus d'un demi-mètre trop tôt et c'est une pénalité de 5 secondes pour départ anticipé. Tant que les feux sont allumés, les touches **1–5** vous placent dans la voiture de cette position sur la grille.

Les voitures de l'IA suivent la trajectoire idéale, s'aspirent mutuellement dans les lignes droites, sortent de l'aspiration, utilisent le DRS quand elles sont à moins d'une seconde au point de détection, et plongent à l'intérieur au freinage. Dans le commit qui a réglé les dépassements, les courses de 3 tours sur les 18 circuits sont passées de 16 dépassements à 34, et de 8 contacts à aucun. Une voiture qui se retrouve coincée contre une barrière enclenche la marche arrière, recule le long d'une trajectoire vérifiée pour éviter le trafic et les murs, puis reprend la piste.

Les règles de course s'appliquent. Chaque voiture classée doit utiliser deux gommes de pneus, vous devez donc vous arrêter une fois sous peine de disqualification. **B** demande à l'équipe des tendres, des médiums ou des durs. Un excès de vitesse dans la voie des stands, et c'est +5 s.

Chaque session commence en pilote automatique : la voiture roule toute seule jusqu'à ce que vous preniez le relais. Appuyez sur **P**, touchez une manette ou changez de rapport, et elle est à vous.

## La voiture et le cockpit

Chaque voiture de la grille utilise un modèle RB22 de 2026 réalisé par Tyler_Dave (CC BY 4.0, sur Sketchfab). Au chargement, `rb22.mjs` le repeint aux couleurs de chaque voiture et y projette les noms des sponsors du projet et un numéro de course. De près, chaque pièce du modèle est subdivisée et lissée, avec des versions moins détaillées plus loin.

Appuyez sur **C** pour le cockpit. L'œil du pilote est fixé sur la caisse suspendue, si bien que le roulis, le tangage et les mouvements verticaux font bouger la vue, et la tête bouge un peu avec les forces g. Les rétroviseurs affichent la scène reflétée à travers chaque miroir, sans vos propres pneus arrière, pour que vous voyiez la piste et les voitures derrière vous.

Le son est lui aussi synthétisé à partir de la physique : une note d'allumage de V6 qui suit le régime, le sifflement du turbo, le crissement des pneus selon le glissement et un bruit du vent qui augmente avec la vitesse.

<figure style="margin:2rem 0">
<img src="/agentiloop-racing-spa.jpg" alt="AgentiLoop Racing : un contre-la-montre à Spa-Francorchamps." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Le contre-la-montre de Spa.</figcaption>
</figure>

## Regardez-le

<figure style="margin:2rem 0">
<div style="position:relative;padding-top:56.25%;border-radius:20px;overflow:hidden">
<iframe src="https://www.youtube-nocookie.com/embed/2RluAIH3iQw?rel=0&amp;modestbranding=1&amp;color=white" title="AgentiLoop Racing — F1 simulator built with AgentiLoop.ai in Three.js" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="position:absolute;inset:0;width:100%;height:100%;border:0"></iframe>
</div>
</figure>

## Essayez-le

- [Une course à Monza](https://f1.gokart.games/?track=monza&race)
- [Le contre-la-montre de Spa](https://f1.gokart.games/?track=spa)
- [Une course de 5 tours à Spa en pneus tendres](https://f1.gokart.games/?track=spa&race&laps=5&tyre=soft)

Le code source se trouve sur [AgentiLoop/F1](https://github.com/AgentiLoop/F1). Il n'a aucune dépendance npm ni bundler : Three.js est inclus dans le dépôt, donc `python3 -m http.server` dans le dossier suffit pour le lancer en local. Le site lui-même est un Cloudflare Worker qui sert le dépôt sous forme de fichiers statiques.

*AgentiLoop Racing est un projet indépendant, sans affiliation avec la Formule 1, la FIA ni aucune écurie. Les modèles 3D conservent leurs propres licences ; voir `models/CREDITS.md` dans le dépôt.*
