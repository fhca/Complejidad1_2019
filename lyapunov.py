__author__ = 'fhca'

import numpy as np
import matplotlib.pyplot as plt
#from matplotlib import cm


def logistic(R, x):
    return R * x * (1 - x)


def evaluate(n, x0, c, f):
    """Returns n orbit values after the first 500 values."""
    res = np.empty(n)
    res[0] = x0
    for _ in range(500):
        res[0] = f(c, res[0])  # wasted
    for i in range(1, n):
        res[i] = f(c, res[i - 1])  # first n evaluations are wasted
    return res


fig = plt.figure()
ax = fig.add_subplot(111)

N = 1000  # N x N square window, (resolution)
C = np.linspace(0, 4, N)
Y = np.zeros_like(C)
for i, c in enumerate(C):
    T = evaluate(1000, .5, c, logistic)
    Y[i] = sum(np.log(np.abs(c - 2 * c * T))) / N

ax.plot(C, Y)
ax.plot(C, np.zeros_like(C))
plt.show()
