---
title: Enseigner, ou concevoir des cours
title_html: <i>J'enseigne</i>, ou je conçois des cours
kicker: Éducation · une cohorte, un exercice, un chapitre à vous
lede: Un enseignant utilise Softanza pour proposer des exercices vérifiés en les exécutant, pour suivre une cohorte par un rapport qui est lui-même une narration, et pour accompagner là où un programme ne le peut pas. Un concepteur de cours écrit des chapitres en texte brut dont toutes les cellules s'exécutent. Voici chaque étape, exécutée.
description: Enseigner avec Softanza : former une cohorte, proposer des exercices jugés par l'exécution, lire le rapport d'une cohorte, et écrire un cours.
---

## Ce que fait un enseignant, dans l'ordre {#steps}

1. **Choisir le cours et le monde.** La bibliothèque porte aujourd'hui quatre cours (l'introduction élémentaire, neuf missions situées à Zindara, les agents gouvernés, les mathématiques) et trois mondes sur lesquels les exemples raisonnent : un restaurant, une coopérative, une école. Une institution peut poser son propre monde sur chacun : <a href="education-programme.html#overlay">la surcouche</a>.
2. **Former une cohorte.** Une cohorte est un dossier avec un fichier de trois lignes : son nom, le cours qu'elle suit et, s'il y en a une, la surcouche sous laquelle elle vit. Chaque apprenant est un dossier à l'intérieur, qui contient son travail et sa progression.
3. **Proposer des exercices.** Le cours en contient déjà 23. Les vôtres ont la même forme : une tâche dans chaque langue, une promesse, au moins une réponse connue pour être fausse et une pour être juste.
4. **Les apprenants soumettent.** Le vérificateur exécute chaque soumission dans un processus neuf et écrit le verdict dans le dossier de l'apprenant. Personne ne lit le code pour le comparer à un corrigé.
5. **Lire le rapport.** Un appel écrit le rapport de progression de la cohorte. Le rapport est une narration : chaque chiffre est une promesse à côté de la cellule qui le calcule.
6. **Accompagner.** Le tuteur pose la question qui manque à l'apprenant ; il ne donne jamais la réponse. Ce qu'un programme ne peut pas faire est à vous : la salle, l'encouragement, la deuxième explication, la décision d'avancer.

## Une cohorte, exécutée {#cohort}

<!--EDU:cohort-->

Le fichier de la cohorte est celui de trois lignes que décrit le guide, et `AddLearner` a créé un dossier pour chaque apprenant dessous. Rien d'autre n'a été installé.

## Un exercice est une promesse {#exercise}

Un exercice est une courte tâche et les lignes que le programme de l'apprenant doit afficher. Il n'entre dans le cours que lorsqu'une réponse connue pour être fausse a été vue échouer et une réponse connue pour être juste a été vue passer, et les deux sont exécutées de nouveau chaque fois que le cours est vérifié.

<!--EDU:exercise-->

Le premier 0 est la réponse connue pour être fausse, refusée ; le 1 est la réponse connue pour être juste, acceptée. Le même appel juge le fichier d'un apprenant, dans la langue de l'apprenant, et c'est ce qu'exécute le vérificateur.

## Le rapport est une narration {#report}

<!--EDU:report-->

Sous le tableau, une cellule par apprenant calcule la ligne de cet apprenant, avec une promesse dessous. Exécutez de nouveau le fichier par la bibliothèque et elle dit s'il est encore vrai : quand un autre apprenant réussit, l'ancien rapport signale lui-même qu'il est périmé, et un rapport régénéré tient. Un enseignant garde le rapport comme un fichier, dans un dépôt s'il le veut, et il ne devient jamais faux en silence.

## Concevoir un cours {#design}

Un chapitre est un fichier de texte brut, <span class="mono">NN-slug.fr.md</span>, au format de narration de la maison : de la prose et des cellules, chaque cellule suivie des lignes qu'elle doit afficher. Une sortie conservée est refusée au chargement du cours, parce qu'une sortie conservée peut être fausse. Un chapitre se termine par un récapitulatif en trois parties : ce qui a été accompli, pourquoi cela compte, ce qui vient ensuite. Le même chapitre a une édition par langue, et une édition manquante est un garde en échec.

<div class="cards">
<div class="card"><h3>Intégré</h3><p class="stage">construit</p><p><b>Vingt-cinq compétences en sept familles</b> (formuler, exprimer, motifs, voir, savoir, gouverner, façonner), chacune à trois niveaux, Fondation, Praticien, Expert, avec un champ de preuve nommant le garde qui prouve chaque niveau. <b>Trois étapes</b> : Rencontre, Expression, Gouvernance. <b>Cinq profils</b> (jeune, étudiant, professionnel, designer, décideur) qui changent la profondeur et les exemples, pas seulement une note. <b>Les missions</b> situées à Zindara, au Niger, pour que chaque pas exécute du vrai code. <b>Construit, pas testé</b> : un niveau se gagne par un projet qui passe ses gardes, jamais par un examen.</p></div>
<div class="card"><h3>Refusé, avec la raison</h3><p>Un dialecte doux dont on exporterait : inutile, parce que les chaînes quasi naturelles et les instructions dans votre langue sont Softanza même. Les points d'expérience et les classements : une réussite est une preuve, pas un score. Un certificat par examen ou un titre signé : l'empreinte du travail remis le remplace. Un tuteur à modèle de langage : refusé par la loi ; le tuteur tourne sur la couche naturelle.</p></div>
<div class="card"><h3>Proposé</h3><p class="stage">proposé</p><p><b>La révélation progressive</b> : une notion n'apparaît que quand le travail précédent de l'apprenant montre qu'il est prêt, jugé par les gardes. Elle demande la progression de l'apprenant, que seul le lecteur de bureau peut voir : c'est à la bibliothèque de la construire. Deux voisines sont construites : <b>l'échelle toujours visible</b> (chaque chapitre du lecteur nomme son barreau) et <b>de la cellule à sa preuve</b> (chaque cellule mène à son exécution).</p></div>
</div>

<p class="way"><span>La manière Softanza</span> Le récit avant la syntaxe ; une idée à la fois ; les erreurs comme information sur ce qui reste à déclarer ; déclarer, puis voir.</p>

<p class="proof">Le guide de la bibliothèque pour ceux qui écrivent des cours : <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/CHARTER.md">CHARTER.md</a>. Ensuite, la porte de l'institution : <a href="education-programme.html">une surcouche, des cohortes, la propriété</a>.</p>
