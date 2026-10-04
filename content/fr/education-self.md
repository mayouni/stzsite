---
title: Apprendre seul
title_html: <i>J'apprends</i> seul
kicker: Éducation · le chemin, le bureau, l'échelle
lede: Il vous faut un ordinateur portable, la bibliothèque et un après-midi. Le chemin va d'une première phrase à un projet qui gagne un niveau, dans votre langue, avec un tuteur qui pose des questions quand vous êtes bloqué. Personne ne vous note : c'est votre propre programme qui est exécuté.
description: Apprendre Softanza seul : les quinze chapitres, le bureau de l'apprenant, les cinq niveaux gagnés par des projets, et un tuteur qui questionne.
---

## Le chemin {#path}

Les quinze chapitres du livre sont une seule histoire, racontée en cellules que vous pouvez exécuter. Lisez une cellule, exécutez-la, changez-la, exécutez-la encore. Les quatre premiers chapitres donnent tout le modèle mental ; les autres l'élargissent.

<ol class="narr">
<li>Trouver, puis agir</li><li>Une première phrase</li><li>Lire le nom comme une phrase</li><li>Le dire dans votre langue</li><li>Un objet, toute structure</li><li>Parcourir, demander, produire, agir</li><li>Déclarer quoi, pas comment</li><li>Motifs dans le texte</li><li>Motifs dans la structure</li><li>Quand le code rencontre les cellules</li><li>Dessiner la réponse</li><li>Enseigner un monde</li><li>La question de l'écart</li><li>Un agent qui ne peut pas nuire</li><li>Écrire une narration</li>
</ol>

<p class="proof">Ouvrez <a href="../reader.html">le livre interactif</a>, ou lisez <a href="book.html">la page du livre</a> : chaque chapitre a une <a href="book.html#proof">page de preuve</a> qui consigne son exécution, cellule par cellule, dans ses quatre éditions. Au chapitre 12 vous construisez un monde à vous, et au chapitre 15 vous écrivez un chapitre.</p>

Vous choisissez trois choses, et pouvez en changer à tout moment : **la langue** des chapitres, du vérificateur et du tuteur (anglais, français, arabe, haoussa) ; **le monde** sur lequel les exemples raisonnent (un restaurant, une coopérative ou une école) ; et **le rythme**. Le modèle mental en cinq questions est sur la <a href="learn.html">page Apprendre</a>.

## Le bureau {#desk}

Le bureau de l'apprenant est un seul outil de la bibliothèque, <span class="mono">learn.ring</span>, lancé depuis son dossier avec votre dossier et un verbe. Il dit où vous en êtes, juge un programme que vous avez écrit, répond à une question comme le ferait un tuteur, et juge le projet qui gagne un niveau. Chaque verdict est celui du vérificateur : il a **exécuté** votre fichier dans un processus neuf, et personne ne l'a lu.

<pre>learn.ring  &lt;votre dossier&gt; status
learn.ring  &lt;votre dossier&gt; submit &lt;id de l'exercice&gt; &lt;votre fichier&gt;
learn.ring  &lt;votre dossier&gt; ask &lt;id de l'exercice&gt; "&lt;votre question&gt;"
learn.ring  &lt;votre dossier&gt; project &lt;id du projet&gt;

options :  --lang en|fr|ar|ha   --world workplace|cooperative|school   --overlay &lt;dossier&gt;</pre>
<p class="proof">L'usage tel que la bibliothèque l'écrit : <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/tools/learn.ring">education/tools/learn.ring</a>. Le code de sortie est 0 quand une soumission a réussi et 2 quand elle a été refusée.</p>

Un exercice est une courte tâche avec une promesse : les lignes que votre programme doit afficher. Voici le premier du cours :

<pre>La cuisine a reçu ces commandes aujourd'hui :

    [ "tea", "rice", "tea", "fish", "rice", "tea" ]

Affichez la liste des plats à cuisiner, chacun une seule fois, dans l'ordre
où il a été commandé la première fois.

PROMESSE   [ "tea", "rice", "fish" ]</pre>

Votre réponse est vérifiée en l'exécutant. Une réponse connue pour être fausse échoue et une réponse connue pour être juste passe : l'exercice n'entre dans le cours que si l'on a vu les deux le faire.

## Le tuteur {#tutor}

Quand vous êtes bloqué, vous demandez. Le tuteur répond par une question sur l'écart entre ce que vous avez écrit et ce que l'exercice demande. C'est un programme de la bibliothèque, avec trois règles qu'il ne peut pas enfreindre : il n'écrit pas votre code, il n'explique pas ce que vous n'avez pas encore rencontré, et il ne donne pas la réponse avant que vous ayez essayé.

<pre>Moussa : « Je ne comprends rien. Donne-moi juste la réponse. »
Tuteur :  Je n'écrirai pas la réponse à votre place : c'est la seule chose qu'un tuteur ne doit jamais faire.
          Essayez d'abord. Écrivez votre tentative et soumettez-la ; je vous dirai alors ce qui manque
          encore, sous forme de question.
Moussa : « Qu'est-ce qui me manque ? »
Tuteur :  Où sont les éléments répétés ? Quelle ligne de votre programme demande leurs positions ?
          (pourquoi : le modèle mental trouve avant d'appliquer)
PROUVÉ    aucune réponse ne contient une méthode de la solution, ni la solution elle-même
PROUVÉ    le tuteur a trouvé l'étape manquante par du codage sage, sans deviner
PROUVÉ    aucun modèle de langage n'a été utilisé</pre>
<p class="ran">exécuté le 2026-09-30 à 23:10, la démonstration d'éducation, scène 4</p>

Si vous ne connaissez pas un nom de la bibliothèque, demandez plutôt à la bibliothèque : un objet répond à <span class="mono">Ask("how do I remove duplicates")</span> par les méthodes qui le font. <a href="ask.html">Interroger la bibliothèque</a>.

## L'échelle {#ladder}

Vous ne passez pas d'examen. Un niveau se gagne par un **projet** que vous construisez dans votre propre dossier, et un garde le juge : il exécute le projet, dit quelles promesses sont tenues, et quand l'une ne l'est pas, dit pourquoi en mots.

<div class="cards">
<div class="card"><h3>S0 · Explorateur</h3><p>Après le chapitre 4. <b>Projet :</b> une narration de cinq cellules sur une liste à vous, où chaque cellule s'exécute et porte une promesse qui tient.</p></div>
<div class="card"><h3>S1 · Constructeur</h3><p>Après le chapitre 7. <b>Projet :</b> un petit outil sur votre lieu de travail, ses conditions déclarées comme des données (une règle comme <span class="mono">{ @item &gt; 20 }</span> dans un fichier), et non écrites dans le code.</p></div>
<div class="card"><h3>S2 · Artisan</h3><p>Après le chapitre 11. <b>Projet :</b> un rapport sur un vrai fichier de données, avec les motifs qu'il trouve, un tableau et une image.</p></div>
<div class="card"><h3>S3 · Architecte</h3><p>Après le chapitre 14. <b>Projet :</b> un monde que vous avez enseigné, d'au moins cinq faits, interrogé par un agent que vous gouvernez, admis par le tribunal, dont chaque acte peut être annulé.</p></div>
<div class="card"><h3>S4 · Maître</h3><p>Chapitre 15. <b>Projet :</b> un nouveau chapitre pour ce cours, en deux langues, dont le garde est vert.</p></div>
</div>

<p class="proof">Le projet de chaque barreau est jugé par un garde, montré exécuté sur un échantillon faux et un échantillon juste : <a href="learn.html#ladder">l'échelle sur la page Apprendre</a>. Où vous en êtes est nommé par la bibliothèque sur votre machine, à partir des preuves de votre dossier ; ce site ne voit pas ce dossier.</p>

## Quand vous avez fini {#end}

Vous avez un dossier de texte brut qui est à vous : vos programmes, et un fichier de progression qui consigne chaque fait avec sa preuve. Emportez-le sur l'ordinateur suivant, gardez-le dans un dépôt, montrez-le à un employeur. L'étape suivante est l'autre porte : <a href="education-teach.html">enseigner ce que vous avez appris</a>, c'est-à-dire les chapitres 12 et 15 tournés vers les autres.
