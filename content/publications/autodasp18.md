---
title: "A Multi-level Elasticity Framework for Distributed Data Stream Processing"
authors: "M. Nardelli, G. Russo Russo, V. Cardellini, F. Lo Presti"
info: "International Workshop on Autonomic Solutions for Parallel and Distributed Data Stream Processing (Auto-DaSP 2018), in conjunction with Euro-Par 2018, Turin, Italy, August 2018"
doi: "http://dx.doi.org/10.1007/978-3-030-10549-5_5"
pdf: http://www.ce.uniroma2.it/publications/autodasp2018.pdf
year: 2018
publication_type: Conference
selected: false
layout: publication
---

Data Stream Processing (DSP) applications should be capable to efficiently process high-velocity continuous data streams by elastically scaling the parallelism degree of their operators so to deal with high variability in the workload. Moreover, to efficiently use computing resources, modern DSP frameworks should seamlessly support infrastructure elasticity, which allows to exploit resources available on-demand in geo-distributed Cloud and Fog systems. In this paper we propose E2DF, a framework to autonomously control the multi-level elasticity of DSP applications and the underlying computing infrastructure. E2DF revolves around a hierarchical approach, with two control layers that work at different granularity and time scale. At the lower level, fully decentralized Operator and Region managers control the reconfiguration of distributed DSP operators and resources. At the higher level, centralized managers oversee the overall application and infrastructure adaptation. We have integrated the proposed solution into Apache Storm, relying on a previous extension we developed, and conducted an experimental evaluation. It shows that, even with simple control policies, E2DF can improve resource utilization without application performance degradation.
