---
title: Bienvenido al blog de Agent!: una app, cualquier IA, control total de tu Mac
description: Qué es AgentiLoop Agent!, cómo está construido y de qué hablará este blog diario, contado directamente desde el código fuente.
tags: Anuncio, Arquitectura
---
Este es el blog oficial de **AgentiLoop Agent!**, el agente de IA nativo para macOS. El plan es sencillo: una entrada al día, escrita sobre todo a partir de lo que mejor conocemos, el propio código. Encontrarás análisis a fondo de cómo funciona el bucle del agente, por qué cada salvaguarda tiene la forma que tiene, qué ha cambiado en la última release candidate y, de vez en cuando, una mirada al panorama general de los agentes de IA.

Si acabas de llegar, esta primera entrada es tu mapa.

## Qué es Agent!

Agent! es una app 100% nativa en Swift / SwiftUI. Escribes (o dices) lo que quieres y hace el trabajo en tu Mac en lugar de limitarse a describirlo:

- **Programa de verdad.** Lee tu proyecto, edita archivos con diffs de reemplazo de cadenas, compila en Xcode, lee los errores, los corrige y hace commit con git.
- **Controla cualquier app del Mac** mediante la API de Accesibilidad, además de AppleScript, JXA y 51 puentes de ScriptingBridge para apps.
- **Ejecuta comandos de shell como tú o como root**, a través de un Launch Agent y un Launch Daemon registrados con SMAppService y accesibles por XPC.
- **Habla con 23 proveedores de LLM** además de Apple Intelligence en el dispositivo: Claude, Codex, OpenAI, Gemini, Grok, Mistral, DeepSeek, Qwen, Z.ai, OpenRouter, Ollama, vLLM, LM Studio y más.
- **Escucha.** Di *"Agent!"* seguido de una tarea, o envíale un mensaje desde tu iPhone por iMessage (solo remitentes aprobados).

El README lo resume en una línea: *Siri responde. Agent! actúa.*

## Sin NPM, sin Electron

Lo que más sorprende a la gente es lo que Agent! *no* incluye. No hay envoltorio de Electron, ni runtime de Node, ni `node_modules`. Cada paquete Swift del que depende lo ha escrito el mismo autor, y cada uno vive en su propio repositorio dentro de la organización [AgentiLoop](https://github.com/AgentiLoop):

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

El resultado es una app que consume muy poca RAM y que, de serie, ofrece automatización de Xcode, análisis de sintaxis Swift, Accesibilidad, AppleScript, automatización de Safari y MCP.

## El bucle en el centro

Todo gira en torno a una idea: un **bucle de tareas que se verifica a sí mismo**. El modelo razona, llama a una herramienta, ve el resultado real y se corrige. Unas pocas reglas hacen que ese bucle sea fiable:

- **Las herramientas no se pueden simular.** Cada llamada pasa por un único despachador y devuelve una salida real. Si el modelo afirma *"lo he pulsado"* sin haber llamado a ninguna herramienta, Agent! inyecta una corrección.
- **"Terminado" exige pruebas.** Una tarea no puede darse por finalizada hasta que sus criterios de `goal_state` se marquen como cumplidos con evidencias, como una compilación en verde o un test superado.
- **Primero se lee, luego se edita.** Se rechazan las ediciones de un archivo que el modelo no ha leído, o que ha cambiado en disco desde que lo leyó (se comprueba con SHA-256). El propio rechazo lee el archivo para el modelo, de modo que el siguiente intento usa líneas actualizadas.
- **Todo es reversible.** Cada edición se guarda como instantánea durante una semana. Puedes revertir un solo archivo o rebobinar una tarea completa con `rewind_task`.

Desmontaremos cada una de estas reglas en próximas entradas.

## AgentScript: Swift con permisos completos

Una de las piezas más características es **AgentScript**. Los scripts son archivos Swift normales. Agent! compila cada uno en un `.dylib` con SwiftPM y lo carga en el propio proceso con `dlopen`, así que el script hereda los permisos de macOS de Agent!: Accesibilidad, Automatización, Calendario, Contactos, Mail, Fotos, etc. Para escribir uno basta con un único punto de entrada:

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

Agent! puede ejecutarse como root, así que la seguridad no es una diapositiva de una presentación. Es código que puedes abrir en GitHub. Un `ShellSafetyService` programado de forma fija rechaza los comandos catastróficos antes de despacharlos, y el daemon con privilegios vuelve a hacer la misma comprobación por su lado. Una segunda opinión opcional, llamada **Jev**, evalúa la probabilidad de que un comando destruya datos. Nuestro [primer análisis a fondo](/blog/inside-agent-shell-guardrails/) explica exactamente cómo funciona.

## La familia sigue creciendo

El mismo bucle de agente funciona ahora también en la terminal de macOS, Windows y Linux, en forma de dos CLI con las mismas capacidades: [AgentiLoopCLI](https://github.com/AgentiLoop/AgentiLoopCLI) en Rust y [AgentiLoopGo](https://github.com/AgentiLoop/AgentiLoopGo) en Go. Un dato curioso del README: Agent! para Mac escribió a sus propios hermanos pequeños.

## Qué encontrarás aquí

- **Funcionamiento interno:** el bucle del agente, la compactación de contexto, el despacho de herramientas, los subagentes, la memoria y los planes.
- **Seguridad:** salvaguardas, el modelo de confianza de XPC y lo que los incidentes recientes con agentes enseñan a quienes los construyen.
- **Notas de versión con el porqué:** qué cambió en cada build y el bug que lo motivó.
- **Guías prácticas:** recetas de AgentScript, cómo elegir proveedor con un presupuesto ajustado y cómo trabajar de forma totalmente local.
- **El mundo de los agentes en general:** noticias y análisis, siempre vinculados a lo que significan para tu Mac.

Agent! funciona en macOS 14.6 o posterior, tanto en Apple Silicon como en Intel, y es gratuito para uso personal. Descárgalo a continuación y vuelve mañana.
