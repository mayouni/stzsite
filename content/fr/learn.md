---
title: Apprendre
title_html: <i>Apprendre</i>, en trois étapes
kicker: Étape 1 sur 3 · trouver d'abord, agir ensuite
lede: Apprendre Softanza se fait en trois étapes : une courte introduction qui donne le modèle mental, un livre interactif où chaque cellule s'exécute, et la documentation complète générée depuis la bibliothèque elle-même. Cette page est la première étape.
description: Comment apprendre Softanza, étape 1 : le modèle mental, trouver d'abord, agir ensuite.
---

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
<p class="ran">exécuté le 2026-09-30 à 23:11, Softanza au commit 0e72e2e2c. L'introduction complète est la narration <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/narrations/stz-mental-mode-narration.md">le modèle mental Softanza</a>.</p>

Trois habitudes complètent le modèle. Une méthode qui finit en <b>-ed</b> rend une copie et laisse l'objet tranquille ; le même verbe sans ce suffixe change l'objet. Une méthode qui finit en <b>Q</b> rend un objet qu'on peut continuer à interroger, donc une phrase peut s'enchaîner. Et si vous ne connaissez pas un nom, demandez : un objet répond à <code>Ask("how do I remove duplicates")</code> par les méthodes qui le font.

<div class="run"><div><div class="lbl">Softanza</div><pre>? Q("softanza is a platform for makers").SpacesRemovedQ().UppercaseQ().Boxed()</pre></div><div class="out"><div class="lbl">Sortie</div><pre>┌──────────────────────────────┐
│ SOFTANZAISAPLATFORMFORMAKERS │
└──────────────────────────────┘</pre></div></div>
<p class="ran">exécuté le 2026-10-01 à 09:26</p>

## L'échelle {#ladder}

<!--LADDER-->

<p class="way"><span>La manière Softanza</span> L'humain est l'analyseur. Une ligne se lit comme une phrase parce qu'elle a été conçue pour être lue, et pas seulement exécutée.</p>
