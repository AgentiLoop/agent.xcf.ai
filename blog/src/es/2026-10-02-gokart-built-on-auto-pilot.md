---
title: GoKart: un juego de carreras al estilo Mario Kart que Auto-Pilot construyó en una tarde
description: Dale a Auto-Pilot de Agent! un único objetivo - "crea un clon de Mario Kart llamado GoKart" - y vuelve para encontrarte un juego de carreras en Godot 4 con tres circuitos, ocho objetos, rivales controlados por IA y 3.344 comprobaciones de test en verde. Dos días y 87 commits del agente después es GoKart 0.0.2: cuatro circuitos, modo Batalla, Contrarreloj, un menú al estilo Mario Kart 64 y 14.134 comprobaciones en verde. Esto es lo que dice el registro que ocurrió de verdad, incluidas las partes en las que se quedó atascado.
tags: Auto-Pilot, Vitrina, Godot
updated: 2026-10-04
---
<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-title.png" alt="La pantalla de título de GoKart 0.0.2: la palabra GOKART dispuesta en un arco con grandes letras en degradado de amarillo a rojo, laterales de bloque azul marino y una sombra suave, sobre una demo de atracción en vivo de karts de la CPU dando vueltas a un circuito, con PRESS ENTER debajo." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>La pantalla de título de GoKart 0.0.2. El logo entra volando y rebota hasta detenerse sobre una demo de atracción en vivo que recorre los circuitos. Cada malla, shader, disposición de fuente y sonido se generó desde código.</figcaption>
</figure>

*Actualizado el 4 de octubre: esta entrada ahora cubre los dos días posteriores a la primera tarde, las dos sesiones de Auto-Pilot que se ejecutaron al mismo tiempo en el mismo repositorio y la versión [GoKart 0.0.2](#gokart-0-0-2). Las capturas se volvieron a tomar desde la etiqueta 0.0.2.*

La entrada de ayer presentó [Auto-Pilot](/blog/agent-1-1-87-and-agentiloop-cli-0-0-5/): escribe `/auto <objetivo>` en Agent! para Mac y ejecuta ciclos sin supervisión hacia ese objetivo hasta que pulsas Stop All. Esta entrada va de lo que salió por el otro lado cuando lo apunté a un juego.

El objetivo, pegado más o menos tal como lo escribí:

> create a Mario Kart clone called GoKart with all Mario Kart effects. I believe Godot 4 can do the Mario Kart effects, but I haven't built any of them yet: drift sparks and boost flames (GPUParticles3D), speed lines and boost blur (screen-space shaders, glow and tonemapping), item effects and tire trails (shaders plus ribbon meshes), kart movement (VehicleBody3D or custom arcade physics). Write unit tests and test the game frequently.

Presupuesto: sin límite de tiempo, ciclos ilimitados. El modelo dentro de Agent! en todos los ciclos fue Claude Sonnet 5.5. El primer commit llegó a las 12:39. A las 16:32 de esa misma tarde el repositorio tenía 33 commits, 47 archivos GDScript, unas 5.500 líneas de GDScript y código de shaders, y una suite unitaria que pasaba 3.344 comprobaciones. Dos días después, en la etiqueta 0.0.2, son 126 commits, 150 archivos GDScript, unas 24.500 líneas y 14.134 comprobaciones, y cada uno de esos commits tiene al agente como autor. Todo está en GitHub, en [AgentiLoop/GoKart](https://github.com/AgentiLoop/GoKart).

## Qué hace Auto-Pilot, ciclo a ciclo

Auto-Pilot mantiene un registro continuo en `.agent/autopilot/progress.md` dentro del proyecto, y cada ciclo añade lo que hizo, lo que asumió, lo que queda y si algo lo bloqueó. Ese registro es la fuente de todo lo que sigue. Lo cito en lugar de fiarme de mi memoria porque el registro es más honesto que yo.

El **ciclo 1** no tenía Godot en la máquina. Ejecutó `brew install --cask godot`, creó un enlace simbólico al binario, hizo `git init` y escribió `kart_physics.gd` como un modelo puro sin dependencias de escena: aceleración, frenado, marcha atrás, fricción, dirección, un derrape bloqueado en la dirección en la que lo iniciaste y tres niveles de miniturbo. Eligió a propósito una física arcade propia en lugar de `VehicleBody3D`, y explicó por qué: "para que el manejo al estilo Mario Kart sea fácil de probar con tests unitarios". Once tests, 17 comprobaciones, primer commit.

El **ciclo 2** añadió los efectos que había pedido por su nombre: chispas de derrape con GPUParticles3D coloreadas según el nivel de miniturbo, llamas de escape, estelas de neumáticos con mallas de cinta y un shader de espacio de pantalla para el desenfoque radial del turbo, las líneas de velocidad y una viñeta. 43 comprobaciones.

El **ciclo 3** construyó un circuito. Un bucle Catmull-Rom remuestreado cada 3 metros, una cinta de carretera, muros a rayas rojas y blancas con colisionadores, plataformas de turbo con un shader de chevrones desplazándose, ocho checkpoints ordenados y un contador de vueltas que se niega a contar atajos o vueltas en sentido contrario. Uno de los nuevos tests es un bot de persecución que conduce tres vueltas completas usando el modelo de física real. Terminó en 1:02.5. 90 comprobaciones.

El **ciclo 4** añadió cajas de objetos con un shader fresnel arcoíris, una ruleta y los tres primeros objetos: champiñón, plátano y un caparazón verde que rebota en los muros. Recibir un impacto hace girar el kart durante 1,2 segundos. 235 comprobaciones.

Y entonces se quedó atascado.

## La parte en la que se quedó atascado

El siguiente ciclo empezó a añadir karts controlados por IA y una carrera de humo sin interfaz, y nunca volvió. La causa, encontrada en la sesión siguiente, fue un único tabulador perdido en la línea 115 de `main.gd`: un error de análisis que hizo que el script de humo escupiera errores sin parar, sin límite de tiempo en el comando de shell que lo ejecutaba.

Pulsé **Stop All** y abrí una sesión nueva con el mismo objetivo más una nota en mayúsculas que no reproduciré entera. La esencia: *te quedaste atascado probando la carrera de humo, no te quedes atascado, pon un límite de tiempo al shell.*

El primer ciclo de la segunda sesión arregló el tabulador, redujo la anticipación de la IA de 10 muestras de carretera a 6 para que la IA dejara de cortar curvas contra el muro interior, añadió un limitador de velocidad en curva y envolvió cada ejecución de shell en `perl -e 'alarm 100; exec @ARGV'`, porque macOS viene sin el comando `timeout`. A partir de ahí, el registro dice "todas las ejecuciones estuvieron bajo límites de perl alarm" al final de casi todos los ciclos. Aprendió la lección del texto del objetivo y siguió aplicándola.

Esa sesión ejecutó 15 ciclos en aproximadamente una hora y cuarto, y cada uno es una funcionalidad: cuenta atrás de salida con turbo de salida relámpago para quien acelera en el momento justo; estallidos al subir de nivel de miniturbo y un destello en el borde de la pantalla; un minimapa; el caparazón rojo teledirigido y la estrella; un modelo de kart procedural con ruedas que giran, ruedas delanteras que doblan y un piloto que gira la cabeza; un rayo que encoge a todos los rivales; caparazones triples que orbitan el kart; el caparazón azul con púas que persigue al líder por la carretera; una pantalla de resultados con puntos; audio totalmente sintetizado sin archivos de audio, desde el bucle del motor hasta la melodía de meta; un menú de título con un segundo circuito; una opción de número de vueltas; un tercer circuito; y zumbido de motor 3D posicional en cada kart de la IA.

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-sunset-speedway.png" alt="GoKart 0.0.2 en Sunset Speedway: el kart del jugador derrapando en 3.ª posición de 8 en la vuelta 1 bajo el cielo de atardecer, con el HUD al estilo Mario Kart 64: un mapa del circuito translúcido en la esquina inferior izquierda, posición, vuelta y velocidad en una fuente redondeada dorada y crema." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Sunset Speedway en 0.0.2: un bot de conducción aleatoria en pleno derrape en 3.ª posición de 8. El segundo circuito se añadió en el ciclo 12 del primer día, junto con el menú de título. El tráfico, los edificios más allá de los muros y el HUD llegaron dos días después.</figcaption>
</figure>

## La parte en la que fue honesto

Lo que más me gusta del registro es el patrón de confesiones. Agent! no puede mirar un PNG, y lo dijo, ciclo tras ciclo:

> La ejecución de capturas en ventana no registró errores, pero no puedo ver imágenes, así que no he mirado cómo se renderizan el circuito o el HUD.

> No he oído los sonidos, y no ejecuté la carrera de humo ni la herramienta de capturas.

> No puedo ver imágenes con mis herramientas, así que esa revisión necesita a una persona.

Así que probó lo que podía: comprobaciones de escena sin interfaz que instancian la escena real y hacen aserciones sobre el estado. Lanzar un rayo, confirmar que tres rivales están a escala 0,5 y girando y que los relámpagos se limpian después. Lanzar un caparazón azul contra una parrilla de salida apiñada, confirmar la explosión en el fotograma 12 y dos karts girando. Forzar al jugador a terminar, confirmar que el piloto automático entrega el kart a un `AiDriver` y que el panel de resultados muestra "1st YOU".

Una tercera sesión se atascó de la misma manera, esta vez detrás de una alarma de 240 segundos que era demasiado generosa, y la detuve tras un ciclo. Entonces miró una persona. Esa persona fui yo, y el objetivo de la cuarta sesión fueron mis notas de prueba, ligeramente ordenadas:

> the UI needs to scale with the window. the UI should not be prone to the screen speed effects and blurry. Should be able to use cursor keys. it's not clear when power ups are released. the tops of the walls flicker. Little too hard to steer the kart. hard to keep up with the computer AI karts. maybe have AI difficulty levels Easy Medium and Hard.

Un ciclo después: estirado de canvas items para que la UI escale con la ventana, el HUD movido a una capa de canvas por encima de la superposición de efectos de velocidad, teclas de flecha, Enter y Ctrl para los objetos con una pista en pantalla, dirección con entrada suavizada, un arreglo del z-fighting en las rayas de los muros (los segmentos rojos y blancos vecinos se peleaban por los mismos píxeles, así que los blancos se hicieron ligeramente más grandes), MSAA 4x, y Fácil / Medio / Difícil, que escalan la velocidad máxima de la IA a 0,72, 0,85 y 1,0. Los tests pasaron de 2.156 a 3.344 comprobaciones, en parte porque también encontró y arregló un error de análisis preexistente en `tests/test_items.gd` que impedía que la suite se cargara.

## La parte en la que se detuvo a sí mismo

Los ciclos 2 a 8 de esa última sesión no hicieron cambios de código. Cada uno releyó el repositorio, volvió a ejecutar la suite y escribió una variante del mismo párrafo:

> No pude ver el resultado en pantalla, así que no declaro el objetivo alcanzado. Cuatro puntos siguen necesitando que un humano los pruebe en el juego.

Ese es el comportamiento correcto. El objetivo era "la dirección se siente mal" y "los muros parpadean", y ningún test sin interfaz puede cerrar ese objetivo. Auto-Pilot no tiene límite de iteraciones, así que habría seguido comprobando para siempre. La sesión terminó tras el ciclo 8, y lo que GoKart necesitaba a continuación era una partida de prueba, no otro ciclo. Esa tarde el repositorio se etiquetó como 0.0.1 y se exportó para macOS, Windows y Linux.

## Dos días después: dos Auto-Pilots en un mismo repositorio

El 3 de octubre volví con un tipo de objetivo distinto. No una lista de funcionalidades, sino una referencia:

> keep building GoKart to resemble Mario Kart Nintendo 64 version. search Mario Kart N64 or Mario Kart Nintendo 64 and keep improving, iterating, making GoKart better

Esa quinta sesión empezó a las 14:19 y ejecutó 28 ciclos, y casi cada ciclo es una cosa de Mario Kart 64 que el agente buscó y construyó: la parrilla de 8 corredores en dos columnas, el rubber-banding según la dificultad, 50cc / 100cc / 150cc y la clase Extra en espejo, karts Ligero / Medio / Pesado que se empujan entre sí, Grand Prix con 9/6/3/1 puntos y la regla de eliminación por puesto, Contrarreloj con un fantasma, modo Batalla con globos en Big Donut, Block Fort y Skyscraper, champiñones triples y dorados, la caja de objetos falsa, el racimo de plátanos, Boo, caparazones rojos triples, el bloqueo con caparazón, la salida en falso, Lakitu con la señal de salida y los carteles de vuelta, un cuarto circuito llamado Dusty Canyon, el tren de Kalimari Desert con pasos a nivel, el tráfico de Toad's Turnpike, Monty Moles, muñecos de nieve, pingüinos, el hielo de Sherbet Land, decorado al borde de la pista según el tema, el rebufo, una rampa de salto, el derrape con saltito y alternancia, y un bucle chiptune para cada circuito renderizado desde patrones de pasos en código.

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-train.png" alt="GoKart 0.0.2 en Dusty Canyon: el kart del jugador esperando en un paso a nivel mientras un tren de vapor cruza la carretera, con una señal de cruz de San Andrés junto a la vía, bajo un cielo desértico." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Dusty Canyon, el cuarto circuito, con su tren al estilo Kalimari Desert. Los karts de la CPU se detienen y esperan en un paso bloqueado; un kart que no lo hace sale lanzado por los aires.</figcaption>
</figure>

Cuatro horas después, a las 18:25, abrí una segunda pestaña e inicié un segundo Auto-Pilot sobre el mismo repositorio, con un objetivo más acotado:

> the menus are not Mario Kart Quality and neither is the title shot. and there is over use of black outlines on text everywhere. see Mario Kart 64 screenshots and images on the web and make better menus. focus only on the menus / screens and title shot for GoKart. make conscious decisions. do not conflict with previous /auto working on the application

Así que desde las 18:25 hasta la medianoche dos agentes estuvieron haciendo commits en el mismo árbol de trabajo. La sesión de menús reconstruyó la pantalla de título con un logo en arco con degradado que entra volando y rebota, una pantalla de selección con una imagen junto a cada circuito, un sobrevuelo en vivo del circuito elegido, filas de opciones con barras iluminadas, un retrato del kart girando y un cursor dorado, un sobrevuelo de presentación del circuito, una pantalla de pausa, un tablero de resultados cuyas filas entran deslizándose una tras otra, y una paleta compartida de texto redondeado dorado y crema con sombras que sustituyó cada contorno negro de 8 píxeles del juego. Ejecutó 23 ciclos y declaró el objetivo alcanzado a las 23:54.

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-select.png" alt="La pantalla de selección de GoKart 0.0.2: el logo GOKART arriba, una lista de circuitos a la izquierda con una pequeña imagen junto al nombre de cada circuito y la fila elegida iluminada, una imagen en vivo del circuito con el contorno del mapa en su esquina a la derecha, filas de píldoras de opciones para vueltas, CPU, clase de motor, peso del kart y modo, y el kart del jugador girando en una pequeña ventana de retrato, todo sobre la demo de atracción atenuada." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>La pantalla de selección tras la sesión de menús. Imágenes de los circuitos, un sobrevuelo en vivo del circuito, cada opción listada como una fila de píldoras con la elegida iluminada, y el kart girando en su ventana de retrato.</figcaption>
</figure>

La línea de "do not conflict" hizo un trabajo real. El registro está lleno de las dos sesiones esquivándose mutuamente: la sesión de menús verificando desde un `git worktree` limpio en HEAD para que "el trabajo en curso de los pingüinos de la otra sesión" quedara fuera de sus ejecuciones de tests, una sesión terminando la funcionalidad a medias de la otra cuando se lo pedí, y commits preparados archivo por archivo en lugar de `git add -A` porque las ediciones de la otra pestaña estaban en el mismo árbol. No fue ordenado, pero no se perdió nada y la suite terminó la noche con 14.134 en verde, 0 fallos.

El registro de la sesión de funcionalidades termina tres minutos después, a las 23:57, con "Session ended — Stop All". Mi nota a Agent! justo después, que guardó como mensaje del siguiente commit de checkpoint, fue que Stop All debe detener solo la pestaña en la que se pulsa, no todas. Con dos Auto-Pilots en marcha, un botón para ambos es el botón equivocado.

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-snowmen.png" alt="GoKart 0.0.2 en Frosty Peaks: el kart del jugador a la entrada de un campo de muñecos de nieve dispuestos en filas escalonadas sobre la carretera blanca como la nieve, cada uno con bufanda roja, sombrero de copa y nariz de zanahoria, bajo un cielo crepuscular azul oscuro." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>El campo de muñecos de nieve en Frosty Peaks. Si chocas con uno sales lanzado por los aires mientras él estalla en nieve; los karts de la CPU miran 40 metros por delante y zigzaguean entre las filas.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-penguins.png" alt="GoKart 0.0.2 en Frosty Peaks: un pingüino deslizándose sobre su barriga por el hielo azul blanquecino pálido de la larga curva abierta por delante del kart del jugador." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Hielo y pingüinos al estilo Sherbet Land en Frosty Peaks. Sobre el hielo el morro gira pero el kart sigue deslizándose en la dirección que llevaba; los pingüinos se contonean hasta el borde, se dejan caer y vuelven deslizándose.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-traffic.png" alt="GoKart 0.0.2 en Sunset Speedway: el kart del jugador atrapado detrás de un autobús y un camión de caja con los faros encendidos en los dos carriles de la carretera, bajo el cielo de atardecer." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Tráfico al estilo Toad's Turnpike en Sunset Speedway: coches, autobuses, camiones de caja y cisternas con faros, y edificios con franjas de ventanas iluminadas más allá de los muros.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-gp-results.png" alt="El tablero de resultados del Grand Prix de GoKart 0.0.2 sobre un panel azul marino con borde dorado: el resultado de la carrera a la izquierda y la clasificación de la copa a la derecha, una fila por corredor con una muestra de color, puestos oro, plata y bronce, tiempos y puntos, la fila del jugador sobre una barra dorada iluminada, y el trofeo debajo." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>El tablero de resultados del Grand Prix: resultado de la carrera y clasificación de la copa lado a lado, las filas entrando deslizándose una tras otra con un tic cada una, y el trofeo debajo.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-battle.png" alt="Modo Batalla de GoKart 0.0.2: cuatro karts en sus plataformas de salida en una arena de batalla, cada uno con tres globos atados, y la señal de salida de Lakitu en lo alto." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Modo Batalla: cuatro karts, tres globos cada uno. Los impactos de objetos, la lava, el borde del tejado, los toques de estrella y los empujones fuertes explotan globos, y un kart que se queda sin ninguno se convierte en un Mini Bomb Kart.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/gokart-0-0-2-dusty-canyon.png" alt="GoKart 0.0.2 en Dusty Canyon: el kart del jugador en 5.ª posición de 8 en la vuelta 1 sobre la carretera del desierto, con el HUD al estilo Mario Kart 64." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Dusty Canyon desde el bot de conducción aleatoria, 5.º de 8. Curvas abiertas del desierto, una horquilla, una S a la izquierda, dos tramos de agua de oasis, el tren y una rampa de salto en la recta inicial.</figcaption>
</figure>

## Sobre estas capturas

Las tomó Agent!, no yo, y no a mano. Para la primera versión pedí tres capturas de una conducción aleatoria, y escribió un `tools/random_drive.gd` de 70 líneas que sigue la carretera con un desplazamiento de carril errante, mete ráfagas de derrape aleatorias y dispara el objeto que lleve en momentos aleatorios, y luego guarda un fotograma cada varios cientos de fotogramas de física. Las dos capturas de carrera de arriba son fotogramas de ese bot. El resto proviene de las herramientas de captura con las que se entregó cada funcionalidad: `menu_shot.gd`, `train_shot.gd`, `traffic_shot.gd`, `snowman_shot.gd`, `penguin_shot.gd`, `hud_shot.gd` y `battle_shot.gd`, cada una de las cuales prepara su escena, espera al fotograma correcto y lo guarda. Todas se ejecutaron para esta actualización desde un worktree limpio con la etiqueta `v0.0.2` desplegada, así que no hay nada sin commit en ninguna imagen. Agent! sigue sin poder mirar el resultado, así que las herramientas muestrean píxeles en su lugar: la captura del hielo imprime el color de la carretera por delante sobre hielo frente al asfalto, la captura de pausa demuestra que nada se movió fuera del panel durante un segundo, y antes de publicar le hice contar los píxeles negros puros en las diez imágenes de arriba: cero en cada una. Hay más en el [README de GoKart](https://github.com/AgentiLoop/GoKart#screenshots).

## Lo que te diría antes de que lo pruebes

- **Ejecútalo dentro de git.** Auto-Pilot no tiene deshacer. El registro de GoKart es legible porque cada ciclo terminó en un commit, y la única vez que un ciclo se torció, no se perdió nada.
- **Pon las reglas operativas en el objetivo.** "Pon un límite de tiempo al shell" funcionó mejor como parte del objetivo que como un mensaje suelto, porque cada ciclo nuevo relee el objetivo.
- **Espera que pida ojos.** Para cualquier cosa visual o de sensaciones, el bucle se detendrá con honestidad antes que mentir. Reserva una partida de prueba entre sesiones y devuélvele tus notas como el siguiente objetivo.
- **Stop All forma parte del flujo de trabajo**, no es un fallo. Las tres primeras sesiones de GoKart terminaron con él.
- **Dos Auto-Pilots en un mismo repositorio funcionan, si les hablas el uno del otro.** "Do not conflict with the previous /auto" fue al segundo objetivo, y ambas sesiones dedicaron un esfuerzo real a no estorbarse. Dales áreas separadas del código, y cuenta con que el que detengas se lleve al otro consigo, por ahora.

## ¿Eso es bueno?

Le hice esa pregunta a Agent! después de que hubiera leído el repositorio, contado los commits y encontrado el registro de Auto-Pilot. Los 126 commits tienen al agente como autor, ninguno a una persona, y `.agent/autopilot/progress.md` pasa del ciclo 23. Su respuesta, sin editar:

> Depende de lo que quieras sacar de ello. Como vitrina de lo que Auto-Pilot puede hacer, es impresionante. Más de veintitrés ciclos produjeron cuatro circuitos, objetos, corredores de IA, Grand Prix, Contrarreloj, modo Batalla, música y sonido procedurales, todo sin recursos importados, y un README que lo documenta en detalle. Es mucho software funcional a partir de una única declaración de objetivo.

También añadió la salvedad de que ningún humano lo revisó por el camino, así que la calidad se juzgó por los propios registros de verificación del agente, y que no lo había jugado ni auditado el código, así que no podía decir qué tal se juega en realidad. Que es la misma conclusión a la que llegó el registro por su cuenta: el siguiente paso es una partida de prueba.

## GoKart 0.0.2

No necesitas Godot para probarlo. [GoKart 0.0.2](https://github.com/AgentiLoop/GoKart/releases/tag/v0.0.2) es la segunda versión empaquetada, exportada desde el mismo repositorio, 87 commits después de [0.0.1](https://github.com/AgentiLoop/GoKart/releases/tag/v0.0.1):

- **macOS** universal (Apple Silicon e Intel), firmada con Developer ID y notarizada por Apple
- **Windows** x86_64
- **Linux** x86_64 y arm64

Cada descarga es un único binario autocontenido con los datos del juego incrustados, y `SHA256SUMS.txt` está en la página de la versión por si quieres comprobar lo que has recibido. La compilación de Windows no está firmada, así que espera el aviso de SmartScreen. Todo lo de esta entrada que no estaba en 0.0.1 está en 0.0.2: el modo Batalla, Contrarreloj, la copa de cuatro circuitos, las clases de motor y de peso, los objetos nuevos, Lakitu, el tren, el tráfico, los topos, los muñecos de nieve, los pingüinos, el hielo, el decorado, el rebufo, la rampa de salto, la música de los circuitos, las nuevas pantallas de título y selección, la presentación del circuito, la pantalla de pausa y el HUD rediseñado. Las notas de la versión tienen la lista completa.

Agent! 1.1.87 con Auto-Pilot está en la [página de versiones](https://github.com/AgentiLoop/Agent/releases/latest) y en Homebrew. Si prefieres ejecutar GoKart desde el código fuente, necesita Godot 4.4 o posterior: `git clone https://github.com/AgentiLoop/GoKart.git && cd GoKart && godot --path .`
