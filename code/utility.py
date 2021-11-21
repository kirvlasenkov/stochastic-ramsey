import consts as const
import numpy as np


def utility_function(z, k1, k2):
    c = z * (k1 ** const.ALPHA) + (1 - const.DELTA) * k1 - k2

    if c < 0:
        raise ValueError('consumption is negative')
    else:
        if const.ETA == 1:
            return np.log(c)
        else:
            return (c ** (1 - const.ETA)) / (1 - const.ETA)
