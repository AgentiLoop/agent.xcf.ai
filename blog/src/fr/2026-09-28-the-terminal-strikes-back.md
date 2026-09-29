---
title: Le terminal contre-attaque : la boucle de l'agent devient multiplateforme en Rust et en Go
description: Agent! est une app Mac, mais un agent de code a sa place partout où travaillent les développeurs. Voici comment la boucle de l'agent est devenue deux CLI, l'une en Rust et l'autre en Go, avec une TUI plein écran sur macOS, Windows et Linux.
tags: Annonce, Multiplateforme, Ingénierie
---
Pendant la majeure partie de son existence, Agent! a été une app Mac assumée : Swift et SwiftUI natifs, intégration profonde avec AppleScript et l'Accessibilité, et un Launch Daemon pour root. C'est toujours le produit phare. Mais ces derniers jours, quelque chose a changé dans notre façon de concevoir les agents de code, et cela sort aujourd'hui.

**La boucle de l'agent tourne désormais dans votre terminal, sur macOS, Windows et Linux.** Elle existe en deux éditions aux capacités identiques : [AgentiLoopCLI](https://github.com/AgentiLoop/AgentiLoopCLI) en Rust et [AgentiLoopGo](https://github.com/AgentiLoop/AgentiLoopGo) en Go. Et oui, Agent! pour Mac a écrit une bonne partie de ses propres petits frères.

## Le changement de paradigme : retour au terminal

La première vague d'outils de code à base d'IA vivait dans les éditeurs et les fenêtres de chat. La vague qui s'impose vit dans le **terminal**. Et pour de bonnes raisons :

- **Le terminal est déjà l'endroit où le travail se fait.** Builds, tests, git, gestionnaires de paquets et sessions SSH y vivent tous. Un agent dans le terminal n'a pas besoin d'une intégration pour chacun ; il a `bash`.
- **Il va partout.** Une CLI tourne sur une machine de build Linux, dans un conteneur, via SSH sur un Raspberry Pi ou dans une VM de développement Windows. Une app Mac tourne sur un Mac.
- **Il se compose.** Le mode one-shot (`agentiloop "explain this project"`) s'intègre directement dans les scripts et la CI.
- **Il est transparent sur ce qu'il fait.** Chaque appel d'outil, chaque diff et chaque demande d'autorisation défile en texte brut.

Les superpouvoirs de l'app Mac, comme piloter Photo Booth via l'Accessibilité ou scripter Mail avec ScriptingBridge, sont réellement propres au Mac. La **boucle de l'agent**, elle, ne l'est pas. Raisonner, appeler un outil, lire le vrai résultat, corriger et recommencer : cela fonctionne sur n'importe quel OS doté d'un shell et d'un système de fichiers. Nous avons donc extrait la boucle.

## Pourquoi deux langages ?

Nous aurions pu en choisir un seul. Au lieu de cela, nous avons porté la même conception deux fois, volontairement.

**Rust (AgentiLoopCLI)** est arrivé en premier. Le workspace a été créé le 20 septembre avec une boucle centrale, le fournisseur Anthropic, des outils intégrés et la CLI. Il est découpé en cinq crates : `agentiloop-core` (la boucle, les messages, les sessions et les autorisations), `agentiloop-provider`, `agentiloop-tools`, `agentiloop-mcp` et `agentiloop-cli`. Il tourne sur `tokio`, utilise `reqwest` avec `rustls` pour éviter d'avoir à se battre avec OpenSSL sous Windows, et dessine sa TUI avec `ratatui`. Le Markdown passe par `pulldown-cmark`, et le code bénéficie de la coloration syntaxique de `syntect`.

**Go (AgentiLoopGo)** est arrivé le 23 septembre en une rafale de commits : le cœur (messages, boucle de l'agent, compaction, sessions et autorisations) avec ses tests, puis les fournisseurs, puis le client MCP, puis la CLI avec son REPL, sa TUI, le Markdown, la coloration syntaxique, les sessions et les commandes slash. Il dessine la TUI avec `tcell`, rend le Markdown avec `goldmark`, colore avec `chroma` et gère l'édition de ligne avec `liner`. Son workflow de release cible les cinq mêmes plateformes que l'édition Rust.

Le faire deux fois, c'est la meilleure revue de conception qui soit. Tout ce qui relevait en fait d'un rustisme ou d'un goïsme saute immédiatement aux yeux, et ce qui reste, c'est la véritable architecture. Il y a aussi un avantage pratique : choisissez la toolchain en laquelle votre équipe a déjà confiance. Puis dites-nous laquelle s'en sort le mieux. 🦀 vs 🐹

## La même boucle, une surface réduite

Les deux CLI démarrent volontairement avec un jeu d'outils réduit et affûté :

| Outil | Ce qu'il fait | Demande d'abord ? |
|---|---|---|
| `read_file` | Lit un fichier avec les numéros de ligne | Non |
| `list_dir` | Liste un dossier | Non |
| `write_file` | Crée ou écrase un fichier | **Oui** |
| `edit_file` | Remplace un passage de texte exact | **Oui** |
| `bash` | Exécute une commande (`sh -c` sur Mac et Linux, `cmd /C` sur Windows) | **Oui** |

Vous en voulez plus ? Les deux éditions incluent un client MCP porté depuis AgentMCP, celui d'Agent!, qui prend en charge stdio, Streamable HTTP et l'ancien HTTP+SSE, de sorte que les outils de n'importe quel serveur MCP se branchent directement.

Les autorisations font partie du cœur, elles ne sont pas greffées sur l'interface. En Rust, un trait `PermissionPolicy` décide si chaque appel peut s'exécuter, en fonction du nom de l'outil, du fait qu'il modifie quelque chose ou non, et de son entrée. La réponse est `Allow`, `Deny` ou `Cancel`. Cette troisième option existe à cause d'un vrai agacement : appuyer sur **Échap** face à une demande d'autorisation devrait ignorer *cet appel-là*, pas mettre fin à toute la tâche. La CLI fournit une politique interactive, tandis que les tests et la CI utilisent `AllowAll`.

## Le multiplateforme se joue dans les détails

« Fonctionne sous Windows » est facile à affirmer et difficile à tenir. Voici quelques-unes des choses que cela a demandé :

- **Tuer pour de bon une commande qui s'emballe.** Quand `bash` dépasse son délai, tuer le shell ne suffit pas s'il a lancé des processus enfants. L'édition Go tue tout l'arbre de processus : un groupe de processus sous Unix, et `taskkill /T` sous Windows. Le code est réparti entre `proc_unix.go` et `proc_windows.go`.
- **La CI sur les trois OS.** Le dépôt Go exécute la CI sur macOS, Linux et Windows, et le workflow de release Rust produit cinq binaires : macOS arm64 et x86_64, Linux x86_64 et arm64, et Windows x86_64.
- **Des binaires Mac signés.** Le workflow de release peut signer et notariser les builds macOS, pour que Gatekeeper ne les bloque pas.
- **Pas d'archéologie des fichiers de configuration.** La CLI se souvient de la façon dont vous l'avez lancée : fournisseur, modèle, mode TUI et session. Après la première exécution, un simple `agentiloop` reprend exactement là où vous vous étiez arrêté.

## Une TUI qui ressemble à une app

Il y a trois façons de l'exécuter : la **TUI** plein écran (`agentiloop --tui`), un mode **chat** ligne par ligne pour les terminaux simples, et le mode **one-shot** pour les scripts. La TUI a connu quelques jours bien remplis :

- un indicateur d'activité animé dans la zone de saisie, avec un spinner, l'activité en cours et le temps écoulé
- le suivi des tokens par seconde
- des liens cliquables
- un historique des prompts conservé d'un lancement à l'autre
- des sessions reprises qui affichent la conversation précédente, pour ne pas vous laisser face à un écran vide
- `/model` alimenté par la liste des modèles en direct du fournisseur

Et quand une clé d'API est manquante ou incorrecte, elle le dit en termes simples et nomme le vrai fournisseur, au lieu de balancer une erreur 401.

## Fournisseurs

Dès le premier jour, elle fonctionne avec Claude (clé d'API ou jeton OAuth Claude Code dans le même identifiant, avec détection automatique du schéma d'authentification), OpenAI et tout serveur compatible OpenAI, les modèles locaux via Ollama ou LM Studio, et **oMLX** sur Apple Silicon. Elle lit automatiquement l'adresse et la clé d'oMLX dans `~/.omlx/settings.json`.

## Essayez la version

Aujourd'hui, nous publions la **v0.0.4**, une version stable. C'est encore jeune et ça évolue vite, et nous voulons vos retours maintenant, tant que les changements coûtent peu. Récupérez un binaire dans les [releases Rust](https://github.com/AgentiLoop/AgentiLoopCLI/releases), ou compilez l'édition Go depuis les [sources](https://github.com/AgentiLoop/AgentiLoopGo).

L'app Mac ne va nulle part. Si vous êtes sur Mac, Agent! fait toujours des choses qu'aucun terminal ne peut faire. Mais si vous avez déjà rêvé du même agent sur le serveur Linux, le portable Windows et le Raspberry Pi, le voici.
