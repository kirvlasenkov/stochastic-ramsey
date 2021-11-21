import numpy as np


def bilinear_interpolation(x, y, z, x0, y0):
    n = len(x)
    m = len(y)

    if (x0 < x[0]) or (x0 > x[-1]):
        raise ValueError('x out of bounds')

    if (y0 < y[0]) or (y0 > y[-1]):
        raise ValueError('y out of bounds')

    i = np.sum(x <= x0)
    j = np.sum(y <= y0)

    if (i == n) and (j == m):
        z0 = z[-1, -1]

    elif (i == n) and (j < m):
        u = (y0 - y[j]) / (y[j + 1] - j[j])
        z = (1 - u) * z[n, j] + u * z[n, j + 1]

    elif (i < n) and (j == m):
        t = (x0 - x[i]) / (x[i + 1] - x[i])
        z = t * z[i + 1, m] + (1 - t) * z[i, m]

    else:
        t = (x0 - x[i]) / (x[i + 1] - x[i])
        u = (y0 - y[j]) / (y[j + 1] - y[j])
        z = (1 - t) * (1 - u) * z[i, j] + t * (1 - u) * z[i + 1, j] + t * u * z[i + 1, j + 1] + (
                1. - t) * u * z[i, j + 1]

    return z
