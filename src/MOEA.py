import numpy as np
from src.operators import mutate
from src.archive import Archive, dominates

def optimise(problem, iterations=5000):
    n = problem.n_assets

    # initial random solution
    x = np.random.rand(n)
    x = x / x.sum()
    y = problem.evaluate(x)

    archive = Archive()
    archive.update(x, y)

    for it in range(iterations):
        xp = mutate(x)
        yp = problem.evaluate(xp)

        # update archive
        archive.update(xp, yp)

        # log archive size every 1000 iterations
        if it % 1000 == 0:
            archive.history.append(len(archive.Y))

        # selection: accept if not dominated
        if not dominates(y, yp):
            x, y = xp, yp

    return archive
