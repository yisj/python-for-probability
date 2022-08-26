import numpy as np


def expected_value(x, px):
    return np.sum(np.multiply(x, px))


def cov(x, px):
    ex = expected_value(x, px)
    x = x - ex
    x = x * x
    return expected_value(x, px)


def cov2(x, px):
    ex = expected_value(x, px)
    x = x * x
    ex2 = expected_value(x, px)
    return ex2 - ex*ex


x = [1, 2, 3, 4, 5, 6]
px = [1 / 6] * 6
x = np.array(x)
px = np.array(px)

print(cov(x, px))
print(cov2(x, px))