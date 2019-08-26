__author__ = 'fhca'

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def logistica(r, x0=0.2, nvalores=1000):
    evalua = np.frompyfunc(lambda x, _: r*x*(1-x), 2, 1)
    orb = np.empty(nvalores)
    orb[0] = x0
    return evalua.accumulate(orb, dtype=np.object).astype(np.float)


def feigenbaum(f, minimo=0, maximo=4, nr=5000, n=3000):
    erres = np.linspace(minimo, maximo, nr, endpoint=True)
    plt.figure(figsize=(10, 7))
    for i, r in enumerate(erres):
        "x=[r,r,r,...] n-veces"
        plt.plot(np.full(n, r), f(r, x0=f(r)[-1], nvalores=n),
                 ',', color=cm.coolwarm(i/nr))
    plt.show()


feigenbaum(logistica, 1, 4)
