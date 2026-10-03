---
title: De vuelta en Hacker News, seis meses después, con Auto-Pilot
description: Agent! vuelve a estar en Hacker News como Show HN. El hilo de abril trataba de un arnés de programación nativo para Mac; este trata de Auto-Pilot, el bucle guiado por un objetivo que sigue ejecutando ciclos hasta alcanzarlo, y del juego al estilo Mario Kart que ha estado construyendo. Aquí está la publicación, qué hay detrás de cada afirmación y dónde unirse a la discusión.
tags: Auto-Pilot, Comunidad, Hacker News
---
Agent! vuelve hoy a Hacker News como Show HN: [Show HN: AgentiLoop Agent Mac GUI Agent Loop for macOS 14.6 or Later](https://news.ycombinator.com/item?id=49948810). Si tienes cuenta en Hacker News, ese hilo es el lugar para hacer preguntas, buscarle fallos y contarnos qué querrías de un agente para Mac. Esta publicación es la versión larga del texto de la propuesta, con un enlace a la fuente de cada afirmación que contiene.

## El material de origen

La propuesta es corta, así que aquí está completa, citada de [el ítem de Hacker News](https://news.ycombinator.com/item?id=49948810):

> Agent! apareció originalmente en Hacker News el pasado abril. Mucho ha cambiado desde entonces. Recientemente se ha desarrollado una nueva función llamada Auto-Pilot. Se le da un objetivo y no se detiene hasta alcanzarlo. Piénsalo como tareas con esteroides. Lo que hace Agent es crear múltiples tareas. Cada tarea se denomina Ciclo. Por defecto, los Auto-Pilot lanzados con auto [objetivo] no tienen límite de tiempo. A Agent! se le indica que siga ejecutándose hasta alcanzar su objetivo. Auto-Pilot tiene un interruptor de emergencia, un botón "Stop All". El usuario también puede matar solo el Ciclo actual con auto stop y puede matar todo con auto stop all. En noviembre un usuario podrá tener múltiples Auto-Pilots ejecutándose en el mismo proyecto. Y una pestaña de Auto-Pilot podrá generar automáticamente otras pestañas. Actualmente estamos desarrollando un clon al estilo Mario Kart llamado "GoKart", escrito en GoDot 4. Hasta ahora se han registrado más de 20 horas desarrollando y mejorando el juego. *(traducido del inglés)*

Todo lo que sigue amplía una frase de ese texto.

## "Agent! apareció originalmente en Hacker News el pasado abril"

El primer hilo fue [Agent — Native macOS coding IDE/harness](https://news.ycombinator.com/item?id=47787127), el 16 de abril de 2026: 83 puntos y 54 comentarios. La app entonces requería macOS 26.4 y Apple silicon, tenía 17 proveedores de LLM y se presentaba sobre todo como un arnés de programación que además podía manejar apps de Mac mediante la API de Accesibilidad. Ambos hilos aparecen en la sección [Reviews](/#reviews) de este sitio, junto con los artículos independientes que llegaron entre medias.

Desde abril: soporte para macOS 14.6 e Intel ([la historia de ese port](/blog/sonoma-intel-and-the-mac-that-was-not-dead-yet/)), 23 proveedores, [compactación de contexto de la que puedes recuperarte](/blog/context-compaction-half-the-window/), una [CLI en Rust y Go](/blog/agent-1-1-87-and-agentiloop-cli-0-0-5/) para Mac, Windows y Linux, una versión el primer día de cada mes, y la función de la que realmente trata la nueva propuesta.

## "Se le da un objetivo y no se detiene hasta alcanzarlo"

Auto-Pilot es el comando `/auto` de Agent! para Mac. De la sección Auto-pilot del README: ejecuta el bucle de tareas en ciclos desatendidos, en la pestaña principal o en cualquier pestaña de LLM, hasta que se alcanza un objetivo, se agota un presupuesto de tiempo o pulsas Stop. No hay límite de ciclos ni tope de iteraciones por ciclo. Cuando la tarea de un ciclo termina y el objetivo no se ha alcanzado, el siguiente ciclo arranca automáticamente.

| Comando | Qué hace |
|---|---|
| `/auto <goal>` | Trabajar hacia el objetivo hasta que el LLM informe de que se ha alcanzado |
| `/auto 4h <goal>` | Lo mismo, pero deteniéndose tras 4 horas (`30m`, `1.5h` también funcionan) |
| `/auto` | Revisar primero el proyecto y luego pedirte el objetivo |
| `/auto history`, `/auto last`, `/auto #N` | Listar objetivos anteriores, reiniciar el más reciente o el N-ésimo |
| `/auto status` / `/auto stop` | Mostrar la sesión, o terminarla después del ciclo actual |

"Piénsalo como tareas con esteroides" es el modelo mental correcto. Cada ciclo *es* una tarea normal de Agent!, con las mismas herramientas, las mismas salvaguardas (leer antes de editar, evidencia de goal_state, lista de bloqueo del shell) y el mismo contrato de `done()`. Lo que Auto-Pilot añade es el bucle alrededor: el resumen del ciclo se añade a `.agent/autopilot/progress.md` dentro del proyecto y se inyecta en el prompt del siguiente ciclo, de modo que cada ciclo empieza leyendo qué hicieron, asumieron y dejaron pendiente los anteriores. La sesión solo termina cuando el LLM comienza su resumen final con `AUTOPILOT: GOAL REACHED`. Los ciclos que terminan sin ningún resumen, por errores o cancelaciones, nunca terminan la sesión; el siguiente ciclo simplemente espera más, 15 segundos, luego 30, luego 60, hasta cinco minutos.

"Por defecto … no tienen límite de tiempo" es literal: `/auto <goal>` sin duración se ejecuta hasta alcanzar el objetivo o hasta que lo detengas. Si quieres un techo, `/auto 4h <goal>` te lo da. Las sesiones activas también sobreviven a los reinicios de la app. Salir, o un fallo, las pausa, y en el siguiente arranque cada una se reanuda en su pestaña con el ciclo siguiente.

## "Auto-Pilot tiene un interruptor de emergencia"

Tres formas de parar, y hacen cosas distintas:

- **Stop All** (el botón, "Detener todo") termina todas las sesiones de Auto-Pilot en todas las pestañas y detiene todas las tareas en ejecución. En `RunStop.swift` el comentario es explícito: una parada de una sola tarea, Esc o el botón de stop, mantiene Auto-Pilot en marcha; Stop All lo termina.
- **`/auto stop`** termina la sesión cuando acaba el ciclo actual, o inmediatamente si estás entre ciclos. Al ciclo actual se le permite aterrizar.
- **`/auto stop all`** (también `stopall` o `stop-all`) es lo mismo que pulsar Stop All, para quienes prefieren no alargar la mano hasta el ratón. Se gestiona en `AutoPilot.swift` justo antes de `/auto stop`.

La propuesta describe `auto stop` como matar "solo el Ciclo actual". La versión más precisa es que termina la *sesión* después del ciclo actual; el ciclo en sí corre hasta su final natural, que es lo que mantiene limpios el registro de progreso y el historial de git.

## "En noviembre … múltiples Auto-Pilots ejecutándose en el mismo proyecto"

Esta es la parte de la propuesta que es un punto de la hoja de ruta y no una función ya publicada, y conviene dejar claro cuál es cuál. A día de hoy, la rama principal del repositorio de Agent tiene un commit titulado *Auto-Pilot: multiple tabs per project — per-tab progress, shared registry, auto/forced git worktree isolation, shared memory from worktrees*. Esa es la base: cada pestaña mantiene su propio registro de progreso, las pestañas se registran entre sí, y cuando dos Auto-Pilots editarían de otro modo los mismos archivos, reciben worktrees de git separados. Todavía no está en ninguna versión publicada; llegó después de la etiqueta 1.1.87. Las versiones salen el primer día del mes, así que la del 1 de noviembre es la primera en la que puede llegarte, y la parte de la "pestaña que genera otras pestañas" está, según la propuesta, prevista para la misma ventana.

## "Un clon al estilo Mario Kart llamado GoKart"

GoKart es el proyecto en el que Auto-Pilot ha pasado la mayor parte de su vida. La [publicación anterior](/blog/gokart-built-on-auto-pilot/) cubre en detalle la primera tarde, directamente desde el registro de progreso: Godot 4 instalado en el ciclo 1, físicas arcade personalizadas elegidas en lugar de `VehicleBody3D` para poder probar el manejo con tests unitarios, chispas de derrape y desenfoque de turbo en el ciclo 2, una pista en el ciclo 3, objetos en el ciclo 4, un atasco por un carácter de tabulación perdido, un Stop All, y una segunda sesión que puso un límite de tiempo `perl -e 'alarm'` a cada ejecución de shell y luego entregó quince funciones seguidas.

No se ha detenido. El [repositorio de GoKart](https://github.com/AgentiLoop/GoKart) pasó de su primer commit a las 12:39 del 1 de octubre a 71 commits la tarde del 3 de octubre. Los commits recientes se leen como una lista de tareas de Mario Kart 64: tráfico al estilo Toad's Turnpike en Sunset Speedway, Monty Moles al estilo Moo Moo Farm en Green Hills, una pantalla de título con demo de atracción en vivo, un tablero de resultados y una ventana de objetos dibujada en el HUD. Cada uno llega con su propio archivo de tests y un script `tools/*_check.gd`, porque el modelo sigue sin poder ver la pantalla y tiene que demostrar de otra manera que una función está ahí. Las "más de 20 horas" de la propuesta son el total de tiempo real de esas sesiones. [GoKart 0.0.1](https://github.com/AgentiLoop/GoKart/releases/tag/v0.0.1) se puede descargar para macOS, Windows y Linux si prefieres jugarlo a leer sobre él.

## Qué preguntar en el hilo

Si vienes de Hacker News, las preguntas que más nos gustaría responder allí:

- Cómo decide Auto-Pilot que un objetivo se ha alcanzado, y por qué dejamos que lo diga el modelo en lugar de una métrica fija.
- Qué pasa cuando un ciclo sale mal, y por qué git es el verdadero deshacer.
- Si un bucle desatendido en tu Mac es siquiera una buena idea, y qué hacen las salvaguardas al respecto.

El hilo está en [news.ycombinator.com/item?id=49948810](https://news.ycombinator.com/item?id=49948810). Agent! 1.1.87 con Auto-Pilot está en la [página de versiones](https://github.com/AgentiLoop/Agent/releases/latest) y en Homebrew: `brew install --cask agentiloop-agent`.
