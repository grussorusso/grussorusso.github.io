---
authors: "G. Russo Russo, V. Cardellini, F. Lo Presti"
title: "Reinforcement learning based policies for elastic stream processing on heterogeneous resources"
info: "Proc. of DEBS 2019"
doi: "https://doi.org/10.1145/3328905.3329506"
year: 2019
type: Conference
selected: false
layout: publication
---

Data Stream Processing (DSP) has emerged as a key enabler to develop pervasive services that require to process data in a near real-time fashion. DSP applications keep up with the high volume of produced data by scaling their execution on multiple computing nodes, so as to process the incoming data flow in parallel. Workloads variability requires to elastically adapt the application parallelism at run-time in order to avoid over-provisioning. Elasticity policies for DSP have been widely investigated, but mostly under the simplifying assumption of homogeneous infrastructures. The resulting solutions do not capture the richness and inherent complexity of modern infrastructures, where heterogeneous computing resources are available on-demand. In this paper, we formulate the problem of controlling elasticity on heterogeneous resources as a Markov Decision Process (MDP). The resulting MDP is not easily solved by traditional techniques due to state space explosion, and thus we show how linear Function Approximation and Tile Coding can be used to efficiently compute elasticity policies at run-time. In order to deal with parameters uncertainty, we integrate the proposed approach with Reinforcement Learning algorithms. Our numerical evaluation shows the efficacy of the presented solutions compared to standard methods in terms of accuracy and convergence speed.
