#Graficar móvil en funcion del tiempo

from numpy import *
t=range(1,21)
tf=[]

for n in t:
    y=5+3*n
    tf.append(y)

print(tf)

from pylab import *
plot(t,tf)
xlabel="Tiempo"
ylabel="Posicion"
title("Chota")
show()