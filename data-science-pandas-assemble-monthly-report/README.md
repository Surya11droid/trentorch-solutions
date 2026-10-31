# Assemble: A Monthly Sales Report

Intermediate | data-science | pandas | eda | assemble

### The problem, from first principles

This is the question the previous ones were building towards, and it is the shape of a thousand real tasks: raw order lines arrive as text, customers live in another table, and someone wants **one tidy table per month**: how many orders, how much revenue, the average order, how revenue moved against the month before, and which region sold the most. No single pandas call produces that. It needs parsing, a join, a group-by on a derived key, a calendar with no gaps, a shifted comparison, and a rule for ties.

Each of those steps is something you have already built. The point of the question is combining them without losing rows silently, and with every edge defined: bad dates, orders for unknown customers, empty months.

### From theory to code

Implement `monthly_report(orders, customers)`. The signature and docstring are already in the editor.

### Constraints

- `orders` has `order_id`, `customer_id`, `order_date` (text `YYYY-MM-DD`, possibly invalid) and `amount` (a number). `customers` has `id` (unique) and `region`.
- Ignore (do not count anywhere) orders whose `order_date` is not a valid `YYYY-MM-DD` date, and orders whose `customer_id` is not in `customers`.
- The result is indexed by **month start** (first day of the month, midnight), named `month`, covering **every month** from the earliest to the latest valid order, including months with no orders.
- Columns, in this order: `orders` (integer count), `revenue` (float sum of `amount`, `0.0` for an empty month), `avg_order_value` (`revenue / orders`, `NaN` when there are no orders), `growth_pct` (`100 * (revenue - previous month's revenue) / previous month's revenue`, `NaN` for the first month or when the previous month's revenue is `0`), `top_region` (the region with the highest revenue that month; ties go to the alphabetically smaller region; `None` or `NaN` for an empty month).
- If there is no valid order at all, return an empty frame with those five columns.
- The input frames are not changed.

### Hints

<details>
<summary>Hint 1</summary>

Build the pieces in order: parse the dates and drop the invalid ones, join the region, derive a month-start column, then aggregate.

</details>

<details>
<summary>Hint 2</summary>

`reindex` to a `pd.date_range(first, last, freq="MS")` creates the empty months, and `shift(1)` aligns each month with the one before it.

</details>

<details>
<summary>Hint 3</summary>

For `top_region`: sum revenue per (month, region), sort by month, revenue descending, region ascending, and keep the first row per month.

</details>
