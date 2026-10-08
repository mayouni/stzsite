---
title: Pour les agents qui codent
title_html: Des juges pour <i>les agents qui codent</i>
kicker: Softanza comme boîte à outils des agents qui écrivent du code
lede: Un agent qui écrit du code a déjà de bonnes mains : il lit, cherche, modifie et lance un shell. Ce qui lui manque, c'est un moyen de connaître une API sur laquelle il n'a jamais été entraîné, de vérifier que ce qu'il a écrit tient ses promesses, et de montrer un changement avant qu'il n'arrive. Softanza a ces trois choses sur un seul moteur. Cette page les montre en marche, dit ce qu'un agent peut atteindre aujourd'hui, et décrit la porte qui lui ouvrira le reste.
description: Softanza comme boîte à outils des agents qui codent : une API qui répond, un juge pour le code et les promesses, des changements montrés comme des plans, un moteur pour calculer ; et la commande stz qui les ouvrira à Claude Code et aux autres agents.
---

## Les mains et les juges {#judges}

Les agents qui codent, comme Claude Code, Codex ou Cursor, viennent avec leurs propres outils : ils lisent des fichiers, y cherchent, les modifient et lancent des commandes. De nouvelles façons de trouver du code les aident peu ; ils reviennent toujours à la simple recherche. Ce qu'ils ne savent pas faire seuls, c'est connaître une API inconnue sans deviner, juger leur travail face à des règles et à des promesses, et présenter un changement comme une intention qu'une personne relit avant que rien ne bouge.

<p class="way"><span>La manière Softanza</span> Softanza ne concurrence pas les outils de l'agent pour trouver du code. Elle fournit les juges : quelque chose qui connaît l'API, quelque chose qui vérifie l'affirmation, et quelque chose qui montre le changement avant qu'il n'arrive. L'agent garde ses mains.</p>

<figure class="diagram"><img src="../assets/img/diagrams/codingagents-fr.png" alt="Trois boîtes reliées par des flèches. L'agent qui code, les mains : lire et chercher, modifier des fichiers, lancer un shell ; Claude Code, Codex, Cursor et d'autres. La porte, une commande stz, décidée et dessinée en pointillé : une ligne de commande, un serveur MCP, compétence et hook, un plugin à installer. Les juges, Softanza, construits : connaître l'API, juger code et promesses, montrer le plan d'abord, calculer sur un moteur. Sous les trois : le modèle propose ; une personne valide ; chaque outil dit s'il peut agir, et refuse en disant pourquoi." width="1376" height="650"><figcaption>Les juges sont construits et s'exécutent aujourd'hui. La porte entre eux et l'agent est décidée et pas encore construite.</figcaption></figure>

## Les juges, en marche {#run}

Ils s'exécutent aujourd'hui dans la bibliothèque. Un agent peut déjà les atteindre en écrivant un court script ; la porte décrite plus bas lui permettra de les appeler comme des commandes.

<!--SHOWCASE:coding-agents-->

## Ce qu'un agent atteint aujourd'hui {#today}

- **À l'intérieur, les juges sont profonds.** La bibliothèque explique chaque méthode à partir de son propre code. Des règles maison et un vérificateur de programme entier jugent le code. Des milliers de promesses écrites et cinq cents gardes de scénario disent ce que le code doit afficher. Un changement peut être répété puis validé à travers des portes, et un schéma peut tenir les réponses d'un modèle local dans une forme.
- **De l'extérieur, peu de choses passent.** Un agent peut lancer un script, mais il ne peut pas encore appeler une commande qui répond, juge ou planifie. Un échec ne se traduit pas encore en code de sortie, aucun hook ne peut donc se fier à une réussite, et aucun fichier d'instructions n'est écrit pour les agents.
- **Cet écart est le constat.** La revue que Softanza a faite de la question a jugé la capacité profonde et la portée presque nulle. Le travail n'est pas une nouvelle machinerie ; c'est une porte.

## La porte : une commande stz {#door}

<p class="proof"><b>proposition ratifiée</b> Décidée le 2 octobre 2026. Pas encore construite. Chaque verbe ci-dessous répond depuis la bibliothèque et le moteur, jamais depuis un modèle.</p>

<div class="cards">
<div class="card"><h3>stz ask · explain · howto</h3><p>Ce que fait une méthode, ses formes, un exemple avec sa promesse, et où elle se trouve. La réponse vient d'un catalogue généré depuis le code source : elle ne peut pas inventer une méthode.</p></div>
<div class="card"><h3>stz check</h3><p>Des constats sous forme de données : la règle, le fichier, la ligne, la gravité et ce qu'il faut faire. Les règles maison de la bibliothèque, les règles du programme entier et le tribunal des langues déclarées, sous une seule forme.</p></div>
<div class="card"><h3>stz promise · guard</h3><p>Chaque affirmation écrite, ou chaque scénario d'une garde, tenu ou rompu, avec un code de sortie auquel un hook peut se fier.</p></div>
<div class="card"><h3>stz rehearse · commit</h3><p>Le changement comme un plan, sans toucher au disque ; puis sa validation à travers les portes, par quelqu'un qui a le droit de valider.</p></div>
<div class="card"><h3>stz do</h3><p>Un court programme contre le moteur, pour le travail lui-même : texte, tables, graphes, cartes, statistiques et diagrammes, en un appel et un seul binaire.</p></div>
<div class="card"><h3>stz grammar</h3><p>La grammaire de chaque langue déclarée, pour que la phrase d'un agent soit validée avant de s'exécuter, et qu'un modèle local ne puisse produire que des phrases valides.</p></div>
</div>

Chaque verbe suit les mêmes lois. Il répond sous forme de données quand il ne parle pas à une personne. Il sort avec 0 en cas de succès, 1 en cas de constats et 2 en cas de refus. Il ne contient aucun modèle : l'agent apporte le modèle, Softanza apporte le jugement. Chaque refus dit où, quoi, pourquoi et que faire. Et les verbes restent les mêmes, quelle que soit la langue dans laquelle la plateforme elle-même est écrite.

## Cinq façons d'entrer {#ways}

- **Une ligne de commande.** Tout agent qui dispose d'un shell peut s'en servir, et ses réponses se composent avec des tubes.
- **Un serveur MCP.** Les mêmes verbes comme outils typés, pour les clients sans shell, tenus dans un seul processus déjà chaud, en lecture seule d'abord. La couche applicative de la plateforme sert déjà ainsi un projet déclaré aux outils d'IA, en lecture seule et sous journal, et s'inscrit elle-même auprès des outils installés sur la machine.
- **Une compétence.** Une page que l'agent ne charge que lorsqu'il en a besoin, et qui lui apprend quel verbe employer et quand.
- **Un hook.** Une vérification facultative après chaque modification, pour que l'agent corrige une erreur dans le même tour.
- **Un plugin.** Une seule installation pour Claude Code, qui réunit la compétence, le hook et le serveur. Les autres agents lisent un fichier AGENTS.md et utilisent le même serveur.

## Des outils qui savent s'ils peuvent agir {#governed}

Chaque outil porte l'une des sortes de capacité de la plateforme : calcul, perception, inférence ou effet. Le modèle de l'agent est traité pour ce qu'il est, un acteur qui peut inférer et proposer, mais pas agir. Un outil qui calcule ou qui lit répond donc aussitôt. Un outil qui agirait rend un plan avec un identifiant et ne change rien. Seule une personne qui confirme à l'invite de permission de l'agent, ou un acteur gouverné, valide ce plan, et chaque appel est consigné.

<p class="way"><span>La manière Softanza</span> La différence avec un serveur d'outils ordinaire n'est pas d'avoir plus d'outils. C'est que chaque outil sait s'il peut agir, et refuse en disant pourquoi quand il ne le peut pas.</p>

## L'ordre du travail {#order}

1. Rendre l'échec visible : chaque exécuteur échoue avec un code de sortie quand une promesse est rompue.
2. Ouvrir la porte : un fichier AGENTS.md et une compétence qui enseignent les verbes.
3. Les deux verbes à la valeur la plus nette : `stz check` et `stz ask`.
4. Les verbes que personne d'autre n'offre : `stz promise`, `stz rehearse` et `stz grammar`.
5. Le serveur MCP, généré depuis les verbes, puis le plugin.
6. Mesurer vingt tâches réelles avec et sans les verbes. Ce site n'annoncera aucun gain avant cette mesure.

<p class="proof">Décidé le 2 octobre 2026 par délégation de l'auteur, à partir de la revue que Softanza a faite des outils pour agents. Les juges ci-dessus se sont exécutés dans la bibliothèque au commit 0e72e2e2c.</p>
