---
layout: single
title: "Average-case Complexity of Teaching Convex Polytopes via Halfspace Queries"
authors: "A Kumar, A Singla, Y Yue, Y Chen"
venue: "Preprint"
date: 2020-06-25
paperurl: https://arxiv.org/abs/2006.14677
arxiv: https://arxiv.org/abs/2006.14677
selected: false
abstract: |
  We examine the task of locating a target region among those induced by intersections of $n$ halfspaces in $\mathbb{R}^d$. This generic task connects to fundamental machine learning problems, such as training a perceptron and learning a $\phi$-separable dichotomy. We investigate the average teaching complexity of the task, i.e., the minimal number of samples (halfspace queries) required by a teacher to help a version-space learner in locating a randomly selected target.
  
  As our main result, we show that the average-case teaching complexity is $\Theta(d)$, which is in sharp contrast to the worst-case teaching complexity of $\Theta(n)$. If instead, we consider the average-case learning complexity, the bounds have a dependency on $n$ as $\Theta(n)$ for \tt{i.i.d.} queries and $\Theta(d \log(n))$ for actively chosen queries by the learner. Our proof techniques are based on novel insights from computational geometry, which allow us to count the number of convex polytopes and faces in a Euclidean space depending on the arrangement of halfspaces. Our insights allow us to establish a tight bound on the average-case complexity for $\phi$-separable dichotomies, which generalizes the known $\mathcal{O}(d)$ bound on the average number of "extreme patterns" in the classical computational geometry literature (Cover, 1965).
---
