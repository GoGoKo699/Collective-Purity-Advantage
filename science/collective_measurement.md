# The collective measurement and its finite-error guarantee

The [model](model.md) defines the source mixture and the exact scale $`t_{n,\eta}`$. This page constructs one collective observable and proves its performance using the exact [Haar moment formulas](haar_moments.md). Its pair terms share input registers. The measurement is of their Hermitian sum, rather than a sequence of measurements on overlapping pairs.

## A collective pair-sum observable

Define a Hermitian observable on two copies by

```math
W=\sum_{P\neq I}\eta^{2w(P)}P\otimes P
=\bigotimes_{j=1}^n
\big[I+\eta^2(X\otimes X+Y\otimes Y+Z\otimes Z)\big]-I.
\qquad\text{(32)}
```

For $`m\geq2`$, set

```math
U_m=\binom m2^{-1}\sum_{1\leq a\lt b\leq m}W_{ab}.
\qquad\text{(33)}
```

The test measures the spectral projectors of $`U_m`$ and chooses $`H_1`$ exactly when the measured eigenvalue is at least $`\overline\mu/2`$, where

```math
\mu_\psi=\mathrm{Tr}(W\sigma_\psi^{\otimes2})
=\sum_{P\neq I}\eta^{4w(P)}r_P^2,
\qquad
\overline\mu=\mathbb E_\psi\mu_\psi=\frac{L}{d+1}.
\qquad\text{(34)}
```

The overlapping terms in (33) need not commute. Nevertheless $`U_m`$ is Hermitian and its spectral measurement is allowed by the model. Separately measuring overlapping pair terms would define a different procedure.

For a fixed source $`\psi`$, write

```math
\begin{aligned}
A_\psi&=\mathrm{Tr}(W^2\sigma_\psi^{\otimes2}),\\
H_\psi&=\mathrm{Tr}_2[W(I\otimes\sigma_\psi)]
=\sum_{P\neq I}\eta^{3w(P)}r_PP,\\
B_\psi&=\mathrm{Tr}(\sigma_\psi H_\psi^2).
\end{aligned}
\qquad\text{(35)}
```

In particular, $`H_\psi`$ is Hermitian, $`B_\psi\geq0`$, and

```math
\mathrm{Tr}(W_{12}W_{13}\sigma_\psi^{\otimes3})
=B_\psi.
\qquad\text{(36)}
```

The reversed ordering has the same real expectation. Disjoint pairs have expectation $`\mu_\psi^2`$. There are $`\binom m2`$ identical ordered edge pairs, and each edge has $`2(m-2)`$ distinct edges sharing one vertex. Therefore

```math
\mathrm{Var}_{\sigma_\psi^{\otimes m}}(U_m)
=\frac{2(A_\psi-\mu_\psi^2)}{m(m-1)}
+\frac{4(m-2)(B_\psi-\mu_\psi^2)}{m(m-1)}.
\qquad\text{(37)}
```

In particular,

```math
\mathrm{Var}(U_m\mid\psi)
\leq\frac{2A_\psi}{m(m-1)}+\frac{4B_\psi}{m}.
\qquad\text{(38)}
```

Under $`H_0`$, $`H=0`$, the mean is zero, and Pauli orthogonality gives

```math
\mathrm{Var}_0(U_m)=\frac{2L}{m(m-1)}.
\qquad\text{(39)}
```

## Finite-error upper bound

The spectral outcome under $`\Omega_{1,m}`$ is a mixture of the spectral outcome distributions for the fixed states $`\sigma_\psi^{\otimes m}`$. Thus the total-variance identity is

```math
\mathrm{Var}_1(U_m)
=\mathbb E_\psi\mathrm{Var}(U_m\mid\psi)
+\mathrm{Var}_\psi(\mu_\psi).
\qquad\text{(64)}
```

This step retains the shared source across all copies. Applying (38) and (52) gives

```math
\mathrm{Var}_1(U_m)
\leq\frac{4S}{m(m-1)}
+\frac{12S^{3/2}}{dm}
+\mathrm{Var}_\psi(\mu_\psi).
\qquad\text{(65)}
```

Suppose $`n\geq n_0(\eta)`$, $`C\geq2`$, and $`m\geq Ct_{n,\eta}`$. Since $`S\leq d^2`$, one has $`t_{n,\eta}\gt 1`$, so $`m\geq2`$ and $`m(m-1)\geq m^2/2`$. From (39),

```math
\frac{\mathrm{Var}_0(U_m)}{\overline\mu^2}
\leq\frac{4(d+1)^2}{m^2L}
\leq\frac4{C^2}\frac{d+1}{d}
\leq\frac6{C^2}.
\qquad\text{(66)}
```

For (65), the same substitutions, $`S/L\leq2`$, and $`(d+1)/d\leq3/2`$ give

```math
\begin{aligned}
\frac{\mathrm{Var}_1(U_m)}{\overline\mu^2}
&\leq
\frac8{C^2}\frac{S}{L}\frac{d+1}{d}
+\frac{12}{C}
\left(\frac{S}{L}\frac{d+1}{d}\right)^{3/2}
+\delta_{n,\eta}\\
&\leq\frac{24}{C^2}+\frac{36\sqrt3}{C}+\delta_{n,\eta}\\
&\leq\frac{24}{C^2}+\frac{64}{C}+\delta_{n,\eta}.
\end{aligned}
\qquad\text{(67)}
```

Let $`\alpha_m`$ be the error probability under $`H_0`$, and let $`\beta_m`$ be the error probability under the Haar-averaged $`H_1`$. Their means are respectively $`0`$ and $`\overline\mu`$, while the threshold is $`\overline\mu/2`$. Chebyshev's inequality therefore yields

```math
\alpha_m\leq\frac{24}{C^2},
\qquad
\beta_m\leq\frac{96}{C^2}+\frac{256}{C}+4\delta_{n,\eta}.
\qquad\text{(68)}
```

Using $`C=1024`$ and (63), each of these errors is less than $`1/3`$. Their equal-prior average obeys the stronger bound

```math
R_m=\frac{\alpha_m+\beta_m}{2}
\leq\frac{60}{1024^2}+\frac{128}{1024}+\frac1{32}
=\frac{5}{32}+\frac{60}{1024^2}
\lt \frac16.
\qquad\text{(69)}
```

Taking the ceiling in (7) only increases the number of copies and preserves these inequalities. This proves the upper part of Theorem 1.

## Relation to the quantum U-statistics framework

The collective pair average (33) is a degree-two quantum U-statistic in the framework of [Guţă and Butucea, *Quantum U-statistics*, J. Math. Phys. 51, 102202 (2010)](https://arxiv.org/abs/1004.2452). The proof above specifies its noise-dependent kernel, evaluates its Haar moments without a large-dimension approximation, and supplies the corresponding collective converse for the fixed-source prior in (1). The moment identities and finite-error estimates are derived in full here; no generic asymptotic U-statistics theorem is needed to exchange the growing system dimension with the growing number of copies.

The [measurement resource account](measurement_resources.md) implements an approximate spectral test with an explicit error margin and no QRAM. The [pair comparison](pair_comparison.md) studies a different experiment that uses fresh disjoint pairs in successive rounds.
