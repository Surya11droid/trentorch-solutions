# Distributions: histplot, kdeplot & ecdfplot

Intermediate | data-science | visualization | seaborn | distributions

### The problem, from first principles

Seaborn is matplotlib with the statistics built in. You hand it a table and the names of columns, and it does the grouping, binning and smoothing before drawing. For one numeric column it offers three views of the same distribution: a **histogram** (counts in bins), a **kernel density estimate** (a smooth curve that integrates to 1) and an **empirical CDF** (the fraction of values at or below each point, with no binning at all).

Each is a function that draws on an `Axes` and returns it, so everything it drew can be read back: the bar heights, the curve, the labels. The details of what _scale_ each one uses (counts, density or proportion) is exactly the sort of thing that changes a picture's meaning, so this question builds all three, plus a comparison of one distribution per group on a fair, per-group scale.

### From theory to code

Implement `histogram_axes(df, column, bins, stat)`, `kde_axes(df, column)`, `kde_by_group(df, column, group, order)` and `ecdf_axes(df, column)`. The signatures and docstrings are already in the editor.

### Constraints

- Draw with seaborn (`import seaborn as sns`), passing `data=df` and the column names, and **return the `Axes`** the call returns. Do not call `plt.show()`.
- `histogram_axes(df, column, bins, stat)` draws a histogram of `column` with `bins` bins and the statistic `stat` (`"count"`, `"density"` or `"probability"`).
- `kde_axes(df, column)` draws one kernel density curve of `column`.
- `kde_by_group(df, column, group, order)` draws one density curve per value of `group`, in the colour order given by `order` (a list of the group values), **each curve normalised on its own** (so every curve integrates to 1 whatever the group size).
- `ecdf_axes(df, column)` draws the empirical cumulative distribution function of `column`.

### Hints

<details>
<summary>Hint 1</summary>

`sns.histplot`, `sns.kdeplot` and `sns.ecdfplot` all take `data=` and `x=`. `histplot` has `bins` and `stat`.

</details>

<details>
<summary>Hint 2</summary>

`hue=` splits a plot by a column, `hue_order=` fixes which value gets which colour, and `common_norm=False` normalises each hue level separately.

</details>

<details>
<summary>Hint 3</summary>

Each call returns the `Axes` it drew on.

</details>
