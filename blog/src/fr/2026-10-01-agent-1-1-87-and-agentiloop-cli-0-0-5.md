---
title: Toute la famille sort : Agent! 1.1.87 et AgentiLoop CLI 0.0.5
description: Agent! pour Mac accueille Auto-Pilot, six nouveaux fournisseurs, un critique plus strict et la prise en charge de macOS 14.6. Les CLI en Rust et en Go s'offrent une boîte à outils plus fournie : recherche, récupération web, tâches, AGENTS.md, /undo, commandes personnalisées et --json.
tags: Annonce, Version, Multiplateforme
---
<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 380" role="img" aria-labelledby="fam-title fam-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="fam-title">La famille AgentiLoop : une app Mac et deux terminaux</title>
<desc id="fam-desc">Une grande fenêtre Mac étiquetée Agent! 1.1.87 trône au centre. À sa gauche, une fenêtre de terminal montre un petit crabe et l'étiquette Rust 0.0.5 ; à sa droite, une fenêtre de terminal montre un petit gopher et l'étiquette Go 0.0.5. Des lignes pointillées relient les trois à un symbole de boucle commun en haut.</desc>
<rect width="760" height="380" rx="20" fill="#0f1724"/>
<g fill="#6fb6ff" opacity=".35"><circle cx="60" cy="50" r="2"/><circle cx="700" cy="70" r="2"/><circle cx="640" cy="330" r="2"/><circle cx="110" cy="320" r="2"/><circle cx="380" cy="350" r="2"/><circle cx="520" cy="40" r="2"/><circle cx="230" cy="36" r="2"/></g>
<g fill="none" stroke="#6fb6ff" stroke-width="3" stroke-dasharray="4 8" stroke-linecap="round"><path d="M380 80V112"/><path d="M350 62Q170 70 140 150"/><path d="M410 62Q590 70 620 150"/></g>
<g fill="none" stroke="#9fd2ff" stroke-width="5" stroke-linecap="round"><path d="M380 55C392 39 412 39 412 55C412 71 392 71 380 55C368 39 348 39 348 55C348 71 368 71 380 55Z"/></g>
<rect x="250" y="112" width="260" height="190" rx="16" fill="#1d2a3d" stroke="#6fb6ff" stroke-width="3"/>
<rect x="250" y="112" width="260" height="34" rx="16" fill="#26364d"/><rect x="250" y="130" width="260" height="16" fill="#26364d"/>
<circle cx="272" cy="129" r="6" fill="#ff5f57"/><circle cx="292" cy="129" r="6" fill="#febc2e"/><circle cx="312" cy="129" r="6" fill="#28c840"/>
<rect x="340" y="164" width="80" height="80" rx="20" fill="#2f7bf5"/>
<g fill="#fff"><circle cx="358" cy="186" r="5"/><circle cx="402" cy="186" r="5"/><circle cx="380" cy="204" r="5"/><circle cx="360" cy="226" r="5"/><circle cx="400" cy="226" r="5"/></g>
<g fill="none" stroke="#fff" stroke-width="2" opacity=".8"><path d="M358 186L380 204L402 186M380 204L360 226M380 204L400 226M360 226H400M358 186H402M358 186L360 226M402 186L400 226"/></g>
<text x="380" y="280" text-anchor="middle" font-family="system-ui,sans-serif" font-size="22" font-weight="700" fill="#e8f2ff">Agent! 1.1.87</text>
<rect x="40" y="150" width="190" height="150" rx="12" fill="#121c2a" stroke="#f08a4b" stroke-width="3"/>
<text x="56" y="178" font-family="ui-monospace,monospace" font-size="15" fill="#f08a4b">$ agentiloop</text>
<g fill="#f08a4b" stroke="#0f1724" stroke-width="2"><ellipse cx="135" cy="236" rx="34" ry="22"/><circle cx="92" cy="214" r="10"/><circle cx="178" cy="214" r="10"/></g>
<g stroke="#f08a4b" stroke-width="4" stroke-linecap="round"><path d="M110 256l-10 14M122 258l-6 14M148 258l6 14M160 256l10 14M100 222l8 6M170 222l-8 6"/></g>
<circle cx="124" cy="230" r="4" fill="#0f1724"/><circle cx="146" cy="230" r="4" fill="#0f1724"/>
<text x="135" y="292" text-anchor="middle" font-family="system-ui,sans-serif" font-size="17" font-weight="700" fill="#ffd2b5">Rust 0.0.5</text>
<rect x="530" y="150" width="190" height="150" rx="12" fill="#121c2a" stroke="#4fd1e8" stroke-width="3"/>
<text x="546" y="178" font-family="ui-monospace,monospace" font-size="15" fill="#4fd1e8">$ agentiloop</text>
<g stroke="#0f1724" stroke-width="2"><ellipse cx="625" cy="236" rx="30" ry="36" fill="#4fd1e8"/><circle cx="600" cy="204" r="7" fill="#4fd1e8"/><circle cx="650" cy="204" r="7" fill="#4fd1e8"/></g>
<circle cx="612" cy="222" r="9" fill="#fff"/><circle cx="638" cy="222" r="9" fill="#fff"/><circle cx="612" cy="222" r="4" fill="#0f1724"/><circle cx="638" cy="222" r="4" fill="#0f1724"/>
<text x="625" y="292" text-anchor="middle" font-family="system-ui,sans-serif" font-size="17" font-weight="700" fill="#c8f4fb">Go 0.0.5</text>
<text x="380" y="345" text-anchor="middle" font-family="system-ui,sans-serif" font-size="18" fill="#9fb6d4">Une boucle. Trois façons de la lancer.</text>
</svg>
<figcaption>La famille AgentiLoop le 1er octobre : Agent! pour Mac, plus les éditions en ligne de commande en Rust et en Go.</figcaption>
</figure>

Aujourd'hui, toute la famille sort en même temps. **Agent! 1.1.87** est la nouvelle version de l'app Mac, et **AgentiLoop CLI 0.0.5** est disponible en [Rust](https://github.com/AgentiLoop/AgentiLoopCLI/releases/tag/v0.0.5) comme en [Go](https://github.com/AgentiLoop/AgentiLoopGo/releases/tag/v0.0.5). C'est une version complète, pas une préversion, et c'est la plus grande avancée à ce jour pour les trois.

Voici les nouveautés, tout droit sorties de l'historique git.

## Agent! 1.1.87 pour Mac

La dernière version complète de l'app Mac était la 1.1.33, le 12 septembre. Il s'est passé beaucoup de choses depuis : 449 commits sont entrés dans la 1.1.87. En voici les points forts.

### 🤖 Auto-Pilot : `/auto <goal>`

La fonctionnalité phare. Donnez un objectif à Agent!, et `/auto` l'exécute sous forme d'une série de cycles sans surveillance, dans un budget de temps. Chaque cycle progresse vers l'objectif, vérifie où il en est et continue.

- Aucune limite de cycles ni d'itérations. Il fonctionne dans les onglets LLM et conserve un historique des objectifs, si bien que `/auto last` et `/auto #N` rappellent un objectif précédent.
- Les sessions survivent aux redémarrages de l'app et reprennent dans le même onglet.
- **Échap** n'arrête que le cycle en cours. **Stop All** (ou `/auto stop all`) met fin à la session.

C'est la boucle de l'agent avec l'humain qui prend volontairement du recul : vous fixez la destination et le budget, et Agent! prend le volant.

### 🔌 Six nouveaux fournisseurs, et moins de réglages à bricoler

Nouveau dans la 1.1.87 : **Sidrune AI** (avec des options de protocole OpenAI et Anthropic), **Muse Code** (réutilise votre abonnement `muse login`), **Requesty**, **A2Agent**, **OrcaRouter** et **Qwen Code** avec le Coding Plan. Il y a aussi un fournisseur expérimental, **fm serve**, qui expose Apple Foundation Models via une API Chat Completions locale.

La prise en charge de la vision est désormais détectée à partir des métadonnées du catalogue de chaque fournisseur, si bien que l'option Force Vision n'est plus nécessaire. Sous le capot, tous les fournisseurs vivent maintenant dans un seul registre, `APIProvider`, au lieu d'une douzaine de chemins de code distincts.

### 🧐 Un critique qu'on ne peut pas faire changer d'avis

Agent! dispose d'une porte critique : un second modèle relit la modification avant que la tâche soit déclarée terminée. Dans la 1.1.87, cette relecture est **imposée**. Un diff inchangé est refusé, un diff modifié est relu à nouveau, et les problèmes ne peuvent pas être balayés comme « hors périmètre ». Le critique fonctionne désormais aussi avec Codex et Apple Intelligence, et le journal indique quels problèmes il a trouvés et si le code a changé ensuite.

À ses côtés se trouve **Jev**, la couche de décision TypeSafe System One qui conseille la boucle d'outils. Ses réglages se trouvent dans les nouveaux Réglages communs LLM.

### 🧠 Un contexte plus intelligent

La compaction a été revue avec soin. Les seuils sont désormais calculés d'après le modèle *réellement utilisé* (celui de l'onglet ou celui de secours), et les fenêtres de contexte récupérées auprès d'Ollama sont mémorisées. Cela corrige un bug qui faisait compacter certains modèles à 16K. La fin conservée et la microcompaction sont bornées en tokens plutôt qu'en nombre de messages, les blocs trop volumineux sont plafonnés en premier, et les erreurs de dépassement de contexte et de `max_tokens` sont détectées de la même manière chez tous les fournisseurs.

### 🖥️ Plus de Mac, plus de langues

- **macOS 14.6 Sonoma et versions ultérieures**, sur Apple Silicon et Intel. Les fonctionnalités Apple Intelligence (Foundation Models) nécessitent macOS 26.
- L'app est traduite en espagnol, français, allemand, chinois (simplifié), russe, coréen et japonais.
- Nouvelles actions d'accessibilité : `wait_until_actionable`, `select_text_range` et `observe_start/poll/stop/list`.
- Installation avec Homebrew : `brew update && brew install --cask agentiloop-agent`.

### 🔒 Plus sûr par défaut

La suppression récursive du dossier de projet courant est désormais bloquée. Une chasse aux bugs dans toute l'app a corrigé un contournement du mode lecture seule de ShellSafety via `&`, un blocage du streaming Ollama et plusieurs plantages. `task_complete` est refusé quand le résumé renvoie à une sortie qui n'a jamais été écrite, et les modèles locaux à court de mémoire s'arrêtent immédiatement avec une raison claire au lieu de tourner en rond.

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 330" role="img" aria-labelledby="box-title box-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="box-title">Une boîte à outils plus fournie pour la CLI</title>
<desc id="box-desc">Une boîte à outils rouge ouverte, étiquetée 0.0.5. Des outils en sortent avec des étiquettes : glob et grep avec une loupe, web_fetch avec un globe, todo_write avec une liste de contrôle, /undo avec une flèche courbe, AGENTS.md avec un document et --json avec des accolades.</desc>
<rect width="760" height="330" rx="20" fill="#fff6ea"/>
<path d="M60 296H700" stroke="#c9a77f" stroke-width="10" stroke-linecap="round"/>
<path d="M240 178L270 140H490L520 178Z" fill="#b8323a" stroke="#5a1418" stroke-width="4" stroke-linejoin="round"/>
<rect x="240" y="178" width="280" height="112" rx="10" fill="#d9444d" stroke="#5a1418" stroke-width="4"/>
<path d="M340 140V120Q340 108 352 108H408Q420 108 420 120V140" fill="none" stroke="#5a1418" stroke-width="8"/>
<rect x="340" y="214" width="80" height="40" rx="8" fill="#fff" stroke="#5a1418" stroke-width="3"/>
<text x="380" y="241" text-anchor="middle" font-family="ui-monospace,monospace" font-size="20" font-weight="700" fill="#5a1418">0.0.5</text>
<g font-family="ui-monospace,monospace" font-size="17" font-weight="700" text-anchor="middle">
<g><rect x="60" y="40" width="150" height="44" rx="12" fill="#d7eaff" stroke="#3377b9" stroke-width="3"/><text x="135" y="68" fill="#173452">glob · grep</text><circle cx="232" cy="102" r="16" fill="none" stroke="#3377b9" stroke-width="5"/><path d="M244 114l14 14" stroke="#3377b9" stroke-width="6" stroke-linecap="round"/></g>
<g><rect x="60" y="120" width="140" height="44" rx="12" fill="#d9f5e4" stroke="#2f8f5b" stroke-width="3"/><text x="130" y="148" fill="#14432a">web_fetch</text><circle cx="222" cy="186" r="16" fill="#bfe9cf" stroke="#2f8f5b" stroke-width="3"/><path d="M206 186H238M222 170Q212 186 222 202Q232 186 222 170" fill="none" stroke="#2f8f5b" stroke-width="2.5"/></g>
<g><rect x="295" y="20" width="170" height="44" rx="12" fill="#fce9b6" stroke="#9a701b" stroke-width="3"/><text x="380" y="48" fill="#4a3608">todo_write</text><path d="M362 76l6 6 10-12M362 94l6 6 10-12" fill="none" stroke="#9a701b" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><path d="M386 78H404M386 96H404" stroke="#9a701b" stroke-width="4" stroke-linecap="round"/></g>
<g><rect x="560" y="40" width="140" height="44" rx="12" fill="#efe1ff" stroke="#7a4bb8" stroke-width="3"/><text x="630" y="68" fill="#341a5a">/undo</text><path d="M548 128Q520 128 520 104Q520 84 546 84" fill="none" stroke="#7a4bb8" stroke-width="5" stroke-linecap="round"/><path d="M538 74l12 10-12 10" fill="none" stroke="#7a4bb8" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></g>
<g><rect x="560" y="120" width="140" height="44" rx="12" fill="#ffe0e6" stroke="#b83a5a" stroke-width="3"/><text x="630" y="148" fill="#5a1426">AGENTS.md</text><path d="M528 172h20l8 8v26h-28z" fill="#fff" stroke="#b83a5a" stroke-width="3" stroke-linejoin="round"/></g>
<g><rect x="560" y="210" width="140" height="44" rx="12" fill="#e2e8f0" stroke="#4b617e" stroke-width="3"/><text x="630" y="238" fill="#173452">--json { }</text></g>
</g>
</svg>
<figcaption>AgentiLoop CLI 0.0.5 : la même boucle, et bien plus dans la boîte.</figcaption>
</figure>

## AgentiLoop CLI 0.0.5 : une boîte à outils plus fournie

Quand nous avons [emmené la boucle de l'agent dans le terminal](/blog/the-terminal-strikes-back/), la CLI a démarré avec cinq outils affûtés : lire, lister, écrire, éditer et bash. La version 0.0.4 lui a appris à s'arrêter proprement. La version 0.0.5 consiste à lui donner davantage de matière. Tout est arrivé d'abord en Rust puis a été reproduit commit par commit en Go, si bien que les deux éditions ont exactement les mêmes fonctionnalités.

### Nouveaux outils

| Outil | Ce qu'il fait | Demande d'abord ? |
|---|---|---|
| `glob` | Trouve des fichiers par motif | Non |
| `grep` | Recherche dans le contenu des fichiers, avec 0 à 5 lignes de contexte | Non |
| `web_fetch` | Récupère une page http(s) sous forme de texte, avec des limites de taille | **Oui** |
| `todo_write` | Tient une liste de contrôle pour les travaux en plusieurs étapes (affichez-la avec `/todos`) | Non |

`glob` et `grep` ignorent `.git`, `node_modules`, `target` et les fichiers binaires, et respectent `.gitignore`, y compris les fichiers imbriqués, la négation, l'ancrage et les règles réservées aux dossiers. Ils sont ainsi plus rapides qu'un appel à `find` dans le shell et plus sûrs que de déverser toute une arborescence dans le contexte.

### Elle lit les instructions de votre projet

Si votre dépôt contient un **`AGENTS.md`** ou un **`CLAUDE.md`**, la CLI le charge dans le prompt système, ainsi qu'un fichier dans `~/.agentiloop` pour vos préférences personnelles. Des lignes comme `@docs/style.md` importent d'autres fichiers (imbriqués et protégés contre les cycles). Pas encore de fichier ? **`/init`** écrit un `AGENTS.md` de départ avec les commandes de build et de test qu'il détecte.

### Annuler, diff et compagnie

- **`/undo`** : chaque modification faite par `write_file`, `edit_file` et `apply_patch` est journalisée par prompt, ce qui vous permet d'annuler le dernier tour de l'agent.
- **`/diff`** affiche le statut git et le diff de l'arbre de travail.
- **`/export`** enregistre la conversation en Markdown.
- **`/usage`** affiche le total de tokens depuis le démarrage et le taux de remplissage du contexte.

### Faites-la vôtre

- **Commandes slash personnalisées** : déposez un fichier Markdown dans `.agentiloop/commands/`, par exemple `review.md` contenant `Review $1 for bugs`, et `/review main.rs` l'exécute. `$ARGUMENTS` et `$1`..`$9` sont pris en charge, et `/commands` les liste.
- Les **prompts MCP** de vos serveurs apparaissent sous forme de commandes `/mcp__<server>__<prompt>`.

### Conçue pour les scripts et la CI

- **`--json`** affiche une réponse one-shot sous la forme d'un unique objet JSON : result, is_error, session_id, provider, model et usage.
- **`--allow-tool` / `--deny-tool`** définissent des règles d'autorisation par nom d'outil ou par préfixe `mcp_*`. Deny l'emporte toujours, même sur `--yes`.
- **`--append-system-prompt`** ajoute du texte au prompt système le temps d'une exécution.
- **Les pipes fonctionnent, tout simplement** : un `-` isolé dans le prompt est remplacé par stdin, donc `git diff | agentiloop "review this" -` fait exactement ce qu'il annonce.

Mis bout à bout, cela donne une étape de CI qui relit une pull request, refuse de toucher au shell et renvoie une sortie lisible par une machine :

```
git diff origin/main | agentiloop --deny-tool bash --json "review this diff" -
```

## Pourquoi les sortir ensemble ?

Parce que c'est la même idée sous trois formes. Agent! pour Mac est le produit phare : il pilote vos apps, vos builds Xcode et tout votre bureau. Les CLI emmènent la même boucle dans n'importe quel terminal sous macOS, Windows et Linux. L'Échap pour annuler de la CLI et l'Auto-Pilot de l'app Mac avec son bouton Stop All répondent à la même question sous deux angles : *comment une personne garde-t-elle la main sur une boucle qui tourne toute seule ?*

C'est ce qui nous tient le plus à cœur. Pas un avatar mignon, pas un score plus élevé sur un benchmark, mais l'humain dans la boucle : vous fixez l'objectif, vous voyez chaque étape, vous pouvez l'arrêter. Dans la CLI, `/undo` annule en plus les dernières modifications de fichiers de l'agent. Auto-Pilot ne peut pas être annulé, alors utilisez-le dans un projet suivi par git.

## Les obtenir

- **Agent! 1.1.87 pour Mac** : [téléchargement sur GitHub](https://github.com/AgentiLoop/Agent/releases/tag/v1.1.87.287) ou `brew update && brew install --cask agentiloop-agent`. macOS 14.6 ou ultérieur, Apple Silicon ou Intel.
- **AgentiLoop CLI 0.0.5 (Rust)** : [version sur GitHub](https://github.com/AgentiLoop/AgentiLoopCLI/releases/tag/v0.0.5).
- **AgentiLoopGo 0.0.5 (Go)** : [version sur GitHub](https://github.com/AgentiLoop/AgentiLoopGo/releases/tag/v0.0.5).

Les binaires de la CLI pour macOS sont signés et notarisés. Décompressez, placez `agentiloop` dans votre PATH et lancez-le ; l'assistant de configuration s'occupe du reste.

Les testeurs sont les bienvenus. Essayez `/undo` après une grosse modification, pointez-la vers un dépôt contenant un `AGENTS.md` ou branchez `--json` dans un script, puis dites-nous ce qui a cassé. Indiquez votre OS, votre fournisseur et votre modèle, et n'incluez jamais de clés d'API.
