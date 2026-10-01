---
title: Toda la familia se publica: Agent! 1.1.87 y AgentiLoop CLI 0.0.5
description: Agent! para Mac estrena Auto-Pilot, seis proveedores nuevos, un crítico más estricto y compatibilidad con macOS 14.6. Las CLI en Rust y Go amplían su caja de herramientas: búsqueda, descarga web, tareas, AGENTS.md, /undo, comandos personalizados y --json.
tags: Anuncio, Versión, Multiplataforma
---
<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 380" role="img" aria-labelledby="fam-title fam-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="fam-title">La familia AgentiLoop: una app para Mac y dos terminales</title>
<desc id="fam-desc">Una gran ventana de Mac con la etiqueta Agent! 1.1.87 ocupa el centro. A su izquierda, una ventana de terminal muestra un pequeño cangrejo y la etiqueta Rust 0.0.5; a su derecha, una ventana de terminal muestra una pequeña tuza y la etiqueta Go 0.0.5. Unas líneas punteadas unen las tres a un símbolo de bucle compartido en la parte superior.</desc>
<rect width="760" height="380" rx="20" fill="#0f1724"/>
<g fill="#6fb6ff" opacity=".35"><circle cx="60" cy="50" r="2"/><circle cx="700" cy="70" r="2"/><circle cx="640" cy="330" r="2"/><circle cx="110" cy="320" r="2"/><circle cx="380" cy="350" r="2"/><circle cx="520" cy="40" r="2"/><circle cx="230" cy="36" r="2"/></g>
<g fill="none" stroke="#6fb6ff" stroke-width="3" stroke-dasharray="4 8" stroke-linecap="round"><path d="M380 80V112"/><path d="M350 62Q170 70 140 150"/><path d="M410 62Q590 70 620 150"/></g>
<g fill="none" stroke="#9fd2ff" stroke-width="5" stroke-linecap="round"><path d="M380 55C392 39 412 39 412 55C412 71 392 71 380 55C368 39 348 39 348 55C348 71 368 71 380 55Z"/></g>
<rect x="250" y="112" width="260" height="190" rx="16" fill="#1d2a3d" stroke="#6fb6ff" stroke-width="3"/>
<rect x="250" y="112" width="260" height="34" rx="16" fill="#26364d"/><rect x="250" y="130" width="260" height="16" fill="#26364d"/>
<circle cx="272" cy="129" r="6" fill="#ff5f57"/><circle cx="292" cy="129" r="6" fill="#febc2e"/><circle cx="312" cy="129" r="6" fill="#28c840"/>
<rect x="340" y="164" width="80" height="80" rx="20" fill="#2f7bf5"/>
<g fill="#fff"><circle cx="358" cy="186" r="5"/><circle cx="402" cy="186" r="5"/><circle cx="380" cy="204" r="5"/><circle cx="360" cy="226" r="5"/><circle cx="400" cy="226" r="5"/></g>
<g fill="none" stroke="#fff" stroke-width="2" opacity=".8"><path d="M358 186L380 204L402 186M380 204L360 226M380 204L400 226M360 226H400M358 186H402M358 186L360 226M402 186L400 226"/></g>
<text x="380" y="280" text-anchor="middle" font-family="system-ui,sans-serif" font-size="22" font-weight="700" fill="#e8f2ff">Agent! 1.1.87</text>
<rect x="40" y="150" width="190" height="150" rx="12" fill="#121c2a" stroke="#f08a4b" stroke-width="3"/>
<text x="56" y="178" font-family="ui-monospace,monospace" font-size="15" fill="#f08a4b">$ agentiloop</text>
<g fill="#f08a4b" stroke="#0f1724" stroke-width="2"><ellipse cx="135" cy="236" rx="34" ry="22"/><circle cx="92" cy="214" r="10"/><circle cx="178" cy="214" r="10"/></g>
<g stroke="#f08a4b" stroke-width="4" stroke-linecap="round"><path d="M110 256l-10 14M122 258l-6 14M148 258l6 14M160 256l10 14M100 222l8 6M170 222l-8 6"/></g>
<circle cx="124" cy="230" r="4" fill="#0f1724"/><circle cx="146" cy="230" r="4" fill="#0f1724"/>
<text x="135" y="292" text-anchor="middle" font-family="system-ui,sans-serif" font-size="17" font-weight="700" fill="#ffd2b5">Rust 0.0.5</text>
<rect x="530" y="150" width="190" height="150" rx="12" fill="#121c2a" stroke="#4fd1e8" stroke-width="3"/>
<text x="546" y="178" font-family="ui-monospace,monospace" font-size="15" fill="#4fd1e8">$ agentiloop</text>
<g stroke="#0f1724" stroke-width="2"><ellipse cx="625" cy="236" rx="30" ry="36" fill="#4fd1e8"/><circle cx="600" cy="204" r="7" fill="#4fd1e8"/><circle cx="650" cy="204" r="7" fill="#4fd1e8"/></g>
<circle cx="612" cy="222" r="9" fill="#fff"/><circle cx="638" cy="222" r="9" fill="#fff"/><circle cx="612" cy="222" r="4" fill="#0f1724"/><circle cx="638" cy="222" r="4" fill="#0f1724"/>
<text x="625" y="292" text-anchor="middle" font-family="system-ui,sans-serif" font-size="17" font-weight="700" fill="#c8f4fb">Go 0.0.5</text>
<text x="380" y="345" text-anchor="middle" font-family="system-ui,sans-serif" font-size="18" fill="#9fb6d4">Un bucle. Tres formas de ejecutarlo.</text>
</svg>
<figcaption>La familia AgentiLoop el 1 de octubre: Agent! para Mac, más las ediciones de línea de comandos en Rust y Go.</figcaption>
</figure>

Hoy se publica toda la familia a la vez. **Agent! 1.1.87** es la nueva versión de la app para Mac, y **AgentiLoop CLI 0.0.5** ya está disponible tanto en [Rust](https://github.com/AgentiLoop/AgentiLoopCLI/releases/tag/v0.0.5) como en [Go](https://github.com/AgentiLoop/AgentiLoopGo/releases/tag/v0.0.5). Es una versión completa, no una preliminar, y es el mayor paso hasta ahora para las tres.

Esto es lo nuevo, directamente del historial de git.

## Agent! 1.1.87 para Mac

La última versión completa de la app para Mac fue la 1.1.33, el 12 de septiembre. Desde entonces han pasado muchas cosas: 449 commits entraron en la 1.1.87. Estos son los puntos destacados.

### 🤖 Auto-Pilot: `/auto <goal>`

La función estrella. Dale un objetivo a Agent! y `/auto` lo ejecuta como una serie de ciclos desatendidos dentro de un presupuesto de tiempo. Cada ciclo avanza hacia el objetivo, comprueba en qué punto está y sigue adelante.

- Sin límite de ciclos ni de iteraciones. Funciona en las pestañas de LLM y guarda un historial de objetivos, así que `/auto last` y `/auto #N` recuperan un objetivo anterior.
- Las sesiones sobreviven a los reinicios de la app y se reanudan en la misma pestaña.
- **Esc** detiene solo el ciclo actual. **Stop All** (o `/auto stop all`) termina la sesión.

Es el bucle del agente con la persona dando un paso atrás a propósito: tú fijas el destino y el presupuesto, y Agent! conduce.

### 🔌 Seis proveedores nuevos y menos ajustes que toquetear

Novedades en la 1.1.87: **Fluxion AI** (con opciones de protocolo OpenAI y Anthropic), **Muse Code** (reutiliza tu suscripción de `muse login`), **Requesty**, **A2Agent**, **OrcaRouter** y **Qwen Code** con el Coding Plan. También hay un proveedor experimental, **fm serve**, que expone Apple Foundation Models a través de una API local de Chat Completions.

La compatibilidad con visión ahora se detecta a partir de los metadatos del catálogo de cada proveedor, así que el interruptor Force Vision ya no hace falta. Por dentro, todos los proveedores viven ahora en un único registro, `APIProvider`, en lugar de en una docena de rutas de código separadas.

### 🧐 Un crítico al que no se puede convencer

Agent! tiene una puerta crítica: un segundo modelo revisa el cambio antes de dar la tarea por terminada. En la 1.1.87 la revisión es **obligatoria**. Un diff sin cambios se rechaza, un diff modificado se vuelve a revisar, y los problemas no pueden despacharse como "fuera de alcance". El crítico ahora también funciona con Codex y Apple Intelligence, y el registro muestra qué problemas encontró y si el código cambió después.

Junto a él está **Jev**, la capa de decisión TypeSafe System One que asesora al bucle de herramientas. Sus ajustes viven en los nuevos Ajustes comunes de LLM.

### 🧠 Un contexto más inteligente

La compactación recibió un repaso cuidadoso. Los umbrales ahora se calculan a partir del modelo *realmente en uso* (el modelo de la pestaña o el de respaldo), y se recuerdan las ventanas de contexto obtenidas de Ollama. Eso corrige un error por el que algunos modelos se compactaban a 16K. La cola conservada y la microcompactación se limitan por tokens en lugar de por número de mensajes, los bloques demasiado grandes se recortan primero, y los errores de desbordamiento de contexto y de `max_tokens` se detectan igual en todos los proveedores.

### 🖥️ Más Macs, más idiomas

- **macOS 14.6 Sonoma y posteriores**, en Apple Silicon e Intel. Las funciones de Apple Intelligence (Foundation Models) requieren macOS 26.
- La app está traducida al español, francés, alemán, chino (simplificado), ruso, coreano y japonés.
- Nuevas acciones de accesibilidad: `wait_until_actionable`, `select_text_range` y `observe_start/poll/stop/list`.
- Instalación con Homebrew: `brew update && brew install --cask agentiloop-agent`.

### 🔒 Más seguro por defecto

Ahora se bloquea el borrado recursivo de la carpeta del proyecto actual. Una caza de errores en toda la app corrigió una forma de saltarse el modo de solo lectura de ShellSafety con `&`, un bloqueo en el streaming de Ollama y varios cierres inesperados. `task_complete` se rechaza cuando el resumen apunta a una salida que nunca se escribió, y los modelos locales que se quedan sin memoria se detienen de inmediato con un motivo claro en lugar de quedarse dando vueltas.

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 330" role="img" aria-labelledby="box-title box-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="box-title">Una caja de herramientas más grande para la CLI</title>
<desc id="box-desc">Una caja de herramientas roja abierta con la etiqueta 0.0.5. De ella salen herramientas con etiquetas: glob y grep con una lupa, web_fetch con un globo terráqueo, todo_write con una lista de tareas, /undo con una flecha curva, AGENTS.md con un documento y --json con llaves.</desc>
<rect width="760" height="330" rx="20" fill="#fff6ea"/>
<path d="M60 296H700" stroke="#c9a77f" stroke-width="10" stroke-linecap="round"/>
<path d="M240 178L270 140H490L520 178Z" fill="#b8323a" stroke="#5a1418" stroke-width="4" stroke-linejoin="round"/>
<rect x="240" y="178" width="280" height="112" rx="10" fill="#d9444d" stroke="#5a1418" stroke-width="4"/>
<path d="M340 140V120Q340 108 352 108H408Q420 108 420 120V140" fill="none" stroke="#5a1418" stroke-width="8"/>
<rect x="340" y="214" width="80" height="40" rx="8" fill="#fff" stroke="#5a1418" stroke-width="3"/>
<text x="380" y="241" text-anchor="middle" font-family="ui-monospace,monospace" font-size="20" font-weight="700" fill="#5a1418">0.0.5</text>
<g font-family="ui-monospace,monospace" font-size="17" font-weight="700" text-anchor="middle">
<g><rect x="60" y="40" width="150" height="44" rx="12" fill="#d7eaff" stroke="#3377b9" stroke-width="3"/><text x="135" y="68" fill="#173452">glob · grep</text><circle cx="232" cy="102" r="16" fill="none" stroke="#3377b9" stroke-width="5"/><path d="M244 114l14 14" stroke="#3377b9" stroke-width="6" stroke-linecap="round"/></g>
<g><rect x="60" y="120" width="140" height="44" rx="12" fill="#d9f5e4" stroke="#2f8f5b" stroke-width="3"/><text x="130" y="148" fill="#14432a">web_fetch</text><circle cx="222" cy="186" r="16" fill="#bfe9cf" stroke="#2f8f5b" stroke-width="3"/><path d="M206 186H238M222 170Q212 186 222 202Q232 186 222 170" fill="none" stroke="#2f8f5b" stroke-width="2.5"/></g>
<g><rect x="295" y="20" width="170" height="44" rx="12" fill="#fce9b6" stroke="#9a701b" stroke-width="3"/><text x="380" y="48" fill="#4a3608">todo_write</text><path d="M362 76l6 6 10-12M362 94l6 6 10-12" fill="none" stroke="#9a701b" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><path d="M386 78H404M386 96H404" stroke="#9a701b" stroke-width="4" stroke-linecap="round"/></g>
<g><rect x="560" y="40" width="140" height="44" rx="12" fill="#efe1ff" stroke="#7a4bb8" stroke-width="3"/><text x="630" y="68" fill="#341a5a">/undo</text><path d="M548 128Q520 128 520 104Q520 84 546 84" fill="none" stroke="#7a4bb8" stroke-width="5" stroke-linecap="round"/><path d="M538 74l12 10-12 10" fill="none" stroke="#7a4bb8" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></g>
<g><rect x="560" y="120" width="140" height="44" rx="12" fill="#ffe0e6" stroke="#b83a5a" stroke-width="3"/><text x="630" y="148" fill="#5a1426">AGENTS.md</text><path d="M528 172h20l8 8v26h-28z" fill="#fff" stroke="#b83a5a" stroke-width="3" stroke-linejoin="round"/></g>
<g><rect x="560" y="210" width="140" height="44" rx="12" fill="#e2e8f0" stroke="#4b617e" stroke-width="3"/><text x="630" y="238" fill="#173452">--json { }</text></g>
</g>
</svg>
<figcaption>AgentiLoop CLI 0.0.5: el mismo bucle, mucho más en la caja.</figcaption>
</figure>

## AgentiLoop CLI 0.0.5: una caja de herramientas más grande

Cuando [llevamos el bucle del agente a la terminal](/blog/the-terminal-strikes-back/), la CLI empezó con cinco herramientas afiladas: leer, listar, escribir, editar y bash. La versión 0.0.4 le enseñó a detenerse limpiamente. La versión 0.0.5 consiste en darle más con qué trabajar. Todo llegó primero a Rust y se replicó commit a commit en Go, así que ambas ediciones tienen exactamente las mismas funciones.

### Herramientas nuevas

| Herramienta | Qué hace | ¿Pregunta antes? |
|---|---|---|
| `glob` | Busca archivos por patrón | No |
| `grep` | Busca en el contenido de los archivos, con 0–5 líneas de contexto | No |
| `web_fetch` | Descarga una página http(s) como texto, con límites de tamaño | **Sí** |
| `todo_write` | Mantiene una lista de tareas para trabajos de varios pasos (consúltala con `/todos`) | No |

`glob` y `grep` omiten `.git`, `node_modules`, `target` y los archivos binarios, y respetan `.gitignore`, incluidos los archivos anidados, la negación, el anclaje y las reglas solo para directorios. Eso los hace más rápidos que recurrir a `find` en el shell y más seguros que volcar un árbol entero en el contexto.

### Lee las instrucciones de tu proyecto

Si tu repositorio tiene un **`AGENTS.md`** o un **`CLAUDE.md`**, la CLI lo carga en el prompt del sistema, junto con uno en `~/.agentiloop` para tus preferencias personales. Líneas como `@docs/style.md` importan otros archivos (anidados y a salvo de ciclos). ¿Todavía no tienes ninguno? **`/init`** escribe un `AGENTS.md` inicial con los comandos de compilación y de tests que detecta.

### Deshacer, diff y compañía

- **`/undo`**: cada cambio hecho por `write_file`, `edit_file` y `apply_patch` se registra por prompt, así que puedes revertir el último turno del agente.
- **`/diff`** muestra el estado de git y el diff del árbol de trabajo.
- **`/export`** guarda la conversación como Markdown.
- **`/usage`** muestra el total de tokens desde el inicio y lo lleno que está el contexto.

### Hazla tuya

- **Comandos de barra personalizados**: coloca un archivo Markdown en `.agentiloop/commands/`, por ejemplo `review.md` con `Review $1 for bugs`, y `/review main.rs` lo ejecuta. Se admiten `$ARGUMENTS` y `$1`..`$9`, y `/commands` los lista.
- Los **prompts MCP** de tus servidores aparecen como comandos `/mcp__<server>__<prompt>`.

### Pensada para scripts y CI

- **`--json`** imprime una respuesta de ejecución única como un solo objeto JSON: result, is_error, session_id, provider, model y usage.
- **`--allow-tool` / `--deny-tool`** definen reglas de permisos por nombre de herramienta o por prefijo `mcp_*`. Deny siempre gana, incluso frente a `--yes`.
- **`--append-system-prompt`** añade texto al prompt del sistema para una sola ejecución.
- **Las tuberías simplemente funcionan**: un `-` suelto en el prompt se sustituye por stdin, así que `git diff | agentiloop "review this" -` hace lo que dice.

Todo junto, eso es un paso de CI que revisa un pull request, se niega a tocar el shell y devuelve una salida legible por máquinas:

```
git diff origin/main | agentiloop --deny-tool bash --json "review this diff" -
```

## ¿Por qué publicarlos juntos?

Porque son la misma idea con tres formas. Agent! para Mac es el producto estrella: controla tus apps, tus compilaciones de Xcode y todo tu escritorio. Las CLI llevan el mismo bucle a cualquier terminal en macOS, Windows y Linux. El Esc para cancelar de la CLI y el Auto-Pilot de la app para Mac con su botón Stop All responden a la misma pregunta desde dos lados: *¿cómo sigue una persona al mando de un bucle que se ejecuta solo?*

Esa es la parte que más nos importa. No un avatar simpático, ni una cifra más alta en un benchmark, sino la persona en el bucle: tú fijas el objetivo, ves cada paso, puedes detenerlo. En la CLI, `/undo` además revierte las últimas ediciones de archivos del agente. Auto-Pilot no se puede deshacer, así que úsalo en un proyecto que esté en git.

## Consíguelos

- **Agent! 1.1.87 para Mac**: [descárgalo desde GitHub](https://github.com/AgentiLoop/Agent/releases/tag/v1.1.87.287) o `brew update && brew install --cask agentiloop-agent`. macOS 14.6 o posterior, Apple Silicon o Intel.
- **AgentiLoop CLI 0.0.5 (Rust)**: [versión en GitHub](https://github.com/AgentiLoop/AgentiLoopCLI/releases/tag/v0.0.5).
- **AgentiLoopGo 0.0.5 (Go)**: [versión en GitHub](https://github.com/AgentiLoop/AgentiLoopGo/releases/tag/v0.0.5).

Los binarios de la CLI para macOS están firmados y notarizados. Descomprime, pon `agentiloop` en tu PATH y ejecútalo; el asistente de configuración se encarga del resto.

Los testers son muy bienvenidos. Prueba `/undo` después de una edición grande, apúntala a un repositorio con un `AGENTS.md` o integra `--json` en un script, y luego cuéntanos qué se rompió. Incluye tu sistema operativo, proveedor y modelo, y nunca incluyas claves de API.
