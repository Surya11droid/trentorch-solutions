# Row & Columnar Storage

Intermediate | databases | storage

### The problem, from first principles

A table is a grid, and a disk holds a line of bytes, so somebody has to decide how to lay the grid out along the line. **Row storage** writes one whole record after another, which is ideal for fetching or changing a single customer. **Columnar storage** writes all of one column, then all of the next, which is ideal for analytics: the average of one column over a hundred million rows touches only that column, and a column of similar values also compresses far better than a mix of types. The choice shapes the speed of every query, and almost every analytics engine and every dataframe library is columnar. This question builds both layouts, a simple compression that columns make possible and a cost model that shows why the choice matters.

### From theory to code

Implement `rows_to_columns(rows)` and `columns_to_rows(columns)`, which convert between the two layouts, then `run_length_encode(values)` and `run_length_decode(pairs)`, a compression that exploits repeated values, then `bytes_scanned(layout, num_rows, num_columns, columns_needed, value_bytes)`, the amount of data a query reads in each layout. The signatures and docstrings are already in the editor.

### Constraints

- A **row table** is a list of dicts that all have the same keys in the same order. A **column table** is a dict mapping each column name to the list of that column's values, in row order, with columns in the same order as the keys of the rows.
- `rows_to_columns(rows)` returns the column table. For an empty list of rows it returns `{}`. `columns_to_rows(columns)` returns the list of row dicts, with keys in the order of `columns`. An empty column table gives `[]`. Converting there and back must return the original rows.
- `run_length_encode(values)` returns a list of `(value, count)` pairs, one per **run** of equal consecutive values, in order. `run_length_decode(pairs)` returns the original list. An empty list encodes to `[]`.
- `bytes_scanned(layout, num_rows, num_columns, columns_needed, value_bytes)` returns an int. For `layout == "row"` a query must read every value of every row: `num_rows * num_columns * value_bytes`. For `layout == "column"` it reads only the needed columns: `num_rows * columns_needed * value_bytes`. Any other layout raises `ValueError`.
- Inputs must not be modified.

### Hints

<details>
<summary>Hint 1</summary>

Going from rows to columns is a transpose. For each column name collect that key from every row, in order.

</details>

<details>
<summary>Hint 2</summary>

A run is a maximal stretch of equal neighbours, so a new run starts exactly when a value differs from the one before it.

</details>

<details>
<summary>Hint 3</summary>

A row store has no way to read one column without also reading the rest of the record, because the values of a row sit next to each other on disk.

</details>
