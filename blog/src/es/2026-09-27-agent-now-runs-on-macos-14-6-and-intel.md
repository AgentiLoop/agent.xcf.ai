---
title: Agent! ya funciona en macOS 14.6 y en Macs con Intel: cómo nos liberamos de macOS 26
description: Agent! se creó en torno a Apple Intelligence en macOS 26. Así es como un día de controles #available y actualizaciones de paquetes lo llevó a macOS 14.6 en Apple Silicon e Intel.
tags: Notas de la versión, Ingeniería
---
Hasta hoy, Agent! requería macOS 26. Desde la versión preliminar de hoy funciona en **macOS 14.6 o posterior, en Apple Silicon e Intel**. Eso incluye muchos Macs perfectamente válidos que se habían quedado fuera, muchos de los cuales no pueden ejecutar Apple Intelligence en absoluto.

Esto es lo que hizo falta, commit a commit, en un solo día.

## El obstáculo: FoundationModels

Agent! utiliza el modelo integrado en el dispositivo de Apple a través del framework **FoundationModels**, que solo existe en macOS 26. No es el cerebro principal, ya que de eso se encarga el proveedor que elijas. Pero cumple varias funciones: resúmenes rápidos durante la compactación del contexto, recuento de tokens en el dispositivo, una sesión precalentada al iniciar y algo de triaje.

El código que hace referencia a un tipo de macOS 26 no compila para un destino de implementación anterior. Así que el primer paso (`ea5ce624`) fue colocar **todos** los usos de FoundationModels detrás de `#available(macOS 26, *)`. Eso abarcó `FoundationModelService`, `AppleIntelligenceMediator`, el precalentamiento en `AgentApp`, los resúmenes de compactación y el recuento de tokens en `Compression.swift`, y `AboutSelf`.

## El truco: borrar el tipo de la propiedad almacenada

`#available` sirve para rutas de código, pero no para una propiedad almacenada. Una clase no puede contener un `LanguageModelSession?` cuando ese tipo no existe en el sistema operativo en ejecución. La solución es almacenarlo como `AnyObject?` y volver a convertirlo donde se usa, dentro de código protegido:

```swift
/// Type-erased `LanguageModelSession` so the stored property compiles below macOS 26.
private(set) var session: AnyObject?

@available(macOS 26.0, *)
var transcript: Transcript? {
    (session as? LanguageModelSession)?.transcript
}
```

Como dice el mensaje del commit, las propiedades almacenadas ya no «arrastran el tipo del framework a la disposición de la clase».

Las comprobaciones de disponibilidad también recibieron una respuesta honesta para los sistemas más antiguos:

```swift
static var unavailabilityReason: String {
    guard #available(macOS 26.0, *) else { return "Apple Intelligence requires macOS 26 or later." }
    ...
}
```

Así, en macOS 14 o 15, Apple Intelligence simplemente aparece como no disponible con un motivo claro, y todo lo demás funciona. En macOS 26 no cambia nada.

## La larga cola: diez paquetes

Agent! está construido a partir de sus propios paquetes Swift, y cada uno declaraba su propio sistema operativo mínimo. El commit `4d7fca86` actualizó los diez a versiones que declaran `.macOS(.v14)`:

| Paquete | Versión |
|---|---|
| AgentAccess | 2.10.24 |
| AgentAudit | 1.3.9 |
| AgentColorSyntax | 1.2.8 |
| AgentD1F | 1.0.15 |
| AgentEventBridges | 1.1.8 |
| AgentLLM | 1.0.8 |
| AgentMCP | 1.6.10 |
| AgentSwift | 1.1.11 |
| AgentTerminalNeo | 1.37.9 |
| AgentTools | 2.53.19 |

Ser dueños de todas las dependencias compensa en días como este. No hubo que esperar a ningún mantenedor externo, solo crear diez etiquetas.

## La sorpresa: 26.4

Una API necesitaba algo más que un control para 26.0. `SystemLanguageModel.tokenCount(for:)` solo existe a partir de **macOS 26.4**, así que su comprobación de disponibilidad pasó de 26.0 a 26.4. Sin eso, un Mac con 26.0 a 26.3 habría intentado llamar a un método que todavía no existe. Es un buen recordatorio de que «el framework está disponible» y «este método está disponible» no son la misma pregunta.

## Qué obtienes en Macs más antiguos

En macOS 14.6 y 15, en Apple Silicon o Intel, Agent! funciona de la misma manera:

- los 23 proveedores de LLM en la nube y locales
- el bucle de herramientas completo: programación, compilaciones de Xcode, git, shell como tu usuario o como root, Accesibilidad, AppleScript, JXA, AgentScript, automatización de Safari y MCP
- compactación del contexto, que utiliza los propios resúmenes del modelo y los recuentos de tokens del proveedor, solo que sin el nivel de Apple Intelligence

Solo las funciones de Apple Intelligence en el dispositivo requieren macOS 26.

## Consíguelo

Cada versión y versión preliminar incluye un binario firmado, notarizado y grapado. Nunca necesitas compilar desde el código fuente:

```sh
brew update && brew install --cask agentiloop-agent
```

O descarga el `.dmg` desde [GitHub Releases](https://github.com/AgentiLoop/Agent/releases). Si estabas esperando con un MacBook antiguo o un Mac mini con Intel, hoy es el día.
