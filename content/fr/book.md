---
title: Le livre
title_html: Le <i>livre</i> interactif
kicker: Étape 2 sur 3 · quinze chapitres, quatre langues
lede: L'Introduction élémentaire est un cours de quinze chapitres, en anglais, français, arabe et haoussa. Les trois dernières sont des brouillons : aucun locuteur natif n'a encore relu une seule de leurs 35 unités. On le lit dans **le lecteur**, une page de ce site construite en exécutant chaque cellule de chaque chapitre dans chaque langue : la construction est rouge si une cellule échoue ou si la promesse d'un exercice n'est pas tenue.
description: Le livre interactif de Softanza : quinze chapitres en anglais, français, arabe et haoussa, chaque cellule exécutée.
---

<div class="doors doors-wide">
<a class="door big" href="../reader.html"><div class="who">Le lecteur</div><div class="what">Ouvrir le livre interactif</div><div class="how">Quinze chapitres · en · fr · ar · ha · trois mondes d'enseignement · chaque cellule a tourné quand la page a été construite le 2026-09-30 à 23:02, en 3 minutes 22 secondes. L'arabe se lit de droite à gauche.</div></a>
</div>

<div class="figures">
<div class="figure"><b>15 × 4</b><span>chapitres × langues, l'Introduction élémentaire</span><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/base/education/program/courses/elementary-introduction/chapters">chapters/</a></div>
<div class="figure"><b>15 × 4</b><span>chapitres × langues, le cours de mathématiques</span><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/base/education/program/courses/math/chapters">math/chapters/</a></div>
<div class="figure"><b>3</b><span>mondes d'enseignement : le restaurant, la coopérative, l'école</span></div>
<div class="figure"><b>14</b><span>gardes qui jugent le système d'apprentissage lui-même, 716 assertions, exécutés par les auteurs du module</span><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/base/test/education">test/education</a></div>
</div>

Le même chapitre s'ouvre par la même phrase dans les quatre langues, et la même cellule s'exécute dans chacune. Les éditions française, arabe et haoussa portent, sur chaque chapitre et chaque page de monde, une note dans leur propre langue disant qu'elles attendent la relecture d'un locuteur natif : 0 unité sur 35 a été relue (<a href="education-record.html#limits">le bilan</a>). C'est écrit sur la page, pas caché.

<div class="pair">
<div><h4>Haoussa · Nemo, sannan ka aiwatar</h4><p>Kowane wurin aiki yana karɓar buƙatu: gidan abinci yana karɓar oda, banki yana karɓar tikiti, kuma buƙata ɗaya takan zo fiye da sau ɗaya.</p><pre>o1 = new stzList([ "tea", "rice", "tea", "fish", "rice", "tea" ])
? o1.NumberOfItems()
#--> 6</pre><p class="proof"><a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/program/courses/elementary-introduction/chapters/01-find-then-apply.ha.md">01-find-then-apply.ha.md</a></p></div>
<div><h4>Français · Trouver, puis agir</h4><p>Tout lieu de travail reçoit des demandes : un restaurant reçoit des commandes, une banque reçoit des tickets, et la même demande arrive souvent plusieurs fois.</p><pre>o1 = new stzList([ "tea", "rice", "tea", "fish", "rice", "tea" ])
? o1.NumberOfItems()
#--> 6</pre><p class="proof"><a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/program/courses/elementary-introduction/chapters/01-find-then-apply.fr.md">01-find-then-apply.fr.md</a></p></div>
</div>

La couche naturelle de la bibliothèque comprend une instruction dans les quatre langues du cours et l'exécute :

<div class="run"><div><div class="lbl">Softanza</div><pre>? @@( Naturally("Create a list with [ 5, 3, 5, 1 ] and remove its duplicates").Result() )
? @@( NaturallyIn("ha", "Yi jeri dauke [ 5, 3, 5, 1 ] cire maimaitattu").Result() )
? @@( NaturallyIn("ar", "أنشئ قائمة مع [ 5, 3, 5, 1 ] أزل التكرارات").Result() )</pre></div><div class="out"><div class="lbl">Sortie</div><pre>[ 5, 3, 1 ]
[ 5, 3, 1 ]
[ 5, 3, 1 ]</pre></div></div>
<p class="ran">exécuté le 2026-09-30 à 23:10 par <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/demo/demo.ring">demo</a>, dernière ligne « DEMO: 20 proved, 0 not proved », en 49 secondes</p>

## La preuve de chaque chapitre {#proof}

<!--PROOF-->
