from src.data import load_portfolio_data
from src.problem import PortfolioProblem
from src.MOEA import optimise
from src.plots import plot_pareto
import numpy as np

mu, cov = load_portfolio_data("data/port3.txt")

np.random.seed(42)

problem = PortfolioProblem(mu, cov)
archive = optimise(problem, iterations=5000)

plot_pareto(archive)
