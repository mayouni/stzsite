---
title: La plateforme
title_html: La <i>plateforme</i>
kicker: Un moteur, vingt-huit domaines
lede: Softanza est une seule plateforme de calcul. Un moteur, écrit en Zig, traite le texte, les nombres exacts, les tables, les graphes, les cartes, les images, le son, les réseaux de neurones, les agents gouvernés et la sécurité qui les entoure. Une langue, Haro, met tout cela dans une phrase. Rien sur cette page n'est cru : tout ce qui s'y trouve a été exécuté le soir de la publication.
description: La plateforme Softanza en mots simples : ce que fait le moteur, les vingt-huit domaines, la comparaison avec .NET, Python, Wolfram et la JVM, ce que veut dire une seule installation, et le code à côté de Python et JavaScript.
---

## Ce que c'est, en mots simples {#what}

La plupart des logiciels sont assemblés à partir de nombreuses bibliothèques séparées, écrites par des gens différents, chacune avec ses règles et son calendrier de versions. Softanza prend l'autre route. C'est **un seul** corps de code où chaque domaine, du comptage des lettres d'un mot arabe au dessin d'une carte du Niger ou à un agent qui propose un changement, obéit aux mêmes lois.

<p class="way"><span>La manière Softanza</span> Tout est déclaré, tout est jugé en s'exécutant, et rien n'est cru. Une page de ce site, un chapitre du cours, un garde dans le dépôt : chacun exécute son code quand on le lit ou quand on le construit. Ce qui n'a pas tourné n'est pas montré.</p>

<div class="figures">
<div class="figure"><b>28</b><span>domaines de calcul, 334 couloirs notés</span><a href="atlas.html">l'Atlas</a></div>
<div class="figure"><b>401</b><span>fichiers source du moteur Zig, 179 000 lignes</span><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/engine/src">engine/src</a></div>
<div class="figure"><b>531 000</b><span>lignes de bibliothèque, 1 227 fichiers, hors tests et archives</span><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/base">base/</a></div>
<div class="figure"><b>501</b><span>gardes narrés, 306 000 lignes de tests</span><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/base/test">base/test</a></div>
<div class="figure"><b>618</b><span>classes, 26 949 méthodes, chacune expliquée par la bibliothèque elle-même</span><a href="reference.html">la référence</a></div>
<div class="figure"><b>5 824</b><span>commits sur la branche principale depuis le 12 mars 2022</span><a href="https://github.com/mayouni/stzlib/commits/main">commits/main</a></div>
</div>

<p class="proof">Compté le 2026-10-01 dans le dépôt au commit <a href="https://github.com/mayouni/stzlib/commit/0e72e2e2c">0e72e2e2c</a> : les fichiers <code>*.ring</code> sous <code>libraries/stzlib</code> hors dossiers <code>archive</code>, séparés entre <code>base/test</code> et le reste ; les fichiers <code>*.zig</code> sous <code>engine/src</code> ; les gardes sont les fichiers de test dont le nom finit par <code>_narrated.ring</code>. Le nombre de commits est lu sur la branche principale le même jour.</p>

## Les vingt-huit domaines {#areas}

Chaque image ci-dessous a été produite par la plateforme elle-même. Cliquez un domaine pour lire ce qu'un maker en fait, un exemple exécuté, et une note honnête de chacun de ses couloirs contre les meilleurs de sa catégorie.

<!--ATLAS-WALL-->

<p class="proof">Les notes, couloir par couloir, avec les lacunes à côté des forces, sont sur <a href="atlas.html">la page de l'Atlas</a>. Atlas version 21, lu le 2026-09-30 au commit <a href="https://github.com/mayouni/stzlib/commit/0e72e2e2c">0e72e2e2c</a>.</p>

## Ce que « moteur » veut dire ici {#engine}

Sous la langue, il y a un programme écrit en Zig, un langage système, compilé en code machine. Il fait le travail lourd : il compte des caractères et non des octets, garde les entiers exacts à toute taille, dessine les images au pixel, exécute l'inférence neuronale et surveille l'horloge. La langue que vous écrivez est son visage.

Un exemple petit et réel. Le mot arabe « سلام » fait huit octets et quatre lettres. Beaucoup d'outils répondent huit. Le moteur répond quatre, et connaît l'écriture.

<div class="run"><div><div class="lbl">Softanza</div><pre>? Q("سلام").NumberOfChars()
? Q("مرحبا بالعالم").Script()
? Q(2).Power(64)
? Q("Softanza").Boxed()</pre></div><div class="out"><div class="lbl">Sortie</div><pre>4
arabic
18446744073709551616
┌──────────┐
│ Softanza │
└──────────┘</pre></div></div>
<p class="ran">exécuté le 2026-10-01 à 09:26 depuis <code>libraries/stzlib</code>, Softanza au commit 0e72e2e2c, en 6,6 secondes chargement de la bibliothèque compris</p>

<p class="way"><span>La manière Softanza</span> La substance vit dans le moteur, et la langue en est un visage. Une seconde langue, ou une seconde machine, partage le même moteur par une seule interface C : rien n'est écrit deux fois et rien ne diverge.</p>

## La langue : Haro {#haro}

Haro est la langue de la plateforme. Elle est conçue pour qu'un humain la lise comme une phrase et qu'un agent l'écrive sous une grammaire qui interdit les phrases malformées. Sa machine virtuelle à registres et son compilateur sont écrits en Zig et exécutent déjà le code de la plateforme d'aujourd'hui. Sa charte, un brouillon du 26 septembre 2026, attend la ratification de l'auteur.

<p class="proof"><span class="pill charter">en construction</span> Ce site ne dira pas que Haro est disponible avant qu'il le soit. Chaque bloc de code de ce site est du code Softanza tel qu'il tourne sur la plateforme aujourd'hui.</p>

La bibliothèque se documente elle-même : un objet connaît ses méthodes et peut expliquer chacune. Une chaîne seule répond avec 5 384 méthodes. C'est ainsi que <a href="reference.html">la référence</a> de ce site a été générée, à partir des explications de la bibliothèque et non d'un manuel écrit à la main.

<div class="run"><div><div class="lbl">Softanza</div><pre>? len( Q("Softanza").Methods() )
? Q([ 1, 2, 2 ]).Ask("how do I remove duplicates")</pre></div><div class="out"><div class="lbl">Sortie</div><pre>5384
Unique
1.10
remove duplicates / unique (engine-backed)
UniqueCS
...
RemoveDuplicates</pre></div></div>
<p class="ran">exécuté le 2026-10-01 à 09:26 et à 01:40</p>

## Le code, à côté de Python et de JavaScript {#code}

Une plateforme se juge à ce que son code a l'air et à ce qu'il répond. Quatre courtes comparaisons, chaque côté exécuté ce soir, chaque sortie telle qu'elle est sortie. Python et JavaScript sont d'excellents langages ; la question n'est pas qu'ils échouent, c'est ce qu'une ligne coûte et ce qu'elle répond.

<div class="vs">
<div class="side stz"><div class="lbl">Softanza</div><pre>? Q(2).Power(64)</pre><pre class="o">18446744073709551616</pre></div>
<div class="side other"><div class="lbl">JavaScript, Node 22</div><pre>console.log(2 ** 64);</pre><pre class="o">18446744073709552000</pre></div>
</div>
<p class="ran">Exact par défaut : un entier est exact à toute taille. Le nombre de JavaScript est un flottant 64 bits, donc les derniers chiffres sont arrondis ; <code>9007199254740993</code> s'affiche <code>9007199254740992</code>. Exécuté le 2026-10-01 à 09:26.</p>

<div class="vs">
<div class="side stz"><div class="lbl">Softanza</div><pre>o1 = new stzList([ "tea", "rice", "tea", "fish", "rice", "tea" ])
? @@( o1.FindAll("tea") )
? @@( o1.DuplicatesRemoved() )</pre><pre class="o">[ 1, 3, 6 ]
[ "tea", "rice", "fish" ]</pre></div>
<div class="side other"><div class="lbl">Python 3.13</div><pre>items = ["tea", "rice", "tea", "fish", "rice", "tea"]
print([i + 1 for i, x in enumerate(items) if x == "tea"])
print(list(dict.fromkeys(items)))</pre><pre class="o">[1, 3, 6]
['tea', 'rice', 'fish']</pre></div>
</div>
<p class="ran">Trouver d'abord, agir ensuite. La question se dit comme elle se pense : trouver tout, retirer les doublons. Les réponses de Python sont justes aussi ; elles sont construites avec des mécanismes (enumerate, les clés d'un dictionnaire) que le lecteur doit décoder. Exécuté le 2026-10-01 à 09:26.</p>

<div class="vs">
<div class="side stz"><div class="lbl">Softanza</div><pre>? Q("مرحبا بالعالم").Script()</pre><pre class="o">arabic</pre></div>
<div class="side other"><div class="lbl">Python 3.13</div><pre>import unicodedata
s = "مرحبا بالعالم"
print({unicodedata.name(c).split()[0] for c in s if not c.isspace()})</pre><pre class="o">{'ARABIC'}</pre></div>
</div>
<p class="ran">L'écriture d'un texte est une question à laquelle la plateforme répond directement. En Python on l'assemble à partir des noms Unicode de chaque caractère. Exécuté le 2026-10-01 à 09:26.</p>

<div class="vs">
<div class="side stz"><div class="lbl">Softanza</div><pre>? @@( Naturally("Create a list with [ 5, 3, 5, 1 ] and remove its duplicates").Result() )</pre><pre class="o">[ 5, 3, 1 ]</pre></div>
<div class="side other"><div class="lbl">Python 3.13</div><pre># pas d'équivalent sans un modèle de langage externe</pre><pre class="o"></pre></div>
</div>
<p class="ran">Une instruction en anglais, français, arabe ou haoussa s'exécute. La couche naturelle est fondée sur un dictionnaire et locale : pas de réseau, pas de modèle, pas de clé d'API. Exécuté le 2026-10-01 à 09:26.</p>

## Comparée aux plateformes que vous connaissez {#compare}

Softanza est faite pour se tenir à côté de .NET, de Python et de son écosystème, de la pile Wolfram et de la JVM, et non à côté d'une seule bibliothèque. La matrice ci-dessous vient de la boussole de la plateforme elle-même. Ses notes des autres sont volontairement généreuses envers eux, et les deux couloirs où Softanza est absente sont montrés dans leur couleur.

<!--COVERAGE-->

<p class="proof">Source : la boussole Softanza, section « Functional coverage against the platforms », lue sur la branche principale le 2026-09-17 ; le fichier derrière cette table est <a href="https://github.com/mayouni/stzsite/blob/main/data/coverage.json">data/coverage.json</a>. « Deep » veut dire de premier rang, souvent le meilleur de la catégorie ; « Solid » pleinement utilisable ; « Partial » présent mais partiel ou jeune ; « Absent » non couvert, ou refusé par choix.</p>

<p class="way"><span>La manière Softanza</span> Un seul arrêt. Pour couvrir ces trente lignes en Python, on assemble numpy, pandas, matplotlib, scikit-learn, nltk, cryptography, geopandas et un cadre neuronal, chacun avec son calendrier de versions et sa propre idée d'une chaîne de caractères. Ici c'est un moteur, un vocabulaire, un ensemble de lois, et un Atlas qui dit clairement où la plateforme est encore en retard.</p>

## Un dossier, copié {#install}

Il n'y a ni installateur ni registre de paquets. Le dépôt est un dossier ; le moteur est livré en bibliothèques compilées pour Windows et se construit pour Linux et macOS depuis la source. Un script placé dans le dossier de la bibliothèque charge tout en une ligne.

<pre>git clone https://github.com/mayouni/stzlib.git
cd stzlib/libraries/stzlib</pre>

La direction, dite comme une direction : un programme Haro compilé en un seul binaire statique qui emporte le moteur avec lui. Aujourd'hui la plateforme tourne depuis son dossier avec l'exécutant que le dépôt indique. <a href="start.html">La page Démarrer</a> le fait en une heure.

## Où la plateforme va ensuite {#next}

L'Atlas liste trente-six couloirs « Emerging » à côté de ses cent un « Strong », et <a href="vision.html">la page Vision</a> place la plateforme dans tout le domaine : la machine en dessous, la langue au-dessus, la couche d'intelligence à venir. Une plateforme qui montre ses lacunes est crue sur ses forces.
