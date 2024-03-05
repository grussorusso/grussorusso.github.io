---
title: "QoS-aware offloading policies for serverless functions in the Cloud-to-Edge continuum"
authors: "G. Russo Russo, D. Ferrarelli, D. Pasquali, V. Cardellini, F. Lo Presti"
info: "Future Generation Computer Systems, vol. 156"
doi: "https://doi.org/10.1016/j.future.2024.02.019"
pdf: "https://www.sciencedirect.com/science/article/pii/S0167739X24000645/pdfft?md5=ff66ea9ba91fa82ae0d63b6faed27bbd&pid=1-s2.0-S0167739X24000645-main.pdf"
year: 2024
publication_type: Journal
layout: publication
---

Function-as-a-Service (FaaS) paradigm is increasingly attractive to bring the benefits of serverless computing to the edge of the network, besides traditional Cloud data centers. However, FaaS adoption in the emerging Cloud-to-Edge Continuum is challenging, mostly due to geographical distribution and heterogeneous resource availability. This emerging landscape calls for effective strategies to trade off low latency at the edge of the network with Cloud resource richness, taking into account the needs of different functions and users.

In this paper, we present QoS-aware offloading policies for serverless functions running in the Cloud-to-Edge continuum. We consider heterogeneous functions and service classes, and aim to maximize utility given a monetary budget for resource usage. Specifically, we introduce a two-level approach, where (i) FaaS nodes rely on a randomized policy to schedule every incoming request according to a set of probability values, and (ii) periodically, a linear programming model is solved to determine the probabilities to use for scheduling. We show by extensive simulation that our approach outperforms alternative approaches in terms of generated utility across multiple scenarios. Moreover, we demonstrate that our solution is computationally efficient and can be adopted in large-scale systems. We also demonstrate the functionality of our approach through a proof-of-concept experiment on an open-source FaaS framework.
