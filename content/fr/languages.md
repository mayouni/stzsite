---
title: Langue des langues
title_html: Une langue <i>des langues</i>
kicker: Déclarez la vôtre
lede: L'acte fondateur de Softanza, et sa propre réponse à la programmation à l'ère agentique, est que **déclarer une langue est aussi simple que déclarer une variable.** Ce n'est pas ainsi que l'on écrit les logiciels aujourd'hui ; c'est la voie que Softanza propose. Un expert du métier écrit, en texte brut, les choses de son monde, les règles entre elles et les flux qui les font bouger. De cette seule déclaration sortent une langue dans son jargon, une base de connaissances de son monde, et un agent qui la parle. Tout cela tourne sur la machine, propulsé par les propres outils de la plateforme : pas d'API, pas de modèle distant, pas d'abonnement.
description: L'approche de Softanza : un expert du métier déclare une langue et obtient une langue du métier, une base de connaissances et un agent local.
---

<figure class="diagram"><img src="../assets/img/diagrams/languages-fr.png" alt="Un expert du métier déclare : DEFINE LANGUAGE tontine, ENTITY member et deposit, NORM amount supérieur à zéro, FLOW round et payout. Par une grammaire fermée viennent trois résultats : une langue de votre métier, fermée et jugée, construite ; une base de connaissances, en pointillé ; un agent qui la parle en local, en pointillé. En pointillé : une direction, pas un fait aujourd'hui." width="1376" height="768"><figcaption>La langue du métier existe et est prouvée : 16 cas de conformité sur 16, sur trois exécutants. La base de connaissances et l'agent conversationnel, comme une seule chaîne depuis une seule déclaration, sont spécifiés et ne tournent pas encore de bout en bout. Dessiné le 2026-10-01.</figcaption></figure>

À quoi ressemble une déclaration, prise dans la langue machine du domaine lui-même. Soixante-dix-neuf lignes déclarent toute la langue ; le méta-tribunal l'a jugée : sept déclarations, cinq formes, zéro expression.

<pre>DEFINE LANGUAGE machine AS (
  VERSION "0.1", GRAMMAR "0.1",
  COURT "declarative/machine/fixtures.json",
  EXTENSION ".machine"
)
...
REFUSAL closed_verbs AS (
  MESSAGE "The machine verb set is closed (DEFINE)."
)</pre>

Et à quoi ressemble le monde d'un expert du métier, pris dans les cas de conformité de la langue de requête : une tontine, déclarée dans ses propres mots.

<pre>DEFINE ENTITY deposit (id: uuid, member: text, amount: currency, ...)
  RATIONALE "One member's contribution to one round of the circle"
DEFINE NORM positive_deposit AS (
  RULE: amount > 0,
  MESSAGE: "A deposit must bring something to the circle"
)</pre>

<p class="proof">Trois strates par langue : une syntaxe fermée, une sémantique en base de connaissances, une pragmatique conversationnelle ; la couche naturelle compile vers la propre grammaire de requête fermée de la langue et jamais vers du code hôte, et elle est fondée sur un dictionnaire, ce qui explique qu'elle n'ait besoin d'aucun modèle. La déclaration de la machine est dans <a href="https://github.com/mayouni/harobanda">le dépôt Harobanda</a>, fichier <code>declarative/machine/machine.stzu</code>. Le dépôt de la discipline de fabrication de langues n'est pas encore public ; son stade, dans ses propres mots : « Phase 1 fermée, phase 1.5 ouverte ; plan et études, pas de code dans ce dépôt encore ». Ce qui tourne aujourd'hui tourne dans la plateforme : le chapitre 12 du cours, « Enseigner un monde », et la couche naturelle montrée sur la page Plateforme.</p>

<p class="way"><span>La manière Softanza</span> Ce n'est pas ainsi que l'on programme aujourd'hui ; c'est la proposition de Softanza pour l'ère agentique : une plateforme qui connaît votre monde, parce que vous l'avez déclaré, dans votre langue, et qu'elle a jugé la déclaration.</p>
