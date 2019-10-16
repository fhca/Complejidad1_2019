import numpy as np
import matplotlib.pyplot as plt

d = 5
v = np.zeros((d, d))
ancho = [-1, 1]
alto = [-1, 1]
re = np.linspace(*ancho, d, endpoint=True)
im = np.linspace(*alto, d, endpoint=True)
v = np.array((re, im)).T
print(v)
