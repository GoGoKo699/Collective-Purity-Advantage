"""Direct finite-matrix checks for the collective noisy-purity test.

Build the exact Haar third moment, apply the physical product depolarizing
channel, then measure the actual Hermitian U-statistic matrix. The fourth
moment is checked separately by tracing the signal kernel against all 24
copy permutations. These are deterministic finite checks, not Haar sampling
or a proof of the asymptotic theorem.
"""

from itertools import permutations, product
import json
import numpy as np

PAULI = [np.eye(2), np.array([[0, 1], [1, 0]]),
         np.array([[0, -1j], [1j, 0]]), np.diag([1, -1])]


def kron_all(mats):
    out = np.array([[1.0 + 0j]])
    for mat in mats:
        out = np.kron(out, mat)
    return out


def copy_permutation(d, permutation):
    m = len(permutation)
    out = np.zeros((d**m, d**m), dtype=complex)
    for inputs in product(range(d), repeat=m):
        outputs = tuple(inputs[permutation[j]] for j in range(m))
        col = np.ravel_multi_index(inputs, (d,) * m)
        row = np.ravel_multi_index(outputs, (d,) * m)
        out[row, col] = 1
    return out


def haar_third_moment(d):
    return sum((copy_permutation(d, p) for p in permutations(range(3))),
               np.zeros((d**3, d**3), dtype=complex)) / (d * (d + 1) * (d + 2))


def local_depolarize_all(rho, eta, qubits):
    # D_eta = [(1+3 eta)/4] I(.)I + [(1-eta)/4] sum_P=X,Y,Z P(.)P.
    weights = [(1 + 3 * eta) / 4] + [(1 - eta) / 4] * 3
    out = rho.copy()
    for site in range(qubits):
        updated = np.zeros_like(out)
        for k, weight in enumerate(weights):
            mats = [PAULI[0]] * qubits
            mats[site] = PAULI[k]
            p = kron_all(mats)
            updated += weight * (p @ out @ p)
        out = updated
    return out


def pair_observable(n, m, a, b, eta):
    out = np.zeros((2**(n*m),) * 2, dtype=complex)
    for labels in product(range(4), repeat=n):
        weight = sum(label != 0 for label in labels)
        if weight == 0:
            continue
        mats = [PAULI[0]] * (n*m)
        for site, label in enumerate(labels):
            mats[a*n + site] = PAULI[label]
            mats[b*n + site] = PAULI[label]
        out += eta**(2*weight) * kron_all(mats)
    return out


def moments(n, eta):
    d = 2**n
    s = (1 + 3*eta**4)**n
    t = (1 + 9*eta**4 - 6*eta**6)**n
    v = (1 + 3*eta**6)**n
    q0 = 1 + 6*eta**4 + 3*eta**6
    c = ((q0 + 6*eta**7)**n + (q0 - 6*eta**7)**n) / 2
    mu = (s - 1)/(d + 1)
    b2 = (d*(s-1) + t - 2*s + 1)/(d + 1)
    overlap = (d*(v-1) + 2*c - 4*s + 2)/((d+1)*(d+2))
    return mu, b2, overlap


def run(eta):
    n, m, d = 2, 3, 4
    omega = local_depolarize_all(haar_third_moment(d), eta, n*m)
    pairs = [pair_observable(n, m, a, b, eta)
             for a, b in [(0, 1), (0, 2), (1, 2)]]
    u = sum(pairs)/3
    mu, b2, overlap = moments(n, eta)
    observed = {
        "mean": np.trace(u @ omega),
        "pair_second_moment": np.trace(pairs[0] @ pairs[0] @ omega),
        "overlap": np.trace(pairs[0] @ pairs[1] @ omega),
        "u_second_moment": np.trace(u @ u @ omega),
    }
    expected = {
        "mean": mu,
        "pair_second_moment": b2,
        "overlap": overlap,
        "u_second_moment": (b2 + 2*overlap)/3,
    }
    errors = {key: float(abs(observed[key] - expected[key])) for key in observed}
    assert np.linalg.norm(u - u.conj().T) < 1e-12
    assert abs(np.trace(omega) - 1) < 1e-12
    assert max(errors.values()) < 2e-12
    return {"n": n, "m": m, "eta": eta,
            "expected": expected,
            "observed": {key: float(value.real) for key, value in observed.items()},
            "max_abs_error": max(errors.values()),
            "max_imaginary_part": float(max(abs(value.imag) for value in observed.values()))}


def signal_fourth_moment(n, eta):
    """Compute E(mu_psi^2) directly from the fourth Haar moment."""
    d = 2**n
    # Passing sqrt(eta^4)=eta^2 gives the signal kernel coefficients eta^(4w).
    z = pair_observable(n, 2, 0, 1, eta**2)
    z_four = np.kron(z, z)
    denom = d * (d + 1) * (d + 2) * (d + 3)
    observed = sum(np.trace(z_four @ copy_permutation(d, p))
                   for p in permutations(range(4))) / denom
    s = (1 + 3*eta**4)**n
    b8 = (1 + 3*eta**8)**n
    c8 = (1 + 6*eta**4 - 3*eta**8)**n
    expected = ((d + 4)*(s - 1)**2 + 2*(c8 - 2*s + 1)
                + 2*d*(b8 - 1)) / ((d + 1)*(d + 2)*(d + 3))
    mean = (s - 1)/(d + 1)
    variance_formula = 2*(d*(d + 1)*b8 + (d + 1)*c8 - s**2
                          - 2*d*s - d**2) / ((d + 1)**2*(d + 2)*(d + 3))
    error = max(abs(observed - expected),
                abs(observed - mean**2 - variance_formula))
    assert error < 2e-12
    assert abs(observed.imag) < 2e-12
    return {"n": n, "eta": eta,
            "signal_second_moment_observed": float(observed.real),
            "signal_second_moment_formula": float(expected),
            "signal_variance_formula": float(variance_formula),
            "max_abs_error": float(error)}


def run_all():
    return {"third_moment_checks": [run(0.3), run(0.9)],
            "fourth_moment_checks": [signal_fourth_moment(n, eta)
                                     for n in (1, 2)
                                     for eta in (0.0, 0.3, 0.9, 1.0)]}


if __name__ == "__main__":
    import argparse
    from pathlib import Path
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        help="Optional JSON result path; stdout always shows results.")
    args = parser.parse_args()
    output = json.dumps(run_all(), indent=2) + "\n"
    if args.output:
        args.output.write_text(output, encoding="utf-8")
    print(output, end="")
