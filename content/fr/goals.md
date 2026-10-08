---
title: Sept buts de conception
title_html: Sept <i>buts de conception</i>
kicker: Pourquoi une fonction existe
lede: Une fonction qui ne sert aucun but est refusée, et un but sans fonction est un trou. Sept buts tiennent ensemble la conception de Softanza depuis 2022. Cette page place chacun face aux fonctions qui le servent, avec l'état de chacune aujourd'hui.
description: Les sept buts de conception de Softanza, expressivité, flexibilité, fiabilité, cohérence, métaphores centrées sur l'humain, abstractions pratiques et gouvernabilité, chacun avec ses fonctions, leur état aujourd'hui et une exécution.
---

Quatre vocabulaires racontent la conception de Softanza, et ils répondent à quatre questions différentes. Un but dit <b>pourquoi</b> une fonction existe. Un principe dit <a href="principles.html">ce que Softanza croit</a>. Une convention dit <a href="craft.html">comment le code s'écrit</a>. Une loi dit ce que l'arbre refuse. Cette page est la première : la raison, qu'un relecteur peut lire but par but au lieu de ligne par ligne.

La diapositive de 2022 plaçait sept buts face à trente-trois fonctions. Les voici redessinés avec l'état de chaque fonction aujourd'hui, et une exécution par but.

<!--GOALS-->

## Ce que dit le décompte {#tally}

Le squelette a tenu : la plupart des fonctions existent comme déclaré, et celles qui ont changé l'ont fait pour des raisons dites, comme le langage hôte qui passe à Haro. La gouvernabilité est le but qui a le plus dérivé. Sa pile d'appels visualisée est un nom et rien n'a été construit dessous, et les formes décoratives de la mise en cache et de la journalisation ont cédé la place à des classes. Une conception qui a dérivé mérite une décision et pas un remplacement silencieux : soit les décorateurs reviennent comme des balises que le moteur honore, soit la forme par classes est déclarée finale et ce tableau est amendé. Cette décision revient à l'auteur.

<p class="proof"><b>en construction</b> Les décomptes ont été lus dans les fichiers de la bibliothèque au commit 93d7a39 par une évaluation extérieure le 2026-10-07 : une définition trouvée par son nom compte comme construite, et aucune fonction n'a été exécutée pour le décompte. Les buts sont écrits dans des milliers de balises de commentaire au-dessus des définitions de méthodes, en une quatre-vingtaine d'orthographes, et aucun contrôle ne les lit encore. Un juge qui le fait, et qui imprime ce tableau depuis le code, est spécifié et pas construit.</p>
