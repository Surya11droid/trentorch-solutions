# Random Forest regression, and out-of-bag error estimation

Intermediate | classical-ml | ensembles | random-forest | regression

### The problem, from first principles

Bootstrap training leaves some rows out of every tree. For regression, tree outputs are averaged rather than voted, and the trees that omitted a row form a free, honest evaluation set for that row. This exercise records those omitted indices and uses only them for out-of-bag error.

### From theory to code

Implement bootstrap sampling with omitted indices, train a forest of `(tree, oob_indices)` pairs, average all tree predictions, and calculate OOB mean squared error.

### Constraints

- Bootstrap arrays have the original shapes and share one replacement-drawn index array.
- `oob_indices` contains original positions never drawn in that tree's bag.
- Train exactly `n_trees` with one advancing seeded generator.
- Regression forest prediction averages across trees along axis 0.
- OOB error uses only a sample's own OOB trees; samples with zero OOB predictions are excluded.
- Return OOB error as a Python float.

### Hints

Open one at a time. Each gives away a little more than the last.

<details><summary>Hint 1</summary>

Mark every replacement-drawn index in a Boolean `in_bag` array; its inverse identifies omitted positions.

</details>

<details><summary>Hint 2</summary>

Keep one running OOB prediction sum and count per original row, then divide only where the count is positive.

</details>
