# Epsilon-insensitive loss

Beginner | classic-ml

### The problem, from first principles

`Hinge loss` lets a classifier ignore any point that is comfortably on the right side of the margin. Regression needs the same idea with a different shape: a prediction that lands within `epsilon` of the true value should cost nothing, and a prediction outside that tube should be charged only for the distance beyond its edge. This is the epsilon-insensitive loss, the loss behind Support Vector Regression.

Given predictions and targets of the same shape, return `max(0, |prediction - target| - epsilon)` for each pair, then reduce it.

### Constraints

- `reduction` is `"mean"` (default), `"sum"`, or `"none"`. Any other value raises `ValueError`.
- `epsilon` defaults to `0.1`.
- A residual exactly equal to `epsilon` costs `0`.
- Do not modify the inputs.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

Compute the absolute residual first, subtract `epsilon`, then clip at zero with `np.maximum`.

</details>

<details>
<summary>Hint 2</summary>

With `epsilon = 0` this loss is exactly the mean absolute error, which is a useful check.

</details>
