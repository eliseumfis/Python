import numpy as np
from scipy import integrate,interpolate
import pylab as pl

#1)


def T(x):
    def f(t):
        return t**(x-1)*np.exp(-t)
    return integrate.quadrature(f,0,100)[0]
h=0.5
array_x=np.arange(0,5.5,h)
array_y=[]
for k in array_x:
    array_y.append(T(k+1))
dx=np.gradient(array_y,h)

pl.plot(array_x,array_y,"-r",label="f(x)")
pl.plot(array_x,dx,"-b",label="f'(x)")
pl.xlabel("x");pl.ylabel("y")
pl.grid()
pl.legend()
pl.show()

#2)

semana=np.array([1,3,5,7,9,11,13])
altura=np.array([22,51,127,202,227,248,252])

coef1=np.polyfit(semana,altura,1)
funcion_altura1=np.poly1d(coef1)
print("La altura aproximada en la semana 6 por polinimio de grado 1 es:",funcion_altura1(6))

coef2=np.polyfit(semana,altura,2)
funcion_altura2=np.poly1d(coef2)
print("La altura aproximada en la semana 6 por polinimio de grado 2 es:",funcion_altura2(6))

coef3=np.polyfit(semana,altura,3)
funcion_altura3=np.poly1d(coef3)
print("La altura aproximada en la semana 6 por polinimio de grado 3 es:",funcion_altura3(6))


pl.subplot(2,2,1)

pl.plot(semana,altura,".r",label="Datos discretos")
pl.xlabel("Semanas");pl.ylabel("Altura [cm]")
pl.legend()
pl.grid()


pl.subplot(2,2,2)
pl.plot(np.linspace(1,13,50),funcion_altura1(np.linspace(1,13,50)),"-g",label="Polinomio grado 1")
pl.xlabel("Semanas");pl.ylabel("Altura [cm]")
pl.legend()
pl.grid()



pl.subplot(2,2,3)
pl.plot(np.linspace(1,13,50),funcion_altura2(np.linspace(1,13,50)),"-b",label="Polinomio grado 2")
pl.xlabel("Semanas");pl.ylabel("Altura [cm]")
pl.legend()
pl.grid()


pl.subplot(2,2,4)
pl.plot(np.linspace(1,13,50),funcion_altura3(np.linspace(1,13,50)),"-r",label="Polinomio grado 3")
pl.xlabel("Semanas");pl.ylabel("Altura [cm]")
pl.legend()
pl.grid()

pl.show()
