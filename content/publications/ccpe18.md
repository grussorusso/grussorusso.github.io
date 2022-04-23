---
title: Optimal operator deployment and replication for elastic distributed data stream processing
authors: V. Cardellini, F. Lo Presti, M. Nardelli, G. Russo Russo
year: 2018
info: "Concurrency and Computation: Practice &amp; Experience, Vol. 30, No. 9, May 2018"
pdf: "http://www.ce.uniroma2.it/publications/ccpe2018.pdf"
publication_type: Journal
selected: false
doi: "https://doi.org/10.1002/cpe.4334"
layout: publication
---

Processing data in a timely manner, data stream processing (DSP) applications are receiving an increasing interest for building new pervasive services. Due to the unpredictability of data sources, these applications often operate in dynamic environments; therefore, they require the ability to elastically scale in response to workload variations. In this paper, we deal with a key problem for the effective runtime management of a DSP application in geo‐distributed environments: We investigate the placement and replication decisions while considering the application and resource heterogeneity and the migration overhead, so to select the optimal adaptation strategy that can minimize migration costs while satisfying the application quality of service (QoS) requirements. We present elastic DSP replication and placement (EDRP), a unified framework for the QoS‐aware initial deployment and runtime elasticity management of DSP applications. In EDRP, the deployment and runtime decisions are driven by the solution of a suitable integer linear programming problem, whose objective function captures the relative importance between QoS goals and reconfiguration costs. We also present the implementation of EDRP and the related mechanisms on Apache Storm. We conduct a thorough experimental evaluation, both numerical and protopublication_type‐based, that shows the benefits achieved by EDRP on the application performance.
