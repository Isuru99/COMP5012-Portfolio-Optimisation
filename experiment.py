from src.data import load_portfolio_data
from src.problem import PortfolioProblem
from src.MOEA import optimise
from src.plots import plot_pareto

mu, cov = load_portfolio_data("data/port3.txt")

problem = PortfolioProblem(mu, cov)
archive = optimise(problem, iterations=10000)

plot_pareto(archive)
