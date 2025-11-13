---
layout: single
title: "Mirror Descent on Reproducing Kernel Banach Space (RKBS)"
authors: "A Kumar, M Belkin, P Pandit"
venue: "Journal of Machine Learning Research (JMLR), 2025 (To appear)"
date: 2025-01-01
paperurl: https://arxiv.org/abs/2411.11242
arxiv: https://arxiv.org/abs/2411.11242
selected: true
abstract: |
  Recent advances in machine learning have led to increased interest in
  reproducing kernel Banach spaces (RKBS) as a more general framework that extends beyond
  reproducing kernel Hilbert spaces (RKHS). These works have resulted in the
  formulation of representer theorems under several regularized learning schemes.
  However, little is known about an optimization method that encompasses these results in
  this setting. This paper addresses a learning problem on Banach spaces endowed
  with a reproducing kernel, focusing on efficient optimization within RKBS. To
  tackle this challenge, we propose an algorithm based on mirror descent (MDA). Our
  approach involves an iterative method that employs gradient steps in the dual
  space of the Banach space using the reproducing kernel. We analyze the convergence properties
  of our algorithm under various assumptions and establish two types of results: first, we identify
  conditions under which a linear convergence rate is achievable, akin to optimization in the Euclidean
  setting, and provide a proof of the linear rate; second, we demonstrate a standard
  convergence rate in a constrained setting. Moreover, to instantiate this
  algorithm in practice, we introduce a novel family of RKBSs with $p$-norm ($p \neq 2$),
  characterized by both an explicit dual map and a kernel.
---

