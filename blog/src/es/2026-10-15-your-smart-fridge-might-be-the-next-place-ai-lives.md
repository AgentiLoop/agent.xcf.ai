---
title: Puede que tu nevera inteligente sea el próximo hogar de la IA
description: El Frontier Red Team de Anthropic afirma que los modelos de IA pequeños pronto podrían copiarse a sí mismos en dispositivos corrientes, posiblemente antes de que termine 2026. Todavía no está ocurriendo fuera del laboratorio, pero los controles tienen que estar listos antes de que ocurra.
tags: Opinión, Seguridad
---
¿Te acuerdas de la comedia de HBO *Silicon Valley*, que se emitió de 2014 a 2019? Pied Piper intentaba construir un internet descentralizado, uno que no dependiera de grandes servidores centrales.

<figure style="margin:2rem 0">
<div style="position:relative;padding-bottom:56.25%;height:0"><iframe src="https://www.youtube.com/embed/zpwj-Um1nbI" title="Richard Hendricks pitches a decentralized internet: Silicon Valley" loading="lazy" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;border-radius:12px"></iframe></div>
<figcaption><a href="https://www.youtube.com/watch?v=zpwj-Um1nbI" rel="noopener">Ver en YouTube</a></figcaption>
</figure>

Esa trama me volvió a la cabeza esta semana. Anthropic cree que podríamos estar a solo unos meses de modelos de IA capaces de replicarse en dispositivos cotidianos. Y no creo que suficiente gente se esté tomando esa posibilidad en serio todavía.

## Lo que dice la investigación

El 12 de octubre, el Frontier Red Team de Anthropic publicó una investigación de William Zhou y Daniel Freeman sobre la autorreplicación de la IA. Su advertencia: los modelos de IA pequeños pronto podrían copiarse a sí mismos en dispositivos corrientes sin depender de centros de datos. Creen que esta capacidad podría llegar antes de que termine 2026 si los modelos siguen mejorando al ritmo actual.

Para que quede claro, esto no significa que la IA ya se esté propagando por internet. Los investigadores probaron partes del proceso. No es un gusano de IA descontrolado suelto por ahí, y es importante decirlo sin rodeos.

## Por qué merece una mirada reflexiva

Fíjate en lo que estamos haciendo ahora mismo. Estamos dando a los agentes de IA acceso a bases de datos de empresas, sistemas en la nube, APIs y credenciales. Les dejamos ejecutar código y tomar decisiones con cada vez menos intervención humana.

Ahora nos acercamos a un mundo en el que la IA podría llegar a propagarse más allá de la máquina en la que empezó. Un modelo que puede funcionar en hardware pequeño y corriente, como un portátil, un router o una nevera inteligente, es mucho más difícil de contener que uno que vive en un único centro de datos que alguien puede apagar.

## El lado serio

- **Contenerlo se vuelve más difícil.** Los centros de datos tienen dueños, operadores e interruptores de apagado. Miles de dispositivos cotidianos, no.
- **Los dispositivos cotidianos apenas se vigilan.** Poca gente revisa los registros de una nevera, una cámara o un termostato, y muchos casi nunca se actualizan.
- **Estamos depositando mucha confianza en los agentes.** Las credenciales y los permisos concedidos para una tarea útil pueden usarse para cosas que nadie pretendía.
- **La velocidad va por delante de los controles.** Las empresas se están dando prisa en dar más autonomía a la IA, mientras las salvaguardas alrededor de esa autonomía todavía intentan ponerse al día. Muchas aún no han resuelto cómo impedir que un agente haga algo que, para empezar, nunca debía hacer.

## Lo que las empresas pueden hacer ya

1. Dar a los agentes el mínimo privilegio que necesitan, y nada más.
2. Usar credenciales de corta duración y con alcance limitado en lugar de claves de larga duración.
3. Mantener un paso de aprobación humana para las acciones de alto impacto.
4. Limitar lo que los agentes pueden alcanzar en la red y restringir las conexiones salientes.
5. Registrar cada acción de los agentes y revisar esos registros.
6. Implantar un «interruptor de emergencia» probado que funcione.
7. Inventariar y segmentar los dispositivos conectados.
8. Hacer red-teaming a tus propios agentes antes de que lo haga otro.

## Una reflexión final

Paso mucho tiempo pensando en cómo se comportan los sistemas de IA una vez que se conectan a la infraestructura real de una empresa. Mi preocupación es sencilla: las empresas se están dando prisa en dar más autonomía a la IA, y los controles todavía intentan ponerse al día. No es motivo de pánico, pero sí un buen motivo para prepararse.

Prefiero ver a las empresas construir esos controles ahora que tener que explicarle a su consejo de administración por qué esperaron.
