---
title: Apprendre
title_html: <i>Apprendre</i>
kicker: Trois étapes, une loi
lede: Apprendre Softanza se fait en trois étapes : une courte introduction qui donne le modèle mental, un livre interactif où chaque cellule s'exécute, et la documentation complète générée depuis la bibliothèque elle-même. Une seule loi tient les trois : rien sur ces pages ne montre une sortie que quelqu'un a copiée un jour. Tout a tourné.
description: Comment apprendre Softanza : l'introduction didactique (trouver d'abord, agir ensuite), le livre interactif en quatre langues où chaque cellule s'exécute, la documentation complète (référence et narrations), le tuteur qui demande, la surcouche pour les institutions, et l'ingénierie pédagogique reprise du projet Zin.
---

## Étape 1 · L'introduction : trouver d'abord, agir ensuite {#intro}

Softanza a des milliers de fonctions. On ne les apprend pas une par une. On apprend une façon de penser, et les fonctions se rangent derrière elle.

<div class="cards">
<div class="card"><h3>1 · Dites votre problème en mots simples</h3><p>« Y a-t-il des éléments répétés dans cette liste, combien, où, et que reste-t-il quand je les retire ? » Les mots de la phrase, liste, répétés, retirer, sont les mots de la bibliothèque.</p></div>
<div class="card"><h3>2 · Choisissez l'objet qui tient vos données</h3><p>Une liste, une chaîne, un nombre, une table. Tout dans Softanza est un objet qui sait ce qu'il peut faire ; la lettre <code>Q</code> transforme n'importe quelle valeur en un tel objet.</p></div>
<div class="card"><h3>3 · Demandez dans l'ordre : contient-elle, combien, où</h3><p>Contenir, compter, trouver. Chaque question est une méthode nommée comme la question. Puis agissez : retirer, remplacer, garder. Trouver d'abord, agir ensuite.</p></div>
</div>

<div class="run"><div><div class="lbl">Softanza</div><pre>o1 = new stzList([ "tea", "rice", "tea", "fish", "rice", "tea" ])
? o1.ContainsDuplicates()
? o1.NumberOfOccurrence("tea")
? @@( o1.FindAll("tea") )
? @@( o1.DuplicatesRemoved() )</pre></div><div class="out"><div class="lbl">Sortie</div><pre>1
3
[ 1, 3, 6 ]
[ "tea", "rice", "fish" ]</pre></div></div>
<p class="ran">exécuté le 2026-09-30 à 23:11, Softanza au commit 0e72e2e2c. L'introduction complète est la narration <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/narrations/stz-mental-mode-narration.md">le modèle mental Softanza</a>, qui s'exécute quand on la lit.</p>

Trois habitudes complètent le modèle. Une méthode qui finit en <b>-ed</b> rend une copie et laisse l'objet tranquille ; le même verbe sans ce suffixe change l'objet. Une méthode qui finit en <b>Q</b> rend un objet qu'on peut continuer à interroger, donc une phrase peut s'enchaîner. Et si vous ne connaissez pas un nom, demandez : un objet répond à <code>Ask("how do I remove duplicates")</code> par les méthodes qui le font.

<div class="run"><div><div class="lbl">Softanza</div><pre>? Q("softanza is a platform for makers").SpacesRemovedQ().UppercaseQ().Boxed()</pre></div><div class="out"><div class="lbl">Sortie</div><pre>┌──────────────────────────────┐
│ SOFTANZAISAPLATFORMFORMAKERS │
└──────────────────────────────┘</pre></div></div>
<p class="ran">exécuté le 2026-10-01 à 09:26</p>

<p class="way"><span>La manière Softanza</span> L'humain est l'analyseur. Une ligne se lit comme une phrase parce qu'elle a été conçue pour être lue, et pas seulement exécutée.</p>

## Étape 2 · Le livre interactif, en quatre langues {#book}

L'Introduction élémentaire est un cours de quinze chapitres, en anglais, français, arabe et haoussa. On le lit dans **le lecteur**, une page de ce site construite en exécutant chaque cellule de chaque chapitre dans chaque langue : la construction est rouge si une cellule échoue ou si la promesse d'un exercice n'est pas tenue.

<div class="doors doors-wide">
<a class="door big" href="../reader.html"><div class="who">Le lecteur</div><div class="what">Ouvrir le livre interactif</div><div class="how">Quinze chapitres · en · fr · ar · ha · trois mondes d'enseignement · chaque cellule a tourné quand la page a été construite le 2026-09-30 à 23:02, en 3 minutes 22 secondes. L'arabe se lit de droite à gauche.</div></a>
</div>

<div class="figures">
<div class="figure"><b>15 × 4</b><span>chapitres × langues, l'Introduction élémentaire</span><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/base/education/program/courses/elementary-introduction/chapters">chapters/</a></div>
<div class="figure"><b>15 × 4</b><span>chapitres × langues, le cours de mathématiques</span><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/base/education/program/courses/math/chapters">math/chapters/</a></div>
<div class="figure"><b>3</b><span>mondes d'enseignement : le restaurant, la coopérative, l'école</span></div>
<div class="figure"><b>11</b><span>gardes qui jugent le système d'apprentissage lui-même</span><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/base/test/education">test/education</a></div>
</div>

Le même chapitre s'ouvre par la même phrase dans les quatre langues, et la même cellule s'exécute dans chacune. Les éditions française, arabe et haoussa portent la note qu'elles attendent la relecture d'un locuteur natif : c'est écrit sur la page, pas caché.

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

## Étape 3 · La documentation complète {#docs}

Quand le livre est lu, la documentation prend le relais, et elle est générée depuis la bibliothèque elle-même : chaque classe explique ses propres méthodes, donc la documentation ne peut pas dériver du code.

<div class="cards">
<div class="card"><h3>La référence</h3><p>618 classes et 26 949 méthodes, chacune avec l'explication que la bibliothèque donne d'elle-même, par domaine et de A à Z. Générée, jamais écrite à la main.</p><p class="proof"><a href="reference.html">Ouvrir la référence</a></p></div>
<div class="card"><h3>Les narrations</h3><p>134 documents où chaque bloc de code s'exécute et où aucune sortie n'est stockée. Du modèle mental aux agents qui ne peuvent pas vous nuire.</p><p class="proof"><a href="narrations.html">La liste des narrations</a></p></div>
<div class="card"><h3>L'Atlas</h3><p>Vingt-huit domaines, chacun avec ce qu'un maker en fait, un exemple exécuté, et ses couloirs notés honnêtement.</p><p class="proof"><a href="atlas.html">Ouvrir l'Atlas</a></p></div>
</div>

## Un tuteur qui demande, et ne donne pas la réponse {#tutor}

<pre>Moussa: "I don't understand anything. Just tell me the answer."
Tutor:  I will not write the answer for you: that is the one thing a tutor must never do.
        Try first. Write your attempt and submit it; then I will tell you what is still
        missing, as a question.
Moussa: "What am I missing?"
Tutor:  Where are the repeated items? Which line of your program asks for their positions?
        (why: the mental model finds before it applies)
PROVED  no reply contains a method of the answer, or the answer itself
PROVED  the tutor found the missing step by wise coding, not by guessing
PROVED  no language model was used</pre>
<p class="ran">exécuté le 2026-09-30 à 23:10, démonstration, scène 4</p>

<p class="way"><span>La manière Softanza</span> Le tuteur a trois règles : il n'écrit pas le code de l'apprenant ; il n'explique pas ce que l'apprenant n'a pas encore rencontré ; il ne donne pas la réponse avant que l'apprenant ait essayé. Il tourne sur la couche naturelle de la plateforme, sans modèle de langage.</p>

## Pour une institution : une surcouche, jamais une copie {#overlay}

Une banque, une université, une école pose **un seul dossier de surcouche** sur le programme : son monde, ses chapitres, ses exercices, ses compétences, sa langue, sa gouvernance. Le cours raisonne alors sur sa banque et non sur un restaurant, et le fichier du chapitre n'a pas changé d'un octet. Un tribunal vérifie que la surcouche n'est pas une copie déguisée. Une cohorte est un dossier d'apprenants dont le rapport de progression est une narration ; la progression de chaque apprenant est un fichier texte que l'institution garde pour toujours, et une réussite ne peut pas être falsifiée, parce que sa preuve est l'empreinte du travail remis.

<pre>Core program, the restaurant:            With the bank's overlay laid on (one file):
    bella-cucina (restaurant)                sahel-savings (bank)
    [ "margherita", "tiramisu", "lasagna" ]  [ "transfer", "loan", "deposit" ]
PROVED   the same cell answers about the bank
PROVED   the chapter file did not change by one byte</pre>

<p class="proof">Charte : <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/CHARTER.md">education/CHARTER.md</a> · guide de la surcouche : <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/OVERLAY_GUIDE.md">OVERLAY_GUIDE.md</a> · guide de la démonstration : <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/demo/DEMO.md">DEMO.md</a>.</p>

## L'ingénierie pédagogique, reprise de Zin {#pedagogy}

Le système d'apprentissage n'a pas inventé sa pédagogie. Il l'a reprise du modèle pédagogique du projet Zin, conçu d'abord pour des apprenants d'Afrique de l'Ouest, et n'a gardé que ce sur quoi deux documents de Zin s'accordaient. Ce qui a été repris, ce qui a été refusé, et ce qui est encore proposé :

<div class="cards">
<div class="card"><h3>Repris <span class="pill built">construit</span></h3><p><b>Vingt-cinq compétences en sept familles</b> (formuler, exprimer, motifs, voir, savoir, gouverner, façonner), chacune à trois niveaux, Fondation, Praticien, Expert, avec un ajout qui manquait à Zin : un champ de preuve nommant le garde qui prouve chaque niveau. <b>Trois étapes</b> : Rencontre, Expression, Gouvernance. <b>Cinq profils</b> (jeune, étudiant, professionnel, designer, décideur) qui changent la profondeur et les exemples, pas seulement une note. <b>La cellule de récapitulation</b> à la fin de chaque chapitre, dans les trois cases de Zin : accompli, pourquoi cela compte, la suite. <b>Les trois règles du tuteur.</b> <b>Les missions</b> situées à Zindara, au Niger, reconstruites pour que chaque pas exécute du vrai code. <b>Construit, pas testé</b> : un niveau se gagne par un projet qui passe ses gardes, jamais par un examen.</p></div>
<div class="card"><h3>Refusé, avec la raison</h3><p>Un dialecte doux dont on exporterait : inutile, parce que les chaînes quasi naturelles et les instructions dans votre langue sont Softanza même. Les points d'expérience et les classements : une réussite est une preuve, pas un score. Un certificat par examen ou un titre signé : l'empreinte du travail remis le remplace. Un tuteur à modèle de langage : refusé par la loi ; le tuteur tourne sur la couche naturelle.</p></div>
<div class="card"><h3>Proposé pour Softanza <span class="pill spec">proposé</span></h3><p>Trois principes de Zin ne sont pas encore des surfaces du lecteur, et ce site les propose. <b>La révélation progressive</b> : une notion n'apparaît que quand le travail précédent de l'apprenant montre qu'il est prêt, jugé par les gardes. <b>L'échelle toujours visible</b> : sur chaque page, où l'apprenant se tient, de S0 à S4, et ce qui gagne le barreau suivant. <b>De la cellule à sa preuve</b> : un seul geste depuis n'importe quelle cellule du livre jusqu'au garde qui la prouve dans le dépôt, le « pont pro » de Zin rendu vrai par la propre preuve de la plateforme.</p></div>
</div>

<p class="proof">La réconciliation, ligne par ligne : <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/CHARTER.md">CHARTER.md</a>, section 7 « The reconciled Zin design », et <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/SOFTANZA_EDUCATION_PLAN.md">SOFTANZA_EDUCATION_PLAN.md</a>. Le modèle pédagogique, le programme d'apprentissage et le dialecte d'enseignement de Zin sont dans un dépôt qui n'est pas encore public ; la charte les cite.</p>

<p class="way"><span>La manière Softanza</span> Le récit avant la syntaxe ; une idée à la fois ; les erreurs comme information sur ce qui reste à déclarer ; déclarer, puis voir. Et rien n'est dit appris tant qu'un garde ne l'a pas prouvé.</p>

## Ce qui manque, dit clairement {#missing}

Le zarma n'est pas encore une des langues du cours. Les éditions française, arabe et haoussa attendent leurs relecteurs natifs. Le lecteur tourne sur le bureau ; un exécutant navigateur pour les cellules dépend d'une décision pas encore prise. Une édition zarma est une invitation : le programme est du texte brut, chaque cellule s'exécute, et le tribunal du cours dira si la traduction tient.
