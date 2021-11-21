import numpy as np
from scipy.stats import norm


def markov_ar(grid_size, nz, rho, sigma):
    sigma_z = np.sqrt(sigma ** 2 / (1 - rho ** 2))
    z_bar = sigma_z * grid_size

    # compute Z grid
    start = - z_bar
    step = 2 * z_bar / (nz - 1)
    stop = start + (nz - 1) * step
    zt = np.append(np.arange(start, stop, step), stop)

    # compute transition matrix
    transition_matrix = np.zeros((nz, nz))
    for i in range(nz):
        transition_matrix[i, 0] = norm.cdf(((zt[0] - rho * zt[i]) / sigma) + (step / (2 * sigma)))

        for j in range(1, nz - 1):
            transition_matrix[i, j] = norm.cdf(
                ((zt[j] - rho * zt[i]) / sigma) + (step / (2 * sigma))) - norm.cdf(
                ((zt[j] - rho * zt[i]) / sigma) - (step / (2 * sigma)))

        transition_matrix[i, nz-1] = 1 - np.sum(transition_matrix[i, 0:(nz - 2)])

    return zt, transition_matrix
