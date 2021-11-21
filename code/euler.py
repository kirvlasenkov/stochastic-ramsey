import numpy as np

import consts as const
from policy import policy_function


def compute_euler_residuals(k_vector, z_vector, k_grid, z_grid):
    n = len(k_vector)
    m = len(z_vector)
    eer = np.zeros(n, m)

    for i in range(n):
        for j in range(m):
            z0 = const.RHO * np.log(z_vector[j])
            k1 = policy_function(k_vector, z_vector, k_grid, z_grid)

