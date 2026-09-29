---
title: La terminal contraataca: el bucle del agente se vuelve multiplataforma en Rust y Go
description: Agent! es una app para Mac, pero un agente de programación debe estar allí donde trabajan los desarrolladores. Así es como el bucle del agente se convirtió en dos CLI, una en Rust y otra en Go, con una TUI a pantalla completa en macOS, Windows y Linux.
tags: Anuncio, Multiplataforma, Ingeniería
---
Durante la mayor parte de su vida, Agent! ha sido una orgullosa app para Mac: Swift y SwiftUI nativos, integración profunda con AppleScript y Accesibilidad, y un Launch Daemon para root. Sigue siendo el producto estrella. Pero en los últimos días algo ha cambiado en nuestra forma de pensar sobre los agentes de programación, y hoy ve la luz.

**El bucle del agente ahora se ejecuta en tu terminal, en macOS, Windows y Linux.** Llega en dos ediciones con las mismas capacidades: [AgentiLoopCLI](https://github.com/AgentiLoop/AgentiLoopCLI) en Rust y [AgentiLoopGo](https://github.com/AgentiLoop/AgentiLoopGo) en Go. Y sí, Agent! para Mac escribió buena parte de sus propios hermanos pequeños.

## El cambio de paradigma: de vuelta a la terminal

La primera ola de herramientas de programación con IA vivía dentro de editores y ventanas de chat. La ola que está ganando vive en la **terminal**. Hay buenas razones para ello:

- **La terminal ya es donde ocurre el trabajo.** Compilaciones, tests, git, gestores de paquetes y sesiones SSH viven ahí. Un agente en la terminal no necesita una integración para cada uno; tiene `bash`.
- **Va a cualquier parte.** Una CLI se ejecuta en un servidor de compilación Linux, dentro de un contenedor, por SSH en una Raspberry Pi o en una VM de desarrollo con Windows. Una app para Mac se ejecuta en un Mac.
- **Se puede combinar.** El modo de ejecución única (`agentiloop "explain this project"`) encaja directamente en scripts y en CI.
- **Es transparente sobre lo que hace.** Cada llamada a herramienta, cada diff y cada solicitud de permiso pasan por pantalla en texto plano.

Los superpoderes de la app para Mac, como controlar Photo Booth mediante Accesibilidad o automatizar Mail con ScriptingBridge, son realmente exclusivos de Mac. El **bucle del agente** no lo es. Razonar, llamar a una herramienta, leer el resultado real, corregir y repetir: eso funciona en cualquier sistema operativo con un shell y un sistema de archivos. Así que extrajimos el bucle.

## ¿Por qué dos lenguajes?

Podríamos haber elegido uno. En cambio, portamos el mismo diseño dos veces, a propósito.

**Rust (AgentiLoopCLI)** fue el primero. El workspace se creó el 20 de septiembre con un bucle central, el proveedor de Anthropic, herramientas integradas y la CLI. Está dividido en cinco crates: `agentiloop-core` (el bucle, los mensajes, las sesiones y los permisos), `agentiloop-provider`, `agentiloop-tools`, `agentiloop-mcp` y `agentiloop-cli`. Se ejecuta sobre `tokio`, usa `reqwest` con `rustls` para no tener que lidiar con OpenSSL en Windows, y dibuja su TUI con `ratatui`. El Markdown pasa por `pulldown-cmark`, y el código obtiene resaltado de sintaxis de `syntect`.

**Go (AgentiLoopGo)** llegó el 23 de septiembre en una ráfaga de commits: el núcleo (mensajes, bucle del agente, compactación, sesiones y permisos) con tests, luego los proveedores, luego el cliente MCP y después la CLI con su REPL, TUI, Markdown, resaltado de sintaxis, sesiones y comandos de barra. Dibuja la TUI con `tcell`, renderiza Markdown con `goldmark`, resalta con `chroma` y gestiona la edición de líneas con `liner`. Su flujo de publicación apunta a las mismas cinco plataformas que la edición en Rust.

Hacerlo dos veces es la mejor revisión de diseño que existe. Cualquier cosa que en realidad fuera un rustismo o un goísmo salta a la vista de inmediato, y lo que queda es la arquitectura de verdad. También hay una ventaja práctica: elige la toolchain en la que tu equipo ya confía. Y luego cuéntanos cuál lo hace mejor. 🦀 vs 🐹

## El mismo bucle, menos superficie

Ambas CLI empiezan deliberadamente con un conjunto de herramientas pequeño y afilado:

| Herramienta | Qué hace | ¿Pregunta antes? |
|---|---|---|
| `read_file` | Lee un archivo con números de línea | No |
| `list_dir` | Lista una carpeta | No |
| `write_file` | Crea o sobrescribe un archivo | **Sí** |
| `edit_file` | Reemplaza un fragmento exacto de texto | **Sí** |
| `bash` | Ejecuta un comando (`sh -c` en Mac y Linux, `cmd /C` en Windows) | **Sí** |

¿Quieres más? Ambas ediciones incluyen un cliente MCP portado del propio AgentMCP de Agent!, compatible con stdio, Streamable HTTP y el antiguo HTTP+SSE, así que las herramientas de cualquier servidor MCP se conectan directamente.

Los permisos forman parte del núcleo, no son un añadido de la interfaz. En Rust, un trait `PermissionPolicy` decide si cada llamada puede ejecutarse, según el nombre de la herramienta, si modifica algo y su entrada. La respuesta es `Allow`, `Deny` o `Cancel`. Esa tercera opción existe por una molestia real: pulsar **Esc** ante una solicitud de permiso debería omitir *esa llamada concreta*, no terminar toda la tarea. La CLI proporciona una política interactiva, y los tests y la CI usan `AllowAll`.

## Lo multiplataforma está en los detalles

"Funciona en Windows" es fácil de decir y difícil de cumplir. Algunas de las cosas que hizo falta:

- **Matar de verdad un comando desbocado.** Cuando `bash` agota el tiempo, matar el shell no basta si el shell lanzó procesos hijos. La edición en Go mata todo el árbol de procesos: un grupo de procesos en Unix y `taskkill /T` en Windows. El código está dividido en `proc_unix.go` y `proc_windows.go`.
- **CI en los tres sistemas operativos.** El repositorio de Go ejecuta CI en macOS, Linux y Windows, y el flujo de publicación de Rust compila cinco binarios: macOS arm64 y x86_64, Linux x86_64 y arm64, y Windows x86_64.
- **Binarios de Mac firmados.** El flujo de publicación puede firmar y notarizar las compilaciones de macOS, para que Gatekeeper no las bloquee.
- **Sin arqueología de archivos de configuración.** La CLI recuerda cómo la lanzaste: proveedor, modelo, modo TUI y sesión. Tras la primera ejecución, un simple `agentiloop` retoma exactamente donde lo dejaste.

## Una TUI que se siente como una app

Hay tres formas de ejecutarla: la **TUI** a pantalla completa (`agentiloop --tui`), un modo de **chat** línea a línea para terminales sencillas y el modo de **ejecución única** para scripts. La TUI ha tenido unos días muy movidos:

- un indicador de actividad animado en el cuadro de entrada, con un spinner, la actividad actual y el tiempo transcurrido
- seguimiento de tokens por segundo
- enlaces clicables
- historial de prompts que persiste entre ejecuciones
- sesiones reanudadas que muestran la conversación anterior, para que no te quedes mirando una pantalla en blanco
- `/model` respaldado por la lista de modelos en vivo del proveedor

Y cuando falta una clave de API o es incorrecta, lo dice con palabras claras y nombra al proveedor real, en lugar de soltar un 401.

## Proveedores

Desde el primer día funciona con Claude (clave de API o token OAuth de Claude Code en la misma credencial, con el esquema de autenticación detectado automáticamente), OpenAI y cualquier servidor compatible con OpenAI, modelos locales mediante Ollama o LM Studio, y **oMLX** en Apple Silicon. Lee automáticamente la dirección y la clave de oMLX desde `~/.omlx/settings.json`.

## Prueba la versión

Hoy lanzamos la **v0.0.4**, una versión estable. Es temprana y avanza rápido, y queremos tu opinión ahora, mientras cambiar cosas sale barato. Descarga un binario desde las [releases de Rust](https://github.com/AgentiLoop/AgentiLoopCLI/releases), o compila la edición en Go desde el [código fuente](https://github.com/AgentiLoop/AgentiLoopGo).

La app para Mac no se va a ninguna parte. Si usas un Mac, Agent! sigue haciendo cosas que ninguna terminal puede hacer. Pero si alguna vez has querido el mismo agente en el servidor Linux, el portátil con Windows y la Raspberry Pi, ya está aquí.
