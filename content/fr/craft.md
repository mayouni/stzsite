---
title: Comment Softanza s'écrit
title_html: Comment Softanza <i>s'écrit</i>
kicker: Le métier du code Softanza
lede: Softanza s'écrit de sorte qu'un nom dise ce que fait un appel, qu'une condition voyage dans un argument, qu'une boucle laisse place à une métaphore, et que la bibliothèque puisse s'expliquer elle-même. Ce sont des conventions tenues sur des milliers de méthodes. Cette page montre chacune en marche.
description: Comment s'écrit le code Softanza : la grammaire de ses noms, les petites langues dans ses arguments, les quatre métaphores qui remplacent les boucles, ses conventions, et une bibliothèque qui s'explique elle-même.
---

## Un nom est une phrase {#names}

Le nom d'une méthode se lit comme une courte phrase : le verbe dit ce qui se passe, et la forme du mot dit comment. `Remove()` modifie l'objet. `Removed()` rend une copie modifiée et garde l'original. `RemoveQ()` le modifie et le rend, pour que la phrase continue. Les suffixes ajoutent un sens de la même façon dans toutes les classes : un réglage de casse, une condition, des options étendues, des positions ou des sections, une position de départ.

<figure class="diagram"><img src="../assets/img/diagrams/forms-fr.png" alt="À gauche, mise en avant : les formes de Remove. Remove() modifie la chaîne ; Removed() rend une copie modifiée ; RemoveQ() modifie, et enchaîne ; RemoveCS() avec un réglage de casse ; RemoveW() là où une condition vaut ; RemoveXT() avec options étendues. À droite : les suffixes sont des mots. ed, une copie, l'original gardé ; Q, continuer la chaîne ; CS, sensible à la casse ; W, une condition écrite en ligne ; XT, étendu ; Z et ZZ, positions et sections ; ST, depuis une position." width="1376" height="640"><figcaption>Les huit formes de Remove dans la classe des chaînes, lues dans la référence que ce site génère depuis la bibliothèque.</figcaption></figure>

Les formes sont un système, pas une habitude : la bibliothèque lit ses propres noms avec une grammaire, et un audit liste chaque verbe auquel il manque l'une de ses trois formes principales. C'est pourquoi la classe des chaînes porte 2 117 méthodes propres et la classe des listes 1 583, et pourquoi un lecteur qui connaît un verbe connaît déjà sa famille.

<!--SHOWCASE:craft:1,2-->

- **Un verbe, jamais un nom nu.** Un nom dit ce que fait l'appel : `AddCircle()`, pas `Circle()`.
- **Des verbes calmes.** Remove, Clear, Close ; jamais Kill ni Destroy.
- **Donnée ou objet, dit par le nom.** Une forme simple rend une donnée ; la forme `Q` rend l'objet, pour qu'une chaîne d'appels ne devine jamais ce qu'elle tient.
- **Le nom d'un paramètre dit son type.** `pc` pour un texte, `pn` pour un nombre, `pa` pour une liste, `pb` pour un oui ou un non.

## De petites langues dans les arguments {#languages}

Certains arguments ne sont pas des valeurs mais des phrases dans une petite langue. Une condition comme `"{ @item > 5 }"` est compilée par le moteur et vérifiée sur chaque élément, sans jamais évaluer de code : elle reste sûre même quand elle vient d'un utilisateur ou d'un fichier. Un paramètre nommé comme `:With = "coffee"` ou `:StartingAt = 3` fait lire un appel comme une phrase. Les motifs sur les listes, les nombres, les tables et le temps suivent la même idée, et les chaînes quasi naturelles laissent une ligne de code se lire comme de l'anglais.

<!--SHOWCASE:craft:3,4,6-->

<p class="way"><span>La manière Softanza</span> Une petite langue dans un argument dit ce que l'on veut, et la bibliothèque décide comment l'obtenir. La boucle, l'indice et la variable temporaire disparaissent de la page.</p>

## Quatre métaphores au lieu des boucles {#metaphors}

Une boucle cache le geste qu'elle fait. Softanza nomme les quatre gestes, et une tâche se décompose en eux.

<div class="cards">
<div class="card"><h3>Le marcheur</h3><p>Parcourt des positions : il connaît tout son trajet avant de bouger, les pas qu'il fera, ceux qu'il sautera, et l'endroit où il se trouve. Il vit dans la couche max.</p></div>
<div class="card"><h3>Le vérificateur</h3><p>Pose des questions par oui ou par non sur les éléments : tous, l'un d'eux, aucun, là où une condition vaut.</p></div>
<div class="card"><h3>Le producteur</h3><p>Produit de nouvelles données à partir des anciennes : il filtre, transforme et réduit, et son cœur tourne dans le moteur.</p></div>
<div class="card"><h3>L'acteur</h3><p>Agit sur place : il change les éléments qu'on lui dit de changer, là où une condition vaut.</p></div>
</div>

<!--SHOWCASE:craft:5-->

## Quatorze règles d'écriture {#rules}

Tout ce qui précède est une seule grammaire. Écrite en règles, elle en compte quatorze, et une ligne de code qui les suit se lit comme la pensée qui la porte. Ce sont des lectures du code et des articles de la bibliothèque, énoncées en règles. L'exemple de chaque règle est écrit sous elle, sans être exécuté ; les exécutions qui suivent en montrent plusieurs à l'œuvre.

<!--RULES-->

<!--SHOWCASE:craft:8,9,10,11-->

<p class="way"><span>La manière Softanza</span> Les mêmes règles servent les sept étapes du modèle mental, une règle ou deux à chaque étape. <a href="way.html">La page suivante</a> met les deux côte à côte.</p>

## Conventions {#conventions}

- **Les positions commencent à 1, et 0 veut dire « absent ».** On compte à partir de un ; chaque couche aussi, moteur compris.
- **Des caractères, pas des octets.** Une longueur ou une position compte les lettres qu'une personne lit, dans toutes les écritures.
- **Le moteur d'abord.** La substance va dans le moteur, écrite une fois, et la langue au-dessus en est le visage.
- **`Q()` fait d'une valeur un objet.** Une valeur simple reste une donnée ; `Q("texte")` devient un objet chaîne et ses milliers de méthodes.
- **Trouver d'abord, puis appliquer.** Où est-ce, et que dois-je y faire : les deux mêmes étapes dans tous les domaines.
- **Les mêmes verbes pour toutes les structures.** Ce qui marche sur une chaîne marche en général sur une liste.
- **Un vrai s'affiche 1.** La console affiche une réponse vraie par 1 et une fausse par 0 : c'est pourquoi les sorties de ce site se lisent ainsi.

## Une bibliothèque qui s'explique {#selfdoc}

Chaque méthode porte, juste au-dessus de sa définition, une ligne qui dit ce qu'elle fait dans les mots de l'utilisateur, et des étiquettes facultatives : d'autres noms qu'un lecteur pourrait employer, la forme de la réponse, un exemple, les méthodes voisines. Une vraie, tirée de la classe des textes :

<pre># The overall tone/mood of the text as "positive", "negative", or "neutral".
#@ aka  mood, emotion, feeling, attitude, opinion, how positive or negative
#@ out  string: "positive" | "negative" | "neutral"
#@ eg   Q("The food was terrible.").Text().Sentiment()   #--> "negative"
#@ see  SentimentScore, IsPositive, IsNegative
def Sentiment()</pre>

Un moissonneur lit ces lignes, les titres de section et les exemples promis dans les tests. Chaque objet répond alors à `Ask()`, `HowTo()` et `ExplainMethod()` à partir d'eux, sans aucun modèle : la réponse est celle de la bibliothèque, et une méthode qui n'existe pas est refusée nommément.

<!--SHOWCASE:craft:7-->

<p class="proof"><b>en construction</b> La convention n'est encore pleinement employée que sur peu de méthodes : 106 lignes donnent d'autres mots pour une méthode, et le moissonneur ne lit pas encore les étiquettes d'exemple et de forme de réponse. La référence de ce site est générée à partir de ce qui existe.</p>

<p class="proof">Sources : les formes sont décrites dans la narration <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/narrations/stz-functions-as-linguistic-expressions.md">stz-functions-as-linguistic-expressions.md</a> ; la langue des conditions est compilée par <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/engine/src/expr.zig">engine/src/expr.zig</a> ; la convention des commentaires est fixée dans <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/design/stz-information-tagging-strategy.md">stz-information-tagging-strategy.md</a>. Nombres de méthodes lus dans la bibliothèque au commit 010743cce.</p>
