---
title: Par l'exemple
title_html: Par <i>l'exemple</i>
kicker: Un paradigme
lede: Montrez-le. La bibliothèque le trouve, le prouve, et garde votre exemple comme test.
description: La programmation par l'exemple dans Softanza, à trois niveaux avec une étape honnête à chacun : trouver une méthode à partir d'un exemple, induire un motif à partir d'exemples, et synthétiser une chaîne de verbes, sans que rien n'induise encore.
---

## Le sol est déjà là {#ground}

Softanza n'a pas à inventer l'exemple. La maison écrit ses tests comme un appel avec sa réponse sous une flèche, et un juge compare cette réponse avec ce qui s'est vraiment affiché. Cette forme est l'unité de promesse de la bibliothèque, et elle est déjà partout.

<!--SHOWCASE:byexample:1-->

Plus de neuf mille promesses de cette sorte se trouvent dans l'arbre de tests, les articles et les fichiers de démarrage rapide, comptées comme un marqueur de texte au commit 93d7a39 de la bibliothèque, ce qui est un décompte de promesses écrites et pas de tests qui passent. Parmi les réponses distinctes et non triviales de celles qui associent un appel à son résultat sur une seule ligne, 276 sur 299 sont promises par une seule méthode. La limite de l'idée est la couverture, 193 méthodes parmi des milliers, et pas l'ambiguïté.

## Trois niveaux {#levels}

<div class="cards">
<div class="card"><h3>Trouver <b>(chaque pièce construite, le verbe pas encore)</b></h3><p>Des paires entrent : <code>"hello"</code> vers <code>"HELLO"</code>, <code>[3, 1, 3]</code> vers <code>[3, 1]</code>. Les méthodes candidates viennent de la forme des paires confrontée aux promesses enregistrées et à la grammaire des formes ; chacune est vérifiée en l'exécutant dans un processus neuf. Aucune induction n'est nécessaire.</p></div>
<div class="card"><h3>Induire <b>(l'agent est déclaré et réservé)</b></h3><p>Des exemples qui décrivent une forme, comme <code>+216 21 298 374</code>, induisent un motif de la famille des langages de motifs. Quand il reste deux candidats, la conversation demande l'exemple qui les départage. La bibliothèque dit d'elle-même que c'est la partie pas encore construite.</p></div>
<div class="card"><h3>Synthétiser <b>(conçu)</b></h3><p>Une chaîne de deux ou trois verbes trouvée par une recherche bornée dans la grammaire des chaînes Q, jugée en l'exécutant, et racontée pas à pas comme le modèle mental raconte.</p></div>
</div>

## Ce qui existe aujourd'hui {#today}

Aujourd'hui la bibliothèque trouve une méthode à partir des mots d'un besoin, sans modèle. La trouver à partir d'un exemple du besoin est l'étape suivante, et elle n'est pas construite.

<!--SHOWCASE:byexample:2-->

## Les trois issues {#branches}

Une réponse par l'exemple est l'un des cinq registres dans lesquels la bibliothèque accepte une réponse, et elle suit le même juge que les autres : le candidat est exécuté et jugé contre les règles du monde avant de devenir connaissance. Si une lecture convient, elle est acceptée et racontée. Si plusieurs conviennent, elles sont listées et la personne choisit. Si aucune ne convient, elle est refusée avec les raisons et les alternatives les plus proches. Le protocole est raconté sur la <a href="wise.html">page du wise coding</a>, et il n'y a pas de quatrième issue.

## Ce que vous montrez, vous l'obtenez, et ce que vous obtenez est prouvé {#law}

<p class="proof"><b>conçu</b> Un candidat admis réécrit son exemple comme une promesse, un appel avec sa réponse sous une flèche, dans le fichier de l'appelant et le garde du projet, et le même juge le juge comme n'importe quel autre. Spécification, test et documentation deviennent une seule ligne. C'est une règle de la conception et elle n'est pas construite.</p>

## Ce que ce n'est pas {#not}

La programmation par l'exemple est une idée ancienne. Ce que celle-ci ajoute, c'est la façon de juger un candidat : en l'exécutant contre un vocabulaire qui se documente lui-même, et par un juge qui peut refuser. Ce que l'on trouve est un motif fermé ou une chaîne de verbes nommés, jamais du code libre, et un modèle, s'il en est utilisé un, est un générateur de candidats à l'intérieur du protocole et le dernier en ligne.

Les coûts sont nommés. Plusieurs candidats est le cas normal, c'est pourquoi la deuxième issue existe. Trois exemples peuvent coller trop bien, et le remède est la question qui départage deux candidats. L'index est aussi propre que les balises qu'il lit.

<p class="proof"><b>en construction</b> Rien n'induit encore. Les trois niveaux ci-dessus portent leur étape dans leur titre ; le reste de cette page est ce qui existe.</p>

<p class="proof">Sources : la forme de promesse est expliquée dans les articles <a href="narrations/stz-functions-as-linguistic-expressions.html">les fonctions comme expressions de la langue</a> et <a href="narrations/stz-mental-mode-narration.html">le modèle mental</a> ; le protocole de réponse est dans <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/design/SOFTANZA_INTELLIGENCE_ARCHITECTURE.md">SOFTANZA_INTELLIGENCE_ARCHITECTURE.md</a>. Les décomptes ont été faits en lisant des fichiers, pas en les exécutant.</p>
