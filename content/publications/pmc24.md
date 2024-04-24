---
title: "A framework for offloading and migration of serverless functions in the Edge–Cloud Continuum"
authors: "G. Russo Russo, V. Cardellini, F. Lo Presti"
info: "Pervasive and Mobile Computing, vol. 100"
doi: "https://doi.org/10.1016/j.pmcj.2024.101915"
pdf: "https://www.sciencedirect.com/science/article/pii/S1574119224000415/pdfft?md5=0b746bfff0acade4c42c5e021cec20da&pid=1-s2.0-S1574119224000415-main.pdf"
year: 2024
publication_type: Journal
layout: publication
---

Function-as-a-Service (FaaS) has emerged as an evolution of traditional Cloud service models, allowing users to define and execute pieces of codes (i.e., functions) in a serverless manner, with the provider taking care of most operational issues. With the unending growth of resource availability in the Edge-to-Cloud Continuum, there is increasing interest in adopting FaaS near the Edge as well, to better support geo-distributed and pervasive applications. However, as the existing FaaS frameworks have mostly been designed with Cloud in mind, new architectures are necessary to cope with the additional challenges of the Continuum, such as higher heterogeneity, network latencies, limited computing capacity.

In this paper, we present an extended version of Serverledge, a FaaS framework designed to span Edge and Cloud computing landscapes. Serverledge relies on a decentralized architecture, where each FaaS node is able to autonomously schedule and execute functions. To take advantage of the computational capacity of the infrastructure, Serverledge nodes also rely on horizontal and vertical function offloading mechanisms. In this work we particularly focus on the design of mechanisms for function offloading and live function migration across nodes. We implement these mechanisms in Serverledge and evaluate their impact and performance considering different scenarios and functions.

