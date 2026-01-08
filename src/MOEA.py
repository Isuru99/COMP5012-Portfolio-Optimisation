from src.operators import mutate
from src.archive import Archive, dominates

def optimise(problem, iterations=5000):
    n = problem.n_assets

    x = np.random.rand(n)
    x = x / x.sum()
    y = problem.evaluate(x)

    archive = Archive()
    archive.update(x, y)

    for _ in range(iterations):
        xp = mutate(x)
        yp = problem.evaluate(xp)

        archive.update(xp, yp)

        if not dominates(y, yp):
            x, y = xp, yp

    return archive

