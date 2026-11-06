# Implementing the collective measurement

## Model and resource statement

Let $`d=2^n`$, let $`0\lt \eta\lt 1`$ be fixed and known, and use $`M=t_{n,\eta}`$ and $`A=L`$ from the [main theorem](model.md). Thus

```math
 S=(1+3\eta^4)^n,\qquad A=S-1,\qquad
 M=\sqrt{d(d+1)/A},\qquad
 \bar\mu=\frac{A}{d+1}=\frac d{M^2}.
```

The source is either $`I/d`$ or one Haar-random pure state $`\psi`$, sampled once and held fixed. Each supplied copy independently undergoes $`\mathcal D_\eta^{\otimes n}`$ before the learner receives it. All processing discussed here acts on the received copies. The decision guarantee is averaged over the fixed Haar source.

Choose a power of two $`m\ge4096M`$ within a constant factor of this bound. The finite-precision procedure below makes this choice from certified parameter bounds, without an exact-real comparison. The collective statistic is

```math
 W_{ab}=\bigotimes_{j=1}^n
 [I+\eta^2(X_{a,j}X_{b,j}+Y_{a,j}Y_{b,j}+Z_{a,j}Z_{b,j})]-I,
 \qquad
 U_m=\binom m2^{-1}\sum_{a\lt b}W_{ab}.
```

There is an explicit implementation of a constant-error threshold measurement of $`U_m`$ using

```math
 \begin{array}{ll}
 \text{supplied copies:}&m=\Theta_\eta(M),\\
 \text{protected data qubits:}&mn,\\
 \text{additional protected qubits:}&O_\eta(n),\\
 \text{block-encoding queries:}&O_\eta(M^2),\\
 \text{finite-library gates:}&\widetilde O_\eta(nm^3).
 \end{array}
```

The gate bound uses a circuit model with arbitrary two-qubit connectivity and an explicit linear scan of the data registers. It assumes no QRAM or unit-cost addressed access. The tilde hides only polylogarithmic factors in the input size and accuracy. A deliberately conservative conversion to a one-dimensional nearest-neighbor circuit costs at most a further $`O(mn)`$ factor. No shallow-circuit or physical fault-tolerance-overhead bound is asserted.

This construction supplies a gate implementation polynomial in the received input size. At every fixed $`\eta\lt 1`$, that input size, the protected memory, and the copy count are exponential in $`n`$. The [advantage over pair experiments](pair_comparison.md) concerns copies; the conservative collective gate upper bound can exceed the gate cost of repeated pair measurements.

## A Hermitian block encoding of each pair factor

Write

```math
 a=\eta^2,\quad c=(1+a)^n,\quad
 q=\frac{1-3a}{1+a}\in[-1,1],\quad
 T_{ab}=W_{ab}+I.
```

On one physical qubit pair, the normalized factor

```math
 \Lambda=\frac{I+a(XX+YY+ZZ)}{1+a}
   =P_{\rm trip}+qP_{\rm sing}
```

has eigenvalue one on the triplet subspace and $`q`$ on the singlet. Add one flag qubit and define

```math
 R(q)=qZ+\sqrt{1-q^2}\,X,
 \qquad
 F=P_{\rm trip}\otimes I_{\rm flag}
   +P_{\rm sing}\otimes R(q).
```

Then $`F=F^\dagger`$, $`F^2=I`$, and
$`\langle0|_{\rm flag}F|0\rangle_{\rm flag}=\Lambda`$.
This is a unitary dilation; its implementation never postselects the flag.

A CNOT and a Hadamard decode the Bell basis. In that basis the singlet is one computational basis state. With $`\theta=\arccos q`$, implement its controlled flag operation as

```math
 R(q)=R_y(\theta) Z R_y(-\theta).
```

Only a constant number of fixed-size controlled gates and one-qubit rotations are needed per physical pair. Using $`n`$ independent flags gives the Hermitian unitary

```math
 F_{ab}=\prod_{j=1}^nF_{ab,j},\qquad
 \langle0^n|F_{ab}|0^n\rangle=T_{ab}/c.
```

The factors commute because they act on disjoint qubit pairs and flags. In particular, the pair dilation is both unitary and Hermitian, a property used explicitly in the next step.

## Uniform pair selection with explicit routing

Set $`\ell=\log_2m`$. Two $`\ell`$-qubit address registers are prepared by Hadamards in the uniform superposition of all ordered pairs $`(a,b)\in\{0,\ldots,m-1\}^2`$. Include a guard qubit $`g`$, initially zero, and two clean $`n`$-qubit work registers.

For $`a\ne b`$, coherently route data register $`a`$ into the first work register and data register $`b`$ into the second, apply the local dilation above, and undo the routing. For $`a=b`$, apply $`X_g`$. The diagonal-address branch therefore has zero upper-left block. Equal-address detection is computed and uncomputed reversibly.

The routing operation is explicit. Scan every physical register $`j`$; reversibly compute the predicate $`a=j`$, perform $`n`$ controlled SWAPs, and uncompute the predicate. Do the same for $`b`$, with the routing disabled on the equal-address branch. The selected registers are distinct, so the second routing does not disturb the first selected state. Undo the second scan and then the first scan after the pair operation. Each scan costs $`O(m(n+\ell))`$ elementary gates with $`O(\ell)`$ reusable comparison workspace. This is a gate cost, not an oracle abstraction.

Let $`\mathsf{SELECT}`$ denote the resulting controlled operation, including routing and uncomputation. It is a conjugate of a direct sum of Hermitian involutions, hence
$`\mathsf{SELECT}=\mathsf{SELECT}^\dagger`$ and $`\mathsf{SELECT}^2=I`$.
Conjugating by the address Hadamards produces a Hermitian involution $`B`$. Projecting every auxiliary register onto zero gives

```math
 \begin{aligned}
 H&=\langle0_{\rm aux}|B|0_{\rm aux}\rangle\\
  &=\frac1{m^2c}\sum_{a\ne b}T_{ab}
    =\frac{m-1}{mc}(U_m+I)
    =\frac{U_m+I}{\alpha},\\
 \alpha&=c\frac m{m-1}\le2c.
 \end{aligned}
```

Thus $`B`$ block encodes a shifted version of the desired observable. The known identity shift is removed in classical postprocessing. This avoids a separate negative-identity LCU branch and avoids nonuniform preparation of unordered pairs.

One use of $`B`$, or its controlled version, has gate cost

```math
 O(m(n+\ell))
```

in a gate set allowing arbitrary one-qubit rotations. Its auxiliary space is $`O(n+\ell)`$: two routed work registers, $`n`$ flags, the address registers, the guard, and reusable comparison workspace. A control on the whole circuit adds only constant-size gate overhead. The source copies themselves are not re-prepared or queried again.

## Qubitization and eigenvalue discrimination

Let

```math
 \Pi=|0_{\rm aux}\rangle\langle0_{\rm aux}|\otimes I,
 \qquad Q=(2\Pi-I)B.
```

The reflection $`2\Pi-I`$ costs $`O(n+\ell)`$ Toffoli gates with reusable clean workspace. This is the Hermitian special case of qubitization [Low–Chuang](https://doi.org/10.22331/q-2019-07-12-163). Its spectral relation can be verified directly here, without a Hamiltonian-simulation approximation.

For an eigenvector $`|u\rangle`$ of $`U_m`$, let

```math
 \lambda=\frac{u+1}{\alpha},\qquad
 |g_u\rangle=|0_{\rm aux}\rangle|u\rangle.
```

When $`|\lambda|\lt 1`$, define
$` |b_u\rangle=(B|g_u\rangle-\lambda|g_u\rangle)/\sqrt{1-\lambda^2}`$.
It lies in the orthogonal complement of $`\Pi`$. Because $`B^2=I`$, the matrices on the invariant span of these two vectors are

```math
 B=\begin{pmatrix}\lambda&\sqrt{1-\lambda^2}\\
 \sqrt{1-\lambda^2}&-\lambda\end{pmatrix},
 \qquad
 Q=\begin{pmatrix}\lambda&\sqrt{1-\lambda^2}\\
 -\sqrt{1-\lambda^2}&\lambda\end{pmatrix}.
```

Consequently the walk eigenphases are $`\pm\arccos\lambda`$. The endpoint cases follow by continuity. Phase estimation of $`Q`$, followed by

```math
 \widehat u=\alpha\cos\widehat\vartheta-1,
```

therefore estimates an eigenvalue of $`U_m`$. The two phase signs give the same result. Since cosine is one-Lipschitz, phase error $`\delta`$ implies eigenvalue error at most $`\alpha\delta`$. Standard Fourier phase estimation with a constant success probability uses $`O(1/\delta)`$ walk queries and $`O(\log(1/\delta))`$ phase qubits. A constant number of extra phase bits makes each round succeed with probability at least $`3/4`$. Taking a median of repeated estimates on the same register reduces failure to $`\zeta`$ using

```math
 N_Q=O\!\left(\frac\alpha\Delta\log\frac1\zeta\right)
```

queries for additive error $`\Delta`$. This repetition consumes no additional supplied copies. Conditional on a walk eigenphase, phase-estimation rounds are nondemolition measurements and their readout randomness can be repeated; both walk phases associated with one $`u`$ have the same target value. Only the phase-estimation ancillas are reset between repetitions; the walk register, including its block-encoding auxiliaries, is retained. For an arbitrary input state, this realizes an approximate spectral measurement with the usual spectral probabilities.

This last statement requires no preparation of an eigenvector, no inverse of a state-preparation oracle, and no postselection on the block-encoding flags. In particular, the normalization $`\alpha`$ costs walk queries rather than additional copies.

## A threshold margin preserves the copy bound

Use threshold $`t=\bar\mu/2`$, and give the sum of eigenvalue-estimation error and threshold-rounding error a budget $`\Delta=\bar\mu/8`$. For an explicit finite-dimensional statement, take the same cutoff as the collective-copy theorem:

```math
 a_\eta=\frac{1+3\eta^8}{(1+3\eta^4)^2},\qquad
 n_0(\eta)=\max\!\left\{1,
 \left\lceil\frac{\log2}{\log(1+3\eta^4)}\right\rceil,
 \left\lceil\frac{\log1024}{-\log a_\eta}\right\rceil\right\}.
```

For $`n\ge n_0(\eta)`$, one has $`S\ge2`$ and
$`\delta_{n,\eta}:=\mathrm{Var}_{\rm Haar}(\mu_\psi)/\bar\mu^2\le1/64`$.
The proven moment estimates then give, for $`m\ge CM`$,

```math
 \frac{\mathrm{Var}_0(U_m)}{\bar\mu^2}\le\frac6{C^2},\qquad
 \frac{\mathrm{Var}_1(U_m)}{\bar\mu^2}
     \le\frac{24}{C^2}+\frac{64}{C}+\delta_{n,\eta}.
```

Here the alternative variance includes Haar fluctuations of the conditional mean. If the eigenvalue and threshold approximations obey their combined error budget, an incorrect decision requires one of the spectral tail events

```math
 \{U_m\ge3\bar\mu/8\}\quad\text{under }H_0,\qquad
 \{U_m\le5\bar\mu/8\}\quad\text{under }H_1.
```

The events refer to the ideal spectral distribution of $`U_m`$. Both are deviations of at least $`3\bar\mu/8`$ from the relevant hypothesis mean. Therefore their equal-prior average is at most

```math
 R_{\rm margin}\le\frac{32}{9}
 \left(\frac{30}{C^2}+\frac{64}{C}+\delta_{n,\eta}\right).
```

Set the phase-estimation failure probability to $`\zeta=1/100`$ and the total circuit-implementation error to at most $`1/100`$. Parameter-approximation errors below are included in the latter budget. A sufficient deterministic allocation is phase-estimation value error at most $`\bar\mu/16`$, scalar arithmetic error at most $`\bar\mu/32`$, and threshold error at most $`\bar\mu/32`$.

Taking $`C=4096`$ gives the explicit circuit risk

```math
 R_{\rm circuit}
 \le\frac19+\frac{320}{3\cdot4096^2}+\frac1{50}
 \lt 0.132\lt \frac16.
```

The false-positive probability $`p_0`$ under $`H_0`$ and the Haar-average false-negative probability $`p_1`$ under $`H_1`$ obey
$`p_0\le128/(3C^2)+1/50`$ and
$`p_1\le512/(3C^2)+2/9+1/50\lt 1/3`$.
Thus the same cutoff $`n_0(\eta)`$ suffices, and a constant-factor increase from the ideal-readout sample coefficient preserves its copy order. If only equal-prior error below $`1/3`$ is required, $`C=1024`$ already gives
$`R_{\rm circuit}\le5/18+320/(3\cdot1024^2)+1/50\lt 0.298`$.

For constant $`\zeta`$, the walk-query bound is

```math
 N_Q=O\!\left(\frac\alpha{\bar\mu}\right)
 \le O\!\left(\frac c{\bar\mu}\right)
 =O\!\left(\frac cdM^2\right)
 \le O(M^2),
```

because $`c=(1+\eta^2)^n\le d`$. With $`m=\Theta(M)`$, multiplying by the scan cost gives

```math
 G_{\rm rotation}
 =O\!\left(m(n+\log m)\frac\alpha{\bar\mu}
       +\log^2\frac\alpha{\bar\mu}\right)
 =O_\eta(nm^3).
```

The first expression is the more informative resource bound; $`O_\eta(nm^3)`$ is a conservative simplification. Additional phase and reflection workspace is
$`O(n+\log m+\log(\alpha/\bar\mu))=O_\eta(n)`$
at fixed decision error.

## Finite gate precision and the supplied value of eta

The preceding construction first uses exact one-qubit rotations. It also admits a finite universal gate library. There are

```math
 L_{\rm rot}=O(nN_Q+r^2\log(1/\zeta)),\qquad
 r=O(\log(\alpha/\bar\mu)),
```

rotation occurrences, including phase-estimation Fourier transforms. Approximate each one to operator-norm error $`O(\varepsilon_{\rm syn}/L_{\rm rot})`$. A telescoping hybrid bound then limits the final measurement distribution's total-variation change to $`O(\varepsilon_{\rm syn})`$, for every input state. The forward and inverse pieces of a local reflection can use the same synthesized gate sequence in reverse, preserving the involution exactly if desired.

An unconditional sufficient synthesis guarantee is the Solovay–Kitaev bound: each constant-size rotation has a sequence of $`O(\log^{3.97}(L_{\rm rot}/\varepsilon_{\rm syn}))`$ finite-library gates [Dawson–Nielsen](https://arxiv.org/abs/quant-ph/0505030). Thus a fully explicit conservative bound is

```math
 G=O\!\left(
   m(n+\log m)N_Q
   +L_{\rm rot}\log^{3.97}\frac{L_{\rm rot}}{\varepsilon_{\rm syn}}
 \right)
 =\widetilde O_\eta(nm^3)
```

at fixed decision error. The routing comparisons, SWAPs, and reflections use exactly representable Clifford/Toffoli gates; they require no precision proportional to the Hilbert-space dimension.

The parameter must also be supplied at adequate classical precision, with a certified absolute-error bound. The copy count and phase-estimation schedule are selected before the fine gate-precision input is requested. For fixed $`\eta\in(0,1)`$, the angle above has derivative

```math
 \left|\frac{d\theta}{d\eta}\right|
 =\frac{2\sqrt2}{(1+\eta^2)\sqrt{1-\eta^2}},
```

which is bounded on a sufficiently small neighborhood of that fixed $`\eta`$. The logarithmic derivatives of $`c`$, $`\bar\mu`$, and $`M`$ are $`O_\eta(n)`$. First obtain a certified interval

```math
0\lt \eta_-\le\eta\le\eta_+\lt 1,
\qquad \eta_+-\eta_-=O_\eta(1/n).
```

Choose the width small enough that these quantities vary by at most fixed factors across the interval. Since $`M`$ decreases with $`\eta`$, use outward-rounded classical arithmetic to obtain $`M_+\ge M(\eta_-)`$ with, for example, $`M_+\le2M(\eta_-)`$, then choose a power of two $`m\ge4096M_+`$ within a factor of two. This ensures $`m\ge4096M(\eta)`$ and $`m=\Theta_\eta(M(\eta))`$ even at a rounding boundary.

Define

```math
\mu_- = \bar\mu(\eta_-),\qquad
\alpha_+=\frac{m}{m-1}c(\eta_+).
```

Use a certified lower bound on $`\mu_-`$ and upper bound on $`\alpha_+`$, each within a fixed factor, to select a fixed phase precision at most $`\mu_-/(16\alpha_+)`$ and an integer query budget

```math
Q_{\max}=O\!\left(\frac{\alpha_+}{\mu_-}\log\frac1\zeta\right).
```

The schedule achieves the required value accuracy for the true $`\eta`$, and $`Q_{\max}=O_\eta(\alpha/\bar\mu)`$. It is now sufficient to refine the supplied parameter to absolute error

```math
 |\widetilde\eta-\eta|
 \le c_\eta\frac{\varepsilon_{\rm par}}{nQ_{\max}}
```

for a sufficiently small constant $`c_\eta`$. The same hybrid argument controls the accumulated angle errors relative to the ideal circuit at the true parameter. Because the scalar normalization multiplies a cosine of magnitude at most one, its value error is also controlled by this precision choice: an absolute normalization error of order $`\alpha n|\widetilde\eta-\eta|`$ is at most a constant times $`\bar\mu\varepsilon_{\rm par}`$. Threshold error is smaller still. The constants are chosen to fit the stated decision margin. This procedure does not change the noise on the input states; it approximates the known measurement coefficients and scalar postprocessing. This requires

```math
 b_\eta=O_\eta\!\left(\log\frac{nQ_{\max}}{\varepsilon_{\rm par}}\right)
       =O_\eta(n+\log n)
```

bits at fixed error budgets. Computing $`c`$, $`\bar\mu`$, and the final cosine to the corresponding additive accuracy also uses $`O_\eta(n+\log n)`$ bits and polynomial-time classical arithmetic. This is a sufficient, conservative precision requirement. Its absolute tolerance is exponentially small in $`n`$; a calibration experiment and its sample cost are not supplied by the known-$`\eta`$ model. No optimal robustness claim is needed for this implementation.

All data and work qubits remain protected throughout the circuit. A physical fault-tolerant overhead requires specifying a hardware noise model and error-correcting code. The protected-data count $`mn`$ does not purport to include that additional physical overhead. For a purely geometric compilation, placing all $`N=mn+O_\eta(n)`$ qubits on a line and transporting the endpoints of each two-qubit gate by SWAPs gives the stated conservative $`O(NG)`$ nearest-neighbor gate bound with no additional asymptotic space.


The [bibliography](../references/references.bib) contains the complete source records for qubitization and gate synthesis. The construction above supplies its own state access, routing, normalization and accuracy account.
