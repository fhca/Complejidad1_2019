import numpy as np
import matplotlib.pyplot as plt


tres_vertices = np.array([[0, 0], [1, 0], [0.5, np.sqrt(.75)]])

azar = np.random.randint(0, 3, 10000)

x = np.array([.5, .3])

plt.plot(*tres_vertices.T, "*", color="red")
for v in tres_vertices[azar]:
    plt.plot(*x, '.')
    x = (x + v)/2
plt.show()
