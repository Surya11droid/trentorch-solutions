# Ordinal & Target Encoding

Intermediate | data-science | encoding

### The problem, from first principles

`01-one-hot-encoding` turns a category into one column per value, which works until a column has thousands of values (a zip code, a product ID) and the table explodes. Two other encodings keep a single column. **Ordinal encoding** replaces each category by its rank when the categories have a natural order (small, medium, large). **Target encoding** replaces each category by the average of the label over the rows that have it, which packs the category's predictive signal into one number. Target encoding is also one of the easiest ways to leak the label into a feature by accident, so this question builds the safe versions.

### From theory to code

Implement `ordinal_encode(values, order)` for ordered categories, then `target_encode(categories, y, smoothing)`, which learns a smoothed mean per category, then `apply_target_encoding(categories, mapping, default)`, which uses a learned mapping, then `out_of_fold_target_encode(categories, y, n_folds, smoothing)`, which encodes every row using only rows from other folds. The signatures and docstrings are already in the editor.

### Constraints

- `values` and `categories` are 1D arrays of hashable labels. `y` is a 1D float array of the same length. `order` is a list of labels from lowest to highest.
- `ordinal_encode` returns an integer array where each value is the position of its label in `order`. A label that is not in `order` becomes `-1`.
- `target_encode` returns a dict mapping each category to `(n * category_mean + smoothing * global_mean) / (n + smoothing)`, where `n` is how many rows have that category and `global_mean` is the mean of all of `y`. With `smoothing = 0` this is the plain category mean.
- `apply_target_encoding` returns a float array with one value per entry of `categories`. A category missing from `mapping` gets `default`.
- `out_of_fold_target_encode` splits the row indices `0 .. n-1` into `n_folds` contiguous, nearly equal blocks with `np.array_split`, in order, with no shuffling. For each block it learns the mapping from all other rows with `target_encode` and applies it to the block, using the global mean of the other rows as `default`. It returns a float array of length `n`.

### Hints

<details>
<summary>Hint 1</summary>

The smoothing formula is a weighted average of two numbers: what this category's own rows say, and what the whole dataset says. A rare category has small `n`, so the global mean dominates, which stops one lucky row from setting a category's value.

</details>

<details>
<summary>Hint 2</summary>

A target encoding computed on all the rows includes each row's own label in the number that is then fed back as its feature. Computing it only from other folds removes that.

</details>

<details>
<summary>Hint 3</summary>

For the fold loop, build a boolean mask for the held-out block and call `target_encode` on the complement.

</details>
