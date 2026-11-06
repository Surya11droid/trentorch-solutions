# Class Imbalance

Intermediate | data-science | classification

### The problem, from first principles

`01-stratified-sampling` keeps the class mix when sampling an imbalanced dataset. Keeping the mix does not make the imbalance go away, and the imbalance is the problem. In fraud detection or disease screening, 99% of rows are one class, so a model that always predicts the majority class scores 99% accuracy and finds nothing. The standard remedies change what the model sees: weight the rare class more heavily in the loss, copy rare rows until the classes balance, throw away common rows, or invent new rare rows that lie between existing ones. This question builds all four.

### From theory to code

Implement `class_weights(y)`, which gives each class a loss weight inversely proportional to its frequency, then `random_oversample(X, y, rng)`, which duplicates minority rows, then `random_undersample(X, y, rng)`, which drops majority rows, then `interpolate_minority(minority, n_new, rng)`, which creates synthetic minority points between real ones. The signatures and docstrings are already in the editor.

### Constraints

- `X` is a 2D float array `(rows, features)` and `y` is a 1D array of class labels with one entry per row. `rng` is a `numpy.random.Generator`.
- `class_weights` returns a dict mapping each label to `n_samples / (n_classes * count_of_that_class)`. The weights of the classes, multiplied by their counts, all sum to the same total, so every class carries equal total weight.
- `random_oversample` returns new `(X_resampled, y_resampled)` arrays that keep every original row first, in order, then append extra rows for each class below the largest class count. For each such class in sorted label order, draw `needed = max_count - count` row indices with `rng.choice(rows_of_that_class, size=needed, replace=True)` and append those rows. Every class ends with `max_count` rows.
- `random_undersample` returns new `(X_resampled, y_resampled)` where every class is cut to the smallest class count. For each class in sorted label order, keep `rng.choice(rows_of_that_class, size=min_count, replace=False)` indices. The result lists the kept rows class by class in sorted label order, each class's rows sorted by original index.
- `interpolate_minority` takes a 2D array of minority-class points and returns an array of shape `(n_new, features)`. For each new point, in order, draw two distinct points `a` and `b` with `rng.choice(len(minority), size=2, replace=False)` and a weight `u = rng.random()` and return `a + u * (b - a)`. It needs at least 2 minority points.
- Inputs must not be modified.

### Hints

<details>
<summary>Hint 1</summary>

Balanced weights make a class's weight times its count the same for every class, which is what "each class matters equally" means for a weighted loss.

</details>

<details>
<summary>Hint 2</summary>

Oversampling creates rows that are exact copies, so evaluating on a split made after oversampling would score the model on rows it already saw. Resample the training set only, after splitting.

</details>

<details>
<summary>Hint 3</summary>

A point on the line segment between two real minority points is a convex combination, so it always lies inside the region the minority class already occupies.

</details>
