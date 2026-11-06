# Haar moments of the noisy-source statistic

This page derives the second-, third-, and fourth-moment identities used in the [collective test](collective_measurement.md) and [converse](collective_lower_bound.md). The [model and theorem](model.md) define $`d,S,L,t_{n,\eta}`$ and the fixed-source prior. The calculations keep the exact finite dimension and include Pauli phases; the dimension grows together with the copy count.

## Haar moments and Pauli conventions

Let $`\mathcal P_n=\{I,X,Y,Z\}^{\otimes n}`$ denote the Hermitian Pauli strings, with no extra phases. Their normalization is

```math
\mathrm{Tr}(PQ)=d\,\mathbf 1\{P=Q\}.
\qquad\text{(11)}
```

Write $`w(P)`$ for the number of nonidentity factors of $`P`$, and

```math
r_P=\mathrm{Tr}(\psi P),\qquad
\psi=\frac1d\sum_{P\in\mathcal P_n}r_PP,
\qquad
\mathcal N_\eta(P)=\eta^{w(P)}P.
\qquad\text{(12)}
```

In particular, $`r_I=1`$. When $`PQ`$ has a phase, $`w(PQ)`$ means the weight of its underlying Hermitian Pauli string. Define the commutation sign by

```math
PQ=\chi(P,Q)QP,\qquad \chi(P,Q)\in\{+1,-1\}.
\qquad\text{(13)}
```

Then $`(PQ)^2=\chi(P,Q)I`$.

For Haar-random $`\psi`$, the exact tensor moment is

```math
\int\psi^{\otimes k}\,d\psi
=\frac{1}{(d)_k}\sum_{\pi\in\mathfrak S_k}V_\pi,
\qquad
(d)_k=d(d+1)\cdots(d+k-1),
\qquad\text{(14)}
```

where $`V_\pi`$ permutes the tensor factors. Indeed, the Haar average is supported on the symmetric subspace and is invariant under every $`U^{\otimes k}`$. It is therefore the normalized symmetric projector; expanding that projector gives (14). Contracting (14) with $`A_1\otimes\cdots\otimes A_k`$ gives a product of traces, one for each cycle of $`\pi`$.

For nonidentity Pauli strings, the second moment is

```math
\mathbb E r_Pr_Q=\frac{\mathbf 1\{P=Q\}}{d+1}.
\qquad\text{(15)}
```

The identities below use (14) directly, including the phases in Pauli products.

## Exact second-, third-, and fourth-moment contractions

Introduce the scalar quantities

```math
\begin{aligned}
R&=(1+9\eta^4-6\eta^6)^n,\\
V&=(1+3\eta^6)^n,\\
Q_\pm&=(1+6\eta^4+3\eta^6\pm6\eta^7)^n,\\
B_8&=(1+3\eta^8)^n,\\
C_8&=(1+6\eta^4-3\eta^8)^n.
\end{aligned}
\qquad\text{(40)}
```

The following one-site table records all weights needed below. In a table entry $`(P,Q)`$, $`P,Q`$ are single-qubit Paulis. The global sign and weights multiply over sites.

| One-site pair type | Number | $`\chi(P,Q)`$ | $`\eta^{2[w(P)+w(Q)+w(PQ)]}`$ | $`\eta^{3w(P)+3w(Q)+w(PQ)}`$ | $`\eta^{4[w(P)+w(Q)]}`$ |
| --- | ---: | ---: | ---: | ---: | ---: |
| $`(I,I)`$ | 1 | $`+1`$ | $`1`$ | $`1`$ | $`1`$ |
| Exactly one identity | 6 | $`+1`$ | $`\eta^4`$ | $`\eta^4`$ | $`\eta^4`$ |
| Equal nonidentity Paulis | 3 | $`+1`$ | $`\eta^4`$ | $`\eta^6`$ | $`\eta^8`$ |
| Distinct nonidentity Paulis | 6 | $`-1`$ | $`\eta^6`$ | $`\eta^7`$ | $`\eta^8`$ |

### Pair second moment

Expanding $`W^2`$, terms with $`P=Q`$ contribute $`L`$. For $`P\neq Q`$, the operator $`PQ`$ is traceless, and (14) gives

```math
\mathbb E_\psi[\mathrm{Tr}(\psi PQ)]^2
=\frac{\chi(P,Q)}{d+1}.
\qquad\text{(41)}
```

The signed sum of the fourth column of the table is $`R`$. Removing $`P=I`$ or $`Q=I`$ subtracts $`2S-1`$, and then removing $`P=Q\neq I`$ subtracts $`L`$. Hence

```math
\boxed{
\mathbb E A_\psi
=L+\frac{R-3S+2}{d+1}
=\frac{(d-2)L+R-1}{d+1}.
}
\qquad\text{(42)}
```

### Shared-copy overlap

Using (35),

```math
B_\psi
=\sum_{P,Q\neq I}
\eta^{3w(P)+3w(Q)+w(PQ)}
r_Pr_Q\mathrm{Tr}(\psi PQ).
\qquad\text{(43)}
```

For $`P=Q`$, the expectation is $`\mathbb E r_P^2=1/(d+1)`$, so these terms contribute $`(V-1)/(d+1)`$. For distinct nonidentity $`P,Q`$, only the two three-cycles survive in (14). Their traces are $`d`$ and $`d\chi(P,Q)`$, giving

```math
\mathbb E_\psi\big[r_Pr_Q\mathrm{Tr}(\psi PQ)\big]
=\frac{1+\chi(P,Q)}{(d+1)(d+2)}.
\qquad\text{(44)}
```

Thus anticommuting terms vanish. From the fifth column of the table, the total weighted sum over commuting $`P,Q`$, including identities and diagonal pairs, is $`(Q_++Q_-)/2`$. Removing the identity row and column subtracts $`2S-1`$; removing the remaining diagonal subtracts $`V-1`$. Therefore

```math
\begin{aligned}
\mathbb E B_\psi
&=\frac{V-1}{d+1}
+\frac{Q_++Q_--4S-2V+4}{(d+1)(d+2)}\\
&=\boxed{
\frac{d(V-1)+Q_++Q_--4S+2}{(d+1)(d+2)}
}.
\end{aligned}
\qquad\text{(45)}
```

### Fluctuations of the Haar signal

For every nonidentity $`P`$,

```math
\mathbb E r_P^4=\frac{3}{(d+1)(d+3)}.
\qquad\text{(46)}
```

For distinct nonidentity $`P,Q`$, the four-copy contraction gives

```math
\mathbb E r_P^2r_Q^2
=\frac{d+4+2\chi(P,Q)}{(d+1)(d+2)(d+3)}.
\qquad\text{(47)}
```

To verify (47), the only nonzero double-transposition contraction is $`d^2`$. Among the six four-cycles, four have trace $`d`$ and two have trace $`d\chi(P,Q)`$. Dividing their sum by $`(d)_4`$ gives the formula. For (46), all three double transpositions and all six four-cycles contribute, giving $`[3d^2+6d]/(d)_4`$.

The unsigned weight sums satisfy

```math
\sum_{P\neq I}\eta^{4w(P)}=L,
\qquad
\sum_{P\neq I}\eta^{8w(P)}=B_8-1.
\qquad\text{(48)}
```

The signed sum of the last column of the table, over all global Pauli pairs, is $`C_8`$. Excluding identity rows and columns and then diagonal pairs gives

```math
\sum_{\substack{P,Q\neq I\\P\neq Q}}
\chi(P,Q)\eta^{4w(P)+4w(Q)}
=C_8-2S-B_8+2.
\qquad\text{(49)}
```

Combining (46)–(49) yields

```math
\boxed{
\mathbb E\mu_\psi^2
=\frac{(d+4)L^2+2(C_8-2S+1)+2d(B_8-1)}
{(d+1)(d+2)(d+3)}.
}
\qquad\text{(50)}
```

Subtracting $`\overline\mu^2=L^2/(d+1)^2`$ gives

```math
\boxed{
\mathrm{Var}_\psi(\mu_\psi)
=\frac{
2[d(d+1)B_8+(d+1)C_8-S^2-2dS-d^2]
}{(d+1)^2(d+2)(d+3)}.
}
\qquad\text{(51)}
```

## Uniform moment bounds and a finite concentration cutoff

For $`0\leq\eta\leq1`$, the exact moments obey

```math
\mathbb E A_\psi\leq2S,
\qquad
\mathbb E B_\psi\leq\frac{3S^{3/2}}{d}.
\qquad\text{(52)}
```

Here is a short proof of all bounds needed for (52). First,

```math
\begin{aligned}
2(1+3\eta^4)-(1+9\eta^4-6\eta^6)
&=1-3\eta^4+6\eta^6\\
&=(1-\eta^2)^2(1+2\eta^2)+4\eta^6\geq0.
\end{aligned}
\qquad\text{(53)}
```

Thus $`R\leq dS`$, and (42) gives the first bound. Second, monotonicity of the finite-dimensional $`\ell_p`$ norms gives

```math
1+3\eta^6\leq(1+3\eta^4)^{3/2},
\qquad V\leq S^{3/2}.
\qquad\text{(54)}
```

Let $`q_+=1+6\eta^4+3\eta^6+6\eta^7`$. The identity

```math
(1+3\eta^4)(1+3\eta^2)-q_+
=3\eta^2(1-\eta^2)+6\eta^6(1-\eta)\geq0
\qquad\text{(55)}
```

and Cauchy–Schwarz,

```math
1+3\eta^2\leq2\sqrt{1+3\eta^4},
\qquad\text{(56)}
```

imply $`q_+\leq2s^{3/2}`$. Also

```math
0\lt 1+6\eta^4+3\eta^6-6\eta^7
=1+6\eta^4(1-\eta^3)+3\eta^6\leq q_+.
\qquad\text{(57)}
```

Therefore $`0\lt Q_-\leq Q_+\leq dS^{3/2}`$. Dropping the negative terms in (45) and using $`(d+1)(d+2)\geq d^2`$ proves the second bound in (52).

For the signal variance, divide (51) by $`\overline\mu^2`$, discard the negative terms in its numerator, and use $`d(d+1)\leq(d+2)(d+3)`$. This gives

```math
\delta_{n,\eta}:=
\frac{\mathrm{Var}_\psi(\mu_\psi)}{\overline\mu^2}
\leq\frac{2(B_8+C_8/d)}{L^2}.
\qquad\text{(58)}
```

If $`S\geq2`$, then $`L\geq S/2`$, so

```math
\delta_{n,\eta}
\leq8\left(a_\eta^n+b_\eta^n\right),
\qquad
b_\eta=\frac{1+6\eta^4-3\eta^8}{2(1+3\eta^4)^2}.
\qquad\text{(59)}
```

Both bases are positive, and

```math
a_\eta-b_\eta
=\frac{(1-3\eta^4)^2}{2(1+3\eta^4)^2}\geq0,
\qquad
1-a_\eta
=\frac{6\eta^4(1+\eta^4)}{(1+3\eta^4)^2}\gt 0.
\qquad\text{(60)}
```

Consequently,

```math
\boxed{\delta_{n,\eta}\leq16a_\eta^n\quad\text{when }S\geq2.}
\qquad\text{(61)}
```

For every $`u\gt 0`$, this also supplies the explicit source-concentration statement

```math
\Pr_\psi\!\left(
\left|\frac{\mu_\psi}{\overline\mu}-1\right|\geq u
\right)
\leq\frac{16a_\eta^n}{u^2}
\qquad(S\geq2).
\qquad\text{(62)}
```

In particular, (4) ensures both $`S\geq2`$ and

```math
\delta_{n,\eta}\leq\frac1{64}
\qquad(n\geq n_0(\eta)).
\qquad\text{(63)}
```

For example, at this cutoff the Haar probability that $`\mu_\psi`$ differs from $`\overline\mu`$ by at least half of $`\overline\mu`$ is at most $`1/16`$. The test below uses (63) directly through the total variance.

The direct finite-matrix checks in [Verification](../verification/README.md) independently contract the Haar third and fourth tensor moments. The analytical formulas above supply the all-dimension proof.
