# Noisy-source purity testing

A source can be pure before acquisition and mixed by the time it reaches the measuring device. The task here is to identify the source using the known pattern of local depolarization. The Haar source is drawn once: observations from different copies retain correlations through that common unknown state.

The main theorem below gives the exact exponential scale of the number of copies. Its lower bound permits every collective POVM; its upper bound is attained by the weighted observable in [Collective measurement](collective_measurement.md). [Haar moments](haar_moments.md) supplies the exact dimension-dependent estimates, and [Measurement resources](measurement_resources.md) makes a concrete implementation and its costs explicit. Equation numbers are unique across these scientific pages.

## Statistical model and theorem

Let $`n\geq 1`$, $`d=2^n`$, and $`\tau=I_d/d`$. For a known parameter $`0\lt \eta\lt 1`$, define

```math
\mathcal D_\eta(X)
=\eta X+(1-\eta)\mathrm{Tr}(X)\frac{I_2}{2},
\qquad
\mathcal N_\eta=\mathcal D_\eta^{\otimes n}.
```

The two hypotheses have equal prior probabilities. Under $`H_0`$, the source is $`\tau`$. Under $`H_1`$, a pure-state projector $`\psi`$ is drawn from Haar measure once and then held fixed. Each supplied copy passes independently through $`\mathcal N_\eta`$. Thus the two density operators available to a measurement on $`m`$ copies are

```math
\Omega_{0,m}=\tau^{\otimes m},
\qquad
\Omega_{1,m}=\int
\sigma_\psi^{\otimes m}\,d\psi,
\qquad
\sigma_\psi=\mathcal N_\eta(\psi).
\qquad\text{(1)}
```

All processing after this noise layer is unrestricted, and an arbitrary joint POVM on the $`m`$ outputs is permitted. The source is not re-randomized between copies. For a binary effect $`0\leq E\leq I`$, where outcome $`E`$ means $`H_1`$, its equal-prior error is

```math
R_m(E)=\frac12\mathrm{Tr}(E\Omega_{0,m})
+\frac12\mathrm{Tr}[(I-E)\Omega_{1,m}].
\qquad\text{(2)}
```

Write $`R_m^*=\inf_E R_m(E)`$, and let $`m_*(n,\eta)`$ be the least integer $`m`$ for which $`R_m^*\leq 1/3`$.

Define

```math
s=1+3\eta^4,\qquad S=s^n,\qquad L=S-1,
\qquad
t_{n,\eta}=\sqrt{d(d+1)/L},
\qquad\text{(3)}
```

and

```math
\begin{aligned}
a_\eta&=\frac{1+3\eta^8}{(1+3\eta^4)^2}\in(0,1),\\
n_0(\eta)&=\max\left\{
1,
\left\lceil\frac{\log 2}{\log(1+3\eta^4)}\right\rceil,
\left\lceil\frac{\log 1024}{-\log a_\eta}\right\rceil
\right\}.
\end{aligned}
\qquad\text{(4)}
```

All logarithms in (4) may be taken in any common base.

### Theorem 1

For every $`n\geq 1`$ and $`0\lt \eta\lt 1`$, if

```math
m\leq \frac{t_{n,\eta}}{12},
\qquad\text{(5)}
```

then every collective measurement has equal-prior error

```math
R_m^*\geq
\frac{15}{32}-\frac14\sqrt{11/45}
\gt \frac13.
\qquad\text{(6)}
```

For every $`n\geq n_0(\eta)`$, there is a collective measurement using

```math
m=\left\lceil 1024\,t_{n,\eta}\right\rceil
\qquad\text{(7)}
```

copies whose equal-prior error satisfies

```math
R_m\leq\frac{5}{32}+\frac{60}{1024^2}\lt \frac16.
\qquad\text{(8)}
```

In particular,

```math
\frac{t_{n,\eta}}{12}
\lt m_*(n,\eta)
\leq \left\lceil 1024\,t_{n,\eta}\right\rceil
\qquad(n\geq n_0(\eta)),
\qquad\text{(9)}
```

and, for every fixed $`0\lt \eta\lt 1`$,

```math
\boxed{
m_*(n,\eta)
=\Theta_\eta\!\left(
\left[\frac{2}{\sqrt{1+3\eta^4}}\right]^n
\right).
}
\qquad\text{(10)}
```

The upper bound is a Haar-average statement for (1). It does not assert the same performance for every pure source. Its measurement is an ideal collective spectral measurement; a circuit or memory restriction is not part of this theorem.

## Access and resource contract

The single acquisition channel acts independently on each qubit and copy. Its parameter is known. The learner receives no environmental record, source-preparation circuit, inverse preparation oracle, or pre-noise encoding opportunity. Protected downstream gates and storage are allowed. The direct collective construction holds every received copy, so its memory includes all $`mn`$ input qubits. The analysis counts sample, gate and memory resources separately.

An adaptive two-copy strategy receives two fresh outputs per round, may perform an arbitrary joint POVM chosen using the complete preceding classical transcript, and retains no quantum state between rounds. This is the model of the cited [adaptive-pair lower bound](pair_comparison.md). The collective class includes such protocols but can retain and jointly process a larger register.

The upper theorem concerns average error under the stated Haar prior. A lower bound for this prior also lower-bounds worst-case pure-source testing, but the matching upper theorem does not establish a worst-case exponent. The parameter is fixed as $`n`$ grows; a simultaneous limit $`\eta=\eta_n`$ requires using the displayed finite bounds instead of assuming uniform asymptotic constants.

## Asymptotic rate and the noiseless or fully depolarized endpoints

For fixed $`0\lt \eta\lt 1`$, the exact scale in (3) is

```math
t_{n,\eta}
=\left[\frac{2}{\sqrt{1+3\eta^4}}\right]^n
\sqrt{(1+2^{-n})/[1-(1+3\eta^4)^{-n}]}.
\qquad\text{(70)}
```

The second factor tends to one, and $`1\lt 2/\sqrt{1+3\eta^4}\lt 2`$. Equations (9) and (70) prove (10). The constants in (5) and (7) are universal; only the sufficient starting dimension $`n_0(\eta)`$ depends on the fixed noise parameter.

At $`\eta=0`$, every output is $`\tau`$, so $`R_m^*=1/2`$ for all $`m`$, and $`m_*(n,0)=\infty`$.

At $`\eta=1`$, Haar invariance gives

```math
\Omega_{1,m}=\frac{\Pi_{\mathrm{sym}}^{(m)}}{\binom{d+m-1}{m}}.
\qquad\text{(71)}
```

On the symmetric subspace its eigenvalues are at least those of $`\tau^{\otimes m}`$, and it vanishes on the orthogonal complement. Hence

```math
R_m^*(n,1)=\frac{1}{2d^m}\binom{d+m-1}{m}.
\qquad\text{(72)}
```

For the error target $`1/3`$, this gives $`m_*(1,1)=3`$ and $`m_*(n,1)=2`$ for $`n\geq2`$. One copy is uninformative for every $`\eta`$, since $`\int\sigma_\psi\,d\psi=\tau`$.
