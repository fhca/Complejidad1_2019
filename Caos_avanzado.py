import numpy as np
import matplotlib.pyplot as plt


tres_vertices = np.array([[0, 0], [1, 0], [0.5, np.sqrt(.75)]])

# azar = np.random.randint(0, 3, 1000000)
# azar = np.random.randn(1000000)


#azar[azar > 1] = 2
#azar[(-1 < azar) & (azar < 1)] = 1
# azar[azar < -1] = 0  # esta linea tiene que ir despues de asignar a uno

#azar = azar.astype(int)

roundrobin = np.array([[0, 1, 2]]).repeat(300000, axis=0).flatten()


def avg(a, b):
    return (a+b)/2


avg_p = np.frompyfunc(avg, 2, 1)
x = avg_p.accumulate(tres_vertices[roundrobin], dtype=np.ndarray)
plt.plot(*x.T, '.')
plt.show()
