import numpy as np
from scipy.optimize import fsolve
import math as mt
import pylab as pl


# 1)
print("1)")
print("  ")
print("    a)")

#Ecuaciones encontradas
# 3V1/R - V2-R - V3/R = V+/R
# -V1/R + 4V2/R - V3/R - V4/R = V+/R
# -V1/R - V2/R + 4V3/R - V4/R = 0
# -V2/R - V3/R + 3V4/R = 0

#Constantes
R=5.0#[ohm]
Vplus=5.0#[V]

#Definir matriz de coeficientes

A=np.array([[3/R,-1/R,-1/R,0],[-1/R,4/R,-1/R,-1/R],[-1/R,-1/R,4/R,-1/R],[0,-1/R,-1/R,3/R]],float)

#Definir variables de valores

V=np.array([Vplus/R,Vplus/R,0,0],float)

sol=np.linalg.solve(A,V)
for i in np.arange(0,4,1):
    print("    El valor de V",i+1,"es =",sol[i])

print("    b)")


#para comprobar haremos
F = np.dot(A,sol)
print("    ",V)
print("    ",F)




#2)

#x=f


#definir funcion conre variable dependiente de f

solu=[]
for re in np.arange(3,8+0.001,0.001):
    def g(x):
        return (2*np.log10(0.001/3.7 + 2.51/re*np.sqrt(x)) + 1/np.sqrt(x))
    solucion=fsolve(g,0.001)
    solu.append(solucion[0])

ree=np.linspace(3,8,np.size(solu))

pl.plot(ree,g(solu),color="blue")
pl.grid()
pl.title("Soluciones")
pl.ylabel("g(f)")
pl.xlabel("re")
# ploteo de soluciones en el arreglo solu
for h in solu:
    pl.plot(h,g(h),"*r")
pl.show()







