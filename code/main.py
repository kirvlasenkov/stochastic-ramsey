import numpy as np

import consts as const
from markov_ar import markov_ar
from utility import utility_function
from solver import solver
from euler import compute_euler_residuals

def main():
    z_grid, transition_matrix = markov_ar(const.Z_GRID_SIZE, const.Z_NUMBER, const.RHO, const.SIGMA)

    z_grid = np.exp(z_grid)
    z_min = z_grid[0]
    z_max = z_grid[-1]

    k_min = ((1 - const.BETA * (1 - const.DELTA)) / (const.ALPHA * const.BETA * z_min)) ** (1 / (const.ALPHA - 1))
    k_max = ((1 - const.BETA * (1 - const.DELTA)) / (const.ALPHA * const.BETA * z_max)) ** (1 / (const.ALPHA - 1))

    # stationary solution of deterministic model
    k_star = ((1 - const.BETA * (1 - const.DELTA)) / (const.ALPHA * const.BETA)) ** (1 / (const.ALPHA - 1))
    c_star = k_star ** const.ALPHA - const.DELTA * k_star

    k_min_grid = const.K_MIN_GRID_SIZE * k_min
    k_max_grid = const.K_MAX_GRID_SIZE * k_max

    k_min_euler = const.K_MIN_EULER * k_star
    k_max_euler = const.K_MAX_EULER * k_star

    # initialization of value function
    v0 = utility_function(z=1, k1=k_star, k2=k_star) * np.ones((const.K_NUMBER[0], const.Z_NUMBER))

    for i in range(len(const.K_NUMBER)):
        k_number = const.K_NUMBER[i]

        start = k_min_grid
        step = (k_max_grid - k_min_grid) / (k_number - 1)
        stop = start + (k_number - 1) * step
        k_grid = np.append(np.arange(start, stop, step), stop)
        assert k_grid.shape[0] == k_number, f'{k_grid.shape[0]} != {k_number}'

        # value function iteration step
        v1, policy_choices = solver(k_grid, z_grid, transition_matrix, v0)
        assert v1.shape == v0.shape, f'{v0.shape} != {v1.shape}'

        if not const.WITH_INTERPOLATION:  # w/o interpolation
            policy_values = np.zeros(k_number, const.Z_NUMBER)

            for l in range(k_number):
                for j in range(const.Z_NUMBER):
                    policy_values = k_grid[policy_choices[l, j]]

        else:
            raise NotImplementedError('Interpolation not available so far')

        # Euler residuals computation
        start = k_min_euler
        step = (k_max_euler - k_min_euler) / (const.RES_EULER_NUMBER - 1)
        stop = start + step * (const.RES_EULER_NUMBER - 1)
        k_vector = np.append(np.arange(start, stop, step), stop)

        start = 0.95
        step = 0.1 / (const.RES_EULER_NUMBER - 1)
        stop = start + (const.RES_EULER_NUMBER - 1) * step
        z_vector = np.append(np.arange(start, stop, step), stop)

        z0 = 0
        k1 = 0

        eer = compute_euler_residuals(k_vector, z_vector, k_grid, z_grid, )





if __name__ == '__main__':
    main()
