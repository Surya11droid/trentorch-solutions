\
import numpy as np


def importance_estimate(f, p_pdf, q_pdf, draws) -> float:
    """Estimate E_p[f(X)] using samples drawn from q."""
    weights = p_pdf(draws) / q_pdf(draws)
    return float(np.mean(f(draws) * weights))


def self_normalized_estimate(f, p_pdf, q_pdf, draws) -> float:
    """Estimate E_p[f(X)] using normalized importance weights."""
    weights = p_pdf(draws) / q_pdf(draws)
    return float(
        np.sum(f(draws) * weights) / np.sum(weights)
    )


def effective_sample_size(weights) -> float:
    """Calculate effective sample size from importance weights."""
    weights = np.asarray(weights, dtype=float)
    return float(
        np.sum(weights) ** 2 / np.sum(weights ** 2)
    )
