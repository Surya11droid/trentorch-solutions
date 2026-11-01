# Histograms with hist, Density & Overlays

Intermediate | data-science | visualization | matplotlib | histogram

### The problem, from first principles

`ax.hist` is a one-line call that hides three decisions: how the range is cut into bins, whether the bar heights are _counts_ or a _density_, and, when two histograms share a plot, whether they use the **same bins**. Skip the last one and the comparison is meaningless: two samples drawn with different bin edges can look different purely because of where the cuts fell.

Because `hist` also returns the numbers it drew (the counts and the edges), the chart can be checked against `np.histogram` exactly. This question draws a histogram and reads its numbers back, draws a density histogram whose bars have total area 1, and overlays two samples on a shared set of bins so the comparison is fair.

### From theory to code

Implement `draw_histogram(data, bins)`, `density_histogram(data, bins)` and `overlay_histograms(a, b, bins, labels)`. The signatures and docstrings are already in the editor.

### Constraints

- `data`, `a`, `b` are 1D sequences of at least two numbers with at least two distinct values. `bins` is an integer number of bins.
- `draw_histogram(data, bins)` draws on a new `Axes` with `ax.hist` and returns `(fig, ax, counts, edges)` where `counts` and `edges` are the arrays returned by `hist`. There are `bins` bars.
- `density_histogram(data, bins)` returns `(fig, ax)` of a histogram whose bar heights are a **density** (the total area of the bars is 1) and whose y label is `"density"`.
- `overlay_histograms(a, b, bins, labels)` draws both samples on **one** `Axes` using the **same bin edges**, computed from the combined data with `np.histogram_bin_edges(np.concatenate([a, b]), bins=bins)`, each with `alpha=0.5` and its label from `labels` (a pair), shows a legend, and returns `(fig, ax, edges)`.
- Do not call `plt.show()`.

### Hints

<details>
<summary>Hint 1</summary>

`ax.hist(data, bins=...)` returns `(counts, edges, patches)`.

</details>

<details>
<summary>Hint 2</summary>

`density=True` rescales the heights so that `sum(height * width) == 1`.

</details>

<details>
<summary>Hint 3</summary>

Passing the _edges array_ as `bins` makes both histograms use exactly those cuts.

</details>
