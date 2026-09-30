---
title: Sonoma, Intel et le Mac qui n’était pas encore mort
description: Agent! pour Mac fonctionne désormais sous macOS Sonoma 14.6 et ultérieur, sur Apple Silicon et Intel. Vous étiez nombreux à réclamer une version antérieure à macOS 26. La voici.
tags: Notes de version, Coulisses
---
<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 340" role="img" aria-labelledby="macs-title macs-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="macs-title">Deux Mac heureux et un nouveau panneau</title>
<desc id="macs-desc">Un Mac Intel et un Mac Apple Silicon sont posés sur un bureau, tous deux souriants. Entre eux, un panneau où « macOS 26 uniquement » est barré et remplacé par « macOS 14.6+, Apple Silicon et Intel ».</desc>
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
<text x="380" y="88" font-size="13" fill="#8a97a8">Seulement macOS 26</text>
<text x="380" y="118" font-size="19" font-weight="700">macOS 14.6+</text>
<text x="380" y="141" font-size="16">Apple Silicon</text>
<text x="380" y="162" font-size="16">et Intel</text>
<text x="190" y="315" font-size="20">Mac Intel</text>
<text x="570" y="315" font-size="20">Mac Apple Silicon</text>
</g>
<path d="M318 83H442" stroke="#d94877" stroke-width="3" stroke-linecap="round"/>
</svg>
<figcaption>Même bureau. Mêmes Mac. Nouveau panneau.</figcaption>
</figure>

Soyons honnêtes. Quand Agent! affichait « nécessite macOS 26 », beaucoup de bons Mac restaient sur le carreau.

Vous étiez sous Sonoma ? Pas de chance. Sous Sequoia ? Pareil. Et sur un Mac Intel, vous ne faisiez même pas partie de la discussion.

Ça m’a toujours embêté. Ces Mac fonctionnent encore. Des gens s’en servent tous les jours. Ils codent dessus, font tourner leur entreprise dessus et y gardent bien trop d’onglets ouverts. Ils n’ont rien fait de mal. Ils n’étaient juste pas sur le dernier OS.

C’est fini. **Agent! pour Mac fonctionne désormais sous macOS Sonoma 14.6 et ultérieur, sur Apple Silicon comme sur Intel.**

Vous êtes nombreux à attendre une version antérieure à macOS 26. Celle-ci est pour vous.

## Pourquoi c’était réservé à macOS 26 au départ

Agent! utilise le modèle intégré à l’appareil d’Apple via un framework appelé FoundationModels. Ce n’est pas le cerveau principal. C’est le fournisseur que vous choisissez qui fait le gros du travail. Mais le modèle intégré aide pour des tâches plus petites : résumer pendant la compaction du contexte, compter les tokens et préchauffer une session au lancement de l’app.

Voilà le hic. FoundationModels n’existe que sous macOS 26. Si votre code mentionne ne serait-ce qu’un de ses types, il ne compile pas pour un Mac plus ancien. Le compilateur dit non, point.

La solution de facilité, c’était donc d’exiger macOS 26 et de passer à autre chose. Facile pour moi, en tout cas. Nettement moins pour tous les autres.

Et franchement, c’était un peu bête. Le modèle intégré est un assistant. C’est un plus. Ça n’a jamais été la raison pour laquelle Agent! fonctionne. Exclure tous les Mac plus anciens à cause d’un assistant, c’est comme refuser de préparer le dîner parce qu’il n’y a plus de persil.

## Alors, comment on règle ça ?

On demande d’abord. Avant de toucher au modèle intégré, Agent! vérifie : suis-je sous macOS 26 ? Si oui, parfait, on l’utilise. Si non, ce code ne s’exécute tout simplement pas, et votre fournisseur continue de faire le vrai travail.

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 300" role="img" aria-labelledby="fork-title fork-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="fork-title">Demander avant d’utiliser</title>
<desc id="fork-desc">Un organigramme. Agent! veut le modèle intégré à l’appareil. Il demande : est-ce macOS 26 ? Oui mène à l’utilisation des assistants intégrés. Non mène à leur mise de côté, pendant que le fournisseur continue de travailler.</desc>
<defs><marker id="fork-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0 0L10 5 0 10Z" fill="#4b617e"/></marker></defs>
<rect width="760" height="300" rx="20" fill="#f0f5fb"/>
<g fill="none" stroke="#4b617e" stroke-width="4"><path d="M380 90V113" marker-end="url(#fork-arrow)"/><path d="M320 150H170V206" marker-end="url(#fork-arrow)"/><path d="M440 150H590V206" marker-end="url(#fork-arrow)"/></g>
<rect x="230" y="30" width="300" height="60" rx="18" fill="#d7eaff" stroke="#3377b9" stroke-width="3"/>
<path d="M380 115L440 150 380 185 320 150Z" fill="#fce9b6" stroke="#9a701b" stroke-width="3"/>
<rect x="40" y="210" width="260" height="66" rx="18" fill="#cff3e4" stroke="#29836a" stroke-width="3"/>
<rect x="460" y="210" width="260" height="66" rx="18" fill="#dfd9ff" stroke="#7760b5" stroke-width="3"/>
<g font-family="system-ui,sans-serif" text-anchor="middle" fill="#173452">
<text x="380" y="67" font-size="18" font-weight="700">Besoin du modèle intégré ?</text>
<text x="380" y="156" font-size="16" font-weight="700">macOS 26 ?</text>
<text x="245" y="140" font-size="17">Oui</text>
<text x="515" y="140" font-size="17">Non</text>
<text x="170" y="238" font-size="18" font-weight="700">On l’utilise.</text>
<text x="170" y="262" font-size="15">Résumés, comptage de tokens</text>
<text x="590" y="238" font-size="18" font-weight="700">On s’en passe.</text>
<text x="590" y="262" font-size="15">Votre fournisseur continue</text>
</g>
</svg>
<figcaption>Tout le secret est là. Demander avant d’utiliser.</figcaption>
</figure>

Il reste un petit détail. Swift ne permet pas à une classe de contenir une propriété dont le type n’existe pas sur l’OS en cours d’exécution. La session est donc stockée comme un simple `AnyObject` et reconvertie uniquement dans le code réservé à macOS 26. Pas joli. Mais ça marche très bien.

## Les commits

Tout s’est passé le 27 septembre 2026. Quatre commits, une journée, et tout est dans Git.

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 260" role="img" aria-labelledby="day-title day-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="day-title">27 septembre 2026, commit par commit</title>
<desc id="day-desc">Une frise chronologique de midi à 20 h. Commit ea5ce624 à 12 h 46, 4d7fca86 à 12 h 57, 3a993205 à 19 h 14 et 81079e2a à 19 h 32.</desc>
<rect width="760" height="260" rx="20" fill="#f0f5fb"/>
<g stroke="#4b617e" stroke-width="2"><path d="M121 104V130M136 130V148M639 104V130M663 130V148"/></g>
<path d="M60 130H700" stroke="#4b617e" stroke-width="4" stroke-linecap="round"/>
<g fill="#227657" stroke="#fff" stroke-width="3"><circle cx="121" cy="130" r="8"/><circle cx="136" cy="130" r="8"/><circle cx="639" cy="130" r="8"/><circle cx="663" cy="130" r="8"/></g>
<g font-family="system-ui,sans-serif" text-anchor="middle" fill="#173452">
<text x="121" y="56" font-size="16" font-weight="700">conditionner</text><text x="121" y="76" font-size="15">ea5ce624</text><text x="121" y="96" font-size="15">12 h 46</text>
<text x="136" y="166" font-size="15">12 h 57</text><text x="136" y="186" font-size="15">4d7fca86</text><text x="136" y="206" font-size="16" font-weight="700">packages à jour</text>
<text x="639" y="56" font-size="16" font-weight="700">docs</text><text x="639" y="76" font-size="15">3a993205</text><text x="639" y="96" font-size="15">19 h 14</text>
<text x="663" y="166" font-size="15">19 h 32</text><text x="663" y="186" font-size="15">81079e2a</text><text x="663" y="206" font-size="16" font-weight="700">1.1.76</text>
<g font-size="14" fill="#4b617e"><text x="60" y="244">midi</text><text x="380" y="244">16 h</text><text x="700" y="244">20 h</text></g>
</g>
</svg>
<figcaption>Heures des commits d’après Git, heure de l’Est (États-Unis).</figcaption>
</figure>

**[`ea5ce624`](https://github.com/AgentiLoop/Agent/commit/ea5ce62493aef5ca74e694a8ec85b16621ec6388)** : conditionner chaque utilisation de FoundationModels à macOS 26. Cela concerne le service du modèle, le médiateur Apple Intelligence, le préchauffage au lancement dans `AgentApp`, les résumés et le comptage de tokens dans `Compression.swift`, ainsi que `AboutSelf`. Sur les systèmes plus anciens, il indique désormais simplement « nécessite macOS 26 ou ultérieur » au lieu de refuser de compiler. Aucun changement si vous êtes déjà sous 26.

**[`4d7fca86`](https://github.com/AgentiLoop/Agent/commit/4d7fca863a15d91d8e3734f991fabfcb90da734c)** : mettre à jour les dix packages Swift d’AgentiLoop vers des versions compatibles avec macOS 14. AgentAccess, AgentAudit, AgentColorSyntax, AgentD1F, AgentEventBridges, AgentLLM, AgentMCP, AgentSwift, AgentTerminalNeo, AgentTools. Tous les dix. C’était la partie fastidieuse. On ne peut pas juste changer un chiffre dans Xcode et s’arrêter là. Tout ce dont l’app dépend doit suivre le mouvement. Ce même commit a aussi repéré qu’un appel de comptage de tokens nécessite macOS 26.4, et non 26.0 : cette vérification a donc été resserrée.

**[`3a993205`](https://github.com/AgentiLoop/Agent/commit/3a9932053630a21ec9df481c8f137cea30ff87a0)** : docs. Le README et la FAQ indiquent désormais **Apple Silicon ou Intel, macOS 14.6+**. Deux mots, « ou Intel ». Il a fallu un moment pour les mériter.

**[`81079e2a`](https://github.com/AgentiLoop/Agent/commit/81079e2a937f62d2d68389a3c124214f80cb3bc3)** : version 1.1.76, build 276, cible de déploiement 14.6. On livre.

C’est tout. Pas de magie. Juste des vérifications `#available`, des mises à jour de packages, et des compilations jusqu’à ce que ça arrête de me crier dessus.

## Les petites lignes (version honnête)

Sous Sonoma ou Sequoia, vous n’aurez pas les fonctions Apple Intelligence, parce qu’Apple ne les propose pas sur ces systèmes. Agent! fait simplement sans. Vous ne manquerez pas grand-chose. Votre fournisseur faisait déjà le vrai travail.

Un Mac Intel reste un Mac Intel. Il fera tourner Agent! sans souci avec un fournisseur cloud. Les gros modèles locaux, c’est une autre histoire. La FAQ indique déjà 64 Go ou plus pour les modèles locaux de 30B, et c’est vrai sur n’importe quel Mac, pas seulement les anciens.

Et 14.6, c’est le minimum. Si votre Mac ne peut pas faire tourner Sonoma, je ne peux rien pour vous. Je suis bon, mais pas à ce point-là.

## Les fans d’Intel, cette partie est pour vous

Je sais que beaucoup d’entre vous gardent leur Mac Intel parce qu’il fait encore le travail. Il est payé. Votre configuration est aux petits oignons. Vous savez où tout se trouve. Vous n’avez pas envie d’acheter une nouvelle machine juste pour essayer une app.

C’est tout à fait légitime. Vous ne devriez pas avoir à le faire.

Même chose pour ceux qui sont sur Apple Silicon et qui ne sont pas encore prêts à passer à macOS 26. Peut-être que vous attendez une mise à jour mineure. Peut-être qu’un outil dont vous avez besoin n’est pas encore prêt. Peut-être que vous n’en avez juste pas envie. Aucun jugement. Restez sous Sonoma aussi longtemps que vous voulez.

## Foncez le récupérer

**Agent! pour Mac. macOS Sonoma 14.6 et ultérieur. Apple Silicon et Intel.**

Si vous attendiez, l’attente est terminée. Essayez-le et dites-moi comment il tourne sur votre machine. Surtout vous, la bande Intel. Je veux savoir.

Votre Mac n’est pas encore mort. Il lui fallait juste une invitation.

Envie de la version détaillée, avec du code ? Jetez un œil à l’[article technique](/blog/agent-now-runs-on-macos-14-6-and-intel/).
