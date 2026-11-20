# The SVM dual objective

Advanced | classical-ml | svm | dual | kernel | optimization

### Score a set of dual variables and check they are legal

The soft-margin SVM can be solved in its dual form, where one variable `alpha_i` per training point carries the whole solution. The dual objective to maximize is `W(alpha) = sum(alpha) - 0.5 * sum_ij alpha_i alpha_j y_i y_j K_ij`, with labels `y_i` in `{-1, +1}` and kernel matrix `K`.

Implement two functions.

- `dual_objective(alpha, y, K)`: returns `W(alpha)` as a float. `alpha` and `y` have length `n` and `K` is an `n` by `n` kernel matrix.
- `is_dual_feasible(alpha, y, C, tol=1e-9)`: returns `True` when every `alpha_i` lies in `[0, C]` (within `tol`) and `sum(alpha_i * y_i)` is zero (within `tol`). Otherwise it returns `False`.

### Constraints

- `alpha` and `y` must have length `n`, and `K` must be `n` by `n`. Otherwise raise `ValueError`.
- `C < 0` raises `ValueError`.
- Do not modify the inputs.

### Hints

<details>
<summary>Hint 1</summary>

With `ay = alpha * y`, the quadratic term is `ay @ K @ ay`.

</details>
