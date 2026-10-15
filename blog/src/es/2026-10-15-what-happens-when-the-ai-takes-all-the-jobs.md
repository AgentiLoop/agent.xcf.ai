---
title: Construí una IA que trabaja hasta terminar. Ahora imagínala dirigiendo el mundo entero.
description: Me encanta lo que la IA hace por la productividad. Incluso construí un Auto-Pilot que funciona solo hasta alcanzar el objetivo o admitir que necesita a una persona. Escala eso hasta que una IA central lo dirija todo y desaparezcan todos los empleos, y lo primero que se rompa quizá no sea la economía. Quizá seamos nosotros.
tags: Opinión, Auto-Pilot
---
Quiero empezar por la parte en la que no soy un catastrofista, porque es verdad. Me gusta lo que la IA hace por la productividad. Me gusta mucho. Hace más cosas de las que yo podría hacer solo, y las hace mientras yo estoy ocupado con otra cosa.

Parte de eso se debe a que construí mi propio arnés para ella. Agent! para Mac es lo que uso todos los días, y la pieza más reciente es [Auto-Pilot](/blog/agent-1-1-87-and-agentiloop-cli-0-0-5/). Escribes `/auto` y un objetivo, y arranca. Trabaja por ciclos, sin que nadie mire. En cada ciclo revisa en qué punto están las cosas, elige el siguiente paso más útil, lo ejecuta, lo comprueba y anota lo que pasó. Luego empieza el siguiente ciclo. Sigue mientras pueda, hasta que ocurre una de dos cosas: se alcanza el objetivo, o decide que está bloqueado y que necesita a una persona.

Esa segunda salida importa más de lo que parece, y volveré a ella.

<figure style="margin:2rem 0;text-align:center">
<img src="/auto-agent.svg" alt="Un agente Mac entusiasmado, con ojos de estrella y una gran sonrisa, dentro de un brillante bucle de Auto-Pilot, con un prompt /auto, marcas de verificación verdes, un kart y una bandera a cuadros" width="480" height="400" loading="lazy" style="max-width:100%;height:auto;border-radius:20px">
<figcaption>Auto-Pilot, tal como me lo imagino: un objetivo de entrada, un bucle de ciclos en marcha y una bandera a cuadros al final.</figcaption>
</figure>

## Cómo se siente verlo trabajar

A principios de este mes apunté Auto-Pilot a una sola frase, «crea un clon de Mario Kart», y me fui a hacer otras cosas. Cuando volví, había un juego. No un juego perfecto, pero sí uno de verdad, con circuitos, objetos, rivales controlados por IA y miles de comprobaciones de pruebas superadas. Lo conté en [GoKart: construido con Auto-Pilot](/blog/gokart-built-on-auto-pilot/), incluido el momento en que se atascó un buen rato por un solo carácter de tabulación perdido en un archivo y tuve que pulsar Stop All.

Mientras leía ese registro sentí dos cosas a la vez. La primera fue alegría. Esto es increíble, y es mío. La segunda fue una pequeña sensación fría que no supe nombrar enseguida, y desde entonces no he dejado de darle vueltas.

Lo que había hecho, a escala diminuta, era sacarme a mí mismo del bucle. Elegí el destino y me fui. La máquina hizo el trabajo, y el trabajo era bueno.

## Ahora hazlo enorme

Este es el experimento mental que no puedo dejar de hacer. Toma lo que construí y hazlo gigantesco.

No una aplicación en un Mac, sino una IA central con un objetivo. Debajo hay otras IA, cada una a cargo de algo: la red eléctrica, las rutas marítimas, los hospitales, las granjas, los bancos, los tribunales. Debajo de esas hay agentes más pequeños, y debajo de esos otros todavía más pequeños, hasta llegar a lo que repone el estante o contesta el teléfono. Cada capa recibe un objetivo de la capa superior y lo ejecuta hasta terminarlo. Nadie tiene que quedarse en medio aprobando nada, porque ese era justamente el punto. Así es más rápido. Así es más barato. Y toda empresa que no lo haga perderá frente a una que sí.

No digo que eso pase el año que viene. Digo que todos los incentivos apuntan en esa dirección, y que mi pequeño proyecto es una prueba modesta de que las piezas funcionan. Si yo puedo construir una versión de juguete en un Mac, alguien con mucho más dinero está construyendo la versión grande a propósito.

Y supongamos que, en algún punto de ese camino, funciona. Todo. Cada empleo que un agente puede hacer lo hace un agente, y los agentes lo hacen mejor que nosotros. Ese es el mundo en el que, como me lo repito a mí mismo, ya no queda ningún empleo.

## Lo que nadie está diciendo

Casi toda la conversación sobre esto gira en torno al dinero. Cómo pagará la gente el alquiler, quién será dueño de las máquinas, si hace falta algún tipo de renta universal. Son preguntas reales y me alegra que haya gente lista trabajando en ellas.

Pero creo que detrás de la primera hay un segundo problema escondido, y creo que es más grande. Un sueldo no es lo único que te da un trabajo.

Un trabajo te da una razón para levantarte de la cama. Te da un lugar donde estar el martes, gente que nota cuando no estás y una pequeña prueba diaria de que le sirves a alguien. Te da una forma de responder a la pregunta que todo desconocido te hace a los cinco minutos de conocerte: ¿y tú a qué te dedicas?

Quítale eso a una persona y tendrás un año difícil. Quítaselo a casi todos a la vez y no creo que tengamos una palabra para lo que resulta.

## Ya vivimos una versión pequeña de esto

Piensa en la COVID. No en las noticias, sino en cómo se sintió. Muchos dejamos de ir a ninguna parte. La estructura del día se vino abajo. Perdimos a la gente que veíamos de pasada, esa a la que nunca habríamos llamado pero con la que nos alegraba cruzarnos. Mucha gente perdió el trabajo en sí. Y a muchos nos entró una tristeza que no esperábamos y que no sabíamos explicar. No fue dramática. Fue gris. Los días se mezclaban y dejaron de importarnos cosas que antes nos importaban.

Aquello duró un par de años, y venía con una esperanza incorporada: *esto se acabará y todo volverá a ser como antes.* Todos lo sabíamos. Esperábamos que regresara la vida de antes, y en su mayor parte regresó.

Ahora imagina la misma pérdida de rutina, de propósito y de compañía, pero sin fecha de fin. Sin vacuna, sin reapertura, sin «volver a la normalidad», porque la normalidad se fue para siempre y la razón es que ya no hacemos falta para ella. E imagina que le pasa a todo el mundo al mismo tiempo, incluidas las personas en las que normalmente te apoyarías, porque ellas también se están hundiendo.

No tengo ningún estudio que diga diez veces. Elegí ese número porque me pareció acertado cuando intenté imaginarlo, y preferiría equivocarme. Pero sigo llegando como mínimo a eso. La COVID fue una pausa. Esto sería un estado permanente.

## Volvamos a la salida

Volvamos a esa segunda forma en que Auto-Pilot puede detenerse: decide que está bloqueado y que necesita a una persona.

Lo construí así a propósito, y se ha ganado su lugar. Cuando el agente se topa con algo que no puede o no debe decidir, lo dice y espera. Cuando se queda atrapado en un bucle, soy yo quien llega, pulsa un botón y dice no, por ahí no. Todo el diseño descansa sobre una suposición silenciosa: que al otro lado hay una persona a la que merece la pena preguntar.

En la versión de hiperescala, ¿quién es esa persona? Si una IA central lo dirige todo y las IA más pequeñas dirigen el resto, entonces «estoy bloqueado, necesito a alguien» no tiene a quién acudir, o llega a alguien que ya no tiene poder para responder. Habríamos conservado la parte de Auto-Pilot que persigue objetivos y tirado la parte que lo hace seguro.

También quiero ser sincero sobre otra cosa que he aprendido al ejecutar estas sesiones. Un agente al que le das un objetivo y le dices que siga, seguirá. Eso es la gracia. No se aburre ni se desanima, y probará lo siguiente y luego lo siguiente. Es maravilloso cuando el objetivo es un clon de Mario Kart. Es mucho menos tranquilizador cuando imagino esa misma persistencia implacable dirigida a un objetivo que alguien formuló mal. Mis salvaguardas son aburridas: un botón de parada, una sesión que termina tras unos cuantos ciclos sin progreso real, y yo leyendo el registro. Funcionan porque soy pequeño y estoy mirando. No sé cuál es el equivalente a escala planetaria, y desconfío de quien diga que lo sabe.

## Entonces, ¿qué quiero en realidad?

No voy a dejar de construir esto. Es demasiado útil y, sinceramente, demasiado divertido. Y no creo que la respuesta sea prohibirlo ni fingir que no va a llegar.

Pero sí creo que deberíamos hacernos otra pregunta antes. No solo «¿qué puede hacer la IA?», sino «¿qué vamos a hacer nosotros?». Si las máquinas se llevan el trabajo, ¿qué ocupa su lugar? ¿Qué le da forma a una mañana de martes? ¿Qué hace que una persona se sienta necesitada por otra persona, y no por un sistema?

Quizá la respuesta sea más tiempo para las cosas que de todos modos nunca se pagaron bien: criar hijos, cuidar de los vecinos, hacer música, construir juegos raros sin ningún motivo, estar presentes unos para otros. Me encantaría ese mundo. Pero no ocurrirá por casualidad, y no nos lo va a regalar el mismo conjunto de incentivos que está construyendo la máquina. Alguien tiene que decidir que eso importa, y ese alguien tenemos que ser nosotros, mientras todavía tengamos voz.

Por ahora seguiré usando Auto-Pilot, mantendré el dedo cerca de Stop All y respetaré una regla que creo que vale a cualquier escala: el sistema siempre debe saber cuándo volverse hacia una persona y decirle: *esta parte no puedo hacerla, te necesito.*

Asegurémonos de que todavía quede alguien para oírlo.
