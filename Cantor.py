import matplotlib.pyplot as plt


def cantor(a, b, p):
    return (a, a*(1-p)+p*b), (a*p+(1-p)*b, b)


p = 1/3
s = [(0, 1)]
iteraciones = 2
for _ in range(iteraciones):
    nuevo_s = []
    for segmento in s:
        nuevo_s.extend(cantor(*segmento, p))
    s = nuevo_s

coords_y = (0, 0)
for coords_x in s:
    plt.plot(coords_x, coords_y)
plt.show()
