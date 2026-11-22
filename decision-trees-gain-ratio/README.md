# Gain ratio for a categorical feature

Intermediate | classical-ml | decision-trees | splitting-criteria

### The problem, from first principles

Information gain has a flaw: a feature with many distinct values (an ID column, say) splits the data into tiny, perfectly pure groups and looks wonderful, while telling you nothing about unseen samples. Gain ratio divides the gain by how finely the feature splits the data, so many-valued features are penalised.

### From theory to code

Implement `gain_ratio(feature, labels)`. Split `labels` into one group per distinct value of `feature`, compute the information gain of that split, then divide by the split's intrinsic value. Use base-2 logarithms throughout.

### Constraints

- `feature` and `labels` are one-dimensional arrays of equal length; either can hold arbitrary integers.
- Return a Python `float`.
- Return `0.0` for empty input, and `0.0` when the feature has a single distinct value (its intrinsic value is zero).
- Use base-2 logs, so entropy is measured in bits.

### Hints

Open one at a time. Each gives away a little more than the last.

<details><summary>Hint 1</summary>

Entropy is `-sum(p * log2(p))` over class proportions. Information gain is the parent entropy minus the size-weighted entropy of the child groups.

</details>

<details><summary>Hint 2</summary>

The intrinsic value is the entropy of the _group sizes_ themselves: `-sum(w * log2(w))`, where `w` is each group's share of the samples.

</details>
