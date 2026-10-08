---
title: Sept langues, une porte
title_html: Sept langues, <i>une porte</i>
kicker: Une raison d'être avant d'être un pont
lede: Une solution a des couches, et chaque couche a un langage qui y excelle. Softanza en a choisi sept, et un qui les orchestre. Cette page dit pourquoi chacun a été choisi, comment fonctionne la porte vers eux, et ce que son propre registre ne peut pas encore dire.
description: La porte polyglotte de Softanza : pourquoi sept langages ont été choisis pour sept couches d'une solution, comment le code étranger est exécuté et collé, la différence entre une facette de Haro et une porte vers un environnement d'exécution, et l'état honnête de la porte.
---

## La raison d'être {#why}

La porte n'a jamais été une façon d'exécuter n'importe quoi. C'est une position : une solution a des couches, chaque couche a un langage qui y excelle, sept ont été choisis et un orchestre, et un programmeur de n'importe lequel des sept entre par la couche qu'il connaît.

<ol class="steps">
<li value="1"><b>Performance système : C.</b> Opérations bas niveau et algorithmes critiques en performance.</li>
<li value="2"><b>Systèmes événementiels : NodeJS.</b> Traitement asynchrone, flux en temps réel, orchestration d'API.</li>
<li value="3"><b>Calcul scientifique : Julia.</b> Modélisation mathématique et simulation numérique.</li>
<li value="4"><b>Analyse statistique : R.</b> Transformation de données, modélisation statistique, tracés.</li>
<li value="5"><b>Raisonnement logique : SWI-Prolog.</b> Systèmes à règles, représentation de connaissances, retour arrière.</li>
<li value="6"><b>Apprentissage automatique : Python.</b> Entraînement de modèles et écosystème de la science des données.</li>
<li value="7"><b>Raisonnement d'IA : le modèle.</b> Compréhension du langage naturel et synthèse de connaissances, comme une faculté et jamais comme la définition de l'esprit.</li>
<li value="8"><b>Intégration de la solution : le langage propre de Softanza.</b> Orchestration de la logique métier et transformation de données entre domaines.</li>
</ol>

L'ennemi qu'elle nomme est la friction d'orchestration : des développeurs qui passent une grande part de leur effort sur la plomberie entre langages. La réponse pour l'âge agentique n'est ni de forcer un développeur à maîtriser chaque domaine, ni de s'en remettre à du code généré pour lui, mais de façonner des abstractions qui exposent la puissance de chaque domaine par de simples fonctions.

## Deux portes {#doors}

<div class="cards">
<div class="card"><h3>Exécuter le code étranger là où il vit</h3><p>Le code est écrit dans un fichier, l'environnement d'exécution est lancé comme un processus, et le résultat est relu et converti. Les verbes sont : poser le code, l'exécuter, lire le résultat, lire la durée du dernier appel, et lire la trace des appels. Les environnements d'exécution sont trouvés par des chemins de la configuration.</p></div>
<div class="card"><h3>Coller le code étranger là où vous êtes</h3><p>Trouver une solution sur internet dans un autre langage, coller son code, et faire de petits changements. Des adaptateurs existent pour C, C#, JavaScript, Perl, PHP, Python et SQL.</p></div>
</div>

## Une facette et une porte sont deux choses {#facet}

Deux choses porteront le mot langage, et il ne faut pas les confondre. Une <b>facette</b> de Haro est une surface : une grammaire, jugée par un juge, portée dans une autre syntaxe, si bien qu'un programmeur écrit Softanza dans une syntaxe qu'il connaît déjà. Une <b>porte</b> est un environnement d'exécution : du vrai Python avec ses bibliothèques, du vrai R, du vrai Prolog, atteint depuis la solution et rendant son résultat dans le monde. La facette amène le programmeur. La porte amène l'écosystème. Elles se rencontrent dans la même personne.

<p class="proof"><b>nommé</b> Les facettes prévues de Haro, selon la déclaration de l'auteur du 2026-10-07, sont sa face actuelle aujourd'hui et, prévus, Python et JavaScript. La charte du langage ne les nomme pas encore, de sorte que cette page consigne le plan comme celui de l'auteur et pas comme une spécification.</p>

## L'état honnête {#state}

<p class="proof"><b>en construction</b> La porte est fondée sur des processus aujourd'hui : elle marche en lançant des processus et par des fichiers. Un pont dans le moteur, qui gérerait la conversion des types et les processus, est prévu, et sa liste de langages (cinq) ne correspond pas à celle de la raison d'être (huit). La porte compte cinquante-huit fichiers de garde, avec un script de lancement par langage. La dernière exécution enregistrée montre trente-huit échecs et aucune réussite, et plusieurs de leurs promesses ne peuvent pas coïncider par construction, parce qu'elles nomment un fichier temporaire au hasard ou une durée. Le registre d'exécution ne dit donc pas si la porte marche, et cette page n'exécute rien : elle ne montrera pas une exécution que ses propres gardes ne peuvent pas confirmer.</p>

La performance de la porte a été confrontée au domaine dans un article de la bibliothèque, qui publie les pertes de l'hôte : trier un million de nombres a pris bien plus longtemps par l'hôte qu'en Python. Cette mesure précède l'environnement d'exécution actuel et doit être refaite, et une perte qui subsiste sera publiée telle qu'elle subsiste.

<p class="proof">Sources : les articles <a href="narrations/stzexcis-polyglot-programming-in-ring.html">la programmation polyglotte</a>, <a href="narrations/stzexterlib-domain-driven-polyglot-programming.html">la programmation polyglotte pilotée par le domaine</a> et <a href="narrations/stzexcis-performance-battle.html">la bataille de performance</a>, dont le code ne s'exécute pour l'essentiel pas dans l'exécuteur de ce site faute des environnements d'exécution. Le registre a été lu dans les fichiers de la bibliothèque par une évaluation extérieure le 2026-10-07 ; rien n'a été exécuté pour cette page.</p>
