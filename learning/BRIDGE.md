# From Watrous to collective purity testing

A source repeatedly prepares the same unknown quantum state. Before each sample reaches a measuring device, local noise acts on every qubit. The source is either maximally mixed or a pure state drawn once from a specified random ensemble. The task is to identify which source was used. This distinction concerns the state before acquisition: a pure source generally produces mixed received samples.

The project asks how the required number of samples changes when the device can retain and process all of them coherently, compared with a device that measures two fresh samples at a time. The [model and main theorem](../science/model.md) give the exact statistical question. This bridge develops the mathematical objects, an explicit two-qubit experiment, and the additional arguments connecting them to the theorem.

## The selected source and the relevant reading

The educational anchor is **John Watrous, *The Theory of Quantum Information*, Cambridge University Press, 2018**, ISBN 9781107180567, DOI [10.1017/9781316848142](https://doi.org/10.1017/9781316848142). The [author's book page](https://cs.uwaterloo.ca/~watrous/TQI/) provides chapter PDFs. All section and theorem numbers below refer to that edition.

The useful route through the book is selective. The first three rows supply the objects used in the experiment; the last two supply the operational and symmetry statements used in the proofs.

| Purpose in this project | Relevant sections of Watrous | What is used here |
| --- | --- | --- |
| Tensor products, adjoints, spectra, and norms | [Chapter 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf), §§1.1.1–1.1.3 | Composite registers, adjoint maps, the spectral theorem, and Schatten norms. Theorem 1.3 justifies the spectral decomposition of a Hermitian observable. |
| States and inaccessible environments | [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), §2.1.2, *Quantum states of registers*, and §2.1.3, *Reductions and purifications of quantum states* | Density operators, mixtures, product states, and partial traces. A mathematical purification does not give the measuring device access to the purifying system. |
| Channels and measurements | [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), §§2.2.1–2.2.3 and §§2.3.1–2.3.2 | Completely positive trace-preserving maps, channel representations, identity and replacement channels, measurement effects, and outcome probabilities. |
| Optimal binary decisions | [Chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf), §3.1.1, *Discriminating between pairs of quantum states*, especially Theorem 3.4 | The Holevo–Helstrom relation between optimal error and trace distance. |
| The Haar prior and its tensor moments | [Chapter 7](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf), §7.1.1 and §7.2.1 | Proposition 7.1 gives the symmetric projector; Corollary 7.3 gives its dimension. Definition 7.16 specifies the uniform spherical measure, and Lemma 7.24 gives its exact tensor moment. |

The book supplies the foundations and the Haar identity. The Pauli conventions, noise-dependent weights, growing-dimension moment estimates, trimmed-prior converse, and explicit measurement circuit are developed in the project. In particular, Watrous does not prove the local-noise sample law or supply this qubitization circuit. The cited research ingredients remain identified in [Related work](../references/RELATED_WORK.md).

Sections 3.2 and 3.3 of Watrous discuss fidelity and channel discrimination. They are useful neighboring subjects, but the present proof uses trace distance between states produced by one known channel. Distinguishing two unknown channels, choosing a probe before noise, and accessing a channel environment would define different experiments.

## Notation and the physical experiment

Let $`n`$ be the number of qubits in one sample and $`d=2^n`$ its Hilbert-space dimension. Let $`m`$ be the number of supplied samples. The maximally mixed state is $`\tau=I_d/d`$. A pure source is written $`\psi=|u\rangle\langle u|`$, where $`|u\rangle`$ is a unit vector. Thus $`\psi`$ denotes a density operator throughout the project.

Several notation changes matter when moving from the book to the scientific pages.

| Book notation or object | Project notation and interpretation |
| --- | --- |
| A complex Euclidean space $`\mathcal X`$ | One source register is $`(\mathbb C^2)^{\otimes n}`$; the received data register has $`mn`$ qubits. |
| A unit vector $`u`$ and projector $`uu^*`$ | $`\lvert u\rangle`$ and $`\psi=\lvert u\rangle\langle u\rvert`$. The prior is on the pure source, before noise. |
| The identity $`1_{\mathcal X}`$ and an operator adjoint $`A^*`$ | $`I`$ and $`A^\dagger`$. The star in $`\mathcal N_\eta^*`$ still denotes the adjoint **map** with respect to the Hilbert–Schmidt inner product. |
| A measurement $`a\mapsto\mu(a)`$ | A binary effect $`E`$ means “choose the pure-source hypothesis”; its other effect is $`I-E`$. The scalar $`\mu_\psi`$ used later is an expectation value, not a POVM. |
| A permutation operator $`W_\pi`$ | $`V_\pi`$ in the Haar formula. The unindexed $`W`$ in this project is instead the weighted two-copy observable. |
| A tensor power indexed by an integer in Chapter 7 | Use $`k`$ for the moment order here, so it is distinct from the physical qubit count $`n`$ and the available copy count $`m`$. |

The single-qubit acquisition channel is

```math
\mathcal D_\eta(A)
=\eta A+(1-\eta)\mathrm{Tr}(A)\frac{I_2}{2},
\qquad 0\lt\eta\lt1.
```

It is the convex combination of the identity channel and the completely depolarizing replacement channel described in Watrous §2.2.3. The parameter $`\eta`$ is a retention factor: larger values mean less acquisition noise. For one $`n`$-qubit sample the channel is $`\mathcal N_\eta=\mathcal D_\eta^{\otimes n}`$, and a received sample has state $`\sigma_\psi=\mathcal N_\eta(\psi)`$.

Under the pure-source hypothesis, the same $`\psi`$ is used every time. Noise acts independently on the qubits and on successive samples. Conditional on $`\psi`$, the samples therefore have product state $`\sigma_\psi^{\otimes m}`$. Averaging over the one hidden source gives

```math
\Omega_{0,m}=\tau^{\otimes m},
\qquad
\Omega_{1,m}=\int\sigma_\psi^{\otimes m}\,d\psi.
```

The order of these operations is essential. In general,

```math
\int\sigma_\psi^{\otimes m}\,d\psi
\ne
\left(\int\sigma_\psi\,d\psi\right)^{\otimes m}.
```

The expression on the right describes independently redrawing the source for every sample. It equals $`\tau^{\otimes m}`$ and would make this test impossible for every copy count. The expression on the left retains the correlations created by sharing one unknown source. Even in the actual experiment, the one-copy average equals $`\tau`$, so one copy provides no information about the hypothesis.

The acquisition channel and its parameter are known. The device receives the output registers, with no source-preparation oracle or environmental record. Protected downstream gates and storage are allowed. These conditions are part of the [access and resource contract](../science/model.md#access-and-resource-contract), rather than consequences of the textbook formalism.

## A complete example: a hidden qubit and a Bell measurement

Consider $`n=1`$. Define the Pauli matrices

```math
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
Y=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\qquad
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
```

A pure qubit can be written using a unit Bloch vector $`\mathbf r=(r_x,r_y,r_z)`$:

```math
\psi_{\mathbf r}
=\frac12(I+r_xX+r_yY+r_zZ),
\qquad \|\mathbf r\|_2=1.
```

The Haar prior makes $`\mathbf r`$ uniform on the unit sphere. Hence its coordinate means vanish and $`\mathbb E r_jr_k=\delta_{jk}/3`$. Local depolarization shrinks the vector to $`\eta\mathbf r`$:

```math
\sigma_{\mathbf r}
=\frac12(I+\eta r_xX+\eta r_yY+\eta r_zZ).
```

The average of one received qubit is $`I/2`$. For two received qubits from the same source, expanding the tensor product and averaging gives

```math
\Omega_{1,2}
=\frac14\left[
I\otimes I+\frac{\eta^2}{3}
(X\otimes X+Y\otimes Y+Z\otimes Z)
\right],
\qquad
\Omega_{0,2}=\frac{I\otimes I}{4}.
```

The surviving terms contain two factors of the same hidden coordinate, one from each sample. This is the information that a single sample cannot reveal.

Let $`F`$ exchange the two qubits. The identity

```math
X\otimes X+Y\otimes Y+Z\otimes Z=2F-I
```

shows how to measure the relevant correlation. The symmetric, three-dimensional triplet subspace has swap eigenvalue $`+1`$. The antisymmetric singlet
$`|\Psi^-\rangle=(|01\rangle-|10\rangle)/\sqrt2`$ has swap eigenvalue $`-1`$. The project's two-copy observable is

```math
W=\eta^2(X\otimes X+Y\otimes Y+Z\otimes Z).
```

It has only two distinct reported values. Their exact probabilities are:

| Outcome subspace | Reported value of $`W`$ | Mixed source | Fixed pure source after noise |
| --- | ---: | ---: | ---: |
| Triplet | $`\eta^2`$ | $`3/4`$ | $`(3+\eta^2)/4`$ |
| Singlet | $`-3\eta^2`$ | $`1/4`$ | $`(1-\eta^2)/4`$ |

For the last column, the singlet projector is $`(I-F)/2`$ and
$`\mathrm{Tr}[F(\sigma\otimes\sigma)]=\mathrm{Tr}(\sigma^2)`$.
Here $`\mathrm{Tr}(\sigma_{\mathbf r}^2)=(1+\eta^2)/2`$, giving the displayed probabilities. They are the same for every direction $`\mathbf r`$ in this one-qubit example.

An explicit Bell-basis measurement uses a CNOT from the first qubit to the second, a Hadamard on the first qubit, and computational-basis measurement of both. The singlet decodes to $`11`$. Report $`-3\eta^2`$ for that outcome and $`\eta^2`$ for the other three outcomes. This consumes two supplied qubits, two gates, and two measured bits. It requires no knowledge of the hidden direction.

The expected reported values are

```math
\mathbb E_0 W=0,\qquad
\mathbb E_1 W
=\eta^2\frac{3+\eta^2}{4}
-3\eta^2\frac{1-\eta^2}{4}
=\eta^4.
```

For example, at $`\eta=1/2`$, the singlet probability changes from $`1/4`$ to $`3/16`$. The two reported values are $`1/4`$ and $`-3/4`$, and their mean changes from zero to $`1/16`$. These are noisy statistical outcomes, so one pair does not identify the source with certainty.

This calculation also checks the normalization used later: $`d=2`$, $`L=(1+3\eta^4)-1=3\eta^4`$, and the general Haar mean $`L/(d+1)`$ is exactly $`\eta^4`$. It illustrates shared-source information and a physical pair measurement. The exponential separation concerns increasing $`n`$ and requires the additional arguments below.

## From the book's Haar identity to the weighted observable

Watrous Lemma 7.24 states that the average of $`(|u\rangle\langle u|)^{\otimes k}`$ is the normalized symmetric projector. Combining it with Proposition 7.1 and Corollary 7.3 gives

```math
\int\psi^{\otimes k}\,d\psi
=\frac{\Pi_{\mathrm{sym}}^{(k)}}{\binom{d+k-1}{k}}
=\frac1{(d)_k}\sum_{\pi\in\mathfrak S_k}V_\pi,
\qquad
(d)_k=d(d+1)\cdots(d+k-1).
```

This is an exact finite-dimensional identity. Contracting a tensor product of operators with a permutation produces one trace for each cycle of that permutation. The [Haar-moment derivation](../science/haar_moments.md#haar-moments-and-pauli-conventions) uses this rule at orders two, three, and four, keeping the Pauli multiplication signs.

The identity applies to the source before noise. The received average is obtained by applying $`\mathcal N_\eta^{\otimes k}`$ to it. It generally has support outside the symmetric subspace, even though it is invariant under permuting the received copies. The positive singlet probability in the example demonstrates this distinction. For multiple qubits, the output ensemble generally lacks global unitary invariance because different Pauli weights undergo different attenuation, even though the source prior has that invariance.

For $`n`$ qubits, let $`P\in\{I,X,Y,Z\}^{\otimes n}`$ be a Hermitian Pauli string, and let $`w(P)`$ count its nonidentity factors. The project uses

```math
\mathrm{Tr}(PQ)=d\,\mathbf1\{P=Q\},\qquad
r_P=\mathrm{Tr}(\psi P),\qquad
\mathcal N_\eta(P)=\eta^{w(P)}P.
```

A direction of weight one is attenuated by $`\eta`$, while a direction of weight two is attenuated by $`\eta^2`$. This unequal attenuation across Pauli directions is the feature exploited by the measurement. The Haar second moment gives $`\mathbb E r_Pr_Q=\mathbf1\{P=Q\}/(d+1)`$ for nonidentity strings.

The chosen observable and its mean are

```math
\begin{aligned}
W&=\sum_{P\ne I}\eta^{2w(P)}P\otimes P,\\
\mu_\psi
&=\mathrm{Tr}(W\sigma_\psi^{\otimes2})
=\sum_{P\ne I}\eta^{4w(P)}r_P^2,\\
\overline\mu&=\mathbb E_\psi\mu_\psi
=\frac{L}{d+1},\qquad
L=(1+3\eta^4)^n-1.
\end{aligned}
```

Two factors of attenuation come from the two received samples; two more come from the observable's coefficient. At each site there is one identity choice and three nonidentity choices, explaining the product $`(1+3\eta^4)^n`$. The identity string is subtracted because it carries no distinction between the hypotheses.

These coefficients have a statistical justification. For a kernel $`\sum_{P\ne I}a_PP\otimes P`$ with real weights $`a_P`$, the null variance is $`\sum_Pa_P^2`$ and the average signal is $`\sum_Pa_P\eta^{2w(P)}/(d+1)`$. Cauchy–Schwarz maximizes their squared signal-to-variance ratio when $`a_P`$ is proportional to $`\eta^{2w(P)}`$. This explains the kernel within that family. Optimality over all collective measurements requires the separate converse.

## From a pair operation to a collective measurement

The Bell measurement extends directly to $`n`$ qubits because

```math
W+I=\bigotimes_{j=1}^n
\left[I+\eta^2(X\otimes X+Y\otimes Y+Z\otimes Z)\right]_j.
```

Measure corresponding qubits from two samples in the Bell basis. If $`k`$ of the $`n`$ outcomes are singlets, the reported value is

```math
Y=(1+\eta^2)^{n-k}(1-3\eta^2)^k-1.
```

The singlet factor can be negative; it is retained with its sign. Repeating this experiment on fresh pairs gives the [pair protocol](../science/pair_comparison.md#an-explicit-repeated-pair-upper-bound).

The collective observable instead averages over every pair of retained samples:

```math
U_m=\binom m2^{-1}\sum_{1\le a\lt b\le m}W_{ab}.
```

This is one Hermitian operator, so its spectral decomposition defines a valid measurement. The test compares its measured eigenvalue with $`\overline\mu/2`$. Terms that share a sample need not commute. Measuring each pair separately would therefore implement a different experiment; the $`\binom m2`$ terms do not represent independently accessible classical records. The operator is a degree-two quantum U-statistic in the established framework of Guţă and Butucea, as explained in [Collective measurement](../science/collective_measurement.md#relation-to-the-quantum-u-statistics-framework).

The [circuit construction](../science/measurement_resources.md) makes the spectral measurement concrete. It first replaces destructive Bell readout by coherent Bell decoding and a flag operation that has the desired normalized factor as a matrix block. It then prepares address registers, scans the physical data registers using controlled SWAPs, applies the selected pair operation, and reverses the routing. This constructs a block encoding of a known rescaling of $`U_m+I`$. No flag outcome is postselected.

A reflection and this block encoding form a qubitized walk. Its eigenphases determine the eigenvalues of $`U_m`$, so phase estimation supplies an approximate threshold measurement. The proof includes the phase-to-value conversion, the decision margin, and the accumulation of finite gate errors. Repeated phase readout uses the same retained input registers; it does not call a state-preparation oracle or consume another batch of source copies.

At this stage the costs can be read without assuming the sample theorem. One block-encoding call costs $`O(m(n+\log m))`$ gates for explicit routing. With $`c=(1+\eta^2)^n`$, constant-error eigenvalue discrimination uses $`O(c/\overline\mu)`$ such calls. The input storage is $`mn`$ protected qubits. The cited block-encoding, qubitization, and synthesis results are research ingredients; the project supplies this observable's access circuit and resource accounting.

## The additional arguments needed for the sharp law

### The upper bound needs more than an average signal

At the null state, Pauli orthogonality makes the covariance of distinct pair terms vanish, including overlapping pairs. Consequently,

```math
\mathrm{Var}_0(U_m)=\frac{L}{\binom m2}.
```

The standard deviation decreases as $`\sqrt L/m`$, while the average alternative signal is $`L/(d+1)`$. Balancing them suggests the scale

```math
t_{n,\eta}=\sqrt{d(d+1)/L}.
```

This balance is only the beginning of the proof. Under the alternative, two pair terms can share a received sample. Their expectation requires a three-copy Haar contraction. In addition, the conditional signal $`\mu_\psi`$ varies with the one hidden source. Averaging more measurement outcomes does not remove this source variation. The relevant variance is

```math
\mathrm{Var}_1(U_m)
=\mathbb E_\psi\mathrm{Var}(U_m\mid\psi)
+\mathrm{Var}_\psi(\mu_\psi).
```

The [exact third- and fourth-moment formulas](../science/haar_moments.md#exact-second--third--and-fourth-moment-contractions) control both contributions. In particular, they prove that the relative source variance decays at fixed $`\eta`$:

```math
\frac{\mathrm{Var}_\psi(\mu_\psi)}{\overline\mu^2}
\le16a_\eta^n,
\qquad
a_\eta=\frac{1+3\eta^8}{(1+3\eta^4)^2}\lt1,
```

whenever $`(1+3\eta^4)^n\ge2`$. This supplies a finite sufficient starting dimension. The [upper-bound proof](../science/collective_measurement.md#finite-error-upper-bound) then uses Chebyshev's inequality at the stated threshold. It does not replace the correlated Pauli coefficients of a Haar pure state by independent random variables or rely on a fixed-dimension asymptotic theorem.

### The lower bound must cover every measurement

Watrous Theorem 3.4 gives the optimal equal-prior error as

```math
R_m^*=\frac12\left[1-D(\Omega_{1,m},\Omega_{0,m})\right],
\qquad
D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1.
```

The two density operators here already include the prior and all supplied copies. Every downstream strategy defines a measurement effect on them, including strategies using ancillas, adaptive processing, and large quantum memory. A bound on this trace distance therefore applies to the whole collective class.

The remaining problem is to bound it sharply for the locally noisy Haar mixture. The [collective converse](../science/collective_lower_bound.md) uses the round-trip channel and a centered operator:

```math
\mathcal K=\mathcal N_\eta^*\mathcal N_\eta
=\mathcal D_{\eta^2}^{\otimes n},\qquad
B_\phi=\mathcal K(\phi)-\tau,
\qquad
v=\mathbb E_\phi\mathrm{Tr}(B_\phi^2)
=\frac{L}{d(d+1)}=t_{n,\eta}^{-2}.
```

The same fourth-power channel weight appears here for a different reason: the Hilbert–Schmidt overlap of two received states contains two channel applications. Squaring the round-trip Pauli eigenvalues gives $`\eta^{4w(P)}`$.

The mixture collision identity converts the many-copy comparison to powers of this overlap. High powers can overemphasize exceptional source states, so the proof first conditions the Haar prior on
$`G=\{\phi:\mathrm{Tr}(B_\phi^2)\le16v\}`$.
Markov's inequality gives $`\Pr(G)\ge15/16`$. Centering removes every permutation with a one-cycle from the Haar expansion; a Schatten-norm bound controls the remaining cycle traces. This yields a uniform collision bound on $`G`$ when $`m`$ is a small constant times $`t_{n,\eta}`$. The omitted probability mass is then paid explicitly in trace distance before applying the binary error formula.

This reasoning is stronger than substituting a mean squared norm inside a high power. It preserves the actual Haar prior and keeps both conditioning normalizations. Mixture-divergence methods and prior conditioning are established statistical tools; [Related work](../references/RELATED_WORK.md#mixture-divergences-and-the-converse) identifies their antecedents. The channel-specific evaluation and matching scale are supplied by the present proof.

### Matching the bounds

The upper and lower arguments meet at $`t_{n,\eta}`$. [Theorem 1](../science/model.md#theorem-1) specifies the finite constants, error guarantees, and sufficient cutoff. For fixed $`0\lt\eta\lt1`$, it gives

```math
m_*(n,\eta)=\Theta_\eta(t_{n,\eta})
=\Theta_\eta\!\left[
\left(\frac2{\sqrt{1+3\eta^4}}\right)^n
\right].
```

The upper guarantee averages over the fixed Haar source. It does not establish the same rate for every pure input. The lower bound also obstructs worst-case pure-source testing, because a procedure succeeding on every pure source would succeed on this prior. That implication does not convert the average upper bound into a worst-case upper bound.

## The consequence and its resource scope

An adaptive pair learner may choose any POVM on two fresh outputs using its entire preceding classical transcript, but retains no quantum register between rounds. The [pair comparison](../science/pair_comparison.md) combines the repeated Bell protocol with the matching-model lower bound of Cotler, Gong, and Kannan. Writing $`M=t_{n,\eta}`$, the resulting bounds are

```math
m_{\mathrm{collective}}=\Theta_\eta(M),\qquad
\Omega_\eta\!\left(\min\{2^{n/2},M^2\}\right)
\le m_{\mathrm{pair}}\le O_\eta(M^2).
```

The collective sample advantage is exponential for $`3^{-1/4}\lt\eta\lt1`$. For
$`[(2\sqrt2-1)/3]^{1/4}\le\eta\lt1`$, the pair count is $`\Theta_\eta(M^2)`$, so the optimal sample counts have a quadratic relation. The intermediate range has an exponential separation without a settled optimal pair exponent. At and below the lower threshold, the quoted comparison does not decide whether an exponential separation exists. The imported adaptive lower bound is essential: a small distance between averaged two-copy states alone would not control a transcript whose rounds share the same source.

Substituting the proven sample scale into the explicit construction gives the following resource account at fixed decision error and fixed $`\eta`$.

| Resource | What the construction establishes |
| --- | --- |
| Received copies | $`m=\Theta_\eta(M)`$, with a constant-factor increase for approximate readout. |
| Protected data storage | All $`mn`$ input qubits, plus $`O_\eta(n)`$ auxiliary qubits. |
| Gates from a finite universal library | A conservative bound $`\widetilde O_\eta(nm^3)`$ with arbitrary two-qubit connectivity and explicitly charged register scans. |
| Parameter information | A supplied certified value of $`\eta`$ to sufficient $`O_\eta(n+\log n)`$-bit precision. A calibration experiment is outside this known-parameter model. |
| Hardware assumptions | Protected storage and gates after acquisition. Physical error-correction overhead requires a separate hardware model. |

The copy count remains exponential in $`n`$ for every fixed $`\eta\lt1`$. The gate bound is polynomial in that already exponential received input size; it is not a polynomial-time algorithm in $`n`$ or a claimed computational speedup over pair measurements. The construction supplies no free data-loading operation or QRAM, and its conservative gate count can exceed the gate cost of the pair protocol. The [resource page](../science/measurement_resources.md) also states a geometric compilation bound and the required precision budgets.

The endpoints illustrate why the fixed-parameter qualification matters. At $`\eta=0`$, the two received ensembles coincide for every $`m`$. At $`\eta=1`$, the noiseless symmetric-projector formula yields a constant-copy test; the [model page](../science/model.md#asymptotic-rate-and-the-noiseless-or-fully-depolarized-endpoints) gives its exact error. A simultaneous limit in which $`\eta`$ changes with $`n`$ must use the finite inequalities rather than assume uniform constants in the fixed-$`\eta`$ asymptotic expression.

## Routes into the complete scientific account

The [30-milestone map](MILESTONES.md) records the project's common understanding targets and dependencies. Its 11 background milestones build the experiment from individual states and operations; its 19 narrative milestones assemble the measurement, proof, and architectural consequence. The following groups connect this bridge to that map without replacing its detailed targets.

| Map group | Connection developed here | Canonical next source |
| --- | --- | --- |
| M01–M11: background and full model | Density operators, local channels, effects, shared-source averaging, Haar moments, and the allowed measurement classes | [Model](../science/model.md), then [Haar conventions](../science/haar_moments.md#haar-moments-and-pauli-conventions) |
| M12–M17: constructing and charging the measurement | Weighted Pauli kernel, Bell outcomes, coherent pair operation, register routing, eigenvalue readout, and costs before choosing the sample rate | [Collective observable](../science/collective_measurement.md#a-collective-pair-sum-observable) and [Measurement resources](../science/measurement_resources.md) |
| M18–M21: proving the upper guarantee | Null variance, overlap moments, concentration of the hidden-source signal, and finite error | [Haar moments](../science/haar_moments.md) and [Finite-error upper bound](../science/collective_measurement.md#finite-error-upper-bound) |
| M22–M25: proving optimality | Mixture collision, centered moments, conditioning with an explicit probability cost, and the matching law | [Collective converse](../science/collective_lower_bound.md) and [Theorem 1](../science/model.md#theorem-1) |
| M26–M30: the complete consequence | Pair upper and lower bounds, noise regimes, endpoints, inherited ingredients, and physical scope | [Pair comparison](../science/pair_comparison.md), [Interpretation](../science/interpretation.md), and [Related work](../references/RELATED_WORK.md) |

The [verification guide](../verification/README.md) provides independent finite-matrix checks of the third- and fourth-moment contractions, including the zero source-variance one-qubit limit illustrated above. Those checks support the algebra; the all-dimension theorem and implementation guarantee rest on the displayed analytical proofs. [Related work](../references/RELATED_WORK.md) also separates the sharp Haar-average law from the earlier noise-budget obstruction, generic quantum U-statistics, mixture-testing methods, and the cited adaptive-pair theorem.
