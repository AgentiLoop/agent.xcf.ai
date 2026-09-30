---
title: Sonoma, Intel y el Mac que todavía no estaba muerto
description: Agent! para Mac ya funciona en macOS Sonoma 14.6 y posteriores, en Apple Silicon e Intel. Muchos pedisteis una versión anterior a macOS 26. Aquí la tenéis.
tags: Notas de versión, Entre bastidores
---
Seamos sinceros. Cuando Agent! decía «requiere macOS 26», un montón de Macs buenos se quedaban fuera.

Si estabas en Sonoma, mala suerte. Si estabas en Sequoia, lo mismo. Y si tenías un Mac con Intel, ni siquiera entrabas en la conversación.

Eso siempre me fastidió. Esos Macs siguen funcionando. La gente los usa todos los días. Programan en ellos, llevan sus negocios con ellos y tienen demasiadas pestañas del navegador abiertas en ellos. No hicieron nada malo. Simplemente no estaban en el sistema más nuevo.

Se acabó. **Agent! para Mac ya funciona en macOS Sonoma 14.6 y posteriores, en Apple Silicon y en Intel.**

Muchos llevabais tiempo esperando una versión anterior a macOS 26. Esta va por vosotros.

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 340" role="img" aria-labelledby="macs-title macs-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="macs-title">Dos Macs felices y un cartel nuevo</title>
<desc id="macs-desc">Un Mac con Intel y un Mac con Apple Silicon están sobre un escritorio, los dos sonriendo. Entre ellos, un cartel tiene tachado «Solo macOS 26», sustituido por «macOS 14.6+, Apple Silicon e Intel».</desc>
<rect width="760" height="340" rx="20" fill="#eef6ff"/>
<rect x="182" y="215" width="16" height="50" fill="#8a97a8"/><rect x="150" y="263" width="80" height="12" rx="4" fill="#8a97a8"/>
<rect x="562" y="215" width="16" height="50" fill="#8a97a8"/><rect x="530" y="263" width="80" height="12" rx="4" fill="#8a97a8"/>
<rect x="374" y="170" width="12" height="105" fill="#8b684c"/>
<path d="M30 280H730" stroke="#8b684c" stroke-width="10" stroke-linecap="round"/>
<rect x="90" y="100" width="200" height="125" rx="14" fill="#c9d3df" stroke="#173452" stroke-width="4"/>
<rect x="104" y="114" width="172" height="97" rx="6" fill="#559ef5"/>
<circle cx="160" cy="150" r="9" fill="#fff"/><circle cx="220" cy="150" r="9" fill="#fff"/>
<circle cx="162" cy="151" r="4" fill="#173452"/><circle cx="222" cy="151" r="4" fill="#173452"/>
<path d="M165 178Q190 196 215 178" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
<rect x="470" y="100" width="200" height="125" rx="14" fill="#e7e2f7" stroke="#173452" stroke-width="4"/>
<rect x="484" y="114" width="172" height="97" rx="6" fill="#7b6ad6"/>
<circle cx="540" cy="150" r="9" fill="#fff"/><circle cx="600" cy="150" r="9" fill="#fff"/>
<circle cx="542" cy="151" r="4" fill="#173452"/><circle cx="602" cy="151" r="4" fill="#173452"/>
<path d="M545 178Q570 196 595 178" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
<rect x="303" y="60" width="154" height="115" rx="10" fill="#fff" stroke="#8b684c" stroke-width="4"/>
<g font-family="system-ui,sans-serif" text-anchor="middle" fill="#173452">
<text x="380" y="88" font-size="16" fill="#8a97a8">Solo macOS 26</text>
<text x="380" y="118" font-size="19" font-weight="700">macOS 14.6+</text>
<text x="380" y="141" font-size="16">Apple Silicon</text>
<text x="380" y="162" font-size="16">e Intel</text>
<text x="190" y="315" font-size="20">Mac con Intel</text>
<text x="570" y="315" font-size="20">Mac con Apple Silicon</text>
</g>
<path d="M318 83H442" stroke="#d94877" stroke-width="3" stroke-linecap="round"/>
</svg>
<figcaption>El mismo escritorio. Los mismos Macs. Cartel nuevo.</figcaption>
</figure>

## Por qué era solo para 26 en primer lugar

Agent! usa el modelo en el dispositivo de Apple a través de un framework llamado FoundationModels. No es el cerebro principal. El proveedor que elijas hace el trabajo pesado. Pero el modelo en el dispositivo ayuda con tareas más pequeñas, como resumir durante la compactación del contexto, contar tokens y precalentar una sesión al abrir la app.

Aquí está la trampa. FoundationModels solo existe en macOS 26. Si tu código menciona siquiera uno de sus tipos, no compila para un Mac más antiguo. El compilador dice que no y punto.

Así que lo fácil era exigir macOS 26 y seguir adelante. Fácil para mí, claro. No tanto para todos los demás.

Y, sinceramente, era un poco absurdo. El modelo en el dispositivo es un ayudante. Está bien tenerlo. Nunca fue el motivo por el que Agent! funciona. Dejar fuera a todos los Macs antiguos por un ayudante es como negarse a hacer la cena porque se te ha acabado el perejil.

## ¿Y cómo se arregla eso?

Preguntando primero. Antes de tocar el modelo en el dispositivo, Agent! comprueba: ¿estoy en macOS 26? Si sí, genial, a usarlo. Si no, ese código simplemente no se ejecuta, y tu proveedor sigue haciendo el trabajo de verdad.

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 300" role="img" aria-labelledby="fork-title fork-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="fork-title">Pregunta antes de usarlo</title>
<desc id="fork-desc">Un diagrama de flujo. Agent! quiere el modelo en el dispositivo. Pregunta: ¿es esto macOS 26? Sí lleva a usar los ayudantes en el dispositivo. No lleva a omitirlos mientras el proveedor sigue trabajando.</desc>
<defs><marker id="fork-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0 0L10 5 0 10Z" fill="#4b617e"/></marker></defs>
<rect width="760" height="300" rx="20" fill="#f0f5fb"/>
<g fill="none" stroke="#4b617e" stroke-width="4"><path d="M380 90V113" marker-end="url(#fork-arrow)"/><path d="M320 150H170V206" marker-end="url(#fork-arrow)"/><path d="M440 150H590V206" marker-end="url(#fork-arrow)"/></g>
<rect x="230" y="30" width="300" height="60" rx="18" fill="#d7eaff" stroke="#3377b9" stroke-width="3"/>
<path d="M380 115L440 150 380 185 320 150Z" fill="#fce9b6" stroke="#9a701b" stroke-width="3"/>
<rect x="40" y="210" width="260" height="66" rx="18" fill="#cff3e4" stroke="#29836a" stroke-width="3"/>
<rect x="460" y="210" width="260" height="66" rx="18" fill="#dfd9ff" stroke="#7760b5" stroke-width="3"/>
<g font-family="system-ui,sans-serif" text-anchor="middle" fill="#173452">
<text x="380" y="67" font-size="17" font-weight="700">¿Quieres el modelo integrado?</text>
<text x="380" y="156" font-size="16" font-weight="700">¿macOS 26?</text>
<text x="245" y="140" font-size="17">Sí</text>
<text x="515" y="140" font-size="17">No</text>
<text x="170" y="238" font-size="18" font-weight="700">Se usa.</text>
<text x="170" y="262" font-size="15">Resúmenes, recuento de tokens</text>
<text x="590" y="238" font-size="18" font-weight="700">Se omite.</text>
<text x="590" y="262" font-size="15">Tu proveedor sigue trabajando</text>
</g>
</svg>
<figcaption>Ese es todo el truco. Pregunta antes de usarlo.</figcaption>
</figure>

Hay un detalle más. Swift no deja que una clase tenga una propiedad cuyo tipo no existe en el sistema en ejecución. Así que la sesión se guarda como un simple `AnyObject` y solo se vuelve a convertir dentro del código de macOS 26. No es bonito. Funciona de maravilla.

## Los commits

Todo pasó el 27 de septiembre de 2026. Cuatro commits, un día, y todo está en Git.

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 260" role="img" aria-labelledby="day-title day-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="day-title">27 de septiembre de 2026, commit a commit</title>
<desc id="day-desc">Una línea de tiempo del mediodía a las 20:00. Commit ea5ce624 a las 12:46, 4d7fca86 a las 12:57, 3a993205 a las 19:14 y 81079e2a a las 19:32.</desc>
<rect width="760" height="260" rx="20" fill="#f0f5fb"/>
<g stroke="#4b617e" stroke-width="2"><path d="M121 104V130M136 130V148M639 104V130M663 130V148"/></g>
<path d="M60 130H700" stroke="#4b617e" stroke-width="4" stroke-linecap="round"/>
<g fill="#227657" stroke="#fff" stroke-width="3"><circle cx="121" cy="130" r="8"/><circle cx="136" cy="130" r="8"/><circle cx="639" cy="130" r="8"/><circle cx="663" cy="130" r="8"/></g>
<g font-family="system-ui,sans-serif" text-anchor="middle" fill="#173452">
<text x="121" y="56" font-size="16" font-weight="700">protegerlo</text><text x="121" y="76" font-size="15">ea5ce624</text><text x="121" y="96" font-size="15">12:46</text>
<text x="136" y="166" font-size="15">12:57</text><text x="136" y="186" font-size="15">4d7fca86</text><text x="136" y="206" font-size="16" font-weight="700">actualizar paquetes</text>
<text x="639" y="56" font-size="16" font-weight="700">documentación</text><text x="639" y="76" font-size="15">3a993205</text><text x="639" y="96" font-size="15">19:14</text>
<text x="663" y="166" font-size="15">19:32</text><text x="663" y="186" font-size="15">81079e2a</text><text x="663" y="206" font-size="16" font-weight="700">1.1.76</text>
<g font-size="14" fill="#4b617e"><text x="60" y="244">mediodía</text><text x="380" y="244">16:00</text><text x="700" y="244">20:00</text></g>
</g>
</svg>
<figcaption>Horas de los commits según Git, hora del Este de EE. UU.</figcaption>
</figure>

**[`ea5ce624`](https://github.com/AgentiLoop/Agent/commit/ea5ce62493aef5ca74e694a8ec85b16621ec6388)**: proteger todos los usos de FoundationModels tras macOS 26. Eso incluye el servicio del modelo, el mediador de Apple Intelligence, el precalentamiento al arrancar en `AgentApp`, los resúmenes y el recuento de tokens en `Compression.swift`, y `AboutSelf`. En sistemas más antiguos ahora simplemente informa de que «requiere macOS 26 o posterior» en lugar de negarse a compilar. Ningún cambio si ya estás en 26.

**[`4d7fca86`](https://github.com/AgentiLoop/Agent/commit/4d7fca863a15d91d8e3734f991fabfcb90da734c)**: actualizar los diez paquetes Swift de AgentiLoop a versiones compatibles con macOS 14. AgentAccess, AgentAudit, AgentColorSyntax, AgentD1F, AgentEventBridges, AgentLLM, AgentMCP, AgentSwift, AgentTerminalNeo, AgentTools. Los diez. Esta fue la parte tediosa. No basta con cambiar un número en Xcode y darlo por hecho. Todo aquello de lo que depende la app tiene que subirse al carro. En el mismo commit también se detectó que una llamada de recuento de tokens necesita macOS 26.4, no 26.0, así que esa comprobación se afinó.

**[`3a993205`](https://github.com/AgentiLoop/Agent/commit/3a9932053630a21ec9df481c8f137cea30ff87a0)**: documentación. El README y las FAQ ahora dicen **Apple Silicon o Intel, macOS 14.6+**. Dos palabras, «o Intel». Costó un rato ganárselas.

**[`81079e2a`](https://github.com/AgentiLoop/Agent/commit/81079e2a937f62d2d68389a3c124214f80cb3bc3)**: versión 1.1.76, build 276, destino de implementación 14.6. A publicar.

Eso es todo. Sin magia. Solo comprobaciones `#available`, actualizaciones de paquetes y compilar hasta que dejó de gritarme.

## La letra pequeña (de la honesta)

En Sonoma o Sequoia no tendrás las partes de Apple Intelligence, porque Apple no las incluye ahí. Agent! simplemente las esquiva. No te perderás gran cosa. Tu proveedor ya hacía el trabajo de verdad.

Un Mac con Intel sigue siendo un Mac con Intel. Ejecutará Agent! sin problema con un proveedor en la nube. Los modelos locales grandes son otra historia. Las FAQ ya dicen 64 GB o más para modelos locales de 30B, y eso vale para cualquier Mac, no solo para los antiguos.

Y 14.6 es el mínimo. Si tu Mac no puede con Sonoma, ahí no puedo ayudarte. Soy bueno, pero no tanto.

## Gente de Intel, esta parte es para vosotros

Sé que muchos seguís con Macs con Intel porque todavía cumplen. Están pagados. Tenéis vuestro entorno a punto. Sabéis dónde está cada cosa. No queréis comprar una máquina nueva solo para probar una app.

Totalmente justo. No deberíais tener que hacerlo.

Lo mismo vale para quienes tenéis Apple Silicon y todavía no estáis listos para dar el salto a macOS 26. Quizá esperáis a una actualización menor. Quizá una herramienta que necesitáis aún no está preparada. Quizá simplemente no os apetece. Sin juicios. Quedaos en Sonoma todo lo que queráis.

## Ve a por él

**Agent! para Mac. macOS Sonoma 14.6 y posteriores. Apple Silicon e Intel.**

Si estabas esperando, se acabó la espera. Pruébalo y cuéntame qué tal va en tu máquina. Sobre todo vosotros, los de Intel. Quiero saberlo.

Tu Mac todavía no está muerto. Resulta que solo necesitaba una invitación.

¿Quieres la versión a fondo, con código? Echa un vistazo al [artículo técnico](/blog/agent-now-runs-on-macos-14-6-and-intel/).
