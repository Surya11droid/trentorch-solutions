
import pandas as pd
import numpy as np
from pandas.api.types import is_integer_dtype, is_float_dtype


def profile(df):
    result = {
        "n_rows": int(df.shape[0]),
        "n_cols": int(df.shape[1]),
        "missing": {},
        "n_duplicate_rows": int(df.duplicated().sum()),
        "numeric": {},
        "categorical": {},
    }

    for col in df.columns:
        series = df[col]
        result["missing"][col] = int(series.isna().sum())

        dtype = series.dtype
        is_numeric = (
            is_integer_dtype(dtype) or is_float_dtype(dtype)
        )

        if is_numeric:
            values = series.dropna()

            if len(values) == 0:
                mean = std = minimum = maximum = float("nan")
            else:
                mean = float(values.mean())
                minimum = float(values.min())
                maximum = float(values.max())

                if len(values) < 2:
                    std = float("nan")
                else:
                    std = float(values.std(ddof=1))

            result["numeric"][col] = {
                "mean": mean,
                "std": std,
                "min": minimum,
                "max": maximum,
            }

        else:
            values = series.dropna()
            counts = values.value_counts()

            if len(counts) == 0:
                top = None
                top_count = 0
            else:
                top_count = int(counts.max())
                tied_values = counts[counts == top_count].index.tolist()
                top = min(tied_values)

            result["categorical"][col] = {
                "n_unique": int(values.nunique()),
                "top": top,
                "top_count": top_count,
            }

    return result
