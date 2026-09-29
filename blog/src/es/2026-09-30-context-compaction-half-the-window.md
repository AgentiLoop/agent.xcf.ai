---
title: Por qué Agent! compacta a la mitad de la ventana, y los tres bugs que la redujeron a 16K
description: Cómo decide la compactación de contexto de Agent! cuándo resumir una tarea larga, y las correcciones del 28 de septiembre para modelos de respaldo, Ollama y una ventana de 272K en Codex.
tags: Funcionamiento interno, Notas de versión
---
Las tareas largas de un agente tienen un problema de física. Cada llamada a una herramienta añade su salida a la transcripción: la lectura de un archivo, un log de compilación, un diff. Tarde o temprano, la transcripción ya no cabe en la ventana de contexto del modelo y el proveedor rechaza la petición. Un agente que trabaja toda la noche tiene que **compactar**: reducir la conversación sin perder lo importante.

La compactación vive en `Agent/AgentViewModel/Messages/Compression.swift`. El 28 de septiembre recibió tres correcciones en una sola tarde, todas por el mismo síntoma: tareas que se compactaban a 16K tokens en modelos con ventanas mucho mayores. Así funciona el sistema y esto es lo que falló.

## Cuándo compactar: a la mitad de la ventana, con tope

El disparador es un struct llamado `CompactionState`. Su núcleo es una única función:

```swift
static func threshold(for contextWindow: Int, maxTokens: Int = 0) -> Int {
    let byFraction = Int(Double(min(contextWindow, compactionWindowCap)) * compactionFraction)
    let reservedOutput = maxTokens > 0 ? min(maxTokens, contextWindow / 2) : 8_192
    return max(2_000, min(byFraction, contextWindow - reservedOutput))
}
```

Con `compactionFraction = 0.5` y `compactionWindowCap = 256_000`, esto se traduce en:

- **Compactar al 50% de la ventana.** Es un porcentaje, no un número fijo de tokens. La otra mitad es el presupuesto de salida, así que entrada y salida siempre caben.
- **Nunca por encima de 128K.** Las ventanas anunciadas por encima de 256K (Claude 1M, MiniMax 1M, Gemini y Grok 2M) compactan todas a 128K. Una ventana de 200K compacta a 100K.
- **Dejar siempre espacio para la respuesta.** El umbral no puede ser tan tardío que la salida reservada deje de caber.
- **Nunca por debajo de 2K**, como mínimo para los modelos locales más pequeños.

¿Por qué limitar una ventana de 2M a 128K? El comentario es tajante. Con ventanas anunciadas enormes, un porcentaje sin tope retrasa tanto la compactación que cualquier discrepancia del lado del proveedor se convierte en un desbordamiento de contexto en toda regla en lugar de una compactación. Por ejemplo, un router que sirve una ventana más corta de la que declara, o un prompt de sistema mal contado. Compactar pronto cuesta un resumen. Compactar demasiado tarde cuesta la tarea.

## La medición: confiar en el proveedor y, si no, estimar

Para comparar con el umbral hace falta un recuento de tokens. Adivinarlo a partir de los caracteres es impreciso, así que `measuredTokens` prefiere el dato real: los `input_tokens` que el proveedor informó para la última petición. Esa cifra incluye el prompt de sistema y los esquemas de herramientas, que una estimación local no puede ver. Solo se estiman los mensajes añadidos *después* de ese informe.

Sin informe, recurre a la clásica estimación de caracteres ÷ 4, inflada un 25%, porque el código denso se acerca más a 3.3 caracteres por token. Antes de pagar una compactación basándose solo en una estimación, el bucle lo confirma con un contador en el dispositivo.

## Cómo compacta: por niveles

Cuando se supera el umbral, `tieredCompact` recorre una serie de pasos cada vez más agresivos:

1. **Nivel 0: un resumen estructurado** de la transcripción *completa*, hecho por el modelo activo. Va primero para que quien resume todavía vea la salida de las herramientas que está resumiendo.
2. **Microcompactación:** los resultados antiguos de herramientas se convierten en marcadores breves y recuperables. La herramienta `restore_tool_result` puede traer de vuelta cualquiera de ellos.
3. **Eliminación de imágenes:** las capturas de pantalla ocupan muchísimo y no se resumen bien.
4. **Nivel 1: resumen con Apple Intelligence,** rápido y en el dispositivo.
5. **Nivel 2: poda agresiva,** que condensa los mensajes intermedios en un resumen.

Un comentario resume la filosofía: la compactación estructural "es un mecanismo de seguridad, no una función". Se ejecuta incluso si desactivas Token Compression. Solo el nivel de Apple Intelligence respeta ese interruptor.

Tras la compactación, el modelo recupera lo que más echaría de menos: los criterios de objetivo abiertos, la lista de comprobación del plan activo y el contenido actual de hasta cinco archivos que editó durante la tarea (unos 10K tokens en total). También se reinicia la caché de deduplicación de lecturas, así que se vuelve a permitir releer un archivo.

Por último, hay un **cortocircuito**. Tras tres compactaciones seguidas que no logran reducir la transcripción, el bucle deja de intentarlo. Pero no se rinde para siempre: en cuanto la transcripción crece otro 25% por encima del último intento fallido, vuelve a probar.

## Los bugs: tres caminos hacia 16K

Todas las correcciones del 28 de septiembre desembocaban en el mismo número. Una ventana de respaldo de 32K da `min(16K, 32K − 8K) = 16K`. Para un modelo de más de 200K, compactar a 16K significa resumir casi sin parar y olvidar archivos que el modelo acaba de leer.

### 1. El modelo de respaldo tomaba prestada la ventana equivocada

Agent! admite una cadena de respaldo. Si un proveedor devuelve un 429, agota el tiempo de espera o se cae de la red, la tarea continúa con el siguiente proveedor configurado. Las pestañas también pueden sobrescribir el modelo. Pero `contextWindow(for:)` buscaba la ventana del modelo *seleccionado globalmente* para el proveedor, no la del que se estaba ejecutando realmente. Para un modelo de respaldo sin entrada propia, caía al tamaño estático de 32K.

La corrección añade el modelo a la búsqueda:

```swift
func contextWindow(for provider: APIProvider, model: String? = nil) -> Int
```

Ahora todos los puntos de llamada pasan el modelo en uso: el bucle principal, las tareas de pestaña, la ruta de respaldo y los subagentes.

### 2. Ollama olvidaba lo que había aprendido

Los servidores locales informan de su ventana real por modelo de forma asíncrona: Ollama mediante `/api/show`, LM Studio mediante `/api/v0/models` y vLLM mediante `/v1/models`. Por eso el bucle llama a `refreshThreshold` en cada iteración después de la primera. Una consulta que llega cuando la tarea ya ha empezado sigue surtiendo efecto.

En Ollama, sin embargo, las ventanas obtenidas no se guardaban, así que la compactación seguía volviendo a los 16K por defecto. La corrección guarda las ventanas de contexto obtenidas y las consulta al inicio de la tarea cuando la ventana es desconocida. Llegó acompañada de una nueva batería de tests, `OllamaContextWindowTests.swift`.

### 3. Un presupuesto de salida generoso se comía el de entrada

Este es sutil. Codex declara una ventana de 272K para su modelo GPT-6 Astra. Un usuario configura **Max Output Tokens** en 256K. El código anterior reservaba el presupuesto de salida completo:

```text
272K − 256K = 16K   →   threshold = min(128K, 16K) = 16K
```

El código nuevo reserva como máximo la mitad de la ventana para la salida:

```swift
let reservedOutput = maxTokens > 0 ? min(maxTokens, contextWindow / 2) : 8_192
```

El mismo caso da ahora `min(128K, 272K − 136K) = 128K`. El tope porcentual sigue usando la ventana limitada, pero la comprobación de que la salida cabe usa la ventana *real*. De lo contrario, el presupuesto de salida por defecto de 500K de Claude en una ventana de 1M volvería negativo `window − maxTokens` y dejaría el umbral en el mínimo de 2K.

## Por qué te importa

Si ejecutas tareas largas, sobre todo sesiones de programación nocturnas, con proveedores de respaldo o modelos locales, ahora deberían conservar mucho más contexto de trabajo. Eso significa menos bucles de "tengo que volver a leer ese archivo", menos detalles perdidos y menos tokens gastados en resúmenes. Estas correcciones se publicaron el 28 de septiembre junto con la versión 1.1.77 (build 277), release candidate 6, además de la detección entre proveedores de los errores de desbordamiento de contexto y de `max_tokens`.

La lección para quienes construyen agentes es general: **dimensiona la memoria según el modelo que realmente se está ejecutando**, confía más en los recuentos de tokens del proveedor que en tus propias estimaciones y pon tope a cada presupuesto para que ningún ajuste pueda dejar sin recursos a los demás.
