---
title: The host
title_html: The <i>host</i>
kicker: Where an application is served
lede: A host driven by the engine's reactor, a live back end that every part of a solution shares, and a plane that scales it to many nodes. What is built, and what the Atlas says is not.
description: The Softanza application host: the reactor-driven server, the live back end, the scale plane and the virtualisable services, with the Atlas's own statement of what is missing.
---

## What is built {#built}

<div class="cards">
<div class="card"><h3>The server <b>(built)</b></h3><p>A host driven by the engine's reactor: HTTP/1.1, routing in the manner of the web frameworks, HTTPS and mutual TLS, and automatic create-read-update-delete over an embedded database. Five modules and eleven guards.</p></div>
<div class="card"><h3>The request bracket <b>(built)</b></h3><p>Every request is measured as it is served: its time, its count, its errors, with percentiles, a health route, a metrics route and a trace header, which is more than the best-known web frameworks give by default.</p></div>
<div class="card"><h3>The authentication router <b>(built)</b></h3><p>A router that mounts as an identity provider with discovery, keys and authorisation, and is itself a sign-in standard's provider.</p></div>
<div class="card"><h3>The scale plane <b>(built)</b></h3><p>Nodes, supervision, mutual TLS between nodes, request signing, rate limiting, federation. Thirty-five guards across fourteen and nineteen files.</p></div>
<div class="card"><h3>The services plane <b>(built)</b></h3><p>The dependencies a solution reaches, virtualised: HTTP, data, mail, text messages, payments, a language model and sign-in. A service is declared, a sandbox is bound to it while developing, the live service at deployment, and production refuses the fake.</p></div>
</div>

## What the Atlas says is missing {#gaps}

<p class="proof"><b>in construction</b> The server is real and competent, and the Atlas states its gaps in its own words: middleware is registered and never invoked, and there is no JSON body parsing, no streaming and no WebSocket. The standout of this area is not the server but the services plane, where a stateful double sits under a governance gate and a production deployment structurally refuses a fake dependency, even for a fully entitled human. The ratings, lane by lane, are on the Atlas page of the <a href="atlas/web.html">web and application server</a> and of <a href="atlas/concurrency.html">concurrency</a>.</p>

<p class="proof">Sources: the articles <a href="narrations/stzappserver-article.html">the application server</a> and <a href="narrations/stz-service-virtualization-code-first-subscribe-later.html">service virtualization</a>; the guards of the library's appserver, cluster and service folders. The inventory was read from the library's files by an outside assessment on 2026-10-07.</p>
