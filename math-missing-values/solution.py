
import numpy as np


# 1. Detect missing values
def missing_mask(x):
    return np.isnan(x)


# 2. Count missing values per column
def missing_count_per_column(x):
    mask = missing_mask(x)
    return np.sum(mask, axis=0)


# 3. Calculate missing fraction per column
def missing_fraction_per_column(x):
    mask = missing_mask(x)
    return np.mean(mask, axis=0)


# 4. Impute missing values using column mean
def impute_with_mean(x):
    x = x.copy()

    mask = missing_mask(x)
    means = np.nanmean(x, axis=0)

    rows, cols = np.where(mask)
    x[rows, cols] = means[cols]

    return x


# 5. Impute missing values using column median
def impute_with_median(x):
    x = x.copy()

    mask = missing_mask(x)
    medians = np.nanmedian(x, axis=0)

    rows, cols = np.where(mask)
    x[rows, cols] = medians[cols]

    return x
