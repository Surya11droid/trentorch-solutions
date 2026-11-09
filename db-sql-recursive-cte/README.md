# Recursive CTE: Hierarchical Data

Advanced | db

`employees.manager_id` points to the manager's `id`. Alice (id 1) is at the top of one reporting tree; Gina (id 7) heads a different one.

Write a recursive CTE that returns `id`, `name` and `depth` of everyone below Alice: her direct reports have depth 1, their reports depth 2, and so on. Do not include Alice herself or anyone from Gina's tree.

### Constraints

- Columns, in order: `id`, `name`, `depth`
- Direct reports of id 1 have depth 1; each further level adds 1
- Use `WITH RECURSIVE`

### Hints

<details>
<summary>Hint 1</summary>

A recursive CTE has an anchor query, `UNION ALL`, and a recursive query that joins back to the CTE.

</details>

<details>
<summary>Hint 2</summary>

The anchor is Alice's direct reports; the recursive step finds employees whose `manager_id` is already in the CTE.

</details>
