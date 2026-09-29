---
title: Bienvenue sur le blog d'Agent! : une app, n'importe quelle IA, le contrôle total de votre Mac
description: Ce qu'est AgentiLoop Agent!, comment il est conçu et ce que couvrira ce blog quotidien, directement à partir du code source.
tags: Annonce, Architecture
---
Voici le blog officiel d'**AgentiLoop Agent!**, l'agent d'IA natif pour macOS. Le principe est simple : un article par jour, rédigé surtout à partir de ce que nous connaissons le mieux, le code lui-même. Attendez-vous à des plongées détaillées dans le fonctionnement de la boucle de l'agent, aux raisons pour lesquelles tel garde-fou a été conçu ainsi, aux nouveautés de la dernière release candidate et, de temps à autre, à un regard sur l'univers plus large des agents d'IA.

Si vous découvrez ce blog, ce premier article vous servira de carte.

## Qu'est-ce qu'Agent! ?

Agent! est une app 100 % native en Swift / SwiftUI. Vous tapez (ou dites) ce que vous voulez, et il fait le travail sur votre Mac au lieu de simplement le décrire :

- **Il code pour de vrai.** Il lit votre projet, modifie les fichiers avec des diffs par remplacement de chaînes, compile dans Xcode, lit les erreurs, les corrige et commit avec git.
- **Il pilote n'importe quelle app Mac** via l'API d'accessibilité, ainsi qu'AppleScript, JXA et 51 passerelles ScriptingBridge vers des apps.
- **Il exécute des commandes shell en votre nom ou en tant que root**, via un Launch Agent et un Launch Daemon enregistrés avec SMAppService et joignables par XPC.
- **Il dialogue avec 23 fournisseurs de LLM** en plus d'Apple Intelligence sur l'appareil : Claude, Codex, OpenAI, Gemini, Grok, Mistral, DeepSeek, Qwen, Z.ai, OpenRouter, Ollama, vLLM, LM Studio et bien d'autres.
- **Il écoute.** Dites *« Agent! »* suivi d'une tâche, ou envoyez-lui un message depuis votre iPhone via iMessage (expéditeurs approuvés uniquement).

Le README le résume en une ligne : *Siri répond. Agent! agit.*

## Pas de NPM, pas d'Electron

Ce qui surprend le plus, c'est ce qu'Agent! *n'embarque pas*. Pas d'enveloppe Electron, pas de runtime Node, pas de `node_modules`. Chaque package Swift dont il dépend a été écrit par le même auteur, et chacun vit dans son propre dépôt au sein de l'organisation [AgentiLoop](https://github.com/AgentiLoop) :

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

Résultat : une app très économe en RAM qui offre d'emblée l'automatisation de Xcode, l'analyse syntaxique Swift, l'accessibilité, AppleScript, l'automatisation de Safari et MCP.

## La boucle au cœur de tout

Tout repose sur une idée : une **boucle de tâches auto-vérifiée**. Le modèle raisonne, appelle un outil, constate le résultat réel et se corrige. Quelques règles rendent cette boucle digne de confiance :

- **Impossible de simuler un outil.** Chaque appel passe par un répartiteur unique et renvoie une sortie réelle. Si le modèle affirme *« j'ai cliqué »* sans appel d'outil, Agent! injecte une correction.
- **« Terminé » exige des preuves.** Une tâche ne peut se déclarer achevée tant que ses critères `goal_state` ne sont pas marqués comme remplis, preuves à l'appui, par exemple un build au vert ou un test réussi.
- **On lit avant de modifier.** Toute modification d'un fichier que le modèle n'a pas lu, ou qui a changé sur le disque depuis sa lecture (vérifié par SHA-256), est refusée. Le refus lit lui-même le fichier pour le modèle, afin que la tentative suivante s'appuie sur des lignes à jour.
- **Tout est réversible.** Chaque modification est conservée sous forme d'instantané pendant une semaine. Vous pouvez restaurer un seul fichier ou rembobiner une tâche entière avec `rewind_task`.

Nous décortiquerons chacune de ces règles dans de prochains articles.

## AgentScript : du Swift avec toutes les autorisations

L'une des briques les plus originales est **AgentScript**. Les scripts sont de simples fichiers Swift. Agent! compile chacun d'eux en `.dylib` avec SwiftPM et le charge dans son propre processus avec `dlopen` : le script hérite ainsi des autorisations macOS d'Agent! (Accessibilité, Automatisation, Calendrier, Contacts, Mail, Photos, etc.). Un seul point d'entrée suffit pour en écrire un :

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

Agent! peut s'exécuter en tant que root : la sécurité n'est donc pas une simple diapositive dans une présentation. C'est du code que vous pouvez ouvrir sur GitHub. Un `ShellSafetyService` codé en dur refuse les commandes catastrophiques avant leur envoi, et le daemon privilégié refait la même vérification de son côté. Un second avis optionnel, baptisé **Jev**, évalue la probabilité qu'une commande détruise des données. Notre [première analyse approfondie](/blog/inside-agent-shell-guardrails/) explique précisément comment tout cela fonctionne.

## La famille s'agrandit

La même boucle d'agent tourne désormais aussi dans le terminal sous macOS, Windows et Linux, sous la forme de deux CLI aux capacités identiques : [AgentiLoopCLI](https://github.com/AgentiLoop/AgentiLoopCLI) en Rust et [AgentiLoopGo](https://github.com/AgentiLoop/AgentiLoopGo) en Go. Anecdote tirée du README : c'est Agent! pour Mac qui a écrit ses propres petits frères.

## Ce que vous trouverez ici

- **Fonctionnement interne :** la boucle de l'agent, la compaction du contexte, la répartition des outils, les sous-agents, la mémoire et les plans.
- **Sécurité :** les garde-fous, le modèle de confiance XPC et les leçons que les récents incidents impliquant des agents offrent à ceux qui les conçoivent.
- **Des notes de version qui expliquent le pourquoi :** ce qui a changé dans chaque build, et le bug qui en est à l'origine.
- **Tutoriels :** recettes AgentScript, choix d'un fournisseur avec un budget serré, fonctionnement entièrement en local.
- **L'univers des agents au sens large :** actualités et tests, toujours rattachés à ce qu'ils signifient pour votre Mac.

Agent! fonctionne sous macOS 14.6 ou version ultérieure, sur Apple Silicon comme sur Intel, et il est gratuit pour un usage personnel. Téléchargez-le ci-dessous, puis revenez demain.
