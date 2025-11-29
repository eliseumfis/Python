from numpy import *
from pylab import*
from scipy.interpolate.interpolate import interp2d
from scipy.interpolate.interpolate import interp1d


#1)

#En el archivo temp_pressure_PP2.txt se encuentran tres columnas de datos atmosféricos: la primera
#corresponde a mediciones de altura en [km], la segunda corresponde a mediciones de temperatura en [K], y
#la tercera corresponde a mediciones de presión en [Pa]. Asuma los datos como exactos (¡como si no tuvieran
#error experimental!).
#Ahora, existe una propiedad llamada temperatura potencial, la cual denotaremos por "θ". Esta propiedad
#depende tanto de la temperatura como de la presión: θ(T, P) = T*(P/P_0)**(R/cp)

p_0=100000
R=8.31
cp=2.91
h=loadtxt("temp_pressure_PP2.txt",float,usecols=0)
t=loadtxt("temp_pressure_PP2.txt",float,usecols=1)
p=loadtxt("temp_pressure_PP2.txt",float,usecols=2)

#a) Calcular cuál será el valor de la temperatura potencial θ a 2.2 [km] y a 5.8 [km] de altura.

def TP(p, t):
    o = t*((p/p_0)**(R/cp))
    return o

temp_potenciales = TP(p, t)
TP_Func = interp1d(h, temp_potenciales, kind='cubic')

print('Temperatura potencial a altura de 2.2 km: ', TP_Func(2.2), ' [K]')
print('Temperatura potencial a altura de 5.8 km: ', TP_Func(5.8), ' [K]')

#b) Elaborar un gráfico continuo (¡no de puntos discretos!) que muestre cómo varía la temperatura




