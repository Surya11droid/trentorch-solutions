# Date Functions: Time Calculations

Advanced | db

Reports are produced "as of" a fixed date so they are reproducible: **2024-06-30**. For every user compute:

- `age_years`: the number of **completed** years between `birth_date` and 2024-06-30 (a birthday that has not happened yet this year does not count), and
- `days_registered`: the number of whole days between `registered_on` and 2024-06-30.

Dates are stored as `'YYYY-MM-DD'` text. Write a query returning `name`, `age_years` and `days_registered`.

### Constraints

- Columns, in order: `name`, `age_years`, `days_registered`
- Use the fixed reference date `'2024-06-30'`, not `'now'`
- Age counts completed years only (a birthday on 2024-06-30 itself counts as already happened)

### Hints

<details>
<summary>Hint 1</summary>

`julianday(date)` converts a date to a day number, so subtracting two of them gives days.

</details>

<details>
<summary>Hint 2</summary>

Years: subtract the years, then subtract 1 if the month-day of the birthday is still ahead of 2024-06-30.

</details>
