---
title: L'hôte
title_html: L'<i>hôte</i>
kicker: Là où une application est servie
lede: Un hôte piloté par le réacteur du moteur, un dorsal vivant que chaque partie d'une solution partage, et un plan qui le fait passer à plusieurs nœuds. Ce qui est construit, et ce que l'Atlas dit qui ne l'est pas.
description: L'hôte d'applications de Softanza : le serveur piloté par le réacteur, le dorsal vivant, le plan de l'échelle et les services virtualisables, avec l'énoncé de l'Atlas sur ce qui manque.
---

## Ce qui est construit {#built}

<div class="cards">
<div class="card"><h3>Le serveur <b>(construit)</b></h3><p>Un hôte piloté par le réacteur du moteur : HTTP/1.1, routage à la manière des cadriciels web, HTTPS et TLS mutuel, et création, lecture, mise à jour et suppression automatiques sur une base embarquée. Cinq modules et onze gardes.</p></div>
<div class="card"><h3>Le cadre de requête <b>(construit)</b></h3><p>Chaque requête est mesurée pendant qu'elle est servie : son temps, son compte, ses erreurs, avec des percentiles, une route de santé, une route de mesures et un en-tête de trace, ce qui dépasse ce que donnent par défaut les cadriciels web les plus connus.</p></div>
<div class="card"><h3>Le routeur d'authentification <b>(construit)</b></h3><p>Un routeur qui se monte comme fournisseur d'identité avec découverte, clés et autorisation, et qui est lui-même fournisseur d'une norme de connexion.</p></div>
<div class="card"><h3>Le plan de l'échelle <b>(construit)</b></h3><p>Des nœuds, la supervision, le TLS mutuel entre nœuds, la signature des requêtes, la limitation de débit, la fédération. Trente-cinq gardes sur quatorze et dix-neuf fichiers.</p></div>
<div class="card"><h3>Le plan des services <b>(construit)</b></h3><p>Les dépendances qu'atteint une solution, virtualisées : HTTP, données, courriel, SMS, paiements, un modèle de langage et la connexion. Un service est déclaré, un bac à sable lui est lié en développement, le service réel au déploiement, et la production refuse le faux.</p></div>
</div>

## Ce que l'Atlas dit qui manque {#gaps}

<p class="proof"><b>en construction</b> Le serveur est réel et compétent, et l'Atlas énonce ses manques dans ses propres mots : les intergiciels sont enregistrés et jamais invoqués, et il n'y a ni lecture de corps JSON, ni flux continu, ni WebSocket. Ce qui distingue ce domaine n'est pas le serveur mais le plan des services, où un double à état se tient sous une porte de gouvernance et où un déploiement de production refuse structurellement une dépendance factice, même pour un humain pleinement habilité. Les notes, couloir par couloir, sont sur la page de l'Atlas du <a href="atlas/web.html">serveur web et d'applications</a> et de la <a href="atlas/concurrency.html">concurrence</a>.</p>

<p class="proof">Sources : les articles <a href="narrations/stzappserver-article.html">le serveur d'applications</a> et <a href="narrations/stz-service-virtualization-code-first-subscribe-later.html">la virtualisation des services</a> ; les gardes des dossiers appserver, cluster et service de la bibliothèque. L'inventaire a été lu dans les fichiers de la bibliothèque par une évaluation extérieure le 2026-10-07.</p>
