---
title: Démarrer
title_html: <i>Démarrer</i>
kicker: En une heure
lede: Un dépôt public, une installation en trois étapes, un premier programme, le lecteur du cours comme page de ce site. Chaque commande de cette page a été exécutée le soir de la publication.
description: Comment démarrer avec Softanza : le dépôt GitHub, l'installation, le premier programme, la première narration, le lecteur du cours, et où écrire.
---

<p class="proof"><b>L'exécution, en clair</b> <!--RUNTIME--></p>

## Le dépôt {#repository}

Tout est au même endroit : la fondation, son moteur, ses gardes, ses narrations et son cours.

<div class="cards">
<div class="card"><h3>github.com/mayouni/stzlib</h3><p>Public sous licence MIT depuis le 12 mars 2022. Les tickets, les avis de sécurité et tout l'historique y sont.</p><p class="proof"><a href="https://github.com/mayouni/stzlib">github.com/mayouni/stzlib</a></p></div>
</div>

## Installer {#install}

Trois étapes. Rien ne s'installe au sens d'un installateur : un dossier, copié, et l'exécutant qui le lance.

**1. Prendre le dépôt.**

<pre>git clone https://github.com/mayouni/stzlib.git
cd stzlib/libraries/stzlib</pre>

**2. Prendre l'exécutant**, version 1.27.0, celle avec laquelle ces pages ont été exécutées, sur <a href="https://ring-lang.net">ring-lang.net</a>. Lancer l'exécutant sans argument affiche sa version, ce qui montre qu'il est là. Le moteur Zig est livré en bibliothèques compilées pour Windows et se construit pour Linux et macOS depuis la source ; le dépôt dit comment.

**3. Écrire le premier programme.** Dans le dossier <code>libraries/stzlib</code>, créer un fichier <code>first.ring</code> dont la première ligne charge la bibliothèque, puis le programme de la section suivante :

<pre>load "stzLib.ring"</pre>

Le lancer depuis ce dossier :

<pre>ring first.ring</pre>

Le premier lancement prend environ sept secondes, parce que la bibliothèque et son moteur se chargent.

## Le premier programme {#first}

<div class="run"><div><div class="lbl">premier</div><pre>o1 = new stzList([ "A", "", "B", "", "", "C" ])
? o1.ContainsEmptyStrings()

? Q("Softanza").Boxed()</pre></div><div class="out"><div class="lbl">Sortie</div><pre>1
┌──────────┐
│ Softanza │
└──────────┘</pre></div></div>
<p class="ran">exécuté le 2026-10-09 à 00:52 par <code>ring first.ring</code> depuis <code>libraries/stzlib</code>, en 6,9 secondes, Softanza au commit <a href="https://github.com/mayouni/stzlib/commit/4a184e6f0">4a184e6f0</a></p>

## La première narration {#narration}

Une narration est un document qui raconte une partie de la bibliothèque comme une histoire, en code écrit pour être exécuté au fil de la lecture. Commencez par <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/narrations/stz-mental-mode-narration.md">le modèle mental</a>, puis <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/narrations/stz-agents-that-cannot-hurt-you-narration.md">les agents qui ne peuvent pas vous nuire</a> ; les deux s'ouvrent sur GitHub. Pour voir une narration jugée bloc par bloc, ouvrez <a href="narrations/stz-repetition-with-elegance-narration.html">Repetition with Elegance</a>, exécutée pour ce site : ses six blocs affichent ce qu'ils promettent. Les 134 sont listées sous Apprendre, dans Narrations.

## Le lecteur du cours {#reader}

Le lecteur est une page de ce site : <a href="../reader.html">ouvrir le lecteur</a>. Il a été construit depuis la bibliothèque le 2026-09-30, et la page Apprendre dit comment apprendre avec lui, étape par étape. Pour le reconstruire vous-même, depuis votre copie du dépôt :

<pre>cd libraries/stzlib/base/education/tools
ring build_reader.ring reader.html</pre>

<p class="ran">exécuté le 2026-09-30 à 23:02 : « 15 of 15 chapters, 3 of 3 world pages », chaque édition verte, en 3 minutes 22 secondes</p>

Et pour jouer la démonstration de quinze minutes pour décideurs, dont la dernière ligne doit dire « DEMO: 20 proved, 0 not proved » :

<pre>cd libraries/stzlib/base/education/demo
ring demo.ring rehearsal</pre>

<p class="ran">exécuté le 2026-09-30 à 23:10, en 49 secondes, 20 preuves sur 20</p>

## Votre première application {#application}

Un premier programme est une liste. Une première application est un monde : <a href="first.html">votre première application</a> dit de quoi il est fait et quelle narration en construit un, et <a href="applications.html">la page des applications</a> dit ce qui le porte et quelles surfaces existent.

## Écrire {#write}

Les questions, les rapports de défaut et les propositions passent par <a href="https://github.com/mayouni/stzlib/issues">les tickets du dépôt GitHub</a>. Une faille de sécurité se signale en privé par les avis de sécurité du dépôt, comme le dit son <a href="https://github.com/mayouni/stzlib/blob/main/SECURITY.md">SECURITY.md</a>. Une édition du cours dans votre langue commence par un dossier de chapitres en texte brut : la page Apprendre dit comment le tribunal du cours la jugera. Pour l'édition entreprise, écrivez par les mêmes tickets : <a href="editions.html">la page Éditions</a> dit ce qu'elle contient.

## Vérifier ce site hors ligne {#offline}

Avant une présentation sans réseau, ouvrez <a href="../deck-check.html">deck-check.html</a> depuis le dossier du site : la page charge chaque ressource dont la présentation a besoin et dit laquelle manque.
