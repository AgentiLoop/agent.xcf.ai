---
title: Bienvenue sur le blog d'Agent! : une app, n'importe quelle IA, le contrôle total de votre Mac
description: Ce qu'est AgentiLoop Agent!, pourquoi je l'ai conçu ainsi et ce que vous trouverez ici, directement à partir du code source.
tags: Annonce, Architecture
---
<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 340" role="img" aria-labelledby="map-title map-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="map-title">Un petit Mac vous tend la carte</title>
<desc id="map-desc">Un Mac souriant, posé sur un bureau, tient une carte dépliée. La carte compte quatre étapes reliées par un sentier en pointillés : Toute IA, La boucle, AgentScript et Sécurité.</desc>
<rect width="760" height="340" rx="20" fill="#eef6ff"/>
<path d="M30 290H730" stroke="#8b684c" stroke-width="10" stroke-linecap="round"/>
<rect x="132" y="228" width="16" height="52" fill="#8a97a8"/><rect x="100" y="276" width="80" height="12" rx="4" fill="#8a97a8"/>
<rect x="40" y="100" width="200" height="130" rx="14" fill="#c9d3df" stroke="#173452" stroke-width="4"/>
<rect x="54" y="114" width="172" height="102" rx="6" fill="#559ef5"/>
<circle cx="110" cy="152" r="9" fill="#fff"/><circle cx="170" cy="152" r="9" fill="#fff"/>
<circle cx="112" cy="153" r="4" fill="#173452"/><circle cx="172" cy="153" r="4" fill="#173452"/>
<path d="M115 180Q140 198 165 180" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
<path d="M228 180Q262 176 290 160" fill="none" stroke="#173452" stroke-width="6" stroke-linecap="round"/>
<path d="M290 50L400 70L510 50L620 70V260L510 240L400 260L290 240Z" fill="#fff8e6" stroke="#8b684c" stroke-width="4" stroke-linejoin="round"/>
<path d="M400 70V260M510 50V240" stroke="#e6d6b3" stroke-width="3"/>
<path d="M350 175C380 140 410 140 440 140S490 190 520 190 560 130 580 110" fill="none" stroke="#d94877" stroke-width="4" stroke-dasharray="3 10" stroke-linecap="round"/>
<circle cx="350" cy="175" r="11" fill="#559ef5" stroke="#173452" stroke-width="3"/>
<circle cx="440" cy="140" r="11" fill="#7b6ad6" stroke="#173452" stroke-width="3"/>
<circle cx="520" cy="190" r="11" fill="#22c55e" stroke="#173452" stroke-width="3"/>
<circle cx="580" cy="110" r="11" fill="#f59e0b" stroke="#173452" stroke-width="3"/>
<g font-family="system-ui,sans-serif" text-anchor="middle" fill="#173452">
<text x="350" y="152" font-size="15" font-weight="700">Toute IA</text>
<text x="440" y="117" font-size="15" font-weight="700">La boucle</text>
<text x="520" y="222" font-size="15" font-weight="700">AgentScript</text>
<text x="580" y="90" font-size="15" font-weight="700">Sécurité</text>
<text x="345" y="88" font-size="14" fill="#8b684c">Votre carte</text>
<text x="140" y="322" font-size="18">Agent! pour Mac</text>
</g>
</svg>
<figcaption>Tout blog a besoin d'un premier article. Celui-ci, c'est la carte.</figcaption>
</figure>

Bonjour, je m'appelle Todd. Je développe **AgentiLoop Agent!**, un agent d'IA natif pour macOS, et vous êtes sur son blog.

Je voulais un endroit pour expliquer les aspects d'Agent! qui ne tiennent pas dans un README ou dans des notes de version. Pourquoi tel garde-fou a cette forme-là. Pourquoi la boucle de l'agent vérifie son propre travail. Ce qui a cassé dans une release candidate, et comment on l'a réparé. L'essentiel de ce que vous lirez ici vient tout droit du code, parce que c'est ce que je connais le mieux. De temps en temps, je jetterai aussi un œil à l'univers plus large des agents d'IA et à ce qu'il implique pour votre Mac.

Si vous découvrez Agent!, commencez ici. Voyez cet article comme la carte.

## Qu'est-ce qu'Agent! ?

Agent! est 100 % natif, en Swift et SwiftUI. Vous tapez (ou dites) ce que vous voulez, et il fait vraiment le travail sur votre Mac au lieu de vous expliquer comment le faire :

- **Il écrit du vrai code.** Il lit votre projet, modifie les fichiers avec des diffs par remplacement de chaînes, compile dans Xcode, lit les erreurs, les corrige et commit avec git.
- **Il pilote n'importe quelle app Mac** via l'API d'accessibilité, ainsi qu'AppleScript, JXA et 51 passerelles ScriptingBridge vers des apps.
- **Il exécute des commandes shell en votre nom ou en tant que root**, via un Launch Agent et un Launch Daemon enregistrés avec SMAppService et joignables par XPC.
- **Il fonctionne avec 23 fournisseurs de LLM**, plus Apple Intelligence sur l'appareil : Claude, Codex, OpenAI, Gemini, Grok, Mistral, DeepSeek, Qwen, Z.ai, OpenRouter, Ollama, vLLM, LM Studio et bien d'autres.
- **Il vous écoute.** Dites *« Agent! »* suivi d'une tâche, ou envoyez-lui un message depuis votre iPhone via iMessage (expéditeurs approuvés uniquement).

Le README le résume en quatre mots : *Siri répond. Agent! agit.*

## Pas de NPM, pas d'Electron

C'est ce qui surprend le plus les gens. Pas d'enveloppe Electron. Pas de runtime Node. Pas de dossier `node_modules` qui grignote discrètement votre disque. J'ai écrit moi-même chaque package Swift dont dépend Agent!, et chacun vit dans son propre dépôt au sein de l'organisation [AgentiLoop](https://github.com/AgentiLoop) :

| Package | Rôle |
|---|---|
| AgentTools | Schémas d'outils, prompts système et gestion des fournisseurs |
| AgentLLM | Protocoles, types et registre des fournisseurs de LLM |
| AgentMCP | Client MCP (stdio et HTTP) |
| AgentAccess | Automatisation de l'accessibilité |
| AgentEventBridges | Protocoles ScriptingBridge pour plus de 50 apps Mac |
| AgentD1F | Moteur de diff multiligne |
| AgentSwift | Analyse de code avec SwiftSyntax |
| AgentColorSyntax · AgentTerminalNeo | Coloration syntaxique · markdown de terminal rétro |
| AgentAudit | Journalisation d'audit via `os.log` |

Au final, vous avez une app qui consomme très peu de RAM et qui embarque pourtant d'emblée l'automatisation de Xcode, l'analyse syntaxique Swift, l'accessibilité, AppleScript, l'automatisation de Safari et MCP.

## La boucle au cœur de tout

Dans Agent!, tout découle d'une seule idée : une **boucle de tâches auto-vérifiée**. Le modèle réfléchit, appelle un outil, regarde le résultat réel et se corrige. Ça ne marche que si on peut lui faire confiance, alors quelques règles sont gravées dans le marbre :

- **Impossible de faire semblant d'utiliser un outil.** Chaque appel passe par un répartiteur unique et renvoie une sortie réelle. Si le modèle affirme *« j'ai cliqué »* sans avoir réellement appelé d'outil, Agent! le relève et lui envoie une correction.
- **« Terminé » exige des preuves.** Une tâche ne peut se déclarer achevée tant que ses critères `goal_state` ne sont pas cochés, preuves à l'appui, comme un build au vert ou un test qui passe.
- **On lit avant de modifier.** Agent! refuse de modifier un fichier que le modèle n'a pas lu, ou qui a changé sur le disque depuis sa lecture (vérifié par SHA-256). Le refus fournit au modèle le fichier à jour, pour que la tentative suivante porte sur les bonnes lignes.
- **Tout peut être annulé.** Chaque modification est conservée en instantané pendant une semaine. Restaurez un seul fichier, ou rembobinez une tâche entière avec `rewind_task`.

Je décortiquerai chacune de ces règles dans de prochains articles.

## AgentScript : du Swift avec toutes les autorisations

AgentScript fait partie de mes briques préférées. Les scripts sont de simples fichiers Swift. Agent! compile chacun d'eux en `.dylib` avec SwiftPM et le charge dans son propre processus avec `dlopen` : votre script obtient donc les mêmes autorisations macOS qu'Agent! possède déjà (Accessibilité, Automatisation, Calendrier, Contacts, Mail, Photos et tout le reste). Il vous suffit d'un seul point d'entrée :

```swift
import Foundation
import CalendarBridge   // any `import XBridge` auto-wires, no Package.swift edits

@_cdecl("script_main")
public func scriptMain() -> Int32 {
    print("Hello from AgentScript! 👋")
    return 0
}
```

Tout ce que le script affiche est renvoyé au modèle, et la valeur de retour sert de code de sortie. L'app est livrée avec environ 35 exemples, dont `TodayEvents`, `NowPlaying`, `CheckMail` et `CreateDmg`.

## Une sécurité que vous pouvez lire

Agent! peut exécuter des commandes en tant que root. C'est demander beaucoup de confiance, donc la sécurité ne peut pas se résumer à une diapositive dans une présentation. C'est du code, et vous pouvez le lire sur GitHub. Un `ShellSafetyService` codé en dur refuse les commandes catastrophiques avant même qu'elles soient envoyées, et le daemon privilégié refait la même vérification de son côté. Il existe aussi un second avis optionnel, baptisé **Jev**, qui évalue la probabilité qu'une commande détruise des données. La [première analyse approfondie](/blog/inside-agent-shell-guardrails/) explique précisément comment tout cela fonctionne.

## La famille s'agrandit

La même boucle d'agent tourne désormais aussi dans le terminal, sous macOS, Windows et Linux. Il existe deux CLI aux capacités identiques : [AgentiLoopCLI](https://github.com/AgentiLoop/AgentiLoopCLI) en Rust et [AgentiLoopGo](https://github.com/AgentiLoop/AgentiLoopGo) en Go. Mon anecdote préférée du README : c'est Agent! pour Mac qui a écrit ses propres petits frères.

## Ce que vous trouverez ici

- **Fonctionnement interne :** la boucle de l'agent, la compaction du contexte, la répartition des outils, les sous-agents, la mémoire et les plans.
- **Sécurité :** les garde-fous, le modèle de confiance XPC et ce que les récents incidents impliquant des agents nous apprennent à tous.
- **Des notes de version qui expliquent le pourquoi :** ce qui a changé dans chaque build, et le bug qui l'a rendu nécessaire.
- **Tutoriels :** recettes AgentScript, choisir un fournisseur avec un petit budget, tout faire tourner en local.
- **L'univers des agents au sens large :** actualités et tests, toujours ramenés à ce qu'ils signifient pour votre Mac.

Agent! fonctionne sous macOS 14.6 ou version ultérieure, sur Apple Silicon comme sur Intel, et il est gratuit pour un usage personnel. Téléchargez-le ci-dessous, confiez-lui une vraie tâche, et racontez-moi comment ça s'est passé.
