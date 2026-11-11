import numpy as np

def mse_loss(input, target, reduction='mean'):


    squared_error = (input - target) ** 2

    if reduction == 'none':
        return squared_error

    elif reduction == 'sum':
        return float(np.sum(squared_error))

    elif reduction == 'mean':
        return float(np.mean(squared_error))

    else:
        raise ValueError("Invalid reduction")
