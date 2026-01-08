
import numpy as np

def repair(w):
    w = np.clip(w, 0, 1)
    total = w.sum()
    if total == 0:
        w = np.ones_like(w) / len(w)
    else:
        w = w / total
    return w