---
title: Langages de motifs
title_html: Langages de <i>motifs</i>
kicker: Un paradigme
lede: Une seule grammaire en forme d'expression régulière, sur sept sortes de données : chaînes, listes, nombres, temps, tables, matrices et graphes, dans une bibliothèque, avec une seule habitude.
description: Les langages de motifs de Softanza : l'expression régulière élevée aux listes, nombres, temps, tables, matrices et graphes, chacun exécuté, avec les deux dont les propres tests ne passent plus dits en clair.
---

## Une grammaire, sept sujets {#seven}

L'expression régulière a été repensée la première, comme une classe, un fabricant et une bibliothèque de données. Sa grammaire, les accolades et l'arobase, a ensuite été élevée à six autres sortes de données, chacune une classe avec sa petite fonction. La même habitude vaut pour les sept : écrire le motif, demander <code>Match</code>, et demander au motif de s'expliquer.

<ol class="steps">
<li value="1"><b>Chaînes.</b> <code>rx(pat(:email))</code> <span class="rx-src">l'expression régulière, appuyée sur un moteur standard</span></li>
<li value="2"><b>Listes.</b> <code>[@N1-3, @S]</code>, et les intervalles à pas, et les listes imbriquées <span class="rx-src">Lx()</span></li>
<li value="3"><b>Nombres.</b> <code>{@Property(Even) &amp; @Property(Prime)}</code> <span class="rx-src">Nx()</span></li>
<li value="4"><b>Temps.</b> <code>{@Event(Meeting) -&gt; @Duration(30m) -&gt; @Event(Break)}</code> <span class="rx-src">Tmx()</span></li>
<li value="5"><b>Tables.</b> <code>{cols(3) &amp; unique(id) &amp; avgcol(salary:&gt;40000)}</code> <span class="rx-src">Tx()</span></li>
<li value="6"><b>Matrices.</b> <code>{shape(square) &amp; property(symmetric)}</code> <span class="rx-src">Mx()</span></li>
<li value="7"><b>Graphes.</b> <code>{@Node(start) -&gt; @Edge(flows) -&gt; @Node(done)}</code> <span class="rx-src">Gx()</span></li>
</ol>

Les motifs de cette liste sont écrits, pas exécutés. Les exécutions ci-dessous sont celles qui ont tenu leur promesse.

<!--SHOWCASE:patterns-->

## Ce qu'on peut en dire {#claim}

Les articles de la bibliothèque la comparent au domaine : Wolfram a des motifs de listes, l'unicité et les intervalles à pas ; Elixir, Haskell et Rust filtrent des structures ; des langages de requête de graphes et des langages d'événements complexes existent. Ce que les articles ne trouvent dans aucun d'eux, c'est une seule grammaire en forme d'expression régulière sur sept sortes de données dans une bibliothèque, avec la même habitude de petite fonction, la même surface Match, Explain et Debug, et la même discipline de test. C'est la lecture que la bibliothèque fait elle-même du domaine, pas une enquête.

## L'état honnête {#state}

<p class="proof"><b>en construction</b> Deux des sept exécutions ci-dessus manquent, et elles manquent parce qu'elles ont échoué. Les propres tests de la bibliothèque pour les motifs de tables et de temps promettent une correspondance et n'en affichent aucune au commit lu pour cette page. Ils sont signalés à la bibliothèque, et les deux langages sont montrés ici sans exécution. Les quantificateurs de graphes sont analysés et pas encore utilisés. L'analyseur d'expressions régulières est un nom, et les frères du Regexuter sont <a href="softanzuter.html">une vision</a>.</p>

<p class="proof">Sources : les articles <a href="narrations/stzregex-mastering-regex-with-softanza-narration.html">regex</a>, <a href="narrations/stzlistex-pattern-matching-for-lists.html">listes</a>, <a href="narrations/stznumbex-number-patterns-made-simple.html">nombres</a>, <a href="narrations/stztimex-a-pattern-language-for-time-in-softanza.html">temps</a>, <a href="narrations/stztablex-pattern-langauge-for-tables.html">tables</a> et <a href="narrations/stzmatrex-declarative-pattern-matching-for-matrices.html">matrices</a> ; les gardes des dossiers de test de la bibliothèque, liés sous chaque exécution.</p>
