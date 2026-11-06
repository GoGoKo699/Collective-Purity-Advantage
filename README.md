# Collective Purity Advantage

**How many noisy copies are needed to identify a pure source, and what changes when they can be measured together?**

Consider a maximally mixed $`n`$-qubit source versus one Haar-random pure source, drawn once and then fixed. Each copy passes independently through known local depolarization $`\mathcal D_\eta^{\otimes n}`$, with fixed $`0\lt\eta\lt1`$. The optimal number of received copies for constant average error with unrestricted collective measurements is

```math
m_{\mathrm{collective}}
=\Theta_\eta\!\left[
\left(\frac{2}{\sqrt{1+3\eta^4}}\right)^n
\right].
```

The [main theorem](science/model.md) proves matching collective lower and upper bounds, with explicit finite-error constants. The upper measurement uses the known noise pattern to weight Pauli correlations. Its [gate construction](science/measurement_resources.md) uses explicit register routing and no QRAM.

## The measurement consequence

Write $`d=2^n`$ and $`M=\sqrt{d(d+1)/[(1+3\eta^4)^n-1]}`$. The following statements are asymptotic at fixed $`\eta`$ under the same fixed-source prior.

| Measurement capability | Copy complexity |
| --- | --- |
| Arbitrary collective processing | $`\Theta_\eta(M)`$ |
| Adaptive two-copy rounds, classical memory between rounds | At least $`\Omega_\eta(\min\{\sqrt d,M^2\})`$ and at most $`O_\eta(M^2)`$ |
| Adaptive two-copy rounds when $`\eta\ge[(2\sqrt2-1)/3]^{1/4}`$ | $`\Theta_\eta(M^2)`$ |

The adaptive two-copy lower bound is [established prior work by Cotler, Gong and Kannan](references/RELATED_WORK.md#adaptive-two-copy-learning). The pair upper bound is an explicit repeated Bell-measurement protocol. The [comparison](science/pair_comparison.md) proves an exponential collective sample advantage throughout

```math
3^{-1/4}\lt\eta\lt1.
```

For $`[(2\sqrt2-1)/3]^{1/4}\le\eta\lt1`$, the optimal pair and collective copy counts have a quadratic relation. Below that range the bounds retain their precise scope; they do not characterize the optimal pair exponent in every noise regime.

## Read the science

Start with the [model, main theorem and endpoints](science/model.md). The [scientific reading route](science/README.md) connects the full account.

| To inspect | Read |
| --- | --- |
| A lower bound against every collective POVM | [Conditioned Haar converse](science/collective_lower_bound.md) |
| The attaining measurement and its finite-error guarantee | [Collective pair-sum measurement](science/collective_measurement.md) |
| Exact finite-dimensional contractions and source concentration | [Haar moments](science/haar_moments.md) |
| Register routing, eigenvalue discrimination, precision and gate costs | [Measurement resources](science/measurement_resources.md) |
| The adaptive-pair comparison and exact separation ranges | [Pair experiments](science/pair_comparison.md) |
| Why the channel spectrum controls the sample rate | [Interpretation](science/interpretation.md) |
| Established methods and the precise contribution | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| Direct finite-matrix checks and their limits | [Verification](verification/README.md) |

## Learn the argument

The [learning route](learning/README.md) uses John Watrous's *The Theory of Quantum Information* (2018) as its educational anchor. The [source-to-project bridge](learning/BRIDGE.md) translates the relevant state-discrimination and Haar-measure foundations into this problem, beginning with a complete one-qubit example.

The [30-milestone map](learning/MILESTONES.md) has 11 background/preliminaries milestones and 19 narrative/innovation milestones. It develops the measurement, its statistical guarantee and converse, and the collective-versus-pair consequence, with dependencies and direct source pointers.

[The reading guide](llms.txt) maps scientific and learning questions to their authoritative files.

## Reproduce the finite checks

From the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/verify_moments.py
```

The deterministic checks build the physical noisy Haar third moment and the actual collective observable, then independently contract the fourth Haar moment to verify the signal variance. They support the normalization and moment calculations in the tested small systems. The general converse, finite-error theorem, asymptotic rate and circuit costs are established by the analytical arguments.

## Scope

The pure source is fixed across all samples, and the performance guarantee is Haar averaged. The matching upper bound is not uniform over all pure states. The noise parameter is known, and noise acts once during acquisition. Downstream processing and storage are protected.

At fixed nonzero noise, both sample costs remain exponential in $`n`$. The direct collective construction stores $`mn`$ protected input qubits and uses a gate count polynomial in the already exponential input size. Its sample advantage does not imply a computational speedup or a small-memory implementation. [Interpretation](science/interpretation.md) explains these distinctions and the relation to the earlier [Quantum Purity Noise Budget](https://github.com/GoGoKo699/Quantum-Purity-Noise-Budget/tree/c110b915aaff4d96230aa553486620136028ddbd).

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
