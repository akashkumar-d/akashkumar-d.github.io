---
layout: single
title: "Can Representation Learning Decouple from Loss Minimization? Polar Updates Have an Answer"
authors: "A Kumar"
venue: "Preprint (under review)"
date: 2026-09-01
arxiv: https://arxiv.org/abs/2609.36240
selected: true
abstract: |
  Does representation learning stop when the training loss stops improving? We study this
  question for matrix Muon, whose polar-normalised updates have a step length set by the
  gradient's rank rather than its norm. Near the edge of stability, full-batch Muon on
  teacher-student problems enters approximately period-2 loss oscillations that persist
  for thousands of steps: the cycle-mean loss stays flat or rises, yet the weights keep
  moving and the learned features continue to align with the teacher subspace. For linear
  teacher-student learning toys, we derive explicit cycle and alignment formulas and
  conditional plateau and decay bounds. For a population mean-field ReLU model, we prove
  that, under stated dimension, initialisation and small-head conditions, the leading
  eigenspace of the average gradient outer product (AGOP) recovers the teacher subspace
  exactly during a loss plateau, before the loss later drops. In all 33 ReLU, GELU and
  SiLU teacher configurations we study, direction-only alignment metrics show the student
  AGOP aligned with, or still aligning to, the teacher subspace during the period-2
  oscillations; projected head refitting on selected configurations shows that the learned
  directions are useful for prediction, and further measurements distinguish AGOP
  alignment from weight-mass concentration. In deep residual ReLU students, freezing the
  downstream layers while the first layer trains with full-batch exact polar updates
  recreates a nearly flat cycle-mean loss with improving input-AGOP alignment; freezing
  and unfreezing switch between this plateau and loss decrease, and the effect is
  sensitive to momentum and to the choice of orthogonaliser.
---
