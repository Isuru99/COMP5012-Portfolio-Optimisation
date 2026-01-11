import numpy as np

def load_portfolio_data(filepath):
    with open(filepath, "r") as f:
        lines = [ln.strip() for ln in f.readlines()]

    # remove empty lines 
    lines = [ln for ln in lines if ln != ""]

    returns = []

    # Read expected returns block 
    i = 0
    while i < len(lines):
        parts = lines[i].split()

        # If this looks like correlation data, stop reading returns
        if len(parts) == 3 and parts[0].isdigit() and parts[1].isdigit():
            break

        # Otherwise, treat as returns line (take first column only)
        # (File has 2 columns here; use column 1 as expected return)
        returns.append(float(parts[0]))
        i += 1

    mu = np.array(returns, dtype=float)
    num_assets = len(mu)

    # Read correlation data 
    corr = np.eye(num_assets)

    for line in lines[i:]:
        parts = line.split()
        if len(parts) == 3 and parts[0].isdigit() and parts[1].isdigit():
            a = int(parts[0]) - 1
            b = int(parts[1]) - 1
            value = float(parts[2])
            corr[a, b] = value
            corr[b, a] = value

    # Covariance matrix 
    std = np.ones(num_assets)             # unit Standard Deviation assumption
    cov = corr * np.outer(std, std)     # so covariance == correlation

    return mu, cov