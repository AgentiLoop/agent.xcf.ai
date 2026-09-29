---
title: Antes de que el modelo tenga voto: así funcionan las salvaguardas de shell de Agent!
description: Cómo ShellSafetyService, la segunda comprobación en el daemon y la segunda opinión de Jev impiden que un agente de IA borre tu Mac, recorriendo el código Swift real.
tags: Seguridad, Funcionamiento interno
---
Esta semana, TechRadar informó de que un agente de programación borró unos 48,000 archivos en muy poco tiempo y después pidió disculpas. La disculpa no cambió nada. Los archivos ya no estaban.

Agent! puede ejecutar comandos de shell como tú a través de un Launch Agent, y como **root** a través de un Launch Daemon. Eso es lo que lo hace útil, ya que puede grabar una tarjeta SD, arreglar permisos o limpiar una carpeta de compilación. Pero también significa que "seguramente el modelo tendrá cuidado" no es un modelo de seguridad. Por eso Agent! no le pide al modelo que tenga cuidado. Comprueba cada comando en el código, antes de que se ejecute nada, en tres capas.

## Capa 1: una salvaguarda fija que el modelo no puede sortear con palabras

`ShellSafetyService` es un simple `enum` de Swift en `Agent/Services/ShellSafetyService.swift`. El comentario de documentación del principio marca el tono: se ejecuta *antes de cada superficie de ejecución* y rechaza los comandos catastróficos *sin llegar a despacharlos*. A los prompts de sistema se les llama por lo que son: una red de seguridad adicional, no la capa que impone las reglas.

El punto de entrada recibe el comando, el contexto en el que se ejecutará y la carpeta del proyecto de la pestaña:

```swift
static func check(_ command: String,
                  context: Context = .userAgent,
                  projectFolder: String = "") -> Verdict
```

Un `Verdict` consta de `allowed`, un `reason` legible por humanos y un breve identificador `rule` para el registro de auditoría. El motivo está escrito para el modelo: se devuelve como resultado de la herramienta, de modo que el LLM entiende *por qué* se rechazó y no se limita a reintentarlo.

### Interpreta los comandos compuestos igual que una shell

Un filtro ingenuo solo mira el principio de la cadena. Ni los atacantes ni los modelos confundidos se lo ponen tan fácil. `check` divide el comando por `;`, `&&`, `||`, `|` y saltos de línea, y luego comprueba **cada segmento**. Así, `ls; rm -rf /` queda bloqueado aunque la primera mitad sea inofensiva.

Hay una excepción deliberada a ese orden. La clásica fork bomb, `:(){ :|:& };:`, *depende* de `;` y `|`, justo los caracteres que el divisor separa. Por eso la comprobación de fork bomb se ejecuta sobre el comando completo antes de dividirlo.

### Le quita los disfraces

Antes de buscar `rm`, una función auxiliar llamada `stripPrefixWrappers` elimina los envoltorios que no cambian lo que hace un comando: `sudo`, `exec`, `command`, `builtin`, `eval` y `doas`. También elimina las asignaciones de variables de entorno iniciales como `FOO=bar`. Eso significa que `sudo rm -rf ~` y `FOO=1 exec rm -rf ~` caen en la misma regla que el comando sin adornos.

Además, las opciones se analizan en lugar de compararse con patrones. `-rf`, `-fr`, `-Rf`, `-r -f` y `--recursive --force` cuentan todas, porque el analizador busca una `r` y una `f` en cualquier grupo de opciones cortas, además de las formas largas.

### Qué rechaza

Estos son los identificadores de regla que aparecen en el código fuente:

| Regla | Qué impide |
|---|---|
| `rm.catastrophic` | `rm -rf` sobre `/`, un comodín suelto como `*` o `./*`, o tu carpeta de inicio escrita de cualquier forma (`~`, `~/*`, `$HOME`, `${HOME}/*` o la ruta literal de inicio) |
| `rm.no-preserve-root` | `--no-preserve-root`, la forma explícita de saltarse la protección de `/` |
| `rm.project-folder` | Borrar recursivamente la carpeta del proyecto en la que trabaja el agente, o todo su contenido mediante comodines. Borrar una subcarpeta concreta sigue estando permitido. |
| `rm.dangerous-target` | Otros destinos peligrosos de `rm` en la ruta de nivel de usuario |
| `fork-bomb` | Bombas de procesos que se replican a sí mismas |
| `mv.to-devnull` | "Borrar" archivos moviéndolos a `/dev/null` |
| `find.delete-broad-root` | `find … -delete` desde una raíz demasiado amplia |
| `perms.recursive-on-root` | Cambios recursivos de permisos en rutas del nivel raíz |

La regla de la carpeta del proyecto merece un momento. Es la que se corresponde más directamente con el incidente anterior: un agente nunca debería borrar el mismo proyecto en el que se le pidió trabajar, se formule como se formule la petición.

### Root recibe un trato distinto, a propósito

Cabría esperar que el daemon de root tuviera las reglas *más estrictas*. Tiene las más acotadas. El comentario explica por qué: el daemon existe para hacer trabajo a nivel de sistema, como clonar discos o ejecutar `mkfs`, y "no debería ponernos trabas". Así que en el contexto `.rootDaemon`, `check` pasa directamente a `checkCatastrophicRm`, que solo bloquea los tres patrones irrecuperables (`/`, comodines sueltos y la carpeta de inicio), además de `--no-preserve-root` y el borrado de la carpeta del proyecto. Todo lo demás queda a criterio del operador.

Es una decisión de diseño que vale la pena copiar. Una salvaguarda que bloquea trabajo de administración legítimo acaba desactivada. Una salvaguarda que solo bloquea errores irrecuperables se queda activada.

## Capa 2: el daemon vuelve a comprobar

La app ejecuta `ShellSafetyService.check` antes de despachar nada. Los helpers no se fían de eso sin más. En `Shared/DaemonCore.swift`, justo después de escribir la entrada en el registro de auditoría, el daemon ejecuta **la misma comprobación** por su cuenta:

```swift
// Defense-in-depth: the app already runs this same check before
// dispatching, but any same-team-signed client can reach the mach
// service directly.
let verdict = ShellSafetyService.check(
    script,
    context: auditCategory == .launchDaemon ? .rootDaemon : .userAgent,
    projectFolder: workingDirectory
)
```

Un comando bloqueado se registra como denegado con su identificador de regla y recibe el código de salida 126. Nunca llega a `/bin/zsh`. Esto es importante porque los listeners de XPC aceptan cualquier cliente firmado por el mismo equipo. Si otro programa firmado por ese equipo se conecta directamente al servicio mach, también se topa con la salvaguarda.

## Capa 3: Jev, una segunda opinión para lo que se escapa a los patrones

Las reglas basadas en patrones son precisas, pero solo conocen los patrones que has escrito. Muchos comandos destructivos no se parecen a `rm -rf /`: un `truncate` sobre el archivo equivocado, un `DROP` de SQL canalizado a una CLI, un `dd` en la dirección equivocada.

Ese es el trabajo de **Jev**, una capa consultiva opcional en `JevAdvisor.swift`. Todo comando que ya ha *superado* `ShellSafetyService` pasa por Jev, que estima la probabilidad de que destruya datos de forma irreversible. Si supera tu umbral, Agent! lo rechaza con un mensaje claro:

```text
Refused: Jev rated this command 85% likely to irreversibly destroy data.
Command: …
Narrow the target or run it yourself if this is intentional.
```

Algunos detalles muestran con cuánto cuidado se definió su alcance:

- **Complementa, nunca sustituye.** El comentario del código es explícito: `ShellSafetyService` es la capa que impone las reglas, y Jev solo detecta lo que se les escapa a las reglas de patrones. Por eso el umbral es deliberadamente alto. Por defecto es del **70%**, y puedes ajustarlo de 0 a 100% en pasos del 10% en Ajustes.
- **Si falla, deja pasar, pero lo dice alto y claro.** Sin clave, con el interruptor desactivado o ante una caída de red, el resultado es "sin opinión", así que un servicio inestable nunca puede bloquear tu tarea. Aun así, el fallo queda registrado (`⚠️ Jev check failed, command allowed`), de modo que una clave caducada nunca se confunde con "Jev dice que es seguro".
- **Cancelar es cancelar.** Si detienes una tarea mientras Jev está evaluando, el comando no se ejecuta.
- **Cada veredicto es visible.** Cada comprobación registra el porcentaje de riesgo, si se permitió o se rechazó, el modelo que respondió y el recuento de tokens.

## Probado, no supuesto

`AgentTests/ShellSafetyServiceTests.swift` contiene 30 tests para la salvaguarda. Y como cada comando de los helpers se escribe en el registro de auditoría antes de ejecutarse, siempre puedes reconstruir lo que el agente intentó hacer, incluido lo que no se le permitió.

## La lección para quien construye agentes

1. **Impón las reglas en el código, no en el prompt.** Los prompts son sugerencias. Un `enum` de Swift no.
2. **Analiza como analiza la shell.** Divide los comandos compuestos, elimina los envoltorios y normaliza las opciones.
3. **Vuelve a comprobar en la frontera con privilegios.** No des por hecho que tu propio cliente será el único que llame.
4. **Bloquea lo irrecuperable, no lo inusual.** Las reglas acotadas sobreviven; las que generan ruido acaban desactivadas.
5. **Añade criterio por encima, y haz que sus fallos sean visibles.** Una segunda opinión solo es valiosa si puedes saber cuándo no ha respondido.

Todo esto es público en [GitHub](https://github.com/AgentiLoop/Agent). Léelo, búscale los fallos y abre una issue si encuentras un comando que debería haberse bloqueado.
