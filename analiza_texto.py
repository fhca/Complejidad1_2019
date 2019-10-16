import numpy as np
import matplotlib.pyplot as plt
import re


with open("L1piedra.txt", "r") as fp:
    lineas = fp.readlines()

listota = []
separadores = re.compile("[^a-zA-ZáéíóúñÑüÜÁÉÍÓÚ]+")
separadores_inicio = re.compile("^[^a-zA-ZáéíóúñÑüÜÁÉÍÓÚ]+")
separadores_final = re.compile("[^a-zA-ZáéíóúñÑüÜÁÉÍÓÚ]+$")
for p in lineas:
    p1 = p[:-1].lower()
    p15 = separadores_inicio.sub("", p1)
    p16 = separadores_final.sub("", p15)
    p2 = separadores.split(p16)
    listota.extend(p2)

frecuencia = dict()
for p in listota:
    frecuencia[p] = frecuencia.get(p, 0) + 1

palabras_ord = sorted(frecuencia, key=frecuencia.__getitem__, reverse=True)
frecuencias_ord = [frecuencia[p] for p in palabras_ord]

print("graficando...")
x = range(len(palabras_ord))
plt.plot(x, frecuencias_ord)
plt.xscale('log')
plt.yscale('log')
plt.show()
