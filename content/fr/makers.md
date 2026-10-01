---
title: Six portes
title_html: Six <i>portes</i>
kicker: Les makers
lede: Une seule histoire, six façons d'y entrer. Pour chaque lecteur : ce qu'il déclare, ce qu'il obtient, où il commence, et un exemple exécuté ce soir.
description: Les six audiences de Softanza, du programmeur à l'agent : ce que chacune déclare, ce qu'elle obtient, où elle commence, avec un exemple réel exécuté.
---

## Qu'est-ce qu'un maker ?

Un maker transforme ce qu'il sait d'un monde en quelque chose qui tourne, sans attendre l'industrie du logiciel. Il n'est pas défini par sa maîtrise de la programmation mais par la propriété : l'artefact est à lui, en texte brut, et il n'expire pas. Une enseignante, un analyste, un commerçant, un élève, un fonctionnaire, et un agent qui propose sous tous ces mondes. Softanza raconte une seule histoire ; chaque porte ci-dessous l'ouvre à l'endroit qui vous concerne.

<div class="door-section" id="programmeur" markdown="1">
<div class="kicker">Porte 1</div>
## Programmeur ou programmeuse, seul·e ou en petite équipe

**Ce que vous déclarez :** votre intention, dans une bibliothèque qui se lit comme une phrase : on trouve d'abord, on agit ensuite. **Ce que vous obtenez :** un moteur Zig sous chaque appel, correct en Unicode, et une narration qui s'exécute pour chaque idée. **Où commencer :** [la page Commencer](start.html), puis le chapitre 1 du cours.

<div class="run"><div><div class="lbl">Softanza</div><pre>o1 = new stzList([ "tea", "rice", "tea", "fish", "rice", "tea" ])
? o1.ContainsDuplicates()
? o1.NumberOfOccurrence("tea")
? @@( o1.FindAll("tea") )
? @@( o1.DuplicatesRemoved() )</pre></div><div class="out"><div class="lbl">Sortie</div><pre>1
3
[ 1, 3, 6 ]
[ "tea", "rice", "fish" ]</pre></div></div>
<p class="ran">exécuté le 2026-09-30 à 23:11, Softanza au commit 0e72e2e2c</p>
</div>

<div class="door-section" id="analyste" markdown="1">
<div class="kicker">Porte 2</div>
## Analyste fonctionnel ou data

**Ce que vous déclarez :** les entités, les règles et les flux de votre organisation, dans un fichier de connaissance en texte brut. **Ce que vous obtenez :** un monde interrogeable, où le graphe de dépendances et la table des symboles sont le même graphe, et des tables et des statistiques calculées par le moteur. **Où commencer :** le chapitre 12 du cours, « Enseigner un monde », dans [le lecteur](learn.html).

<div class="run"><div><div class="lbl">Softanza</div><pre>o = new stzTable([ [ :region, :population ],
    [ "Agadez", 487620 ], [ "Maradi", 3402094 ], [ "Zinder", 3539764 ] ])
o.Show()
? Q([ 487620, 593821, 2037713, 3402094,
      1026848, 3328365, 2722482, 3539764 ]).Sum()</pre></div><div class="out"><div class="lbl">Sortie</div><pre>╭────────┬────────────╮
│ Region │ Population │
├────────┼────────────┤
│ Agadez │     487620 │
│ Maradi │    3402094 │
│ Zinder │    3539764 │
╰────────┴────────────╯
17138707</pre></div></div>
<p class="ran">exécuté le 2026-09-30 à 23:11 ; les chiffres sont ceux du recensement RGPH 2012 de l'Institut National de la Statistique du Niger, lus par le garde de la carte</p>
</div>

<div class="door-section" id="designer" markdown="1">
<div class="kicker">Porte 3</div>
## Designer UI, UX, CX

**Ce que vous déclarez :** une image, une carte, un écran, comme un programme. **Ce que vous obtenez :** un rendu produit par le moteur, reproductible à l'octet près, et un langage d'interface de vingt-quatre verbes fermés dans la famille Zin. **Où commencer :** le chapitre 11 du cours, « Dessiner la réponse », dans [le lecteur](learn.html).

<figure><img src="../assets/img/niger-density.png" alt="Carte de densité de population du Niger par région : Agadez presque vide au nord, les régions du sud denses, Niamey hors échelle." width="1500" height="1240"><figcaption>« Where Niger lives », rendue ce soir en 5,9 secondes par <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/graphics/niger_density.ring">niger_density</a> : frontières geoBoundaries (ODbL), recensement 2012, surfaces mesurées par la routine géodésique du moteur sur l'ellipsoïde WGS84.</figcaption></figure>
</div>

<div class="door-section" id="decideur" markdown="1">
<div class="kicker">Porte 4</div>
## CTO, gouvernement, startup, entreprise

**Ce que vous déclarez :** votre monde, votre gouvernance, et ce que chaque acteur, humain ou agent, a le droit de commettre. **Ce que vous obtenez :** des agents qui ne peuvent pas vous nuire, un modèle de menace de trente-huit garanties avec leurs gardes, un confinement mesuré, et la propriété de tout : code, configuration, données, en texte brut. **Où commencer :** [Gouverner](govern.html), puis [Produits](products.html) pour les stades.

<div class="run"><div><div class="lbl">Un analyste bancaire déclare un agent</div><pre>A bank analyst declares a stock-watcher agent,
first without saying what it covers:
-> refused / [pia-coverage @ coverage]
   an agent must say WHAT IT COVERS.
...then with its coverage stated:
-> The court judged your declaration,
   and every promise of the exercise was kept.</pre></div><div class="out"><div class="lbl">L'exercice de confinement</div><pre>>> TIME TO DETECT : 395 ms
>> TIME TO CONTAIN: 50 ms
TOTAL: 27 assertions, 27 pass, 0 fail</pre></div></div>
<p class="ran">exécuté le 2026-09-30 à 23:10 (démo, scène 7) et le 2026-10-01 à 00:41 (exercice de confinement)</p>
</div>

<div class="door-section" id="educateur" markdown="1">
<div class="kicker">Porte 5</div>
## Éducateur, linguiste, auteur, architecte de connaissance

**Ce que vous déclarez :** un cours, un calque pour votre institution, une édition dans votre langue, un monde de connaissance. **Ce que vous obtenez :** un programme en texte brut dont chaque cellule s'exécute et chaque exercice se vérifie en s'exécutant, un tuteur qui pose des questions, des cohortes dont le rapport est une narration. **Où commencer :** [Apprendre](learn.html), et le guide des calques.

<div class="run"><div><div class="lbl">Zara, 9 ans, répond à la Mission 1 en haoussa</div><pre>? len( NaturallyIn("ha",
   'Yi jeri dauke [ "Ibrahim", "Fatima", "Ibrahim",
                    "Moussa", "Fatima" ] cire maimaitattu').Result() )
-> Every promise of the exercise was kept when your program ran.
PROVED  the child's Hausa program passed, checked by running it</pre></div><div class="out"><div class="lbl">Le moteur compte des lettres, pas des octets</div><pre>? len("سلام")                       --> 8
? Q("سلام").NumberOfChars()         --> 4
? Q("مرحبا بالعالم").Script()        --> arabic</pre></div></div>
<p class="ran">exécuté le 2026-09-30 à 23:10 et 23:11</p>
</div>

<div class="door-section" id="agent" markdown="1">
<div class="kicker">Porte 6</div>
## Un agent

**Ce que vous déclarez :** vous-même, dans un fichier d'agent : ce que vous couvrez, la réversibilité de vos actes, la posture de chaque fonction que vous appelez. **Ce que vous obtenez :** un établi où tout ce que vous faites est répété sans toucher la réalité, une grammaire contrainte qui vous empêche d'émettre une phrase malformée, et un tribunal qui juge votre plan. **Ce que vous n'obtenez pas :** la capacité de commettre. **Où commencer :** [Gouverner](govern.html), et le chapitre 14 du cours, « Un agent qui ne peut pas nuire ».

<div class="run"><div><div class="lbl">Un agent propose 610 suppressions</div><pre>Update plan (610 of 610 operations to commit):
* 1. delete file '…/course.zknw'
* 2. delete file '…/curriculum.zknw'
...</pre></div><div class="out"><div class="lbl">Le tribunal répond</div><pre>actor 'amina-helper-llm' cannot commit
-- it lacks the 'effectful' capability
   (required by operation 1)
PROVED  the course folder still holds all 610 files</pre></div></div>
<p class="ran">exécuté le 2026-09-30 à 23:10 par <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/demo/demo.ring">demo</a>, scène 6</p>
</div>
