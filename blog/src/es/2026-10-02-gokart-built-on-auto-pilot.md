---
title: GoKart: un juego de carreras al estilo Mario Kart que Auto-Pilot construyó en una tarde
description: Dale a Auto-Pilot de Agent! un único objetivo - "crea un clon de Mario Kart llamado GoKart" - y vuelve para encontrarte un juego de carreras en Godot 4 con tres circuitos, ocho objetos, rivales controlados por IA y 3.344 comprobaciones de test en verde. Esto es lo que dice el registro que ocurrió de verdad, incluidas las partes en las que se quedó atascado.
tags: Auto-Pilot, Vitrina, Godot
---
<figure style="margin:2rem 0">
<img src="/gokart-green-hills-drift.png" alt="GoKart en el circuito Green Hills: vista de cámara de persecución del kart del jugador en pleno derrape sobre una carretera gris con muros a rayas rojas y blancas, suelo verde y cielo azul. El HUD muestra la 1.ª posición, los contadores de vuelta y tiempo y un minimapa del circuito en la esquina inferior izquierda." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Green Hills, vuelta 1, derrapando en primera posición. Cada malla, shader y sonido de este fotograma se generó desde código.</figcaption>
</figure>

La entrada de ayer presentó [Auto-Pilot](/blog/agent-1-1-87-and-agentiloop-cli-0-0-5/): escribe `/auto <objetivo>` en Agent! para Mac y ejecuta ciclos sin supervisión hacia ese objetivo hasta que pulsas Stop All. Esta entrada va de lo que salió por el otro lado cuando lo apunté a un juego.

El objetivo, pegado más o menos tal como lo escribí:

> create a Mario Kart clone called GoKart with all Mario Kart effects. I believe Godot 4 can do the Mario Kart effects, but I haven't built any of them yet: drift sparks and boost flames (GPUParticles3D), speed lines and boost blur (screen-space shaders, glow and tonemapping), item effects and tire trails (shaders plus ribbon meshes), kart movement (VehicleBody3D or custom arcade physics). Write unit tests and test the game frequently.

Presupuesto: sin límite de tiempo, ciclos ilimitados. El primer commit llegó a las 12:39. A las 16:32 de esa misma tarde el repositorio tenía 33 commits. Hoy tiene 47 archivos GDScript, unas 5.500 líneas de GDScript y código de shaders, y una suite unitaria que pasa 3.344 comprobaciones. Todo está en GitHub, en [AgentiLoop/GoKart](https://github.com/AgentiLoop/GoKart).

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
<img src="/gokart-sunset-speedway.png" alt="GoKart en el circuito Sunset Speedway: el kart del jugador a toda velocidad sobre un circuito arenoso bajo un cielo de atardecer de naranja a violeta. El HUD muestra la 4.ª posición, la vuelta 1 y el contorno en el minimapa de un circuito largo con una horquilla." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Sunset Speedway, el segundo circuito, añadido en el ciclo 12 junto con el menú de título. Más largo que Green Hills, con una horquilla y una chicane.</figcaption>
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

Ese es el comportamiento correcto. El objetivo era "la dirección se siente mal" y "los muros parpadean", y ningún test sin interfaz puede cerrar ese objetivo. Auto-Pilot no tiene límite de iteraciones, así que habría seguido comprobando para siempre. La sesión terminó tras el ciclo 8, y lo que GoKart necesitaba a continuación era una partida de prueba, no otro ciclo.

<figure style="margin:2rem 0">
<img src="/gokart-frosty-peaks.png" alt="GoKart en el circuito Frosty Peaks: el kart del jugador a toda velocidad sobre un circuito blanco como la nieve bajo un cielo crepuscular azul oscuro. El HUD muestra la 2.ª posición, la vuelta 1, la velocidad en km/h y el minimapa." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Frosty Peaks, añadido en el ciclo 14 como una entrada nueva en la biblioteca de circuitos. Los tests por circuito lo recogieron automáticamente.</figcaption>
</figure>

## Sobre estas capturas

Las tomó Agent!, no yo, y no a mano. Pedí tres capturas de una conducción aleatoria, y escribió un `tools/random_drive.gd` de 70 líneas que sigue la carretera con un desplazamiento de carril errante, mete ráfagas de derrape aleatorias y dispara el objeto que lleve en momentos aleatorios, y luego guarda un fotograma cada varios cientos de fotogramas de física. Se ejecutó una vez por circuito, y las tres de arriba son un fotograma de cada uno. También están en el [README de GoKart](https://github.com/AgentiLoop/GoKart#screenshots).

## Lo que te diría antes de que lo pruebes

- **Ejecútalo dentro de git.** Auto-Pilot no tiene deshacer. El registro de GoKart es legible porque cada ciclo terminó en un commit, y la única vez que un ciclo se torció, no se perdió nada.
- **Pon las reglas operativas en el objetivo.** "Pon un límite de tiempo al shell" funcionó mejor como parte del objetivo que como un mensaje suelto, porque cada ciclo nuevo relee el objetivo.
- **Espera que pida ojos.** Para cualquier cosa visual o de sensaciones, el bucle se detendrá con honestidad antes que mentir. Reserva una partida de prueba entre sesiones y devuélvele tus notas como el siguiente objetivo.
- **Stop All forma parte del flujo de trabajo**, no es un fallo. Las tres primeras sesiones de GoKart terminaron con él.

Agent! 1.1.87 con Auto-Pilot está en la [página de versiones](https://github.com/AgentiLoop/Agent/releases/latest) y en Homebrew. GoKart necesita Godot 4.4 o posterior: `git clone https://github.com/AgentiLoop/GoKart.git && cd GoKart && godot --path .`
