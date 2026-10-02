---
title: Démarrer
title_html: <i>Démarrer</i>
kicker: En une heure
lede: Un dépôt public, une installation en deux commandes, un premier programme, le lecteur du cours comme page de ce site. Chaque commande de cette page a été exécutée le soir de la publication.
description: Comment démarrer avec Softanza : le dépôt GitHub, l'installation, le premier programme, la première narration, le lecteur du cours, et où écrire.
---

## Le dépôt {#repository}

Tout est au même endroit : la fondation, son moteur, ses gardes, ses narrations et son cours.

<div class="cards">
<div class="card"><h3>github.com/mayouni/stzlib</h3><p>Public sous licence MIT depuis le 12 mars 2022. Les tickets, les avis de sécurité et tout l'historique y sont.</p><p class="proof"><a href="https://github.com/mayouni/stzlib">github.com/mayouni/stzlib</a></p></div>
</div>

## Installer {#install}

Le moteur Zig est livré en bibliothèques compilées pour Windows et se construit pour Linux et macOS depuis la source ; l'exécutant de la plateforme est décrit dans le dépôt. Il n'y a rien à installer au sens d'un installateur : un dossier, copié.

<pre>git clone https://github.com/mayouni/stzlib.git
cd stzlib/libraries/stzlib</pre>

Un script placé dans le dossier <code>libraries/stzlib</code> charge la bibliothèque par une ligne ; l'exécutant qui le lance, et sa version, sont ceux que le dépôt indique.

## Le premier programme {#first}

<div class="run"><div><div class="lbl">premier</div><pre>o1 = new stzList([ "A", "", "B", "", "", "C" ])
? o1.ContainsEmptyStrings()

? Q("Softanza").Boxed()</pre></div><div class="out"><div class="lbl">Sortie</div><pre>1
┌──────────┐
│ Softanza │
└──────────┘</pre></div></div>
<p class="ran">exécuté le 2026-10-01 à 00:45 depuis <code>libraries/stzlib</code>, Softanza au commit <a href="https://github.com/mayouni/stzlib/commit/0e72e2e2c">0e72e2e2c</a></p>

## La première narration {#narration}

Une narration est un document qui raconte une partie de la bibliothèque comme une histoire, en code écrit pour être exécuté au fil de la lecture. Commencez par <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/narrations/stz-mental-mode-narration.md">le modèle mental</a>, puis <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/narrations/stz-agents-that-cannot-hurt-you-narration.md">les agents qui ne peuvent pas vous nuire</a> ; les deux s'ouvrent sur GitHub. Pour voir une narration jugée bloc par bloc, ouvrez <a href="narrations/stz-repetition-with-elegance-narration.html">Repetition with Elegance</a>, exécutée pour ce site : ses six blocs affichent ce qu'ils promettent. Les 134 sont listées sous Apprendre, dans Narrations.

## Le lecteur du cours {#reader}

Le lecteur est une page de ce site : <a href="../reader.html">ouvrir le lecteur</a>. Il a été construit depuis la bibliothèque le 2026-09-30, et la page Apprendre dit comment apprendre avec lui, étape par étape. Pour le reconstruire vous-même, depuis votre copie du dépôt :

<pre>cd libraries/stzlib/base/education/tools
# lancer build_reader avec l'exécutant du dépôt :
#   build_reader reader.html</pre>

<p class="ran">exécuté le 2026-09-30 à 23:02 : « 15 of 15 chapters, 3 of 3 world pages », chaque édition verte, en 3 minutes 22 secondes</p>

Et pour jouer la démonstration de quinze minutes pour décideurs, dont la dernière ligne doit dire « DEMO: 20 proved, 0 not proved » :

<pre>cd libraries/stzlib/base/education/demo
# lancer demo avec l'exécutant du dépôt :
#   demo rehearsal</pre>

<p class="ran">exécuté le 2026-09-30 à 23:10, en 49 secondes, 20 preuves sur 20</p>

## Écrire {#write}

Les questions, les rapports de défaut et les propositions passent par <a href="https://github.com/mayouni/stzlib/issues">les tickets du dépôt GitHub</a>. Une faille de sécurité se signale en privé par les avis de sécurité du dépôt, comme le dit son <a href="https://github.com/mayouni/stzlib/blob/main/SECURITY.md">SECURITY.md</a>. Une édition du cours dans votre langue commence par un dossier de chapitres en texte brut : la page Apprendre dit comment le tribunal du cours la jugera. Pour l'édition entreprise, écrivez par les mêmes tickets : la page Offre dit ce qu'elle contient.

## Vérifier ce site hors ligne {#offline}

Avant une présentation sans réseau, ouvrez <a href="../deck-check.html">deck-check.html</a> depuis le dossier du site : la page charge chaque ressource dont la présentation a besoin et dit laquelle manque.
