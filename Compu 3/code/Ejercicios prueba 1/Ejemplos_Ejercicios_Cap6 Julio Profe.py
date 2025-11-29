#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 18:34:01 2021

@author: julioc
"""

# Ejemplos y ejercicios de Capítulo 6 de Newman
# Usando numpy
import numpy as np

A = np.array([[0,1,4,1],[3,4,-1,-1],[1,-4,1,5],[2,-2,1,3]], float)
B = np.array([-4, 3, 9, 7], float)

A = np.array([[4,-1,-1,-1],[-1,3,0,-1],[-1,0,3,-1],[-1,-1,-1,4]], float)
B = np.array([5, 0, 5, 0], float)

C = np.linalg.solve(A, B)
print(C)

# Usando scipy
from scipy import linalg

D = linalg.solve(A, B)
print(D)

#### Probar que solución es verdadera ######
F = np.dot(A, C)
print(B)
print(F)

#G = np.allclose(np.dot(A, C), D)
#print(G)






#%%
########### Ejercicio ###############
#### Una pizzería vende 20 pizzas y 10 lasañas en un día por un total de 350 mil pesos. El siguiente día 
### la pizzería vende 17 pizzas y 22 lasañas por un total de 500 mil pesos. Si el precio de las pizzas 
### y lasañas se mantuvo constante. Cuál es el valor de una pizza y una lasaña??

import numpy as np

A = np.array([[20, 10], [17, 22]]) 
B = np.array([350000, 500000])
C = np.linalg.solve(A, B)

print("El precio de la pizza = ", C[0], "pesos")
print("El precio de la lasaña = ", C[1], "pesos")

#### Probar que solución es verdadera ######
F = np.dot(A, C) 
print(B) 
print(F)
















#%%
# Ejercicio 6.1
import numpy as np

A = np.array([[4, -1, -1, -1], [-1, 3, 0, -1], [-1, 0, 3, -1], [-1, -1, -1, 4]]) 
B = np.array([5, 0, 5, 0])

C = np.linalg.solve(A, B)
print("Los voltajes son: ", C)
F = np.dot(A, C) 
print(B)
print(F)

AI = np.linalg.inv(A)
print("La inversa de A = ", AI)

print(np.dot(A,AI))

II= np.identity(4)

print(np.linalg.solve(A, II))










#%%
# Exercise 6.5 in Newman. Resuelva el siguiente problema de circuitos. 
# El voltaje varía con el tiempo de forma sinusoidal V+=x+exp(iwt), con x+ siendo una cte. 
# La corriente a través del capacitor puede calcularse usando la ley del capacitor Q = CV: I = CdV/dt.
# a) Asuma que los voltages en los ptos 1, 2 y 3 tienen la forma: 
    # V1 = x1exp(iwt), V2 = x2exp(iwt) and V3 = x3exp(iwt). Aplique la Ley de Kirchoff en cada 
    # uno de los nodos junto con la ley de Ohm y la de los capacitores y obtenga las 3 ecs. para los nodos. 
    # Como referencia le damos la ec. que se obtienen para el nodo 1:

#(1/R1 + 1/R4 + iwC1)x1 - iwC1x2 = x+/R1

#-iwC1x1 + (1/R2 + 1/R5 + iwC1 + iwC2)x2 - iwC2X3 = x+/R2

#-iwC2x2 + (1/R3 + 1/R6 + iwC2)X3 = x+/R3 

#b) Escriba un programa que resuelva para x1,x2 y x3 usando los valores
#R1 = R3 = R5 = 1KO
#R2 = R4 = R6 = 2kO
#C1 = 1mF; C2 = 0.5mF
#x+ = 3V; w = 1000s^-1

# Function solve works with either real or complex arguments

from numpy.linalg import solve
from numpy import array
import cmath as cmt

# Define ctes
R1 = R3 = R5 = 1000; R2 = R4 = R6 = 2000; 
C1 = 1.0*10**-6; 
C2 = 0.5*10**-6
xmas = 3.0; omega = 1000.0

#(1/R1 + 1/R4 + iwC1)x1 - iwC1x2 = x+/R1
# -iwC1x1 + (1/R2 + 1/R5 + iwC1 + iwC2)x2 - iwC2X3 = x+/R2
#-iwC2x2 + (1/R3 + 1/R6 + iwC2)X3 = x+/R3 

A1 = array([[1.0/R1 + 1/R4, 0, 0], [0, 1.0/R2 + 1.0/R5, 0],
            [0, 0, 1.0/R3 + 1.0/R6]],float)
A2 = array([[omega*C1, -C1*omega,0],
            [-omega*C1, omega*C1+omega*C2, -omega*C2],
            [0,-omega*C2, omega*C2]],float)

A = A1 + 1j*A2

v1 = array([xmas/R1, xmas/R2, xmas/R3],float)
#v2 = array([xmas/R2,xmas/R2,xmas/R2],float)
#v = v1 + 1j*v2

xx = solve(A,v1)
print(xx)

################################################
######## Imprimir las amplitudes y fases de los 3 voltajes 
###################################################

for ii in range(3):
    r,phase = cmt.polar(xx[ii])
    print("La amplitud de V",str(ii+1),"= ", r,"volts")
    print("La fase de V",str(ii+1),"= ", np.degrees(phase),"º")
    print()




#%%
# ####### Imprimir voltaje a los 10 seconds #######
# V1 = xx[0].real*np.cos(omega*10)
# print("El voltaje en nodo 1 a los 10 segundos = ", V1, "volts")

# print()

# V2 = xx[1].real*np.cos(omega*10)
# print("El voltaje en nodo 2 a los 10 segundos = ", V2, "volts")

# print()

# V3 = xx[2].real*np.cos(omega*10)
# print("El voltaje en nodo 3 a los 10 segundos = ", V3, "volts")


#%%

from numpy.linalg import inv

X1 = inv(A1)

X2 = solve(A1,)

#%%
# Ejemplos
#

import numpy as np
from numpy.linalg import inv

A = np.arange(1,17).reshape(4,4)
# Opción 1
X1 = inv(A1)
print(X1)

print()

# Opción 2
X2 = np.linalg.solve(A1, np.identity(3))
print(X2)






#%%

A = np.array([[1,2,3],[22,32,42],[55,66,100]])
v = np.array([1,2,3])

X1 = np.linalg.solve(A,v)
print('X = ',X1)

X2 = np.dot(inv(A),v)
print('X = ',X2)

# print ('Residual = ', np.dot(A, X) - v)






#%%

A = np.array([[4,-2,1],[3,6,-4],[2,1,8]])
AI = np.linalg.inv(A)

print(AI)
print()

print ('Id1 = ', np.dot(np.linalg.inv(A), A))
print ('Id2 = ', np.dot(A, np.linalg.inv(A)))







#%%
# Ejemplo de resolución de sistema de ecs. lineales usando solve e inv
A = np.array([[4, -1, -1, -1], [-1, 3, 0, -1], [-1, 0, 3, -1], [-1, -1, -1, 4]]) 
B = np.array([5, 0, 5, 0])

# Método 1
C = np.linalg.solve(A, B)
print('C = ', C)
print()
# Método 2
D = np.linalg.inv(A).dot(B)
print('D = ', D)



























#%%
import numpy as np
import matplotlib.pyplot as plt

def plot_vect(x, b, xlim, ylim):
    plt.clf()
    plt.quiver(0,0,x[0],x[1],\
        color='k',angles='xy',\
        scale_units='xy',scale=1,\
        label='Vector Original')
    plt.quiver(0,0,b[0],b[1],\
        color='g',angles='xy',\
        scale_units='xy',scale=1,\
        label ='Vector Transformado')
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()

# Caso de vector no-propio
A = np.array([[2, 0],[0, 1]])
x = np.array([[1],[1]])
b = np.dot(A, x)
plot_vect(x,b,(0,3),(0,2))

## Caso de vector propio
#x = np.array([[1], [0]])
#b = np.dot(A, x)
#plot_vect(x,b,(0,3),(-0.5,0.5))

####### 6 Abril 2021 #######
#%%
import numpy as np

A = np.array([[1,2],[2,1]], float)

#x, V = np.linalg.eigh(A)
x, V = np.linalg.eig(A)
print('Los auovalores son ', x)
print('Los auovectores son ', V)

x1 = np.linalg.eigvalsh(A)
print('Los auovalores son ', x1)

# Comprobar resultados
B = A.dot(V[:,0])
print('Producto AV[:,0] = ', B)

C = V[:, 0]*x[0]
print('Producto Lambda V[:,0] = ', C)






#%%
import numpy as np

x = 1.0
for ii in range(10):
    x = 2 - np.exp(-x)
    print(x)

print()





























#%%
ii = 1
x1 = 1.0; x0 = 0.1
Er = abs(x1 - x0)
while (Er > 10**-5):
    x0 = x1
    x1 = 2 - np.exp(-x0)
        
    Er = abs(x1 - x0)
    ii += 1
    
    print("Solución x1 = ", x1)
    print("Diferencia entre iteraciones = ", Er)
    print("Iteración No. ", ii)
    print()








#%%
x = 0.2
for ii in range(15):
#    x = np.exp(1 - x**2)
    x = np.sqrt(1 - np.log(x))
    print(x)








