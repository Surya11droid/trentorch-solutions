# Feature Engineering

Intermediate | data-processing

### The problem, from first principles

Imagine labeling points as "inside" or "outside" a circle of radius 3, based only on their `(x, y)` coordinates. Individually, `x` alone tells you almost nothing about the label (a point at `x=2` could be inside the circle or far outside it, depending on `y`), and the same goes for `y` alone, `04-data-leakage`'s own correlation check would find both features nearly USELESS on their own, even though the label is entirely determined by `x` and `y` together. A linear model, in particular, genuinely cannot represent "inside a circle" as a straight-line decision boundary in raw `(x, y)` space, no matter how it's trained, the true boundary is curved.

But compute ONE new number, `sqrt(x^2 + y^2)` (distance from the origin), and the exact same problem becomes trivial: "inside the circle" is now just "this single number is less than 3," a problem any linear model handles instantly. That's feature engineering: deriving a new feature from existing ones specifically because it captures the actual structure of the problem in a form the model can use directly, rather than hoping the model discovers that structure on its own from raw, poorly-shaped inputs.

### From theory to code

Theory gives two concrete, common engineered features: distance from the origin (`sqrt(x^2 + y^2)`, useful whenever "how far from center" matters more than raw coordinates) and a ratio between two raw features (useful whenever the RELATIONSHIP between two quantities matters more than either alone).

Implement `radius_feature(x, y)` and `ratio_feature(numerator, denominator)` against that reasoning. The signatures and docstrings are already in the editor.

### Constraints

- Both functions are vectorized: they accept arrays and return arrays of the same shape.
- `radius_feature` always returns non-negative values.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`radius_feature` is a direct translation of the Euclidean distance formula, `sqrt(x^2 + y^2)`.

</details>

<details>
<summary>Hint 2</summary>

`ratio_feature` is a single division, no special handling needed for this question (a real pipeline would guard against `denominator == 0` separately).

</details>
