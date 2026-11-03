# Skew Transforms

Intermediate | data-science | feature-transformation

### The problem, from first principles

`03-feature-scaling` puts features on a common scale, but scaling does not change a distribution's shape. Incomes, prices, counts and response times pile up near zero with a long tail of huge values, and in that shape a handful of extreme rows dominate the mean, the variance and any linear model's fit. A transform that compresses the tail, a logarithm or a power, pulls such a feature closer to symmetric and makes the extreme rows ordinary again. This question measures skewness and builds the transforms that reduce it.

### From theory to code

Implement `skewness(x)`, which measures how lopsided a sample is, then `log1p_transform(x)` and its inverse `inverse_log1p(z)`, then `box_cox(x, lam)`, a family of power transforms controlled by one number, then `best_box_cox_lambda(x, candidates)`, which picks the candidate that makes the sample most symmetric. The signatures and docstrings are already in the editor.

### Constraints

- `x` is a 1D float array. `skewness` returns the population skewness, the mean of cubed standardized values, `mean(((x - mean) / std) ** 3)` with `std` the population standard deviation. It returns `0.0` when `std` is zero.
- `log1p_transform(x)` returns `log(1 + x)` and raises `ValueError` if any value is negative. `inverse_log1p(z)` returns `exp(z) - 1`. Use `np.log1p` and `np.expm1`.
- `box_cox(x, lam)` requires every value to be strictly positive and raises `ValueError` otherwise. It returns `(x ** lam - 1) / lam` for `lam != 0` and `log(x)` for `lam == 0`.
- `best_box_cox_lambda(x, candidates)` returns the value in `candidates` whose Box-Cox transform has the smallest absolute skewness. On a tie it returns the earliest candidate in the list.
- Inputs must not be modified.

### Hints

<details>
<summary>Hint 1</summary>

A symmetric sample has skewness near zero. A long right tail gives a positive number, a long left tail a negative one.

</details>

<details>
<summary>Hint 2</summary>

`log1p` is used instead of `log` because it accepts zero, which counts, clicks and many amounts contain. It is also more accurate than `log(1 + x)` for tiny `x`.

</details>

<details>
<summary>Hint 3</summary>

Box-Cox with `lam = 1` is the identity up to a shift, `lam = 0.5` is a square-root-like transform and `lam = 0` is the logarithm, so trying a short list of lambdas covers the usual choices.

</details>
