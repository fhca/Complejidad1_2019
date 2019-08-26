
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.cm as cmx


class Tela:
    def __init__(self, f, x, xiniciales, itera=10000):
        xiniciales = np.array(xiniciales).flatten()
        # self.fig, self.ax = plt.subplots()
        self.fig = plt.figure()

        plt.grid(True)
        n = xiniciales.size
        x1 = np.empty((n, itera))
        x1[:, 0] = xiniciales
        _f = np.frompyfunc(lambda x, _: f(x), 2, 1)
        x2 = _f.accumulate(x1, dtype=np.object, axis=1).astype(np.float)
        x3 = np.repeat(x2, 2, axis=1)
        y1 = x3[:, 2:].copy()
        y2 = np.concatenate((np.array([[0]]*n), y1,
                             np.array(list(map(f, y1[:, -1]))).reshape(n, -1)), axis=1)
        plt.plot(x, np.array(_f(x, None)), color='k', linewidth=.3)
        plt.plot(x, x, color='r', linewidth=.3)
        self.x, self.y = x3, y2
        self.tela = [plt.plot([], [], color=cmx.jet(i/n), linewidth=1)[0]
                     for i in range(n)]
        self.itera = itera

    def animacion(self, i):
        """Tela contiene los Artist devueltos por cada plot, así a cada t
        hay que asignarle el l-ésimo renglón de self.x y self.y hasta la
        columna 2i-esima (i-esima iteración)"""
        for l, t in enumerate(self.tela):
            t.set_data(self.x[l, 2*i-100:2*i], self.y[l, 2*i-100:2*i])
        return self.tela

    def muestra(self, retardo=1000):  # retardo en milisegundos
        a = animation.FuncAnimation(self.fig, self.animacion,
                                    frames=np.arange(self.itera),
                                    interval=retardo,
                                    blit=True)
        plt.show()


# tienda
# Tela(lambda x: 2*x if x < 0.5 else 2-2*x, np.arange(0, 1, .01), .24,
#     itera=300000).muestra(retardo=200)


# logística
R = 4
Tela(lambda x: R*x*(1-x), np.arange(0, 1, .01),
     [.09], itera=300000).muestra(retardo=100)
# Tela(lambda x: 3.5*x*(1-x), np.arange(0, 1, .01), [.9],
#      itera=3000).muestra(retardo=20)
