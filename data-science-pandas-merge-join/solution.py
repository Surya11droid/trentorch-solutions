
import pandas as pd


def orders_with_customers(customers, orders):
    result = orders.merge(
        customers,
        left_on="customer_id",
        right_on="id",
        how="inner"
    )

    result = result[
        ["order_id", "customer_id", "name", "amount"]
    ]

    return result.sort_values("order_id").reset_index(drop=True)


def customer_totals(customers, orders):
    merged = customers.merge(
        orders,
        left_on="id",
        right_on="customer_id",
        how="left"
    )

    result = merged.groupby(["id", "name"]).agg(
        n_orders=("order_id", "count"),
        total=("amount", "sum")
    )

    result["total"] = result["total"].fillna(0.0)

    return result.reset_index().sort_values(
        "id"
    ).reset_index(drop=True)


def customers_without_orders(customers, orders):
    mask = ~customers["id"].isin(orders["customer_id"])

    return customers[mask].reset_index(drop=True)


def safe_merge(left, right, key):
    if right[key].duplicated().any():
        raise ValueError("Duplicate keys found in right DataFrame")

    return left.merge(
        right,
        on=key,
        how="left",
        sort=False
    ).reset_index(drop=True)
