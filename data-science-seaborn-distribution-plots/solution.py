import seaborn as sns
import matplotlib.pyplot as plt


def histogram_axes(df, column, bins, stat):
    ax = sns.histplot(
        data=df,
        x=column,
        bins=bins,
        stat=stat
    )
    return ax


def kde_axes(df, column):
    ax = sns.kdeplot(
        data=df,
        x=column
    )
    return ax


def kde_by_group(df, column, group, order):
    ax = sns.kdeplot(
        data=df,
        x=column,
        hue=group,
        hue_order=order,
        common_norm=False
    )
    return ax


def ecdf_axes(df, column):
    ax = sns.ecdfplot(
        data=df,
        x=column
    )
    return ax
