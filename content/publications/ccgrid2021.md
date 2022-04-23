---
authors: "G. Russo Russo, V. Cardellini, G. Casale, F. Lo Presti"
title: "MEAD: Model-based Vertical Auto-Scaling for Data Stream Processing"
info: "Proc. of IEEE/ACM CCGRID '21"
doi: "https://doi.org/10.1109/CCGrid51090.2021.00041"
pdf: "http://www.ce.uniroma2.it/publications/ccgrid2021.pdf"
year: 2021
publication_type: Conference
selected: true
layout: publication
---

The unpredictable variability of Data Stream Processing (DSP) application workloads calls for advanced mechanisms and policies for elastically scaling the processing capacity
of DSP operators. Whilst many different approaches have been
used to devise policies, most of the solutions have focused on data
arrival rate and operator resource utilization as key metrics for
auto-scaling. We here show that, under burstiness in the data
flows, overly simple characterizations of the input stream can
yet lead to very inaccurate performance estimations that affect
such policies, resulting in sub-optimal resource allocation.
We then present MEAD, a vertical auto-scaling solution
that relies on online state-based representation of burstiness
to drive resource allocation. We use in particular Markovian
Arrival Processes (MAPs), which are composable with analytical
queueing models, allowing us to efficiently predict performance
at run-time under burstiness. We integrate MEAD in Apache
Flink, and evaluate its benefits over simpler yet popular auto-scaling solutions, using both synthetic and real-world workloads.
Differently from existing approaches, MEAD satisfies response
time requirements under burstiness, while saving up to 50% CPU
resources with respect to a static allocation.



