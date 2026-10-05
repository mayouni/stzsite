---
title: Ce qui est prouvé, et ce qui ne l'est pas
title_html: Ce qui est <i>prouvé</i>, et ce qui ne l'est pas
kicker: Éducation · le bilan
lede: Chaque chiffre sur le système d'apprentissage de ce site vient d'un garde de la bibliothèque, nommé à côté, et chaque affirmation a sa limite à côté. Les traductions sont des brouillons, les cellules s'exécutent sur le bureau, et aucune institution ne l'a adopté. Cette page dit chacun de ces points d'abord, puis les chiffres, puis deux outils exécutés pour vous.
description: Le système d'apprentissage de Softanza, chiffre par chiffre : ce que prouve chaque garde de la bibliothèque, la limite à côté de chaque affirmation, et le bureau de l'apprenant exécuté pour de vrai.
---

## Trois limites, dites d'abord {#limits}

<div class="cards">
<div class="card"><h3>Les traductions sont des brouillons</h3><p>Aucun locuteur natif ne les a encore relues : <b>0 unité sur 35</b> en français, en arabe et en haoussa (l'exécution plus bas l'affiche). L'anglais est l'original. Chaque chapitre et chaque page de monde traduits s'ouvrent par une note dans leur langue (en français : <i>Traduction provisoire : pas encore relue par un locuteur natif</i>), jusqu'à ce qu'une validation soit enregistrée pour eux ; la page nomme alors qui l'a signée. Donc « quatre langues », ici et sur les autres pages, veut dire quatre éditions, dont trois pas encore lues par un locuteur natif.</p></div>
<div class="card"><h3>Les cellules s'exécutent sur le bureau</h3><p>Le lecteur est une page qui s'ouvre dans n'importe quel navigateur, mais ses cellules s'exécutent sur le bureau, et la page le dit sur chaque cellule. Les exécuter dans le navigateur dépend du moteur navigateur de Softanza et n'est pas construit. Chaque chiffre ci-dessous a été mesuré sur le bureau.</p></div>
<div class="card"><h3>Aucune institution ne l'a adopté</h3><p>Une banque et une université existent dans la bibliothèque comme deux <i>surcouches de référence</i>, écrites pour montrer ce qu'est une surcouche. Ce ne sont pas des clients, et ce site ne nomme aucune institution comme telle. L'auteur n'a pas choisi de première institution.</p></div>
</div>

Deux choses encore, en mots simples. Le tuteur est **fondé sur des règles** : il n'utilise aucun modèle de langage, et ce site ne l'appelle pas IA. Et la licence est celle du dépôt, MIT, décidée le 2026-10-05 sur délégation de l'auteur (section 8 de la charte) : l'auteur peut la remplacer avant la livraison d'une première institution.

## Les chiffres, chacun à côté de son garde et de sa limite {#figures}

Mesurés par les auteurs du module le 2026-10-05, dans une copie neuve de la bibliothèque au commit 4a184e6f0. Un **garde** est un fichier de la bibliothèque qui s'exécute et affiche combien de ses assertions ont tenu. Ce site n'a pas rejoué les quatorze gardes, qui prennent une vingtaine de minutes ensemble ; il a rejoué deux outils, le bureau de l'apprenant et la fiche du relecteur, montrés plus bas.

<div class="lanes rtable">
<div class="lane lane2"><div class="ln">Le cours</div><div class="lt"><b>L'Introduction élémentaire : 15 chapitres en anglais, français, arabe et haoussa, soit 60 éditions. Chaque cellule s'est exécutée, chaque promesse a tenu, aucune sortie n'est conservée.</b> Garde <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/education/course_narrated.ring">course_narrated</a>, 249 assertions. <b>À côté :</b> le français, l'arabe et le haoussa sont des brouillons, 0 unité sur 35 relue ; les cellules s'exécutent sur le bureau.</div></div>
<div class="lane lane2"><div class="ln">Les exercices</div><div class="lt"><b>23 exercices qui se prouvent eux-mêmes :</b> chacun refuse ses mauvaises réponses et accepte ses bonnes, en les exécutant. Le même garde. <b>À côté :</b> ils sont vérifiés sur le bureau ; les énoncés en français, arabe et haoussa sont des brouillons.</div></div>
<div class="lane lane2"><div class="ln">Les mondes</div><div class="lt"><b>3 mondes d'enseignement</b> (un restaurant, une coopérative, une école), <b>une page chacun en 4 langues : 12 pages.</b> Gardes <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/education/worlds_narrated.ring">worlds_narrated</a>, 26 assertions, et <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/education/world_pages_narrated.ring">world_pages_narrated</a>, 45. <b>À côté :</b> les neuf pages en français, arabe et haoussa sont des brouillons.</div></div>
<div class="lane lane2"><div class="ln">Compétences et niveaux</div><div class="lt"><b>25 compétences en 7 familles, et 5 niveaux, chacun gagné par un dossier de projet qui passe son garde.</b> Gardes <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/education/spine_narrated.ring">spine_narrated</a>, 33, et <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/education/levels_narrated.ring">levels_narrated</a>, 35. <b>À côté :</b> la formulation des compétences en français, arabe et haoussa est un brouillon ; aucune institution n'a adopté le système.</div></div>
<div class="lane lane2"><div class="ln">Le tuteur</div><div class="lt"><b>Il pose la question ouverte, refuse d'écrire la réponse, et n'explique jamais un chapitre en avance sur l'apprenant, en 4 langues ; aucun modèle de langage.</b> Gardes <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/education/tutor_narrated.ring">tutor_narrated</a>, 45, <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/education/tutor_gaps_narrated.ring">tutor_gaps_narrated</a>, 31, et <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/education/slice_narrated.ring">slice_narrated</a>, 68. <b>À côté :</b> il est fondé sur des règles, pas une IA ; ses textes en français, arabe et haoussa sont des brouillons.</div></div>
<div class="lane lane2"><div class="ln">Les institutions</div><div class="lt"><b>Une surcouche (son monde, ses exercices, ses règles et son nom) passe un tribunal ; il y a deux surcouches de référence, celle d'une banque et celle d'une université ; les étapes du guide sont exécutées par un garde.</b> Garde <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/education/institution_narrated.ring">institution_narrated</a>, 39. <b>À côté :</b> aucune institution ne l'a adopté ; les deux surcouches sont des références, pas des adoptantes.</div></div>
<div class="lane lane2"><div class="ln">La propriété</div><div class="lt"><b>La progression est un fichier texte dans le dossier de l'apprenant, et une réussite porte l'empreinte de ce qui a été exécuté.</b> Gardes <code>slice_narrated</code>, ci-dessus, et <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/education/desk_narrated.ring">desk_narrated</a>, 24. <b>À côté :</b> le vérificateur s'exécute sur le bureau.</div></div>
<div class="lane lane2"><div class="ln">La démonstration</div><div class="lt"><b>Quinze minutes, huit scènes, 20 affirmations prouvées.</b> Garde <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/education/demo_narrated.ring">demo_narrated</a>, 17 assertions ; le guide du présentateur est <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/demo/DEMO.md">DEMO.md</a>. <b>À côté :</b> elle tourne sur un seul ordinateur, hors ligne, sur le bureau ; le français, l'arabe et le haoussa qu'elle montre sont des brouillons.</div></div>
<div class="lane lane2"><div class="ln">L'ensemble</div><div class="lt"><b>14 gardes racontés, 716 assertions, exécutés dans une copie neuve en une vingtaine de minutes.</b> Les fichiers sont dans <a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/base/test/education">test/education</a>. <b>À côté :</b> ils ont été exécutés par les auteurs du module ; ce site ne les a pas rejoués.</div></div>
<div class="lane lane2"><div class="ln">La page du lecteur</div><div class="lt"><b>Tout, 15 chapitres et 3 mondes (72 éditions), construit en une seule page HTML en une centaine de secondes.</b> Outil <code>build_reader.ring</code>, garde <code>desk_narrated</code>. <b>À côté :</b> la page s'ouvre partout, ses cellules s'exécutent sur le bureau, et chaque brouillon le dit.</div></div>
</div>

## Le bureau de l'apprenant, exécuté pour de vrai {#runs}

Le bureau de l'apprenant est une commande de la bibliothèque, lancée depuis son dossier avec le dossier d'un apprenant et un verbe. Tout ce qui suit a été exécuté par ce site, sur la bibliothèque au commit 4a184e6f0, dans un dossier d'apprenant temporaire qui n'est pas celui de la bibliothèque.

Un apprenant qui vient de commencer est au chapitre 1 et n'a rien réussi. Le bureau dit où il en est, et ce que le premier niveau demande encore : quatre exercices et un projet, puis les niveaux suivants.

<!--EDUREC:status-->

Une mauvaise réponse à l'exercice 1.1 est refusée. Le vérificateur a exécuté le fichier dans un processus neuf et dit ce qu'il a affiché ; il ne dit pas ce qu'il aurait dû afficher.

<!--EDUREC:refused-->

Une bonne réponse passe. Le verdict est celui du vérificateur : il a exécuté le fichier, et personne ne l'a lu. L'apprenant est maintenant au chapitre 2 et un exercice plus près du premier niveau, avec quatre manquants au lieu de cinq.

<!--EDUREC:passed-->

<!--EDUREC:status2-->

Au chapitre 2, l'apprenant demande quelque chose qu'il n'a pas atteint. Le tuteur nomme le chapitre à venir, n'en explique rien, et interroge sur l'exercice en cours. Il est fondé sur des règles : ni modèle de langage, ni réseau.

<!--EDUREC:tutor-->

Interrogé en français, en arabe ou en haoussa, le tuteur répond dans cette langue, et ces réponses sont des brouillons comme les chapitres. Combien d'unités un locuteur natif a relues est un nombre que la bibliothèque affiche, et aujourd'hui il est nul :

<!--EDUREC:review-->

## Comment un brouillon cesse d'en être un {#reviews}

La définition d'une **unité** par la bibliothèque elle-même : un chapitre avec ses exercices, une page de monde, les compétences, ou les textes du tuteur. Le français, l'arabe et le haoussa en ont chacun 35. Une unité cesse d'être un brouillon quand la validation d'un locuteur natif est enregistrée pour elle dans un fichier nommé d'après la langue ; la page retire alors l'avis et nomme qui l'a signée. Le relecteur n'a pas besoin de connaître Softanza ni Git : la fiche est un seul fichier texte avec tout ce qu'il faut lire, et dit ce qu'il faut juger (la formulation) et ce qu'il ne faut pas toucher (le code des cellules, et chaque ligne qui commence par <span class="mono">#--&gt;</span>, qu'un garde vérifie en l'exécutant).

Si vous lisez le français, l'arabe ou le haoussa comme votre propre langue et voulez relire une unité, ouvrez une issue sur le dépôt de la bibliothèque et demandez la fiche. Le zarma n'est pas une langue du cours ; une édition zarma est une invitation, comme le dit la <a href="education.html#missing">page Éducation</a>.

## Ce que cette page n'affirme pas {#claims}

Que le cours soit disponible en quatre langues relues ; qu'il tourne dans le navigateur ; qu'une institution l'utilise ; que le tuteur soit une IA ; que les chiffres ci-dessus aient été re-mesurés par ce site, hormis ce que les deux outils ci-dessus ont affiché. Là où le site dit « quatre langues » ailleurs, lisez-le avec la première limite de cette page à côté.

<p class="proof">La conception et son journal, ligne par ligne : <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/CHARTER.md">CHARTER.md</a> (neuf lois, chacune avec le test qui la fait respecter), <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/SOFTANZA_EDUCATION_PLAN.md">SOFTANZA_EDUCATION_PLAN.md</a> (chaque phase et ce qu'elle n'affirme pas), <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/OVERLAY_GUIDE.md">OVERLAY_GUIDE.md</a>. Retour à <a href="education.html">Éducation</a>.</p>
