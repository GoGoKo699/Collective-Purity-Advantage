# What the optimal rate measures

## A source test after a known channel

The experiment distinguishes two source hypotheses. The pure state is unknown, fixed across all copies, and Haar distributed before acquisition. Local noise creates an anisotropic distribution of output Pauli coefficients: a string of weight $`w`$ is attenuated by $`\eta^w`$. The output reference state remains maximally mixed.

The [main theorem](model.md) concerns this source ensemble. It does not estimate arbitrary output purity to a relative accuracy, and its upper guarantee does not hold uniformly for every pure input. The [converse](collective_lower_bound.md) is unrestricted over measurements, while the [constructive test](collective_measurement.md) attains its exponential copy rate using the known noise pattern.

## Why the fourth power of attenuation appears

Let $`\lambda_P=\eta^{w(P)}`$ and consider a Pauli-diagonal two-copy kernel

```math
W_a=\sum_{P\ne I}a_P P\otimes P.
```

Under the null, Pauli orthogonality gives

```math
\mathrm{Tr}(W_a\tau^{\otimes2})=0,
\qquad
\mathrm{Tr}(W_a^2\tau^{\otimes2})=\sum_{P\ne I}a_P^2.
```

Under the fixed Haar-source alternative, the averaged signal is

```math
\mathbb E_\psi\mathrm{Tr}(W_a\sigma_\psi^{\otimes2})
=\frac{1}{d+1}\sum_{P\ne I}a_P\lambda_P^2.
```

Cauchy–Schwarz therefore gives

```math
\frac{\left(\sum_{P\ne I}a_P\lambda_P^2\right)^2}
{\sum_{P\ne I}a_P^2}
\leq\sum_{P\ne I}\lambda_P^4
=(1+3\eta^4)^n-1=L.
```

The chosen weights $`a_P=\lambda_P^2`$ attain this ratio. They match the covariance of the received Haar ensemble. This explains the kernel; by itself, the calculation optimizes only this kernel family. Global optimality comes from the separate [collective converse](collective_lower_bound.md), and the alternative-hypothesis error requires the full third and fourth moments.

The same $`L`$ is the nonidentity Hilbert–Schmidt spectral weight of the round-trip channel $`\mathcal N_\eta^*\mathcal N_\eta`$. The testing scale is $`t_{n,\eta}=\sqrt{d(d+1)/L}`$. Two noise factors enter the round trip, and squaring its spectrum produces the fourth power.

## How collective processing changes sampling

At the maximally mixed state, overlapping terms of the collective pair sum have zero covariance. The spectral variance is therefore

```math
\mathrm{Var}_0(U_m)=\frac{L}{\binom m2}.
```

The standard deviation is proportional to $`\sqrt L/m`$, while the averaged signal is $`L/(d+1)`$. Their balance gives $`m\asymp d/\sqrt L`$. A protocol that measures fresh disjoint pairs obtains only linearly many independent pair outcomes; its elementary weighted-pair estimator instead needs order $`d^2/L`$ copies.

This comparison of explicit estimators is supplemented by the cited adaptive two-copy lower bound in [Pair measurements](pair_comparison.md). That theorem is needed to cover every adaptive pair strategy. A small chi-square divergence of a single averaged pair is insufficient, because all rounds share the same unknown source.

The observable uses all pairs algebraically, but it is one quantum measurement. It does not copy unknown states or assert that overlapping pair observables can be measured simultaneously. Its [circuit construction](measurement_resources.md) implements approximate spectral discrimination on the original retained input registers.

## Resources and physical meaning

For every fixed $`0\lt\eta\lt1`$, the optimal number of copies remains exponential in $`n`$. The collective advantage is an exponential ratio of sample counts in the stated parameter range. The construction uses a protected register holding every sample and a gate count polynomial in that already exponential input size. Its resource analysis supplies an explicit acquisition-to-decision protocol without QRAM; it does not establish a shallow laboratory implementation or a computational speedup.

The architectural separation asks what ideal coherent processing can recover from noisy acquisitions. It does not model noise accumulating during storage or measurement. A memory threshold, fault-tolerant overhead, unknown-noise calibration problem, and worst-case pure-source upper bound are separate problems. They are not assumed resolved by the sharp Haar-average law.

## Relation to the existing noise-budget result

[Quantum Purity Noise Budget](https://github.com/GoGoKo699/Quantum-Purity-Noise-Budget/tree/c110b915aaff4d96230aa553486620136028ddbd) establishes an unrestricted collective obstruction and a polynomial-learnability criterion in a worst-case pure-source task. The channel, collision framework and fixed-noise hardness are shared foundations. The present project sharpens a specified Bayesian source-ensemble problem and derives its collective-versus-adaptive-pair consequence. It does not settle the earlier project's optimal worst-case exponent. The precise inheritance and external comparisons are in [Related work](../references/RELATED_WORK.md).
