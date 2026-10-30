import pandas as pd


def group_summary(df, key, value):
    result = (
        df.groupby(key, sort=True)[value]
        .agg(
            n="count",
            mean="mean",
            median="median",
            max="max"
        )
    )

    return result


def add_group_mean(df, key, value):
    result = df.copy()

    result[f"{value}_group_mean"] = (
        result.groupby(key)[value]
        .transform("mean")
    )

    return result


def zscore_within_group(df, key, value):
    grouped = df.groupby(key)[value]

    group_mean = grouped.transform("mean")
    group_std = grouped.transform("std")

    zscore = (df[value] - group_mean) / group_std

    return zscore.astype(float)


def top_n_per_group(df, key, value, n):
    valid = df.dropna(subset=[key, value])

    result = (
        valid.sort_values(
            by=[key, value],
            ascending=[True, False],
            kind="stable"
        )
        .groupby(key, sort=True, group_keys=False)
        .head(n)
    )

    return result
