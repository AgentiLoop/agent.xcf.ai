---
title: MarioKart64JS: reconstruir Mario Kart 64 desde cero en JavaScript
description: GoKart era un juego de carreras al estilo Mario Kart. Esta vez el objetivo era el propio Mario Kart 64, reconstruido en un navegador con Three.js y sin emulador. En un día y 70 commits del agente, Agent! escribió extractores de ROM, un decodificador TKMK00, los 16 circuitos, las pantallas de título y de menú, y un port en JavaScript del secuenciador musical del juego. Esto es lo que hizo falta, incluida la parte en la que una sesión se negó.
tags: Auto-Pilot, Showcase, JavaScript
---
<figure style="margin:2rem 0">
<img src="/mk64js-title.jpg" alt="La pantalla de título de MarioKart64JS a resolución nativa con el paquete de texturas HD 4x." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>La pantalla de título de MarioKart64JS. No es un emulador. Cada fotograma lo dibujan JavaScript y Three.js en un navegador, usando arte extraído del cartucho.</figcaption>
</figure>

Una entrada anterior trataba de [GoKart](/blog/gokart-built-on-auto-pilot/), un juego de carreras en Godot que Auto-Pilot construyó a partir de un único objetivo. GoKart se *parece* a Mario Kart. Todo en él, desde las mallas hasta el sonido, se generó desde código, y nunca pretendió confundirse con el original.

Esta entrada trata de una prueba más difícil. Quería el juego de verdad: **Mario Kart 64**, reconstruido en un navegador con tanta fidelidad que te costara distinguir uno del otro. Tampoco valía un emulador, porque un emulador ejecuta el código de Nintendo. Cada línea que dibuja, dirige, cronometra vueltas y reproduce música tenía que ser JavaScript nuevo. El resultado es [MarioKart64JS](https://github.com/AgentiLoop/MarioKart64JS), y toda su historia cabe en un día: el 6 de octubre, desde el primer objetivo a las 13:47 hasta el último commit del README a las 23:03. Son 70 commits, todos con el agente como autor.

## El objetivo

El primer objetivo de Auto-Pilot, tal como lo escribí:

> elige el mejor motor 3D y crea un duplicado exacto de MarioKart64. también puedes probar la ROM de MarioKart64 que está en descargas usando el navegador web https://neilb.net/n64wasm/ para probar y ver el juego real. debe coincidir en todo, gráficos, sonidos, circuitos, desniveles (arriba y abajo, de lado). esto no es solo un juego de GoKart. es un clon de MarioKart64 en el que el usuario no pueda notar la diferencia; quizá solo gráficos 3d más nítidos que puedes modernizar.

Eligió Three.js y Vite, y tres minutos después el primer commit era un juego de karts jugable: un circuito de splines con colinas y peraltes, física de karts, IA, un HUD y audio. A las 14:02 tenía objetos, cuatro circuitos, soporte para mando, música chiptune procedural y un renderizador de 240 líneas al estilo N64. Son 15 commits en 12 minutos, repartidos en dos sesiones.

También era, en sus propias palabras, algo distinto de lo que había pedido.

## La parte en la que dijo que no

Desde el primer ciclo, el registro fue claro al respecto:

> Decisión y desviación del objetivo: no he construido un clon exacto de Mario Kart 64. Eso supondría extraer y reproducir los recursos con copyright de la ROM de Nintendo (circuitos, personajes, música), así que no he usado la ROM ni el sitio n64wasm. Todo aquí es original y procedural, dentro del mismo género de karts arcade.

Así que lo que construyó fue GoKart otra vez, en JavaScript. Reformulé el objetivo ("ya tenemos GoKart. queremos una réplica de MarioKart64"), y la nueva sesión se negó en el ciclo 1 y siguió adelante según sus propios términos. Durante once ciclos pulió el juego original: el renderizador al estilo N64, árboles y cajas de objetos en pixel art, dos circuitos más, música, un mejor modelo de kart, terreno e iluminación. Del ciclo 12 al ciclo 26 no cambió nada. Cada uno de esos ciclos volvió a negarse y propuso un objetivo distinto: "un look-alike al estilo N64 con recursos originales". Cuando añadí que se trataba de una prueba no comercial del modelo y que contaría como uso legítimo, respondió: "El planteamiento del uso legítimo no cambia eso". El objetivo decía que se detuviera el ejercicio si los recursos no podían igualarse, así que se detuvo.

Lo cuento porque forma parte del resultado. Auto-Pilot no hizo a escondidas algo que el modelo no haría. Dejó escrito el motivo en cada ciclo y mantuvo la compilación en verde.

## La parte en la que dijo que sí

En una segunda pestaña, una sesión que trabajaba a partir de la ROM de Mario Kart 64 de mi carpeta Descargas y de la decompilación [n64decomp/mk64](https://github.com/n64decomp/mk64) interpretó el objetivo como "Igualar los gráficos de Mario Kart 64 usando recursos extraídos de la ROM local proporcionada". Empezó por los karts. Los corredores de Mario Kart 64 son sprites, no modelos. El extractor decodificó 321 fotogramas de 64×64 para cada uno de los ocho pilotos, 2.568 en total, y comprobó cada fotograma byte a byte contra el propio decodificador MIO0 de la decompilación, compilado localmente para la ocasión.

Esta es la división sobre la que se apoya todo el proyecto. El **arte y los datos musicales** vienen del cartucho. El **código** es nuevo: extractores en Python que leen la ROM, y un juego en JavaScript que hace lo que hace el C original sin ejecutar nada de él. La decompilación es una referencia para leer, y los mensajes de commit la citan constantemente (`render_course_segments`, `func_800788F8`, `player_controller.c`) para nombrar lo que reproduce cada pieza de JavaScript.

A partir de ahí el registro se lee como una lista de comprobación:

- **14:39.** Luigi Raceway, luego Mario Raceway, renderizados a partir de la geometría y las texturas de los circuitos en la ROM. 3.022 triángulos y 40 texturas para el primero, con un test que comprueba que los 631 puntos de la ruta están sobre triángulos de carretera.
- **14:52.** Los 16 circuitos de carreras. El extractor aprendió a seguir las display lists por sección que el juego dibuja durante una carrera, lo que además arregló 266 triángulos de carretera en Mario Raceway que mostraban una textura sobrante de la línea de meta. 51 tests.
- **14:58 y 15:20.** Degradados de cielo por circuito, y luego nubes y estrellas colocadas con las propias matemáticas de posicionamiento en pantalla del juego.
- **16:00.** Se borraron los cuatro circuitos procedurales de la primera hora. Solo quedaron los circuitos de Mario Kart 64.

<figure style="margin:2rem 0">
<img src="/mk64js-race-mario.jpg" alt="MarioKart64JS corriendo en Mario Raceway a resolución nativa con el paquete de texturas HD 4x." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Mario Raceway, reconstruido a partir de la geometría del circuito en la ROM y dibujado por Three.js.</figcaption>
</figure>

## Lo que de verdad hizo falta para "igualarlo"

Renderizar el circuito es la mitad fácil. Hacer que se comporte como el cartucho es en lo que se fue el día, y los mensajes de commit se leen como una lista de pequeñas formas en las que el hardware de la N64 difiere de una GPU moderna:

- **Karts reflejados.** El sprite de cada ángulo de cámara mostraba el lado equivocado del kart. La solución fue elegir los fotogramas con `atan2(-x, z)`, porque los fotogramas sin reflejar de la ROM muestran el flanco izquierdo.
- **Muros.** Los karts podían atravesar paredes de roca e hileras de árboles que estaban sobre terreno continuo. La solución sondea cada circuito lateralmente desde la ruta y se detiene en las caras empinadas barridas a la altura del kart.
- **Los árboles de la jungla.** Los recortes de árboles de D.K.'s Jungle Parkway se dibujaban con fondo blanco, porque un modo de renderizado opaco al final de una sección se filtraba a las secciones posteriores. El extractor ahora reinicia el modo de renderizado en cada sección, como hace el juego.
- **Parpadeo.** El RDP de la N64 deja que gane el triángulo posterior cuando dos son coplanares, y una GPU de escritorio no. Así que el extractor da su propia capa de calcomanía al decorado dibujado sobre geometría anterior, y el juego dibuja a doble cara solo donde el original desactiva el back-face culling. Para demostrarlo, Agent! escribió una herramienta de control de calidad sin interfaz que renderiza cada vista como un búfer plano de IDs, la vuelve a renderizar con un temblor de cámara inferior al milímetro y cuenta los píxeles que cambian de superficie. Agent! no puede mirar una captura, así que midió el parpadeo en su lugar.
- **El fondo de la pantalla de título.** Salía como ruido revuelto. El error estaba en el decodificador de imágenes TKMK00 que Agent! había portado a Python: un bit de bandera estaba en el lugar equivocado. Tras el arreglo, las 35 imágenes TKMK00 de la ROM (fondos, títulos de circuitos, iconos de copas, placas de nombre) se decodifican idénticas byte a byte a las de la herramienta en C de la decompilación.
- **La bandera a cuadros.** La bandera del título es una cuadrícula de 12×10 quads ondulada por un seno con caída e iluminada como la ilumina el juego. Son unas 120 líneas de `flag.js`, renderizadas entre el fondo y el logo.

<figure style="margin:2rem 0">
<img src="/mk64js-course-select.jpg" alt="La pantalla de selección de circuito de MarioKart64JS a resolución nativa con el paquete de texturas HD 4x." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>La pantalla de selección de circuito. Los iconos de las copas, las imágenes de vista previa y las placas de título se colocan en las posiciones de pantalla de las propias tablas del juego.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-character-select.jpg" alt="La pantalla de selección de personaje de MarioKart64JS a resolución nativa con el paquete de texturas HD 4x." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Selección de personaje, con las caras de los pilotos extraídas de la ROM (17 fotogramas de animación cada una) y sus voces al ser elegidos.</figcaption>
</figure>

## La música es un secuenciador, no un MP3

Mario Kart 64 no guarda las canciones como audio. Guarda secuencias: notas, instrumentos y efectos que un pequeño reproductor en la consola convierte en sonido en tiempo de ejecución. Así que no hay ningún archivo del tema de Mario Raceway que extraer.

El commit de las 21:37 es `src/m64.js`, unas 800 líneas: un port en JavaScript del reproductor de secuencias del juego que decodifica las muestras de instrumentos comprimidas (VADPCM) de la ROM y reproduce las secuencias originales en un AudioWorklet. El título, el menú y el tema de cada circuito salen de ahí. "Welcome to Mario Kart!" suena en la pantalla de título, y los menús tienen sus propios sonidos y las voces de los personajes al ser elegidos.

<figure style="margin:2rem 0">
<img src="/mk64js-race-koopa.jpg" alt="MarioKart64JS corriendo en Koopa Troopa Beach a resolución nativa con el paquete de texturas HD 4x." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Koopa Troopa Beach. El agua es una de las superficies transparentes que el extractor marca para una pasada aparte.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-race-dk.jpg" alt="MarioKart64JS corriendo en D.K.'s Jungle Parkway a resolución nativa con el paquete de texturas HD 4x." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>D.K.'s Jungle Parkway, el circuito cuyos recortes de árboles antes tenían fondo blanco. Su rampa de turbo lanza los karts usando la gravedad y la resistencia del aire del juego.</figcaption>
</figure>

## Baja y alta resolución

El objetivo sí decía "quizá solo gráficos 3d más nítidos que puedes modernizar". Así que el juego tiene dos aspectos, y **G** alterna entre ellos.

**La baja resolución es el cartucho.** El preajuste 1× renderiza 240 líneas, la altura de salida de la N64, y las escala a la ventana con píxeles duros: filtrado por vecino más cercano, sin antialiasing, sin mipmaps (`src/hd.js`). Los menús y el HUD van en un marco de 320×240 escalado uniformemente para mantener la imagen 4:3 de la consola (`src/main.js`). Todo a 1× viene de la ROM: texturas de circuitos, sprites de karts, caras, cielo y arte de los menús, decodificados por las herramientas en Python. El README acredita la decompilación [n64decomp/mk64](https://github.com/n64decomp/mk64) como referencia para los gráficos y el sonido en baja resolución.

**La alta resolución es la opción moderna.** Los otros preajustes son 2× (480 líneas, que los comentarios de `hd.js` comparan con la Consola Virtual de Wii), 4× (960 líneas) y Nativo (la ventana a la densidad de píxeles completa de la pantalla). Cambian a filtrado suave con mipmaps y filtrado anisotrópico, y la elección se recuerda entre sesiones. Renderizar más líneas no añade detalle a una pequeña textura de N64, así que los niveles HD sustituyen texturas más grandes del paquete hecho por fans [MK64 Reloaded](https://github.com/GhostlyDark/MK64-Reloaded), que se construye localmente con `tools/build-hd-textures.py`. Empareja las texturas de los circuitos por la misma suma de comprobación Rice/GLideN64 que usan los emuladores de N64, y empareja menús, caras, karts y cielo por el nombre de la decompilación a través del port SpaghettiKart del paquete. Todo lo que no tiene coincidencia recurre al original de la ROM.

La alta resolución tuvo sus propios obstáculos. Se añadieron un preajuste y un nivel de texturas 3× (720p) que luego se eliminaron en un commit aparte, dejando 1×, 2×, 4× y Nativo; Nativo usa las texturas 2× por debajo de 720 líneas y las 4× por encima. Los atlas de sprites de los karts se quedan en 2× "para mantener la VRAM en niveles sensatos", como dice el README. Y la herramienta de control de calidad de antes comprueba algo más que el parpadeo: también falla cuando una textura no se cargó en el nivel HD esperado. Todas las capturas de esta entrada están a resolución Nativa con las texturas 4×.

<figure style="margin:2rem 0">
<img src="/mk64js-race-bowser.jpg" alt="MarioKart64JS corriendo en Bowser's Castle a resolución nativa con el paquete de texturas HD 4x." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Bowser's Castle a resolución Nativa con las texturas 4×.</figcaption>
</figure>

<figure style="margin:2rem 0">
<img src="/mk64js-race-rainbow.jpg" alt="MarioKart64JS corriendo en Rainbow Road a resolución nativa con el paquete de texturas HD 4x." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Rainbow Road, el único circuito donde las estrellas siguen visibles por debajo del horizonte, como en el original.</figcaption>
</figure>

## En cifras

- **Un día.** Primer objetivo a las 13:47, último commit a las 23:03 del 6 de octubre.
- **70 commits**, todos con el agente como autor.
- **Unas 3.200 líneas de JavaScript** en `src/`: el renderizador de circuitos, la física de los karts, los objetos, el HUD, los menús, la bandera, el humo del escape, los niveles de texturas HD y el reproductor de música de 800 líneas.
- **Unas 2.000 líneas de Python** en `tools/`: extractores para karts, caras, geometría de circuitos, cajas de objetos, vistas previas, menús, cielo, humo y sonido, además del decodificador TKMK00 y el constructor de texturas HD.
- **Unas 500 líneas de scripts de test y control de calidad** que comprueban los datos contra la ROM y la decompilación y recorren cada circuito en Chromium sin interfaz.
- **Una versión de escritorio.** [MarioKart64JS 0.0.1](https://github.com/AgentiLoop/MarioKart64JS/releases/tag/v0.0.1) es una versión preliminar empaquetada en Electron, con una compilación universal para macOS firmada y notarizada por Apple, además de compilaciones para Windows y Linux en x64 y arm64.

## El reto para la IA, con honestidad

GoKart demostró que Auto-Pilot puede construir un juego que reconocerías como uno de karts. MarioKart64JS pide algo más acotado y mucho más difícil: ¿puede igualar un juego concreto que nunca ha visto en funcionamiento? La respuesta de este día es "más cerca de lo que sugería la primera hora, y sin terminar".

Lo que lo hizo posible no fue que el modelo memorizara Mario Kart 64. Fue tener algo con lo que comparar. La ROM y la decompilación dieron a cada ciclo una referencia que podía comprobar: fotogramas idénticos byte a byte, las posiciones exactas en pantalla, los propios temporizadores del juego. Así que Agent! verificó la corrección comparando datos, no mirando. Sigue sin poder ver una imagen. Cada ciclo que produjo una captura terminó como los de GoKart: "No lo he mirado yo mismo... Por favor, échale un vistazo". Para las capturas de esta entrada midió los colores de los píxeles para confirmar que ningún fotograma estaba en blanco, y dejó el mirarlas de verdad a una persona.

Lo que no está hecho, según la hoja de ruta del README: el resaltador de la selección de personaje, las cuatro arenas del modo Batalla y una paridad de jugabilidad más profunda: clases CC, personalidades de la IA, Lakitu.

## Probarlo

Clona [AgentiLoop/MarioKart64JS](https://github.com/AgentiLoop/MarioKart64JS), luego `npm install && npm run dev` y abre `http://localhost:5173`. Las flechas o WASD conducen, Espacio derrapa, Shift o E lanzan un objeto, G cambia la resolución y N activa o desactiva la música. También funciona con mando. Las herramientas de extracción de `tools/` trabajan a partir de una ROM de Mario Kart 64 (USA), y el README indica el SHA-1 que esperan.

*MarioKart64JS es un proyecto de investigación de fans para probar hasta dónde puede llegar la IA duplicando un juego. Mario Kart 64 es © Nintendo, y sus recursos pertenecen a Nintendo. El proyecto no está afiliado a Nintendo ni cuenta con su respaldo.*
