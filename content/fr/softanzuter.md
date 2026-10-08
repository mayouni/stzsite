---
title: Le Softanzuter
title_html: Le <i>Softanzuter</i>
kicker: Un paradigme
lede: Pas de l'informatique réactive sur une machine abstraite. Une façon de programmer de façon déclarative des disciplines complexes : des motifs liés à du code, des facultés qui partagent un état, et un esprit construit dessus.
description: Le paradigme du Softanzuter : une définition, une échelle de quatre échelons du motif à l'agent, deux moteurs qui tournent, un moteur universel prévu et les frères qui restent une vision, chacun avec son étape.
---

## La définition {#definition}

Les documents de conception de la bibliothèque la définissent dans les mots de l'auteur, repris et rendus mécaniques :

> Un Softanzuter est la représentation computationnelle d'une machine pensante, fondée sur un ou plusieurs Regexuters, qui lui permet de reconnaître des motifs de pensée et d'y réagir.

L'unité est le motif. Un motif sur n'importe quel support est lié à du code. Le déclencher est la réaction. L'état que le déclenchement écrit est lui-même un support sur lequel d'autres motifs se déclenchent, et chaque déclenchement garde sa provenance, la réponse à pourquoi. C'est ce qui le sépare d'un flux de données qui traverse le temps.

## L'échelle {#ladder}

<ol class="steps">
<li value="0"><b>Le motif.</b> Reconnaissance pure sur un support : une chaîne, une liste, un nombre, une matrice, une table, un temps, un graphe. Il ne fait rien. <span class="rx-src">construit · six langages de motifs dans la bibliothèque</span></li>
<li value="1"><b>Le Regexuter, et ses frères sur d'autres supports.</b> Un arc réflexe : des motifs liés à du code, un moteur par support. On lui donne des données, il déclenche ce qui correspond et enregistre un état avec son heure, son ordre, la correspondance et la valeur calculée. Une faculté, pas un esprit. <span class="rx-src">construit · un Regexuter et un Listexuter tournent</span></li>
<li value="2"><b>Le Softanzuter.</b> Plusieurs Xuters qui partagent un état et enchaînent jusqu'à un point fixe : l'état qu'une faculté écrit est un support sur lequel les autres se déclenchent. <span class="rx-src">conçu, pas construit · aujourd'hui chaque déclencheur part une fois et les Xuters ne partagent pas un état</span></li>
<li value="3"><b>L'agent.</b> Un Softanzuter incarné dans un monde, avec un but, une mémoire, des outils et une responsabilité. Les agents contiennent des Softanzuters, les Softanzuters contiennent des Xuters. <span class="rx-src">construit · l'enchaînement ci-dessous s'exécute</span></li>
</ol>

## Échelon 1, exécuté {#rung1}

<!--SHOWCASE:softanzuter:1-->

## Échelon 3, exécuté {#rung3}

L'agent ci-dessous garde sa mémoire sous forme de faits, et trois compétences s'enchaînent : une commande passée est cuisinée, puis dressée, puis servie. Le résultat de chaque compétence est un fait sur lequel la suivante se déclenche, et l'agent continue jusqu'à ce que plus rien ne change.

<!--SHOWCASE:softanzuter:2-->

<p class="way"><span>La manière Softanza</span> L'esprit est programmatique par défaut, et un modèle est une faculté parmi les autres, jamais la définition de l'esprit. La boucle de l'industrie, un modèle qui appelle des outils, est le cas particulier de cette échelle : une faculté, aucune gouvernance. Softanza offre le cas général, en local.</p>

## Ce qui reste une vision {#vision}

<div class="cards">
<div class="card"><h3>Le moteur universel <b>(prévu)</b></h3><p>N'importe quel langage de motifs devient un support de calcul, avec une seule interface pour ajouter des déclencheurs et des calculs, traiter des données et lire les dépendances. C'est l'un des douze moteurs de paradigme de la conception du moteur.</p></div>
<div class="card"><h3>Le Regexuter génétique <b>(vision)</b></h3><p>Fait évoluer une population de motifs contre un critère d'adaptation. Son but a été trouvé plus tard : induire un motif à partir d'exemples, ce dont <a href="byexample.html">répondre par l'exemple</a> a besoin.</p></div>
<div class="card"><h3>Le Regexuter quantique <b>(vision)</b></h3><p>Tient un motif dans plusieurs états à la fois, chaque lecture pondérée et classée. Son but : l'espace des solutions du même protocole, quand plusieurs réponses sont acceptables.</p></div>
<div class="card"><h3>Le Regexuter linguistique <b>(vision)</b></h3><p>Prend des règles de grammaire pour déclencheurs.</p></div>
</div>

## Un mot, trois sens {#word}

Dans la conception, le Softanzuter est le support universel de l'échelon 2. Dans le moteur tel que construit, le module qui porte le nom est le substrat de l'agent, ses emplacements et ses boîtes aux lettres bornées, qui est le corps de l'échelon 3 et rien de l'enchaînement de l'échelon 2. Dans l'architecture de l'intelligence, c'est la machine pensante de plusieurs Xuters. Les trois sont une seule échelle lue de trois côtés, et l'échelle ci-dessus montre comment elles s'emboîtent.

<p class="proof"><b>en construction</b> L'échelon 2 est le maillon manquant : l'enchaînement jusqu'au point fixe et l'état partagé ne sont pas construits, et les deux moteurs de l'échelon 1 tournent chacun seul. Une narration du Regexuter est publiée avec son code, et une partie ne se compile pas : ses derniers blocs sont le pseudo-code des frères. C'est pourquoi cette page raconte les frères comme une vision.</p>

<p class="proof">Sources : l'article <a href="narrations/stzregexuter-regex-as-computational-reactive-medium.html">le Regexuter comme support de calcul réactif</a> ; les gardes <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/regexuter/06_computing_multiple_triggers.ring">06_computing_multiple_triggers.ring</a> et <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/agentic/piagent_narrated.ring">piagent_narrated.ring</a> ; l'échelle est dans <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/design/SOFTANZA_INTELLIGENCE_ARCHITECTURE.md">SOFTANZA_INTELLIGENCE_ARCHITECTURE.md</a>.</p>
