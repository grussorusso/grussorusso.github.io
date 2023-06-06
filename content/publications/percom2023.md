---
authors: "G. Russo Russo, T. Mannucci, V. Cardellini, F. Lo Presti"
title: "Serverledge: Decentralized Function-as-a-Service for the Edge-Cloud Continuum"
info: "Proc. of IEEE PerCom '23"
doi: "https://doi.org/10.1109/PERCOM56429.2023.10099372"
pdf: "http://www.ce.uniroma2.it/publications/serverledgePerCom2023.pdf"
year: 2023
publication_type: Conference
selected: true
award: Artifact Certified; Results Certified
layout: publication
---

As the Function-as-a-Service (FaaS) paradigm enjoys growing popularity within Cloud-based systems, there is increasing interest in moving serverless functions towards the Edge, to better support geo-distributed and pervasive applications. However, enjoying both the reduced latency of Edge and the scalability of FaaS is not straightforward, calling for new architectures and implementations to cope with Edge challenges (e.g., nodes with limited computational capacity). While first solutions have been proposed for Edge-based FaaS, including light function sandboxing techniques, we lack a platform with the ability to span both Edge and Cloud and adaptively exploit both. In this paper, we present Serverledge, a FaaS platform designed for the Edge-to-Cloud continuum. Serverledge adopts a decentralized architecture, where function invocation requests can be fully served within Edge nodes in most the cases. To cope with load peaks, Serverledge also supports vertical (i.e., from Edge to Cloud) and horizontal (i.e., among Edge nodes) computation offloading. Our evaluation shows that Serverledge outperforms Apache OpenWhisk in an Edge-like scenario and has competitive performance with state-of-the-art frameworks optimized for the Edge, with the advantage of built-in support for vertical and horizontal offloading.
