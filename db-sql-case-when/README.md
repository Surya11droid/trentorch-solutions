# CASE WHEN

Intermediate | db

The reporting layer groups users into age bands: `minor` (under 18), `adult` (18 to 64) and `senior` (65 and over).

Write a query returning each user's `name` and their band as `age_group`.

### Constraints

- Columns, in order: `name`, `age_group`
- Values are exactly `minor`, `adult`, `senior` (lowercase)
- 17 is a minor, 18 an adult, 64 an adult, 65 a senior

### Hints

<details>
<summary>Hint 1</summary>

`CASE WHEN condition THEN value ... ELSE value END` is SQL's if/else.

</details>

<details>
<summary>Hint 2</summary>

Branches are checked top to bottom; the first true one wins.

</details>
