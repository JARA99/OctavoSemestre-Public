#-----------------------------------------------------------------------------------------#
#----------------------------------------   MAIN   ---------------------------------------#
#-----------------------------------------------------------------------------------------#
#   Author: Jorge Alejandro Rodriguez Aldana                                              #
#   Date: 09/2021                                                                         #
#   File: Main.py                                                                         #
#-----------------------------------------------------------------------------------------#


#-----------------------------------------------------------------------------------------#
#                                        Packages                                         #
#-----------------------------------------------------------------------------------------#
import random as random
import numpy as np

#-----------------------------------------------------------------------------------------#
#                                         Code                                            #
#-----------------------------------------------------------------------------------------#

# f = input("Cantidad de variables [filas]: ")
# c = input("Cantidad de datos [columnas]: ")
# A = input("Amplitud máxima: ")

f = 20
c = 10 # Para 2D, 13 para 3D
A = 10

fila = []

def rnd():
    return np.power(int(A),random.random())

for i in range(int(f)):
    for j in range(int(c)):
        # fila.append(',')
        fila.append(rnd())
        # print(rnd())
    # print(i,',')
    print(i,*fila)
    fila = []

