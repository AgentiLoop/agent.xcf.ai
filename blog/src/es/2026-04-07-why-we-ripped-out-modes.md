---
title: Por qué eliminamos el modo de programación: dejemos que el modelo elija sus propias herramientas
description: Agent! solía adivinar si querías programar o automatizar y ocultaba herramientas en consecuencia. Una tarea fallida con Photo Booth demostró por qué el entorno debe dejar de cuestionar al modelo.
tags: Arquitectura, Diseño
---
Las primeras versiones de Agent! tenían **modos**: programación, automatización y estándar. La idea parecía razonable. Una tarea de programación no necesita la herramienta de Accesibilidad, y una tarea del tipo «haz clic en este botón» no necesita Xcode. Si ocultas lo que no es relevante, el modelo ve una lista de herramientas más corta, gasta menos tokens y se equivoca menos al elegir.

El 7 de abril de 2026, el commit `7ea44c0d` eliminó todo el sistema. Este es el bug que lo provocó y el principio que nos dejó.

## Cómo funcionaban los modos

En el segundo turno de una tarea, el entorno examinaba lo que habías pedido y lo comparaba con dos listas de palabras clave. Palabras como `build`, `compile`, `edit`, `fix` y `refactor` indicaban programación. Palabras como `click`, `button`, `window`, `photo` y `accessibility` indicaban automatización. Después activaba un indicador, `codingModeEnabled` o `automationModeEnabled`, y reducía las herramientas visibles para el modelo a los grupos de ese modo. El propio modelo también podía cambiar de modo mediante una herramienta `mode`.

## El bug: Photo Booth en modo de programación

El informe decía simplemente «la accesibilidad no funciona». La causa, en palabras del propio mensaje del commit: el cambio automático interpretó `open -a Photo Booth` como una señal desconocida y **recurrió por defecto al modo de programación**. El modo de programación excluía el grupo Auto, y el grupo Auto es donde reside la herramienta `accessibility`.

Así que se le pidió al modelo que tomara una foto, y la única herramienta diseñada para pulsar el botón del obturador había desaparecido a mitad de la tarea. Hizo lo que hace un modelo competente con las herramientas que le quedan: recurrió a `osascript` a través del shell, que fallaba una y otra vez con *«No se puede obtener la barra de herramientas 1 de la ventana 1.»*

El modelo no tenía ningún problema, y la herramienta de accesibilidad tampoco. El entorno había adivinado mal la intención y había retirado discretamente la respuesta correcta.

## La solución que no lo era

El parche obvio era añadir `open -a` a las palabras clave de automatización. El mensaje del commit lo señala sin rodeos: habría sido «un parche más en una larga lista». Detectar la intención mediante palabras clave es una batalla perdida. Cada nueva aplicación, formulación e idioma abre otro agujero, y cada fallo se produce de la forma más confusa posible: con un modelo que de repente no puede hacer algo que sí podía hacer un turno antes.

## Qué lo sustituyó: nada

Se eliminó todo el sistema de modos: 13 archivos, 141 líneas borradas y 39 añadidas. Eso incluyó:

- los indicadores `codingModeEnabled` y `automationModeEnabled` y sus listas de grupos de herramientas
- el cambio automático del turno 2, tanto en el bucle principal de tareas como en las tareas de pestaña
- `predictToolGroups()`, la función que adivinaba grupos de herramientas a partir de tu prompt
- la reducción de la lista de herramientas para endpoints locales en los servicios de Claude y compatibles con OpenAI
- los alias `coding` y `automation` para subagentes (ahora se pasan los nombres reales de los grupos)

Ahora las herramientas se filtran **únicamente según tus propios interruptores** en Ajustes (`ToolPreferencesService`). Todas las herramientas que hayas activado están disponibles en cada turno, y el modelo elige lo que necesita.

Dos pequeños detalles muestran el cuidado que exige una eliminación así. La herramienta `mode` no se eliminó por completo. Se convirtió en una operación vacía que responde *«el cambio de modo se ha eliminado»*, porque un modelo con una conversación antigua en su contexto podría seguir llamándola, y una respuesta clara es mejor que un error de herramienta desconocida. Además, la revisión del prompt del sistema pasó de 71 a 72, de modo que cualquier prompt guardado en disco que mencionara los modos se vuelve a sincronizar.

## El resultado

Se acabó el spam de registros *«Modo de programación activado automáticamente»*. Se acabaron las herramientas que desaparecen a mitad de tarea. Se acabó la lista de herramientas que cambia de un turno a otro.

## El principio

Esta decisión marcó buena parte de lo que vino después, así que vale la pena expresarlo con claridad:

> El entorno debe imponer **seguridad**, no adivinar **intenciones**.

Agent! es estricto donde el rigor es objetivo. Rechaza comandos de shell catastróficos, ediciones de archivos que el modelo no ha leído y un «terminado» sin pruebas. Son hechos que puede comprobar. Qué herramienta necesita una tarea es una cuestión de criterio, y el modelo es mejor en eso que una lista de palabras clave. Cuando el entorno invalida al modelo en una cuestión de criterio, falla en silencio y de forma confusa. Cuando impone una regla verificable, falla de forma visible y con un motivo.

Si estás creando un agente, es tentador «ayudar» al modelo recortando sus opciones. Mide primero. Una lista de herramientas algo más larga cuesta unos pocos tokens. Una herramienta que falta puede costarte la tarea entera.
