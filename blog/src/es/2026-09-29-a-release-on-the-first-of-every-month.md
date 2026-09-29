---
title: Una versión el día 1 de cada mes, y versiones preliminares entre medias
description: Agent! publica ahora una versión estable el día 1 de cada mes. Las versiones preliminares diarias (pronto semanales) son donde se prueban las novedades y correcciones, y las release candidates lo dejan todo atado antes del gran día.
tags: Notas de versión, Entre bastidores
---
Agent! tiene un nuevo ritmo. A partir del **1 de octubre de 2026** habrá una versión estable el **día 1 de cada mes**. Entre medias habrá versiones preliminares (pre-releases): ahora mismo, más o menos una al día, y tenemos previsto bajar a una por semana. En algún momento del último tramo de cada mes, las versiones preliminares pasan a ser **release candidates**, y la mejor candidata se convierte en la versión del día 1.

Ese es todo el plan. El resto de esta entrada cuenta cómo llegamos hasta aquí, con algunos gráficos de nuestro propio historial de git.

## De dónde venimos

Agent! 1.0.0 se etiquetó el **13 de marzo de 2026**. Desde entonces el repositorio ha acumulado **188 etiquetas de versión**. No llegaron de forma regular.

<figure class="chart"><div class="chart-title">Etiquetas de versión por mes, 2026</div><div class="bars"><div class="lbl">Mar</div><div><div class="bar" style="--w:0.738"><span>57</span></div></div><div class="lbl">Abr</div><div><div class="bar" style="--w:0.880"><span>68</span></div></div><div class="lbl">May</div><div><div class="bar dim" style="width:3.9%"><span>3</span></div></div><div class="lbl">Jun</div><div><div class="bar dim" style="width:3.9%"><span>3</span></div></div><div class="lbl">Jul</div><div><div class="bar dim" style="width:1.3%"><span>1</span></div></div><div class="lbl">Ago</div><div><div class="bar" style="--w:0.194"><span>15</span></div></div><div class="lbl">Sep</div><div><div class="bar" style="--w:0.531"><span>41</span></div></div></div><figcaption>188 etiquetas desde la 1.0.0 del 13 de marzo. Una primavera intensa, un verano tranquilo y una vuelta a lo grande en septiembre. Fuente: <code>git for-each-ref refs/tags</code>.</figcaption></figure>

Marzo y abril fueron un sprint: 125 etiquetas en dos meses, a veces varias en un mismo día. Luego llegó el verano. Mayo, junio y julio sumaron siete etiquetas entre los tres. A finales de agosto el ritmo volvió a subir, y septiembre lleva 41 etiquetas por ahora.

Las versiones estables siguieron el mismo camino accidentado. La página de Releases muestra cuatro: **1.0.80.170** el 25 de abril, **1.0.88.182** el 3 de junio, **1.0.89.183** el 26 de julio y **1.1.33.233** el 12 de septiembre, la versión de las 600 estrellas.

<figure class="chart"><div class="chart-title">Días entre versiones estables</div><div class="bars"><div class="lbl">1.0.88</div><div><div class="bar" style="--w:0.648"><span>39 días · 25 abr → 3 jun</span></div></div><div class="lbl">1.0.89</div><div><div class="bar" style="--w:0.880"><span>53 días · 3 jun → 26 jul</span></div></div><div class="lbl">1.1.33</div><div><div class="bar" style="--w:0.797"><span>48 días · 26 jul → 12 sep</span></div></div><div class="lbl">1 oct</div><div><div class="bar next" style="--w:0.315"><span>19 días · 12 sep → 1 oct</span></div></div></div><figcaption>Cada versión estable en GitHub, medida desde la anterior. La barra rayada es la versión del 1 de octubre, que ya está en el calendario. A partir de ahí, el intervalo es de un mes, todos los meses.</figcaption></figure>

Intervalos de 39, 53 y 48 días no están mal, pero no podías poner el reloj en hora con ellos. Si querías saber cuándo llegaba el próximo Agent!, la respuesta sincera era «cuando esté listo». Nos gusta que esté listo. También nos gusta saber cuándo.

## El camino hacia el 1 de octubre

El nuevo ciclo ya tuvo su ensayo general. Tras publicar la 1.1.33, `main` siguió avanzando. Desde la v1.1.37.237 del 13 de septiembre hasta la v1.1.77.277 del 28 de septiembre, cada etiqueta fue una compilación preliminar, y la mayoría de los días hubo al menos una.

<figure class="chart"><div class="chart-title">Etiquetas por día, 13–28 de septiembre</div><div class="cols"><div style="height:10.6%"><span>1</span></div><div style="height:10.6%"><span>1</span></div><div style="height:10.6%"><span>1</span></div><div style="height:42.5%"><span>4</span></div><div style="height:0.0%"><span></span></div><div style="height:53.1%"><span>5</span></div><div style="height:10.6%"><span>1</span></div><div style="height:10.6%"><span>1</span></div><div style="height:31.9%"><span>3</span></div><div style="height:21.2%"><span>2</span></div><div style="height:10.6%"><span>1</span></div><div style="height:21.2%"><span>2</span></div><div style="height:85.0%"><span>8</span></div><div class="rc" style="height:42.5%"><span>4</span></div><div class="rc" style="height:42.5%"><span>4</span></div><div class="rc" style="height:10.6%"><span>1</span></div></div><div class="cols-x"><span>13</span><span>14</span><span>15</span><span>16</span><span>17</span><span>18</span><span>19</span><span>20</span><span>21</span><span>22</span><span>23</span><span>24</span><span>25</span><span>26</span><span>27</span><span>28</span></div><div class="legend"><span><i></i>compilaciones preliminares</span><span><i class="rc"></i>temporada de RC (RC1 el 26 → RC6 el 28)</span></div><figcaption>39 etiquetas en 16 días. Solo el 25 de septiembre salieron ocho compilaciones, de la v1.1.61 a la v1.1.68.</figcaption></figure>

El 26 de septiembre las compilaciones cambiaron de nombre. **La v1.1.72.272 pasó a ser la Release Candidate 1**, con un nuevo titular en sus notas de versión: *Formal Release Date Oct. 1, 2026.* De la RC2 a la RC5 llegaron el 27 de septiembre, y la RC6 (v1.1.77.277) se publicó hoy. Las notas de cada RC piden a los testers que informen de regresiones respecto a la versión estable v1.1.33.233, para que todo el mundo compare con la misma referencia.

Las RC no fueron un simple cambio de etiqueta. Traían correcciones reales:

- **RC1** fijó cada paquete `Agent*` de `Package.resolved` a su última etiqueta, para que correcciones como AgentTools 2.53.18 lleguen de verdad a la compilación.
- **RC6** volvió a hacer funcionar la revisión del crítico con los modelos Claude más recientes, corrigió la detección de desbordamiento de contexto y de max_tokens en todos los proveedores, e hizo que el umbral de compactación siga al modelo que realmente estás usando. (Esto último tiene [su propia entrada en el blog](/blog/context-compaction-half-the-window/).)

Cada versión preliminar pasa por el mismo flujo de Release que una versión estable: se compila, se notariza y se graba el ticket (staple) en el `.zip` y el `.dmg`. Una versión preliminar no es un borrador. Es una compilación terminada con menos kilómetros.

## Cómo funciona un mes ahora

| Cuándo | Qué se publica | Para qué sirve |
|---|---|---|
| El día 1 | Versión estable | La que recomendamos a todo el mundo. Homebrew y la insignia Latest apuntan aquí. |
| Casi todos los días (pronto semanal) | Versión preliminar | Novedades, experimentos y correcciones, disponibles pronto para quien las quiera. |
| Último tramo del mes | Release candidates | Congelación de funciones. Solo correcciones, hasta que una RC sea aburrida en el mejor sentido. |
| El siguiente día 1 | Versión estable | La mejor RC, ascendida. Y el ciclo vuelve a empezar. |

<figure class="chart"><div class="chart-title">Un mes, dos ritmos</div><div class="month"><span class="lbl">Ahora</span><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="rc"></b><b class="rc"></b><b class="rc"></b><b class="rc"></b><b class="rc"></b><b class="rc"></b><b class="gold"></b></div><div class="month"><span class="lbl">Pronto</span><b></b><b></b><b></b><b></b><b></b><b class="p"></b><b></b><b></b><b></b><b></b><b></b><b></b><b class="p"></b><b></b><b></b><b></b><b></b><b></b><b></b><b class="p"></b><b></b><b></b><b></b><b></b><b class="rc"></b><b></b><b></b><b class="rc"></b><b></b><b></b><b class="gold"></b></div><div class="legend"><span><i></i>versión preliminar</span><span><i class="rc"></i>release candidate</span><span><i style="background:#22c55e"></i>versión estable el día 1</span></div><figcaption>Una ilustración, no un calendario: el mes avanza de izquierda a derecha y termina el día 1. Hoy hay una versión preliminar casi todos los días. Pronto, una por semana.</figcaption></figure>

**Las versiones preliminares son el laboratorio.** Es donde probamos cosas nuevas. Algunas ideas llegan a una versión preliminar, se usan de verdad y mejoran en uno o dos días. Otras resultan ser mala idea, y es mucho mejor descubrirlo en una versión preliminar que en la estable. Las correcciones de errores también llegan aquí primero, así que si algo te molesta, lo normal es que el arreglo aparezca en una versión preliminar en cuestión de días.

**Las release candidates son la calma antes del día 1.** El objetivo de cada ciclo es sencillo: llegar a una RC estable antes de la fecha de lanzamiento y publicarla. La serie de RC de octubre pasó de RC1 a RC6 en tres días, y todas trataban de correcciones, no de funciones nuevas.

**El día 1 es para todo el mundo.** Si solo quieres un Agent! sólido que se actualice una vez al mes, quédate en la versión estable y listo.

## Por qué semanal, más adelante

Una versión preliminar al día es genial para el impulso, y para nosotros. Para un tester es mucho que seguir. Cuando el ciclo mensual se asiente, las versiones preliminares pasarán a publicarse **una vez por semana**. Así cada compilación tendrá unos días de uso real antes de que llegue la siguiente, y merecerá la pena leer las notas de cada versión preliminar de principio a fin.

Anunciaremos el cambio aquí y en las notas de versión cuando ocurra.

## Cómo seguirlo

- **Estable:** `brew update && brew install --cask agentiloop-agent`, o descarga la compilación marcada como *Latest* en la [página de Releases](https://github.com/AgentiLoop/Agent/releases).
- **Versiones preliminares y RC:** están en la misma [página de Releases](https://github.com/AgentiLoop/Agent/releases), marcadas como *Pre-release*. Instala una, úsala para trabajo real y cuéntanos qué se ha roto.
- **¿Has encontrado una regresión?** Abre un issue con tu versión de macOS, el proveedor y el modelo, y la salida relevante del registro de actividad. Por favor, no incluyas tus claves de API.

Apunta el **1 de octubre** en tu calendario, luego el 1 de noviembre, luego el 1 de diciembre. Nos vemos el día 1.
