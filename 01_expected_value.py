import numpy as np


def expected_value(x, px):
    x = np.array(x)
    px = np.array(px)
    return np.sum(np.multiply(x, px))


x = [1, 2, 3, 4, 5, 6]
px = [1 / 6] * 6

print(px)
print(expected_value(x, px))
