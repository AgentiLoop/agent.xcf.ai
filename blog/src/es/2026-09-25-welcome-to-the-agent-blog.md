---
title: Bienvenido al blog de Agent!: una app, cualquier IA, control total de tu Mac
description: Qué es AgentiLoop Agent!, por qué lo construí como lo construí y qué vas a encontrar aquí, contado directamente desde el código fuente.
tags: Anuncio, Arquitectura
---
<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 340" role="img" aria-labelledby="map-title map-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="map-title">Un pequeño Mac te entrega el mapa</title>
<desc id="map-desc">Un Mac sonriente, de pie sobre un escritorio, sostiene un mapa desplegado. El mapa tiene cuatro paradas unidas por un sendero punteado: Cualquier IA, El bucle, AgentScript y Seguridad.</desc>
<rect width="760" height="340" rx="20" fill="#eef6ff"/>
<path d="M30 290H730" stroke="#8b684c" stroke-width="10" stroke-linecap="round"/>
<rect x="132" y="228" width="16" height="52" fill="#8a97a8"/><rect x="100" y="276" width="80" height="12" rx="4" fill="#8a97a8"/>
<rect x="40" y="100" width="200" height="130" rx="14" fill="#c9d3df" stroke="#173452" stroke-width="4"/>
<rect x="54" y="114" width="172" height="102" rx="6" fill="#559ef5"/>
<circle cx="110" cy="152" r="9" fill="#fff"/><circle cx="170" cy="152" r="9" fill="#fff"/>
<circle cx="112" cy="153" r="4" fill="#173452"/><circle cx="172" cy="153" r="4" fill="#173452"/>
<path d="M115 180Q140 198 165 180" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
<path d="M228 180Q262 176 290 160" fill="none" stroke="#173452" stroke-width="6" stroke-linecap="round"/>
<path d="M290 50L400 70L510 50L620 70V260L510 240L400 260L290 240Z" fill="#fff8e6" stroke="#8b684c" stroke-width="4" stroke-linejoin="round"/>
<path d="M400 70V260M510 50V240" stroke="#e6d6b3" stroke-width="3"/>
<path d="M350 175C380 140 410 140 440 140S490 190 520 190 560 130 580 110" fill="none" stroke="#d94877" stroke-width="4" stroke-dasharray="3 10" stroke-linecap="round"/>
<circle cx="350" cy="175" r="11" fill="#559ef5" stroke="#173452" stroke-width="3"/>
<circle cx="440" cy="140" r="11" fill="#7b6ad6" stroke="#173452" stroke-width="3"/>
<circle cx="520" cy="190" r="11" fill="#22c55e" stroke="#173452" stroke-width="3"/>
<circle cx="580" cy="110" r="11" fill="#f59e0b" stroke="#173452" stroke-width="3"/>
<g font-family="system-ui,sans-serif" text-anchor="middle" fill="#173452">
<text x="350" y="152" font-size="15" font-weight="700">Cualquier IA</text>
<text x="440" y="117" font-size="15" font-weight="700">El bucle</text>
<text x="520" y="222" font-size="15" font-weight="700">AgentScript</text>
<text x="580" y="90" font-size="15" font-weight="700">Seguridad</text>
<text x="345" y="88" font-size="14" fill="#8b684c">Tu mapa</text>
<text x="140" y="322" font-size="18">Agent! para Mac</text>
</g>
</svg>
<figcaption>Todo blog necesita una primera entrada. Esta es el mapa.</figcaption>
</figure>

Hola, soy Todd. Desarrollo **AgentiLoop Agent!**, un agente de IA nativo para macOS, y este es su blog.

Quería un sitio donde explicar las partes de Agent! que no caben en un README ni en unas notas de versión. Por qué una salvaguarda tiene la forma que tiene. Por qué el bucle del agente revisa su propio trabajo. Qué se rompió en una release candidate y cómo lo arreglamos. Casi todo lo que leas aquí sale directamente del código, porque es lo que mejor conozco. De vez en cuando también echaré un vistazo al mundo más amplio de los agentes de IA y a lo que significa para tu Mac.

Si acabas de llegar, empieza por aquí. Piensa en esta entrada como en el mapa.

## Qué es Agent!

Agent! es 100% Swift y SwiftUI nativo. Escribes (o dices) lo que quieres y se pone a hacer el trabajo en tu Mac, en vez de explicarte cómo hacerlo:

- **Escribe código de verdad.** Lee tu proyecto, edita archivos con diffs de reemplazo de cadenas, compila en Xcode, lee los errores, los corrige y hace commit con git.
- **Maneja cualquier app del Mac** a través de la API de Accesibilidad, además de AppleScript, JXA y 51 puentes de ScriptingBridge para apps.
- **Ejecuta comandos de shell como tú o como root**, mediante un Launch Agent y un Launch Daemon registrados con SMAppService y accesibles por XPC.
- **Funciona con 23 proveedores de LLM**, además de Apple Intelligence en el dispositivo: Claude, Codex, OpenAI, Gemini, Grok, Mistral, DeepSeek, Qwen, Z.ai, OpenRouter, Ollama, vLLM, LM Studio y más.
- **Te escucha.** Di *"Agent!"* seguido de una tarea, o escríbele desde tu iPhone por iMessage (solo remitentes aprobados).

El README lo resume en cuatro palabras: *Siri responde. Agent! actúa.*

## Sin NPM, sin Electron

Esta es la parte que sorprende a la gente. No hay envoltorio de Electron. No hay runtime de Node. No hay ninguna carpeta `node_modules` comiéndose tu disco en silencio. Escribí yo mismo cada paquete Swift del que depende Agent!, y cada uno vive en su propio repositorio dentro de la organización [AgentiLoop](https://github.com/AgentiLoop):

| Paquete | Función |
|---|---|
| AgentTools | Esquemas de herramientas, prompts de sistema y gestión de proveedores |
| AgentLLM | Protocolos, tipos y registro de proveedores de LLM |
| AgentMCP | Cliente MCP (stdio y HTTP) |
| AgentAccess | Automatización de Accesibilidad |
| AgentEventBridges | Protocolos de ScriptingBridge para más de 50 apps del Mac |
| AgentD1F | Motor de diffs multilínea |
| AgentSwift | Análisis de código con SwiftSyntax |
| AgentColorSyntax · AgentTerminalNeo | Resaltado de sintaxis · markdown de terminal retro |
| AgentAudit | Registro de auditoría con `os.log` |

El resultado es una app que apenas consume RAM y que aun así trae de serie automatización de Xcode, análisis de sintaxis Swift, Accesibilidad, AppleScript, automatización de Safari y MCP.

## El bucle en el centro

Todo en Agent! gira en torno a una idea: un **bucle de tareas que se verifica a sí mismo**. El modelo piensa, llama a una herramienta, mira el resultado real y se corrige. Eso solo funciona si puedes fiarte de él, así que hay unas cuantas reglas integradas:

- **Las herramientas no se pueden fingir.** Cada llamada pasa por un único despachador y devuelve una salida real. Si el modelo dice *"lo he pulsado"* sin haber llamado de verdad a ninguna herramienta, Agent! se lo señala y le envía una corrección.
- **"Terminado" exige pruebas.** Una tarea no puede darse por acabada hasta que sus criterios de `goal_state` estén marcados con evidencias, como una compilación en verde o un test que pasa.
- **Primero se lee, luego se edita.** Agent! se niega a editar un archivo que el modelo no ha leído, o que ha cambiado en disco desde que lo leyó (se comprueba con SHA-256). El rechazo le entrega al modelo el archivo actualizado, así que el siguiente intento usa las líneas correctas.
- **Todo se puede deshacer.** Cada edición se guarda como instantánea durante una semana. Puedes revertir un solo archivo o rebobinar una tarea entera con `rewind_task`.

En próximas entradas desmontaré cada una de estas reglas.

## AgentScript: Swift con permisos completos

AgentScript es una de mis piezas favoritas. Los scripts son archivos Swift normales y corrientes. Agent! compila cada uno en un `.dylib` con SwiftPM y lo carga dentro de su propio proceso con `dlopen`, así que tu script obtiene los mismos permisos de macOS que ya tiene Agent!: Accesibilidad, Automatización, Calendario, Contactos, Mail, Fotos y el resto. Solo necesitas un punto de entrada:

```swift
import Foundation
import CalendarBridge   // any `import XBridge` auto-wires, no Package.swift edits

@_cdecl("script_main")
public func scriptMain() -> Int32 {
    print("Hello from AgentScript! 👋")
    return 0
}
```

Todo lo que imprime el script vuelve al modelo, y el valor de retorno es el código de salida. La app incluye unos 35 ejemplos, entre ellos `TodayEvents`, `NowPlaying`, `CheckMail` y `CreateDmg`.

## Una seguridad que puedes leer

Agent! puede ejecutar comandos como root. Eso es pedir mucha confianza, así que la seguridad no puede ser solo una diapositiva en una presentación. Es código, y puedes leerlo en GitHub. Un `ShellSafetyService` programado de forma fija rechaza los comandos catastróficos antes de que lleguen a enviarse, y el daemon con privilegios repite la misma comprobación por su lado. También hay una segunda opinión opcional llamada **Jev** que valora la probabilidad de que un comando destruya datos. El [primer análisis a fondo](/blog/inside-agent-shell-guardrails/) explica exactamente cómo funciona.

## La familia sigue creciendo

El mismo bucle de agente ahora también funciona en la terminal, en macOS, Windows y Linux. Hay dos CLI con las mismas capacidades: [AgentiLoopCLI](https://github.com/AgentiLoop/AgentiLoopCLI) en Rust y [AgentiLoopGo](https://github.com/AgentiLoop/AgentiLoopGo) en Go. Mi dato curioso favorito del README: Agent! para Mac escribió a sus propios hermanitos.

## Qué encontrarás aquí

- **Funcionamiento interno:** el bucle del agente, la compactación de contexto, el despacho de herramientas, los subagentes, la memoria y los planes.
- **Seguridad:** salvaguardas, el modelo de confianza de XPC y lo que los incidentes recientes con agentes nos enseñan a todos los demás.
- **Notas de versión con el porqué:** qué cambió en cada build y el bug que lo hizo necesario.
- **Guías prácticas:** recetas de AgentScript, cómo elegir proveedor con poco presupuesto y cómo trabajar de forma totalmente local.
- **El mundo de los agentes en general:** noticias y análisis, siempre de vuelta a lo que significan para tu Mac.

Agent! funciona en macOS 14.6 o posterior, en Apple Silicon e Intel, y es gratuito para uso personal. Descárgalo aquí abajo, dale algo real que hacer y cuéntame qué tal te va.
