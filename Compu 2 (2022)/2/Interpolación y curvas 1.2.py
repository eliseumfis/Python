from numpy import *
from scipy import integrate as inte
from scipy.interpolate import interp2d
from pylab import *

#1) La presión atmosférica y la temperatura varían de la siguiente forma en la altura. Usando la ecuación del gas ideal p=ro*R*T , donde R es la 
# cte específica de los gases para el aire seco. 
# Calcule la densidad (ro) y realice un plot de DENSIDAD v/s ALTURA. Luego determine el valor de la densidad a 5.3 [km] de altura.

h=array([0,2,4,6,7,8,9,10,11])
T=array([288.5,280.2,277.4,273.2,269.3,260.4,257.3,250.2,245.1])
P=array([1026.24,803,605,400,350,300,250,200,150])

#Densidad=(P*100)/(287.09*T)

#hh=arange(0,11.1,0.1)
#fden=poly1d(polyfit(h,Densidad,8))
#Densidad_hh=fden(hh)
#Densidad_53=fden(5.3)

#plot(Densidad_hh,hh,"-k",Densidad_53,5.3,"*r",markersize=9)
#xlabel("Densidad [kg/m3]")
#ylabel("Altura [km]")
#legend()
#show()

# 2) INTERPOLACIÓN 2D

x=linspace(0,4,13)
y=array([0,2,3,3.5,3.75,3.875,3.9375,4])
X,Y=meshgrid(x,y)
print(X)
print(Y)
