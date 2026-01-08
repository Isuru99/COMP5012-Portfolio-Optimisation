import numpy as np

def load_portfolio_data(filepath):

    returns = []
    correlations = []

    with open(filepath, "r") as f:
        lines = f.readlines()

    # Read expected returns 
    i = 0
    while lines[i].strip() != "":
        parts = lines[i].split()
        returns.append(float(parts[0]))  # first column = expected return
        i += 1

    mu = np.array(returns)
    n_assets = len(mu)

    # Step 2: read correlation data
    corr = np.eye(n_assets)

    for line in lines[i+1:]:
        parts = line.split()
        if len(parts) == 3:
            a = int(parts[0]) - 1
            b = int(parts[1]) - 1
            value = float(parts[2])
            corr[a, b] = value
            corr[b, a] = value

    # Making Covariance Matrix
    # OR-Library provides correlation, not covariance
    std = np.ones(n_assets)  # get basic assumption 
    cov = corr * np.outer(std, std)

    return mu, cov