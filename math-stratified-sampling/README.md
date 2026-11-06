# Stratified Sampling

Intermediate | data-processing

### The problem, from first principles

A fraud-detection dataset with 95% legitimate transactions and 5% fraudulent ones has a real trap waiting inside it: draw a plain random sample of 20 rows, and there's a meaningful chance you get ZERO fraud examples at all, purely by bad luck, even though fraud makes up a real, nontrivial fifth of every 100 rows. A model, or an evaluation set, built from that unlucky sample would be blind to the exact class it's supposed to detect.

Stratified sampling fixes this directly: instead of sampling from the whole dataset at once, sample from EACH class separately, in proportion to that class's true share of the data. The result is a smaller sample that still faithfully reflects the original class balance, no matter how rare the minority class is or how unlucky a plain random draw might have been.

### From theory to code

Theory computes each class's true proportion of the full dataset first, then draws from each class separately, sized to match that same proportion, so the resulting sample's class balance mirrors the original.

Implement `class_proportions(labels)` first, then `stratified_sample_indices(labels, sample_size, seed=None)` on top of it.

### Constraints

- `class_proportions` returns a dict, `{label: fraction}`, fractions summing to `1.0`.
- `stratified_sample_indices` samples WITHOUT replacement within each class.
- The returned array holds INDICES into `labels`, not the label values themselves.
- Same `seed` must produce the same sample (reproducibility, `01-sampling-estimating-distribution`'s own convention).

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`np.unique(labels, return_counts=True)` gives you both the distinct labels and how many of each there are, in one call.

</details>

<details>
<summary>Hint 2</summary>

For each class, `round(proportion * sample_size)` gives roughly how many samples to draw from that class specifically, then `rng.choice(class_indices, size=that_count, replace=False)`.

</details>
