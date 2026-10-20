---
title: AgentiLoop Racing, Prototype III: un simulador de F1 en tu navegador
description: AgentiLoop Racing es un simulador de carreras de monoplazas que funciona en el navegador, creado con Agent! en Three.js. Tiene física a 240 Hz, 18 circuitos reales, una parrilla de rivales con IA, paradas en boxes, compuestos de neumáticos, combustible, ERS y DRS. Juega en f1.gokart.games.
tags: Showcase, JavaScript
---
<figure style="margin:2rem 0">
<img src="/agentiloop-racing-og.jpg" alt="AgentiLoop Racing: un monoplaza en pista en el simulador del navegador." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>AgentiLoop Racing, Prototype III. Todos los coches de la parrilla son un modelo RB22 de 2026, repintado con sus propios colores y nombres de patrocinadores.</figcaption>
</figure>

**Juega ahora: [f1.gokart.games](https://f1.gokart.games).** Sin descargas ni instalación. Necesita un navegador con WebGL y se juega con teclado o con un mando de Xbox (u otro mando estándar).

AgentiLoop Racing es un simulador de carreras al estilo de la F1 escrito en JavaScript puro y Three.js. El primer commit, un modelo de vehículo determinista de cuatro ruedas, entró la tarde del 16 de octubre. Tres días y 109 commits después, corre contra una parrilla completa de IA en 18 circuitos reales, con paradas en boxes, compuestos de neumáticos, combustible, ERS y DRS, un sonido de motor generado a partir de la física y una cámara de cockpit cuyos retrovisores muestran los coches que llevas detrás. Lo escribió Agent!, un commit pequeño y probado cada vez.

Una etiqueta honesta de entrada, la misma que lleva el README: es un **prototipo, no un simulador de Fórmula 1 validado**. Los parámetros del coche son supuestos ilustrativos, no datos medidos de F1.

## Primero, la física

El proyecto empezó como un banco de pruebas de física y el 3D vino después. `physics.mjs` avanza el coche a una frecuencia fija de **240 Hz**. Cada rueda tiene su propia inercia y su propio deslizamiento, y cada neumático tiene una envolvente de agarre que va del agarre máximo al derrape, con relajación del ángulo de deriva, temperatura y desgaste. La carrocería suspendida se inclina, cabecea y se hunde bajo la carga aerodinámica, y se puede ver en el coche 3D. La caja de cambios es automática o de levas, y hay una marcha atrás protegida para cuando acabas mirando a un muro.

La unidad de potencia también está modelada. El combustible se lleva como masa real, así que el coche se aligera a medida que lo quema. El híbrido despliega hasta 120 kW por encima de 100 km/h, dentro de 4 MJ por vuelta, y recupera energía en las frenadas.

El conjunto de pruebas es el test runner integrado de Node y nada más: `node --test` ejecuta hoy 158 pruebas, todas superadas. Comprueban cosas como que un coche a fondo nunca atraviese un muro, y que el modelo 3D toque el suelo solo con los neumáticos y el fondo plano.

## 18 circuitos reales

<figure style="margin:2rem 0">
<img src="/agentiloop-racing-monza.jpg" alt="AgentiLoop Racing: una carrera en Monza contra la parrilla de IA." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Una carrera en Monza. El panel de tiempos, la clasificación y el minimapa se actualizan en directo durante la carrera.</figcaption>
</figure>

Además de un circuito de pruebas ficticio en un estadio, hay 18 circuitos reales, de Bahrain a Miami, incluidos Monza, Silverstone, Spa y Monaco, con trazados construidos a partir de posiciones reales de los coches. Los datos reales ajustaron el resto:

- **Las zonas de DRS** proceden de la telemetría de carrera de 2024 (OpenF1): donde los pilotos abrían y cerraban realmente el alerón. Monaco tiene una sola zona, en la recta de boxes.
- **El agarre se calibró con velocidades reales en curva.** En los 18 circuitos, la diferencia entre las vueltas del piloto automático y las vueltas rápidas reales en carrera pasó del 17,9 % al 5,8 %. En Monaco la vuelta del piloto automático pasó de 84,2 s a 74,4 s, frente a 73,9 s reales.
- **Las curvas cerradas se abrieron** hasta un radio mínimo de 15 m, para que los coches puedan tomar Ste Devote en Monaco.
- **Todos los circuitos tienen un pit lane** junto a la recta de salida y meta, con un límite de 80 km/h y un box para cada coche.

<figure style="margin:2rem 0">
<img src="/agentiloop-racing-monaco.jpg" alt="AgentiLoop Racing: una carrera en Monaco." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>Monaco, en carrera contra la parrilla de IA.</figcaption>
</figure>

## Correr contra la IA

Un circuito real se abre como contrarreloj en solitario; pulsa **O**, o añade `?race` a la URL, para correr contra la parrilla. La salida son cinco semáforos rojos, uno por segundo, y después una espera aleatoria antes de que se apaguen. Si te mueves más de medio metro antes de tiempo, te cae una penalización de 5 segundos por salida anticipada. Mientras los semáforos están encendidos, las teclas **1–5** te ponen en el coche de esa posición de la parrilla.

Los coches de la IA siguen la trazada ideal, se rebufan unos a otros en las rectas, salen del rebufo, usan el DRS cuando están a menos de un segundo en el punto de detección y se tiran por dentro en las frenadas. En el commit que ajustó los adelantamientos, las carreras de 3 vueltas en los 18 circuitos pasaron de 16 adelantamientos a 34 y de 8 contactos a ninguno. Un coche que se queda atascado contra una barrera mete la marcha atrás, retrocede por una trayectoria comprobada para evitar tráfico y muros, y se reincorpora.

Se aplican las reglas de carrera. Todos los que terminan tienen que usar dos compuestos de neumáticos, así que tienes que parar una vez o quedas descalificado. **B** pide al equipo blandos, medios o duros. Si excedes la velocidad en el pit lane, son +5 s.

Cada sesión empieza con el piloto automático, así que el coche se conduce solo hasta que tomas el control. Pulsa **P**, toca un mando o cambia de marcha, y es tuyo.

## El coche y el cockpit

Todos los coches de la parrilla usan un modelo RB22 de 2026 de Tyler_Dave (CC BY 4.0, de Sketchfab). Al cargar, `rb22.mjs` lo repinta con los colores de cada coche y proyecta sobre él los nombres de patrocinadores del proyecto y un número de carrera. De cerca, cada pieza del modelo se subdivide y suaviza, con versiones de menos detalle a mayor distancia.

Pulsa **C** para el cockpit. El ojo del piloto va sobre la carrocería suspendida, así que el balanceo, el cabeceo y el movimiento vertical mueven la vista, y la cabeza se mueve un poco con las fuerzas g. Los retrovisores renderizan la escena reflejada a través de cada cristal, sin tus propios neumáticos traseros, para que veas la pista y los coches de detrás.

El sonido también se sintetiza a partir de la física: una nota de encendido de V6 que sigue las revoluciones, el silbido del turbo, el chirrido de los neumáticos por el deslizamiento y un ruido del viento que crece con la velocidad.

<figure style="margin:2rem 0">
<img src="/agentiloop-racing-spa.jpg" alt="AgentiLoop Racing: una contrarreloj en Spa-Francorchamps." style="display:block;width:100%;height:auto;border-radius:20px">
<figcaption>La contrarreloj de Spa.</figcaption>
</figure>

## Míralo

<figure style="margin:2rem 0">
<div style="position:relative;padding-top:56.25%;border-radius:20px;overflow:hidden">
<iframe src="https://www.youtube-nocookie.com/embed/2RluAIH3iQw?rel=0&amp;modestbranding=1&amp;color=white" title="AgentiLoop Racing — F1 simulator built with AgentiLoop.ai in Three.js" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="position:absolute;inset:0;width:100%;height:100%;border:0"></iframe>
</div>
</figure>

## Pruébalo

- [Una carrera en Monza](https://f1.gokart.games/?track=monza&race)
- [La contrarreloj de Spa](https://f1.gokart.games/?track=spa)
- [Una carrera de 5 vueltas en Spa con blandos](https://f1.gokart.games/?track=spa&race&laps=5&tyre=soft)

El código fuente está en [AgentiLoop/F1](https://github.com/AgentiLoop/F1). No tiene dependencias de npm ni bundler: Three.js va incluido en el repositorio, así que basta con `python3 -m http.server` en la carpeta para ejecutarlo en local. El propio sitio es un Cloudflare Worker que sirve el repositorio como archivos estáticos.

*AgentiLoop Racing es un proyecto independiente y no está afiliado a la Fórmula 1, la FIA ni a ningún equipo. Los modelos 3D conservan sus propias licencias; consulta `models/CREDITS.md` en el repositorio.*
