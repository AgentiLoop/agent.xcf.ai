---
title: MarioKart64JS passe à la 3D : karts de la Wii, écran titre en 3D et survols après l'arrivée
description: Mario Kart 64 dessine ses pilotes sous forme de sprites plats. Appuyez sur 3 dans MarioKart64JS et chaque kart devient un modèle 3D, Lakitu compris, avec de vraies ombres, un écran titre reconstruit en 3D et une caméra qui tourne autour de votre kart après l'arrivée. Voici comment le mode 3D a été assemblé, en captures d'écran.
tags: Showcase, JavaScript
---
<figure style="margin:2rem 0">
<img src="/mk64js-3d-title.jpg" alt="L'écran titre 3D de MarioKart64JS : Wario, Bowser, Mario, Peach et Toad dans des karts 3D roulant vers la caméra sous le logo de Mario Kart 64." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>L'écran titre en 3D. L'original est une seule illustration plate. Ici, le ciel, les collines et la route sont construits avec Three.js, et les cinq pilotes sont des karts 3D qui roulent vers la caméra.</figcaption>
</figure>

Le [dernier article sur MarioKart64JS](/blog/mariokart64js-from-scratch-in-javascript/) portait sur la reproduction la plus fidèle possible de Mario Kart 64 : géométrie des circuits, sprites et musique tirés de la cartouche, et du JavaScript neuf qui fait ce que fait le C de l'original. Celui-ci va dans la direction opposée. Une touche, **3**, active un mode 3D que la N64 n'a jamais eu.

## Les sprites deviennent des modèles

Les pilotes de Mario Kart 64 ne sont pas des modèles. Chaque pilote correspond à 321 images précalculées de 64×64, et le jeu choisit celle qui correspond à l'angle de la caméra. C'est aussi ce que dessine MarioKart64JS, et c'est toujours le cas par défaut.

Le mode 3D remplace ces sprites par des modèles du Kart Standard de Mario Kart Wii, issus d'exports Collada placés dans le projet par `tools/build-wii-karts.py`. Tout a commencé le soir du 9 octobre par un simple test : à 21:22, la touche 3 plaçait sous le joueur un Kart Standard rouge avec Mario à bord. À 22:02, les huit pilotes avaient le leur, répartis selon les catégories de poids de la Wii : le petit kart pour Toad, le moyen pour Mario, Luigi, Peach et Yoshi, et le grand pour D.K., Wario et Bowser, chacun avec sa propre livrée.

L'essentiel du travail entre les deux a consisté en de petites choses qu'un chargeur de modèles fait mal :

- **Les yeux.** Chaque texture d'œil ne contient qu'un seul œil. Sur Wii, une matrice de texture la duplique et le sampler la retourne en miroir pour former une paire. Le ColladaLoader de Three.js ignore les deux, si bien qu'un seul œil était étiré sur tout le visage. `kart3d.js` rétablit la répétition et le miroir pour chaque personnage.
- **Les roues.** Les roues arrière sont le maillage de la roue avant agrandi. Leur taille et la position des essieux sont mesurées à partir du modèle assemblé du menu de chaque kart, ce qui a rendu les roues arrière 1,29× plus grandes et les a placées là où la Wii les met.
- **Les sièges.** Chaque pilote reçoit une position de siège pour qu'il soit assis dans le siège incliné au lieu de flotter au-dessus.

Agent! ne peut pas regarder une image, il a donc vérifié les modèles avec des chiffres : des vues ASCII de côté, de l'arrière et de dessus de chaque kart, des planches de plateau tournant sur 12 angles, et les écarts mesurés entre les mains de chaque pilote et le volant.

## Courir en 3D

<figure style="margin:2rem 0">
<img src="/mk64js-3d-race-mario.jpg" alt="MarioKart64JS en mode 3D, en course sur Mario Raceway avec des karts 3D." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Mario Raceway en mode 3D. Chaque kart de la course est un modèle 3D, chacun dans le Kart Standard de son personnage.</figcaption>
</figure>

En course, la touche 3 remplace tous les karts sur la piste, pas seulement le vôtre, et un nouvel appui ramène les sprites. Deux autres choses changent avec elle.

**Les ombres.** Les sprites ont sous eux une ombre plate en forme de tache. Les karts 3D projettent de vraies ombres par shadow mapping sur le circuit. Il a fallu une astuce : le circuit est dessiné avec des matériaux non éclairés qui ne peuvent pas recevoir d'ombres, alors le circuit reçoit des copies transparentes de ses surfaces qui captent les ombres et n'apparaissent que là où une ombre tombe.

**Lakitu.** L'arbitre devient le Lakitu de Mario Kart Wii (`src/lakitu3d.js`). Ses bras sont posés grâce aux propres os du modèle : l'un tient la canne à pêche, l'autre agite le drapeau. Les feux de départ, les panneaux de tours et le panneau de sens inverse pendent à l'hameçon de la canne, et l'image d'animation du sprite d'origine continue de régler le timing, si bien que le compte à rebours rouge, rouge, bleu s'allume au même moment que toujours.

<figure style="margin:2rem 0">
<img src="/mk64js-3d-race-koopa.jpg" alt="MarioKart64JS en mode 3D, en course sur Koopa Troopa Beach." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Koopa Troopa Beach, où est passée la majeure partie du 10 octobre : ce sont ces tremplins que le corps du kart 3D a dû apprendre à gravir.</figcaption>
</figure>

Un kart 3D a aussi un corps que le sprite n'avait pas. Contre les murs, c'est une capsule, un cercle au-dessus de chaque essieu, et il se déplace et tourne comme un corps rigide. Cela a eu des effets de bord. Sur Koopa Troopa Beach, le cercle avant atteignait le rebord d'un tremplin avant le centre du kart, et la face arrière du rebord éjectait le kart du saut. La correction teste chaque essieu par rapport au sol situé en dessous. Un commit ultérieur a empêché les murs de faire pivoter le kart du joueur lors d'un choc frontal, car dans Mario Kart 64 un mur renvoie le mouvement du kart sans jamais changer son orientation.

<figure style="margin:2rem 0">
<img src="/mk64js-3d-race-royal.jpg" alt="MarioKart64JS en mode 3D, en course sur Royal Raceway." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Royal Raceway en mode 3D.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-3d-race-bowser.jpg" alt="MarioKart64JS en mode 3D, en course dans Bowser's Castle." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Bowser's Castle, dont le passage de 5 de large est l'endroit où il a fallu empêcher la capsule de se coincer en travers du couloir.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-3d-race-rainbow.jpg" alt="MarioKart64JS en mode 3D, en course sur Rainbow Road." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Rainbow Road avec des karts 3D.</figcaption>
</figure>

## Un écran titre en 3D

Le fond de l'écran titre de Mario Kart 64 est une seule image plate de 320×240. Le ciel, les collines, la route et les cinq pilotes sont tous peints. Appuyer sur 3 à l'écran titre le reconstruit (`src/title3d.js`) : le ciel, les collines et la route sont faits avec Three.js, et les pilotes sont les mêmes karts 3D qu'en course.

La disposition suit l'illustration. Wario est devant à gauche avec Bowser derrière lui, Mario est devant à droite avec Peach derrière, et Toad sort du virage de droite. Chaque kart est placé de sorte que son cadre à l'écran tombe à environ 10 pixels du cadre de son pilote dans l'illustration d'origine. La caméra est placée bas sur la route, devant eux, avec un objectif grand angle de 64°, et la route défile en dessous, si bien que les karts semblent foncer droit sur vous. Le drapeau à damier, le logo, PUSH START et le copyright restent les calques 2D de l'écran titre d'origine.

Les menus situés derrière ont aussi reçu des fonds assortis. Activer la 3D à l'écran titre fait aussi passer au niveau de textures 4×, et les courses démarrent en 3D jusqu'à ce que vous appuyiez de nouveau sur 3.

<figure style="margin:2rem 0">
<img src="/mk64js-3d-game-select.jpg" alt="L'écran de sélection du jeu de MarioKart64JS avec son fond du mode 3D." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>L'écran de sélection du jeu avec son fond du mode 3D.</figcaption>
</figure>

## Survols après l'arrivée

Quand vous franchissez la ligne, Mario Kart 64 confie la caméra à une courte cinématique. MarioKart64JS suit pour cela le code de caméra du jeu (`PLAYER_CINEMATIC_MODE` et les fonctions de plans cinématiques de la décompilation) : la caméra pivote jusqu'à l'avant du kart et le regarde franchir la ligne, puis enchaîne les plans pendant que le pilote CPU prend le contrôle de votre kart. La séquence répète orbite avant, bord de route, grue haute, bord de route, plan bas arrière, bord de route. Une réserve tirée des commentaires du code : la durée et les distances des plans sont réglées à l'œil, et non tirées des tables de la ROM.

Les plans de suivi suivent une copie fortement lissée de la direction du kart. Sans cela, les petites corrections de direction de l'IA faisaient osciller la caméra autour du kart et donnaient l'impression qu'il tournait par à-coups. Avec les karts 3D, ce sont ces plans qui mettent le plus les modèles en valeur, puisque la caméra voit enfin les karts de face et de profil.

<figure style="margin:2rem 0">
<img src="/mk64js-3d-flyover-front.jpg" alt="Survol après l'arrivée sur Mario Raceway : la caméra devant le kart 3D de Mario, tournée vers lui." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Le plan avant sur Mario Raceway : la caméra tourne de l'arrière du kart jusqu'à l'avant et roule devant lui.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-3d-flyover-crane.jpg" alt="Survol après l'arrivée sur Mario Raceway : un plan de grue haute regardant la route derrière le kart." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Le plan de grue haute, au-dessus et derrière le kart, regardant le long de la route.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-3d-flyover-roadside.jpg" alt="Survol après l'arrivée sur Royal Raceway : une caméra placée au bord de la route pendant que le kart passe." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Un plan en bord de route sur Royal Raceway. La caméra se poste au bord de la route, plus loin, et reste en place jusqu'à ce que le kart soit passé.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-3d-flyover-low.jpg" alt="Survol après l'arrivée sur Koopa Troopa Beach : une caméra basse au niveau de l'épaule du kart." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Le plan bas arrière sur Koopa Troopa Beach, au niveau d'un flanc du kart.</figcaption>
</figure>

## Comment les captures ont été prises

Toutes les images de cet article ont été prises dans Chrome sans interface à 1280×960. Les captures de l'écran titre et de la sélection du jeu appuient sur 3 à l'écran titre, comme le ferait un joueur. Les courses tournent en pilote automatique avec le mode 3D enregistré comme activé, et les survols ont été capturés en plaçant le joueur dans la dernière ligne droite du dernier tour et en prenant une image toutes les 0,7 secondes après l'arrivée. Agent! a choisi les images en les mesurant : la position de la caméra par rapport au kart lui indiquait à quel plan correspondait chaque image, et des statistiques de pixels ont écarté les images sombres ou pauvres en détails. Comme pour l'article précédent, il ne les a pas regardées lui-même.

## L'essayer

Clonez [AgentiLoop/MarioKart64JS](https://github.com/AgentiLoop/MarioKart64JS), lancez `npm install && npm run dev`, ouvrez `http://localhost:5173` et appuyez sur **3** à l'écran titre ou en course. La version web inclut aussi les karts 3D, Lakitu et l'écran titre en 3D. Les modèles préparés se trouvent dans `public/wii/` ; `tools/build-wii-karts.py` et `tools/build-wii-lakitu.py` sont les scripts qui les ont préparés à partir des fichiers Collada.

*MarioKart64JS est un projet de recherche de fans visant à tester jusqu'où l'IA peut aller dans la reproduction d'un jeu. Mario Kart 64 et Mario Kart Wii sont © Nintendo, et leurs ressources appartiennent à Nintendo. Le projet n'est ni affilié à Nintendo ni approuvé par Nintendo.*
