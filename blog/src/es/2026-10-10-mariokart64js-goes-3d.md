---
title: MarioKart64JS se pasa al 3D: karts de Wii, una pantalla de título en 3D y vuelos de cámara tras la meta
description: Mario Kart 64 dibuja a sus pilotos como sprites planos. Pulsa 3 en MarioKart64JS y cada kart se convierte en un modelo 3D, Lakitu incluido, con sombras reales, una pantalla de título reconstruida en 3D y una cámara que vuela alrededor de tu kart después de la meta. Así se montó el modo 3D, en capturas de pantalla.
tags: Showcase, JavaScript
---
<figure style="margin:2rem 0">
<img src="/mk64js-3d-title.jpg" alt="La pantalla de título en 3D de MarioKart64JS: Wario, Bowser, Mario, Peach y Toad en karts 3D conduciendo hacia la cámara bajo el logotipo de Mario Kart 64." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>La pantalla de título en 3D. La original es una única ilustración plana. Aquí el cielo, las colinas y la carretera están construidos en Three.js, y los cinco pilotos son karts 3D que conducen hacia la cámara.</figcaption>
</figure>

La [última entrada sobre MarioKart64JS](/blog/mariokart64js-from-scratch-in-javascript/) trataba de igualar Mario Kart 64 lo más fielmente posible: geometría de circuitos, sprites y música sacados del cartucho, y JavaScript nuevo haciendo lo que hace el C del original. Esta va en la dirección contraria. Una tecla, el **3**, activa un modo 3D que la N64 nunca tuvo.

## Los sprites se convierten en modelos

Los pilotos de Mario Kart 64 no son modelos. Cada uno son 321 fotogramas prerrenderizados de 64×64, y el juego elige el fotograma que corresponde al ángulo de la cámara. Eso es también lo que dibuja MarioKart64JS, y sigue haciéndolo por defecto.

El modo 3D sustituye esos sprites por modelos del Kart Estándar de Mario Kart Wii, a partir de exportaciones Collada que `tools/build-wii-karts.py` coloca en el proyecto. Empezó la tarde del 9 de octubre como una sola prueba: a las 21:22 la tecla 3 ponía un Kart Estándar rojo con Mario dentro bajo el jugador. A las 22:02 los ocho pilotos tenían el suyo, repartidos según las categorías de peso de Wii: el kart Pequeño para Toad, el Mediano para Mario, Luigi, Peach y Yoshi, y el Grande para D.K., Wario y Bowser, cada uno con su propia decoración.

La mayor parte del trabajo entre medias fueron pequeñas cosas que un cargador de modelos hace mal:

- **Los ojos.** Cada textura de ojo es un solo ojo. En Wii una matriz de textura la duplica y el sampler la refleja para formar un par. El ColladaLoader de Three.js descarta ambas cosas, así que un solo ojo quedaba estirado por toda la cara. `kart3d.js` restaura la repetición y el reflejo para cada personaje.
- **Las ruedas.** Las ruedas traseras son la malla de la rueda delantera ampliada. Su tamaño y la posición de los ejes se miden a partir del modelo ensamblado del menú de cada kart, lo que hizo las ruedas traseras 1,29× más grandes y las colocó donde las tiene Wii.
- **Los asientos.** Cada piloto tiene una posición de asiento para que vaya sentado en el asiento reclinado en lugar de flotar por encima.

Agent! no puede mirar una imagen, así que comprobó los modelos con números: vistas ASCII lateral, trasera y superior de cada kart, hojas de plataforma giratoria con 12 ángulos, y distancias medidas entre las manos de cada piloto y el volante.

## Correr en 3D

<figure style="margin:2rem 0">
<img src="/mk64js-3d-race-mario.jpg" alt="MarioKart64JS en modo 3D corriendo en Mario Raceway con karts 3D." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Mario Raceway en modo 3D. Cada kart de la carrera es un modelo 3D, cada uno en el Kart Estándar de su personaje.</figcaption>
</figure>

En una carrera, el 3 cambia todos los karts de la pista, no solo el tuyo, y la siguiente pulsación devuelve los sprites. Con él cambian otras dos cosas.

**Sombras.** Los sprites tienen debajo una sombra plana en forma de mancha. Los karts 3D proyectan sombras reales mediante shadow maps sobre el circuito. Eso necesitó un truco: el circuito se dibuja con materiales sin iluminación que no pueden recibir sombras, así que el circuito recibe copias transparentes de sus superficies que atrapan sombras y solo se ven donde cae una sombra.

**Lakitu.** El árbitro pasa a ser el Lakitu de Mario Kart Wii (`src/lakitu3d.js`). Sus brazos se posan mediante los propios huesos del modelo: uno sujeta la caña de pescar y el otro ondea la bandera. Las luces de salida, los carteles de vuelta y la señal de sentido contrario cuelgan del anzuelo de la caña, y el fotograma de animación del sprite original sigue marcando el ritmo, así que la cuenta atrás roja, roja, azul se enciende cuando siempre lo hacía.

<figure style="margin:2rem 0">
<img src="/mk64js-3d-race-koopa.jpg" alt="MarioKart64JS en modo 3D corriendo en Koopa Troopa Beach." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Koopa Troopa Beach, donde se fue la mayor parte del 10 de octubre: los saltos de aquí son los que el cuerpo del kart 3D tuvo que aprender a subir.</figcaption>
</figure>

Un kart 3D también tiene un cuerpo que el sprite no tenía. Contra los muros es una cápsula, un círculo sobre cada eje, y se mueve y gira como un cuerpo rígido. Eso tuvo efectos secundarios. En Koopa Troopa Beach el círculo delantero llegaba al borde de una rampa antes que el centro del kart, y la cara trasera del borde lo expulsaba del salto. La solución comprueba cada eje contra el suelo que tiene debajo. Un commit posterior impidió que los muros giraran el kart del jugador en un choque frontal, porque en Mario Kart 64 un muro refleja el movimiento del kart y nunca cambia hacia dónde mira.

<figure style="margin:2rem 0">
<img src="/mk64js-3d-race-royal.jpg" alt="MarioKart64JS en modo 3D corriendo en Royal Raceway." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Royal Raceway en modo 3D.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-3d-race-bowser.jpg" alt="MarioKart64JS en modo 3D corriendo en Bowser's Castle." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Bowser's Castle, cuyo pasillo de 5 de ancho es donde hubo que evitar que la cápsula se quedara atascada de lado a lado.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-3d-race-rainbow.jpg" alt="MarioKart64JS en modo 3D corriendo en Rainbow Road." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Rainbow Road con karts 3D.</figcaption>
</figure>

## Una pantalla de título en 3D

El fondo del título de Mario Kart 64 es una única imagen plana de 320×240. El cielo, las colinas, la carretera y los cinco pilotos están todos pintados. Pulsar 3 en el título la reconstruye (`src/title3d.js`): el cielo, las colinas y la carretera se hacen en Three.js, y los pilotos son los mismos karts 3D que en las carreras.

La composición sigue la ilustración. Wario va delante a la izquierda con Bowser detrás, Mario va delante a la derecha con Peach detrás, y Toad sale de la curva de la derecha. Cada kart está colocado de modo que su recuadro en pantalla cae a unos 10 píxeles del recuadro de su piloto en el arte original. La cámara está baja sobre la carretera, por delante de ellos, con un objetivo gran angular de 64°, y la carretera se desplaza por debajo, así que los karts parecen conducir directamente hacia ti. La bandera a cuadros, el logotipo, PUSH START y el copyright siguen siendo las capas 2D del título original.

Los menús que hay detrás también recibieron fondos a juego. Activar el 3D en el título también cambia al nivel de texturas 4×, y las carreras empiezan en 3D hasta que vuelvas a pulsar 3.

<figure style="margin:2rem 0">
<img src="/mk64js-3d-game-select.jpg" alt="La pantalla de selección de juego de MarioKart64JS con su fondo del modo 3D." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>La pantalla de selección de juego con su fondo del modo 3D.</figcaption>
</figure>

## Vuelos de cámara tras la meta

Cuando cruzas la línea, Mario Kart 64 cede la cámara a una breve cinemática. MarioKart64JS sigue para ello el código de cámara del juego (`PLAYER_CINEMATIC_MODE` y las funciones de planos cinemáticos de la decompilación): la cámara gira hasta la parte delantera del kart y lo observa cruzar la línea, y luego corta entre planos mientras el piloto de la CPU toma el control de tu kart. La secuencia repite órbita frontal, borde de la carretera, grúa alta, borde de la carretera, plano bajo trasero, borde de la carretera. Una salvedad de los comentarios del código: la duración y las distancias de los planos están ajustadas a ojo, no sacadas de las tablas de la ROM.

Los planos de seguimiento siguen una copia muy suavizada de la dirección del kart. Sin ella, las pequeñas correcciones de dirección de la IA hacían tambalear la cámara alrededor del kart y parecía que giraba a tirones. Con karts 3D, estos planos son donde más lucen los modelos, ya que la cámara por fin ve los karts de frente y de lado.

<figure style="margin:2rem 0">
<img src="/mk64js-3d-flyover-front.jpg" alt="Vuelo de cámara tras la meta en Mario Raceway: la cámara por delante del kart 3D de Mario, mirándolo hacia atrás." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>El plano frontal en Mario Raceway: la cámara orbita desde detrás del kart hasta su parte delantera y avanza por delante de él.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-3d-flyover-crane.jpg" alt="Vuelo de cámara tras la meta en Mario Raceway: un plano de grúa alta mirando la carretera por detrás del kart." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>El plano de grúa alta, por encima y por detrás del kart, mirando carretera abajo.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-3d-flyover-roadside.jpg" alt="Vuelo de cámara tras la meta en Royal Raceway: una cámara colocada junto a la carretera mientras el kart pasa." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Un plano al borde de la carretera en Royal Raceway. La cámara se sitúa junto a la carretera, más adelante, y aguanta hasta que el kart ha pasado.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-3d-flyover-low.jpg" alt="Vuelo de cámara tras la meta en Koopa Troopa Beach: una cámara baja junto al hombro del kart." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>El plano bajo trasero en Koopa Troopa Beach, junto a un costado del kart.</figcaption>
</figure>

## Cómo se tomaron las capturas

Todas las imágenes de esta entrada se tomaron en Chrome sin interfaz a 1280×960. Las capturas del título y de la selección de juego pulsan 3 en el título, igual que lo haría un jugador. Las carreras se juegan en piloto automático con el modo 3D guardado como activado, y los vuelos de cámara se capturaron poniendo al jugador en la última recta de la vuelta final y tomando un fotograma cada 0,7 segundos después de la meta. Agent! eligió los fotogramas midiéndolos: la posición de la cámara respecto al kart le indicaba a qué plano correspondía cada fotograma, y las estadísticas de píxeles descartaron los fotogramas oscuros o con poco detalle. Como en la entrada anterior, no los miró él mismo.

## Pruébalo

Clona [AgentiLoop/MarioKart64JS](https://github.com/AgentiLoop/MarioKart64JS), ejecuta `npm install && npm run dev`, abre `http://localhost:5173` y pulsa **3** en la pantalla de título o en una carrera. La versión web también incluye los karts 3D, Lakitu y el título en 3D. Los modelos preparados están en `public/wii/`; `tools/build-wii-karts.py` y `tools/build-wii-lakitu.py` son los scripts que los prepararon a partir de los archivos Collada.

*MarioKart64JS es un proyecto de investigación de fans para comprobar hasta dónde puede llegar la IA al duplicar un juego. Mario Kart 64 y Mario Kart Wii son © Nintendo, y sus recursos pertenecen a Nintendo. El proyecto no está afiliado a Nintendo ni cuenta con su respaldo.*
