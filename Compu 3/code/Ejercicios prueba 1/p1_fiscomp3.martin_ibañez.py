#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 14:30:24 2023

@author: Ibanezmartin
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
# (1)
#  itotal = suma de i individuales, tres ecuaciones para tres nodos

# definicion de constantes
r1= 2500 #[ohms]
r2= 3200
r3= 2000
r4= 1500
r5= 5000
vm= 7 # [v]

# arreglo con coeficientes de los voltajes

v=np.array([[1/r1 + 1/r4 + 1/r2,-1/r4,0],[-1/r4, 1/r2 + 1/r4 + 1/r1 + 1/r3, -1/r1],[0,-1/r1,1/r3 + 1/r1 + 1/r5]],float)

# arreglo con coef no variables
s= np.array([vm/r1,vm/r2,vm/r3],float)
#
x=np.linalg.solve(v,s)
#print(x)
for i in range(0,3):
    print("el valor del voltaje v",i+1,"es ",x[i])
# verificacion del resultado
b=np.dot(v,x)
print("la matriz de coef invididuales es ",b)
# error de calculo para verificar 
print("el error del calculo sobre la matriz es",abs(b-s))

# (2)

#(a) definir polinomio
def p(x):
   return 924*x**6 - 2772*x**5 +3150*x**4 -1680*x**3 +420*x**2 - 42*x + 1

# creacion de rango variable para buscar soluciones
solu=[]
for ii in np.arange(0,1.2,0.2):
    ar= ii
    ar2=ii+0.2
    solucion=fsolve(p,[ar,ar2])
    solu.append(solucion[0])

print()
print("las raices del polinomio en el intervalo [0,1] son",solu)

#  (b) grafica

# ploteo de soluciones en el arreglo solu
for h in solu:
    plt.plot(h,p(h),"*")
    
r=np.arange(0,1,0.001)
plt.plot(r,p(r))
plt.xlabel("x")
plt.ylabel("p(x)")
plt.title("grafica de p(x) sobre intervalo [0,1]")
plt.grid()
plt.show()
