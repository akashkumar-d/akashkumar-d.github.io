# Publications

Generated on 2025-11-15T19:51:04.425976 UTC

**[The Complexity of Learning Sparse Superposed Features with Feedback](https://proceedings.mlr.press/v267/kumar25b.html)**
*Authors:* A Kumar
*Venue:* The 42nd International Conference on Machine Learning (ICML 2025)
*Year:* 2025
*Links:* [proceedings](https://proceedings.mlr.press/v267/kumar25b.html) · [arxiv](https://arxiv.org/abs/2502.05407)
<details><summary>Abstract</summary><div>The success of deep networks is crucially attributed to their ability to capture latent features within a representation space. In this work, we investigate whether the underlying learned features of a model can be efficiently retrieved through feedback from an agent, such as a large language model (LLM), in the form of relative triplet comparisons. These features may represent various constructs, including dictionaries in LLMs or components of a covariance matrix of Mahalanobis distances. We analyze the feedback complexity associated with learning a feature matrix in sparse settings. Our results establish tight bounds when the agent is permitted to construct activations and demonstrate strong upper bounds in sparse scenarios when the agent’s feedback is limited to distributional information. We validate our theoretical findings through experiments on two distinct applications: feature recovery from Recursive Feature Machine-trained models and dictionary extraction from sparse autoencoders trained on Large Language Models.</div></details>

---

**[A Gap Between the Gaussian RKHS and Neural Networks: An Infinite-Center Asymptotic Analysis](https://proceedings.mlr.press/v291/kumar25b.html)**  _(selected)_
*Authors:* A Kumar, R Parhi, M Belkin
*Venue:* The 38th Annual Conference on Learning Theory (COLT 2025)
*Year:* 2025
*Links:* [proceedings](https://proceedings.mlr.press/v291/kumar25b.html) · [arxiv](https://arxiv.org/abs/2502.16331)
<details><summary>Abstract</summary><div>Recent works have characterized the function-space inductive bias of infinite-width bounded-norm single-hidden-layer neural networks as a kind of bounded-variation-type space. This novel neural network Banach space encompasses many classical multivariate function spaces, including certain Sobolev spaces and the spectral Barron spaces. Notably, this Banach space also includes functions that exhibit less classical regularity, such as those that only vary in a few directions. On bounded domains, it is well-established that the Gaussian reproducing kernel Hilbert space (RKHS) strictly embeds into this Banach space, demonstrating a clear gap between the Gaussian RKHS and the neural network Banach space. It turns out that when investigating these spaces on unbounded domains, e.g., all of $\mathbb{R}^d$, the story is fundamentally different. We establish the following fundamental result: certain functions that lie in the Gaussian RKHS have infinite norm in the neural network Banach space. This provides a nontrivial gap between kernel methods and neural networks by exhibiting functions that kernel methods easily represent, whereas neural networks cannot.</div></details>

---

**Convergence of Nearest Neighbor Selective Classification**
*Authors:* A Kumar, S Dasgupta
*Venue:* Manuscript on request
*Year:* 2025
<details><summary>Abstract</summary><div>An elementary approach to \emph{selective classification} (also known as \emph{classification with a reject option}) is the $(k,k')$-rule: given a query $x$, find its $k$ nearest neighbors in the training set and if at least $k'$ of them have the same label, then predict that label; otherwise, abstain. We study this method under minimal assumptions to understand its convergence properties and its tradeoffs between error and abstention rate.</div></details>

---

**[Mirror Descent on Reproducing Kernel Banach Space (RKBS)](https://arxiv.org/abs/2411.11242)**  _(selected)_
*Authors:* A Kumar, M Belkin, P Pandit
*Venue:* Journal of Machine Learning Research (JMLR), 2025 (To appear)
*Year:* 2025
<details><summary>Abstract</summary><div>Recent advances in machine learning have led to increased interest in reproducing kernel Banach spaces (RKBS) as a more general framework that extends beyond reproducing kernel Hilbert spaces (RKHS). These works have resulted in the formulation of representer theorems under several regularized learning schemes. However, little is known about an optimization method that encompasses these results in this setting. This paper addresses a learning problem on Banach spaces endowed with a reproducing kernel, focusing on efficient optimization within RKBS. To tackle this challenge, we propose an algorithm based on mirror descent (MDA). Our approach involves an iterative method that employs gradient steps in the dual space of the Banach space using the reproducing kernel. We analyze the convergence properties of our algorithm under various assumptions and establish two types of results: first, we identify conditions under which a linear convergence rate is achievable, akin to optimization in the Euclidean setting, and provide a proof of the linear rate; second, we demonstrate a standard convergence rate in a constrained setting. Moreover, to instantiate this algorithm in practice, we introduce a novel family of RKBSs with $p$-norm ($p \neq 2$), characterized by both an explicit dual map and a kernel.</div></details>

---

**[Learning Smooth Distance Functions via Queries](https://arxiv.org/abs/2412.01290)**  _(selected)_
*Authors:* A Kumar, S Dasgupta
*Venue:* Preprint
*Year:* 2024
<details><summary>Abstract</summary><div>In this work, we investigate the problem of learning distance functions within the query-based learning framework, where a learner is able to pose triplet queries of the form: “Is $x_i$ closer to $x_j$ or $x_k$?” We establish formal guarantees on the query complexity required to learn smooth, but otherwise general, distance functions under two notions of approximation: $\omega$-additive approximation and $(1 + \omega)$-multiplicative approximation. For the additive approximation, we propose a global method whose query complexity is quadratic in the size of a finite cover of the sample space. For the (stronger) multiplicative approximation, we introduce a method that combines global and local approaches, utilizing multiple Mahalanobis distance functions to capture local geometry. This method has a query complexity that scales quadratically with both the size of the cover and the ambient space dimension of the sample space.</div></details>

---

**[Robust Empirical Risk Minimization with Tolerance](https://proceedings.mlr.press/v201/bhattacharjee23a)**  _(selected)_
*Authors:* R Bhattacharjee, K Chaudhuri, M Hopkins, A Kumar, H Yu
*Venue:* The 34th International Conference on Algorithmic Learning Theory (ALT'23)
*Year:* 2023
*Links:* [proceedings](https://proceedings.mlr.press/v201/bhattacharjee23a) · [arxiv](https://arxiv.org/abs/2210.00635)
<details><summary>Abstract</summary><div>Developing simple, sample-efficient learning algorithms for robust classification is a pressing issue in today’s tech-dominated world, and current theoretical techniques requiring exponential sample complexity and complicated improper learning rules fall far from answering the need. In this work we study the fundamental paradigm of (robust) empirical risk minimization (RERM), a simple process in which the learner outputs any hypothesis minimizing its training error. RERM famously fails to robustly learn VC classes, a bound we show extends even to ‘nice’ settings such as (bounded) halfspaces. As such, we study a recent relaxation of the robust model called tolerant robust learning, where the output classifier is compared to the best achievable error over slightly larger perturbation sets. We show that under geometric niceness conditions, a natural tolerant variant of RERM is indeed sufficient for $\gamma$-tolerant robust learning of VC classes over $\mathbb{R}^d$, and requires only $\tilde{\mathcal{O}}(\mathrm{VC}(\mathcal{H})\,d\,\log(D/\gamma)/\varepsilon^2)$ samples for robustness regions of (maximum) diameter $D$.</div></details>

---

**[Teaching via Best-Case Counterexamples in the Learning-with-Equivalence-Queries Paradigm](https://proceedings.neurips.cc/paper/2021/hash/e22dd5dabde45eda5a1a67772c8e25dd-Abstract.html)**
*Authors:* A Kumar, Y Chen, A Singla
*Venue:* The 35th Conference on Neural Information Processing Systems (NeurIPS 2021)
*Year:* 2021
*Link:* [proceedings](https://proceedings.neurips.cc/paper/2021/hash/e22dd5dabde45eda5a1a67772c8e25dd-Abstract.html)
<details><summary>Abstract</summary><div>We study the sample complexity of teaching, termed as "teaching dimension" (TD) in the literature, for the learning-with-equivalence-queries (LwEQ) paradigm. More concretely, we consider a learner who asks equivalence queries (i.e., “is the queried hypothesis the target hypothesis?”), and a teacher responds either “yes” or “no” along with a counterexample to the queried hypothesis. This learning paradigm has been extensively studied when the learner receives worst-case or random counterexamples; in this paper, we consider the optimal teacher who picks best-case counterexamples to teach the target hypothesis within a hypothesis class. For this optimal teacher, we introduce LwEQ-TD, a notion of TD capturing the teaching complexity (i.e., the number of queries made) in this paradigm. We show that a significant reduction in queries can be achieved with best-case counterexamples, in contrast to worst-case or random counterexamples, for different hypothesis classes. Furthermore, we establish new connections of LwEQ-TD to the well-studied notions of TD in the learning-from-samples paradigm.</div></details>

---

**[The Teaching Dimension of Kernel Perceptron](https://proceedings.mlr.press/v130/kumar21a.html)**  _(selected)_
*Authors:* A Kumar, H Zhang, A Singla, Y Chen
*Venue:* The 24th International Conference on Artificial Intelligence and Statistics (AISTATS 2021)
*Year:* 2021
*Links:* [proceedings](https://proceedings.mlr.press/v130/kumar21a.html) · [arxiv](https://arxiv.org/abs/2010.14043)
<details><summary>Abstract</summary><div>Algorithmic machine teaching has been studied under the linear setting where exact teaching is possible. However, little is known for teaching nonlinear learners. Here, we establish the sample complexity of teaching, aka teaching dimension, for kernelized perceptrons for different families of feature maps. As a warm-up, we show that the teaching complexity is $\Theta(d)$ for the exact teaching of linear perceptrons in $\mathbb{R}^d$, and $\Theta(d^k)$ for kernel perceptron with a polynomial kernel of order $k$. Furthermore, under certain smooth assumptions on the data distribution, we establish a rigorous bound on the complexity for approximately teaching a Gaussian kernel perceptron. We provide numerical examples of the optimal (approximate) teaching set under several canonical settings for linear, polynomial and Gaussian kernel perceptrons.</div></details>

---

**[Deletion to Induced Matching](https://arxiv.org/abs/2008.09660)**
*Authors:* A Kumar, M Kumar
*Venue:* Preprint
*Year:* 2020
<details><summary>Abstract</summary><div>In the DELETION TO INDUCED MATCHING problem, we are given a graph $G$ on $n$ vertices, $m$ edges and a non-negative integer $k$ and asks whether there exists a set of vertices $S \subseteq V(G)$ such that $|S|\le k$ and the size of any connected component in $G-S$ is exactly 2. In this paper, we provide a fixed-parameter tractable (FPT) algorithm of running time $O^*(1.748^{k})$ for the DELETION TO INDUCED MATCHING problem using branch-and-reduce strategy and path decomposition. We also extend our work to the exact-exponential version of the problem.</div></details>

---

**[Average-case Complexity of Teaching Convex Polytopes via Halfspace Queries](https://arxiv.org/abs/2006.14677)**
*Authors:* A Kumar, A Singla, Y Yue, Y Chen
*Venue:* Preprint
*Year:* 2020
<details><summary>Abstract</summary><div>We examine the task of locating a target region among those induced by intersections of $n$ halfspaces in $\mathbb{R}^d$. This generic task connects to fundamental machine learning problems, such as training a perceptron and learning a $\phi$-separable dichotomy. We investigate the average teaching complexity of the task, i.e., the minimal number of samples (halfspace queries) required by a teacher to help a version-space learner in locating a randomly selected target. As our main result, we show that the average-case teaching complexity is $\Theta(d)$, which is in sharp contrast to the worst-case teaching complexity of $\Theta(n)$. If instead we consider the average-case learning complexity, the bounds have a dependency on $n$ as $\Theta(n)$ for i.i.d. queries and $\Theta(d\,\log n)$ for actively chosen queries by the learner. Our proof techniques are based on novel insights from computational geometry, which allow us to count the number of convex polytopes and faces in a Euclidean space depending on the arrangement of halfspaces. Our insights allow us to establish a tight bound on the average-case complexity for $\phi$-separable dichotomies, which generalizes the known $\mathcal{O}(d)$ bound on the average number of "extreme patterns" in the classical computational geometry literature (Cover, 1965).</div></details>

---
