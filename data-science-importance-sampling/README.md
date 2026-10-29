# Importance Sampling

Advanced | data-science | simulation | probability

### The problem, from first principles

`01-monte-carlo` averages draws from the distribution of interest. That fails for rare events: to estimate the chance that a payment is fraudulent when one in a million is, a million draws contain one hit on average, and the estimate is noise. Importance sampling draws from a _different_ distribution that lands in the interesting region far more often, and then corrects for the switch by weighting each draw by how much more (or less) likely it is under the real distribution. It also lets one set of draws answer questions about several distributions. This question builds the estimator, its self-normalized version and the diagnostic that tells you whether the weights are trustworthy.

### From theory to code

Implement `importance_estimate(f, p_pdf, q_pdf, draws)`, the weighted average that estimates an expectation under `p` from draws taken under `q`, then `self_normalized_estimate(f, p_pdf, q_pdf, draws)`, which works even when `p` is known only up to a constant, then `effective_sample_size(weights)`, which measures how many equally good draws the weighted ones are worth. The signatures and docstrings are already in the editor.

### Constraints

- `draws` is a 1D float array of samples already taken from the proposal distribution `q`. `p_pdf` and `q_pdf` are vectorized functions returning the target and proposal densities at every draw. `f` is a vectorized function of the draws.
- `importance_estimate` returns `mean(f(draws) * w)` as a float, where `w = p_pdf(draws) / q_pdf(draws)`.
- `self_normalized_estimate` returns `sum(f(draws) * w) / sum(w)` as a float, with the same `w`. It must give the same answer if `p_pdf` is multiplied by any positive constant.
- `effective_sample_size(weights)` returns `sum(weights) ** 2 / sum(weights ** 2)` as a float, for a 1D array of non-negative weights with at least one positive entry.
- The proposal density must be positive wherever `p_pdf(x) * f(x)` is nonzero. Inputs must not be modified.

### Hints

<details>
<summary>Hint 1</summary>

Reweighting is a change of measure: $\mathbb{E}_p[f] = \mathbb{E}_q[f \cdot p/q]$. Averaging $f \cdot p/q$ over draws from $q$ therefore estimates the expectation under $p$.

</details>

<details>
<summary>Hint 2</summary>

If $p$ is only known up to a constant (a posterior without its normalizing integral), the plain estimator is off by that constant. Dividing by the sum of the weights cancels it.

</details>

<details>
<summary>Hint 3</summary>

When a few weights are huge and the rest are tiny, the average is really made of a handful of draws. The effective sample size drops to close to that handful.

</details>
