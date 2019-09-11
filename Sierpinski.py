import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def sierpinski(triangulo):
    "toma un triángulo y devuelve 3"
    a, b, c = triangulo
    ab = (a+b)/2
    ca = (c+a)/2
    bc = (b+c)/2
    return ((a, ab, ca),
            (ab, b, bc),
            (ca, bc, c))


def sierpinski2(triangulo):
    "toma un triángulo y devuelve 3, torcido"
    a, b, c = triangulo
    pc = .01
    ri = np.random.randint(3, size=3)
    rn = np.random.rand(3)
    r = triangulo[ri[0]]*pc*rn[0]
    ab = (a+b)/2+r
    r = triangulo[ri[1]]*pc*rn[1]
    ca = (c+a)/2+r
    r = triangulo[ri[2]]*pc*rn[2]
    bc = (b+c)/2+r

    return (np.array((a, ab, ca)),
            np.array((ab, b, bc)),
            np.array((ca, bc, c)))


s = [(np.array([0, 0]),
      np.array([1, 0]),
      np.array([.5, .866]),
      )]

iteraciones = 6
for _ in range(iteraciones):
    nuevo_s = []
    for triangulo in s:
        nuevo_s.extend(sierpinski(triangulo))
    s = nuevo_s

f, ax = plt.subplots(1)
for t in s:
    ax.add_patch(Polygon(t))
plt.show()
