from numpy import loadtxt, array, gradient, linspace, polyfit, poly1d
from scipy import interpolate
from matplotlib import pyplot as pl

velocidades = loadtxt('datos.txt', float, usecols=0)
tiempos = loadtxt('datos.txt', float, usecols=1)

func_velocidad = interpolate.interp1d(tiempos, velocidades, kind='cubic')
tiempos_de_interes = range(2, 16)

aceleraciones = []

h = 0.01

for t in tiempos_de_interes:
    array_x = array([t-h, t, t+h])
    array_y = func_velocidad(array_x)
    derivada = gradient(array_y, h)[1]
    aceleraciones.append(derivada)

print('Aceleraciones desde 2[s] hasta 15[s]:', aceleraciones)