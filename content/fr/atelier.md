---
title: L'Atelier
title_html: L'<i>Atelier</i>
kicker: Les vérifications propres de la bibliothèque, enregistrées
lede: L'Atelier est un programme qui exécute les tests de la bibliothèque, une assertion à la fois, et enregistre le verdict de chacune. Cette page l'explique et renvoie à son édition statique, un ensemble de pages en lecture seule qui montrent ce qui a été enregistré à un commit de la bibliothèque. Rien n'y est exécuté.
description: L'Atelier de Softanza et son édition statique : les assertions de la bibliothèque, jugées et enregistrées à un commit, les cinq états d'une ligne de test montrés séparément, et chaque vérification citable par son commit et son identité.
---

## Ce qu'est l'Atelier {#what}

L'Atelier est un programme qui exécute les tests de la bibliothèque Softanza et enregistre ce que chacun a trouvé. Chaque fichier de test de la bibliothèque raconte une courte histoire : quelques appels, chacun suivi d'une ligne qui dit ce que la bibliothèque doit répondre. Les tests appellent une telle ligne une *ligne Then*. Une **vérification** est l'une de ces lignes prise entière : sa description, les deux valeurs qu'elle compare et les aides que son fichier définit pour elle. La valeur attendue est toujours celle qu'a écrite l'auteur du test, jamais une valeur choisie par l'Atelier.

Pour juger une vérification, l'Atelier charge la bibliothèque dans un programme en marche, appelle le code de la vérification et compare la réponse avec la valeur attendue. Le verdict est l'un de trois : la vérification a réussi ; elle a échoué, avec ce qui était attendu et ce qui est venu ; ou elle s'est terminée en erreur.

Sur une machine qui a la bibliothèque, l'Atelier peut aussi tourner en direct. Il ne répond qu'à l'adresse 127.0.0.1, c'est-à-dire à cette machine seule. Ce site ne peut pas le faire tourner, et aucune page du site n'exécute de code. Ce qu'un site peut montrer, c'est ce qui a été enregistré.

## L'édition statique {#edition}

Une édition est un dossier de pages construit à partir des données qu'un commit de la bibliothèque porte : les vérifications groupées par domaine, avec une zone de recherche ; la couverture de fichiers de test entiers ; et une page par vérification, trouvée par son identité. Tout est statique : la lire n'a pas besoin de serveur et ne charge rien.

Les chiffres ci-dessous sont ceux de l'édition. Chacun est une affirmation sur le commit nommé sous eux et sur aucun autre, et l'édition le dit elle-même.

<!--ATELIER:counts-->

## Deux comptes différents {#counts}

Les quatre premiers chiffres comptent des vérifications : les lignes Then que l'Atelier exécute une à une dans un programme en marche. Les cinq suivants comptent chaque ligne Then des fichiers de test narrés, que l'Atelier exécute entiers : un fichier va de sa première ligne à sa dernière, et un juge compare ce qu'il a imprimé avec les affirmations qu'on y a trouvées.

Chaque ligne Then finit dans l'un de cinq états. Ils sont montrés séparément et jamais additionnés :

- **tenue** : la ligne a été jugée, et la réponse était celle qui était attendue.
- **divergente** : la ligne a été jugée, et la réponse était différente.
- **non atteinte** : le fichier s'est brisé, ou n'a jamais démarré, avant la ligne.
- **non jugée** : le fichier a fini sans parcourir la ligne.
- **non perçue** : la ligne concerne quelque chose qu'une personne doit voir ou entendre, et personne n'a encore dit ce qu'elle a perçu.

Les verser dans « réussi » et « échoué » cacherait les lignes qui n'ont jamais été atteintes, qui ne sont ni des échecs ni des réussites.

## Citer une vérification {#cite}

Chaque vérification a une identité : son fichier de test, un `#`, et huit chiffres hexadécimaux tirés de son texte. Jointe au commit auquel elle a été enregistrée, elle forme une citation, écrite `commit:identité`. Une citation sans son commit n'est pas une citation, parce qu'un verdict est vrai d'un seul commit. Le résolveur refuse une citation dont le commit n'est pas celui qui a été enregistré.

Là où une page de ce site dit quelque chose que les tests de la bibliothèque disent aussi, elle cite la vérification. L'exemple ci-dessous est une vérification de la classe des chaînes : la page [Prouvé](proven.html#checks) en cite trois autres.

<!--CITE:string/00_string_narrated#87ed4de2-->

## Ce que cette page ne fait pas {#limits}

- Elle n'exécute rien : ni terrain de jeu, ni bouton qui lance du code. Un terrain de jeu hébergé a besoin d'un bac à sable, et il n'en existe pas encore.
- Elle ne change pas l'étape d'une page. Une citation dit qu'une vérification a réussi à un commit ; elle ne dit pas qu'une page est terminée.
- Elle ne cache pas ce qui n'est pas connu. Une ligne que personne n'a atteinte ni perçue reste dans son propre état.
