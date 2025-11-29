import numpy as np
from scipy.optimize import fsolve
import pylab as pl

#1) 




#Constantes
R1=2500 #[ohm]
R2=3200
R3=2000
R4=1500
R5=5000
V=7

A=np.array([[-1/R4, 1/R1 + 1/R2 + 1/R4,0],[1/R1 + 1/R2 + 1/R3 + 1/R4,-1/R4,-1/R1],[-1/R1,0,1/R1 + 1/R5 + 1/R3]],float)
B=np.array([V/R2,V/R1,V/R3])
#print(A)
#print(B)

sol=np.linalg.solve(A,B)
for i in np.arange(0,3,1):
    print("V",i+1,"=",sol[i])

#para comprobar haremos
#F = np.dot(A,sol)
#print(B)
#print(F)


#2)

def P(x):
    return 924*x**6 -2772*x**5 + 3150*x**4 - 1680*x**3 + 420*x**2 - 42*x +1

soluciones=[]

for i in np.arange(0,1.2,0.2):
    argumento=i
    argumento2=i+0.2
    solu=fsolve(P,[argumento,argumento2])
    soluciones.append(solu[0])


print()
print("Las 6 soluciones son:",soluciones)

x_pob=np.linspace(0,1,10000)

pl.plot(x_pob,P(x_pob),color="blue")
pl.grid()
pl.title("Soluciones")
pl.ylabel("P(x)")
pl.xlabel("X")
# ploteo de soluciones en el arreglo solu
for h in soluciones:
    pl.plot(h,P(h),"*r")
pl.show()
