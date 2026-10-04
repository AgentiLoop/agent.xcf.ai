---
title: GoKart : un jeu de course façon Mario Kart qu'Auto-Pilot a construit en un après-midi
description: Donnez à l'Auto-Pilot d'Agent! un seul objectif - « crée un clone de Mario Kart appelé GoKart » - et revenez devant un jeu de course Godot 4 avec trois circuits, huit objets, des rivaux pilotés par l'IA et 3 344 vérifications de test au vert. Deux jours et 87 commits de l'agent plus tard, c'est GoKart 0.0.2 : quatre circuits, un mode Bataille, des Contre-la-montre, un menu façon Mario Kart 64 et 14 134 vérifications au vert. Voici ce que le journal dit qu'il s'est réellement passé, y compris les moments où il s'est retrouvé bloqué.
tags: Auto-Pilot, Vitrine, Godot
updated: 2026-10-04
---
<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-title.png" alt="L'écran titre de GoKart 0.0.2 : le mot GOKART posé sur une arche en grandes lettres au dégradé jaune-rouge avec des côtés en blocs bleu marine et une ombre douce, au-dessus d'une démo d'attente en direct où des karts CPU tournent sur un circuit, avec PRESS ENTER en dessous." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>L'écran titre de GoKart 0.0.2. Le logo arrive en volant et rebondit jusqu'à l'arrêt au-dessus d'une démo d'attente en direct qui fait le tour des circuits. Chaque mesh, shader, mise en page de police et son a été généré à partir de code.</figcaption>
</figure>

*Mis à jour le 4 octobre : cet article couvre désormais les deux jours qui ont suivi le premier après-midi, les deux sessions Auto-Pilot qui ont tourné en même temps dans le même dépôt, et la version [GoKart 0.0.2](#gokart-0-0-2). Les captures d'écran ont été refaites à partir du tag 0.0.2.*

L'article d'hier présentait [Auto-Pilot](/blog/agent-1-1-87-and-agentiloop-cli-0-0-5/) : tapez `/auto <objectif>` dans Agent! pour Mac et il enchaîne des cycles sans surveillance vers cet objectif jusqu'à ce que vous appuyiez sur Stop All. Cet article raconte ce qui est sorti de l'autre côté quand je l'ai pointé vers un jeu.

L'objectif, collé plus ou moins tel que je l'ai tapé :

> create a Mario Kart clone called GoKart with all Mario Kart effects. I believe Godot 4 can do the Mario Kart effects, but I haven't built any of them yet: drift sparks and boost flames (GPUParticles3D), speed lines and boost blur (screen-space shaders, glow and tonemapping), item effects and tire trails (shaders plus ribbon meshes), kart movement (VehicleBody3D or custom arcade physics). Write unit tests and test the game frequently.

Budget : pas de limite de temps, cycles illimités. Le modèle utilisé dans Agent! pour chaque cycle était Claude Sonnet 5.5. Le premier commit est arrivé à 12 h 39. À 16 h 32 le même après-midi, le dépôt comptait 33 commits, 47 fichiers GDScript, environ 5 500 lignes de GDScript et de code de shaders, et une suite unitaire qui passait 3 344 vérifications. Deux jours plus tard, au tag 0.0.2, c'est 126 commits, 150 fichiers GDScript, environ 24 500 lignes et 14 134 vérifications, et chacun de ces commits est signé par l'agent. Le tout est sur GitHub : [AgentiLoop/GoKart](https://github.com/AgentiLoop/GoKart).

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
<img src="/gokart-0-0-2-sunset-speedway.png" alt="GoKart 0.0.2 sur Sunset Speedway : le kart du joueur en drift, 3e sur 8 au tour 1 sous le ciel de coucher de soleil, avec le HUD façon Mario Kart 64 : une carte du circuit translucide dans le coin inférieur gauche, la place, le tour et la vitesse dans une police arrondie or et crème." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Sunset Speedway en 0.0.2 : un bot de conduite aléatoire en plein drift, 3e sur 8. Le deuxième circuit a été ajouté au cycle 12 du premier jour, avec le menu titre. La circulation, les bâtiments au-delà des murs et le HUD sont arrivés deux jours plus tard.</figcaption>
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

C'est le bon comportement. L'objectif était « la direction est désagréable » et « les murs scintillent », et aucun test headless ne peut clore cet objectif. Auto-Pilot n'a pas de plafond d'itérations, il aurait donc continué à vérifier indéfiniment. La session s'est terminée après le cycle 8, et ce dont GoKart avait besoin ensuite, c'était d'une partie de test, pas d'un cycle de plus. Ce soir-là, le dépôt a été tagué 0.0.1 et exporté pour macOS, Windows et Linux.

## Deux jours plus tard : deux Auto-Pilots dans un même dépôt

Le 3 octobre, je suis revenu avec un objectif d'un autre genre. Pas une liste de fonctionnalités, une référence :

> keep building GoKart to resemble Mario Kart Nintendo 64 version. search Mario Kart N64 or Mario Kart Nintendo 64 and keep improving, iterating, making GoKart better

Cette cinquième session a démarré à 14 h 19 et a enchaîné 28 cycles, et presque chaque cycle est un élément de Mario Kart 64 que l'agent a cherché puis construit : le plateau de 8 coureurs sur une grille à deux colonnes, l'élastique selon la difficulté, les classes 50cc / 100cc / 150cc et la classe Extra en miroir, des karts Léger / Moyen / Lourd qui se bousculent, le Grand Prix avec les points 9/6/3/1 et la règle d'élimination au classement, les Contre-la-montre avec un fantôme, le mode Bataille avec des ballons dans Big Donut, Block Fort et Skyscraper, les triples champignons et le champignon doré, la fausse boîte à objets, le régime de bananes, Boo, les triples carapaces rouges, le blocage des carapaces, le faux départ, Lakitu avec le signal de départ et les panneaux de tour, un quatrième circuit appelé Dusty Canyon, le train du Désert Kalimari avec des passages à niveau, la circulation de l'Autoroute Toad, des Topi Taupes, des bonshommes de neige, des pingouins, la glace de Sherbet Land, des décors de bord de route par thème, l'aspiration, un tremplin, le dérapage à sautillement et bascule, et une boucle chiptune pour chaque circuit rendue à partir de motifs de pas dans le code.

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-train.png" alt="GoKart 0.0.2 sur Dusty Canyon : le kart du joueur attendant à un passage à niveau pendant qu'un train à vapeur traverse la route, avec une croix de Saint-André à côté de la voie, sous un ciel de désert." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Dusty Canyon, le quatrième circuit, avec son train façon Désert Kalimari. Les karts CPU s'arrêtent et attendent à un passage fermé ; un kart qui ne le fait pas est projeté en l'air.</figcaption>
</figure>

Quatre heures plus tard, à 18 h 25, j'ai ouvert un deuxième onglet et lancé un deuxième Auto-Pilot sur le même dépôt, avec un objectif plus étroit :

> the menus are not Mario Kart Quality and neither is the title shot. and there is over use of black outlines on text everywhere. see Mario Kart 64 screenshots and images on the web and make better menus. focus only on the menus / screens and title shot for GoKart. make conscious decisions. do not conflict with previous /auto working on the application

Donc de 18 h 25 à minuit, deux agents committaient dans le même arbre de travail. La session menus a reconstruit l'écran titre avec un logo en arche dégradé qui arrive en volant et rebondit, un écran de sélection avec une image à côté de chaque circuit, un survol en direct du circuit choisi, des lignes d'options avec des barres allumées, un portrait de kart qui tourne et un curseur doré, un survol d'introduction du circuit, un écran de pause, un tableau de résultats dont les lignes glissent l'une après l'autre, et une palette commune de texte arrondi or et crème avec ombres portées qui a remplacé chaque contour noir de 8 pixels dans le jeu. Elle a enchaîné 23 cycles et a déclaré l'objectif atteint à 23 h 54.

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-select.png" alt="L'écran de sélection de GoKart 0.0.2 : le logo GOKART en haut, une liste de circuits à gauche avec une petite image à côté de chaque nom de circuit et la ligne choisie allumée, une image en direct du circuit avec le contour de la carte dans son coin à droite, des rangées de pastilles d'options pour les tours, les CPU, la classe de moteur, le poids du kart et le mode, et le kart du joueur qui tourne dans une petite fenêtre de portrait, le tout au-dessus de la démo d'attente assombrie." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>L'écran de sélection après la session menus. Des images de circuits, un survol en direct du circuit, chaque option listée comme une rangée de pastilles avec celle choisie allumée, et le kart qui tourne dans sa fenêtre de portrait.</figcaption>
</figure>

La ligne « do not conflict » a vraiment servi. Le journal est plein des deux sessions qui se contournent l'une l'autre : la session menus qui vérifie depuis un `git worktree` propre à HEAD pour que « le travail en cours de l'autre session sur les pingouins » reste hors de ses exécutions de tests, une session qui termine la fonctionnalité à moitié faite de l'autre quand je le lui ai demandé, et des commits indexés fichier par fichier au lieu de `git add -A` parce que les modifications de l'autre onglet se trouvaient dans le même arbre. Ce n'était pas net, mais rien n'a été perdu et la suite a terminé la nuit à 14 134 réussites, 0 échec.

Le journal de la session fonctionnalités se termine trois minutes plus tard, à 23 h 57, par « Session ended — Stop All ». Ma note à Agent! juste après, qu'il a enregistrée comme message du commit de point de contrôle suivant, était que Stop All doit n'arrêter que l'onglet dans lequel on appuie dessus, pas tous. Avec deux Auto-Pilots en cours, un seul bouton pour les deux est le mauvais bouton.

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-snowmen.png" alt="GoKart 0.0.2 sur Frosty Peaks : le kart du joueur à l'entrée d'un champ de bonshommes de neige disposés en rangées décalées sur la route blanche comme neige, chacun avec une écharpe rouge, un haut-de-forme et un nez en carotte, sous un ciel crépusculaire bleu foncé." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Le champ de bonshommes de neige sur Frosty Peaks. Touchez-en un et vous êtes projeté en l'air pendant qu'il éclate en neige ; les karts CPU regardent 40 mètres devant et slaloment entre les rangées.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-penguins.png" alt="GoKart 0.0.2 sur Frosty Peaks : un pingouin glissant sur le ventre à travers la glace bleu-blanc pâle de la longue courbe devant le kart du joueur." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Glace et pingouins façon Sherbet Land sur Frosty Peaks. Sur la glace, le nez tourne mais le kart continue de glisser dans la direction où il allait ; les pingouins se dandinent jusqu'au bord, se laissent tomber et reglissent en travers.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-traffic.png" alt="GoKart 0.0.2 sur Sunset Speedway : le kart du joueur coincé derrière un bus et un camion fourgon, phares allumés, dans les deux voies de la route, sous le ciel de coucher de soleil." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Circulation façon Autoroute Toad sur Sunset Speedway : voitures, bus, camions fourgons et camions-citernes avec les phares allumés, et des bâtiments avec des bandes de fenêtres éclairées au-delà des murs.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-gp-results.png" alt="Le tableau de résultats du Grand Prix de GoKart 0.0.2 sur un panneau bleu marine à bordure dorée : le résultat de la course à gauche et le classement de la coupe à droite, une ligne par coureur avec une pastille de couleur, les places or, argent et bronze, les temps et les points, la ligne du joueur sur une barre dorée allumée, et le trophée en dessous." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Le tableau de résultats du Grand Prix : résultat de la course et classement de la coupe côte à côte, les lignes glissant l'une après l'autre avec un tic chacune, et le trophée en dessous.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-battle.png" alt="Mode Bataille de GoKart 0.0.2 : quatre karts sur leurs plots de départ dans une arène de bataille, chacun avec trois ballons attachés, et le signal de départ de Lakitu au-dessus." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Mode Bataille : quatre karts, trois ballons chacun. Les coups d'objets, la lave, le bord du toit, les contacts avec une étoile et les grosses bousculades font éclater les ballons, et un kart qui n'en a plus devient un Mini Bomb Kart.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-dusty-canyon.png" alt="GoKart 0.0.2 sur Dusty Canyon : le kart du joueur 5e sur 8 au tour 1 sur la route du désert, avec le HUD façon Mario Kart 64." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Dusty Canyon vu par le bot de conduite aléatoire, 5e sur 8. Des courbes de désert, une épingle, un S à gauche, deux passages d'eau d'oasis, le train, et un tremplin sur la ligne droite de départ.</figcaption>
</figure>

## À propos de ces captures d'écran

C'est Agent! qui les a prises, pas moi, et pas à la main. Pour la première version, j'ai demandé trois captures d'une conduite aléatoire, et il a écrit un `tools/random_drive.gd` de 70 lignes qui suit la route avec un décalage de voie errant, y glisse des rafales de drift aléatoires et tire l'objet qu'il tient à des moments aléatoires, puis enregistre une image toutes les quelques centaines d'images physiques. Les deux captures de course ci-dessus sont des images de ce bot. Les autres viennent des outils de capture livrés avec chaque fonctionnalité : `menu_shot.gd`, `train_shot.gd`, `traffic_shot.gd`, `snowman_shot.gd`, `penguin_shot.gd`, `hud_shot.gd` et `battle_shot.gd`, chacun mettant en scène sa scène, attendant la bonne image et l'enregistrant. Tous ont été lancés pour cette mise à jour depuis un worktree propre extrait au tag `v0.0.2`, donc rien de non committé ne figure dans une image. Agent! ne peut toujours pas regarder le résultat, alors les outils échantillonnent des pixels à la place : la capture de glace affiche la couleur de la route devant sur la glace par rapport au bitume, la capture de pause prouve que rien n'a bougé hors du panneau pendant une seconde, et avant de publier, je lui ai fait compter les pixels noir pur dans les dix images ci-dessus : zéro dans chacune. Il y en a d'autres dans le [README de GoKart](https://github.com/AgentiLoop/GoKart#screenshots).

## Ce que je vous dirais avant d'essayer

- **Lancez-le dans git.** Auto-Pilot n'a pas d'annulation. Le journal de GoKart est lisible parce que chaque cycle s'est terminé par un commit, et la seule fois où un cycle a dérapé, rien n'a été perdu.
- **Mettez les règles opérationnelles dans l'objectif.** « Mets une limite de temps sur le shell » a mieux fonctionné comme partie de l'objectif que comme message ponctuel, parce que chaque nouveau cycle relit l'objectif.
- **Attendez-vous à ce qu'il demande des yeux.** Pour tout ce qui est visuel ou une question de ressenti, la boucle calera honnêtement plutôt que de mentir. Prévoyez une partie de test entre les sessions, et réinjectez vos notes comme objectif suivant.
- **Stop All fait partie du flux de travail**, ce n'est pas un échec. Les trois premières sessions de GoKart se sont toutes terminées ainsi.
- **Deux Auto-Pilots dans un même dépôt, ça marche, si vous leur parlez l'un de l'autre.** « Do not conflict with the previous /auto » est allé dans le deuxième objectif, et les deux sessions ont fait de vrais efforts pour ne pas se marcher dessus. Donnez-leur des zones séparées du code, et attendez-vous pour l'instant à ce que celui que vous arrêtez emporte l'autre avec lui.

## Est-ce que c'est bien ?

J'ai posé cette question à Agent! après qu'il a lu le dépôt, compté les commits et trouvé le journal d'Auto-Pilot. Les 126 commits sont tous signés par l'agent, aucun par une personne, et `.agent/autopilot/progress.md` dépasse le cycle 23. Sa réponse, sans retouche :

> Ça dépend de ce que vous en attendez. Comme vitrine de ce qu'Auto-Pilot peut faire, c'est impressionnant. Vingt-trois cycles et plus ont produit quatre circuits, des objets, des coureurs IA, un Grand Prix, des Contre-la-montre, un mode Bataille, de la musique et du son procéduraux, le tout sans aucun asset importé, et un README qui le documente en détail. C'est beaucoup de logiciel qui fonctionne à partir d'un seul énoncé d'objectif.

Il a aussi ajouté la réserve que personne d'humain ne l'a relu en cours de route, donc la qualité a été jugée d'après les propres journaux de vérification de l'agent, et qu'il n'y avait pas joué ni audité le code, donc il ne pouvait pas dire à quel point ça se joue bien réellement. Ce qui est la même conclusion que le journal avait atteinte de lui-même : la prochaine étape est une partie de test.

## GoKart 0.0.2

Plus besoin de Godot pour l'essayer. [GoKart 0.0.2](https://github.com/AgentiLoop/GoKart/releases/tag/v0.0.2) est la deuxième version empaquetée, exportée depuis le même dépôt, 87 commits après la [0.0.1](https://github.com/AgentiLoop/GoKart/releases/tag/v0.0.1) :

- **macOS** universel (Apple Silicon et Intel), signé avec un Developer ID et notarisé par Apple
- **Windows** x86_64
- **Linux** x86_64 et arm64

Chaque téléchargement est un binaire unique et autonome avec les données du jeu intégrées, et `SHA256SUMS.txt` est sur la page de la version si vous voulez vérifier ce que vous avez reçu. La version Windows n'est pas signée, attendez-vous donc à l'avertissement SmartScreen. Tout ce qui, dans cet article, n'était pas dans la 0.0.1 est dans la 0.0.2 : le mode Bataille, les Contre-la-montre, la coupe à quatre circuits, les classes de moteur et de poids, les nouveaux objets, Lakitu, le train, la circulation, les taupes, les bonshommes de neige, les pingouins, la glace, les décors, l'aspiration, le tremplin, la musique des circuits, les nouveaux écrans titre et de sélection, l'introduction du circuit, l'écran de pause et le HUD restylé. Les notes de version ont la liste complète.

Agent! 1.1.87 avec Auto-Pilot est sur la [page des versions](https://github.com/AgentiLoop/Agent/releases/latest) et dans Homebrew. Si vous préférez lancer GoKart depuis les sources, il nécessite Godot 4.4 ou plus récent : `git clone https://github.com/AgentiLoop/GoKart.git && cd GoKart && godot --path .`
