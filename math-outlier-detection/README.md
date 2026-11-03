# Outlier Detection

Beginner | data-processing

### The problem, from first principles

`02-imputing-missing-values` assumed missing values are cleanly flagged as `NaN`, easy. Bad data is rarely that considerate: a sensor briefly malfunctions and reports a temperature of 9999, a data-entry error turns "$50,000" into "$50,000,000", nothing marks these as wrong, they're just numbers sitting in the dataset, quietly distorting every mean, variance and gradient that touches them. Before you can trust a model built on real data, you need a systematic way to flag "this number looks implausible," not just eyeball a scatter plot and hope.

Two standard, complementary tools do this: the IQR method (based on percentiles, robust to extreme values) and the z-score method (based on standard deviations, but with a real weakness this question makes visible). Understanding both, and where each one fails, is a genuinely practical skill for any real dataset.

### From theory to code

Theory gives both detection rules directly: IQR flags anything outside a fixed multiple of the interquartile range beyond Q1/Q3, z-score flags anything more than a fixed number of standard deviations from the mean.

Implement `detect_outliers_iqr(x, k=1.5)` and `detect_outliers_zscore(x, threshold=3.0)` against that reasoning. The signatures and docstrings are already in the editor.

### Constraints

- Both functions return a boolean mask, same shape as `x`, `True` where a value is flagged.
- `detect_outliers_iqr` uses `np.percentile` for Q1 (25th) and Q3 (75th).
- `detect_outliers_zscore` uses the population std (`np.std`'s default `ddof=0`).

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`np.percentile(x, 25)` and `np.percentile(x, 75)` give Q1 and Q3 directly, `IQR = Q3 - Q1`.

</details>

<details>
<summary>Hint 2</summary>

Both functions boil down to one comparison against two computed bounds (IQR) or one computed statistic (z-score), `|value| > threshold`-style logic.

</details>
