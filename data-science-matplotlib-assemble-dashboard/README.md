# Assemble: A Small Sales Dashboard

Intermediate | data-science | visualization | matplotlib | assemble

### The problem, from first principles

A dashboard is several charts answering several questions about the same data, on one figure, with one consistent look. The pieces are all things you have built: a time series, a ranked bar chart, a histogram. The work is in the joining: aggregating the data _for_ each panel (the line wants monthly totals, the bars want per-region totals, the histogram wants the raw order values), labelling every axis so each panel stands alone, and putting a title over the whole figure.

This question builds a three-panel sales dashboard from one table of orders, and because every panel is built from matplotlib objects you can check each one against the aggregation it should show.

### From theory to code

Implement `sales_dashboard(df)`. The signature and docstring are already in the editor.

### Constraints

- `df` has the columns `date` (datetime), `region` (text) and `amount` (number), with at least one row.
- Return `fig`, a figure with **exactly three** Axes in one row (`plt.subplots(1, 3)`), in this order: **revenue by month**, **revenue by region**, **order amounts**.
- Panel 1 is a line of the total `amount` per calendar month, in chronological order, with the title `"Revenue by month"`, x label `"Month"` and y label `"Revenue"`.
- Panel 2 is a bar chart of the total `amount` per region, **largest total first** (ties by region name ascending), bars centred at `0..n-1` with the region names as tick labels, title `"Revenue by region"`, x label `"Region"`, y label `"Revenue"`.
- Panel 3 is a histogram of the raw `amount` values with **5 bins**, title `"Order amounts"`, x label `"Amount"`, y label `"Orders"`.
- The figure has the overall title (`suptitle`) `"Sales dashboard"`. Do not call `plt.show()`.

### Hints

<details>
<summary>Hint 1</summary>

Aggregate with pandas first (`groupby`), then draw. `df["date"].dt.to_period("M")` gives a calendar month to group by.

</details>

<details>
<summary>Hint 2</summary>

Draw each panel on its own Axes from the array that `plt.subplots(1, 3)` returns.

</details>

<details>
<summary>Hint 3</summary>

Sort the region totals with `sort_values(ascending=False, kind="mergesort")` after sorting by name, so ties come out in name order.

</details>
