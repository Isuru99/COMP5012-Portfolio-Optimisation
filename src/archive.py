import numpy as np

def dominates(a, b):
    return np.all(a <= b) and np.any(a < b)

class Archive:
    def __init__(self):
        self.X = []
        self.Y = []

    def update(self, x, y):
        for y_old in self.Y:
            if dominates(y_old, y):
                return

        keep = []
        for i, y_old in enumerate(self.Y):
            if not dominates(y, y_old):
                keep.append(i)

        self.X = [self.X[i] for i in keep]
        self.Y = [self.Y[i] for i in keep]

        self.X.append(x)
        self.Y.append(y)
