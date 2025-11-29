## Soluciones sobre rangos infinitos

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
# Funcion que entrega dx/dt
def model(x,u):
    dxdu = 1/(x**2*(1-u)**2 + u**2)
    return dxdu
x0 = 1.0 # Condicion inicial
u = np.linspace(0,0.99,100); t = u/(1 - u)
xp = odeint(model, x0, u) # Resolver ODE
plt.clf()
plt.plot(t, xp, '-k')
plt.ylabel('x(t)'); plt.xlabel('t')
plt.show()

#Resolver ec. diferencial 
#dx/dt = 1/(x+t) desde t = 0 a t al infinito con x = 2 en t = 0

def model(x,u):
    dxdu= (1/(1-u)**2)*(1/(x+u/(1-u)))
    return dxdu
x0=2
u=np.linspace(0,0.99,100);t=u/(1-u)
xp=odeint(model,x0,u)

plt.plot(t, xp, '-k')
plt.ylabel('x(t)'); plt.xlabel('t')
plt.show()


#Resolver ODE 
#5dy/dt = -y(t) + u(t) en el intervalo
#t = (0 - 50) con la condicion inicial y(t = 0) = 1 y
#u = 0 para t < 10 y u = 2 para t>=10

def model(y,t):
    if t<10:
        u=0
    else:
        u=2
    dydt=(-y+u)/5
    return dydt
y0=1
t=np.linspace(0,50,300)
yp=odeint(model,y0,t)
plt.plot(t, yp, '-k')
plt.ylabel('y(t)'); plt.xlabel('t')
plt.show()