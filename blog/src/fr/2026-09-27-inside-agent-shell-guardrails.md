---
title: Avant que le modèle n'ait voix au chapitre : dans les coulisses des garde-fous shell d'Agent!
description: Comment ShellSafetyService, la seconde vérification côté daemon et le second avis de Jev empêchent un agent d'IA d'effacer votre Mac, en parcourant le vrai code Swift.
tags: Sécurité, Fonctionnement interne
---
Cette semaine, TechRadar a rapporté qu'un agent de programmation avait supprimé environ 48,000 fichiers en un rien de temps, avant de présenter ses excuses. Les excuses n'ont rien changé. Les fichiers avaient disparu.

Agent! peut exécuter des commandes shell en votre nom via un Launch Agent, et en tant que **root** via un Launch Daemon. C'est ce qui le rend utile : il peut flasher une carte SD, corriger des permissions ou nettoyer un dossier de build. Mais cela signifie aussi que « le modèle fera sans doute attention » ne constitue pas un modèle de sécurité. Agent! ne demande donc pas au modèle de faire attention. Il vérifie chaque commande dans le code, avant toute exécution, en trois couches.

## Couche 1 : un garde-fou codé en dur que le modèle ne peut pas contourner à coups d'arguments

`ShellSafetyService` est un simple `enum` Swift dans `Agent/Services/ShellSafetyService.swift`. Le commentaire de documentation en tête de fichier donne le ton : il s'exécute *avant chaque surface d'exécution* et rejette les commandes catastrophiques *sans jamais les envoyer*. Les prompts système y sont désignés pour ce qu'ils sont : des filets de sécurité, pas la couche qui fait respecter les règles.

Le point d'entrée reçoit la commande, le contexte dans lequel elle s'exécutera et le dossier de projet de l'onglet :

```swift
static func check(_ command: String,
                  context: Context = .userAgent,
                  projectFolder: String = "") -> Verdict
```

Un `Verdict` se compose de `allowed`, d'une `reason` lisible par un humain et d'un court identifiant `rule` destiné au journal d'audit. La raison est rédigée pour le modèle : elle lui est renvoyée comme résultat de l'outil, afin que le LLM comprenne *pourquoi* la commande a été refusée au lieu de simplement réessayer.

### Il lit les commandes composées comme le fait un shell

Un filtre naïf examine le début de la chaîne. Les attaquants et les modèles égarés ne jouent pas le jeu. `check` découpe la commande sur `;`, `&&`, `||`, `|` et les retours à la ligne, puis vérifie **chaque segment**. Ainsi, `ls; rm -rf /` est bloqué, même si la première moitié est inoffensive.

Il existe une exception délibérée à cet ordre. La fork bomb classique, `:(){ :|:& };:`, *repose* sur `;` et `|`, précisément les caractères que le découpage sépare. La détection de fork bomb s'exécute donc sur la commande entière, avant le découpage.

### Il fait tomber les déguisements

Avant de rechercher `rm`, une fonction utilitaire appelée `stripPrefixWrappers` retire les enveloppes qui ne changent rien à ce que fait une commande : `sudo`, `exec`, `command`, `builtin`, `eval` et `doas`. Elle supprime aussi les affectations de variables d'environnement placées en tête, comme `FOO=bar`. Résultat : `sudo rm -rf ~` et `FOO=1 exec rm -rf ~` tombent sous la même règle que la commande nue.

Les options sont en outre analysées plutôt que comparées à des motifs. `-rf`, `-fr`, `-Rf`, `-r -f` et `--recursive --force` sont tous pris en compte, car l'analyseur cherche un `r` et un `f` dans n'importe quel groupe d'options courtes, en plus des formes longues.

### Ce qu'il refuse

Voici les identifiants de règles présents dans le code source :

| Règle | Ce qu'elle bloque |
|---|---|
| `rm.catastrophic` | `rm -rf` sur `/`, un joker seul comme `*` ou `./*`, ou votre dossier personnel, quelle que soit sa graphie (`~`, `~/*`, `$HOME`, `${HOME}/*` ou le chemin littéral du dossier personnel) |
| `rm.no-preserve-root` | `--no-preserve-root`, le contournement explicite de la protection de `/` |
| `rm.project-folder` | La suppression récursive du dossier de projet dans lequel travaille l'agent, ou de tout son contenu via un joker. Supprimer un sous-dossier nommé reste autorisé. |
| `rm.dangerous-target` | Les autres cibles `rm` dangereuses sur le chemin de niveau utilisateur |
| `fork-bomb` | Les bombes de processus auto-réplicantes |
| `mv.to-devnull` | La « suppression » de fichiers en les déplaçant vers `/dev/null` |
| `find.delete-broad-root` | `find … -delete` à partir d'une racine trop large |
| `perms.recursive-on-root` | Les modifications récursives de permissions sur des chemins de niveau racine |

La règle du dossier de projet mérite qu'on s'y arrête. C'est celle qui correspond le plus directement à l'incident évoqué plus haut : un agent ne devrait jamais effacer le projet même sur lequel on lui a demandé de travailler, quelle que soit la formulation de la demande.

### Root est traité différemment, et c'est voulu

On pourrait s'attendre à ce que le daemon root ait les règles *les plus strictes*. Il a les plus restreintes. Le commentaire explique pourquoi : le daemon existe pour effectuer des tâches au niveau système, comme le clonage de disques ou `mkfs`, et il « ne devrait pas nous mettre des bâtons dans les roues ». Dans le contexte `.rootDaemon`, `check` passe donc directement à `checkCatastrophicRm`, qui ne bloque que les trois motifs irrécupérables (`/`, les jokers seuls et le dossier personnel), plus `--no-preserve-root` et l'effacement du dossier de projet. Tout le reste relève de la décision de l'opérateur.

C'est un choix de conception qui mérite d'être imité. Un garde-fou qui bloque un travail d'administration légitime finit désactivé. Un garde-fou qui ne bloque que les erreurs irrécupérables reste en place.

## Couche 2 : le daemon vérifie à nouveau

L'app exécute `ShellSafetyService.check` avant d'envoyer quoi que ce soit. Les helpers ne se contentent pas de lui faire confiance. Dans `Shared/DaemonCore.swift`, juste après avoir écrit l'entrée du journal d'audit, le daemon exécute **la même vérification** de son côté :

```swift
// Defense-in-depth: the app already runs this same check before
// dispatching, but any same-team-signed client can reach the mach
// service directly.
let verdict = ShellSafetyService.check(
    script,
    context: auditCategory == .launchDaemon ? .rootDaemon : .userAgent,
    projectFolder: workingDirectory
)
```

Une commande bloquée est journalisée comme refusée avec son identifiant de règle et reçoit le code de sortie 126. Elle n'atteint jamais `/bin/zsh`. C'est important, car les listeners XPC acceptent tout client signé par la même équipe. Si un autre programme signé par cette équipe se connecte directement au service mach, il se heurte malgré tout au garde-fou.

## Couche 3 : Jev, un second avis pour ce qui échappe aux motifs

Les règles fondées sur des motifs sont précises, mais elles ne connaissent que les motifs que vous avez écrits. Bien des commandes destructrices ne ressemblent pas à `rm -rf /` : un `truncate` sur le mauvais fichier, un `DROP` SQL envoyé via un pipe à une CLI, un `dd` dans le mauvais sens.

C'est le rôle de **Jev**, une couche consultative optionnelle définie dans `JevAdvisor.swift`. Chaque commande qui a déjà *passé* `ShellSafetyService` est soumise à Jev, qui estime la probabilité qu'elle détruise des données de manière irréversible. Au-delà de votre seuil, Agent! refuse avec un message clair :

```text
Refused: Jev rated this command 85% likely to irreversibly destroy data.
Command: …
Narrow the target or run it yourself if this is intentional.
```

Quelques détails montrent avec quel soin son périmètre a été défini :

- **Il complète, sans jamais remplacer.** Le commentaire du code est explicite : `ShellSafetyService` est la couche qui fait respecter les règles, et Jev ne rattrape que ce qui échappe aux règles fondées sur des motifs. C'est pourquoi le seuil est volontairement élevé. Il est de **70%** par défaut, et vous pouvez l'ajuster de 0 à 100% par paliers de 10% dans les Réglages.
- **En cas de panne, il laisse passer, mais le signale haut et fort.** Pas de clé, option désactivée ou panne réseau : le résultat est « pas d'avis », si bien qu'un service capricieux ne peut jamais bloquer votre tâche. L'échec est tout de même journalisé (`⚠️ Jev check failed, command allowed`), de sorte qu'une clé expirée n'est jamais confondue avec « Jev juge la commande sûre ».
- **Annuler, c'est annuler.** Si vous arrêtez une tâche pendant que Jev réfléchit, la commande ne s'exécute pas.
- **Chaque verdict est visible.** Chaque vérification journalise le pourcentage de risque, l'autorisation ou le refus, le modèle qui a répondu et le nombre de tokens.

## Testé, pas présumé

`AgentTests/ShellSafetyServiceTests.swift` contient 30 tests consacrés au garde-fou. Et comme chaque commande des helpers est inscrite dans le journal d'audit avant son exécution, vous pouvez toujours reconstituer ce que l'agent a tenté de faire, y compris ce qu'il n'a pas été autorisé à faire.

## À retenir pour qui conçoit des agents

1. **Faites respecter les règles dans le code, pas dans le prompt.** Un prompt n'est qu'une suggestion. Un `enum` Swift, non.
2. **Analysez comme le shell analyse.** Découpez les commandes composées, retirez les enveloppes et normalisez les options.
3. **Vérifiez à nouveau à la frontière privilégiée.** Ne partez pas du principe que votre propre client sera le seul appelant.
4. **Bloquez l'irrécupérable, pas l'inhabituel.** Les règles ciblées perdurent ; celles qui font trop de bruit finissent désactivées.
5. **Ajoutez du discernement par-dessus, et faites en sorte que ses échecs soient visibles.** Un second avis n'a de valeur que si vous pouvez savoir quand il n'a pas répondu.

Tout cela est ouvert à tous sur [GitHub](https://github.com/AgentiLoop/Agent). Lisez le code, cherchez-lui des failles et ouvrez une issue si vous trouvez une commande qui aurait dû être bloquée.
