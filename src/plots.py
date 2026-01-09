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

def plot_archive_growth(archive):
    import matplotlib.pyplot as plt
    plt.plot(archive.history)
    plt.xlabel("Iteration")
    plt.ylabel("Archive size")
    plt.title("Growth of Non-dominated Archive")
    plt.show()

