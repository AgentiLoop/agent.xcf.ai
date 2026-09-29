---
title: Une version le 1er de chaque mois, et des préversions entre les deux
description: Agent! publie désormais une version stable le 1er de chaque mois. Les préversions quotidiennes (bientôt hebdomadaires) servent à essayer les nouveautés et les correctifs, et les release candidates verrouillent le tout avant le grand jour.
tags: Notes de version, Coulisses
---
Agent! a un nouveau rythme. À partir du **1er octobre 2026**, une version stable sortira le **1er de chaque mois**. Entre les deux, il y aura des préversions (pre-releases) : en ce moment, environ une par jour, et nous prévoyons de passer à une par semaine. Quelque part dans la dernière ligne droite de chaque mois, les préversions deviennent des **release candidates**, et la meilleure candidate devient la version du 1er.

C'est tout le plan. La suite de cet article raconte comment nous en sommes arrivés là, avec quelques graphiques tirés de notre propre historique git.

## D'où nous venons

Agent! 1.0.0 a été tagué le **13 mars 2026**. Depuis, le dépôt a accumulé **188 tags de version**. Ils ne sont pas arrivés de façon régulière.

<figure class="chart"><div class="chart-title">Tags de version par mois, 2026</div><div class="bars"><div class="lbl">Mars</div><div><div class="bar" style="--w:0.738"><span>57</span></div></div><div class="lbl">Avr</div><div><div class="bar" style="--w:0.880"><span>68</span></div></div><div class="lbl">Mai</div><div><div class="bar dim" style="width:3.9%"><span>3</span></div></div><div class="lbl">Juin</div><div><div class="bar dim" style="width:3.9%"><span>3</span></div></div><div class="lbl">Juil</div><div><div class="bar dim" style="width:1.3%"><span>1</span></div></div><div class="lbl">Août</div><div><div class="bar" style="--w:0.194"><span>15</span></div></div><div class="lbl">Sept</div><div><div class="bar" style="--w:0.531"><span>41</span></div></div></div><figcaption>188 tags depuis la 1.0.0 du 13 mars. Un printemps chargé, un été calme et un retour en force en septembre. Source : <code>git for-each-ref refs/tags</code>.</figcaption></figure>

Mars et avril ont été un sprint : 125 tags en deux mois, parfois plusieurs par jour. Puis l'été est arrivé. Mai, juin et juillet n'ont ajouté que sept tags à eux trois. Fin août, le rythme a repris, et septembre compte déjà 41 tags.

Les versions stables ont suivi le même chemin cahoteux. La page Releases en liste quatre : **1.0.80.170** le 25 avril, **1.0.88.182** le 3 juin, **1.0.89.183** le 26 juillet et **1.1.33.233** le 12 septembre, la version des 600 étoiles.

<figure class="chart"><div class="chart-title">Jours entre les versions stables</div><div class="bars"><div class="lbl">1.0.88</div><div><div class="bar" style="--w:0.648"><span>39 jours · 25 avr → 3 juin</span></div></div><div class="lbl">1.0.89</div><div><div class="bar" style="--w:0.880"><span>53 jours · 3 juin → 26 juil</span></div></div><div class="lbl">1.1.33</div><div><div class="bar" style="--w:0.797"><span>48 jours · 26 juil → 12 sept</span></div></div><div class="lbl">1er oct</div><div><div class="bar next" style="--w:0.315"><span>19 jours · 12 sept → 1er oct</span></div></div></div><figcaption>Chaque version stable sur GitHub, mesurée depuis la précédente. La barre hachurée est la version du 1er octobre, déjà au calendrier. Ensuite, l'écart est d'un mois, tous les mois.</figcaption></figure>

Des écarts de 39, 53 et 48 jours, ce n'est pas mal, mais on ne pouvait pas régler sa montre dessus. Si vous vouliez savoir quand viendrait le prochain Agent!, la réponse honnête était « quand il sera prêt ». Nous aimons que ce soit prêt. Nous aimons aussi savoir quand.

## La route vers le 1er octobre

Le nouveau cycle a déjà eu sa répétition générale. Après la sortie de la 1.1.33, `main` a continué d'avancer. De v1.1.37.237 le 13 septembre à v1.1.77.277 le 28 septembre, chaque tag était une préversion, et la plupart des jours il y en a eu au moins une.

<figure class="chart"><div class="chart-title">Tags par jour, 13–28 septembre</div><div class="cols"><div style="height:10.6%"><span>1</span></div><div style="height:10.6%"><span>1</span></div><div style="height:10.6%"><span>1</span></div><div style="height:42.5%"><span>4</span></div><div style="height:0.0%"><span></span></div><div style="height:53.1%"><span>5</span></div><div style="height:10.6%"><span>1</span></div><div style="height:10.6%"><span>1</span></div><div style="height:31.9%"><span>3</span></div><div style="height:21.2%"><span>2</span></div><div style="height:10.6%"><span>1</span></div><div style="height:21.2%"><span>2</span></div><div style="height:85.0%"><span>8</span></div><div class="rc" style="height:42.5%"><span>4</span></div><div class="rc" style="height:42.5%"><span>4</span></div><div class="rc" style="height:10.6%"><span>1</span></div></div><div class="cols-x"><span>13</span><span>14</span><span>15</span><span>16</span><span>17</span><span>18</span><span>19</span><span>20</span><span>21</span><span>22</span><span>23</span><span>24</span><span>25</span><span>26</span><span>27</span><span>28</span></div><div class="legend"><span><i></i>builds de préversion</span><span><i class="rc"></i>saison des RC (RC1 le 26 → RC6 le 28)</span></div><figcaption>39 tags en 16 jours. Le 25 septembre à lui seul a vu huit builds, de v1.1.61 à v1.1.68.</figcaption></figure>

Le 26 septembre, les builds ont changé de nom. **v1.1.72.272 est devenue la Release Candidate 1**, avec un nouveau titre dans ses notes de version : *Formal Release Date Oct. 1, 2026.* Les RC2 à RC5 ont suivi le 27 septembre, et la RC6 (v1.1.77.277) est sortie aujourd'hui. Les notes de chaque RC demandent aux testeurs de signaler les régressions par rapport à la version stable v1.1.33.233, pour que tout le monde compare avec la même référence.

Les RC n'étaient pas un simple changement d'étiquette. Elles apportaient de vrais correctifs :

- **RC1** a épinglé chaque paquet `Agent*` de `Package.resolved` sur son dernier tag, pour que des correctifs comme AgentTools 2.53.18 arrivent vraiment dans le build.
- **RC6** a rétabli la relecture par le critique avec les modèles Claude récents, corrigé la détection du dépassement de contexte et de max_tokens chez tous les fournisseurs, et fait en sorte que le seuil de compaction suive le modèle que vous utilisez réellement. (Ce dernier point a [son propre article de blog](/blog/context-compaction-half-the-window/).)

Chaque préversion passe par le même workflow Release qu'une version stable : elle est compilée, notariée, et le ticket est agrafé (staple) au `.zip` et au `.dmg`. Une préversion n'est pas un brouillon. C'est un build fini, avec moins de kilomètres au compteur.

## Comment se déroule un mois désormais

| Quand | Ce qui sort | À quoi ça sert |
|---|---|---|
| Le 1er | Version stable | Celle que nous recommandons à tout le monde. Homebrew et le badge Latest pointent ici. |
| La plupart des jours (bientôt chaque semaine) | Préversion | Nouveautés, expériences et correctifs, disponibles tôt pour qui les veut. |
| Dernière ligne droite du mois | Release candidates | Gel des fonctionnalités. Des correctifs uniquement, jusqu'à ce qu'une RC soit ennuyeuse, dans le meilleur sens du terme. |
| Le 1er suivant | Version stable | La meilleure RC, promue. Puis la boucle recommence. |

<figure class="chart"><div class="chart-title">Un mois, deux rythmes</div><div class="month"><span class="lbl">Maintenant</span><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="p"></b><b class="rc"></b><b class="rc"></b><b class="rc"></b><b class="rc"></b><b class="rc"></b><b class="rc"></b><b class="gold"></b></div><div class="month"><span class="lbl">Bientôt</span><b></b><b></b><b></b><b></b><b></b><b class="p"></b><b></b><b></b><b></b><b></b><b></b><b></b><b class="p"></b><b></b><b></b><b></b><b></b><b></b><b></b><b class="p"></b><b></b><b></b><b></b><b></b><b class="rc"></b><b></b><b></b><b class="rc"></b><b></b><b></b><b class="gold"></b></div><div class="legend"><span><i></i>préversion</span><span><i class="rc"></i>release candidate</span><span><i style="background:#22c55e"></i>version stable le 1er</span></div><figcaption>Une illustration, pas un calendrier : le mois se lit de gauche à droite et se termine le 1er. Aujourd'hui, il y a une préversion presque chaque jour. Bientôt, une par semaine.</figcaption></figure>

**Les préversions sont le laboratoire.** C'est là que nous essayons de nouvelles choses. Certaines idées arrivent dans une préversion, sont utilisées pour de vrai et s'améliorent en un jour ou deux. D'autres se révèlent être de mauvaises idées, et il vaut bien mieux l'apprendre avec une préversion qu'avec la version stable. Les corrections de bugs arrivent aussi ici en premier : si quelque chose vous gêne, le correctif apparaît généralement dans une préversion en quelques jours.

**Les release candidates sont le calme avant le 1er.** L'objectif de chaque cycle est simple : atteindre une RC stable avant la date de sortie, puis la publier. La série de RC d'octobre est passée de RC1 à RC6 en trois jours, et toutes portaient sur des correctifs, pas sur des fonctionnalités.

**Le 1er, c'est pour tout le monde.** Si vous voulez simplement un Agent! solide qui se met à jour une fois par mois, restez sur la version stable, et c'est tout.

## Pourquoi hebdomadaire, à terme

Une préversion par jour, c'est excellent pour l'élan, et pour nous. Pour un testeur, c'est beaucoup à suivre. Une fois le cycle mensuel bien installé, les préversions passeront à **une par semaine**. Chaque build aura ainsi quelques jours d'utilisation réelle avant l'arrivée du suivant, et les notes de chaque préversion vaudront la peine d'être lues du début à la fin.

Nous annoncerons le changement ici et dans les notes de version le moment venu.

## Comment suivre

- **Stable :** `brew update && brew install --cask agentiloop-agent`, ou récupérez le build marqué *Latest* sur la [page Releases](https://github.com/AgentiLoop/Agent/releases).
- **Préversions et RC :** elles sont sur la même [page Releases](https://github.com/AgentiLoop/Agent/releases), marquées *Pre-release*. Installez-en une, utilisez-la pour du vrai travail et dites-nous ce qui a cassé.
- **Vous avez trouvé une régression ?** Ouvrez une issue avec votre version de macOS, le fournisseur et le modèle, et la sortie pertinente du journal d'activité. Merci de ne pas y mettre vos clés d'API.

Notez le **1er octobre** dans votre agenda, puis le 1er novembre, puis le 1er décembre. Rendez-vous le premier.
