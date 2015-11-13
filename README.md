# Supercomputing 2015 Tutorial

Shantenu Jha, Andre Luckow, Ioannis Paraskevakos

## Overview

High performance computing (HPC) environments have traditionally been designed to meet the compute demands of scientific applications; data has only been a second order concern. With science moving toward data-driven discoveries relying on correlations and patterns in data to form scientific hypotheses, the limitations of HPC approaches become apparent: Low-level abstractions and architectural paradigms, such as the separation of storage and compute, are not optimal for data-intensive applications. While there are powerful computational kernels and libraries available for traditional HPC, e. g., linear algebra, there is an apparent lack of functional completeness of analytical libraries. In contrast, the Apache Hadoop ecosystem has grown to be rich with analytical libraries, e. g., Spark MLlib. Bringing the richness of the Hadoop ecosystem to traditional HPC environments will help address some gaps.

In this tutorial, we explore a light-weight and extensible way to provide the best of both: We utilize the Pilot- Abstraction to execute a diverse set of data-intensive and analytics workloads using Hadoop and Spark on HPC infrastructures. The tutorial has three parts: In part (i) we provide the conceptual basis needed to understand the characteristics of “traditional” HPC workloads, large-scale multi-component scientific simulations as well as data-intensive analysis, in part (ii) we introduce the concept of Pilot-Abstraction that combines the ability to support extreme-scale task-parallel workloads with a clean model and flexible execution of heterogeneous concurrent tasks. In part (iii) we learn how to combine HPC with Apache Hadoop and Spark using the Pilot- Abstraction to facilitate the use MapReduce and emerging frameworks, such as Spark, to implement advanced data-intensive algorithms, e. g., KMeans for clustering and graph analytics.

## Agenda


1. Introduction to Apache Hadoop and HPC 

2. Introduction to Pilot-Abstraction

3.  Advanced Analytics with Apache Hadoop, Spark and Pilot-Abstraction

## Practical Exercises:

[see Wiki](https://github.com/radical-cybertools/supercomputing2015-tutorial/wiki)
