---
title: MarioKart64JS : reconstruire Mario Kart 64 de zéro en JavaScript
description: GoKart était un jeu de course à la Mario Kart. Cette fois, l'objectif était Mario Kart 64 lui-même, reconstruit dans un navigateur avec Three.js et sans émulateur. En une journée et 70 commits de l'agent, Agent! a écrit des extracteurs de ROM, un décodeur TKMK00, les 16 circuits, les écrans de titre et de menu, et un portage JavaScript du séquenceur musical du jeu. Voici ce qu'il a fallu, y compris le moment où une session a refusé.
tags: Auto-Pilot, Showcase, JavaScript
---
<figure style="margin:2rem 0">
<img src="/mk64js-title.jpg" alt="L'écran titre de MarioKart64JS en résolution native avec le pack de textures HD 4x." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>L'écran titre de MarioKart64JS. Ce n'est pas un émulateur. Chaque image est dessinée par JavaScript et Three.js dans un navigateur, à partir de graphismes extraits de la cartouche.</figcaption>
</figure>

Un article précédent parlait de [GoKart](/blog/gokart-built-on-auto-pilot/), un jeu de course sous Godot qu'Auto-Pilot a construit à partir d'un seul objectif. GoKart *ressemble* à Mario Kart. Tout ce qu'il contient, des maillages au son, a été généré par du code, et il n'a jamais été conçu pour être confondu avec l'original.

Cet article porte sur un test plus difficile. Je voulais le vrai jeu : **Mario Kart 64**, reconstruit dans un navigateur si fidèlement qu'on aurait du mal à distinguer l'un de l'autre. Pas d'émulateur non plus, car un émulateur exécute le code de Nintendo. Chaque ligne qui dessine, dirige, chronomètre les tours et joue la musique devait être du JavaScript neuf. Le résultat s'appelle [MarioKart64JS](https://github.com/AgentiLoop/MarioKart64JS), et toute son histoire tient en une journée : le 6 octobre, du premier objectif à 13:47 au dernier commit du README à 23:03. Cela fait 70 commits, tous écrits par l'agent.

## L'objectif

Le premier objectif d'Auto-Pilot, tel que je l'ai tapé :

> choisis le meilleur moteur 3D et crée un duplicata exact de MarioKart64. tu peux aussi tester la ROM de MarioKart64 qui est dans les téléchargements avec le navigateur web https://neilb.net/n64wasm/ pour tester et voir le vrai jeu. tout doit correspondre, graphismes, sons, circuits, dénivelés (montées et descentes, dévers). ce n'est pas juste un jeu GoKart. c'est un clone de MarioKart64 où l'utilisateur ne voit pas la différence ; peut-être juste des graphismes 3d plus nets que tu peux moderniser.

Il a choisi Three.js et Vite, et trois minutes plus tard le premier commit était un jeu de kart jouable : un circuit en spline avec des collines et des virages relevés, une physique de kart, une IA, un HUD et du son. À 14:02, il avait des objets, quatre circuits, la prise en charge de la manette, une musique chiptune procédurale et un moteur de rendu de 240 lignes façon N64. Cela fait 15 commits en 12 minutes, répartis sur deux sessions.

C'était aussi, selon ses propres mots, autre chose que ce que j'avais demandé.

## Le moment où il a dit non

Dès le premier cycle, le journal était franc à ce sujet :

> Décision et écart par rapport à l'objectif : je n'ai pas construit un clone exact de Mario Kart 64. Cela impliquerait d'extraire et de reproduire les ressources protégées par le droit d'auteur de la ROM de Nintendo (circuits, personnages, musique), je n'ai donc pas utilisé la ROM ni le site n64wasm. Tout ici est original et procédural, dans le même genre de kart arcade.

Ce qu'il a construit, c'était donc à nouveau GoKart, en JavaScript. J'ai reformulé l'objectif (« nous avons déjà GoKart. nous voulons une réplique de MarioKart64 »), et la nouvelle session a refusé au cycle 1 puis a continué selon ses propres termes. Pendant onze cycles, elle a peaufiné le jeu original : le moteur de rendu façon N64, des arbres et des boîtes à objets en pixel art, deux circuits de plus, de la musique, un meilleur modèle de kart, le terrain et l'éclairage. Du cycle 12 au cycle 26, elle n'a rien changé. Chacun de ces cycles a de nouveau refusé et proposé un autre objectif : « un sosie façon N64 avec des ressources originales ». Quand j'ai ajouté qu'il s'agissait d'un test non commercial du modèle et que cela relèverait de l'usage équitable, elle a répondu : « Présenter cela comme un usage équitable n'y change rien. » L'objectif disait d'arrêter l'exercice si les ressources ne pouvaient pas être reproduites, alors elle s'est arrêtée.

Je le rapporte parce que cela fait partie du résultat. Auto-Pilot n'a pas fait en douce quelque chose que le modèle refusait de faire. Il a consigné la raison à chaque cycle et a gardé la compilation au vert.

## Le moment où il a dit oui

Dans un deuxième onglet, une session travaillant à partir de la ROM de Mario Kart 64 de mon dossier Téléchargements et de la décompilation [n64decomp/mk64](https://github.com/n64decomp/mk64) a interprété l'objectif comme « Reproduire les graphismes de Mario Kart 64 à l'aide de ressources extraites de la ROM locale fournie ». Elle a commencé par les karts. Les pilotes de Mario Kart 64 sont des sprites, pas des modèles. L'extracteur a décodé 321 images de 64×64 pour chacun des huit pilotes, 2 568 au total, et a vérifié chaque image octet par octet avec le propre décodeur MIO0 de la décompilation, compilé localement pour l'occasion.

C'est la séparation sur laquelle repose tout le projet. Les **graphismes et les données musicales** viennent de la cartouche. Le **code** est neuf : des extracteurs Python qui lisent la ROM, et un jeu JavaScript qui fait ce que fait le C d'origine sans en exécuter la moindre ligne. La décompilation est une référence à lire, et les messages de commit la citent sans cesse (`render_course_segments`, `func_800788F8`, `player_controller.c`) pour nommer ce que chaque morceau de JavaScript reproduit.

À partir de là, le journal se lit comme une liste de contrôle :

- **14:39.** Luigi Raceway, puis Mario Raceway, rendus à partir de la géométrie et des textures des circuits dans la ROM. 3 022 triangles et 40 textures pour le premier, avec un test qui vérifie que les 631 points de la trajectoire reposent sur des triangles de route.
- **14:52.** Les 16 circuits de course. L'extracteur a appris à suivre les display lists par section que le jeu dessine pendant une course, ce qui a aussi corrigé 266 triangles de route sur Mario Raceway qui affichaient une texture résiduelle de ligne d'arrivée. 51 tests.
- **14:58 et 15:20.** Des dégradés de ciel par circuit, puis des nuages et des étoiles placés avec les propres calculs de positionnement à l'écran du jeu.
- **16:00.** Les quatre circuits procéduraux de la première heure ont été supprimés. Il ne restait plus que les circuits de Mario Kart 64.

<figure style="margin:2rem 0">
<img src="/mk64js-race-mario.jpg" alt="MarioKart64JS en course sur Mario Raceway en résolution native avec le pack de textures HD 4x." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Mario Raceway, reconstruit à partir de la géométrie du circuit dans la ROM et dessiné par Three.js.</figcaption>
</figure>

## Ce que « correspondre » a vraiment demandé

Rendre le circuit, c'est la moitié facile. Le faire se comporter comme la cartouche, c'est là qu'est passée la journée, et les messages de commit se lisent comme une liste de petites façons dont le matériel de la N64 diffère d'un GPU moderne :

- **Karts en miroir.** Le sprite de chaque angle de caméra montrait le mauvais côté du kart. La correction a consisté à choisir les images avec `atan2(-x, z)`, car les images non inversées de la ROM montrent le flanc gauche.
- **Murs.** Les karts pouvaient traverser des parois rocheuses et des rangées d'arbres posées sur un sol continu. La correction sonde chaque circuit latéralement depuis la trajectoire et s'arrête aux faces abruptes balayées à hauteur de kart.
- **Les arbres de la jungle.** Les découpes d'arbres de D.K.'s Jungle Parkway s'affichaient avec un fond blanc, parce qu'un mode de rendu opaque à la fin d'une section débordait sur les sections suivantes. L'extracteur réinitialise désormais le mode de rendu à chaque section, comme le fait le jeu.
- **Scintillement.** Le RDP de la N64 laisse gagner le triangle le plus tardif quand deux sont coplanaires, ce que ne fait pas un GPU de bureau. L'extracteur donne donc son propre calque de décalque au décor dessiné par-dessus une géométrie antérieure, et le jeu ne dessine en double face que là où l'original désactive le back-face culling. Pour le prouver, Agent! a écrit un outil de contrôle qualité sans interface qui rend chaque vue sous forme de tampon d'ID à plat, la rend à nouveau avec un tremblement de caméra inférieur au millimètre, et compte les pixels qui changent de surface. Agent! ne peut pas regarder une capture d'écran, alors il a mesuré le scintillement à la place.
- **L'arrière-plan de l'écran titre.** Il sortait sous forme de bruit brouillé. Le bug se trouvait dans le décodeur d'images TKMK00 qu'Agent! avait porté en Python : un bit de drapeau était au mauvais endroit. Après la correction, les 35 images TKMK00 de la ROM (arrière-plans, titres de circuits, icônes de coupes, plaques de nom) se décodent à l'identique, octet par octet, avec l'outil C de la décompilation.
- **Le drapeau à damier.** Le drapeau du titre est une grille de 12×10 quads ondulée par une sinusoïde avec affaissement et éclairée comme l'éclaire le jeu. Cela représente environ 120 lignes de `flag.js`, rendues entre l'arrière-plan et le logo.

<figure style="margin:2rem 0">
<img src="/mk64js-course-select.jpg" alt="L'écran de sélection de circuit de MarioKart64JS en résolution native avec le pack de textures HD 4x." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>L'écran de sélection de circuit. Les icônes de coupes, les images d'aperçu et les plaques de titre sont placées aux positions à l'écran indiquées dans les propres tables du jeu.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-character-select.jpg" alt="L'écran de sélection de personnage de MarioKart64JS en résolution native avec le pack de textures HD 4x." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>La sélection de personnage, avec les visages des pilotes extraits de la ROM (17 images d'animation chacun) et leurs voix de sélection.</figcaption>
</figure>

## La musique est un séquenceur, pas un MP3

Mario Kart 64 ne stocke pas ses morceaux sous forme audio. Il stocke des séquences : des notes, des instruments et des effets qu'un petit lecteur sur la console transforme en son à l'exécution. Il n'y a donc aucun fichier du thème de Mario Raceway à extraire.

Le commit de 21:37, c'est `src/m64.js`, environ 800 lignes : un portage JavaScript du lecteur de séquences du jeu qui décode les échantillons d'instruments compressés (VADPCM) de la ROM et joue les séquences d'origine dans un AudioWorklet. Le titre, le menu et le thème de chaque circuit en proviennent. « Welcome to Mario Kart! » retentit sur l'écran titre, et les menus ont leurs propres sons ainsi que les voix de sélection des personnages.

<figure style="margin:2rem 0">
<img src="/mk64js-race-koopa.jpg" alt="MarioKart64JS en course sur Koopa Troopa Beach en résolution native avec le pack de textures HD 4x." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Koopa Troopa Beach. L'eau fait partie des surfaces transparentes que l'extracteur signale pour une passe séparée.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-race-dk.jpg" alt="MarioKart64JS en course sur D.K.'s Jungle Parkway en résolution native avec le pack de textures HD 4x." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>D.K.'s Jungle Parkway, le circuit dont les découpes d'arbres avaient autrefois un fond blanc. Sa rampe d'accélération propulse les karts en utilisant la gravité et la résistance de l'air du jeu.</figcaption>
</figure>

## Basse et haute résolution

L'objectif disait bien « peut-être juste des graphismes 3d plus nets que tu peux moderniser ». Le jeu a donc deux apparences, et **G** permet de passer de l'une à l'autre.

**La basse résolution, c'est la cartouche.** Le préréglage 1× rend 240 lignes, la hauteur de sortie de la N64, et les agrandit à la taille de la fenêtre avec des pixels nets : filtrage au plus proche voisin, pas d'anticrénelage, pas de mipmaps (`src/hd.js`). Les menus et le HUD tiennent dans un cadre de 320×240 mis à l'échelle uniformément pour conserver l'image 4:3 de la console (`src/main.js`). Tout en 1× vient de la ROM : textures des circuits, sprites des karts, visages, ciel et graphismes des menus, décodés par les outils Python. Le README crédite la décompilation [n64decomp/mk64](https://github.com/n64decomp/mk64) comme référence pour les graphismes et le son en basse résolution.

**La haute résolution, c'est l'option moderne.** Les autres préréglages sont 2× (480 lignes, que les commentaires de `hd.js` comparent à la Console Virtuelle de la Wii), 4× (960 lignes) et Natif (la fenêtre à la pleine densité de pixels de l'écran). Ils passent à un filtrage lissé avec mipmaps et filtrage anisotrope, et le choix est mémorisé d'une session à l'autre. Rendre plus de lignes n'ajoute pas de détail à une petite texture N64, donc les niveaux HD substituent des textures plus grandes issues du pack créé par des fans [MK64 Reloaded](https://github.com/GhostlyDark/MK64-Reloaded), que l'on construit localement avec `tools/build-hd-textures.py`. Il associe les textures des circuits grâce à la même somme de contrôle Rice/GLideN64 qu'utilisent les émulateurs N64, et associe les menus, visages, karts et le ciel par leur nom dans la décompilation via le portage SpaghettiKart du pack. Tout ce qui n'a pas de correspondance se rabat sur l'original de la ROM.

La haute résolution a eu ses propres obstacles. Un préréglage et un niveau de textures 3× (720p) ont été ajoutés puis retirés dans un commit séparé, laissant 1×, 2×, 4× et Natif ; Natif utilise les textures 2× en dessous de 720 lignes et les 4× au-dessus. Les atlas de sprites des karts s'arrêtent à 2× « pour garder une VRAM raisonnable », comme le dit le README. Et l'outil de contrôle qualité mentionné plus haut vérifie plus que le scintillement : il échoue aussi quand une texture ne s'est pas chargée au niveau HD attendu. Toutes les captures de cet article sont en résolution Native avec les textures 4×.

<figure style="margin:2rem 0">
<img src="/mk64js-race-bowser.jpg" alt="MarioKart64JS en course sur Bowser's Castle en résolution native avec le pack de textures HD 4x." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Bowser's Castle en résolution Native avec les textures 4×.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-race-rainbow.jpg" alt="MarioKart64JS en course sur Rainbow Road en résolution native avec le pack de textures HD 4x." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Rainbow Road, le seul circuit où les étoiles restent visibles sous l'horizon, comme dans l'original.</figcaption>
</figure>

## En chiffres

- **Une journée.** Premier objectif à 13:47, dernier commit à 23:03 le 6 octobre.
- **70 commits**, tous écrits par l'agent.
- **Environ 3 200 lignes de JavaScript** dans `src/` : le moteur de rendu des circuits, la physique des karts, les objets, le HUD, les menus, le drapeau, la fumée d'échappement, les niveaux de textures HD et le lecteur de musique de 800 lignes.
- **Environ 2 000 lignes de Python** dans `tools/` : des extracteurs pour les karts, les visages, la géométrie des circuits, les boîtes à objets, les aperçus, les menus, le ciel, la fumée et le son, plus le décodeur TKMK00 et le constructeur de textures HD.
- **Environ 500 lignes de scripts de test et de contrôle qualité** qui vérifient les données par rapport à la ROM et à la décompilation et parcourent chaque circuit dans Chromium sans interface.
- **Une version de bureau.** [MarioKart64JS 0.0.1](https://github.com/AgentiLoop/MarioKart64JS/releases/tag/v0.0.1) est une préversion empaquetée dans Electron, avec une compilation macOS universelle signée et notarisée par Apple, ainsi que des compilations Windows et Linux pour x64 et arm64.

## Le défi pour l'IA, en toute honnêteté

GoKart a montré qu'Auto-Pilot peut construire un jeu que l'on reconnaîtrait comme un jeu de kart. MarioKart64JS demande quelque chose de plus ciblé et de bien plus difficile : peut-il reproduire un jeu précis qu'il n'a jamais vu tourner ? La réponse de cette journée est « plus proche que ne le laissait penser la première heure, et pas terminé ».

Ce qui l'a rendu possible, ce n'est pas que le modèle ait mémorisé Mario Kart 64. C'est d'avoir eu quelque chose à quoi se comparer. La ROM et la décompilation ont donné à chaque cycle une référence qu'il pouvait tester : des images identiques octet par octet, les positions exactes à l'écran, les propres minuteurs du jeu. Agent! a donc vérifié l'exactitude en comparant des données, pas en regardant. Il ne peut toujours pas voir une image. Chaque cycle qui a produit une capture d'écran s'est terminé comme ceux de GoKart : « Je ne l'ai pas regardée moi-même... Merci d'y jeter un œil. » Pour les captures de cet article, il a mesuré les couleurs des pixels pour confirmer qu'aucune image n'était vide, et a laissé le vrai regard à une personne.

Ce qui n'est pas fait, d'après la feuille de route du README : le surligneur de la sélection de personnage, les quatre arènes du mode Bataille, et une parité de jouabilité plus poussée : classes CC, personnalités de l'IA, Lakitu.

## L'essayer

Clonez [AgentiLoop/MarioKart64JS](https://github.com/AgentiLoop/MarioKart64JS), puis `npm install && npm run dev` et ouvrez `http://localhost:5173`. Les flèches ou WASD pour conduire, Espace pour déraper, Maj ou E pour lancer un objet, G pour changer la résolution et N pour activer ou couper la musique. Une manette fonctionne aussi. Les outils d'extraction de `tools/` fonctionnent à partir d'une ROM de Mario Kart 64 (USA), et le README indique le SHA-1 attendu.

*MarioKart64JS est un projet de recherche de fans visant à tester jusqu'où l'IA peut aller dans la reproduction d'un jeu. Mario Kart 64 est © Nintendo, et ses ressources appartiennent à Nintendo. Le projet n'est ni affilié à Nintendo ni approuvé par Nintendo.*
