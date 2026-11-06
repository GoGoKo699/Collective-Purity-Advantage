# A converse for arbitrary collective measurements

Use the [statistical model](model.md) and [Haar tensor identity](haar_moments.md#haar-moments-and-pauli-conventions). The goal is to bound the trace distance between the actual fixed-source mixture and the null state for every collective POVM. A small exceptional set of Haar states is conditioned away before bounding the collision integral; its discarded mass is then paid explicitly in trace distance.

The mixture collision method is established quantum testing machinery. The channel-specific evaluation here uses the centered round-trip spectrum and Haar moment contractions; [Related work](../references/RELATED_WORK.md) identifies the imported framework and prior conditioning arguments.

## Collective lower bound by trimming the Haar prior

Set

```math
\mathcal K=\mathcal N_\eta^*\mathcal N_\eta
=\mathcal D_{\eta^2}^{\otimes n}.
\qquad\text{(16)}
```

This is a self-adjoint, unital, trace-preserving positive channel. For a pure state $`\phi`$, define

```math
B_\phi=\mathcal K(\phi)-\tau,
\qquad
q_\phi^2=\mathrm{Tr}(B_\phi^2).
\qquad\text{(17)}
```

By (12) and (15),

```math
v:=\mathbb E_\phi q_\phi^2
=\frac1d\sum_{P\neq I}\eta^{4w(P)}\mathbb E r_P^2
=\frac{L}{d(d+1)}
=t_{n,\eta}^{-2}.
\qquad\text{(18)}
```

### A centered Haar moment bound

Fix $`\phi`$, and draw $`\psi`$ independently from Haar measure. Put

```math
\xi=d\mathrm{Tr}(\psi B_\phi).
\qquad\text{(19)}
```

Since $`\mathrm{Tr}B_\phi=0`$, every permutation with a one-cycle vanishes in the contraction of (14). Consequently,

```math
\mathbb E_\psi\xi^k
=\frac{d^k}{(d)_k}
\sum_{\substack{\pi\in\mathfrak S_k\\\pi\text{ has no fixed points}}}
\prod_{c\text{ cycle of }\pi}
\mathrm{Tr}(B_\phi^{|c|}).
\qquad\text{(20)}
```

For every integer $`\ell\geq 2`$, the Schatten-norm inequality gives

```math
\left|\mathrm{Tr}(B_\phi^\ell)\right|
\leq\mathrm{Tr}|B_\phi|^\ell
\leq\big(\mathrm{Tr}B_\phi^2\big)^{\ell/2}
=q_\phi^\ell.
\qquad\text{(21)}
```

Let $`D_k`$ be the number of derangements of $`k`$ elements. Since $`d^k/(d)_k\leq 1`$, (20) implies

```math
|\mathbb E_\psi\xi^k|\leq D_kq_\phi^k.
\qquad\text{(22)}
```

Also $`\mathbb E\xi=0`$, and

```math
1+\xi=d\mathrm{Tr}[\psi\mathcal K(\phi)]\geq 0.
\qquad\text{(23)}
```

For an integer $`m`$ with $`m q_\phi\lt 1`$, expanding the power and using $`D_k\leq k!`$ yields

```math
\begin{aligned}
\mathbb E_\psi(1+\xi)^m
&\leq 1+\sum_{k=2}^m\binom mkD_kq_\phi^k\\
&\leq 1+\sum_{k=2}^{\infty}(m q_\phi)^k\\
&=1+\frac{(m q_\phi)^2}{1-m q_\phi}.
\end{aligned}
\qquad\text{(24)}
```

This is a bound conditional on $`\phi`$; no replacement of $`q_\phi`$ by its average has been made.

### Truncation and the collision integral

Let

```math
G=\{\phi:q_\phi^2\leq16v\},
\qquad p=\Pr_\phi(G).
\qquad\text{(25)}
```

Markov's inequality gives $`p\geq15/16`$. Let $`\Omega_{G,m}`$ be the alternative state in (1) with the Haar prior conditioned on $`G`$. Because the null is maximally mixed, its collision divergence is

```math
\begin{aligned}
1+\chi^2(\Omega_{G,m}\|\tau^{\otimes m})
&=d^m\mathrm{Tr}(\Omega_{G,m}^2)\\
&=\frac1{p^2}\int_{G\times G}
\big[d\mathrm{Tr}(\psi\mathcal K(\phi))\big]^m
\,d\psi\,d\phi.
\end{aligned}
\qquad\text{(26)}
```

Here

```math
\mathrm{Tr}[\mathcal N_\eta(\psi)\mathcal N_\eta(\phi)]
=\mathrm{Tr}[\psi\mathcal K(\phi)]
\qquad\text{(27)}
```

accounts for the two channel applications. The kernel in (26) is nonnegative by (23). We may therefore enlarge the integration domain for $`\psi`$ from $`G`$ to the full Haar space, while keeping $`\phi\in G`$.

If $`m\sqrt v\leq1/12`$, then $`m q_\phi\leq1/3`$ on $`G`$. By (24),

```math
1+\chi^2(\Omega_{G,m}\|\tau^{\otimes m})
\leq\frac1p\left(1+\frac{(1/3)^2}{1-1/3}\right)
\leq\frac{16}{15}\frac76
=\frac{56}{45}.
\qquad\text{(28)}
```

Thus $`\chi^2\leq11/45`$. For the trace distance
$`D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1`$, Cauchy–Schwarz gives

```math
D(\Omega_{G,m},\tau^{\otimes m})
\leq\frac12\sqrt{11/45}.
\qquad\text{(29)}
```

The unconditioned alternative is
$`\Omega_{1,m}=p\Omega_{G,m}+(1-p)\Omega_{G^c,m}`$, so

```math
D(\Omega_{1,m},\Omega_{G,m})\leq1-p\leq\frac1{16}.
\qquad\text{(30)}
```

The triangle inequality and the binary discrimination formula now give

```math
\begin{aligned}
R_m^*
&=\frac12\big[1-D(\Omega_{1,m},\tau^{\otimes m})\big]\\
&\geq\frac{15}{32}-\frac14\sqrt{11/45}
\gt \frac13.
\end{aligned}
\qquad\text{(31)}
```

Since $`\sqrt v=t_{n,\eta}^{-1}`$, this proves (5)–(6). The two normalizing factors in (26), the nonnegative-kernel enlargement, and the discarded Haar mass in (30) are all necessary to this argument.

This converse applies to all downstream quantum operations because every such test defines an effect on the received $`m`$-copy state. It places no pair, locality, depth or memory restriction on that effect.
