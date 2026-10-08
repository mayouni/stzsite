---
title: Naturel, et exécutable
title_html: Naturel, <i>et exécutable</i>
kicker: Un paradigme
lede: Une phrase dans votre langue s'exécute, sans modèle, parce que chacun de ses mots est dans un dictionnaire que la bibliothèque possède. Ce que la bibliothèque ne connaît pas, elle le refuse, et dit pourquoi.
description: Le langage naturel exécutable dans Softanza : des phrases en anglais, français, arabe, haoussa et turc qui s'exécutent sans modèle, un dictionnaire que la bibliothèque possède, des refus motivés, et une langue ajoutée comme un bloc de données.
---

## Un programme, trois langues {#runs}

L'idée est la plus ancienne de Softanza : la pensée peut s'écrire en phrase, et la phrase peut s'exécuter. Voici un programme écrit comme un paragraphe anglais, exécuté tel quel. Un mot hors du dictionnaire n'est pas deviné ; la bibliothèque lit les mots qu'elle possède et agit sur eux.

<!--SHOWCASE:natural:1,2,3-->

Le programme haoussa a d'autres mots et le même sens : chaque langue est un ensemble de mots rattachés aux mêmes entrées d'un seul dictionnaire, de sorte qu'une phrase dans n'importe laquelle aboutit à la même opération. Les phrases française et arabe ne traduisent pas l'anglais mot à mot, elles suivent leur propre grammaire, et la turque met son verbe à la fin. Chaque programme redit, dans sa langue, ce qu'il a compris.

## Qui analyse {#parses}

Il y a deux sens, et la différence est celle de qui fait la lecture.

<div class="cards">
<div class="card"><h3>La machine analyse</h3><p><code>Naturally()</code> prend un paragraphe. La bibliothèque le lit contre son dictionnaire et doit refuser ce dont elle ne peut prouver qu'elle l'a compris. L'ambiguïté est refusée à voix haute. Le public, ce sont les experts d'un domaine et les agents.</p></div>
<div class="card"><h3>Le programmeur analyse</h3><p>Une chaîne presque naturelle est du code qui se lit comme une phrase. L'humain est l'analyseur, et la chaîne est la phrase : une chaîne qui s'exécute sans se lire comme une phrase grammaticale est une erreur. Le public, ce sont les programmeurs.</p></div>
</div>

<!--SHOWCASE:natural:7-->

## Ce qu'elle ne connaît pas, elle le refuse {#refuses}

Un système qui répond à tout est un système dont on ne peut pas se fier à la réponse. La couche naturelle est un langage fermé : un mot qu'elle ne connaît pas est un littéral et jamais une supposition, un mot mal écrit est nommé avec le mot le plus proche qu'elle connaît, et un modèle de phrase dont un trou reste vide refuse de s'exécuter.

<!--SHOWCASE:natural:4,5-->

<p class="way"><span>La manière Softanza</span> Une phrase dans votre langue s'exécute parce que chacun de ses mots est admis, et le refus vient avec sa raison. Le naturel est à la porte ; l'exécution se fait dans un langage fermé que l'on peut juger.</p>

## Les langues sont des données {#languages}

Un paquet de langue est un bloc de données rattaché aux mêmes sens que l'anglais. Cinq paquets sont livrés : anglais, haoussa en écriture latine, français, arabe et turc. En ajouter un ne demande ni code ni chargement.

<!--SHOWCASE:natural:6-->

Le haoussa en écriture ajami est nommé dans la bibliothèque et pas livré ; le zarma et le peul ne sont pas encore là. Ce sont les prochains paquets à écrire, et un paquet est une donnée.

## Cinq faces {#faces}

<div class="cards">
<div class="card"><h3>Déterminisme et souveraineté</h3><p>La couche naturelle n'appelle aucun modèle et ne demande aucune clé, et la même phrase donne la même réponse n'importe quel jour. C'est la condition d'une banque ou d'un ministère, pas une option. Qu'aucune connexion réseau ne s'ouvre pendant une exécution naturelle n'est pas encore mesuré par un test dédié.</p></div>
<div class="card"><h3>Responsabilité</h3><p>Chaque phrase peut dire ce qu'elle a compris, ce qu'elle a refusé, et pourquoi. C'est ce qui la sépare du code généré par un modèle et d'un langage jouet pour des commandes.</p></div>
<div class="card"><h3>Langues en données</h3><p>Une langue est un bloc, ajouté à l'exécution. Un locuteur du haoussa ou de l'arabe écrit à la même bibliothèque qu'un locuteur de l'anglais.</p></div>
<div class="card"><h3>Deux sens, une discipline</h3><p>La machine qui analyse et l'humain qui analyse partagent un seul lexique : la grammaire des formes de fonction, lue comme un vocabulaire.</p></div>
<div class="card"><h3>La porte de l'agent <b>(conçu)</b></h3><p>Un modèle peut proposer ; une grammaire fermée juge. Tenir un modèle à la grammaire du lexique, pour qu'il ne puisse produire que des phrases que la couche exécute, est conçu et pas construit.</p></div>
</div>

## D'où elle vient {#history}

- **2020.** La première diapositive du premier exposé donne la raison d'être : « exprimer la pensée dans un langage naturel exécutable ».
- **Le tournant.** L'article de l'auteur sur la raison d'être de la couche naturelle pose la thèse : une phrase se modélise comme du code, sans traitement du langage et sans apprentissage automatique, à vitesse native, déterministe, le programmeur gardant la main.
- **Les trois âges.** La couche a été construite en trois temps, chacun contre un mur : l'écart entre l'intention d'une personne et son exécution.
- **2026-07-10.** La revue de la bibliothèque a constaté que sur quinze exemples canoniques exécutés tels qu'écrits, quatre s'exécutaient comme les articles le disaient. La surface s'était dégradée parce qu'aucun test ne l'avait jamais verrouillée. Elle a été rénovée ce jour-là et elle est tenue depuis par des gardes-scénario.

Les trois articles qui la racontent sont publiés ici avec leur code exécuté : <a href="narrations/stznatural-narration.html">stzNatural</a>, <a href="narrations/stznatural-vs-ring-naturallib.html">stzNatural face à l'ancienne bibliothèque naturelle</a> et <a href="narrations/stz-near-natural-language-programming.html">la programmation en langage presque naturel</a>. Plusieurs de leurs blocs ne s'exécutent plus tels qu'écrits, et leurs pages le disent.

## Limites {#limits}

<p class="proof"><b>en construction</b> Le vocabulaire est borné par les paquets, et chaque paquet couvre une partie de ce que la bibliothèque sait faire. Un programme est un objet par bloc. L'ambiguïté est refusée et pas résolue. La surface s'est dégradée une fois et elle est gardée maintenant, ce qui est une promesse sur l'avenir et pas sur le passé. Les blocs d'articles qui ne s'exécutent pas tels qu'écrits ne sont pas encore épinglés comme exemples.</p>

<p class="proof">Sources : les gardes-scénario <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/natural/multilingual_pack_narrated.ring">multilingual_pack_narrated.ring</a>, <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/natural/nnl_narrated.ring">nnl_narrated.ring</a> et <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/natural/literate_templates_narrated.ring">literate_templates_narrated.ring</a> ; le code de la couche est dans <a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/base/natural">base/natural</a>.</p>
