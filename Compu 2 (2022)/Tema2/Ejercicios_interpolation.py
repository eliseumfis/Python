#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 09:29:28 2021

@author: julioc
"""

######## Ejemplos y ejercicios de polinomios y ajuste de curvas ############
# Ejemplo 1: Interpolación spline lineal

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 10); y = np.sin(x)
xvals = np.linspace(0, 2*np.pi, 20)

yinterp = np.interp(xvals, x, y)

plt.clf(); plt.plot(x,y,'o'); plt.plot(xvals,yinterp, '-b')
plt.xlabel('x'); plt.ylabel('Sin(x)')
plt.axhline(y=0, xmin=0, xmax=2*np.pi, color='k')







#%%
##### Ejemplo 2: Interpolación spline lineal y cúbico

from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 11)
y = np.cos(-x**2/9.0); xnew = np.linspace(0, 10, 21)
xnew1 = np.linspace(0, 10, 100)

y1 = np.cos(-xnew1**2/9.0)

f = interp1d(x, y)
f2 = interp1d(x, y, kind='cubic')

plt.clf()
plt.plot(x, y, 'or', xnew, f(xnew), '-r', xnew, f2(xnew), '--g')
plt.plot(xnew1, y1, '-k')
plt.axhline(y=0, xmin=0, xmax=10, color='k')
plt.xlabel('X')
plt.ylabel(r'cos(-$x^{2}/9$)')
plt.legend(['data', 'linear', 'cubic', 'f(x)'], loc=3)



#%%
from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt

H = np.array([0,2,4,6,7,8,9, 10,11])
T = np.array([288.5, 280.2, 277.4, 273.2, 269.3, 260.4, 257.3, 250.2, 245.1])
P = np.array([1026.24, 803, 605, 400, 350, 300, 250, 200, 150])

R = 287.05
dens = P*100/(R*T)
HH = np.arange(0, 11.1, 0.1)

f = interp1d(H, dens, 'cubic')

print("La densidad a 5.3 km = ", f(5.3), " kg/m3")

plt.clf()
plt.plot(dens, H, 'or', f(HH), HH, '-k', f(5.3), 5.3, '*b')
plt.ylabel('Altura [km]')
plt.xlabel("Densidad (kg/m3)")




















#%%

from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

H = np.array([0,2,4,6,7,8,9, 10,11])
T = np.array([288.5, 280.2, 277.4, 273.2, 269.3, 260.4, 257.3, 250.2, 245.1])
P = np.array([1026.24, 803, 605, 400, 350, 300, 250, 200, 150])

densidad = P*100/(287.09*T)

HH = np.arange(0, 11.1, 0.1)
fden = interp1d(H, densidad, kind='cubic')

dens_HH = fden(HH)
dens_53 = fden(5.3)

# Usando where
#ind = np.where((HH > 5.2) & (HH < 5.4))[0]

#print("El valor de densidad en 5.3 km = ", dens_HH[ind][0], 'kg/m3')
print("El valor de densidad en 5.3 km = ", dens_53, 'kg/m3')

plt.clf()
plt.plot(dens_HH, HH, '-k', dens_53, 5.3, '*r', markersize=9)
plt.xlabel('Densidad [kg/m3]')
plt.ylabel('Altura [km]')









#%%
import numpy as np
from scipy.interpolate import interp2d
import matplotlib.pyplot as plt

x = np.linspace(0, 4, 13)
y = np.array([0, 2, 3, 3.5, 3.75, 3.875, 3.9375, 4])
X, Y = np.meshgrid(x, y)
Z = np.sin(np.pi*X/2)*np.exp(Y/2)

x2 = np.linspace(0, 4, 65)
y2 = np.linspace(0, 4, 65)
f = interp2d(x, y, Z, kind='cubic')
Z2 = f(x2, y2)


X2, Y2 = np.meshgrid(x2, y2)

cont1 = np.arange(-7.5, 8.0, 0.5)

plt.clf()

plt.subplot(1,2,1)
CS = plt.contourf(X, Y, Z, cont1, cmap=plt.cm.jet)
plt.colorbar(CS, orientation='horizontal')
plt.title('Datos originales')
plt.xlabel('X')
plt.ylabel('Y')
plt.tight_layout()    

plt.subplot(1,2,2)
CS = plt.contourf(X2, Y2, Z2, cont1, cmap=plt.cm.jet)
plt.colorbar(CS, orientation='horizontal')
plt.title('Datos interpolados')
plt.xlabel('X-Interpolado')
plt.ylabel('Y-Interpolado')    
plt.tight_layout()









#%%
##############################################################################
###### Ejercicio 5.4 Newman #########
import numpy as np
import matplotlib.pyplot as plt
#import scipy.integrate as inte

def J(m,x):
    
    def f(x, m, theta):
        return np.cos(m*theta - x*np.sin(theta))

    
    ##### Simpson Method ##########
    theta1 = 0; theta2 = np.pi; N = 1000; h = (theta2 - theta1)/N
    
    simp = h/3*(f(x,m,theta1) + f(x,m,theta2)); simp1 = 0; simp2 = 0;
    
    for k in np.arange(1,N,2):
        simp1 += h/3*(4*f(x,m,theta1+k*h))
    
    for j in np.arange(2,N,2):
        simp2 += h/3*(2*f(x,m,theta1+j*h))
    
    simp_t = simp + simp1 + simp2
    
    return 1/np.pi*simp_t

J0 = []; J1 = []; J2 = [];

for ii in np.arange(0,21,0.2):
    
    J0.append(J(0,ii))
    J1.append(J(1,ii))
    J2.append(J(2,ii))

### Plots ######
plt.clf()   
plt.plot(np.arange(0,21,0.2), J0, '-k', np.arange(0,21,0.2), J1, '-b', \
         np.arange(0,21,0.2), J2, '-r')
plt.axhline(y=0, xmin=0, xmax=20, color='k')
plt.ylabel('Bessel Functions'); plt.xlabel('X')
plt.legend(('J0','J1','J2'), loc=1)


#%%
# Los datos y =0.7, -2.925, -7.8, -13.25, -18.3, -21.675, -21.8, -16.8,
# -4.5, 17.575 se tomaron para valores de x =1., 1.5, 2., 2.5, 3., 3.5,
# 4., 4.5, 5., 5.5. Cuál es el polinomio de grado 1 a 3 que mejor
# interpola estos datos? Cuál es la expresión de este polinomio?

from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

y = np.array([0.7, -2.925, -7.8, -13.25, -18.3, -21.675, -21.8, -16.8, -4.5, 17.575], float)
x = np.arange(1.0, 6.0, 0.5) 

xx = np.linspace(1.0, 5.5, 100)

f = interp1d(x, y)
f2 = interp1d(x, y, 2)
f3 = interp1d(x, y, 3)

plt.clf()
plt.plot(x, y, 'ok', xx, f(xx), '-k', xx, f2(xx), '-b', xx, f3(xx), '-r')
plt.axhline(y=0, xmin=0, xmax=10, color='k')
plt.xlabel('X')
plt.ylabel('Funciones Interpolación')
plt.legend(['data', 'Int-1', 'Int-2', 'Int-3'], loc=3)



    
