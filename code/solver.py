import numpy as np

import consts as const
from utility import utility_function


def solver(k_grid, z_grid, transition_matrix, v0):
    eps = const.SOLVER_EPS * (1 - const.BETA)

    k_grid_len = len(k_grid)
    z_grid_len = len(z_grid)

    if const.WITH_INTERPOLATION:
        raise NotImplementedError()
    else:
        h1 = np.ones((k_grid_len, z_grid_len))

    h2 = np.ones((k_grid_len, z_grid_len))
    w = np.zeros((3, 1))

    v1 = v0  # old value function
    v2 = np.zeros((k_grid_len, z_grid_len))  # brand new value function
    dv = 1
    nc = 1

    t = 1
    while (t < const.SOLVER_MAX_ITER) and (dv >= eps) and (nc <= const.POLICY_MAX_ITER):
        for j in range(z_grid_len):
            js = 1
            for i in range(k_grid_len):
                j_min = js
                j_max = k_grid_len

                # binary search
                while (j_max - j_min) > 2:
                    jl = int(np.floor((j_min + j_max) / 2))
                    ju = jl + 1

                    w[0] = utility_function(z_grid[j], k_grid[i], k_grid[jl] + np.sum(const.BETA * (
                            transition_matrix[j, :] * (v1[jl, :]))))
                    w[1] = utility_function(z_grid[j], k_grid[i], k_grid[ju] + np.sum(const.BETA * (
                            transition_matrix[j, :] * (v1[ju, :]))))

                    if w[1] > w[0]:
                        j_min = jl
                    else:
                        j_max = ju

                w[0] = utility_function(z_grid[j], k_grid[i], k_grid[j_min] + np.sum(const.BETA * (
                        transition_matrix[j, :] * (v1[j_min, :]))))

                if j_min < j_max:
                    w[1] = utility_function(z_grid[j], k_grid[i], k_grid[j_min + 1] + np.sum(const.BETA * (
                            transition_matrix[j, :] * (v1[j_min + 1, :]))))

                else:
                    w[1] = w[0]

                w[2] = utility_function(z_grid[j], k_grid[i], k_grid[j_max] + np.sum(const.BETA * (
                        transition_matrix[j, :] * (v1[j_max, :]))))

                js = np.argmax(w)

                if not const.WITH_INTERPOLATION:
                    v2[i, j] = w[js]

                else:
                    raise NotImplementedError()

                js = j_min + js - 1

        if not const.WITH_INTERPOLATION:
            di = np.sum(np.sum(h2 != h1))

            if di > 0:
                nc = 0
            else:
                nc += 1
            h1 = h2

        else:
            raise NotImplementedError()

        dv = np.max(np.max(np.abs(v2 - v1)))
        print("# of indices that have changed: %d\n", di)
        print("# of consecutive iterations with constant policy function= %d\n", nc)

        v1 = v2
        t += 1

    policy_choices = h2

    return v1, policy_choices
