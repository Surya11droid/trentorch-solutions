# Polynomial features: expanding inputs before a linear model

Intermediate | classical-ml | regression

### The problem, from first principles

`linear` (this curriculum's very first question) can only ever compute weighted SUMS of its inputs, it fundamentally cannot represent a curve, no matter how it's trained. `Feature engineering: deriving a feature that makes the model's job easier` (Math & Statistics) already showed one fix: hand-derive a specific nonlinear feature (`radius_feature`) when you know exactly what shape the data needs. Polynomial feature expansion generalizes that idea into something systematic, instead of hand-picking one clever feature, generate EVERY power and cross-product of your existing features up to some degree, and let a plain linear model choose which of those (now numerous) features actually matter.

`07-evaluation/03-bias-variance-tradeoff`'s own `polynomial_features` already did this for a SINGLE input variable. This question generalizes it to MULTIPLE features at once, which introduces a genuinely new kind of term that a single-variable expansion never needs: INTERACTION terms, products of two DIFFERENT features (`x0 * x1`), not just powers of one feature alone (`x0^2`).

### From theory to code

Theory enumerates every monomial (a product of input features raised to some powers) of total degree `0` through `degree`, using `itertools.combinations_with_replacement` over feature indices, the systematic way to generate "every way to multiply some number of features together, repeats allowed, order doesn't matter."

Implement `polynomial_features_multivariate(X, degree)` against that reasoning. The signature and docstring are already in the editor.

### Constraints

- `X` is `(n, num_features)`, any number of features, not just one.
- Output columns must be ordered by degree first (`0`, then `1`, then `2`, ...), then by `combinations_with_replacement` order within each degree, matching `sklearn.preprocessing.PolynomialFeatures`' own column ordering exactly.
- Degree `0` always produces exactly one column, all `1`s (the bias/intercept term).

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

For each degree `d` from `0` to `degree`, loop over `combinations_with_replacement(range(num_features), d)`, each combination is a tuple of feature indices (possibly repeated) to multiply together.

</details>

<details>
<summary>Hint 2</summary>

For a combination like `(0, 0, 1)`, the resulting column is `X[:, 0] * X[:, 0] * X[:, 1]`, start from a column of ones and multiply in each feature named in the combination.

</details>
