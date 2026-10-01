---
title: Comparée
title_html: Comparée <i>aux plateformes que vous connaissez</i>
kicker: Un seul arrêt, mesuré honnêtement
lede: Trente domaines, cinq plateformes : là où Softanza est profonde, là où elle est solide, là où elle est en retard, et les deux endroits où elle est absente. Puis ce que veut dire une seule installation, et où la plateforme va ensuite.
description: Softanza face à .NET, Python, Wolfram et la JVM sur trente domaines, et ce que veut dire une seule installation.
---

## Comparée aux plateformes que vous connaissez {#compare}

Softanza est faite pour se tenir à côté de .NET, de Python et de son écosystème, de la pile Wolfram et de la JVM, et non à côté d'une seule bibliothèque. La matrice ci-dessous vient de la boussole de la plateforme elle-même. Ses notes des autres sont volontairement généreuses envers eux, et les deux couloirs où Softanza est absente sont montrés dans leur couleur.

<!--COVERAGE-->

<p class="proof">Source : la boussole Softanza, section « Functional coverage against the platforms », lue sur la branche principale le 2026-09-17 ; le fichier derrière cette table est <a href="https://github.com/mayouni/stzsite/blob/main/data/coverage.json">data/coverage.json</a>. « Deep » veut dire de premier rang, souvent le meilleur de la catégorie ; « Solid » pleinement utilisable ; « Partial » présent mais partiel ou jeune ; « Absent » non couvert, ou refusé par choix.</p>

<p class="way"><span>La manière Softanza</span> Un seul arrêt. Pour couvrir ces trente lignes en Python, on assemble numpy, pandas, matplotlib, scikit-learn, nltk, cryptography, geopandas et un cadre neuronal, chacun avec son calendrier de versions et sa propre idée d'une chaîne de caractères. Ici c'est un moteur, un vocabulaire, un ensemble de lois, et un Atlas qui dit clairement où la plateforme est encore en retard.</p>

## Un dossier, copié {#install}

Il n'y a ni installateur ni registre de paquets. Le dépôt est un dossier ; le moteur est livré en bibliothèques compilées pour Windows et se construit pour Linux et macOS depuis la source. Un script placé dans le dossier de la bibliothèque charge tout en une ligne.

<pre>git clone https://github.com/mayouni/stzlib.git
cd stzlib/libraries/stzlib</pre>

La direction, dite comme une direction : un programme Haro compilé en un seul binaire statique qui emporte le moteur avec lui. Aujourd'hui la plateforme tourne depuis son dossier avec l'exécutant que le dépôt indique. La page Démarrer le fait en une heure.

## Où la plateforme va ensuite {#next}

L'Atlas liste trente-six couloirs « Emerging » à côté de ses cent un « Strong », et la page Vision place la plateforme dans tout le domaine : la machine en dessous, la langue au-dessus, la couche d'intelligence à venir. Une plateforme qui montre ses lacunes est crue sur ses forces.
