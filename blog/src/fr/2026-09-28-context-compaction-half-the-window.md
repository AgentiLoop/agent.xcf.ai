---
title: Pourquoi Agent! compacte à la moitié de la fenêtre, et les trois bugs qui l'ont réduite à 16K
description: Comment la compaction de contexte d'Agent! décide quand résumer une longue tâche, et les correctifs du 28 septembre pour les modèles de repli, Ollama et une fenêtre Codex de 272K.
tags: Fonctionnement interne, Notes de version
---
Les longues tâches d'agent se heurtent à un problème de physique. Chaque appel d'outil ajoute sa sortie à la transcription : une lecture de fichier, un log de build, un diff. Tôt ou tard, la transcription ne tient plus dans la fenêtre de contexte du modèle et le fournisseur rejette la requête. Un agent qui tourne toute la nuit doit donc **compacter** : réduire la conversation tout en conservant l'essentiel.

La compaction se trouve dans `Agent/AgentViewModel/Messages/Compression.swift`. Le 28 septembre, elle a reçu trois correctifs en une seule soirée, tous pour le même symptôme : des tâches compactées à 16K tokens sur des modèles dotés de fenêtres bien plus grandes. Voici comment fonctionne le système, et ce qui a mal tourné.

## Quand compacter : à la moitié de la fenêtre, avec un plafond

Le déclencheur est une struct nommée `CompactionState`. Son cœur tient en une seule fonction :

```swift
static func threshold(for contextWindow: Int, maxTokens: Int = 0) -> Int {
    let byFraction = Int(Double(min(contextWindow, compactionWindowCap)) * compactionFraction)
    let reservedOutput = maxTokens > 0 ? min(maxTokens, contextWindow / 2) : 8_192
    return max(2_000, min(byFraction, contextWindow - reservedOutput))
}
```

Avec `compactionFraction = 0.5` et `compactionWindowCap = 256_000`, cela donne :

- **Compacter à 50% de la fenêtre.** Il s'agit d'un pourcentage plutôt que d'un nombre fixe de tokens. L'autre moitié constitue le budget de sortie, si bien que l'entrée et la sortie tiennent toujours ensemble.
- **Jamais au-delà de 128K.** Les fenêtres annoncées au-dessus de 256K (Claude 1M, MiniMax 1M, Gemini et Grok 2M) compactent toutes à 128K. Une fenêtre de 200K compacte à 100K.
- **Toujours laisser de la place pour la réponse.** Le seuil ne peut pas être si tardif que la sortie réservée ne tienne plus.
- **Jamais en dessous de 2K**, un plancher pour les tout petits modèles locaux.

Pourquoi plafonner une fenêtre de 2M à 128K ? Le commentaire est sans détour. Avec des fenêtres annoncées gigantesques, un pourcentage sans plafond retarde tellement la compaction que le moindre écart côté fournisseur se transforme en véritable dépassement de contexte au lieu d'une compaction. Par exemple, un routeur qui sert une fenêtre plus courte que celle qu'il annonce, ou un prompt système mal comptabilisé. Compacter tôt coûte un résumé. Compacter trop tard coûte la tâche.

## La mesure : se fier au fournisseur, puis estimer

Pour comparer avec le seuil, il faut un nombre de tokens. Le deviner à partir des caractères est approximatif, alors `measuredTokens` privilégie la réalité : les `input_tokens` que le fournisseur a indiqués pour la dernière requête. Ce nombre inclut le prompt système et les schémas d'outils, qu'une estimation locale ne peut pas voir. Seuls les messages ajoutés *depuis* ce relevé sont estimés.

Sans relevé, il se rabat sur l'estimation classique caractères ÷ 4, majorée de 25%, car le code dense se rapproche plutôt de 3.3 caractères par token. Avant de payer une compaction sur la seule foi d'une estimation, la boucle la confirme avec un compteur exécuté sur l'appareil.

## Comment elle compacte : par paliers

Lorsque le seuil est franchi, `tieredCompact` enchaîne des étapes de plus en plus radicales :

1. **Palier 0 : un résumé structuré** de la transcription *complète* par le modèle actif. Il passe en premier pour que le modèle qui résume voie encore la sortie des outils qu'il résume.
2. **Microcompaction :** les anciens résultats d'outils deviennent de courts marqueurs récupérables. L'outil `restore_tool_result` peut restaurer n'importe lequel d'entre eux.
3. **Suppression des images :** les captures d'écran sont énormes et se résument mal.
4. **Palier 1 : résumé par Apple Intelligence,** rapide et sur l'appareil.
5. **Palier 2 : élagage agressif,** qui condense les messages intermédiaires en un résumé.

Un commentaire résume la philosophie : la compaction structurelle « est un mécanisme de sécurité, pas une fonctionnalité ». Elle s'exécute même si vous désactivez Token Compression. Seul le palier Apple Intelligence respecte cette option.

Après la compaction, le modèle récupère ce qui lui manquerait le plus : les critères d'objectif encore ouverts, la checklist du plan actif et le contenu actuel de jusqu'à cinq fichiers qu'il a modifiés pendant la tâche (environ 10K tokens au total). Le cache de déduplication des lectures est également réinitialisé, de sorte qu'il est de nouveau possible de relire un fichier.

Enfin, il y a un **disjoncteur**. Après trois compactions consécutives qui ne parviennent pas à réduire la transcription, la boucle cesse d'essayer. Mais elle n'abandonne pas définitivement : dès que la transcription a encore grossi de 25% par rapport à la dernière tentative ratée, elle réessaie.

## Les bugs : trois chemins vers 16K

Chaque correctif du 28 septembre aboutissait au même nombre. Une fenêtre de repli de 32K donne `min(16K, 32K − 8K) = 16K`. Pour un modèle de plus de 200K, compacter à 16K revient à résumer presque en permanence et à oublier des fichiers que le modèle vient de lire.

### 1. Le modèle de repli empruntait la mauvaise fenêtre

Agent! prend en charge une chaîne de repli. Si un fournisseur renvoie une erreur 429, dépasse le délai d'attente ou disparaît du réseau, la tâche se poursuit avec le fournisseur configuré suivant. Les onglets peuvent aussi imposer leur propre modèle. Mais `contextWindow(for:)` recherchait la fenêtre du modèle *sélectionné globalement* pour le fournisseur, et non celle du modèle réellement en cours d'exécution. Pour un modèle de repli sans entrée dédiée, elle retombait sur la taille statique de 32K.

Le correctif ajoute le modèle à la recherche :

```swift
func contextWindow(for provider: APIProvider, model: String? = nil) -> Int
```

Chaque point d'appel transmet désormais le modèle utilisé : la boucle principale, les tâches d'onglet, le chemin de repli et les sous-agents.

### 2. Ollama oubliait ce qu'il avait appris

Les serveurs locaux communiquent leur véritable fenêtre par modèle de façon asynchrone : Ollama via `/api/show`, LM Studio via `/api/v0/models` et vLLM via `/v1/models`. C'est pourquoi la boucle appelle `refreshThreshold` à chaque itération après la première. Une récupération qui arrive après le démarrage de la tâche est donc tout de même prise en compte.

Sur Ollama, en revanche, les fenêtres récupérées n'étaient pas conservées, si bien que la compaction retombait sans cesse sur 16K par défaut. Le correctif enregistre les fenêtres de contexte récupérées et les interroge au démarrage de la tâche lorsque la fenêtre est inconnue. Il est arrivé accompagné d'une nouvelle suite de tests, `OllamaContextWindowTests.swift`.

### 3. Un budget de sortie généreux dévorait le budget d'entrée

Celui-ci est subtil. Codex annonce une fenêtre de 272K pour son modèle GPT-6 Astra. Un utilisateur règle **Max Output Tokens** sur 256K. L'ancien code réservait l'intégralité du budget de sortie :

```text
272K − 256K = 16K   →   threshold = min(128K, 16K) = 16K
```

Le nouveau code réserve au plus la moitié de la fenêtre à la sortie :

```swift
let reservedOutput = maxTokens > 0 ? min(maxTokens, contextWindow / 2) : 8_192
```

Le même cas donne désormais `min(128K, 272K − 136K) = 128K`. Le plafond en pourcentage utilise toujours la fenêtre plafonnée, mais la vérification de la place disponible pour la sortie utilise la fenêtre *réelle*. Sinon, le budget de sortie par défaut de 500K de Claude sur une fenêtre de 1M rendrait `window − maxTokens` négatif et ramènerait le seuil au plancher de 2K.

## Pourquoi c'est important pour vous

Si vous lancez de longues tâches, en particulier des sessions de code nocturnes, avec des fournisseurs de repli ou des modèles locaux, celles-ci devraient désormais conserver beaucoup plus de contexte de travail. Cela signifie moins de boucles du type « je dois relire ce fichier », moins de détails perdus et moins de tokens dépensés en résumés. Ces correctifs ont été publiés le 28 septembre avec la version 1.1.77 (build 277), release candidate 6, en même temps que la détection multi-fournisseurs des erreurs de dépassement de contexte et de `max_tokens`.

La leçon vaut pour tous ceux qui conçoivent des agents : **dimensionnez votre mémoire d'après le modèle réellement en cours d'exécution**, fiez-vous aux décomptes de tokens du fournisseur plutôt qu'à vos propres estimations, et plafonnez chaque budget pour qu'aucun réglage ne puisse priver les autres de ressources.
