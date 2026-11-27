# Nearest centroid classifier

Beginner | classical-ml | instance-based

### The problem, from first principles

`01-knn` predicts by comparing a query against _every_ training point, accurate, but the prediction cost grows with the size of the training set. Nearest centroid asks whether that's really necessary: if a class's points cluster together, a single summary point per class (its centroid) might capture "what this class looks like" well enough to skip comparing against every individual training example.

### From theory to code

Implement `nearest_centroid_fit(input, labels)`, which returns one centroid per class, and `nearest_centroid_predict(model, queries)`, which assigns each query to its nearest centroid's class. Reuse `01-knn`'s `pairwise_distances`, don't recompute distances by hand.

### Constraints

- `nearest_centroid_fit` returns `{"classes": ..., "centroids": array (n_classes, n_features)}`, one centroid row per distinct class, in the same order as `classes`.
- A centroid is the mean feature vector of that class's own training rows.
- `nearest_centroid_predict` returns one predicted class per row of `queries`, the class of the nearest centroid (Euclidean distance).
- Ties broken toward the lower class label (whichever `np.argmin` returns first).

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

A list comprehension over `np.unique(labels)`, each computing `input[labels == c].mean(axis=0)`, stacked with `np.array(...)`, is the whole fit step.

</details>

<details>
<summary>Hint 2</summary>

`pairwise_distances` doesn't care whether its first argument is "real" training points or centroids, pass the fitted centroids in as if they were the training set, and it returns `(n_queries, n_classes)` distances directly.

</details>
