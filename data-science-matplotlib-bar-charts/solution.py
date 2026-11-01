import matplotlib.pyplot as plt
import numpy as np


def bar_chart(labels, values):
    fig, ax = plt.subplots()

    x = np.arange(len(labels))

    ax.bar(x, values, width=0.8)

    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylim(bottom=0)

    return fig, ax


def grouped_bars(labels, series):
    fig, ax = plt.subplots()

    x = np.arange(len(labels))
    k = len(series)

    width = 0.8 / k

    for j, (name, values) in enumerate(series.items()):
        positions = x + (j - (k - 1) / 2) * width

        ax.bar(positions, values, width=width, label=name)

    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylim(bottom=0)
    ax.legend()

    return fig, ax


def stacked_bars(labels, series):
    fig, ax = plt.subplots()

    x = np.arange(len(labels))

    bottom = np.zeros(len(labels))

    for name, values in series.items():
        ax.bar(
            x,
            values,
            width=0.6,
            bottom=bottom,
            label=name
        )

        bottom += np.array(values)

    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylim(bottom=0)
    ax.legend()

    return fig, ax


def annotate_bars(ax):
    annotations = []

    for bar in ax.patches:
        height = bar.get_height()

        text = f"{height:g}"

        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_y() + height,
            text,
            ha="center",
            va="bottom"
        )

        annotations.append(text)

    return annotations
