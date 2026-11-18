# Elastic Net: combining L1 and L2 penalties

Intermediate | classical-ml | regression

### The problem, from first principles

`Ridge Regression (L2)` and `Lasso Regression (L1), contrasted against Ridge` each have a real, distinct weakness. Ridge never zeroes out irrelevant features, its shrinkage is smooth but never total. Lasso, when several features are strongly correlated with each other, tends to arbitrarily pick just ONE of them and zero out the rest, even when several of them are genuinely, similarly useful, an unstable, somewhat arbitrary selection that can change dramatically with tiny changes to the data.

Elastic Net asks: why not use both penalties at once, and let a tunable knob control the mix? The result inherits Lasso's genuine sparsity (some weights really do land at exactly zero) while inheriting Ridge's stability when features are correlated (it tends to keep or drop CORRELATED features together, rather than arbitrarily favoring one over the others).

### From theory to code

Theory adds Ridge's L2 term directly into Lasso's own coordinate descent update, reusing `Lasso Regression (L1), contrasted against Ridge`'s `soft_threshold` unchanged and its centering/coordinate-cycling structure unchanged, with one modification to the per-coordinate formula.

Implement `elastic_net_coordinate_descent(input, target, alpha=1.0, l1_ratio=0.5, epochs=200)` against that reasoning.

### Constraints

- `l1_ratio` controls the L1/L2 mix: `l1_ratio=1.0` is pure Lasso, `l1_ratio=0.0` is pure Ridge.
- Reuse the imported `soft_threshold` directly, don't reimplement it.
- Center `input`/`target` exactly like Lasso's own coordinate descent does.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

Split `alpha` into two separate penalty strengths: `l1_penalty = alpha * l1_ratio`, `l2_penalty = alpha * (1 - l1_ratio)`.

</details>

<details>
<summary>Hint 2</summary>

The per-coordinate update becomes `soft_threshold(rho_j, l1_penalty) / (z_j + l2_penalty)`, Lasso's own update with `z_j` (the denominator) increased by the L2 penalty.

</details>
