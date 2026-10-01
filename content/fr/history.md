---
title: Depuis les principes
title_html: Depuis <i>les premiers principes</i>
kicker: Sur GitHub depuis le 12 mars 2022
lede: Softanza n'a pas commencé comme une enveloppe autour de bibliothèques existantes. Elle a commencé par la question de ce que programmer devrait être quand l'humain est l'analyseur, et elle a reconstruit le texte, les nombres, les listes, les tables, les erreurs et la documentation à partir de là. La mission n'a pas bougé depuis 2018 ; le dépôt est public depuis le 12 mars 2022.
description: Les années de travail de Softanza depuis les premiers principes, comptées dans le dépôt.
---

<figure class="diagram"><img src="../assets/img/diagrams/trajectory-fr.png" alt="Commits par an sur la branche principale : 136 en 2022, 390 en 2023, 1 171 en 2024, 935 en 2025, 3 192 en 2026 jusqu'au 1er octobre. Fin 2024 : 348 000 lignes de bibliothèque, 63 000 de tests, 1 697 commits, pas encore de moteur. Le 2026-10-01 : 531 000 lignes de bibliothèque, 179 000 lignes de moteur en Zig, 306 000 lignes de tests, 501 gardes narrés." width="1376" height="768"><figcaption>Compté dans le dépôt le 2026-10-01 : commits par année civile sur la branche principale, et l'arbre tel qu'il était le 31 décembre 2024 contre l'arbre au commit 0e72e2e2c.</figcaption></figure>

Fin 2024, après 1 697 commits d'un seul auteur, la bibliothèque tenait 348 mille lignes de code et 63 mille lignes de tests, toutes dans le langage hôte, sans moteur encore. L'auteur déclare que ces lignes ont été écrites à la main, avant les agents de programmation. Depuis, le moteur Zig a été écrit (179 mille lignes), la bibliothèque a grandi jusqu'à 531 mille lignes, les tests jusqu'à 306 mille, et le rythme des commits a triplé : voilà à quoi ressemble construire avec des agents sous un harnais, quand le harnais est Takamba et que la loi est que tout est jugé en s'exécutant.

<p class="proof">Les comptes : <code>git rev-list --count</code> au dernier commit de chaque année sur la branche principale ; lignes comptées sur les fichiers <code>*.ring</code> hors dossiers <code>archive</code>, séparées entre <code>base/test</code> et le reste, dans l'arbre de <a href="https://github.com/mayouni/stzlib/commit/a395d09cd59a3439154ff1b899db04acce2dfb27">a395d09c</a> (2024-12-31) et de <a href="https://github.com/mayouni/stzlib/commit/0e72e2e2c">0e72e2e2c</a> (2026-09-30). La phrase « écrites à la main » est celle de l'auteur ; les dates et les tailles sont celles du dépôt.</p>

<p class="way"><span>La manière Softanza</span> Une plateforme écrite depuis les premiers principes peut obéir partout à un seul ensemble de lois. Une plateforme assemblée de cent bibliothèques ne le peut pas, parce que chaque bibliothèque a déjà choisi les siennes.</p>
