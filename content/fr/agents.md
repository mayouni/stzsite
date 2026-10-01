---
title: Pour les agents
title_html: Pour <i>les agents</i>
kicker: Comment une machine lit Softanza
lede: Cette section s'adresse aussi à un agent qui lit ce site. Softanza est conçue pour être lue par une machine autant que par un humain.
description: Comment un agent lit Softanza : demander à la bibliothèque, se déclarer dans un fichier d'agent, parler la grammaire.
---

<div class="cards">
<div class="card"><h3>Demandez à la bibliothèque</h3><p>La bibliothèque se documente elle-même. Un objet répond à <code>Ask()</code> par ses propres méthodes, explique chacune par <code>ExplainMethod()</code>, et dit comment par <code>HowTo()</code>. Un agent n'a pas besoin de deviner un nom.</p><div class="run"><div><div class="lbl">Softanza</div><pre>? Q([ 1, 2, 2 ]).Ask("how do I remove duplicates")</pre></div><div class="out"><div class="lbl">Sortie</div><pre>Unique
1.10
remove duplicates / unique (engine-backed)
UniqueCS
...
RemoveDuplicates</pre></div></div><p class="ran">exécuté le 2026-10-01 à 01:40</p></div>
<div class="card"><h3>Déclarez-vous dans un fichier d'agent</h3><p>Un agent est un fichier, jugé au chargement : ce qu'il couvre, la classe de réversibilité de ses actes, la posture d'exécution de chaque fonction qu'il appelle. Le tribunal refuse en phrases fixes, les mêmes aux deux portes.</p><pre>A bank analyst declares a stock-watcher agent,
first without saying what it covers:
-> refused / [pia-coverage @ coverage]
   an agent must say WHAT IT COVERS.
...then with its coverage stated:
-> The court judged your declaration,
   and every promise of the exercise was kept.</pre><p class="ran">exécuté le 2026-09-30 à 23:10, démonstration, scène 7</p></div>
<div class="card"><h3>Parlez la grammaire, pas du code général</h3><p>Une langue déclarée émet sa grammaire de contrainte ; un modèle dont l'échantillonneur y est contraint ne peut émettre que des phrases valides. C'est le contrat C9 de la plateforme : la structure tue la malformation, jamais la fausseté.</p><p class="proof"><a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/design/SOFTANZA_INTELLIGENCE_ARCHITECTURE.md">SOFTANZA_INTELLIGENCE_ARCHITECTURE.md</a></p></div>
</div>
