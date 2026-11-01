import matplotlib.pyplot as plt
import pandas as pd


def sales_dashboard(df):
    """
    Build a three-panel sales dashboard.

    Returns
    -------
    fig : matplotlib.figure.Figure
    """

    # Create figure with exactly 3 subplots in one row
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    monthly_revenue = (
        df.groupby(df["date"].dt.to_period("M"))["amount"]
            .sum()
            .sort_index()
    )

    axes[0].plot(
        monthly_revenue.index.astype(str),
        monthly_revenue.values,
        marker="o"
    )

    axes[0].set_title("Revenue by month")
    axes[0].set_xlabel("Month")
    axes[0].set_ylabel("Revenue")


    regional_revenue = (
        df.groupby("region")["amount"]
            .sum()
            .sort_values(ascending=False)
    )

    # Sort ties by region name ascending
    regional_revenue = regional_revenue.reset_index()
    regional_revenue = regional_revenue.sort_values(
        ["amount", "region"],
        ascending=[False, True]
    )

    axes[1].bar(
        range(len(regional_revenue)),
        regional_revenue["amount"]
    )

    axes[1].set_xticks(range(len(regional_revenue)))
    axes[1].set_xticklabels(regional_revenue["region"])

    axes[1].set_title("Revenue by region")
    axes[1].set_xlabel("Region")
    axes[1].set_ylabel("Revenue")


    axes[2].hist(df["amount"], bins=5)

    axes[2].set_title("Order amounts")
    axes[2].set_xlabel("Amount")
    axes[2].set_ylabel("Orders")


    fig.suptitle("Sales dashboard")

    fig.tight_layout()

    return fig
