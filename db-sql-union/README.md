# UNION Combining Queries

Intermediate | db

Active users live in `users`; people who closed their account were moved to `archive_users` (same columns). Cara exists in both tables because she was copied rather than moved.

Write a query returning `id`, `name` and `email` of everyone from either table, with exact duplicate rows listed only once.

### Constraints

- Columns, in order: `id`, `name`, `email`
- Combine both tables into one result
- A row present in both tables appears once

### Hints

<details>
<summary>Hint 1</summary>

`UNION` stacks the results of two `SELECT`s.

</details>

<details>
<summary>Hint 2</summary>

Both `SELECT`s must return the same number of columns, in compatible types.

</details>
