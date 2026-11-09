# SELF JOIN

Intermediate | db

The `employees` table has a `manager_id` column that points at another row in the same table (the manager's `id`). The top person has `manager_id` NULL.

Write a query returning each employee's `name` as `employee` and their manager's `name` as `manager`. Employees without a manager (the top of the chart) are not listed.

### Constraints

- Columns, in order: `employee`, `manager`
- Join `employees` to itself
- Employees with no manager are excluded

### Hints

<details>
<summary>Hint 1</summary>

Use the table twice with two different aliases, e.g. `employees e` and `employees m`.

</details>

<details>
<summary>Hint 2</summary>

Match `e.manager_id` to `m.id`.

</details>
