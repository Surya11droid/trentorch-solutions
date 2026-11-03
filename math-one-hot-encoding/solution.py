
import numpy as np


def get_unique_categories(column):
    return sorted(set(column))


def one_hot_encode(column, categories=None):

    if categories is None:
        categories = get_unique_categories(column)

    category_to_index = {
        category: i
        for i, category in enumerate(categories)
    }

    encoded = np.zeros(
        (len(column), len(categories)),
        dtype=int
    )

    for row, category in enumerate(column):
        encoded[row, category_to_index[category]] = 1

    return encoded
