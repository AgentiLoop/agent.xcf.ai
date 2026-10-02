---
title: GoKart : un jeu de course façon Mario Kart qu'Auto-Pilot a construit en un après-midi
description: Donnez à l'Auto-Pilot d'Agent! un seul objectif - « crée un clone de Mario Kart appelé GoKart » - et revenez devant un jeu de course Godot 4 avec trois circuits, huit objets, des rivaux pilotés par l'IA et 3 344 vérifications de test au vert. Voici ce que le journal dit qu'il s'est réellement passé, y compris les moments où il s'est retrouvé bloqué.
tags: Auto-Pilot, Vitrine, Godot
---
<figure style="margin:2rem 0">
<img src="/gokart-green-hills-drift.png" alt="GoKart sur le circuit Green Hills : vue en caméra de poursuite du kart du joueur en plein drift sur une route grise bordée de murs rayés rouge et blanc, sol vert et ciel bleu. Le HUD affiche la 1re place, les compteurs de tour et de temps et une mini-carte du circuit dans le coin inférieur gauche." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Green Hills, tour 1, en drift en première position. Chaque mesh, shader et son de cette image a été généré à partir de code.</figcaption>
</figure>

L'article d'hier présentait [Auto-Pilot](/blog/agent-1-1-87-and-agentiloop-cli-0-0-5/) : tapez `/auto <objectif>` dans Agent! pour Mac et il enchaîne des cycles sans surveillance vers cet objectif jusqu'à ce que vous appuyiez sur Stop All. Cet article raconte ce qui est sorti de l'autre côté quand je l'ai pointé vers un jeu.

L'objectif, collé plus ou moins tel que je l'ai tapé :

> create a Mario Kart clone called GoKart with all Mario Kart effects. I believe Godot 4 can do the Mario Kart effects, but I haven't built any of them yet: drift sparks and boost flames (GPUParticles3D), speed lines and boost blur (screen-space shaders, glow and tonemapping), item effects and tire trails (shaders plus ribbon meshes), kart movement (VehicleBody3D or custom arcade physics). Write unit tests and test the game frequently.

Budget : pas de limite de temps, cycles illimités. Le modèle utilisé dans Agent! pour chaque cycle était Claude Sonnet 5.5. Le premier commit est arrivé à 12 h 39. À 16 h 32 le même après-midi, le dépôt comptait 33 commits. Aujourd'hui, il contient 47 fichiers GDScript, environ 5 500 lignes de GDScript et de code de shaders, et une suite unitaire qui passe 3 344 vérifications. Le tout est sur GitHub : [AgentiLoop/GoKart](https://github.com/AgentiLoop/GoKart).

## Ce que fait Auto-Pilot, un cycle à la fois

Auto-Pilot tient un journal continu dans `.agent/autopilot/progress.md` à l'intérieur du projet, et chaque cycle y ajoute ce qu'il a fait, ce qu'il a supposé, ce qui reste et si quelque chose l'a bloqué. Ce journal est la source de tout ce qui suit. Je le cite plutôt que ma mémoire parce que le journal est plus honnête que moi.

Le **cycle 1** n'avait pas Godot sur la machine. Il a lancé `brew install --cask godot`, créé un lien symbolique vers le binaire, fait `git init`, et écrit `kart_physics.gd` comme un modèle pur sans dépendance à une scène : accélération, freinage, marche arrière, friction, direction, un drift verrouillé dans la direction où vous l'avez commencé, et trois niveaux de mini-turbo. Il a délibérément choisi une physique arcade maison plutôt que `VehicleBody3D`, et a dit pourquoi : « pour que le comportement façon Mario Kart soit facile à tester unitairement ». Onze tests, 17 vérifications, premier commit.

Le **cycle 2** a ajouté les effets que j'avais demandés nommément : des étincelles de drift en GPUParticles3D colorées selon le niveau de mini-turbo, des flammes d'échappement, des traces de pneus en ruban de mesh, et un shader en espace écran pour le flou radial du boost, les lignes de vitesse et un vignettage. 43 vérifications.

Le **cycle 3** a construit un circuit. Une boucle Catmull-Rom rééchantillonnée tous les 3 mètres, un ruban de route, des murs rayés rouge et blanc avec colliders, des plaques de boost avec un shader de chevrons défilants, huit checkpoints ordonnés et un compteur de tours qui refuse de compter les raccourcis ou les tours à contresens. L'un des nouveaux tests est un bot de poursuite qui boucle trois tours complets avec le vrai modèle physique. Il a terminé en 1:02.5. 90 vérifications.

Le **cycle 4** a ajouté des boîtes à objets avec un shader fresnel arc-en-ciel, une roulette, et les trois premiers objets : champignon, banane et une carapace verte qui ricoche sur les murs. Se faire toucher fait partir le kart en tête-à-queue pendant 1,2 seconde. 235 vérifications.

Puis il s'est retrouvé bloqué.

## Le moment où il s'est retrouvé bloqué

Le cycle suivant a commencé à ajouter des karts IA et une course de fumée headless, et n'est jamais revenu. La cause, trouvée à la session suivante, était une seule tabulation égarée à la ligne 115 de `main.gd` : une erreur de parsing qui faisait cracher des erreurs au script de fumée sans fin, sans limite de temps sur la commande shell qui l'exécutait.

J'ai appuyé sur **Stop All** et ouvert une nouvelle session avec le même objectif plus une note en majuscules que je ne reproduirai pas intégralement. En substance : *tu t'es retrouvé bloqué en testant la course de fumée, ne te bloque pas, mets une limite de temps sur le shell.*

Le premier cycle de la deuxième session a corrigé la tabulation, réduit l'anticipation de l'IA de 10 échantillons de route à 6 pour que l'IA arrête de couper les virages dans le mur intérieur, ajouté un limiteur de vitesse en virage, et enveloppé chaque exécution shell dans `perl -e 'alarm 100; exec @ARGV'`, parce que macOS est livré sans commande `timeout`. À partir de là, le journal dit « toutes les exécutions étaient derrière des limites perl alarm » à la fin de presque chaque cycle. Il a retenu la leçon du texte de l'objectif et a continué à l'appliquer.

Cette session a enchaîné 15 cycles en environ une heure et quart, et chacun est une fonctionnalité : compte à rebours de départ avec un boost de départ canon pour un accélérateur bien chronométré ; des pops de montée de niveau de mini-turbo et un flash en bord d'écran ; une mini-carte ; la carapace rouge à tête chercheuse et l'étoile ; un modèle de kart procédural avec des roues qui tournent, des roues avant qui braquent et un pilote dont la tête se tourne ; un éclair qui rétrécit tous les rivaux ; des triples carapaces qui orbitent autour du kart ; la carapace bleue à épines qui traque le leader le long de la route ; un écran de résultats avec des points ; un audio entièrement synthétisé sans fichier audio, de la boucle moteur au jingle d'arrivée ; un menu titre avec un deuxième circuit ; une option de nombre de tours ; un troisième circuit ; et un ronronnement moteur 3D positionnel sur chaque kart IA.

<figure style="margin:2rem 0">
<img src="/gokart-sunset-speedway.png" alt="GoKart sur le circuit Sunset Speedway : le kart du joueur à pleine vitesse sur un circuit sablonneux sous un ciel de coucher de soleil orange à violet. Le HUD affiche la 4e place, le tour 1, et le contour sur la mini-carte d'un long circuit avec une épingle." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Sunset Speedway, le deuxième circuit, ajouté au cycle 12 avec le menu titre. Plus long que Green Hills, avec une épingle et une chicane.</figcaption>
</figure>

## Le moment où il a été honnête

Ce que j'aime le plus dans le journal, c'est le motif des aveux. Agent! ne peut pas regarder un PNG, et il l'a dit, cycle après cycle :

> L'exécution de capture en mode fenêtré n'a enregistré aucune erreur, mais je ne peux pas voir les images, donc je n'ai pas regardé comment le circuit ou le HUD s'affichent.

> Je n'ai pas entendu les sons, et je n'ai pas lancé la course de fumée ni l'outil de capture.

> Je ne peux pas voir les images avec mes outils, donc cette revue nécessite une personne.

Alors il a testé ce qu'il pouvait : des vérifications de scène headless qui instancient la vraie scène et font des assertions sur l'état. Lancer l'éclair, confirmer que trois rivaux sont à l'échelle 0,5 et en train de tourner, et que les éclairs sont nettoyés ensuite. Tirer une carapace bleue sur une grille de départ serrée, confirmer l'explosion à l'image 12 et deux karts en tête-à-queue. Forcer le joueur à finir, confirmer que le pilote automatique confie le kart à un `AiDriver` et que le panneau de résultats affiche « 1st YOU ».

Une troisième session a calé de la même manière, cette fois derrière une alarme de 240 secondes bien trop généreuse, et je l'ai arrêtée après un cycle. Puis une personne a regardé. Cette personne, c'était moi, et l'objectif de la quatrième session était mes notes de test, légèrement remises en ordre :

> the UI needs to scale with the window. the UI should not be prone to the screen speed effects and blurry. Should be able to use cursor keys. it's not clear when power ups are released. the tops of the walls flicker. Little too hard to steer the kart. hard to keep up with the computer AI karts. maybe have AI difficulty levels Easy Medium and Hard.

Un cycle plus tard : un étirement canvas-items pour que l'UI suive la taille de la fenêtre, le HUD déplacé sur un calque canvas au-dessus de l'overlay d'effets de vitesse, les touches fléchées, Entrée et Ctrl pour les objets avec une indication à l'écran, une direction adoucie à l'entrée, une correction du z-fighting sur les rayures des murs (les segments rouges et blancs voisins se disputaient les mêmes pixels, alors les blancs ont été légèrement agrandis), du MSAA 4x, et Facile / Moyen / Difficile qui ramènent la vitesse maximale de l'IA à 0,72, 0,85 et 1,0. Les tests sont passés de 2 156 à 3 344 vérifications, en partie parce qu'il a aussi trouvé et corrigé une erreur de parsing préexistante dans `tests/test_items.gd` qui empêchait la suite de se charger.

## Le moment où il s'est arrêté de lui-même

Les cycles 2 à 8 de cette dernière session n'ont fait aucune modification de code. Chacun a relu le dépôt, relancé la suite, et écrit une variante du même paragraphe :

> Je n'ai pas pu voir le résultat à l'écran, donc je ne déclare pas l'objectif atteint. Quatre points ont encore besoin qu'un humain les essaie dans le jeu.

C'est le bon comportement. L'objectif était « la direction est désagréable » et « les murs scintillent », et aucun test headless ne peut clore cet objectif. Auto-Pilot n'a pas de plafond d'itérations, il aurait donc continué à vérifier indéfiniment. La session s'est terminée après le cycle 8, et ce dont GoKart avait besoin ensuite, c'était d'une partie de test, pas d'un cycle de plus.

<figure style="margin:2rem 0">
<img src="/gokart-frosty-peaks.png" alt="GoKart sur le circuit Frosty Peaks : le kart du joueur à pleine vitesse sur un circuit blanc comme neige sous un ciel crépusculaire bleu foncé. Le HUD affiche la 2e place, le tour 1, la vitesse en km/h et la mini-carte." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Frosty Peaks, ajouté au cycle 14 comme nouvelle entrée dans la bibliothèque de circuits. Les tests par circuit l'ont pris en compte automatiquement.</figcaption>
</figure>

## À propos de ces captures d'écran

C'est Agent! qui les a prises, pas moi, et pas à la main. J'ai demandé trois captures d'une conduite aléatoire, et il a écrit un `tools/random_drive.gd` de 70 lignes qui suit la route avec un décalage de voie errant, y glisse des rafales de drift aléatoires et tire l'objet qu'il tient à des moments aléatoires, puis enregistre une image toutes les quelques centaines d'images physiques. Il a tourné une fois par circuit, et les trois ci-dessus sont une image de chacun. Elles sont aussi dans le [README de GoKart](https://github.com/AgentiLoop/GoKart#screenshots).

## Ce que je vous dirais avant d'essayer

- **Lancez-le dans git.** Auto-Pilot n'a pas d'annulation. Le journal de GoKart est lisible parce que chaque cycle s'est terminé par un commit, et la seule fois où un cycle a dérapé, rien n'a été perdu.
- **Mettez les règles opérationnelles dans l'objectif.** « Mets une limite de temps sur le shell » a mieux fonctionné comme partie de l'objectif que comme message ponctuel, parce que chaque nouveau cycle relit l'objectif.
- **Attendez-vous à ce qu'il demande des yeux.** Pour tout ce qui est visuel ou une question de ressenti, la boucle calera honnêtement plutôt que de mentir. Prévoyez une partie de test entre les sessions, et réinjectez vos notes comme objectif suivant.
- **Stop All fait partie du flux de travail**, ce n'est pas un échec. Les trois premières sessions de GoKart se sont toutes terminées ainsi.

Agent! 1.1.87 avec Auto-Pilot est sur la [page des versions](https://github.com/AgentiLoop/Agent/releases/latest) et dans Homebrew. GoKart nécessite Godot 4.4 ou plus récent : `git clone https://github.com/AgentiLoop/GoKart.git && cd GoKart && godot --path .`
