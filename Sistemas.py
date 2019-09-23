# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 22:17:56 2013

@author: fhca
"""

import matplotlib.pyplot as plt
from random import random
from math import sin, cos, pi, sqrt
from matplotlib import cm

REPETICIONES = 1000000
I = ((1, 0), (0, 1))


class Ifs(object):
    def __init__(self):
        self._X = [0]
        self._Y = [0]
        self._sistemas = []
        self.fig, self.ax = plt.subplots()

    def plot(self, titulo, color='b'):
        self.ajusta_prob()
        self._afin()
        self.ax.plot(self._X, self._Y, color+',')
        self.ax.set_title(titulo)
        plt.show()

    def _gira(self, grados):
        "Matriz de giro. usa grados, no radianes."
        g = grados*pi/180
        return ((cos(g), -sin(g)), (sin(g), cos(g)))

    def _afin(self):
        for i in range(REPETICIONES):
            r = random()
            pacum = 0.
            ((c00, c01), (c10, c11)), (ix, iy), (fx, fy), p = self._sistemas[0]
            for (a, d, e, p) in self._sistemas:
                pacum += p
                if r < pacum:
                    ((c00, c01), (c10, c11)), (ix, iy), (fx, fy) = a, d, e
                    break
            lx, ly = float(self._X[-1]), float(self._Y[-1])
            self._X.append(fx*(c00*lx+c01*ly)+ix)
            self._Y.append(fy*(c10*lx+c11*ly)+iy)

    def _vec(self, r):
        return (r, r)

    def sistema(self, angulo, desplazamiento, escala=1., probabilidad=0.):
        if isinstance(angulo, float) or isinstance(angulo, int):
            angulo = self._gira(float(angulo))
        if isinstance(desplazamiento, float) or isinstance(desplazamiento, int):
            desplazamiento = self._vec(float(desplazamiento))
        if isinstance(escala, float) or isinstance(escala, int):
            escala = self._vec(float(escala))
        self._sistemas.append((angulo, desplazamiento, escala, probabilidad))

    def ajusta_prob(self):
        pacum = 0.
        cuenta_ceros = 0
        nsist = []
        for (a, d, e, p) in self._sistemas:
            pacum += p
            cuenta_ceros += 1
        for (a, d, e, p) in self._sistemas:
            if p != 0.:
                nsist.append((a, d, e, p))
            else:
                nsist.append((a, d, e, (1.-pacum)/cuenta_ceros))
            self._sistemas = nsist

    def on_key_press(self, event):
        print(event.key)


class BarnsleyInternet(Ifs):
    """Helecho de Barnsley. Como el lo publicó."""

    def __init__(self):
        super(BarnsleyInternet, self).__init__()
        self.sistema(((.85, .04),  (-.04, .85)), (0, 1.6), 1, .85)
        self.sistema(((-.15, .28), (.26, .24)), (0, .44), 1, .07)
        self.sistema(((.20, -.26), (.23, .22)), (0, 1.6), 1, .07)
        self.sistema(((0, 0), (0, .16)), 0, 1, .01)
        self.plot("BarnsleyInternet")


class Sierpinski(Ifs):
    """ No hay rotación (se usa la matriz identidad I)
       Se pone la mitad del desplazamiento, los vértices serán al doble de este.
       La escala es .5
       ie. Este es el juego del caos, con un vértice inicial al azar, se itera
       convirtiéndose en la distancia promedio a los vértices del triángulo.
       """

    def __init__(self):
        super(Sierpinski, self).__init__()
        self.sistema(I, (.25, .5), .5)
        self.sistema(I, (.5, 0), .5)
        self.sistema(I, (0, 0), .5)
        self.plot("Sierpinski")


class Barnsley(Ifs):
    """Helecho de Barnsley con rotaciones."""

    def __init__(self):
        super(Barnsley, self).__init__()
        self.sistema(-2.5,  (0, 1.6), (.85, .85), 0.5)
        self.sistema(49,     (0, 1.6), (.3, .34), 0)
        self.sistema(-50,  (0, .44), (.3, .37), 0)
        self.sistema(0,     0,      (0, .16), .1)
        self.plot("Barnsley")


class Koch1(Ifs):
    """Koch clásico."""

    def __init__(self):
        super(Koch1, self).__init__()
        t = 1./3
        self.sistema(I, 0, t)
        self.sistema(60, (1, 0), t)

        self.sistema(-60, (1.5, sqrt(3)/2), t)
        self.sistema(I, (2, 0), t)

        self.plot("Koch1")


class Koch2(Ifs):
    """Koch cuando el pico no es equilatero sino rectángulo."""

    def __init__(self):
        super(Koch2, self).__init__()
        t = 1./3
        self.sistema(I, 0, t, .25)
        self.sistema(I, (2*t, 0), t, .25)

        self.sistema(90, (t, 0), t, 1./4)
        self.sistema(-45, (t, t), sqrt(2)*t, 1./4)

        self.sistema(-90, (t, 0), t, 1./4)
        self.sistema(45, (t, -t), sqrt(2)*t, 1./4)

        self.plot("Koch2")


class Devaney(Ifs):
    """Nubecitas del Devaney, me parece."""

    def __init__(self):
        super(Devaney, self).__init__()
        t = 1./2
        self.sistema(45, -4, t)
        self.sistema(45, (4, 0), t)
        self.sistema(45, (0, 4), t)
        self.plot("Devaney")


class Arbol(Ifs):
    """Arbol, ver Devaney."""

    def __init__(self):
        super(Arbol, self).__init__()
        t = 1./3
        self.sistema(I, (-7, 7), t)
        self.sistema(I, (0, 7), t)
        self.sistema(I, (7, 7), t)
        self.sistema(I, (0, 1.7), t)
        self.sistema(I, (0, -3.7), t)
        self.plot("Arbol")


class Hexagonos(Ifs):
    """Fractal de hexágonos derivado del cuadrado dividido en nueve."""

    def __init__(self):
        super(Hexagonos, self).__init__()
        t = 1./3
        self.sistema(I, (1./6, 0), t)
        self.sistema(I, (.5, 0), t)
        self.sistema(I, (0, 1./3), t)
        self.sistema(I, (2./3, 1./3), t)
        self.sistema(I, (1./6, 2./3), t)
        self.sistema(I, (1./2, 2./3), t)
        self.plot("Hexagonos")


class Carpeta(Ifs):
    """Carpeta de Menger."""

    def __init__(self):
        super(Carpeta, self).__init__()
        t = 1./3
        self.sistema(I, (0, 0), t)
        self.sistema(I, (1, 0), t)
        self.sistema(I, (2, 0), t)
        self.sistema(I, (0, 1), t)
        self.sistema(I, (2, 1), t)
        self.sistema(I, (0, 2), t)
        self.sistema(I, (1, 2), t)
        self.sistema(I, (2, 2), t)
        self.plot("Carpeta", 'r')


class AntiCarpeta(Ifs):
    """Complemento de la carpeta de Menger."""

    def __init__(self):
        super(AntiCarpeta, self).__init__()
        s = 1./3
        self.sistema(I, (3, 3), s)
        self.sistema(I, (4, 3), s)
        self.sistema(I, (5, 3), s)
        self.sistema(I, (3, 4), s)
        self.sistema(I, (4, 4), s)
        self.sistema(I, (5, 4), s)
        self.sistema(I, (3, 5), s)
        self.sistema(I, (4, 5), s)
        self.sistema(I, (5, 5), s)
        self.sistema(I, (1, 1), s)
        self.sistema(I, (4, 1), s)
        self.sistema(I, (7, 1), s)
        self.sistema(I, (1, 4), s)
        self.sistema(I, (7, 4), s)
        self.sistema(I, (1, 7), s)
        self.sistema(I, (4, 7), s)
        self.sistema(I, (7, 7), s)
        self.plot("AntiCarpeta")


class Pitagoras(Ifs):
    """Los ángulos originales se han perdido."""

    def __init__(self):
        super(Pitagoras, self).__init__()
        self.sistema(35, (0, 5), .8)
        self.sistema(50, (3.2, 7.4), .6)
        self.plot("Pitagoras")


class Atari(Ifs):
    """Parecen navecitas de Atari."""

    def __init__(self):
        super(Atari, self).__init__()
        self.sistema(I, (2, 0), 1./3)
        self.sistema(I, (0, 1), 1./3)
        self.sistema(I, (1, 1), 1./3)
        self.sistema(I, (0, 2), 1./3)
        self.sistema(I, (1, 2), 1./3)
        # self.sistema(I, (2,1), 1./3)
        self.plot("Atari")


class Mosaiquito(Ifs):
    """Mosaiquito, rombo derivado del cuadro dividido en nueve."""

    def __init__(self):
        super(Mosaiquito, self).__init__()
        t = 5./12
        self.sistema(0, (0, 0), t)
        self.sistema(90, (1, 1), t)
        self.sistema(180, (0, 2), t)
        self.sistema(270, (-1, 1), t)
        self.plot("Mosaiquito")


class Vitalis(Ifs):
    """Quesque se parece al señor Vitalis de Remi."""

    def __init__(self):
        super(Vitalis, self).__init__()
        self.sistema(I, (0, 1), 1./3)
        self.sistema(I, (0, 2), 1./3)
        self.sistema(I, (1, 2), 1./3)
        self.sistema(I, (2, 0), 1./3)
        self.sistema(I, (2, 1), 1./3)
        self.plot("Vitalis")


class Mosaiquito2(Ifs):
    """Mosaiquito sin rotaciones."""

    def __init__(self):
        super(Mosaiquito2, self).__init__()
        # self.sistema(I,(0,0),1./3)
        t = 5./12
        self.sistema(I, (0, 1), t)
        self.sistema(I, (1, 0), t)
        self.sistema(I, (1, 2), t)
        self.sistema(I, (2, 1), t)
        self.plot("Mosaiquito2")


BarnsleyInternet()
Sierpinski()
Barnsley()
Devaney()
Arbol()
Pitagoras()
Koch1()
Koch2()
Hexagonos()
Carpeta()
# AntiCarpeta()
Atari()
Mosaiquito()
Vitalis()
Mosaiquito2()
