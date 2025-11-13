---
layout: single
title: "Robust Empirical Risk Minimization with Tolerance"
authors: "R Bhattacharjee, K Chaudhuri, M Hopkins, A Kumar, H Yu"
venue: "The 34th International Conference on Algorithmic Learning Theory (ALT'23)"
date: 2023-03-01
paperurl: https://proceedings.mlr.press/v201/bhattacharjee23a
arxiv: https://arxiv.org/abs/2210.00635
selected: true
authors_note: "Authors listed alphabetically"
abstract: |
  Developing simple, sample-efficient learning algorithms for robust
  classification is a pressing issue in today’s tech-dominated world, and current theoretical
  techniques requiring exponential sample complexity and complicated improper
  learning rules fall far from answering the need. In this work we study the
  fundamental paradigm of (robust) empirical risk minimization (RERM), a simple
  process in which the learner outputs any hypothesis minimizing its training error.
  RERM famously fails to robustly learn VC classes, a bound we show
  extends even to ‘nice’ settings such as (bounded) halfspaces. As such, we study
  a recent relaxation of the robust model called tolerant robust
  learning, where the output classifier is compared to the best achievable
  error over slightly larger perturbation sets. We show that under geometric
  niceness conditions, a natural tolerant variant of RERM is indeed sufficient for
  $\gamma$-tolerant robust learning of VC classes over $\mathbb{R}^d$, and requires only
  $\tilde{\mathcal{O}}(\mathrm{VC}(\mathcal{H})\,d\,\log(D/\gamma)/\varepsilon^2)$ samples for robustness regions of (maximum)
  diameter $D$.
---

