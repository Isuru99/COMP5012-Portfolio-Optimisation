
import numpy as np

class PortfolioProblem:
    def __init__(self, mu, cov):
        self.mu = mu
        self.cov = cov
        self.n_assets = len(mu)

    def evaluate(self, w):
        # Objective 1: maximise return → minimise negative return
        f1 = -np.dot(w, self.mu)

        # Objective 2: minimise risk (variance)
        f2 = w.T @ self.cov @ w

        return np.array([f1, f2])