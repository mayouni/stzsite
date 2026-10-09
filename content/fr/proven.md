---
title: Prouvé
title_html: <i>Prouvé</i>
kicker: Ce qui juge la fondation
lede: Une fondation est prouvée par ce qui essaie de la casser. Voici ce qui essaie, compté dans la bibliothèque, et ce qui manque.
description: Comment la fondation Softanza est prouvée : fichiers de test et gardes-scénario comptés dans la bibliothèque, cinq fuzzers, trois suites de propriétés, une porte locale et une nomenclature, avec ce qui manque dit en clair.
---

<ul class="narr">
<li><b>Tests.</b> 5 284 fichiers de test dans 158 dossiers, dont 527 gardes-scénario et 4 474 tests numérotés de la forme classique, comptés dans la bibliothèque au commit 4a184e6f0. <span class="rx-src">construit · voir <a href="depth.html">profondeur</a></span></li>
<li><b>Fuzzers et suites de propriétés.</b> Cinq fuzzers et trois suites de propriétés sur les analyseurs et la cryptographie du moteur. <span class="rx-src">construit · une lecture d'une évaluation extérieure du 2026-10-07</span></li>
<li><b>Une porte avant chaque commit.</b> Une porte de sécurité locale contrôle un changement avant qu'il soit gardé. <span class="rx-src">construit</span></li>
<li><b>Une nomenclature.</b> Un outil liste de quoi le moteur est fait, bibliothèques embarquées comprises. <span class="rx-src">construit</span></li>
<li><b>Un lecteur de tests.</b> Un exécutant qui lit chaque fichier de test comme une visite, pour dire quelles promesses il tient. <span class="rx-src">en construction</span></li>
</ul>

<p class="proof"><b>en construction</b> Ce qui manque : pas d'intégration continue hébergée, et pas d'instrument qui mesure la couverture. Cinq exécutants plus anciens n'émettent pas de verdict lisible par une machine, ce qui explique que ce site ait le sien. Un test qui passe prouve ce qu'il teste, et la page des motifs montre deux tests de la bibliothèque qui affichent maintenant la mauvaise réponse.</p>
