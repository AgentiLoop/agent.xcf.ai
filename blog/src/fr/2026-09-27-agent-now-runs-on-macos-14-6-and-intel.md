---
title: Agent! fonctionne désormais sous macOS 14.6 et sur les Mac Intel : comment nous nous sommes affranchis de macOS 26
description: Agent! a été conçu autour d’Apple Intelligence sous macOS 26. Voici comment une journée de gardes #available et de mises à jour de packages l’a amené sur macOS 14.6, sur Apple Silicon comme sur Intel.
tags: Notes de version, Ingénierie
---
Jusqu’à aujourd’hui, Agent! nécessitait macOS 26. Depuis la préversion du jour, il fonctionne sous **macOS 14.6 ou ultérieur, sur Apple Silicon et Intel**. Cela concerne de nombreux Mac parfaitement fonctionnels qui étaient jusqu’ici exclus, dont beaucoup ne peuvent pas du tout exécuter Apple Intelligence.

Voici ce qu’il a fallu faire, commit par commit, en une seule journée.

## L’obstacle : FoundationModels

Agent! utilise le modèle embarqué d’Apple via le framework **FoundationModels**, qui n’existe que sous macOS 26. Ce n’est pas le cerveau principal, puisque c’est le fournisseur de votre choix qui s’en charge. Mais il remplit plusieurs rôles : des résumés rapides lors du compactage du contexte, le comptage des tokens sur l’appareil, une session préchauffée au lancement et un peu de tri.

Du code qui fait référence à un type de macOS 26 ne compile pas pour une cible de déploiement plus ancienne. La première étape (`ea5ce624`) a donc consisté à placer **chaque** utilisation de FoundationModels derrière `#available(macOS 26, *)`. Cela concernait `FoundationModelService`, `AppleIntelligenceMediator`, le préchauffage dans `AgentApp`, les résumés de compactage et le comptage des tokens dans `Compression.swift`, ainsi que `AboutSelf`.

## L’astuce : effacer le type de la propriété stockée

`#available` fonctionne pour les chemins de code, mais pas pour une propriété stockée. Une classe ne peut pas contenir un `LanguageModelSession?` lorsque ce type n’existe pas sur le système en cours d’exécution. La solution consiste à le stocker sous forme de `AnyObject?` et à le reconvertir là où il est utilisé, dans du code protégé :

```swift
/// Type-erased `LanguageModelSession` so the stored property compiles below macOS 26.
private(set) var session: AnyObject?

@available(macOS 26.0, *)
var transcript: Transcript? {
    (session as? LanguageModelSession)?.transcript
}
```

Comme le dit le message de commit, les propriétés stockées n’« entraînent » plus « le type du framework dans la structure de la classe ».

Les vérifications de disponibilité ont également obtenu une réponse honnête pour les systèmes plus anciens :

```swift
static var unavailabilityReason: String {
    guard #available(macOS 26.0, *) else { return "Apple Intelligence requires macOS 26 or later." }
    ...
}
```

Ainsi, sous macOS 14 ou 15, Apple Intelligence apparaît simplement comme indisponible, avec une raison claire, et tout le reste fonctionne. Sous macOS 26, rien ne change.

## La longue traîne : dix packages

Agent! est construit à partir de ses propres packages Swift, et chacun déclarait son propre système minimal. Le commit `4d7fca86` a fait passer les dix à des versions qui déclarent `.macOS(.v14)` :

| Package | Version |
|---|---|
| AgentAccess | 2.10.24 |
| AgentAudit | 1.3.9 |
| AgentColorSyntax | 1.2.8 |
| AgentD1F | 1.0.15 |
| AgentEventBridges | 1.1.8 |
| AgentLLM | 1.0.8 |
| AgentMCP | 1.6.10 |
| AgentSwift | 1.1.11 |
| AgentTerminalNeo | 1.37.9 |
| AgentTools | 2.53.19 |

Maîtriser toutes ses dépendances est payant dans ce genre de journée. Pas besoin d’attendre un mainteneur externe, juste dix tags.

## La surprise : 26.4

Une API nécessitait plus qu’une garde 26.0. `SystemLanguageModel.tokenCount(for:)` n’existe qu’à partir de **macOS 26.4**, sa vérification de disponibilité est donc passée de 26.0 à 26.4. Sans cela, un Mac sous 26.0 à 26.3 aurait tenté d’appeler une méthode qui n’existe pas encore. C’est un bon rappel que « le framework est disponible » et « cette méthode est disponible » ne sont pas la même question.

## Ce que vous obtenez sur les Mac plus anciens

Sous macOS 14.6 et 15, sur Apple Silicon ou Intel, Agent! fonctionne de la même manière :

- les 23 fournisseurs de LLM, dans le cloud comme en local
- la boucle d’outils complète : programmation, builds Xcode, git, shell en tant que vous-même ou en tant que root, Accessibilité, AppleScript, JXA, AgentScript, automatisation de Safari et MCP
- le compactage du contexte, qui s’appuie sur les propres résumés du modèle et sur les comptes de tokens du fournisseur, simplement sans le niveau Apple Intelligence

Seules les fonctionnalités Apple Intelligence sur l’appareil nécessitent macOS 26.

## Obtenez-le

Chaque version et préversion est livrée avec un binaire signé, notarié et agrafé. Vous n’avez jamais besoin de compiler depuis les sources :

```sh
brew update && brew install --cask agentiloop-agent
```

Ou téléchargez le `.dmg` depuis [GitHub Releases](https://github.com/AgentiLoop/Agent/releases). Si vous attendiez avec un ancien MacBook ou un Mac mini Intel, c’est le grand jour.
