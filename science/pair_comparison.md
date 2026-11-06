# Adaptive pair measurements and the collective advantage

Use the [fixed-source model](model.md), with $`d=2^n`$, $`S=(1+3\eta^4)^n`$, $`A=S-1=L`$, $`M=t_{n,\eta}=\sqrt{d(d+1)/A}`$, and $`\bar\mu=A/(d+1)`$. The collective law is proved in the [main theorem and converse](collective_lower_bound.md). This page compares it with the model that permits arbitrary two-copy measurements per round, unrestricted classical adaptation, and no quantum register retained between rounds.

The pair upper bound below uses the [weighted two-copy kernel](collective_measurement.md) and the same [finite concentration cutoff](haar_moments.md#uniform-moment-bounds-and-a-finite-concentration-cutoff). The adaptive lower bound is an imported theorem, with the model match explained explicitly.

## An explicit repeated-pair upper bound

There is also an elementary protocol using only two copies at a time. On every fresh pair, measure corresponding physical qubits in the Bell basis. If $`k`$ of the $`n`$ outcomes are singlets, report

```math
 Y=(1+\eta^2)^{n-k}(1-3\eta^2)^k-1.
```

This is exactly the spectral measurement of $`W`$. The signed factor for singlet outcomes is retained, including when $`\eta\gt 1/\sqrt3`$. Repeat on $`r`$ fresh pairs and average the results. Conditioned on the one fixed $`\psi`$, these measurements are independent and have mean $`\mu_\psi`$.

Under the null and Haar alternative respectively,

```math
 \operatorname{Var}_0\overline Y=\frac Ar,\qquad
 \operatorname{Var}_1\overline Y
 \le\frac{2S}{r}+\operatorname{Var}_{\rm Haar}(\mu_\psi).
```

The second inequality uses the already-established pair second moment
$`\mathbb E_\psi\operatorname{Tr}(W^2\sigma_\psi^{\otimes2})\le2S`$.
It does not assume that Haar-averaged pairs are independent. The extra variance term explicitly retains their shared unknown source.

For $`r=C_2M^2`$,

```math
 \frac{\operatorname{Var}_0\overline Y}{\bar\mu^2}
 =\frac{d+1}{C_2d},\qquad
 \frac{\operatorname{Var}_1\overline Y}{\bar\mu^2}
 \le\frac{2S}{A}\frac{d+1}{C_2d}+\delta_{n,\eta}.
```

At the same cutoff $`n\ge n_0(\eta)`$, use $`S/A\le2`$, $`(d+1)/d\le3/2`$, and $`\delta_{n,\eta}\le1/64`$. For $`r=\lceil128M^2\rceil`$, Chebyshev's inequality at threshold $`\bar\mu/2`$ gives equal-prior risk at most
$`15/128+1/32=19/128\lt 1/6`$.
In particular,

```math
 m_{\rm pair}\le 2r=O_\eta(M^2).
```

Each pair requires $`O(n)`$ Bell-decoding gates and measurements, $`2n`$ coherent data qubits, and a classical streaming accumulator. The $`n+1`$ possible values of $`Y`$ can be precomputed; the record of a pair need only retain $`k`$. Polynomially many bits in $`n`$ suffice for the classical arithmetic at the displayed accuracy. This protocol does not require quantum memory between pair experiments.


### Finite classical precision

The Bell-basis measurement itself is independent of $`\eta`$. Its reported value has magnitude at most $`c+1`$, where $`c=(1+\eta^2)^n`$, and its derivative is bounded by $`O_\eta(nc)`$, including when the singlet factor vanishes. Certified $`O_\eta(n+\log n)`$-bit arithmetic therefore suffices to give every reported value error at most $`\bar\mu/16`$, and the threshold error at most $`\bar\mu/16`$. The sample average retains this deterministic error bound. Select the number of pairs from a certified upper bound on $`M`$, as in the [collective parameter prescription](measurement_resources.md#finite-gate-precision-and-the-supplied-value-of-eta).

Using the resulting $`\bar\mu/8`$ decision margin, the same variance bounds give equal-prior risk at most

```math
\frac{32}{9}\left(\frac{15}{2\cdot128}+\frac1{64}\right)
=\frac{19}{72}\lt \frac13.
```

Thus finite classical precision preserves the stated $`O_\eta(M^2)`$ copy upper bound. The parameter is supplied with certified accuracy; no calibration experiment is included.

## Exactly where the quadratic separation is proved

Define the pair model as arbitrary POVMs on two fresh received copies in each round, with unrestricted classical adaptation and no persistent quantum register between rounds. Cotler, Gong, and Kannan, Theorem E.2 and Eq. (31), prove for this same fixed-Haar-source task

```math
 m_{\rm pair}
 =\Omega\!\left(\min\left\{2^{n/2},
       \left(\frac4{1+3\eta^4}\right)^n\right\}\right).
```

Their convention is $`\eta=1-\lambda`$. The text preceding the theorem permits a single initial depolarizing layer followed by arbitrary pair processing; the proof is a fully adaptive learning-tree argument [CGK, Appendix E.1](https://arxiv.org/html/2512.10929v2). The lower bound is therefore inherited from that theorem, not inferred from the Haar-averaged two-copy marginal.

Let

```math
 b=1+3\eta^4,\qquad
 \gamma=1-\tfrac12\log_2b,\qquad
 M=\Theta_\eta(2^{\gamma n}).
```

Combining that lower bound with the explicit pair protocol and the collective result gives

```math
 m_{\rm collective}=\Theta_\eta(M),\qquad
 \Omega_\eta\!\left(\min\{2^{n/2},M^2\}\right)
 \le m_{\rm pair}\le O_\eta(M^2).
```

The exact quadratic regime certified by these bounds is

```math
 \boxed{\left(\frac{2\sqrt2-1}{3}\right)^{1/4}
             \le\eta\lt 1.}
```

Indeed this is precisely $`b\ge2\sqrt2`$, or $`2\gamma\le1/2`$, where the inherited lower bound selects $`M^2`$. The lower endpoint is approximately $`0.8835662126`$ and is included. Throughout this regime,

```math
 m_{\rm pair}=\Theta_\eta(M^2),\qquad
 m_{\rm collective}=\Theta_\eta(M),
```

so the optimal sample counts have a quadratic relation and their ratio grows exponentially in $`n`$.

In the intermediate regime

```math
 3^{-1/4}\lt \eta\lt \left(\frac{2\sqrt2-1}{3}\right)^{1/4},
```

the inherited lower bound gives $`m_{\rm pair}=\Omega(\sqrt d)`$. Its ratio to the collective upper bound is at least a constant times

```math
 \frac{\sqrt d}{M}
 =\Theta_\eta\!\left[\left(\frac b2\right)^{n/2}\right],
```

which is exponential, but the exact optimal pair exponent is not fixed by these bounds. At and below $`\eta=3^{-1/4}\approx0.7598356857`$, the quoted pair lower bound does not certify an exponential separation from the collective law. It does not show that no such separation exists. The collective lower bound also applies to pair learners and should be retained whenever it is stronger.

