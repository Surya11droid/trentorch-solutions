
import numpy as np

def predict_labels(p, threshold=0.5):
    return (p >= threshold).astype(int)
