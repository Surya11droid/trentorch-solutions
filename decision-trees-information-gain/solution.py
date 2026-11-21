
def information_gain(parent_labels, left_labels, right_labels):
    parent_impurity = gini_impurity(parent_labels)

    n = parent_labels.size
    n_left = left_labels.size
    n_right = right_labels.size

    left_weight = n_left / n
    right_weight = n_right / n

    weighted_child_impurity = (
        left_weight * gini_impurity(left_labels)
        + right_weight * gini_impurity(right_labels)
    )

    gain = parent_impurity - weighted_child_impurity

    return float(gain)
