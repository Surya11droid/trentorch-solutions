# Oblique split gain

Advanced | classical-ml | decision-trees | oblique-splits | gini

### Score a split along a slanted direction

An axis-aligned tree asks one question per node: is feature `j` at most `t`? An oblique tree asks about a linear combination instead: is `w . x + b <= 0`? That lets one node cut a diagonal boundary that would otherwise need a staircase of splits.

Implement `oblique_split_gain(X, y, w, b)` that scores this split with Gini impurity.

- `X` is an `n` by `d` float matrix, `y` holds integer labels of length `n`, `w` has length `d`, and `b` is a scalar.
- Left branch: rows where `X @ w + b <= 0`. Right branch: the rest.
- Return `G(parent) - (n_left / n) G(left) - (n_right / n) G(right)`, where `G = 1 - sum_c p_c^2`.

### Constraints

- `X` must be 2-D, `w` must have length `d`, and `y` must have length `n`. Otherwise raise `ValueError`.
- `w` must not be the zero vector. Raise `ValueError` in that case, because the direction is undefined.
- An empty child contributes zero impurity.
- Do not modify the inputs.

### Hints

<details>
<summary>Hint 1</summary>

Scaling `w` and `b` by the same positive number does not change which side a row lands on, so the gain must be unchanged.

</details>
