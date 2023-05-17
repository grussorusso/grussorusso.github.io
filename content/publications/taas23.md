---
authors: G. Russo Russo, V. Cardellini, F. Lo Presti
title: "Hierarchical Auto-Scaling Policies for Data Stream Processing on Heterogeneous Resources"
info: "ACM Transactions on Adaptive Systems"
doi: "https://dl.acm.org/doi/10.1145/3597435"
#pdf: "https://art.torvergata.it/retrieve/handle/2108/288667/577062/csur2022.pdf"
year: 2023
publication_type: Journal
selected: true
layout: publication
---

Data Stream Processing (DSP) applications analyze data flows in near real-time by means of operators, which process and transform incoming data. Operators handle high data rates running parallel replicas across multiple processors and hosts. To guarantee consistent performance without wasting resources in face of variable workloads, auto-scaling techniques have been studied to adapt operator parallelism at run-time. However, most the effort has been spent under the assumption of homogeneous computing infrastructures, neglecting the complexity of modern environments.

We consider the problem of deciding both how many operator replicas should be executed and which types of computing nodes should be acquired. We devise heterogeneity-aware policies by means of a two-layered hierarchy of controllers. While application-level components steer the adaptation process for whole applications, aiming to guarantee user-specified requirements, lower-layer components control auto-scaling of single operators. We tackle the fundamental challenge of performance and workload uncertainty, exploiting Bayesian optimization and reinforcement learning to devise policies. The evaluation shows that our approach is able to meet users’ requirements in terms of response time and adaptation overhead, while minimizing the cost due to resource usage, outperforming state-of-the-art baselines. We also demonstrate how partial model information is exploited to reduce training time for learning-based controllers.
