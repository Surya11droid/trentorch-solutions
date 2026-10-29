# Markov Chain Monte Carlo

Advanced | data-science | simulation | probability | mcmc

### The problem, from first principles

Monte Carlo estimation needs draws from a distribution. For many distributions that matter, such as the posterior of a Bayesian model, there is no way to draw from them directly: the density can be evaluated at any point, but only up to a constant, because the constant is an integral nobody can compute. Markov chain Monte Carlo gets around this by walking. A **Markov chain** takes a random step, proposes a move to a nearby point, and accepts or rejects the move with a probability designed so that, in the long run, the places the walker visits are distributed exactly like the target. This question builds the simplest and most widely used version, the Metropolis algorithm with Gaussian steps, and the tools to judge whether a chain can be trusted.

### From theory to code

Implement `metropolis_hastings(log_target, x0, n_steps, step_size, rng)`, which runs the walk, then `burn_in_and_thin(samples, burn_in, thin)`, which discards the early and redundant samples, then `autocorrelation(samples, lag)`, which measures how strongly each sample depends on the one `lag` steps earlier, then `mcmc_effective_sample_size(samples, max_lag)`, which turns that dependence into the number of independent samples the chain is worth. The signatures and docstrings are already in the editor.

### Constraints

- `log_target(x)` takes a float and returns the log of the target density, up to an additive constant. It may return `-inf` for points outside the support. The state is a single float.
- `metropolis_hastings` starts at `x0`. Each step draws, in this order, `step = rng.normal()` and then `u = rng.random()`. The proposal is `x_new = x + step_size * step`. It accepts when `log(u) < log_target(x_new) - log_target(x)`, otherwise it stays at `x`. The sample recorded for that step is the state after the accept or reject decision, so a rejected step repeats the previous value. It does not record `x0`.
- `metropolis_hastings` returns `(samples, acceptance_rate)`: a float array of length `n_steps` and the fraction of steps that accepted the proposal, as a float. The starting point must satisfy `log_target(x0) > -inf`.
- `burn_in_and_thin(samples, burn_in, thin)` returns `samples[burn_in::thin]` as a new array, for `burn_in >= 0` and `thin >= 1`.
- `autocorrelation(samples, lag)` returns the sample autocorrelation `sum((x[t] - m) * (x[t + lag] - m)) / sum((x[t] - m) ** 2)` with `m` the sample mean, summing `t` over `0 .. n - lag - 1`, as a float. At lag `0` it is `1.0`. It returns `0.0` if the sample has zero variance.
- `mcmc_effective_sample_size(samples, max_lag)` returns `n / (1 + 2 * sum(rho_k))` as a float, where `rho_k` is the autocorrelation at lag `k` and the sum runs over `k = 1, 2, ...` up to `max_lag`, stopping before the first lag whose autocorrelation is negative. The result is at least `1.0` and at most `n`.

### Hints

<details>
<summary>Hint 1</summary>

The acceptance rule never needs the normalizing constant of the target: the constant appears in both `log_target(x_new)` and `log_target(x)` and cancels in their difference. That cancellation is the reason the method works on unnormalized posteriors.

</details>

<details>
<summary>Hint 2</summary>

Compare in log space. A raw density ratio can overflow or underflow, while `log(u) < difference of logs` is stable. A move to a point with a higher density always has a difference above zero and is always accepted.

</details>

<details>
<summary>Hint 3</summary>

The effective sample size shrinks as the autocorrelation grows. If neighbouring samples are nearly copies of each other, thousands of them hold the information of a handful of independent draws.

</details>
