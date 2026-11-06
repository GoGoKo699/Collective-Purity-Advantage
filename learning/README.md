# Learning route

The central question is how a joint measurement can recognize a pure source after each received copy has been mixed by local noise. The route connects the statistical task, a physically specified measurement and the comparison with experiments that can process only two fresh copies at a time.

The educational anchor is **John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018)**: [author's book page](https://cs.uwaterloo.ca/~watrous/TQI/), [publisher edition](https://doi.org/10.1017/9781316848142). Its state, channel, discrimination and Haar-measure foundations support the route. The project supplies the noise-matched statistic, its moment estimates, the conditioned-prior converse and the implementation/resource analysis.

## Start here

Read the [source-to-project bridge](BRIDGE.md) for the relevant parts of Watrous, a notation translation, a complete one-qubit example and the steps from textbook foundations to the theorem. Then follow the [30-milestone map](MILESTONES.md). Each milestone states a question, an understanding target, earlier dependencies, its place in the argument and pointers to the scientific account.

The map has **11 background/preliminaries milestones and 19 narrative/innovation milestones**. The first phase builds from individual states and channels to the complete fixed-source experiment. The second builds a noise-matched pair operation into a collective protocol, establishes its performance and converse, and then derives the architecture comparison.

| Part of the route | Understanding it develops | Scientific destination |
| --- | --- | --- |
| M01–M11: background and the complete model | States, acquisition noise, shared-source correlations, discrimination, Haar symmetry and measurement capabilities | [Model and theorem](../science/model.md) |
| M12–M17: construct the measurement | Weighted Bell outcomes, coherent pair operations, explicit routing, spectral readout and charged resources | [Collective measurement](../science/collective_measurement.md) and [implementation](../science/measurement_resources.md) |
| M18–M25: establish the copy law | Pair-overlap variance, source concentration, a finite-error upper bound, prior conditioning and a universal converse | [Haar moments](../science/haar_moments.md) and [collective lower bound](../science/collective_lower_bound.md) |
| M26–M30: compare and interpret | Pair repetition, the inherited adaptive lower bound, separation regimes, endpoints and scientific scope | [Pair comparison](../science/pair_comparison.md) and [interpretation](../science/interpretation.md) |

## Keep the question fixed

One hidden Haar-random pure state is drawn once and supplies every copy. The performance guarantee averages over that source; it does not assert a matching upper bound for every pure state. Noise acts during acquisition, while downstream storage and gates are protected. Pair experiments keep classical history but no quantum register between rounds. Sample counts, protected memory, gate costs and supplied parameter precision answer different resource questions.

These distinctions recur in the milestones because changing them changes the scientific task. The complete statements and proofs remain in [science/](../science/README.md); the map selects their conceptual connections rather than reproducing every calculation. The [related-work account](../references/RELATED_WORK.md) distinguishes the project's contribution from its inherited ingredients, and the [verification route](../verification/README.md) explains what the finite checks establish.

[Repository overview](../README.md) · [Bridge](BRIDGE.md) · [Milestone map](MILESTONES.md) · [Scientific route](../science/README.md)
