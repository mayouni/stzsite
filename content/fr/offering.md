---
title: Audiences
title_html: Pour <i>qui</i>
kicker: Six portes, une seule histoire
lede: Softanza raconte une seule histoire à six sortes de makers. Chaque porte ci-dessous dit ce que ce lecteur déclare et ce qu'il obtient, et montre un exemple exécuté le soir de la publication.
description: Les six publics de Softanza, du programmeur à l'agent : ce que chacun déclare et obtient, avec un vrai exemple.
---

## Qu'est-ce qu'un maker ? {#maker}

Un maker transforme ce qu'il sait d'un monde en quelque chose qui tourne, sans attendre l'industrie du logiciel. Il n'est pas défini par sa maîtrise de la programmation mais par la propriété : l'artefact est à lui, en texte brut, et il n'expire pas. Une enseignante, un analyste, un commerçant, un élève, un fonctionnaire, et un agent qui propose sous tous ces mondes.

## Six portes {#doors}

<div class="door-section" id="programmeur" markdown="1">
<div class="kicker">Porte 1</div>
### Programmeur ou programmeuse, seul·e ou en petite équipe

**Ce que vous déclarez :** votre intention, dans une bibliothèque qui se lit comme une phrase : on trouve d'abord, on agit ensuite. **Ce que vous obtenez :** un moteur Zig sous chaque appel, correct en Unicode, et des narrations qui racontent ses idées en code. **Où commencer :** la page Démarrer, puis le chapitre 1 du cours.

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
### Analyste fonctionnel ou data

**Ce que vous déclarez :** les entités, les règles et les flux de votre organisation, dans un fichier de connaissance en texte brut. **Ce que vous obtenez :** un monde interrogeable, où le graphe des dépendances et la table des symboles sont le même graphe, plus des tables et des statistiques calculées par le moteur. **Où commencer :** le chapitre 12 du cours, « Enseigner un monde », dans [le lecteur](../reader.html).

<div class="run"><div><div class="lbl">Softanza</div><pre>o = new stzTable([ [ :region, :population ],
    [ "Agadez", 487620 ], [ "Maradi", 3402094 ], [ "Zinder", 3539764 ] ])
o.Show()</pre></div><div class="out"><div class="lbl">Sortie</div><pre>╭────────┬────────────╮
│ Region │ Population │
├────────┼────────────┤
│ Agadez │     487620 │
│ Maradi │    3402094 │
│ Zinder │    3539764 │
╰────────┴────────────╯</pre></div></div>
<p class="ran">exécuté le 2026-10-01 à 09:26 ; les chiffres sont ceux du recensement RGPH 2012 de l'Institut national de la statistique du Niger, tels que lus par le garde de la carte</p>
</div>

<div class="door-section" id="designer" markdown="1">
<div class="kicker">Porte 3</div>
### Designer UI, UX, CX

**Ce que vous déclarez :** une image, une carte, un écran, comme un programme. **Ce que vous obtenez :** un rendu produit par le moteur, reproductible à l'octet, et une constitution des interfaces de 122 règles et 22 verbes qu'une machine peut vérifier. **Où commencer :** le chapitre 11 du cours, « Dessiner la réponse », et la constitution Zui.

<figure><img src="../assets/img/areas/graphics.webp" alt="Une image rendue par le moteur pour le domaine du graphisme." width="1100" height="660"><figcaption>Une des vingt-huit images de la page Plateforme, chacune produite par la plateforme elle-même ; la carte du Niger sur la page Vision en est une autre.</figcaption></figure>
</div>

<div class="door-section" id="decideur" markdown="1">
<div class="kicker">Porte 4</div>
### CTO, gouvernement, startup, entreprise

**Ce que vous déclarez :** votre monde, votre gouvernance, et ce que chaque acteur, humain ou agent, peut commettre. **Ce que vous obtenez :** des agents qui ne peuvent pas vous nuire, un modèle de menace de trente-huit garanties avec leurs gardes, un confinement mesuré, et la propriété de tout : code, configuration, données, en texte brut. **Où commencer :** le paradigme agentique, puis [les éditions ci-dessous](editions.html#editions).

<div class="run"><div><div class="lbl">Un analyste de banque déclare un agent</div><pre>A bank analyst declares a stock-watcher agent,
first without saying what it covers:
-> refused / [pia-coverage @ coverage]
   an agent must say WHAT IT COVERS.
...then with its coverage stated:
-> The court judged your declaration,
   and every promise of the exercise was kept.</pre></div><div class="out"><div class="lbl">L'exercice de confinement</div><pre>>> TIME TO DETECT : 395 ms
>> TIME TO CONTAIN: 50 ms
TOTAL: 27 assertions, 27 pass, 0 fail</pre></div></div>
<p class="ran">exécuté le 2026-09-30 à 23:10 (démonstration, scène 7) et le 2026-10-01 à 00:41 (exercice de confinement)</p>
</div>

<div class="door-section" id="educateur" markdown="1">
<div class="kicker">Porte 5</div>
### Éducateur, linguiste, auteur, architecte de connaissance

**Ce que vous déclarez :** un cours, une surcouche pour votre institution, une édition dans votre langue, un monde de connaissance. **Ce que vous obtenez :** un programme en texte brut où chaque cellule s'exécute et où chaque exercice est vérifié en s'exécutant, un tuteur qui demande, des cohortes dont le rapport est une narration. **Où commencer :** <a href="education.html">Éducation</a>, avec ses trois portes : apprendre, enseigner, diriger un programme. <b>À côté :</b> les éditions française, arabe et haoussa sont des brouillons (0 unité sur 35 relue), les cellules s'exécutent sur le bureau, et aucune institution ne l'a encore adopté : <a href="education-record.html">ce qui est prouvé, et ce qui ne l'est pas</a>.

<div class="run"><div><div class="lbl">Zara, 9 ans, répond à la mission 1 en haoussa</div><pre>? len( NaturallyIn("ha",
   'Yi jeri dauke [ "Ibrahim", "Fatima", "Ibrahim",
                    "Moussa", "Fatima" ] cire maimaitattu').Result() )
-> Every promise of the exercise was kept when your program ran.
PROVED  the child's Hausa program passed, checked by running it</pre></div><div class="out"><div class="lbl">Le moteur compte des lettres, pas des octets</div><pre>? Q("سلام").NumberOfChars()         --> 4
? Q("مرحبا بالعالم").Script()        --> arabic</pre></div></div>
<p class="ran">exécuté le 2026-09-30 à 23:10 et le 2026-10-01 à 09:26</p>
</div>

<div class="door-section" id="agent" markdown="1">
<div class="kicker">Porte 6</div>
### Un agent

**Ce que vous déclarez :** vous-même, dans un fichier d'agent : ce que vous couvrez, la réversibilité de vos actes, la posture de chaque fonction que vous appelez. **Ce que vous obtenez :** un atelier où tout ce que vous faites est répété sans toucher le réel, une grammaire contrainte qui vous empêche d'émettre une phrase malformée, et un tribunal qui juge votre plan. **Ce que vous n'obtenez pas :** la capacité de commettre. **Où commencer :** le paradigme agentique, et le chapitre 14 du cours, « Un agent qui ne peut pas nuire ».

<div class="run"><div><div class="lbl">Un agent propose 610 suppressions</div><pre>Update plan (610 of 610 operations to commit):
* 1. delete file '…/course.zknw'
* 2. delete file '…/curriculum.zknw'
...</pre></div><div class="out"><div class="lbl">Le tribunal répond</div><pre>actor 'amina-helper-llm' cannot commit
-- it lacks the 'effectful' capability
   (required by operation 1)
PROVED  the course folder still holds all 610 files</pre></div></div>
<p class="ran">exécuté le 2026-09-30 à 23:10 par <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/demo/demo.ring">demo</a>, scène 6</p>
</div>
