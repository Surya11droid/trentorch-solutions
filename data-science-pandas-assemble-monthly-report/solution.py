
import pandas as pd
import numpy as np

def monthly_report(orders, customers):

    # 1. Convert order_date into datetime
    df = orders.copy()

    df["order_date"] = pd.to_datetime(
        df["order_date"],
        format="%Y-%m-%d",
        errors="coerce"
    )

    # 2. Remove invalid dates
    df = df.dropna(subset=["order_date"])

    # 3. Merge orders with customer information
    df = df.merge(
        customers,
        left_on="customer_id",
        right_on="id",
        how="inner"
    )

    # 4. If no valid orders remain, return empty report
    columns = [
        "orders",
        "revenue",
        "avg_order_value",
        "growth_pct",
        "top_region"
    ]

    if df.empty:
        result = pd.DataFrame(columns=columns)
        result.index = pd.DatetimeIndex([], name="month")
        return result

    # 5. Extract month start from order_date
    df["month"] = df["order_date"].dt.to_period("M").dt.to_timestamp()

    # 6. Group by month and calculate order count and revenue
    monthly = df.groupby("month").agg(
        orders=("order_id", "count"),
        revenue=("amount", "sum")
    )

    # 7. Create a continuous monthly calendar
    all_months = pd.date_range(
        start=monthly.index.min(),
        end=monthly.index.max(),
        freq="MS"
    )

    monthly = monthly.reindex(all_months)

    # 8. Fill empty months
    monthly["orders"] = monthly["orders"].fillna(0).astype(int)
    monthly["revenue"] = monthly["revenue"].fillna(0.0).astype(float)

    # 9. Calculate average order value
    monthly["avg_order_value"] = (
        monthly["revenue"] / monthly["orders"].replace(0, np.nan)
    )

    # 10. Calculate month-over-month growth
    previous_revenue = monthly["revenue"].shift(1)

    monthly["growth_pct"] = (
        (monthly["revenue"] - previous_revenue)
        / previous_revenue.replace(0, np.nan)
    ) * 100

    # 11. Find the highest-revenue region for each month
    regional = (
        df.groupby(["month", "region"])["amount"]
        .sum()
        .reset_index()
    )

    # Sort alphabetically first, then by revenue descending
    regional = regional.sort_values(
        ["month", "region", "amount"],
        ascending=[True, True, False]
    )

    top_regions = (
        regional.sort_values(
            ["month", "amount", "region"],
            ascending=[True, False, True]
        )
        .drop_duplicates("month")
        .set_index("month")["region"]
    )

    monthly["top_region"] = top_regions.reindex(monthly.index)

    # 12. Set index name and column order
    monthly.index.name = "month"

    return monthly[columns]
