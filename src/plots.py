import matplotlib.pyplot as plt
import numpy as np

def plot_pareto(archive):
    Y = np.array(archive.Y)
    returns = -Y[:, 0]
    risks = Y[:, 1]

    plt.scatter(risks, returns)
    plt.xlabel("Risk (Variance)")
    plt.ylabel("Expected Return")
    plt.title("Pareto Front Approximation")
    plt.grid(True)
    plt.show()

