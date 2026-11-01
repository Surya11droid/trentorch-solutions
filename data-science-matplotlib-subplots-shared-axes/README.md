# Subplots, Shared Axes & Twin Axes

Intermediate | data-science | visualization | matplotlib | subplots

### The problem, from first principles

One chart answers one question. A set of **small multiples**, the same chart repeated once per group, answers "does the pattern hold in every group?", and it only works if the panels use the **same scales**. Panels with their own free axes look similar when the data are wildly different, and different when the data are almost the same. Sharing the axes is what makes the eye's comparison valid.

A second, related tool is the **twin axis**: two quantities with different units (revenue in euros and a conversion rate in percent) drawn against one x axis, each with its own y scale on opposite sides. It is easy to misuse, so the colour of each axis label should match its line.

This question builds a grid of panels with shared axes (and hides the panels left over), a twin-axis chart, and a helper that sets limits, ticks and scale in one place.

### From theory to code

Implement `small_multiples(series, ncols)`, `twin_axis_chart(x, y_left, y_right, left_label, right_label)` and `set_limits_and_ticks(ax, xlim, ylim, xticks, xticklabels, logy)`. The signatures and docstrings are already in the editor.

### Constraints

- `small_multiples(series, ncols)` takes a dict mapping a panel title to an `(x, y)` pair, and returns `(fig, axes)`, where `axes` is a 2D NumPy array of shape `(nrows, ncols)` with `nrows = ceil(len(series) / ncols)`. Panel `i` (row-major order) draws its line and gets its key as its title. **All panels share both the x and the y axis.** Unused panels are made invisible (`set_visible(False)`).
- `twin_axis_chart` returns `(fig, ax_left, ax_right)`. The left axes plots `y_left` in `"tab:blue"`, the right axes (made with `twinx`, so it shares the x axis) plots `y_right` in `"tab:red"`. Each y label is set from its argument and coloured like its line. The x axis is shared.
- `set_limits_and_ticks(ax, xlim, ylim, xticks, xticklabels, logy)` sets the x and y limits, puts the x ticks at `xticks` with the text `xticklabels`, and switches the y axis to a logarithmic scale if `logy` is true (otherwise linear).
- Do not call `plt.show()`.

### Hints

<details>
<summary>Hint 1</summary>

`plt.subplots(nrows, ncols, sharex=True, sharey=True, squeeze=False)` always returns a 2D array of axes, even for one row.

</details>

<details>
<summary>Hint 2</summary>

`ax.twinx()` returns a second Axes on top of the first that shares its x axis and has its own y axis on the right.

</details>

<details>
<summary>Hint 3</summary>

Set the tick _positions_ first (`set_xticks`), then their _text_ (`set_xticklabels`).

</details>
