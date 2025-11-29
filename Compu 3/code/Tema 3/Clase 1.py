#Resolver ODE 
#dx/dt = -x^3 + sin t usando funcion odeint para
#x(t = 0) = 0 en intervalo desde a = 0 a b = 10 en 50 iteraciones.
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def model(x, t):
    dxdt = -x**3 + np.sin(t)
    return dxdt
a, b = 0.0, 10.0 # tiempo inicial y final
x0 = 0.0 # Condicioon inicial
N = 50; h = (b-a)/N; t = np.arange(a, b, h)
# Resolver ODE
xp = odeint(model, x0, t)
print(xp)
plt.plot(t,xp,"--",color="black")
plt.ylabel("x(t)");plt.xlabel("t")
plt.grid
plt.show()
plt.clf()
#Resolver ODE 
#dy/dt = -ky para k = 0.3 entre 0 y 20
#con la condicion inicial y(t = 0) = 5

def modell(y,t):
    k=0.3
    dydt=-k*y
    return dydt
a,b=0.0,20
y0=5
t = np.linspace(0, 20, 50)
yp=odeint(modell,y0,t)
plt.plot(t, yp, '-k')
plt.ylabel('y(t)'); plt.xlabel('t')
plt.show()
plt.clf()
#Se puede agregar un 4to argumento (args) a funcion odeint
#Este 4to argumento es un tuple ( )
#Permite pasarle informacion a funcion 'model'
#En ejemplo anterior supongamos que no conocemos k
def model(y, t, k):
    dydt = -k*y
    return dydt
y0 = 5.0 # Condicion inicial
t = np.linspace(0, 20, 50)
k = 0.3
yp = odeint(model, y0, t, args=(k,)) # Resolver ODE
plt.plot(t, yp, '-k')
plt.ylabel('y(t)'); plt.xlabel('t')
plt.show()


#Resolver ODE
#dy/dt = -ky entre 0 y 20 con condicion
#inicial y(t = 0) = 5 para los siguientes valores de k = 0.1, 0.2 y
#0.5. Plotear las 3 soluciones en el mismo plot


def model(y, t, k):
    dydt = -k*y
    return dydt
y0 = 5.0; t = np.linspace(0,20,50)
# Resolver ODE
k = (0.1, 0.2, 0.5); lab  = ('-k','-b','-r')
plt.clf()
for kk in range(len(k)):
    yp= odeint(model, y0, t, args=(k[kk],))
    plt.plot(t, yp, lab[kk])
plt.ylabel('y(t)'); plt.xlabel('t')
plt.legend(('k=0.1','k=0.2','k=0.5'), loc=1)