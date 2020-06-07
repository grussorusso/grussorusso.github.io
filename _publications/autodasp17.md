---
title: "Towards hierarchical autonomous control for elastic data stream processing in the fog"
authors: "V. Cardellini, F. Lo Presti, M. Nardelli, G. Russo Russo"
info: "International Workshop on Autonomic Solutions for Parallel and Distributed Data Stream Processing (Auto-DaSP 2017), Santiago de Compostela, Spain, August 2017"
doi: "http://dx.doi.org/10.1007/978-3-319-75178-8_9"
pdf: http://www.ce.uniroma2.it/publications/autodasp2017.pdf
year: 2017
type: Conference
selected: false
layout: publication
---

In the Big Data era, Data Stream Processing (DSP) applications should be capable
to seamlessly process huge amount of data. Hence, they need to dynamically scale
their execution on multiple computing nodes so to adjust to unpredictable data
source rate. In this paper, we present a hierarchical and distributed
architecture for the autonomous control of elastic DSP applications. It revolves
around a two layered approach. At the lower level, distributed components issue
requests for adapting the deployment of DSP operations as to adjust to changing
workload conditions. At the higher level, a per-application centralized
component works on a broader time scale; it oversees the application behavior
and grants reconfigurations to control the application performance while
limiting the negative effect of their enactment, i.e., application downtime. We
have implemented the proposed solution in our distributed Storm prototype and
evaluated its behavior adopting simple policies. The experimental results are
promising and show that, even with simple policies, it is possible to limit the
number of reconfigurations while at the same time guaranteeing an adequate level
of application performance.
