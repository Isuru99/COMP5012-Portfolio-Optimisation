
import numpy as np

def repair(w):
    w = np.clip(w, 0, 1)
    total = w.sum()
    if total == 0:
        w = np.ones_like(w) / len(w)
    else:
        w = w / total
    return w

def mutate(w, std=0.05, p_mut=1.0):
    wp = w.copy()
    if np.random.rand() < p_mut:
        idx = np.random.randint(len(w))
        wp[idx] += np.random.normal(0, std)
    return repair(wp)