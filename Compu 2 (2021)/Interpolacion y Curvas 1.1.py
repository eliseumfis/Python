from numpy import *
from scipy import integrate as inte
from pylab import *

x=loadtxt("mediciones.txt",float,usecols=0)
y=loadtxt("mediciones.txt",float,usecols=1)

scatter(x,y)

#INTERPOLACIÓN

lista_coef=polyfit(x,y,6)

p=poly1d(lista_coef)

x1=x[0]
xf=x[-1]
x_poblada=linspace(x1,xf,100)

#plot(x_poblada,p(x_poblada))
#show()

#AJUSTE DE CURVAS

p1=poly1d(polyfit(x,y,1))
plot(x_poblada,p1(x_poblada),color="red",label="Polinomia grado 1")

p2=poly1d(polyfit(x,y,2))
plot(x_poblada,p2(x_poblada),color="green",label="Polinomio grado 2")

p3=poly1d(polyfit(x,y,3))
plot(x_poblada,p3(x_poblada),color="blue",label="Polinomio grado 3")

legend()
show()