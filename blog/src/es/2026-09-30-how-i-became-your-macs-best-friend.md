---
title: Cómo empezó Agent!: tres días de marzo
description: Tres años de piezas sueltas, un bucle que faltaba y 177 commits en menos de dos días. El origen real de Agent!, sacado directamente de git.
tags: Orígenes, Historia
---
<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 380" role="img" aria-labelledby="lego-title lego-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="lego-title">Un robot simpático construye un Mac con bloques de juguete</title>
<desc id="lego-desc">Un robot azul sonriente sostiene un bloque amarillo sobre una pantalla de Mac a medio construir, hecha de bloques de juguete rojos, amarillos, verdes, azules y naranjas. Un bocadillo dice: ¡Casi listo!</desc>
<rect width="760" height="380" rx="20" fill="#eef6ff"/>
<path d="M40 318H720" stroke="#8b684c" stroke-width="13" stroke-linecap="round"/>
<path d="M190 92l-6 26 40-26" fill="#fff"/>
<rect x="120" y="30" width="230" height="64" rx="22" fill="#fff" stroke="#b6c8e4" stroke-width="3"/>
<text x="235" y="72" text-anchor="middle" font-family="system-ui,sans-serif" font-size="26" font-weight="700" fill="#173452">¡Casi listo!</text>
<path d="M140 270V310M210 270V310" stroke="#173452" stroke-width="7" stroke-linecap="round"/>
<path d="M250 200L318 146" stroke="#173452" stroke-width="7" stroke-linecap="round"/>
<rect x="100" y="150" width="150" height="120" rx="28" fill="#559ef5" stroke="#173452" stroke-width="4"/>
<path d="M175 150V124" stroke="#173452" stroke-width="5"/><circle cx="175" cy="115" r="10" fill="#efb943"/>
<circle cx="145" cy="192" r="13" fill="#fff"/><circle cx="205" cy="192" r="13" fill="#fff"/>
<circle cx="149" cy="193" r="5.5" fill="#173452"/><circle cx="209" cy="193" r="5.5" fill="#173452"/>
<path d="M148 228Q175 250 202 228" fill="none" stroke="#173452" stroke-width="6" stroke-linecap="round"/>
<g stroke="#173452" stroke-width="3">
<rect x="300" y="112" width="70" height="34" rx="4" fill="#efb943"/>
<rect x="311" y="102" width="16" height="10" rx="2" fill="#efb943"/><rect x="343" y="102" width="16" height="10" rx="2" fill="#efb943"/>
</g>
<g stroke="#173452" stroke-width="3">
<rect x="430" y="276" width="140" height="34" rx="4" fill="#9aa7b8"/>
<rect x="480" y="244" width="40" height="32" fill="#b8c3d1"/>
<rect x="400" y="210" width="70" height="34" rx="4" fill="#d94877"/>
<rect x="470" y="210" width="70" height="34" rx="4" fill="#4caf6e"/>
<rect x="540" y="210" width="70" height="34" rx="4" fill="#559ef5"/>
<rect x="610" y="210" width="70" height="34" rx="4" fill="#f08a3c"/>
<rect x="400" y="176" width="70" height="34" rx="4" fill="#efb943"/>
<rect x="470" y="176" width="70" height="34" rx="4" fill="#559ef5"/>
<rect x="540" y="176" width="70" height="34" rx="4" fill="#d94877"/>
<rect x="610" y="176" width="70" height="34" rx="4" fill="#4caf6e"/>
<rect x="400" y="142" width="70" height="34" rx="4" fill="#4caf6e"/>
<rect x="470" y="142" width="70" height="34" rx="4" fill="#f08a3c"/>
<rect x="540" y="142" width="70" height="34" rx="4" fill="#efb943"/>
<rect x="400" y="108" width="70" height="34" rx="4" fill="#559ef5"/>
<rect x="470" y="108" width="70" height="34" rx="4" fill="#d94877"/>
<rect x="540" y="108" width="70" height="34" rx="4" fill="#4caf6e"/>
<rect x="610" y="108" width="70" height="34" rx="4" fill="#efb943"/>
</g>
<rect x="610" y="142" width="70" height="34" rx="4" fill="none" stroke="#173452" stroke-width="3" stroke-dasharray="8 6"/>
<text x="190" y="354" text-anchor="middle" font-family="system-ui,sans-serif" font-size="21" fill="#173452">El constructor.</text>
<text x="540" y="354" text-anchor="middle" font-family="system-ui,sans-serif" font-size="21" fill="#173452">El Mac. Falta un bloque.</text>
</svg>
<figcaption>Todo lo grande empieza como un montón de ladrillos pequeños. El truco es saber cuál va después.</figcaption>
</figure>

Toda app tiene un primer día. El de Agent! fue un miércoles: **el 11 de marzo de 2026, a las 3:07 de la tarde.** Sabemos hasta el minuto porque git lo dejó anotado.

Pero los ladrillos llevaban mucho tiempo por ahí tirados.

## Tres años de piezas sueltas

Antes de Agent! hubo otras apps. **ANIE.** **Game Changer.** **BattleScript.** El **XCF MCP Server y Client.** **D1F**, una herramienta para cambiar muchas líneas de un archivo de una sola vez. Y unos ocho paquetes de Swift, todos escritos por la misma persona.

Cada una sabía hacer un trocito del trabajo. Unas podían hablar con una IA. Otras podían editar código. Otras podían toquetear Xcode. Ninguna sabía hacer lo más importante: **seguir adelante por su cuenta.**

Piensa en un juguete de cuerda. Le das cuerda, da tres pasos y se para. Muy mono. Poco útil. Lo que faltaba era un bucle: mirar el problema, elegir una herramienta, usarla, comprobar qué pasó y volver a empezar hasta terminar el trabajo. (Ese bucle tiene [su propia entrada, con un robot y un sándwich](/blog/what-is-an-agent-loop/).)

En cuanto el bucle funcionó, lo mejor de las piezas viejas pudo encajar encima. Esa es toda la historia en una frase. Lo demás son detalles, y los detalles son divertidos.

## Día uno: un cerebro, un ayudante y un botón de Cancelar

El primer commit de verdad se llama *"Autonomous Agent with privileged launch daemon."* Eran 20 archivos y 1.765 líneas de Swift. Esto venía en la caja:

- Una ventana de SwiftUI donde escribes lo que quieres.
- Un cerebro de IA, Claude, encargado de pensar.
- Un **Launch Daemon**: un pequeño ayudante que trabaja en segundo plano con las llaves de toda la casa, para que el agente pueda hacer tareas de sistema de mayores.
- Historial de tareas, capturas de pantalla y pegar.

Una hora después llegó el primer arreglo de un cuelgue (pegar una captura de pantalla lo hacía cascar). Minutos más tarde, un gran botón rojo de **Cancelar**, asignado a la tecla Escape. Cuando construyes algo que actúa por su cuenta, el botón de parar llega pronto.

A las 5:27 de la tarde ya había un segundo ayudante, un **Launch Agent**, que ejecuta comandos como *tú* y no como el todopoderoso root. Pedir la llave maestra para listar una carpeta es como llamar a los bomberos para encender una vela. Seis minutos después, Agent! recibió su segundo cerebro: **Ollama**, para poder usar modelos de IA que viven en tu propio Mac.

Antes de acabar el día también sabía escribir y ejecutar scripts de Swift, manejar Xcode, ver imágenes con modelos de visión y mostrar una pantalla de bienvenida. Además recibió unos puntitos de estado tipo semáforo, que necesitaron más o menos una docena de commits para decidirse por verde, amarillo y rojo. Hay cosas más difíciles que un bucle de agente.

## Día dos: "¿Puedo?"

El 12 de marzo es el día en que Agent! aprendió que un Mac es educado, y muy estricto con eso.

Para controlar otra app, como Música o Pages, macOS te pregunta primero: *"Agent! quiere controlar Música. ¿Permitir?"* Conseguir que esa ventanita apareciera de verdad llevó toda la tarde. Más o menos entre las 8:20 y las 9:40 de la noche, el historial es un montón de intentos separados por pocos minutos: probar de una manera, probar en el hilo principal, abrir Ajustes del Sistema, probar `osascript`, probar pidiendo `every window`, probar solo con `name`. Y además: Keynote, Numbers y Pages habían cambiado sus bundle IDs, así que estaba llamando a las puertas con el nombre equivocado.

Lo logró. Esa misma noche aprendió a mostrar imágenes y páginas web dentro de su propio registro, así que cuando crea la portada de un álbum, ves la portada del álbum.

## Día tres: un nombre y un número de versión

La mañana del 13 de marzo, la app recibió su nombre. El commit de las 9:06 es *"rename app to Agent!"* Con signo de exclamación incluido, a propósito.

Veinte minutos después llegó un cambio que sigue importando hoy: los scripts dejaron de ser programas separados y pasaron a ser **bibliotecas dinámicas** que se cargan dentro de la propia app. Por eso los AgentScripts tienen los mismos permisos del Mac que Agent!, sin volver a pedirlos.

Ese mismo día se etiquetó la versión **1.0.0**. Contando desde el primer commit, son **177 commits en menos de dos días.** Las versiones 1.0.1 a 1.0.16 llegaron en los ocho días siguientes.

Un pequeño detalle: el nombre del autor en esos primeros commits no es el de una persona. Es **"Agent! for MacOS."**

## Hacerse mayor

Tras ese primer sprint, la historia se acelera:

- **6 de abril.** Casi un mes de historial se comprimió en un único commit inicial limpio. El historial completo se guardó en una copia de seguridad.
- **7 de abril.** El "modo programación", el "modo automatización" y el "modo estándar" se [eliminaron por completo](/blog/why-we-ripped-out-modes/). Un solo agente, todas las herramientas, siempre.
- **Abril.** Apple Intelligence ya estaba a bordo como un cerebro que funciona en el propio Mac, gratis.
- **31 de agosto.** El proyecto se mudó de la organización de GitHub `macOS26` a **AgentiLoop**, y la web pasó a ser **agentiloop.ai**.
- **Últimamente.** Agent! aprendió a [funcionar en macOS 14.6 y en Macs Intel](/blog/sonoma-intel-and-the-mac-that-was-not-dead-yet/), y ayudó a construir a sus propios hermanos de terminal: [AgentiLoopCLI](https://github.com/AgentiLoop/AgentiLoopCLI) en Rust y [AgentiLoopGo](https://github.com/AgentiLoop/AgentiLoopGo) en Go.

Empezó con un solo cerebro. Hoy trabaja con **23 proveedores de IA**, además de Apple Intelligence. Desde aquella limpieza de abril, la rama principal ha sumado más de 1.300 commits.

## Por qué es como es

Casi todo lo raro de Agent! viene de esos tres primeros días.

Tiene dos ayudantes, uno para ti y otro para root, porque el día uno necesitó los dos. Es 100 % Swift, como las piezas sueltas de las que salió. Está hecho con código original, no con un montón de 65 paquetes de NPM. Maneja otras apps por su nombre mediante Accesibilidad y AppleScript porque el día dos se pasó aprendiendo a pedirle las cosas al Mac con educación. Y todavía tiene un gran botón de Cancelar.

Todo lo grande empieza como un montón de ladrillos pequeños. Este llevaba tres años amontonándose. El 11 de marzo, por fin, alguien encontró el ladrillo que sujeta a todos los demás: el bucle.
