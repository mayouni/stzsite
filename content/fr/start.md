---
title: Commencer
title_html: <i>Commencer</i>
kicker: En une heure
lede: Deux dépôts publics, une installation en trois commandes, un premier programme, le lecteur du cours. Chaque commande de cette page a été exécutée cette nuit.
description: Comment commencer avec Softanza : les dépôts GitHub et Codeberg, l'installation, le premier programme, la première narration, le lecteur du cours, et où écrire.
---

## Les dépôts

<div class="cards">
<div class="card"><h3>GitHub</h3><p>La fondation, son moteur, ses narrations et son cours.</p><p class="proof"><a href="https://github.com/mayouni/stzlib">github.com/mayouni/stzlib</a></p></div>
<div class="card"><h3>Codeberg</h3><p>Le même dépôt, poussé à chaque commit, sur une forge européenne.</p><p class="proof"><a href="https://codeberg.org/MAyouni/stzlib">codeberg.org/MAyouni/stzlib</a></p></div>
<div class="card"><h3>Ce site</h3><p>Généré par un script Python à partir de fichiers Markdown ; polices et images hébergées ici, pour qu'il s'ouvre hors ligne.</p><p class="proof"><a href="https://github.com/mayouni/stzsite">github.com/mayouni/stzsite</a></p></div>
</div>

## Installer

Softanza s'exécute sur Ring 1.27 ; le moteur Zig est livré en bibliothèques compilées pour Windows, et se construit pour Linux et macOS depuis la source. Il n'y a rien à installer au sens d'un installateur : un dossier, copié.

<pre>git clone https://github.com/mayouni/stzlib.git
cd stzlib/libraries/stzlib
ring premier.ring</pre>

Ring se télécharge sur <a href="https://ring-lang.github.io/">ring-lang.github.io</a>. Un script placé dans le dossier <code>libraries/stzlib</code> charge la bibliothèque par une ligne.

## Le premier programme

<div class="run"><div><div class="lbl">premier.ring</div><pre>load "stzlib.ring"

o1 = new stzList([ "A", "", "B", "", "", "C" ])
? o1.ContainsEmptyStrings()

? Q("Softanza").Boxed()</pre></div><div class="out"><div class="lbl">Sortie</div><pre>1
┌──────────┐
│ Softanza │
└──────────┘</pre></div></div>
<p class="ran">exécuté le 2026-10-01 à 00:45 depuis <code>libraries/stzlib</code>, Ring 1.27, Softanza au commit <a href="https://github.com/mayouni/stzlib/commit/0e72e2e2c">0e72e2e2c</a></p>

## La première narration

Une narration est un document dont chaque bloc de code s'exécute, et dont les sorties ne sont jamais stockées : ce que vous lisez a été produit en lisant. Commencez par <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/narrations/stz-mental-mode-narration.md">le modèle mental</a>, puis <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/narrations/stz-agents-that-cannot-hurt-you-narration.md">les agents qui ne peuvent pas vous nuire</a>. Les 134 narrations sont dans <a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/base/doc/narrations">doc/narrations</a>.

## Le lecteur du cours

Le lecteur est [sur la page Apprendre](learn.html), construit cette nuit. Pour le reconstruire vous-même, depuis votre copie du dépôt :

<pre>cd libraries/stzlib/base/education/tools
ring build_reader.ring lecteur.html</pre>

<p class="ran">exécuté le 2026-09-30 à 23:02 : « 15 of 15 chapters, 3 of 3 world pages », toutes les éditions vertes, en 3 minutes 22 secondes</p>

Et pour jouer la démo de quinze minutes pour décideurs, dont la dernière ligne doit dire « DEMO: 20 proved, 0 not proved » :

<pre>cd libraries/stzlib/base/education/demo
ring demo.ring repetition</pre>

<p class="ran">exécuté le 2026-09-30 à 23:10, en 49 secondes, 20 preuves sur 20</p>

## Écrire

Les questions, les rapports de défaut et les propositions passent par les <a href="https://github.com/mayouni/stzlib/issues">issues du dépôt GitHub</a>. Une faille de sécurité se signale en privé par les avis de sécurité du dépôt, comme l'indique son fichier <a href="https://github.com/mayouni/stzlib/blob/main/SECURITY.md">SECURITY.md</a>. Une édition du cours dans votre langue, zarma ou autre, commence par un dossier de chapitres en texte brut : [la page Apprendre](learn.html) dit comment le tribunal du cours la jugera.

## Vérifier ce site hors ligne

Avant une présentation sans réseau, ouvrez <a href="../deck-check.html">deck-check.html</a> depuis le dossier du site : la page charge chaque ressource dont la présentation a besoin et dit laquelle manque.
