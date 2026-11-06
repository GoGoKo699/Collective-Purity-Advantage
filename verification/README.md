# Verification

## Run the direct matrix checks

Use Python 3.10 or later and NumPy:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/verify_moments.py
```

To save a new result file, pass a path explicitly:

```bash
python3 verification/verify_moments.py --output /tmp/purity-moments.json
```

The script exits unsuccessfully if any asserted residual exceeds its stated tolerance. [expected_results.json](expected_results.json) records a successful reference run. Floating-point roundoff may change final digits; residuals below $`2\times10^{-12}`$ are accepted. Tiny negative values of a displayed variance, at the scale of roundoff, are numerical cancellation residuals.

## What is checked

For $`n=2,m=3`$ and $`\eta=0.3,0.9`$, the script builds the exact Haar third-moment operator as a permutation sum, applies the physical local depolarizing channel by Pauli conjugation, constructs the actual pair-sum matrix, and evaluates its first and second moments. This checks the pair moment, noncommuting shared-copy contraction and edge-counting variance normalization against the [analytical expressions](../science/haar_moments.md). The largest observed absolute error in the reference run is below $`1.8\times10^{-15}`$.

Separately, for $`n=1,2`$ and $`\eta=0,0.3,0.9,1`$, the script traces the signal kernel against all 24 four-copy permutations. It compares the resulting $`\mathbb E\mu_\psi^2`$ and variance with the exact fourth-moment formulas. These checks include the zero-variance one-qubit and noiseless limits. The largest fourth-moment residual is below $`4.5\times10^{-16}`$ in the reference run.

There is no Monte Carlo sampling. The direct matrix construction is independent of the scalar formulas it checks.

## What establishes the general result

The separate [hosted-mathematics check](hosted/README.md) compares pinned source equations with actual GitHub rendering and saves screenshots for visual inspection. It complements these numerical checks; neither kind of check replaces a proof.

The all-dimension converse, finite-error upper theorem and asymptotic rate are proved in the [scientific account](../science/README.md). Small matrices do not establish those universal claims. The [resource construction](../science/measurement_resources.md) and the imported adaptive-pair lower bound are separate analytical arguments. No claim of experimental implementation or independent external replication is made.
