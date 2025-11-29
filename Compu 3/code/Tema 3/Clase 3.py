#Calcular solucion de ecs:
#dx/dt= xy - x;
#dydt= y - xy + sin^2(wt)
#desde t = 0 hasta t = 10 para el caso w = 1 con la condicion
#inicial x = y = 1 en t = 0

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
def model(r,t):
    x = r[0]; y = r[1]
    fx = x*y - x; fy = y - x*y + np.sin(t)**2
    return np.array([fx,fy],float)
r0 = [1.0, 1.0] # Condicion inicial
t = np.linspace(0,10,100)
rp = odeint(model, r0, t) # Resolver ODE
plt.clf()
plt.plot(t, rp[:,0], '-b', t, rp[:,1], '-r')
plt.ylabel('x(t) and y(t)'); plt.xlabel('t')
plt.legend(('x(t)','y(t)'), loc=1)
plt.show()

#Resolver el sistema de ecuaciones:
#dxdt= 3e^(-t)
#dydt= 1 - y
#desde t = 0 hasta t = 10 con la condicion inicial x = y = 0 en t = 0
def model(r,t):
    x = r[0]; y = r[1]
    fx=3*np.exp(-t)
    fy=1-y
    return np.array([fx,fy],float)
r0 = [0, 0] # Condicion inicial
t = np.linspace(0,10,100)
rp = odeint(model, r0, t) # Resolver ODE
plt.clf()
plt.plot(t, rp[:,0], '-b', t, rp[:,1], '-r')
plt.ylabel('x(t) and y(t)'); plt.xlabel('t')
plt.legend(('x(t)','y(t)'), loc=4)
plt.show()

#Ejercicio 8.2: Ecuaciones de Lotka-Volterra


def model(r,t):
    alfa=1
    beta=0.5;gamma=0.5
    delta=2
    x=r[0]
    y=r[1]
    fx=alfa*x -beta*x*y
    fy=gamma*x*y - delta*y
    return np.array([fx,fy],float)
r0=[2,2]
t=np.linspace(0,30,200)

#Resolver ode

rp=odeint(model,r0,t)
plt.clf()
plt.plot(t,rp[:,0],"-b",t,rp[:,1],"-r")
plt.ylabel("x(t) and y(t)");plt.xlabel("t")
plt.legend(("x(t): presas","y(t): predadores"),loc=1)
plt.show()

#Resolver el sistema de ecuaciones:
# (2 - x)dx/dt = -x + u
# (y-1)dy/dt= -y + x
# desde t = 0 hasta t = 15 con la condicion inicial x = y = 0 en
# t = 0. El paraametro u = 0 para t < 5 y u = 2 para t>= 5

def model(r,t):
    x = r[0]; y = r[1]
    if t<5:
        u=0
    else:
        u=2
    fx=(-x+u)/(2-x)
    fy=(-y+x)/(y-1)
    return np.array([fx,fy],float)
r0=[0,0]
t=np.linspace(0,15,200)
rp = odeint(model, r0, t) # Resolver ODE
plt.clf()
plt.plot(t, rp[:,0], '-b', t, rp[:,1], '-r')
plt.ylabel('x(t) and y(t)'); plt.xlabel('t')
plt.legend(('x(t)','y(t)'), loc=4)
plt.show()

