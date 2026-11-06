# Thirty milestones for Collective Purity Advantage

The scientific question is how many noisy acquisitions are needed to identify a pure source, and how that number changes when the received copies can remain in quantum memory and be measured together. This map follows the experiment from individual states and channels to a sharp statistical law, an explicit collective implementation, and a comparison with adaptive pair measurements.

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**, available from the [author's book page](https://cs.uwaterloo.ca/~watrous/TQI/). Read the indicated sections alongside the linked project pages. The [source-to-project bridge](BRIDGE.md) translates notation and develops the entry point; the [scientific reading route](../science/README.md) leads directly to the authoritative statements and proofs. Primary research dependencies remain identified in [Related work](../references/RELATED_WORK.md).

## Allocation and reading order

| Phase | Milestones | Progression |
| --- | --- | --- |
| Background/preliminaries | M01–M11: 11 milestones | Individual states, tensor factors, channels and measurements become a complete fixed-source discrimination experiment with explicit access and resource assumptions. |
| Narrative/innovation | M12–M30: 19 milestones | One noise-matched pair operation becomes a coherent collective protocol; its statistical guarantee and converse determine the optimal rate; the pair comparison and resource account establish the full consequence. |

The allocation reflects the project's combination of statistical inference, quantum measurement and circuit resources. Eleven background targets connect these foundations. Nineteen narrative targets then connect the concrete operation, the two directions of the copy-complexity theorem, and the architectural comparison. Each phase ends by integrating its components into a complete account.

The IDs denote common understanding targets. Listed dependencies are earlier milestones; additional transitive prerequisites are supplied by those dependencies. In the early implementation milestones, the number of received copies is an input size. Its necessary and sufficient scale is established later, before the final resource and architecture synthesis.

Throughout, one copy means one entire received $`n`$-qubit register, $`d=2^n`$, and the known attenuation parameter is fixed with $`0\lt\eta\lt1`$. The pure source is drawn once and held fixed. The upper guarantee averages over this Haar source. Adaptive pair rounds retain classical history but no quantum register between rounds. Collective gates and storage are protected; their costs are counted separately from supplied copies.

## Phase I: Background/preliminaries

### M01: Pure source and mixed received state

**Phase:** Background/preliminaries.

**Central question:** What does it mean to identify a pure source when the state reaching the measuring device can be mixed?

**Understanding target:** Distinguish a pure-state projector, a mixed density operator and the maximally mixed state. Explain why acquisition can change purity, so the source hypothesis and the received density operator play different roles in the experiment. Keep the physical state distinct from a probability distribution expressing uncertainty about its identity.

**Dependencies and story role:** None within this map. This establishes the single-system objects from which the larger experiment is built.

**Conceptual connection:** The density-operator description makes source purity an operational question after a specified transformation. It explains why a test of the source must use information about the acquisition channel.

**Source pointers:** [Watrous §2.1.2, “Quantum states of registers”][W2]. Project: [Noisy-source purity testing](../science/model.md) and [A source test after a known channel](../science/interpretation.md#a-source-test-after-a-known-channel).

### M02: Tensor products and Pauli weight

**Phase:** Background/preliminaries.

**Central question:** How can many-qubit structure be described without confusing physical qubits with repeated copies?

**Understanding target:** Distinguish the $`n`$ tensor factors inside one register from the $`m`$ received registers. Interpret a Hermitian Pauli string, its coefficient in a state expansion and its weight, the number of nonidentity factors. Recognize why weight is a useful label for independent local noise, including for entangled input states.

**Dependencies and story role:** M01. This extends the single-state description to the two tensor structures used throughout the project.

**Conceptual connection:** Tensor products organize both the physical channel and the collective measurement. The project's Pauli conventions turn local attenuation into a tractable description of a large operator space.

**Source pointers:** [Watrous §1.1.1, “Complex Euclidean spaces,” and §1.1.2, “Linear operators”][W1]; [§2.1.2, “Quantum states of registers”][W2]. Project: [Haar moments and Pauli conventions](../science/haar_moments.md#haar-moments-and-pauli-conventions), especially Eqs. (11)–(13). The Pauli basis and its weight convention are supplied by the project.

### M03: A local channel on every acquisition

**Phase:** Background/preliminaries.

**Central question:** What information does one layer of independent local depolarization remove from each received copy?

**Understanding target:** Read the partial depolarizer as a convex combination of the identity channel and replacement by the maximally mixed state. Explain why it preserves the reference state and attenuates a weight-$`w`$ Pauli coefficient by $`\eta^w`$. Distinguish independent noise on each acquisition from a model in which further noise accumulates during storage and processing.

**Dependencies and story role:** M01, M02. This supplies the physical transformation connecting the prepared source to the measurement input.

**Conceptual connection:** Channel linearity turns a physical noise model into a known pattern of information loss. The attenuation depends on operator weight even though the source itself is globally Haar distributed.

**Source pointers:** [Watrous §2.2.1, “Definitions and basic notions concerning channels,” and §2.2.3, “Examples of channels and other mappings”][W2]. The latter supplies identity and replacement channels; the project's convex combination and Pauli attenuation are in the [statistical model](../science/model.md#statistical-model-and-theorem) and [Pauli conventions](../science/haar_moments.md#haar-moments-and-pauli-conventions).

### M04: Effects, observables, and measurement outcomes

**Phase:** Background/preliminaries.

**Central question:** How does a mathematical operator specify an experiment and its classical outcome?

**Understanding target:** Relate a POVM effect to its Born probability and a Hermitian observable to its spectral measurement. Interpret expectation and variance as properties of the outcome distribution. Understand that a Hermitian sum has a valid spectral measurement even when its summands do not commute; separately measuring those summands generally gives a different experiment.

**Dependencies and story role:** M01, M02. This provides the measurement language needed to compare individual, pair and collective experiments.

**Conceptual connection:** The project proposes one observable on retained copies. The distinction between that observable and a list of separately measured terms is essential to the eventual variance advantage.

**Source pointers:** [Watrous §1.1.3, “Operator decompositions and norms,” including the spectral theorem][W1]; [§2.3.1, “Two equivalent definitions of measurements,” and §2.3.2, “Basic notions concerning measurements”][W2]. Project: [The binary decision effect](../science/model.md#statistical-model-and-theorem) and [A collective pair-sum observable](../science/collective_measurement.md#a-collective-pair-sum-observable).

### M05: Error probability and trace-distance discrimination

**Phase:** Background/preliminaries.

**Central question:** What makes two quantum hypotheses distinguishable, and how is their best decision error quantified?

**Understanding target:** State the equal-prior binary error criterion and interpret trace distance as the maximum measurement advantage. Translate between a small trace-distance upper bound and an error lower bound. Track the convention that the project's trace distance is one half of the trace norm of the state difference.

**Dependencies and story role:** M03, M04. This turns the physical setup into an operational statistical objective.

**Conceptual connection:** A converse can rule out every measurement by controlling a distance between the two received density operators. The acquisition channel is known; the hypotheses concern its input source rather than two unknown channel alternatives.

**Source pointers:** [Watrous §3.1, “Quantum state discrimination,” especially §3.1.1, “Discriminating between pairs of quantum states,” and Theorem 3.4][W3]. Project: [Error criterion and Theorem 1](../science/model.md#statistical-model-and-theorem) and [the converse's final trace-distance step](../science/collective_lower_bound.md#truncation-and-the-collision-integral).

### M06: One hidden source across many copies

**Phase:** Background/preliminaries.

**Central question:** Why does drawing one unknown state and keeping it fixed differ from drawing a new state for every copy?

**Understanding target:** Explain that copies are independent conditional on the fixed source, while averaging over that common source can correlate measurement records. Distinguish an average of tensor powers from the tensor power of an average. Recognize that one-copy prior averages can coincide even when several-copy hypotheses are distinguishable.

**Dependencies and story role:** M01, M02, M03, M05. This supplies the latent-source structure that controls both the upper and lower arguments.

**Conceptual connection:** The same hidden state ties every pair experiment and every collective copy together. Replacing it with independently averaged copies would erase the information the task asks the measurement to recover.

**Source pointers:** [Watrous §1.2.2, “Probability theory”][W1]; [§2.1.2, “Quantum states of registers”][W2]. Project: [The two received hypotheses, Eq. (1)](../science/model.md#statistical-model-and-theorem), [the fixed-source interpretation](../science/interpretation.md#a-source-test-after-a-known-channel), and [the hidden-qubit worked example](BRIDGE.md#a-complete-example-a-hidden-qubit-and-a-bell-measurement).

### M07: Haar symmetry and symmetric subspaces

**Phase:** Background/preliminaries.

**Central question:** What does a uniform unknown pure state mean, and how can its tensor moments be evaluated exactly?

**Understanding target:** Interpret the uniform spherical measure and its relation to Haar-distributed unitary rotations. Explain why tensor powers of a pure vector lie in the symmetric subspace, and why their uniform average is its normalized projector. Connect the permutation expansion of that projector with products of traces along permutation cycles.

**Dependencies and story role:** M02, M06. This gives a finite-dimensional tool for the entire common-source ensemble.

**Conceptual connection:** Global unitary symmetry makes Haar moments accessible, while the channel retains its local Pauli structure. Combining these two structures will control the noisy signal without a Gaussian approximation.

**Source pointers:** [Watrous §7.1.1, “The subspace of permutation-invariant vectors,” including Proposition 7.1 and Corollary 7.3; §7.2.1, “Uniform spherical measure and Haar measure,” including Lemma 7.24][W7]. Project: [The Haar tensor identity, Eq. (14)](../science/haar_moments.md#haar-moments-and-pauli-conventions).

### M08: Two copies reveal quadratic information

**Phase:** Background/preliminaries.

**Central question:** How can a measurement obtain a quantity quadratic in an unknown density operator?

**Understanding target:** Relate the swap observable on two copies to purity, and interpret symmetric and antisymmetric outcomes. Explain how a linear expectation on a two-copy state represents a quadratic functional of the single-copy state. Recognize why the existence of a swap measurement alone does not determine the best statistic after local acquisition noise.

**Dependencies and story role:** M02, M04, M07. This supplies the basic two-copy operation from which the noise-dependent statistic will be built.

**Conceptual connection:** The project retains the operational idea of accessing quadratic information through two copies, then adjusts the weights to the received ensemble's attenuation pattern.

**Source pointers:** [Watrous §2.3.1, “Two equivalent definitions of measurements”][W2]; [§7.1.1, “The subspace of permutation-invariant vectors”][W7]. Project: [The two-copy kernel](../science/collective_measurement.md#a-collective-pair-sum-observable) and [the noiseless endpoint](../science/model.md#asymptotic-rate-and-the-noiseless-or-fully-depolarized-endpoints).

### M09: Variance and source-dependent uncertainty

**Phase:** Background/preliminaries.

**Central question:** Which kinds of randomness must a reliable decision rule control?

**Understanding target:** Distinguish measurement fluctuations for a fixed source from fluctuations of the conditional mean across sources. Interpret the law of total variance and explain why a nonzero average signal is insufficient without fluctuation control. Understand the role of finite-variance probability bounds in converting a signal-to-noise calculation into a fixed-error decision guarantee.

**Dependencies and story role:** M04, M06, M08. This supplies the statistical reasoning needed to assess the collective observable rather than just its expectation.

**Conceptual connection:** The common source produces an additional uncertainty term that survives averaging measurement outcomes. Its concentration must be proved separately from the fluctuations of the measuring device.

**Source pointers:** [Watrous §1.2.2, “Probability theory”][W1]; [§2.3.2, “Basic notions concerning measurements”][W2]. Project: [Conditional variance](../science/collective_measurement.md#a-collective-pair-sum-observable) and [total variance, Eq. (64)](../science/collective_measurement.md#finite-error-upper-bound).

### M10: Collective processing and adaptive pair rounds

**Phase:** Background/preliminaries.

**Central question:** Which distinction in measurement access is responsible for the comparison in this project?

**Understanding target:** Specify a collective measurement on retained copies and a protocol using two fresh copies per round with arbitrary classical adaptation. Keep the latter's absence of a persistent quantum register explicit. Explain why retaining many copies coherently is a resource even when the circuit uses gates that each touch only a few qubits.

**Dependencies and story role:** M04, M05, M06, M08. This establishes the two measurement classes under the same source and acquisition model.

**Conceptual connection:** The statistical comparison changes the permitted quantum memory and joint measurement, while keeping the received-copy source promise fixed. Classical adaptation is already included in the pair benchmark.

**Source pointers:** [Watrous §2.2.1, “Definitions and basic notions concerning channels,” and §2.3.1, “Two equivalent definitions of measurements”][W2]. The architecture restrictions are specified by the project's [access and resource contract](../science/model.md#access-and-resource-contract) and [pair comparison](../science/pair_comparison.md).

### M11: The complete model and its resource contract

**Phase:** Background/preliminaries.

**Central question:** What exactly must be held fixed for a statement about sample advantage to have a definite meaning?

**Understanding target:** State the source hypotheses, equal priors, fixed Haar source, known acquisition channel, allowed measurements and constant-error target together. Separate supplied copies, protected qubits and gates. Keep the Haar-average upper quantifier distinct from a guarantee for every pure source, and identify the acquisition and downstream noise assumptions.

**Dependencies and story role:** M03, M05, M06, M07, M09, M10. This completes the background phase by integrating its local objects into one global experiment.

**Conceptual connection:** The later theorem is meaningful because its converse and construction refer to the same statistical problem. The resource contract also distinguishes ideal protected readout from a hardware model with noisy storage, calibration or fault-tolerance overhead.

**Source pointers:** [Watrous §2.2.1, “Definitions and basic notions concerning channels,” and §2.3.1, “Two equivalent definitions of measurements”][W2]; [§3.1.1, “Discriminating between pairs of quantum states”][W3]. Project: [Statistical model](../science/model.md#statistical-model-and-theorem), [access contract](../science/model.md#access-and-resource-contract) and [resources and physical meaning](../science/interpretation.md#resources-and-physical-meaning).

## Phase II: Narrative/innovation

### M12: Match the pair statistic to the noise spectrum

**Phase:** Narrative/innovation.

**Central question:** How should the two-copy correlations be weighted when high-weight Pauli coefficients have been more strongly attenuated?

**Understanding target:** Explain the choice of weights $`\eta^{2w(P)}`$ in the pair kernel. Follow the Cauchy–Schwarz comparison of mean signal with null variance within the Pauli-diagonal kernel family. Identify $`L=(1+3\eta^4)^n-1`$ as the resulting fourth-power spectral weight. Distinguish this optimization within a kernel family from a converse against all measurements.

**Dependencies and story role:** M02, M03, M07, M09, M11. This starts the narrative with one local statistical design decision tied to the physical channel.

**Conceptual connection:** The received Haar ensemble has unequal Pauli variances after noise. Matching the statistic to that structure yields both its mean signal and the spectral quantity that later reappears in the converse.

**Source pointers:** [Watrous §1.1.3, “Operator decompositions and norms”][W1]; [§7.2.1, “Uniform spherical measure and Haar measure,” Lemma 7.24][W7]. Project: [Why the fourth power of attenuation appears](../science/interpretation.md#why-the-fourth-power-of-attenuation-appears) and [the weighted kernel, Eq. (32)](../science/collective_measurement.md#a-collective-pair-sum-observable).

### M13: A concrete weighted Bell-pair experiment

**Phase:** Narrative/innovation.

**Central question:** What are the operations and numerical outcomes of a single measurement of the weighted pair statistic?

**Understanding target:** Describe Bell-basis measurements on corresponding physical qubits in two received copies. Explain how the number of singlet outcomes determines the reported eigenvalue of the pair kernel. Retain the sign of the singlet factor when it is negative. Treat this as an observable experiment whose repeated-sampling requirement still needs analysis.

**Dependencies and story role:** M04, M08, M10, M12. This turns the weighted operator into a complete two-copy laboratory-level measurement primitive.

**Conceptual connection:** Local Bell outcomes give a transparent baseline for what a pair device can observe. The same triplet/singlet decomposition also permits a coherent version of the operation.

**Source pointers:** [Watrous §2.3.1, “Two equivalent definitions of measurements”][W2]; [§7.1.1, “The subspace of permutation-invariant vectors”][W7]. Project: [The explicit Bell-pair experiment](../science/pair_comparison.md#an-explicit-repeated-pair-upper-bound), [the local pair factor](../science/measurement_resources.md#a-hermitian-block-encoding-of-each-pair-factor), and [the complete one-qubit example](BRIDGE.md#a-complete-example-a-hidden-qubit-and-a-bell-measurement). The pair sample bound is established only after the variance analysis.

### M14: Keep the pair operation coherent with a unitary dilation

**Phase:** Narrative/innovation.

**Central question:** How can the weighted pair operator be used coherently without discarding unsuccessful flag outcomes?

**Understanding target:** Explain the normalization of the local pair factor and its triplet/singlet eigenvalues. Follow the flag-assisted Hermitian involution whose zero-flag block equals that normalized factor. Distinguish the mathematical extraction of a block from physical postselection, and recognize why independent flags are used for the physical sites.

**Dependencies and story role:** M03, M04, M12, M13. This supplies the reversible local operation needed for coherent processing of many candidate pairs.

**Conceptual connection:** The ancilla representation of quantum operations gives the language for a block encoding. The project's explicit dilation preserves coherence and charges the auxiliary qubits instead of treating a nonunitary operator as a free gate.

**Source pointers:** [Watrous §2.2.2, “Representations and characterizations of channels”][W2]. Project: [A Hermitian block encoding of each pair factor](../science/measurement_resources.md#a-hermitian-block-encoding-of-each-pair-factor). The particular block-encoding construction is supplied by the project and its cited research tools.

### M15: Assemble all pairs without QRAM

**Phase:** Narrative/innovation.

**Central question:** How can one retained register support a coherent sum over all copy pairs with explicit access costs?

**Understanding target:** Interpret the Hermitian pair average $`U_m`$ and its noncommuting overlapping terms. Explain uniform ordered addresses, the zero-block diagonal-address branch, reversible routing and return of the work registers to zero. Track the known identity shift and normalization, and understand why the linear scan has a gate cost rather than unit-cost addressed access.

**Dependencies and story role:** M02, M10, M14. This composes the local operation into a global observable on the original copies.

**Conceptual connection:** The number of pair terms is an algebraic feature of a collective measurement. It does not provide additional independent source copies or permit simultaneous separate measurements of noncommuting terms.

**Source pointers:** [Watrous §1.1.2, “Linear operators”][W1]; [§2.2.2, “Representations and characterizations of channels”][W2]. Project: [The pair-sum observable](../science/collective_measurement.md#a-collective-pair-sum-observable) and [uniform pair selection with explicit routing](../science/measurement_resources.md#uniform-pair-selection-with-explicit-routing).

### M16: Read a collective eigenvalue on the retained input

**Phase:** Narrative/innovation.

**Central question:** How does the coherent encoding produce a measurement outcome for an arbitrary unknown input state?

**Understanding target:** Follow the invariant two-dimensional subspaces of the walk formed from the block unitary and an auxiliary-register reflection. Explain why the two associated phases give the same eigenvalue after taking a cosine. Interpret phase estimation on an arbitrary spectral mixture, and understand why repeated rounds retain the entire walk register while resetting only phase-readout ancillas.

**Dependencies and story role:** M04, M05, M15. This completes the passage from a local coherent factor to a usable collective spectral measurement.

**Conceptual connection:** Spectral decomposition supplies the measurement interpretation; the explicit walk supplies its implementation. No eigenvector preparation, inverse source-preparation oracle or additional unknown copies are required by the readout repetition.

**Source pointers:** [Watrous §1.1.3, “Operator decompositions and norms”][W1]; [§2.3.1, “Two equivalent definitions of measurements”][W2]. Project: [Qubitization and eigenvalue discrimination](../science/measurement_resources.md#qubitization-and-eigenvalue-discrimination). Qubitization and phase estimation are project-supplied constructions with research attribution, rather than results assigned to these textbook sections.

### M17: Charge precision, gates, and protected memory

**Phase:** Narrative/innovation.

**Central question:** What resources does the collective readout require for a specified number of input copies and a requested value accuracy?

**Understanding target:** Count the $`mn`$ protected input qubits, auxiliary registers, explicit routing gates and phase-estimation calls. Express the query cost in terms of the encoding normalization $`\alpha`$ and a requested additive error $`\Delta`$. Explain certified parameter bounds, a fixed query schedule, subsequent parameter refinement and finite-library gate synthesis. Keep calibration and physical fault-tolerance overhead outside the stated known-parameter protected-processing model.

**Dependencies and story role:** M11, M12, M15, M16. This completes the operational resource account with $`m`$ still an input size; it does not yet assign the statistically required number of copies.

**Conceptual connection:** A smaller decision margin requires more accurate readout and more gates. The eventual sample theorem can be substituted into this conditional account only after the signal and error probabilities have been established.

**Source pointers:** [Watrous §1.1.3, “Operator decompositions and norms”][W1]; [§2.2.2, “Representations and characterizations of channels”][W2]. Project: [The resource statement](../science/measurement_resources.md#model-and-resource-statement), [threshold accuracy](../science/measurement_resources.md#a-threshold-margin-preserves-the-copy-bound) and [finite gate precision and supplied noise parameter](../science/measurement_resources.md#finite-gate-precision-and-the-supplied-value-of-eta). Gate synthesis and routing bounds are supplied by the project and its research references.

### M18: Why null fluctuations fall as one over the copy count

**Phase:** Narrative/innovation.

**Central question:** Why does the collective statistic have a standard deviation proportional to $`1/m`$ under the maximally mixed hypothesis?

**Understanding target:** Separate identical pairs, pairs sharing one copy and disjoint pairs in the second moment of $`U_m`$. Explain why the shared-copy contribution vanishes at the maximally mixed state, leaving variance $`L/\binom m2`$. Distinguish this cancellation from an assumption that all pair terms are independent or jointly measurable.

**Dependencies and story role:** M09, M12, M15, M16. This identifies the statistical mechanism made available by the collective observable.

**Conceptual connection:** The known null state makes the pair kernel degenerate in the variance calculation. That property joins the all-pair algebra to a reduced measurement fluctuation scale without creating extra physical samples.

**Source pointers:** [Watrous §1.2.2, “Probability theory”][W1]; [§2.3.2, “Basic notions concerning measurements”][W2]. Project: [Pair-overlap counting and null variance, Eqs. (37)–(39)](../science/collective_measurement.md#a-collective-pair-sum-observable) and [how collective processing changes sampling](../science/interpretation.md#how-collective-processing-changes-sampling).

### M19: Shared copies and the alternative's two fluctuations

**Phase:** Narrative/innovation.

**Central question:** What additional fluctuations appear when the source is a fixed unknown pure state?

**Understanding target:** Identify the shared-copy overlap as a real nonnegative expectation of a squared Hermitian operator, despite noncommuting pair terms. Separate the conditional measurement variance from the Haar variance of the signal itself. Explain why controlling only the averaged signal or only the null variance cannot establish the alternative's error probability.

**Dependencies and story role:** M06, M09, M15, M18. This exposes the two obstacles that must be controlled before the collective variance advantage becomes a valid test.

**Conceptual connection:** Partial trace reduces a three-copy overlap to a single-copy expectation, while ordinary conditional probability retains the common hidden source. The next estimates must handle both structures.

**Source pointers:** [Watrous §1.2.2, “Probability theory”][W1]; [§2.1.3, “Reductions and purifications of quantum states,” and §2.3.2, “Basic notions concerning measurements”][W2]. Project: [Overlap reduction, Eqs. (35)–(38)](../science/collective_measurement.md#a-collective-pair-sum-observable) and [total variance](../science/collective_measurement.md#finite-error-upper-bound).

### M20: Haar contractions give a concentrating signal

**Phase:** Narrative/innovation.

**Central question:** How can exact finite-dimensional calculations control the signal when the number of physical qubits grows?

**Understanding target:** Connect the second Haar moment to the mean signal, the third to shared-copy overlaps, and the fourth to fluctuations of the conditional mean. Explain how the one-site Pauli table, including commutation signs, produces tensor-product expressions across $`n`$ sites. Interpret the resulting exponentially decreasing relative signal variance and the explicit sufficient cutoff $`n_0(\eta)`$ for fixed $`\eta`$.

**Dependencies and story role:** M02, M07, M12, M19. This supplies uniform control of the two alternative fluctuation terms rather than relying on a large-dimension heuristic.

**Conceptual connection:** The Haar prior is globally symmetric, but the channel and Pauli counting factor over physical sites. Their combination produces exact formulas with the dimension factors retained.

**Source pointers:** [Watrous §7.1.1, “The subspace of permutation-invariant vectors,” and §7.2.1, “Uniform spherical measure and Haar measure,” especially Lemma 7.24][W7]. Project: [Exact contractions](../science/haar_moments.md#exact-second--third--and-fourth-moment-contractions) and [uniform bounds and concentration cutoff](../science/haar_moments.md#uniform-moment-bounds-and-a-finite-concentration-cutoff).

### M21: An explicit finite-error collective test

**Phase:** Narrative/innovation.

**Central question:** How do the signal and variance estimates become a concrete decision guarantee at a specified number of copies?

**Understanding target:** Explain the threshold at half the averaged signal and combine null variance, conditional alternative variance and source concentration. Identify the sufficient scale $`M=t_{n,\eta}=\sqrt{d(d+1)/L}`$ and the role of the finite cutoff. Interpret the explicit error constants as a Haar-average guarantee, and explain how a readout margin preserves that guarantee under controlled implementation error.

**Dependencies and story role:** M09, M12, M17, M18, M19, M20. This establishes an achievable sample scale for the actual experiment.

**Conceptual connection:** A favorable expectation becomes useful only when both hypothesis errors are bounded. The accuracy account of the coherent protocol fits into the same statistical decision margin.

**Source pointers:** [Watrous §1.2.2, “Probability theory”][W1]; [§3.1.1, “Discriminating between pairs of quantum states”][W3]. Project: [Finite-error upper bound](../science/collective_measurement.md#finite-error-upper-bound), [Theorem 1](../science/model.md#theorem-1) and [the implementation margin](../science/measurement_resources.md#a-threshold-margin-preserves-the-copy-bound).

### M22: Output mixtures give a universal converse

**Phase:** Narrative/innovation.

**Central question:** How can the analysis rule out all collective measurements instead of only competing choices of pair weights?

**Understanding target:** Express the discrimination problem through the two full received density operators. Interpret the mixture collision integral and the round-trip channel $`\mathcal N_\eta^*\mathcal N_\eta`$. Distinguish the independent mathematical source variables in that integral from the single physical source fixed across the supplied copies. Recognize the same spectral quantity $`L`$ that governs the constructive signal.

**Dependencies and story role:** M03, M05, M06, M07, M12, M21. This introduces the measurement-independent obstruction needed to establish optimality.

**Conceptual connection:** A bound on the distance of the output mixtures constrains every decision effect. The adjoint channel moves acquisition noise into an overlap kernel, joining the statistical converse to the channel spectrum used by the measurement.

**Source pointers:** [Watrous §1.1.2, “Linear operators,” for adjoint maps][W1]; [§3.1.1, “Discriminating between pairs of quantum states”][W3]. Project: [The round-trip channel and converse](../science/collective_lower_bound.md#collective-lower-bound-by-trimming-the-haar-prior) and [mixture-divergence attribution](../references/RELATED_WORK.md#mixture-divergences-and-the-converse).

### M23: Centering isolates the informative Haar fluctuations

**Phase:** Narrative/innovation.

**Central question:** Why does subtracting the maximally mixed reference make the higher Haar moments manageable?

**Understanding target:** Explain how the centered round-trip output has zero trace, eliminating permutation terms with fixed points. Relate the remaining cycle traces to a Hilbert–Schmidt norm and a conditional moment bound. Identify the remaining obstacle: this norm depends on the source, so its average cannot simply be substituted inside an exponential or high power.

**Dependencies and story role:** M07, M09, M22. This isolates the informative part of the collision kernel and identifies exactly where tail control is still needed.

**Conceptual connection:** Centering removes the common identity component of the two hypotheses. Permutation moments and operator-norm inequalities then control the fluctuations without assuming they are Gaussian.

**Source pointers:** [Watrous §1.1.3, “Operator decompositions and norms,” for Schatten norms and monotonicity][W1]; [§7.2.1, “Uniform spherical measure and Haar measure,” Lemma 7.24][W7]. Project: [A centered Haar moment bound](../science/collective_lower_bound.md#a-centered-haar-moment-bound).

### M24: Trim rare sources while controlling lost prior mass

**Phase:** Narrative/innovation.

**Central question:** How can a converse handle exceptional source states without silently replacing the original testing problem?

**Understanding target:** Explain the high-probability source set, conditioning of both prior variables, and its normalization factors. Identify the nonnegative-kernel step that permits enlarging one integration domain. Restore the original prior by paying the discarded mass in trace distance, thereby obtaining a lower bound at the scale $`M`$. Distinguish conditioning in a proof from an experimentally available source filter or postselection procedure.

**Dependencies and story role:** M05, M09, M22, M23. This completes the converse while keeping the original fixed-Haar-source promise intact.

**Conceptual connection:** Ordinary probability controls the exceptional prior mass, and operational trace distance measures the effect of returning it. The lower bound remains valid for every downstream collective test.

**Source pointers:** [Watrous §1.2.2, “Probability theory”][W1]; [§3.1.1, “Discriminating between pairs of quantum states”][W3]. Project: [Truncation and the collision integral](../science/collective_lower_bound.md#truncation-and-the-collision-integral), including the final error bound.

### M25: Match both directions to obtain the sharp law

**Phase:** Narrative/innovation.

**Central question:** What turns a successful collective measurement into an optimal copy-complexity theorem?

**Understanding target:** Combine the sufficient scale from the test and the necessary scale from the converse. Explain how the exact finite-dimensional scale $`M`$ becomes the fixed-$`\eta`$ exponential law in $`n`$. Preserve the dependence of the cutoff on the noise parameter and the distinction between a Haar-average upper bound and a worst-case lower implication. Now substitute the established $`m=\Theta_\eta(M)`$ scale into the previously conditional implementation account.

**Dependencies and story role:** M11, M17, M21, M24. This joins the constructive and impossibility arguments into the main theorem.

**Conceptual connection:** Agreement of the two bounds proves global statistical optimality; optimizing the kernel alone would not suffice. Combining that theorem with the gate construction supplies an implementable protected readout while leaving gate optimality as a separate question.

**Source pointers:** [Watrous §3.1.1, “Discriminating between pairs of quantum states”][W3]; [§7.2.1, “Uniform spherical measure and Haar measure”][W7]. Project: [Theorem 1](../science/model.md#theorem-1), [the exact-to-asymptotic relation](../science/model.md#asymptotic-rate-and-the-noiseless-or-fully-depolarized-endpoints) and [charged implementation](../science/measurement_resources.md).

### M26: What fresh-pair repetition can achieve

**Phase:** Narrative/innovation.

**Central question:** How many supplied copies suffice when the weighted Bell experiment is repeated on fresh pairs?

**Understanding target:** Derive the meaning of the $`O_\eta(M^2)`$ pair upper bound from conditional independence of fresh pairs and the remaining common-source variance. Explain the streaming classical estimator, its finite-arithmetic margin and its $`2n`$ coherent data-qubit requirement. Keep this constructive guarantee distinct from a lower bound on every pair strategy.

**Dependencies and story role:** M09, M10, M13, M20, M25. This gives the explicit pair architecture a quantitative performance guarantee under the same task as the collective theorem.

**Conceptual connection:** The local measurement primitive stays simple, while its sample average has a different variance scaling from the spectral measurement of the all-pair sum. Both experiments still share the same fixed hidden source.

**Source pointers:** [Watrous §1.2.2, “Probability theory”][W1]; [§2.3.1, “Two equivalent definitions of measurements”][W2]. Project: [Repeated-pair upper bound](../science/pair_comparison.md#an-explicit-repeated-pair-upper-bound) and [finite classical precision](../science/pair_comparison.md#finite-classical-precision).

### M27: What every adaptive pair strategy must pay

**Phase:** Narrative/innovation.

**Central question:** What establishes a limitation on all adaptive pair strategies rather than on one repeated estimator?

**Understanding target:** State the imported adaptive-pair lower bound and match its prior, acquisition noise, measurement access and error criterion to this project. Explain why classical outcomes update a posterior on the fixed source, invalidating an argument that treats prior-averaged pair rounds as independent. Keep the prohibition on persistent quantum memory explicit.

**Dependencies and story role:** M06, M10, M22, M26. This supplies the research-level dependency required for an architecture-wide separation.

**Conceptual connection:** A single averaged pair's distinguishability does not settle an adaptive sequence. The cited learning-tree theorem provides the necessary control over all classical histories within the pair model.

**Source pointers:** [Watrous §3.1.1, “Discriminating between pairs of quantum states”][W3] supplies the operational background. Project: [The imported lower bound and its model match](../science/pair_comparison.md#exactly-where-the-quadratic-separation-is-proved) and [adaptive two-copy learning attribution](../references/RELATED_WORK.md#adaptive-two-copy-learning). The Cotler–Gong–Kannan theorem cited there is a research dependency, not a theorem attributed to the educational anchor.

### M28: Locate the exponential and quadratic separation regimes

**Phase:** Narrative/innovation.

**Central question:** Which noise ranges support an exponential sample advantage, and where are both optimal sample rates known?

**Understanding target:** Compare the collective scale, the explicit pair upper bound and both branches of the inherited pair lower bound. Explain the exponential-separation condition $`\eta\gt3^{-1/4}`$ and the exact quadratic regime $`\eta\ge[(2\sqrt2-1)/3]^{1/4}`$, with $`\eta\lt1`$. Include the latter's lower endpoint, preserve the unresolved pair exponent in the intermediate interval, and distinguish lack of a certified gap below the first threshold from proof that no gap exists.

**Dependencies and story role:** M25, M26, M27. This combines the statistical results into their precise measurement-architecture consequence.

**Conceptual connection:** The separation is an exponential ratio between two sample counts that themselves remain exponential. It depends on both an attaining collective measurement and a lower bound for the full competing pair class.

**Source pointers:** [Watrous §3.1.1, “Discriminating between pairs of quantum states”][W3] fixes the common error criterion. The exponent comparison and its thresholds are project-specific: [Exactly where the quadratic separation is proved](../science/pair_comparison.md#exactly-where-the-quadratic-separation-is-proved).

### M29: Interpret the rate, endpoints, and inherited methods

**Phase:** Narrative/innovation.

**Central question:** What information does the sharp rate measure, and how does it fit its limiting cases and methodological predecessors?

**Understanding target:** Relate the fourth-power attenuation weight to both the signal design and round-trip converse. Explain the fully depolarized impossibility and the noiseless symmetric-subspace test. Distinguish these endpoint statements from a uniform theorem for an arbitrary varying noise sequence. Identify the inherited U-statistic, mixture-divergence and fixed-noise-hardness frameworks, while keeping the new sharp Haar-average rate and pair-architecture consequence explicit.

**Dependencies and story role:** M07, M11, M25, M28. This places the mathematical law inside its physical and research context.

**Conceptual connection:** The endpoints clarify which information acquisition preserves. Attribution clarifies which parts of the reasoning are established tools and why the earlier noise-budget project's optimal worst-case exponent is not determined by the present average-case upper bound.

**Source pointers:** [Watrous §7.1.1, “The subspace of permutation-invariant vectors,” Corollary 7.3; §7.2.1, “Uniform spherical measure and Haar measure,” Lemma 7.24][W7]. Project: [Endpoints](../science/model.md#asymptotic-rate-and-the-noiseless-or-fully-depolarized-endpoints), [interpretation](../science/interpretation.md), and [related work](../references/RELATED_WORK.md).

### M30: Synthesize the result and its remaining limits

**Phase:** Narrative/innovation.

**Central question:** What complete scientific conclusion follows when the experiment, proof, implementation and comparison are considered together?

**Understanding target:** Give one consistent account of the fixed-source Haar-average task, the matching collective bounds, the explicit readout, and the certified pair-separation regimes. Explain the final protected-memory and finite-library gate costs after substituting the sample law. Distinguish analytical proof from the finite matrix checks that support its contractions. Keep the unresolved optimal worst-case pure-source exponent, intermediate pair exponent, unknown-noise calibration and noisy-storage or fault-tolerance questions visible.

**Dependencies and story role:** M11, M17, M20, M24, M25, M28, M29. This completes the narrative phase by integrating the statistical and operational components and their limits.

**Conceptual connection:** Ideal coherent processing can produce an exponential relative sample advantage after noisy acquisition while still requiring exponentially many copies and a large protected register. The constructive gate bound is polynomial in that received input size; a computational speedup or practical hardware threshold is a separate claim.

**Source pointers:** [Watrous §2.2, “Quantum channels,” and §2.3, “Measurements”][W2]; [§3.1.1, “Discriminating between pairs of quantum states”][W3]; [§7.2.1, “Uniform spherical measure and Haar measure”][W7]. Project: [The main model](../science/model.md), [resources and physical meaning](../science/interpretation.md#resources-and-physical-meaning), [measurement resources](../science/measurement_resources.md), [pair comparison](../science/pair_comparison.md), and [what establishes the general result](../verification/README.md#what-establishes-the-general-result).

[W1]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf
[W2]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf
[W3]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf
[W7]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf
