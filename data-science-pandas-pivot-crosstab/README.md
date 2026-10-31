# Pivot Tables, Crosstabs & Reshaping

Intermediate | data-science | pandas | pivot | reshape

### The problem, from first principles

A table of one row per sale is the right shape for storing data and the wrong shape for reading it. A manager wants regions down the side and quarters across the top, with the revenue where they cross. That rearrangement is a **pivot**, and its mirror image, taking such a grid and turning it back into one row per measurement, is a **melt**. Between them they let data move between the _long_ form that analysis tools like and the _wide_ form that people read.

This question builds the four reshapes that come up most: a pivot that sums a measure and fills empty cells, a grid with totals, a count table of two categorical columns (a crosstab) and the row-percentage version of it, and the melt back to long form.

### From theory to code

Implement `revenue_pivot(df)`, `add_totals(grid)`, `count_table(df, row, col)`, `row_percentages(table)` and `to_long(wide, id_col, var_name, value_name)`. The signatures and docstrings are already in the editor.

### Constraints

- `revenue_pivot(df)` takes a frame with columns `region`, `quarter`, `revenue` (one or more rows per region and quarter) and returns a grid with the regions as the index and the quarters as the columns, each cell the **sum** of `revenue` for that pair, `0` where there are no rows. Both axes are sorted ascending.
- `add_totals(grid)` returns a **new** grid with one extra row labelled `"Total"` (column sums) at the bottom and one extra column labelled `"Total"` (row sums) at the right, including the grand total in the corner. The input is not changed.
- `count_table(df, row, col)` returns the number of rows for every pair of values of the columns `row` and `col`: distinct values of `row` down the side, of `col` across the top, both sorted ascending, `0` where a pair never occurs.
- `row_percentages(table)` returns the table with every cell turned into the percentage of its **row** total (each row sums to 100). Rows whose total is zero become `NaN`.
- `to_long(wide, id_col, var_name, value_name)` melts every column other than `id_col` into rows: the result has the columns `id_col`, `var_name`, `value_name`, ordered by `id_col` in the original row order and, within one id, by the original column order. Fresh `0..n-1` index.

### Hints

<details>
<summary>Hint 1</summary>

`pivot_table` aggregates duplicate cells (the default is the mean, so say `aggfunc`) and takes `fill_value`.

</details>

<details>
<summary>Hint 2</summary>

`pd.crosstab(a, b)` counts pairs and sorts both axes. Dividing a table by its row sums with `div(..., axis=0)` divides each row by its own total.

</details>

<details>
<summary>Hint 3</summary>

`melt` stacks one block of rows per column, so every id repeats once per column. A stable sort by the id column puts each id's rows together without reordering its columns.

</details>
