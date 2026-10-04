---
title: Forgée en projets
title_html: Forgée <i>en projets</i>
kicker: Construite à la dure, et dite honnêtement
lede: Softanza n'a pas été construite comme un laboratoire de recherche, même si elle peut en être un. Elle a été construite en l'utilisant, et en se faisant demander des choses par des gens qui avaient un restaurant, une banque ou une organisation à faire tourner. Cette page dit, projet par projet, ce qu'il fallait, ce que la bibliothèque a appris, et le fichier qui porte la leçon.
description: Les projets qui ont forgé Softanza : RestoLean, Organizium et la Sonibank, DIKO. Ce que chacun demandait, ce que la bibliothèque a appris, et où la leçon se trouve dans le code.
---

## Comment lire cette page {#rule}

Trois règles, pour que l'histoire se vérifie. Une leçon n'est listée que lorsqu'un fichier de la bibliothèque la porte, et ce fichier est nommé. Un projet n'est raconté que dans la mesure où un document l'atteste ; quand le document n'est pas encore public, la page le dit et ne cite rien de privé : ni prix, ni chiffre d'un client, ni nom de personne. Et quand la bibliothèque ne fait que prendre un projet pour exemple, la page dit « exemple », pas « origine ».

## L'ordre dans lequel les choses se sont passées {#order}

<ol class="narr">
<li><b>12 mars 2022.</b> Le premier commit de la bibliothèque (<a href="history.html">Depuis les principes</a>).</li>
<li><b>2024, RestoLean.</b> Une mission d'analyse (l'offre est datée du 2 mai 2024), les analyses fondatrices (juin et juillet), puis un « roman de spécification » : des narrations qui spécifient le système par l'histoire (août et septembre).</li>
<li><b>2025, RestoLean.</b> Le premier produit spécifié jusqu'au dernier détail (février et mars) ; deux ans de spécification en tout, sans livrable opérationnel ; un long silence ; et le tournant vers livrer petit et vite.</li>
<li><b>Février 2026, Organizium.</b> Une nouvelle version, et la couche web de Softanza née en son sein (le dépôt commence le 4 février).</li>
<li><b>Juillet et août 2026, RestoLean.</b> La première itération livrée ; le 4 juillet le client renverse l'ordre du travail, et le 4 août l'avenant qui le fixe est clos.</li>
<li><b>Automne 2026, DIKO.</b> L'étude de conception d'un hub qui relie les outils d'une organisation au Niger.</li>
</ol>

## RestoLean, Lyon : une spécification n'est pas une livraison {#restolean}

RestoLean est une plateforme pour le commerce de proximité, portée par le propriétaire d'un restaurant de couscous à Lyon et conçue par l'auteur. Sa première leçon est de méthode, et elle a été payée. Deux ans de spécification riche n'ont produit aucun livrable opérationnel, un silence de six mois a suivi, et le projet a failli s'arrêter. Il en est sorti la doctrine du travail de l'auteur depuis : livrer petit, vite et utile, et laisser les fondations mûrir en parallèle sans jamais bloquer une livraison.

Sa deuxième leçon est une règle. Quand le client a renversé l'ordre du travail le 4 juillet 2026 (le client d'abord, le restaurateur ensuite, le fournisseur en dernier), le projet a fixé **le Verrou** : aucun nouveau virage et aucun gonflement de périmètre en cours de cycle, et toute idée va dans un carnet relu en fin de cycle. Dans la constellation que RestoLean est alors devenue, ajouter un monde ou un lien est un acte déclaré et visible, pas une dérive silencieuse du périmètre.

Ce qu'il fallait, et où la bibliothèque le porte :

<div class="cards">
<div class="card"><h3>Essayer des paiements sans abonnement</h3><p>Le guide de RestoLean nomme la virtualisation de services de la bibliothèque comme la façon d'essayer les paiements avant tout abonnement. La bibliothèque tient la surface de dépendances d'une solution dans un seul registre, lie un faux pendant qu'on programme, et refuse de dire une solution prête pour la production tant qu'un faux y est lié. <span class="mono">base/service/stzServiceRegistry.ring</span>, plan <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/design/SOFTANZA_SERVICE_VIRTUALIZATION_PLAN.md">SOFTANZA_SERVICE_VIRTUALIZATION_PLAN.md</a>.</p></div>
<div class="card"><h3>Voir toute la solution avant de la construire</h3><p>Les conceptions d'émulation et de déploiement de la bibliothèque prennent pour exemple une solution nommée restolean : une application de téléphone, un serveur, un appareil. C'est un exemple là, pas l'origine de la conception. <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/design/SOFTANZA_EMULATION.md">SOFTANZA_EMULATION.md</a>, <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/design/SOFTANZA_DEPLOYMENT.md">SOFTANZA_DEPLOYMENT.md</a>.</p></div>
<div class="card"><h3>Une constellation de mondes sur un même socle</h3><p>Après le virage, RestoLean a été redessinée en constellation : un monde pour le téléphone du client, un pour l'écran de cuisine, un pour l'atelier du commerçant, un pour la gestion et un pour la console de l'éditeur, sur un socle commun d'identité, de catalogue, de commandes, de paiements et de flotte. Le nouveau dessin cite la conception propre de la bibliothèque. <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/design/STZSUPERAPP_DESIGN.md">STZSUPERAPP_DESIGN.md</a>.</p></div>
<div class="card"><h3>Un budget de vitesse est une promesse</h3><p>Les critères d'acceptation de RestoLean fixent un budget de vitesse pour chaque cycle : premier affichage, réaction à un appui, une commande qui arrive en cuisine. Le plan de performance de la bibliothèque énonce une promesse à côté du code qu'elle juge, et rapporte la valeur mesurée à côté de chaque verdict. <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/narrations/stz-perf-judgment-narration.md">stz-perf-judgment-narration.md</a>.</p></div>
</div>

La première, exécutée pour cette page : une solution déclare qu'elle dépend d'un service de courrier, lie le faux, et passe en production. Le registre ne la dit pas saine.

<!--FORGED:registry-->

La première ligne est 0, pas saine. La seconde dit pourquoi : un faux ne doit jamais partir en production. Le faux est refusé par son nom, et un service déclaré mais jamais lié lève une erreur quand on le demande, au lieu de ne rien faire en silence.

<p class="way"><span>La manière Softanza</span> « Nous avons testé contre le bac à sable » ne veut rien dire si le code n'est pas, octet pour octet, celui qui part. Alors c'est la phase qui décide ce qui revient, et la vérification que rien de faux ne part est imposée, pas retenue de mémoire.</p>

Ce qui est vrai aujourd'hui, dit clairement : la première itération de RestoLean est une application web de mondes en fichier unique, sans étape de construction ; la constellation est un dessin que la bibliothèque sait exécuter, pas encore la production de RestoLean.

## Organizium et la Sonibank : une organisation jugée sur son propre organigramme {#organizium}

Organizium est une plateforme d'évaluation des organisations : un questionnaire, un moteur de notation, un modèle de maturité, un référentiel de normes et d'indicateurs, un organigramme avec ses écarts de conformité, une simulation de l'avant et de l'après, et des recommandations. Elle a d'abord été construite pour une banque : Organizium Standard Edition est installée, sous licence, sur le réseau interne de la Sonibank à Niamey, et le guide d'installation remis à la banque l'atteste. Une seconde version, en 2026, a porté 48 questions en huit dimensions, un agent fait de règles sans modèle de langage, et un outil de mise en relation avec des financements, d'abord pour DIKO.

Ce que la bibliothèque en porte est facile à montrer. Le régulateur d'une banque a des règles sur qui rend compte à qui : un conseil doit exister, l'audit doit rendre compte au conseil, une fonction de risque doit exister, les opérations ne doivent pas passer par la trésorerie. L'organigramme de la bibliothèque porte ces règles comme des validateurs, avec à côté les bases de règles des régulateurs (BCEAO, Bâle III, SOX, PCI DSS, ISO 27001, RGPD, HIPAA).

<!--FORGED:orgchart-->

Trois constats, chacun une règle avec un numéro qu'un auditeur de banque sait lire. <span class="mono">base/graph/stzOrgChart.ring</span> porte les validateurs ; la bibliothèque nomme aussi les bases de règles <span class="mono">stzBCEAORuleBase</span>, <span class="mono">stzBaselIIIRuleBase</span> et leurs sœurs.

L'autre chose née dans Organizium est la couche web. Son dépôt, commencé le 4 février 2026, contient un cadre de mondes en fichier unique pour le web, une première notation de requête, et la constitution d'interface avec son fichier de règles et le vérificateur qui contrôle une page contre elle : une forme précoce de ce que le site appelle aujourd'hui <a href="zui.html">Zui</a>. Ils ne sont pas encore publics ; le site n'en cite aucun texte.

## DIKO, Niamey : la plateforme parle la langue de l'organisation {#diko}

DIKO est une organisation qui travaille au Niger, avec un siège à Niamey et des bases sur le terrain. Elle est déjà connectée et déjà équipée en outils. Ce qui lui manque, c'est le lien entre eux : une demande circule des jours sur papier ou dans un document, et les règles existent mais vivent dans des fichiers séparés. L'étude de conception de **DIKO Hub**, un point d'entrée unique qui relie les outils existants sans en remplacer aucun, demande six choses à une plateforme. Chacune repose sur une pièce de Softanza, ou sur un manque que l'étude nomme.

<div class="cards">
<div class="card"><h3>Ses mots et ses règles</h3><p>La plateforme parle le vocabulaire de DIKO, et ses règles sont écrites noir sur blanc, modifiées sans programmeur, chaque changement enregistré et annulable. Dans la notation de l'étude, une règle se lit comme une phrase : <span class="mono">RULE: budget &lt;= ligne.disponible</span>, avec le message que la personne lira. La bibliothèque porte les règles comme des données, avec une gouvernance qui enregistre chaque changement.</p></div>
<div class="card"><h3>Une personne décide</h3><p>Un agent qui connaît DIKO prépare les dossiers et vérifie les pièces, et une personne décide toujours. Les agents de la bibliothèque proposent et seule une porte valide ; leurs actes sont répétés d'abord dans un monde sûr.</p></div>
<div class="card"><h3>Tout est tracé</h3><p>Chaque validation, chaque refus et chaque consultation d'un dossier sensible est enregistré avec son auteur et sa date, et rien ne peut s'effacer. Les données ont trois niveaux de sensibilité. Le plan de sécurité de la bibliothèque porte les garanties ; chacune a un test.</p></div>
<div class="card"><h3>Hors ligne par défaut</h3><p>Chaque appareil garde ce qui est saisi et l'envoie quand le réseau revient. <b>C'est un manque, pas une leçon apprise.</b> RestoLean demandait la même chose (l'usage dans la réserve, sans connexion). L'étude nomme les pièces pour cela, HaroScript et HaroServ, dont la <a href="estate.html">page du domaine</a> dit le stade ; cette page ne le dit pas clos.</p></div>
<div class="card"><h3>Un circuit avec ses délais</h3><p>Une demande se décrit une fois, et l'avance, l'achat et la mission en découlent. Chaque étape a un délai qui se voit, et un avis non rendu est réputé donné, comme le prévoit la matrice de responsabilités de l'organisation. Les classes de flux de travail de la bibliothèque portent les étapes et leur simulation.</p></div>
<div class="card"><h3>Une chaîne de documents</h3><p>L'étude elle-même a été produite par une chaîne qui va de Markdown à un PDF paginé. Elle a montré ce qui manque au domaine : les chaînes qui produisent ses documents, celle de ce site comprise, sont écrites en Python et en Node, et aucune n'appelle le moteur.</p></div>
</div>

Un module d'organigramme, construit sur le noyau d'Organizium, est proposé comme extension du hub : l'organigramme de la banque et celui de l'ONG sont le même moteur avec d'autres mots, ce qui est le but de la plateforme.

Ce qui est vrai aujourd'hui, dit clairement : DIKO Hub est un dessin. L'étude est écrite ; rien du hub n'est en production.

## Ce que les projets ont en commun {#common}

Un restaurant, une banque et une ONG n'ont rien en commun, et chacun a demandé les mêmes cinq choses avec ses mots : un socle commun, un monde pour chaque personne et chaque appareil, des liens entre eux, des règles, et des rôles. La bibliothèque nomme cette construction, une constellation de mondes, et le site l'appelle <a href="platforms.html">une plateforme de plateformes</a>. Ce n'est pas une théorie appliquée après coup : c'est ce que les projets avaient en commun une fois mis côte à côte.

## Ce que les projets n'ont pas prouvé {#limits}

Les plateformes clientes tournent aujourd'hui sur des piles ordinaires : Organizium à la Sonibank est une application Python, RestoLean est faite de mondes web en fichier unique, DIKO Hub n'est pas construit. Leurs déclarations s'écrivent comme celles de Softanza, si bien que les passer sur le moteur de Softanza est un changement de moteur, pas de plan ; c'est une étape devant, pas une étape faite. Certaines leçons ci-dessus sont portées par des fichiers publics et d'autres seulement par des documents qui ne sont pas encore publics : la page marque lesquelles. Et ce dont l'auteur se souvient et qu'aucun fichier ne prouve n'est pas listé.

<p class="proof">Les fichiers de la bibliothèque nommés ci-dessus sont publics ; les dépôts des projets ne le sont pas, et le site n'en cite rien au-delà de ce que chaque section dit. Chaque exécution de cette page a été faite dans la bibliothèque le <!--FORGED-RAN--> au commit 0e72e2e2c.</p>
