
import numpy as np


def metropolis_hastings(log_target, x0, n_steps, step_size, rng):
    """
    Generate samples using the Metropolis-Hastings algorithm.

    Returns:
        samples: float array of length n_steps
        acceptance_rate: fraction of proposals accepted
    """
    x = float(x0)
    current_log_prob = log_target(x)

    if current_log_prob == -np.inf:
        raise ValueError("Starting point must have finite support.")

    samples = np.empty(n_steps, dtype=float)
    accepted = 0

    for i in range(n_steps):
        # 1. Propose a new position
        step = rng.normal()
        x_new = x + step_size * step

        # 2. Evaluate the proposed position
        new_log_prob = log_target(x_new)
        log_ratio = new_log_prob - current_log_prob

        # 3. Draw u AFTER drawing the normal step
        u = rng.random()

        # Equivalent to log(u) < log_ratio,
        # including the special case u == 0.
        if u == 0.0:
            accept = log_ratio > -np.inf
        else:
            accept = np.log(u) < log_ratio

        # 4. Accept or reject
        if accept:
            x = x_new
            current_log_prob = new_log_prob
            accepted += 1

        # Record the state AFTER the decision
        samples[i] = x

    acceptance_rate = accepted / n_steps if n_steps > 0 else 0.0

    return samples, float(acceptance_rate)


def burn_in_and_thin(samples, burn_in, thin):
    """
    Remove the first burn_in samples and keep every thin-th sample.
    Returns a new array.
    """
    return np.array(samples[burn_in::thin], copy=True)


def autocorrelation(samples, lag):
    """
    Calculate sample autocorrelation at the specified lag.
    """
    samples = np.asarray(samples, dtype=float)
    n = len(samples)

    if lag == 0:
        return 1.0

    if lag < 0 or lag >= n:
        raise ValueError("lag must satisfy 0 <= lag < len(samples)")

    mean = np.mean(samples)
    centered = samples - mean

    denominator = np.sum(centered ** 2)

    if denominator == 0:
        return 0.0

    numerator = np.sum(centered[:-lag] * centered[lag:])

    return float(numerator / denominator)


def mcmc_effective_sample_size(samples, max_lag):
    """
    Estimate effective sample size using positive autocorrelations.
    Stop before the first negative autocorrelation.
    """
    samples = np.asarray(samples, dtype=float)
    n = len(samples)

    if n == 0:
        return 0.0

    autocorr_sum = 0.0

    for lag in range(1, min(max_lag, n - 1) + 1):
        rho = autocorrelation(samples, lag)

        if rho < 0:
            break

        autocorr_sum += rho

    ess = n / (1 + 2 * autocorr_sum)

    return float(np.clip(ess, 1.0, float(n)))
