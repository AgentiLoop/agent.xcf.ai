---
title: ¿Qué es un bucle de agente? Un robot, un sándwich y el arte de volver a intentarlo
description: Mirar, elegir, actuar, comprobar. Una guía ilustrada y juguetona sobre los bucles de agente, tan sencilla que la entiende un niño de cinco años y con mucho para los mayores.
tags: Explicaciones, Bucles de agente
---
Imagina un robotito llamado Pip.

Le dices: **«Por favor, hazme un sándwich de mermelada».**

Pip mira la mesa. Hay pan. Hay mermelada. Hay una cuchara con una cantidad sospechosa de mantequilla de cacahuete.

¿Anuncia Pip: «¡Sándwich terminado!»?

No. Eso sería un discurso, no un sándwich.

Pip necesita **mirar, elegir un pasito, darlo y comprobar qué ha pasado**. Entonces Pip puede decidir qué hacer a continuación.

Ese patrón que se repite es un **bucle de agente**.

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 360" role="img" aria-labelledby="pip-title pip-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="pip-title">Pip tiene un objetivo, pero todavía no un sándwich</title>
<desc id="pip-desc">Un simpático robot azul mira dos rebanadas de pan y un tarro de mermelada. Un bocadillo de diálogo dice: Un plan no es un sándwich.</desc>
<rect width="760" height="360" rx="20" fill="#eef6ff"/>
<path d="M300 104l-26 24 58-24" fill="#fff"/>
<rect x="265" y="28" width="450" height="76" rx="24" fill="#fff" stroke="#b6c8e4" stroke-width="3"/>
<text x="490" y="75" text-anchor="middle" font-family="system-ui,sans-serif" font-size="27" font-weight="700" fill="#173452">Un plan no es un sándwich.</text>
<path d="M44 282H716" stroke="#8b684c" stroke-width="13" stroke-linecap="round"/>
<path d="M103 242V276M187 242V276M217 213L260 233" fill="none" stroke="#173452" stroke-width="6" stroke-linecap="round"/>
<rect x="77" y="127" width="140" height="115" rx="27" fill="#559ef5" stroke="#173452" stroke-width="4"/>
<path d="M147 127V100" stroke="#173452" stroke-width="5"/><circle cx="147" cy="91" r="10" fill="#efb943"/>
<circle cx="117" cy="168" r="12" fill="#fff"/><circle cx="177" cy="168" r="12" fill="#fff"/>
<circle cx="120" cy="169" r="5" fill="#173452"/><circle cx="180" cy="169" r="5" fill="#173452"/>
<path d="M121 201Q147 222 173 201" fill="none" stroke="#173452" stroke-width="6" stroke-linecap="round"/>
<g transform="translate(0 12.5)"><path d="M328 260V217Q309 186 349 178Q380 168 402 187Q422 175 445 190Q472 205 449 223V260Z" fill="#fbe3ad" stroke="#ae703f" stroke-width="6"/>
<path d="M353 240V212Q389 190 428 212V240Z" fill="#d94877"/></g>
<path transform="translate(0 9.5)" d="M465 263V225Q449 195 483 187Q517 172 547 191Q578 181 590 211L582 263Z" fill="#fbe3ad" stroke="#ae703f" stroke-width="6"/>
<g transform="translate(0 1)"><rect x="622" y="191" width="60" height="82" rx="12" fill="#d94877" stroke="#173452" stroke-width="3"/>
<rect x="617" y="181" width="70" height="15" rx="5" fill="#173452"/>
<text x="652" y="239" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" font-weight="700" fill="#fff">MERMELADA</text></g>
<text x="147" y="326" text-anchor="middle" font-family="system-ui,sans-serif" font-size="21" fill="#173452">Te presento a Pip.</text>
<text x="495" y="326" text-anchor="middle" font-family="system-ui,sans-serif" font-size="21" fill="#173452">El objetivo: un sándwich de mermelada.</text>
</svg>
<figcaption>Pip es nuestro ayudante imaginario. Ningún robot real acabó pegajoso durante la creación de esta ilustración.</figcaption>
</figure>

## Toda la idea, en cuatro palabritas

**Mirar. Elegir. Actuar. Comprobar.**

- **Mirar:** ¿Qué está pasando ahora mismo?
- **Elegir:** ¿Qué cosa útil puedo hacer a continuación?
- **Actuar:** Hacer esa cosa.
- **Comprobar:** ¿Qué ha pasado de verdad? ¿Hemos terminado?

Si el trabajo no está terminado, se da otra vuelta, con la información nueva.

Un **bucle** simplemente significa que algo se repite. Un **agente** es un sistema capaz de dar pasos hacia un objetivo usando las herramientas y los permisos que se le han dado.

Júntalos: **un bucle de agente permite a un ayudante actuar, ver el resultado y decidir qué viene después.**

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 520" role="img" aria-labelledby="loop-title loop-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="loop-title">Mirar, elegir, actuar, comprobar, y saber cuándo parar</title>
<desc id="loop-desc">Un diagrama de flujo avanza en el sentido de las agujas del reloj de Mirar a Elegir, a Actuar y a Comprobar. Comprobar vuelve a Mirar cuando queda trabajo. Otra flecha lleva de Comprobar a Parar o preguntar cuando se ha terminado, se está bloqueado o se ha agotado el presupuesto.</desc>
<defs><marker id="loop-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0L10 5 0 10Z" fill="#4b617e"/></marker></defs>
<rect width="760" height="520" rx="20" fill="#f0f5fb"/>
<g fill="none" stroke="#4b617e" stroke-width="4" marker-end="url(#loop-arrow)"><path d="M298 100H460"/><path d="M586 150V238"/><path d="M464 290H302"/><path d="M176 240V153"/><path d="M176 342V414"/></g>
<g stroke-width="3"><rect x="54" y="48" width="244" height="100" rx="23" fill="#d7eaff" stroke="#3377b9"/><rect x="464" y="48" width="244" height="100" rx="23" fill="#fce9b6" stroke="#9a701b"/><rect x="464" y="242" width="244" height="100" rx="23" fill="#dfd9ff" stroke="#7760b5"/><rect x="54" y="242" width="244" height="100" rx="23" fill="#cff3e4" stroke="#29836a"/><rect x="54" y="419" width="652" height="68" rx="20" fill="#fff" stroke="#4b617e"/></g>
<g font-family="system-ui,sans-serif" text-anchor="middle" fill="#173452"><g font-size="28" font-weight="700"><text x="176" y="90">1. MIRAR</text><text x="586" y="90">2. ELEGIR</text><text x="586" y="285">3. ACTUAR</text><text x="176" y="285" font-size="25">4. COMPROBAR</text></g><g font-size="20"><text x="176" y="122">¿Qué veo?</text><text x="586" y="122">¿Y ahora qué?</text><text x="586" y="317">Usar una herramienta.</text><text x="176" y="317">¿Qué ha cambiado?</text><text x="380" y="199">¿Queda algo? Otra vuelta.</text><text x="428" y="389">¿Terminado, bloqueado o en el límite?</text><text x="380" y="461" font-size="24" font-weight="700">PARAR, o preguntar a una persona.</text></g></g>
</svg>
<figcaption>Un diagrama didáctico, no un diseño de software obligatorio. Las implementaciones reales pueden combinar estas etapas. Lo importante es que el resultado alimente la siguiente decisión.</figcaption>
</figure>

## De vuelta a la seriísima misión del sándwich

El primer pasito de Pip es abrir el tarro de mermelada.

**Actuar:** Girar la tapa.

**Comprobar:** La tapa no se movió.

Aquí viene lo interesante. Pip no debería fingir que el tarro se abrió solo porque abrirlo era el plan.

Y Pip tampoco debería seguir girando para siempre hasta que el sol se convierta en una pasa.

Pip podría probar una alternativa permitida, o decir: «¿Me ayudas con esta tapa?». Pedir ayuda es un resultado útil, no un fracaso del tamaño de un robot.

Una vez abierto el tarro, Pip puede untar la mermelada, juntar el pan y comprobar el resultado frente a lo que le pediste.

¿Dos rebanadas? ¿Mermelada dentro? ¿En un plato? Genial.

¿Un tarro en equilibrio sobre una barra de pan? Creativo. Pero no es un sándwich.

## ¿Dónde encaja la parte de IA?

Nuestra historia de cocina es de mentira. Las herramientas de un agente de software, en lugar de manejar pan, podrían leer un archivo, buscar en una página, editar un documento o ejecutar una prueba.

En un agente de IA, un modelo de lenguaje puede ayudar a elegir el siguiente paso. El software que lo rodea ejecuta las llamadas a herramientas permitidas y devuelve sus resultados. Después, el modelo tiene otro turno con esa información.

Piensa en tres trabajos distintos:

| Parte | La cocina de mentira de Pip | Versión de software |
| --- | --- | --- |
| Objetivo | Hacer un sándwich de mermelada | Arreglar un enlace roto |
| Quien decide | Elegir el siguiente pasito | El modelo propone una acción |
| Herramienta | Manos y cuchara | Lector de archivos, editor o navegador |
| Observación | La tapa sigue cerrada | La herramienta devuelve un error o un resultado |
| Notas de trabajo | Tarro abierto; pan listo | Historial y resultados relevantes de la tarea |
| Comprobación final | El sándwich pedido está listo | Verificar que el enlace previsto funciona |

**Que un modelo sugiera una acción no es lo mismo que esa acción ocurra.** Y que una acción ocurra no significa automáticamente que se haya cumplido el objetivo.

«He guardado el archivo» y «he guardado el archivo correcto con el contenido correcto» son afirmaciones distintas. Es en la comprobación donde esa diferencia importa.

## Una pequeña aventura: la imagen perdida

Supón que le pides a un ayudante de software que arregle una imagen que falta en una página web.

Un bucle útil podría ser así:

1. **Mirar:** Leer la página e identificar la ruta de la imagen.
2. **Elegir:** Comprobar si la imagen referenciada existe.
3. **Actuar:** Revisar los archivos relevantes.
4. **Comprobar:** La página pide `cat.png`, pero el archivo se llama `cat.jpg`.
5. **Otra vuelta:** Actualizar la referencia y comprobar que la página carga la imagen correcta.
6. **Parar:** Informar del cambio y de las comprobaciones que realmente se hicieron.

Si la imagen sigue sin aparecer, «he editado la página» no basta. El resultado debe guiar el siguiente paso.

Fíjate en qué convierte esto en un bucle: **la siguiente acción depende de lo que reveló la anterior.** No se trata solo de hacer lo mismo una y otra vez.

## ¿Cada vuelta mejora las cosas?

No. Más actividad no significa automáticamente más progreso.

Aquí tienes un gráfico inventado de la misión del sándwich de Pip. Le damos a Pip un punto por cada hito completado: tarro abierto, mermelada untada, sándwich montado y petición final comprobada.

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 450" role="img" aria-labelledby="graph-title graph-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="graph-title">Un gráfico imaginario del progreso del sándwich</title>
<desc id="graph-desc">A lo largo de seis intentos, los hitos completados son cero, cero, uno, dos, tres y cuatro. Los dos primeros intentos no avanzan porque el tarro está atascado. Estos números inventados ilustran la retroalimentación, no un rendimiento medido de un agente.</desc>
<rect width="760" height="450" rx="20" fill="#f0f5fb"/>
<g font-family="system-ui,sans-serif" fill="#173452"><text x="48" y="42" font-size="23" font-weight="700">Avanzar no es lo mismo que estar ocupado.</text><text x="48" y="73" font-size="18">Hitos completados · ejemplo inventado, no un benchmark</text></g>
<g stroke="#c2cedd" stroke-width="1"><path d="M95 335H690M95 280H690M95 225H690M95 170H690M95 115H690"/></g>
<path d="M95 105V345H700" fill="none" stroke="#4b617e" stroke-width="3"/>
<polyline points="115,335 225,335 335,280 445,225 555,170 665,115" fill="none" stroke="#227657" stroke-width="5" stroke-linejoin="round"/>
<g fill="#227657" stroke="#fff" stroke-width="3"><circle cx="115" cy="335" r="8"/><circle cx="225" cy="335" r="8"/><circle cx="335" cy="280" r="8"/><circle cx="445" cy="225" r="8"/><circle cx="555" cy="170" r="8"/><circle cx="665" cy="115" r="8"/></g>
<g font-family="system-ui,sans-serif" font-size="20" fill="#173452" text-anchor="middle"><text x="68" y="341">0</text><text x="68" y="286">1</text><text x="68" y="231">2</text><text x="68" y="176">3</text><text x="68" y="121">4</text><text x="115" y="375">1</text><text x="225" y="375">2</text><text x="335" y="375">3</text><text x="445" y="375">4</text><text x="555" y="375">5</text><text x="665" y="375">6</text><text x="390" y="418">Intentos</text></g>
<g font-family="system-ui,sans-serif" font-size="19" fill="#173452"><text x="116" y="292">¡Tapa atascada!</text><text x="326" y="317">La ayuda funcionó.</text><text x="586" y="99">¡Comprobado!</text></g>
</svg>
<figcaption>Datos imaginarios: 0, 0, 1, 2, 3, 4 hitos completados. El trabajo real puede estancarse, retroceder o resultar imposible con las herramientas disponibles.</figcaption>
</figure>

El tramo plano importa. Si nada cambia, el ayudante tiene que darse cuenta, no celebrar cuántas veces lo ha intentado.

Para los mayores, eso sugiere preguntas útiles: ¿Hemos aprendido algo? ¿Ha cambiado el estado? ¿Estamos repitiendo la misma acción fallida? ¿Merece la pena otro intento para lo que cuesta?

Para todos los demás: **si la puerta dice TIRAR, empujar más fuerte no es una estrategia.**

## Dale al ayudante una valla, no el planeta entero

Un diseño de agente sensato necesita algo más que un botón de repetir.

- **Una meta clara.** «Encuentra tres fotos de pingüinos» es más fácil de comprobar que «haz que todo sea increíble».
- **Permisos adecuados.** Poder redactar un correo no debería significar automáticamente poder enviarlo.
- **Un presupuesto para parar.** Pon límites a los intentos, al tiempo o al gasto. Una tarea atascada no debe convertirse en una tarea infinita.
- **Una forma de preguntar.** La falta de información, la falta de acceso o una decisión con consecuencias pueden requerir a una persona.
- **Comprobaciones honestas.** Usa pruebas adecuadas al objetivo. No conviertas «la herramienta respondió» en «todo está bien».

Son principios de diseño, no la promesa de que todos los productos los implementen. Un bucle no hace que un sistema sea seguro o fiable por arte de magia.

En la cocina de Pip: haz el sándwich, no encargues un camión lleno de mermelada y pregunta antes de usar los electrodomésticos de mayores.

## ¿Un bucle de agente es lo mismo que un script?

No necesariamente, pero la frontera no es «los scripts son tontos y los agentes son listos». Los scripts también pueden tener bucles, condiciones y comprobaciones excelentes.

La diferencia que conviene vigilar es **cómo se elige la siguiente acción**. En un flujo de trabajo fijo, el desarrollador ha trazado las rutas de antemano. En un bucle de agente guiado por un modelo, el modelo puede elegir entre las acciones disponibles según la tarea y las últimas observaciones. Los sistemas reales pueden mezclar ambos enfoques.

Para un trabajo predecible, un pequeño script puede ser justo lo que hace falta. No necesitas un robot filósofo para tocar una campana a mediodía.

Para una tarea con obstáculos desconocidos, elegir el siguiente paso a partir de pruebas recientes puede ser útil. Esa flexibilidad también hace que los límites y la verificación sean importantes.

## La versión para el imán de la nevera

Un bucle de agente es:

> Prueba un paso útil. Mira qué ha pasado. Usa lo que has aprendido. Repite solo mientras tenga sentido.

No es magia. No es una garantía. No es «seguir para siempre».

Es una forma de conectar **un objetivo, una acción y el resultado real**, una y otra vez, hasta que el ayudante termina o necesita parar.

Pip lo explicaría de forma más sencilla:

**«Mira. Prueba. Comprueba. Y no digas sándwich hasta que haya un sándwich».**
