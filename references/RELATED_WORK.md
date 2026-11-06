# Related work and attribution

The [main theorem](../science/model.md) is a sharp Haar-average source-testing result after local depolarization. Its matching upper guarantee retains that prior, and its resource interpretation retains the ideal protected-readout model. This account separates imported methods and comparison theorems from the channel-specific evaluation. Technical section numbers below refer to the explicitly linked extended preprint versions. Full bibliographic records are in [references.bib](references.bib).


## Adaptive two-copy learning

Cotler, Gong, and Kannan study noisy purity testing in the same repeated-source setting. Their extended preprint, Appendix E.1, Definition E.1 and Theorem E.2, Eq. (31), uses an equal-prior Haar-pure-versus-maximally-mixed problem. Each adaptive node may perform an arbitrary POVM on two independently depolarized copies; the paragraph preceding the theorem explicitly permits just one initial noise layer followed by ideal pair processing. With retention $`\eta=1-\lambda`$, their lower bound is
```math
m_{\mathrm{pair}}\ge
\Omega\!\left(
\min\left\{2^{n/2},
\left[\frac{4}{1+3\eta^4}\right]^n
\right\}\right).
```
This is the comparison theorem used here, not a newly proved lower bound. [CGK26](https://arxiv.org/html/2512.10929v2)

Consequently, the collective law proves an exponential separation for fixed $`\eta\gt 3^{-1/4}`$. When combined with an $`O_\eta(M^2)`$ independent-pair upper bound, where $`M=\sqrt{d(d+1)/[(1+3\eta^4)^n-1]}`$, it gives $`m_{\mathrm{pair}}=\Theta_\eta(M^2)`$ for
```math
\left(\frac{2\sqrt2-1}{3}\right)^{1/4}\le\eta\lt 1.
```
These are consequences of the new collective theorem and the cited pair lower bound.

The earlier research repository *Quantum Purity Noise Budget* already allows unlimited downstream quantum memory and collective readout, proves collective hardness at fixed local noise, and characterizes worst-case polynomial-copy learnability by $`\sum_i(1-\eta_i^2)=O(\log n)`$. Its channel converse also contains the exact two-copy collision identity. In the present unital model, writing $`\Omega_{1,2}`$ for the Haar-alternative mixture and $`\mathcal K=\mathcal N_\eta^*\mathcal N_\eta`$, this is
```math
\chi^2(\Omega_{1,2}\Vert\tau^{\otimes2})
=\frac{\|\mathcal K\|_{\mathrm{HS}}^2-1}{(d+1)^2}.
```
The present result gives a sharp Haar-average rate and a pair-versus-collective consequence. The noise-budget criterion and collective fixed-noise obstruction remain attributed to that earlier work. It does not settle the previous repository's optimal worst-case pure-source exponent. [NoiseBudget26](https://github.com/GoGoKo699/Quantum-Purity-Noise-Budget/tree/c110b915aaff4d96230aa553486620136028ddbd), especially [channel_bound.md](https://github.com/GoGoKo699/Quantum-Purity-Noise-Budget/blob/c110b915aaff4d96230aa553486620136028ddbd/science/channel_bound.md).

## Collective quadratic estimators

Quantum U-statistics, including sums of a fixed kernel over subsets of copies, were introduced by Guţă and Butucea. Dasgupta, Warsi, and Chatterjee subsequently establish uniqueness and general variance, efficiency, and concentration properties; their v2 contains purity and squared Hilbert–Schmidt applications and a variance appendix. These are methodological antecedents to the all-pair observable. The channel-dependent kernel, its exact Haar moments, and the matching sample law are the specialized calculations required here. [GB10](https://arxiv.org/pdf/1004.2452v2), [DWC26](https://arxiv.org/html/2609.08745v2), Sections III–V and Appendix C.

O'Donnell and Wright establish optimal general mixedness testing. Bădescu, O'Donnell, and Wright provide collective polynomial-observable methods and a Hilbert–Schmidt tester. In the extended v3, Theorem 7.13 bounds the latter estimator's variance by $`O(m^{-2}+\|\rho-\sigma\|_2^2/m)`$. These results provide useful tools, but do not directly state the present local-channel Haar law. [OW15](https://arxiv.org/abs/1501.05028), [BOW19](https://arxiv.org/pdf/1708.06002v3).

For comparison, our own second-moment calculation gives
```math
\mathbb E_\psi\|\mathcal N_\eta(\psi)-I/d\|_2^2
=\frac{(1+3\eta^2)^n-1}{d(d+1)}.
```
Substitution of this typical scale into the standard unweighted Hilbert–Schmidt guarantee yields the scale $`[4/(1+3\eta^2)]^n`$, whereas the noise-weighted observable yields $`[2/\sqrt{1+3\eta^4}]^n`$. Their ratio has base greater than one because
```math
4(1+3\eta^4)-(1+3\eta^2)^2=3(1-\eta^2)^2\gt 0.
```
This compares a standard guarantee; it is not a lower bound for all spectrum-based algorithms.

## Mixture divergences and the converse

O'Donnell and Wadhwa explicitly introduce the quantum Ingster–Suslina method. Their Lemma 4.3, Eqs. (4.2)–(4.3), supplies the mixture-$`\chi^2`$ identity and its exponential reduction. Their Lemma 4.5 bounds moments for globally unitarily invariant perturbations with bounded operator norm. The [converse here](../science/collective_lower_bound.md) uses this established mixture-divergence framework and evaluates the specific channel-structured Haar prior by conditioning and an exact centered Haar-moment bound. The output ensemble is invariant under local unitaries but not under all global unitaries: Pauli directions of different weights have different variances. The globally invariant estimate therefore does not directly give this channel-dependent exponent. Neither mixture second moments nor prior conditioning should be advertised as a new general method. [OW26](https://arxiv.org/html/2507.06010v1), Sections 3–4.

Lee and Wadhwa characterize multiplicative purity estimation with single-copy measurements. Section 5 uses globally depolarized Haar spikes for a nonadaptive lower bound. Section 6 instead uses isotropic Gaussian perturbations of the maximally mixed state; Appendix A proves a simulation of adaptive single-copy POVMs by noisy linear queries. Their result supplies further statistical context, including conditioning on valid instances, but not the local-depolarizing Haar collective-copy law. [LW26](https://arxiv.org/pdf/2609.40248v1), Lemma 5.3, Proposition 5.4, Section 6, and Appendix A.

## Other multi-copy separations and implementation tools

Nöller, Tran, Gachechiladze, and Kueng construct an infinite family of Weyl–Heisenberg learning tasks exhibiting sharp separations between different numbers of jointly measured copies. This work is an antecedent for multi-copy hierarchies in general; its tasks differ from the noisy purity problem here. [NTGK26](https://arxiv.org/html/2510.08070v2).

The [measurement construction](../science/measurement_resources.md) uses established block-encoding and qubitization machinery. Low and Chuang provide qubitization of a Hamiltonian represented as a projection of a unitary. Gilyén, Su, Low, and Wiebe provide block-encoding composition rules; Lemma 52 covers linear combinations and Lemma 53 products in arXiv v1. The construction supplies the particular address preparation and selection circuits, normalization, register routing, precision, and gate count for the present statistic. These citations do not themselves supply data loading or QRAM. [LC19](https://arxiv.org/abs/1610.06546v3), [GSLW19](https://arxiv.org/pdf/1806.01838v1), Sections 4.3–4.4.


## Finite gate synthesis

The finite-library resource bound uses the constructive Solovay–Kitaev guarantee of Dawson and Nielsen, [*The Solovay–Kitaev algorithm*](https://arxiv.org/abs/quant-ph/0505030), Quantum Information and Computation 6, 81–95 (2006). The proof allocates a per-rotation error and uses a hybrid argument to control the complete measurement distribution. This compilation theorem does not supply protected storage or a fault-tolerance overhead.
