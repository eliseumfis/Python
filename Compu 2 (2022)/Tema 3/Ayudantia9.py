#ayudantia 8
import numpy as np
from scipy import interpolate
import pylab as pl
#a
velocity = np.loadtxt('datos.txt', float, usecols=0)
time = np.loadtxt('datos.txt', float, usecols=1)

f_v = interpolate.interp1d(time, velocity, kind='cubic')
times = range(2, 16)
acceleration = []
h = 0.01

for t in times:
    array_x = np.array([t-h, t, t+h])
    array_y = f_v(array_x)
    ac = np.gradient(array_y, h)[1]
    acceleration.append(ac)
print('Accelerations from the time 2[s] to 15[s] is:', acceleration)

#b plotear velocidad y aceleracion, velocidades discretas

f_ac = interpolate.interp1d(times, acceleration, kind='cubic')
Coef = np.polyfit(time, velocity, 1)
ajuste_lineal = np.poly1d(Coef)
timess = np.linspace(2, 15, 100)
pl.subplot(1, 2, 1)

pl.plot(times, f_v(times), label='velocidad')
pl.plot(times, f_ac(times), label='aceleracion')
pl.grid()
pl.legend()
pl.subplot(1, 2, 2)
pl.grid()
pl.scatter(times, f_v(times), label='velocidades discretas')
pl.plot(times, ajuste_lineal(times), label='Ajuste lineal')
pl.legend()
pl.show()