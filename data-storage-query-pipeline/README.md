# Query Execution Pipeline

Advanced | databases | query-execution

### The problem, from first principles

A SQL query such as `SELECT name FROM users WHERE age > 30 ORDER BY name LIMIT 10` looks like one command and runs as a pipeline of small steps: scan the table, keep the rows that pass the filter, pick the columns, sort, stop after ten. Each step takes a stream of rows in and hands a stream of rows out, and connecting them lets a database answer a query on a billion rows while holding only a few in memory. The key idea is **laziness**: a step does no work until the step after it asks for a row, so `LIMIT 10` reads only as much of the table as it needs. This question builds the operators as Python generators and composes them into a query.

### From theory to code

Implement the operators `scan(table)`, `filter_rows(rows, predicate)`, `project(rows, columns)`, `order_by(rows, column, descending)` and `limit(rows, n)`, each taking and returning an iterable of row dicts, then `run_query(table, where, columns, order_column, descending, row_limit)`, which chains them. The signatures and docstrings are already in the editor.

### Constraints

- A row is a dict. `scan`, `filter_rows`, `project` and `limit` must be **generators** (they use `yield`) that pull rows from their input one at a time. They must not build the full list of rows.
- `scan(table)` yields the rows of a list in order. `filter_rows(rows, predicate)` yields only the rows for which `predicate(row)` is true. `project(rows, columns)` yields a new dict per row holding only the listed columns, in the order listed.
- `limit(rows, n)` yields at most `n` rows and stops **without pulling any more rows from its input** once it has yielded `n` (for `n <= 0` it pulls none).
- `order_by(rows, column, descending=False)` is a **blocking** operator: it must read all input before yielding anything. It yields the rows sorted by `row[column]`, with `descending=True` reversing the order. The sort is stable, so rows with equal keys keep their input order, in descending order as well. Rows whose value is `None` sort last in both directions.
- `run_query(table, where, columns, order_column, descending, row_limit)` returns a **list**. The steps run in the order scan, filter (if `where` is not `None`), sort (if `order_column` is not `None`), limit (if `row_limit` is not `None`), project (if `columns` is not `None`). Sorting and limiting happen **before** projection, so the sort column need not be among the projected columns.
- Input rows and the table must not be modified.

### Hints

<details>
<summary>Hint 1</summary>

A generator function runs only when something asks it for the next value. Writing `for row in rows: if predicate(row): yield row` is a complete lazy filter.

</details>

<details>
<summary>Hint 2</summary>

Sorting cannot be lazy, since the first output row may be the last input row. That is why `LIMIT` after a sort still reads everything, but `LIMIT` with no sort reads only `n` rows.

</details>

<details>
<summary>Hint 3</summary>

For descending order with stability, sort by a key that places `None` last, then reverse only the non-null block's key order using `reverse=True`, which preserves the order of equal elements.

</details>
