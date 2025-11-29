from numpy import *
#Calcular x para t=0.6
v=5
t=0.6
g=9.8
x=v*t-0.5*g*t**2
print (x)
#Calcular x para t=[1-10]
t=arange(1,11,1)
x=v*t-0.5*g*t**2
print(x)
#Graficar resultados
from pylab import *
plot(t,x)
xlabel("Tiempo")
ylabel("Posición")
title("Posición en función del tiempo")
show()