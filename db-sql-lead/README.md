# LEAD: Access Next Row

Advanced | db

A retention analysis asks: after each event, what did the same user do next? Each user's events form their own timeline ordered by `ts`; the last event of a timeline has no next event.

Write a query returning `user_id`, `event` and the following event of the same user as `next_event`, using `LEAD()`.

### Constraints

- Columns, in order: `user_id`, `event`, `next_event`
- Only look at the same user's events (partition by user)
- The last event of each user has `next_event` NULL

### Hints

<details>
<summary>Hint 1</summary>

`LEAD` is the mirror image of `LAG`: it reads the next row.

</details>

<details>
<summary>Hint 2</summary>

Use `PARTITION BY user_id ORDER BY ts` so users do not mix.

</details>
