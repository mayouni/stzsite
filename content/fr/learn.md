---
title: Le Système d'apprentissage
title_html: Le Système <i>d'apprentissage</i>
kicker: Apprendre
lede: Deux cours de quinze chapitres, en anglais, en français, en arabe et en haoussa. Chaque cellule s'exécute. Chaque exercice est une promesse vérifiée en l'exécutant. Aucune sortie n'est stockée.
description: Le Système d'apprentissage Softanza : quinze chapitres en quatre langues, des missions, des kits pour les institutions, des cohortes et un tuteur qui pose des questions au lieu de donner la réponse.
---

## La loi du cours

Une page de cours ordinaire montre des sorties que quelqu'un a copiées un jour. Ici, la page est **construite en exécutant** chaque cellule de chaque chapitre dans chaque langue, et la construction est rouge si une seule cellule échoue ou si une seule promesse n'est pas tenue. Ce que vous lisez ci-dessous a été construit ce soir.

<div class="figures">
<div class="figure"><b>15 × 4</b><span>chapitres × langues, pour l'Introduction élémentaire</span><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/base/education/program/courses/elementary-introduction/chapters">chapters/</a></div>
<div class="figure"><b>15 × 4</b><span>chapitres × langues, pour le cours de mathématiques</span><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/base/education/program/courses/math/chapters">math/chapters/</a></div>
<div class="figure"><b>3</b><span>mondes d'enseignement : le restaurant, la coopérative, l'école</span></div>
<div class="figure"><b>11</b><span>gardes qui jugent le système lui-même</span><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/base/test/education">test/education</a></div>
</div>

## Le lecteur, construit ce soir

Le lecteur ci-dessous a été produit par l'outil <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/tools/build_reader.ring">build_reader</a> le 2026-09-30 à 23:02, en 3 minutes 22 secondes : quinze chapitres dans les quatre langues et trois pages de monde, tous verts. Choisissez la langue dans son menu ; l'arabe se lit de droite à gauche. Ses cellules ont été exécutées sur le bureau au moment de la construction, et la page le dit sur chaque cellule.

<div class="embed"><div class="embed-bar"><a href="../reader.html">Ouvrir le lecteur en plein écran</a><span>Introduction élémentaire · en · fr · ar · ha</span></div><iframe src="../reader.html" title="Le lecteur du cours Softanza, construit le 2026-09-30" loading="lazy"></iframe></div>

<pre>BUILD elementary-introduction in en, fr, ar, ha: 15 of 15 chapters, 3 of 3 world pages
  chapter 1 find-then-apply: en fr ar ha
  chapter 2 a-first-sentence: en fr ar ha
  ...
  chapter 14 an-agent-that-cannot-hurt: en fr ar ha
  chapter 15 write-a-narration: en fr ar ha
  world cooperative: en fr ar ha
  world school: en fr ar ha
  world workplace: en fr ar ha
WROTE reader.html
real    3m22.821s</pre>

## Le même chapitre en haoussa et en français

Le chapitre 1 s'ouvre par la même phrase dans les quatre langues, et la même cellule s'exécute dans chacune. Les éditions française, arabe et haoussa portent la mention qu'elles attendent la relecture d'un locuteur natif : c'est écrit sur la page, pas caché.

<div class="pair">
<div><h4>Haoussa · Nemo, sannan ka aiwatar</h4><p>Kowane wurin aiki yana karɓar buƙatu: gidan abinci yana karɓar oda, banki yana karɓar tikiti, kuma buƙata ɗaya takan zo fiye da sau ɗaya. Wannan babin yana maganin buƙatun da aka maimaita ta hanyar Softanza.</p><pre>o1 = new stzList([ "tea", "rice", "tea", "fish", "rice", "tea" ])
? o1.NumberOfItems()
#--> 6</pre><p class="proof"><a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/program/courses/elementary-introduction/chapters/01-find-then-apply.ha.md">01-find-then-apply.ha.md</a></p></div>
<div><h4>Français · Trouver, puis agir</h4><p>Tout lieu de travail reçoit des demandes : un restaurant reçoit des commandes, une banque reçoit des tickets, et la même demande arrive souvent plusieurs fois. Ce chapitre traite les demandes répétées à la manière de Softanza.</p><pre>o1 = new stzList([ "tea", "rice", "tea", "fish", "rice", "tea" ])
? o1.NumberOfItems()
#--> 6</pre><p class="proof"><a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/program/courses/elementary-introduction/chapters/01-find-then-apply.fr.md">01-find-then-apply.fr.md</a></p></div>
</div>

## Dans votre langue, littéralement

La couche naturelle de la bibliothèque comprend une consigne dans les quatre langues du cours et l'exécute. La démonstration ci-dessous a tourné ce soir ; elle fait partie des vingt preuves de la démo pour décideurs.

<div class="run"><div><div class="lbl">Softanza</div><pre>? @@( NaturallyIn("fr", "Crée une liste avec [ 5, 3, 5, 1 ] et enlève les doublons").Result() )
? @@( NaturallyIn("ha", "Yi jeri dauke [ 5, 3, 5, 1 ] cire maimaitattu").Result() )
? @@( NaturallyIn("ar", "أنشئ قائمة مع [ 5, 3, 5, 1 ] أزل التكرارات").Result() )</pre></div><div class="out"><div class="lbl">Sortie</div><pre>[ 5, 3, 1 ]
[ 5, 3, 1 ]
[ 5, 3, 1 ]</pre></div></div>
<p class="ran">exécuté le 2026-09-30 à 23:10 par <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/demo/demo.ring">demo</a>, dernière ligne : « DEMO: 20 proved, 0 not proved », en 49 secondes</p>

## Un tuteur qui demande, et ne donne pas la réponse

<pre>Moussa : « Donne-moi la réponse, c'est plus simple. »
Tuteur : Je n'écrirai pas la réponse à votre place : c'est la seule chose qu'un tuteur ne doit
         jamais faire. Où sont les éléments répétés ? Quelle ligne de votre programme demande
         leurs positions ? (pourquoi : le modèle mental trouve avant d'agir)
PROVED   no reply contains a method of the answer, or the answer itself
PROVED   the tutor found the missing step by wise coding, not by guessing
PROVED   no language model was used</pre>

## Pour une institution : un calque, jamais une copie

Une banque, une université, une école pose **un dossier de calque** sur le programme : son monde, ses chapitres, ses exercices, ses compétences, sa langue, sa gouvernance. Le cours raisonne alors sur sa banque et non sur un restaurant, et le fichier du chapitre n'a pas changé d'un octet. Un tribunal vérifie que le calque n'est pas une copie déguisée. Une cohorte est un dossier d'apprenants dont le rapport de progression est une narration ; le progrès de chacun est un fichier texte que l'institution garde pour toujours, et une réussite ne peut pas être contrefaite, parce que sa preuve est l'empreinte du travail rendu.

<pre>Core program, the restaurant:            With the bank's overlay laid on (one file):
    bella-cucina (restaurant)                sahel-savings (bank)
    [ "margherita", "tiramisu", "lasagna" ]  [ "transfer", "loan", "deposit" ]
PROVED   the same cell answers about the bank
PROVED   the chapter file did not change by one byte</pre>

## Ce qui manque, dit clairement

Le zarma n'est pas encore l'une des langues du cours. Les quatre éditions actuelles sont l'anglais, le français, l'arabe et le haoussa, et le haoussa attend sa relecture native. Une édition zarma est une invitation : le programme est en texte brut, chaque cellule s'exécute, et le tribunal du cours dira si la traduction tient.

<p class="proof">Charte et plan : <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/CHARTER.md">education/CHARTER.md</a> · guide des calques : <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/OVERLAY_GUIDE.md">OVERLAY_GUIDE.md</a> · guide de la démo : <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/demo/DEMO.md">DEMO.md</a>.</p>
