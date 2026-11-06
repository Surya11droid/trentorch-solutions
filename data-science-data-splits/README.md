# Train, Validation & Test Splits

Intermediate | data-science | evaluation

### The problem, from first principles

`01-stratified-sampling` keeps class proportions when sampling. Before any model is trained there is a more basic question: which rows may it learn from, and which are held back to judge it? A model scored on rows it was trained on looks better than it is, so the data is split into a **training** set to learn from, a **validation** set to tune choices on and a **test** set touched once at the end. Random shuffling is right for independent rows and wrong for anything with a time order, where shuffling lets the model train on the future to predict the past. This question builds the splits for both cases, and the cross-validation variants that reuse limited data.

### From theory to code

Implement `train_val_test_split(n, val_fraction, test_fraction, rng)` for shuffled splits, then `time_ordered_split(n, val_fraction, test_fraction)` for chronological splits, then `k_fold_indices(n, k, rng)` for cross-validation, then `expanding_window_splits(n, n_splits, min_train)` for cross-validation on time-ordered data. The signatures and docstrings are already in the editor.

### Constraints

- `n` is the number of rows, and splits are returned as integer index arrays into `0 .. n-1`. `rng` is a `numpy.random.Generator`.
- `train_val_test_split` shuffles with one `rng.permutation(n)`. The test set has `int(round(test_fraction * n))` indices, the validation set has `int(round(val_fraction * n))`, and the training set has the rest. In the permutation the order is train first, then validation, then test. It returns `(train, val, test)`.
- `time_ordered_split` uses the same sizes but no shuffling: the earliest rows are training, the next block is validation and the latest rows are test, each in increasing order. It returns `(train, val, test)`.
- `k_fold_indices` shuffles with one `rng.permutation(n)` and cuts it into `k` blocks with `np.array_split`. It returns a list of `k` pairs `(train_indices, val_indices)` where `val_indices` is block `i` and `train_indices` is every other block concatenated in block order.
- `expanding_window_splits` returns a list of `n_splits` pairs `(train_indices, val_indices)`. The rows after the first `min_train` rows are cut into `n_splits` contiguous blocks with `np.array_split`. Split `i` validates on block `i` and trains on every row before that block, in increasing order.

### Hints

<details>
<summary>Hint 1</summary>

All three random splits reuse the same trick: permute the row numbers once, then slice the permutation. That guarantees no row lands in two sets.

</details>

<details>
<summary>Hint 2</summary>

In time-ordered data, a row's neighbours in time are correlated. A split that leaves later rows in the training set and earlier rows in the test set lets the model peek at the future.

</details>

<details>
<summary>Hint 3</summary>

For the expanding window, the training set grows with every split because everything before the validation block is already in the past.

</details>
