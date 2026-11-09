# String CONCAT

Intermediate | db

The profile page shows each user's full name in one column: first name, a space, then last name. Some people have only one name (the `last_name` column is NULL) and must show just their first name, with no trailing space and not a blank value.

Write a query returning one column, `full_name`.

### Constraints

- One column named `full_name`
- `first_name` + space + `last_name`
- If `last_name` is NULL, return only `first_name`

### Hints

<details>
<summary>Hint 1</summary>

SQL's concatenation operator is `||`; SQLite (3.39) has no `CONCAT()` function.

</details>

<details>
<summary>Hint 2</summary>

Concatenating with NULL gives NULL; `COALESCE(x, '')` swaps NULL for an empty string.

</details>
