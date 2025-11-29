#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 11:39:45 2023

@author: julioc
"""

#### Uso de función odeint ######
### Ejemplo 1
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Función que entrega dx/dt
def model(x,t):
    dxdt = -x**3 + np.sin(t)
    return dxdt

a, b = 0.0, 10.0   # Comienzo y final del intervalo
x0 = 0.0            # Condición inicial

# N = 50
#h = (b-a)/N        # Tamaño de 1 paso
t = np.arange(a, b, 0.05)
# t = np.linspace(a,b,N)

# Resolver ODE
xp = odeint(model, x0, t)

plt.clf()
plt.plot(t, xp, '--k', label='odeint')
plt.legend(loc=3)
plt.ylabel('x(t)')
plt.xlabel('t')







#%%
# Ejercicio: Resolver ODE dy/dt = −ky para k = 0.3 entre 0 y 20 con la 
# condición inicial y (t = 0) = 5

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model(y, t):
    dydt = -0.3*y
    return dydt

a, b = 0, 20
y0 = 5
t = np.arange(a,b,0.1)

yr = odeint(model, y0, t) 

plt.clf()
plt.plot(t, yr, '-k')
plt.xlabel('t')
plt.ylabel('y(t)')













#%%
### Mismo Ejemplo, usando el tercer argumento ###

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Función que entrega dx/dt
def model(y, t, k):
#    k = 0.3
    dydt = -k*y
    return dydt

y0 = 5.0            # Condición inicial
t = np.linspace(0,20,50)
k = 0.3
# Resolver ODE
yp = odeint(model, y0, t, args=(k,))

plt.clf()
plt.plot(t, yp, '-k')
plt.ylabel('y(t)'); plt.xlabel('t')






#%%
### Ejercicio: Resolver ODE dy/dt = −ky entre 0 y 20 con condición
# inicial y(t = 0) = 5 para los siguientes valores de k = 0.1, 0.2 y 0.5. 
# Plotear las 3 soluciones en el mismo plot

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Función que entrega dx/dt
def model(y, t, k):
    dydt = -k*y
    return dydt

y0 = 5.0            # Condición inicial
t = np.linspace(0,20,50)

# Resolver ODE
k = (0.1, 0.2, 0.5)
lab_p = ('--k','-.m',':c')

plt.clf()
for kk in range(len(k)):
	yp = odeint(model, y0, t, args=(k[kk],))
	
	plt.plot(t, yp, lab_p[kk])
	
plt.ylabel('y(t)'); plt.xlabel('t')
plt.legend(('k=0.1','k=0.2','k=0.5'), loc=1)



#%%
##### ODEs de más de 1 variable #######
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Función que entrega dx/dt, dy/dt
def model(r,t):
    x = r[0]
    y = r[1]
    fx = x*y - x
    fy = y - x*y + np.sin(t)**2
    return np.array([fx,fy], float)

r0 = [1.0, 1.0]            # Condición inicial
t = np.linspace(0,10,100)

# Resolver ODE
rp = odeint(model, r0, t)

plt.clf()
plt.plot(t, rp[:,0], '-b', t, rp[:,1], '-r')
plt.ylabel('x(t) and y(t)'); plt.xlabel('t')
plt.legend(('x(t)','y(t)'), loc=1)





















#%%
##### ODEs de más de 1 variable #######
#### Ejercicio #############
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Función que entrega dx/dt
def model(r,t):
    # x = r[0]
    y = r[1]
    fx = 3*np.exp(-t)
    fy = 1 - y
    return np.array([fx,fy], float)

r0 = [0, 0]            # Condición inicial
t = np.linspace(0,10,100)

# Resolver ODE
rp = odeint(model, r0, t)

plt.clf()
plt.plot(t, rp[:,0], '-b', t, rp[:,1], '-r')
plt.ylabel('x(t) and y(t)'); plt.xlabel('t')
plt.legend(('x(t)','y(t)'), loc=4)






#%%
##### ODEs de más de 1 variable #######
#### Ejercicio 8.2: Ecs. Lotka-Volterra #############
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Función que entrega dx/dt
def model(r,t):
    alfa = 1
    beta = 0.5; ganma = 0.5
    delta = 2
    x = r[0]
    y = r[1]
    fx = alfa*x - beta*x*y
    fy = ganma*x*y - delta*y
    return np.array([fx,fy], float)

r0 = [2, 2]            # Condición inicial
t = np.linspace(0,30,200)

# Resolver ODE
rp = odeint(model, r0, t)

plt.clf()
plt.plot(t, rp[:,0], '-b', t, rp[:,1], '-r')
plt.ylabel('x(t) and y(t)'); plt.xlabel('t')
plt.legend(('x(t): presas','y(t): predadores'), loc=1)
#plt.ylim(0.5,8.5)




#%%
##### ODEs de más de 1 variable #######
#### Ejercicio 8.2: Ecs. Lotka-Volterra #############
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Función que entrega dx/dt
def model(r,t,alfa,beta,ganma,delta):
    
    x = r[0]
    y = r[1]
    fx = alfa*x - beta*x*y
    fy = ganma*x*y - delta*y
    return np.array([fx,fy], float)

r0 = [2, 2]            # Condición inicial
t = np.linspace(0,30,200)
beta = 0.5; ganma = 0.5
delta = 2

plt.clf()
jj = 1
for ii in range(2,5):
    
    # Resolver ODE
    rp = odeint(model, r0, t, args=(ii, beta, ganma, delta))
    
    plt.subplot(3,1,jj)
    plt.plot(t, rp)
    plt.ylabel('x(t) and y(t)')
    plt.title('Alfa = '+str(ii))
    plt.tight_layout()
    jj+=1
    
plt.xlabel('t')
#plt.legend(('x(t): presas','y(t): predadores'), loc=1)
#plt.ylim(0.5,8.5)






#%%
##### ODEs de más de 1 variable #######
#### Ejercicio #############
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Función que entrega dx/dt
def model(r,t):
    if t < 5:
	    u = 0
    else:
        u = 2
    x = r[0]
    y = r[1]
    fx = (-x + u)/(2-x)
    fy = (-y + x)/(y-1)
    return np.array([fx,fy], float)

r0 = [0, 0]            # Condición inicial
t = np.linspace(0, 15, 100)

# Resolver ODE
rp = odeint(model, r0, t)

plt.clf()
plt.plot(t, rp[:,0], '-b', t, rp[:,1], '-r')
plt.ylabel('x(t), y(t)'); plt.xlabel('t')
plt.legend(('x(t)', 'y(t)'), loc=2)




#%%
##### ODEs de más de 1 variable #######
#### Ejercicio #############
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Función que entrega dx/dt
def model(r,t):
    if t < 5:
        u = 0
    else:
        u = 2
    x = r[0]
    y = r[1]
    fx = (-x + u)/2
    fy = (-y + x)/5
    return np.array([fx,fy], float)

r0 = [0, 0]            # Condición inicial
N = 150
t = np.linspace(0, 15, N)
u = np.zeros(N, float)
u[51:] = 2.0

rp = odeint(model, r0, t)

plt.clf()
plt.plot(t, u, '-k', t, rp[:,0], '-b', t, rp[:,1], '-r')
plt.ylabel('x(t), y(t), u(t)'); plt.xlabel('t')
plt.legend(('u(t)','x(t)', 'y(t)'), loc=2)













#%%
####### Ecuaciones diferenciales de orden superior ########
# Ejemplo 8.6: Non-linear pendulum

# Ecs. del pendulo: mld^2(theta)/dt^2 = -mgsin(theta)
# d^2(theta)/dt^2 = -(g/l)sin(theta).
# Haciendo cambio de var. d(theta)/dt = omega, then d(omega)/dt = -(g/l)sin(theta)

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def pendulum(r, t):
    
    theta = r[0]
    omega = r[1]
    
    dthdt = omega
    domegadt = -9.81/0.1*np.sin(theta)
    
    return np.array([dthdt, domegadt], float)

t = np.arange(0, 30, 0.1)
r0 = [np.radians(179), 0]

sol = odeint(pendulum, r0, t)

plt.clf()
plt.subplot(2,1,1)
plt.plot(t, np.degrees(sol[:,0]),'orange')
plt.xlabel('t')
plt.ylabel(r'$\theta(t)$')

plt.subplot(2,1,2)
plt.plot(t, sol[:,1],'-c')
plt.xlabel('t')
plt.ylabel(r'$\omega(t)$')




#%%
####### Ecuaciones diferenciales de orden superior ########
## Ejercicio: Péndulo con fricción

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def pend(y, t, b, c):
    theta, omega = y
    dydt = [omega, -b*omega - c*np.sin(theta)]
    return dydt

b = 0.25
c = 5.0

y0 = [np.pi - 0.1, 0.0]

t = np.linspace(0, 10, 101)

sol = odeint(pend, y0, t, args=(b, c))

plt.clf()
plt.plot(t, sol[:, 0], 'b', label=r'$\theta(t)$')
plt.plot(t, sol[:, 1], 'g', label=r'$\omega(t)$')
plt.ylabel(r'$\theta(t)$ and $\omega(t)$')
plt.legend(loc='best')
plt.xlabel('t')







#%%
####### Ecuaciones diferenciales de orden superior ########
## Ejercicio: y'' + (0.9 + 0.7t)y' + Ky = 0

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def func(r, t, K):
    y = r[0]
    z = r[1]
    dydt = z
#    K = 30
    dzdt = -(0.9 + 0.7*t)*z - K*y
    return np.array([dydt, dzdt], float)

r0 = [2.0, -1]
t = np.linspace(0, 2, 100)

plt.clf()
for ii in range(5,35,5):
	sol = odeint(func, r0, t, args=(ii,))
	
	plt.plot(t, sol[:, 0], label='K='+str(ii))
#    plt.plot(t, sol[:, 1], 'r')
    
plt.ylabel('y(t)')
plt.legend()
plt.xlabel('t')




#%%
####### Ecuaciones diferenciales de orden superior ########
## Ejercicio: Oscilador armónico

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def func(r, t):
    omega = 1
    x = r[0]
    y = r[1]
    dxdt = y
    dydt = -omega**2*x
    return np.array([dxdt, dydt], float)

r0 = [[1, 0],[2, 0],[4, 0]]
t = np.linspace(0, 50, 500)

lab_p = ['-k', '-b', '-r']

plt.clf()
for ii in range(3):
	sol = odeint(func, r0[ii], t)
	
	plt.plot(t, sol[:, 0], lab_p[ii])

#plt.plot(t, sol[:, 1], 'r')
plt.ylabel('x(t)')
plt.ylim(-4,5)
plt.legend(('A=1','A=2', 'A=4'),loc=1)
plt.xlabel('t')







#%%
######### Ejercicio simplificado #########
## Ejemplo 8.8: posición vertical de bola
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

##### Primera parte ######
# Función que entrega dx/dt, dv/dt
def func(r,t):
    x = r[0]
    v = r[1]
    dxdt = v
    dvdt = -9.81
    return np.array([dxdt,dvdt], float)

N = 50
t = np.linspace(0, 10, N)

def yfinal(v0):
    sol = odeint(func, (0, v0), t)
    x = sol[:,0]
    return x[-1]

v0 = np.linspace(0,60,80)

root = fsolve(yfinal, 10)[0]
print("Valor inicial de velocidad = ", root, " m/s")

#### Comprobar que condición inicial v0 = 49 es correcta #####
sol = odeint(func, (0,root), t)

plt.clf()
plt.plot(t, sol[:,0], 'ob')
plt.plot(10, 0, 'or')
plt.ylabel('x(t)')
plt.xlabel('t')
plt.legend(('v0='+str(root)+'m/s',), loc=2)



#%%
###### Ejercicio ############
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

##### Primera parte ######
# Función que entrega dx/dt, dv/dt
def func(r,S):
    c = 8.360795454545*10**-7
    theta = r[0]
    z = r[1]
    dthds = z
#    c = 1
    dzds = -c*np.cos(theta)
    return np.array([dthds,dzds], float)

# Valor de dtheta/dS(S=600) = Kr
Kr = 0.00066937343

#z0 = 0.0011  # Suposición inicial
z0 = 1
r0 = [0, z0]            # Condición inicial
S = np.linspace(0, 600, 600)

sol = odeint(func, r0, S)

plt.clf()
plt.subplot(2,1,1)
plt.plot(S, sol[:,0], 'ok')
plt.ylabel(r'$\theta(S)$')
plt.xlabel('S')
plt.tight_layout()

plt.subplot(2,1,2)
plt.plot(S, sol[:,1], 'ok')
plt.plot(600, Kr, 'or')
plt.ylabel(r'$d\theta/dS$')
plt.xlabel('S')
plt.tight_layout()




#%%
####### Segunda parte ########
#@np.vectorize
def thetaf(z0):
    sol = odeint(func, (0, z0), S)
    return sol[-1,1] - Kr

z0 = np.linspace(0.001,0.002,500)

tf = []
for ii in z0:
    tf.append(thetaf(ii))

plt.clf()
plt.plot(z0, tf, '-b')
plt.hlines(0,0, 0.01, colors='k', lw=2)
plt.xlim(0.001, 0.002)
#plt.xlim(0, 1)








#%%
# Find roots
root = fsolve(thetaf, 0.001)[0]

print("Valor inicial de dtheta/dS = ", root)

#### Comprobar que condición inicial es correcta #####
sol = odeint(func, [0, root], S)

plt.clf()
plt.plot(S, sol[:,1], 'ob')
plt.plot(600, Kr, 'or')
#plt.legend(('v0=60m/s','v0=49m/s'), loc=2)


##%%
#from scipy import optimize
#sol = optimize.root(func, [0, 1], method='hybr')
#print(sol)





#%%
##################################################################
###### Ejercicio: ODE que gobierna deflección de una barra #######
##################################################################
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

##### Primera parte ######
# Función que entrega dx/dt, dv/dt
def func(r,x):
    w = 15000; E = 200*10**6; I = 30000*10**-8; L = 3
    y = r[0]
    z = r[1]
    dydx = z
    dzdx = (w*L*x/2 - w*x**2/2)/(E*I)
    return np.array([dydx, dzdx], float)

# Cond. frontera y(L) = 0
yL = 0
z0 = -2

r0 = [0, z0]            # Condición inicial
x = np.linspace(0, 3, 100)

sol = odeint(func, (0, z0), x)
plt.clf()
plt.plot(x,sol[:,0])

def yfunc(z0):
    sol = odeint(func, (0, z0), x)
    return sol[-1,0]

z0 = np.linspace(-30,30,5000)

yf = np.zeros(z0.size, float)
for ii in range(z0.shape[0]):
    yf[ii] = yfunc(z0[ii])
    
plt.clf()
plt.plot(z0, yf, '-b')
plt.hlines(0, -30, 30)

root = fsolve(yfunc, 0)[0]

sol = odeint(func, (0, root), x)

plt.clf()
plt.subplot(2,1,1)
plt.plot(x, sol[:,0], 'ok')
plt.plot(3, yL, 'or')
plt.ylabel('y(t)')

plt.subplot(2,1,2)
plt.plot(x, sol[:,1], 'ob')
plt.ylabel('dy(t)/dx')
plt.xlabel('X')
plt.legend(('dy/dx','yL'), loc=2)


#%%
##################################################################
###### Ejercicio: ODE que gobierna deflección de una barra #######
##################################################################
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

##### Primera parte ######
# Función que entrega dx/dt, dv/dt
def func(r,x):
    w = 15000; E = 200*10**6; I = 30000*10**-8; L = 3
    y = r[0]
    z = r[1]
    dydx = z
    dzdx = (w*L*x/2 - w*x**2/2)/(E*I)
    return np.array([dydx, dzdx], float)

# Cond. frontera y(L) = 0
yL = 0

z0 = 40  # Suposición inicial
r0 = [0, z0]            # Condición inicial
x = np.linspace(0, 3, 50)

sol = odeint(func, r0, x)

plt.clf()
plt.subplot(2,1,1)
plt.plot(x, sol[:,0], 'ok')
plt.plot(3, yL, 'or')
plt.ylabel('y(x)')
plt.xlabel('x')
plt.tight_layout()

plt.subplot(2,1,2)
plt.plot(x, sol[:,1], 'ok')
plt.ylabel(r'$dy/dx$')
plt.xlabel('x')
plt.tight_layout()




#%%
####### Segunda parte ########
#@np.vectorize
def yfunc(z0):
    sol = odeint(func, (0, z0), x)
    return sol[-1,0]

z0 = np.linspace(-40,40,200)

yf = []
for ii in z0:
    yf.append(yfunc(ii))

plt.clf()
plt.plot(z0, yf, '-b')
plt.hlines(0,-50, 40, colors='k', lw=2)
#plt.xlim(0, 0.002)








#%%
# Find roots
root = fsolve(yfunc, -10)[0]

print("Valor inicial de dy/dx = ", root)

#### Comprobar que condición inicial es correcta #####
sol = odeint(func, [0, root], x)

plt.clf()
plt.subplot(2,1,1)
plt.plot(x, sol[:,0], 'ok')
plt.plot(3, yL, 'or')
plt.ylabel('y(t)')

plt.subplot(2,1,2)
plt.plot(x, sol[:,1], 'ob')
plt.ylabel('dy(t)/dx')
plt.xlabel('X')
plt.legend(('dy/dx','yL'), loc=2)




#%%
###### ejercicio 8.3: Ecs. de Lorenz
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def Lor(r,t):
	x = r[0]; y = r[1]; z = r[2]
	fx = sigma*(y - x)
	fy = r0*x - y - x*z
	fz = x*y - b0*z
	return np.array([fx,fy,fz],float)

t = np.linspace(0.0, 50.0, 5000)
r0 = 28.0; sigma = 10.0; b0 = 8.0/3

r00 = [0, 1, 0]

# Solución de ecuaciones
sol = odeint(Lor, r00, t)

plt.clf()
plt.subplot(2,1,1)
plt.plot(t, sol[:, 0], '-k', label='x(t)')
plt.plot(t, sol[:, 1], '-b', label='y(t)')
plt.plot(t, sol[:, 2], '-r', label='z(t)')
plt.ylabel('x(t), y(t), z(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.tight_layout()

plt.subplot(2,1,2)
plt.plot(sol[:, 0], sol[:, 2], '-k')
plt.ylabel('z(t)')
plt.xlabel('x(t)')
plt.tight_layout()

