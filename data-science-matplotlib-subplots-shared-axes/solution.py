
import numpy as np
import matplotlib.pyplot as plt
import math


def small_multiples(series, ncols):
    """
    Create multiple line charts with shared x and y axes.
    """
    n = len(series)

    if n == 0:
        raise ValueError("series cannot be empty")

    if ncols <= 0:
        raise ValueError("ncols must be positive")

    nrows = math.ceil(n / ncols)

    fig, axes = plt.subplots(
        nrows,
        ncols,
        figsize=(5 * ncols, 4 * nrows),
        sharex=True,
        sharey=True,
        squeeze=False
    )

    for i, (title, (x, y)) in enumerate(series.items()):
        row = i // ncols
        col = i % ncols

        ax = axes[row, col]

        ax.plot(x, y)
        ax.set_title(title)

    # Hide unused panels
    for i in range(n, nrows * ncols):
        row = i // ncols
        col = i % ncols

        axes[row, col].set_visible(False)

    fig.tight_layout()

    return fig, axes


def twin_axis_chart(x, y_left, y_right,
                    left_label, right_label):
    """
    Create a chart with two y axes.
    """

    fig, ax_left = plt.subplots()

    # Left y-axis
    ax_left.plot(x, y_left, color="tab:blue")
    ax_left.set_ylabel(left_label, color="tab:blue")

    # Right y-axis
    ax_right = ax_left.twinx()

    ax_right.plot(x, y_right, color="tab:red")
    ax_right.set_ylabel(right_label, color="tab:red")

    return fig, ax_left, ax_right


def set_limits_and_ticks(ax, xlim, ylim,
                         xticks, xticklabels, logy):
    """
    Set axis limits, ticks, labels and y-axis scale.
    """

    ax.set_xlim(xlim)
    ax.set_ylim(ylim)

    ax.set_xticks(xticks)
    ax.set_xticklabels(xticklabels)

    if logy:
        ax.set_yscale("log")
    else:
        ax.set_yscale("linear")
