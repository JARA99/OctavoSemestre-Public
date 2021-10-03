#   MAIN

#   Packages
import random as random
import numpy as np

f = input("Cantidad de variables [filas]: ")
c = input("Cantidad de datos [columnas]: ")
A = input("Amplitud máxima: ")

fila = []

def rnd():
    return np.power(int(A),random.random())

for i in range(int(c)):
    for j in range(int(f)):
        fila.append(rnd())
        # print(rnd())
    print(*fila)
    fila = []