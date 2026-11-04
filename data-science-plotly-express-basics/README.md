# Plotly Express: Scatter, Bar, Line & Histogram

Beginner | data-science | visualization | plotly | express

### The problem, from first principles

Building a figure trace by trace is flexible and wordy. **Plotly Express** (`px`) is the short way: you give it a DataFrame and column names and it creates the traces, the axis titles, the legend and a sensible colour scheme in one call. `px.scatter(df, x="height", y="weight", color="species")` produces one trace _per species_, named, coloured and listed in the legend, because a column mapped to `color` means "split by this".

Because Express builds ordinary plotly figures, everything it produced can be checked: how many traces, what each is called, what numbers each holds. The decisions that matter are the same as in any chart: which order the groups come in, whether to aggregate before drawing, and whether lines are sorted along the x axis. This question builds four Express charts and pins down each of those.

### From theory to code

Implement `scatter_by_group(df, x, y, group, order)`, `total_bars(df, cat, value)`, `histogram_figure(df, column, bins)` and `lines_by_group(df, x, y, group)`. The signatures and docstrings are already in the editor.

### Constraints

- Use `plotly.express` (`import plotly.express as px`). Do not call `fig.show()`.
- `scatter_by_group(df, x, y, group, order)` returns a scatter with **one trace per value** of `group`, the traces in the order given by `order` (a list of the group values), each trace holding that group's points (rows in their original order).
- `total_bars(df, cat, value)` returns a bar chart with **one bar per category**: the **sum** of `value` per category, **largest total first**, ties by category name ascending. Aggregate with pandas first, then draw.
- `histogram_figure(df, column, bins)` returns a histogram of `column` requesting `bins` bins (`nbinsx`).
- `lines_by_group(df, x, y, group)` returns a line chart with **one line per group**, groups in order of their first appearance in `df`, each line's points **sorted by `x` ascending**.

### Hints

<details>
<summary>Hint 1</summary>

Mapping a column to `color=` creates one trace per value. `category_orders={"group": [...]}` fixes their order.

</details>

<details>
<summary>Hint 2</summary>

`px.bar` draws exactly the rows it is given, so group and sort the data first.

</details>

<details>
<summary>Hint 3</summary>

`px.line` joins points in the order of the rows, so sort by `x` within each group before drawing.

</details>
