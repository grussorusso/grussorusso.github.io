---
title: "Decentralized self-adaptation for elastic Data Stream Processing"
authors: "V. Cardellini, F. Lo Presti, M. Nardelli, G. Russo Russo"
info: "Future Generation Computer Systems, vol. 87, pp. 171–185"
doi: "https://doi.org/10.1016/j.future.2018.05.025"
pdf: "http://www.ce.uniroma2.it/publications/fgcs2018_dsp.pdf"
year: 2018
type: Journal
selected: false
layout: publication
---

Data Stream Processing (DSP) applications are widely used to develop new
pervasive services, which require to seamlessly process huge amounts of data in
a near real-time fashion. To keep up with the high volume of daily produced
data, these applications need to dynamically scale their execution on multiple
computing nodes, so to process the incoming data flow in parallel. In this
paper, we present a hierarchical distributed architecture for the autonomous
control of elastic DSP applications. It consists of a two-layered hierarchical
solution, where a centralized per-application component coordinates the run-time
adaptation of subordinated distributed components, which, in turn, locally
control the adaptation of single DSP operators. Thanks to its features, the
proposed solution can efficiently run in large-scale Fog computing environments.
Exploiting this framework, we design several distributed self-adaptation
policies, including a popular threshold-based approach and two reinforcement
learning solutions. We integrate the hierarchical architecture and the devised
self-adaptation policies in Apache Storm, a popular open-source DSP framework.
Relying on the DEBS 2015 Grand Challenge as a benchmark application, we show the
benefits of the presented self-adaptation policies, and discuss the strengths of
reinforcement learning based approaches, which autonomously learn from
experience how to optimize the application performance.

