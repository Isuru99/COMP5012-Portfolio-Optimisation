import numpy as np

class PortfolioProblem:
    def __init__(self, mu, cov_matrix):
        self.mu = mu
        self.cov_matrix = cov_matrix
        self.no_assets = len(mu)

    def evaluate(self, w):
        # Objective 1: maximise return → minimise negative return
        returns = -np.dot(w, self.mu)

        # Objective 2: minimise risk (variance)
        #risk = w.T @ self.cov @ w
        risk = np.dot(w.T, np.dot(self.cov_matrix, w))

        return np.array([returns, risk])