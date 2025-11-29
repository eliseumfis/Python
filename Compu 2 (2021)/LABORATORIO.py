from numpy import sqrt, linspace, array, loadtxt, exp, pi
from scipy.integrate import quadrature, romberg
from scipy.interpolate import interp1d
from matplotlib import pyplot as pl


#EJERCICIO 4:

print('EJERCICIO 4:')
print(' ')
print(' ')

#Parto importando los datos segun corresponda:

altura = loadtxt('temp_pressure_PP2.txt', float, usecols=0)
temp = loadtxt('temp_pressure_PP2.txt', float, usecols=1)
presion = loadtxt('temp_pressure_PP2.txt', float, usecols=2)

#Definimos la funcion de temperatura potencial con las constantes
#correspondientes:

def TP(presion, temp):
    o = temp*((presion/100000)**(8.31/2.91))
    return o

#El ejercicio nos pide encontrar valores de temperatura potencial que
#no existen explicitamente en el archivo de texto, por lo que primero
#tendre que calcular las temperaturas potenciales para los valores
#conocidos de altura y luego interpolarlos con un spline, y asi obtener
#los valores desconocidos:

temp_potenciales = TP(presion, temp)

#Utilizo spline cubico para interpolar, porque ofrece mejores aproximaciones:

TP_Func = interp1d(altura, temp_potenciales, kind='cubic')

#Ahora puedo conocer los valores de temperatura potencial para:

print('Temperatura potencial a altura de 2.2 km: ', TP_Func(2.2), ' [K]')
print('Temperatura potencial a altura de 5.8 km: ', TP_Func(5.8), ' [K]')
print(' ')
print('(Grafico de variacion de temperatura potencial versus altura mostrado)')
print(' ')

#Ahora solo falta plotear altura vs. temperatura potencial. Lo hare con
#un linspace entre la altura menor y la mayor, para asi tener varias
#subdivisiones entre dichos limites, y por ende, una curva mas suave:

altura_suave = linspace(altura[0], altura[-1], 150)

pl.plot(altura_suave, TP_Func(altura_suave))
pl.title('Temperatura Potencial en funcion de Altura')
pl.xlabel('Altura [km]')
pl.ylabel('Temperatura Potencial [K]')
pl.show()