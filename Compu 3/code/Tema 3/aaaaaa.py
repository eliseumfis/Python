################################# Prueba 3 ################################
####Ejercicio 1

import numpy as np
import scipy.integrate as sc 
import matplotlib.pylab as pl

G = 6.67e-11  #Constante gravitacional
M = 1.9e30    #Masa del sol  

def func(r,t):
    x=r[0]
    y=r[1];vx=r[2];vy=r[3]
    dxdt=vx
    dydt=vy
    R=np.sqrt(x**2+y**2)
    dvx=-(G*M*x)/(R**3)
    dvy=-(G*M*y)/(R**3)
    return np.array([dxdt,dydt,dvx,dvy],float)
R = 1.496e11
T = 3.156e7 
v = 2*np.pi*R/T
t=np.linspace(0,1.6e9,1000)
r0 = [4e12,0,0,500]
sol=sc.odeint(func,r0,t)
x = sol[:, 0]
y = sol[:, 1]
pl.plot(y,x)
pl.title("Orbita de un cometa alrededor del sol")
pl.xlabel("y(t)")
pl.ylabel("x(t)")
pl.grid()
##tiempo
trev = np.argmax(x)
tiempo_vuelta = t[trev]
años = tiempo_vuelta / 365.25  # 365.25 días en un año promedio

print("El cometa da una vuelta completa al Sol aproximadamente en", años, "años.")

import numpy as np
import matplotlib.pylab as plt
import scipy.integrate as sc

######### Ejercicio 2

# Definir la ecuación diferencial
def func(y, t):
    
    return [y[1], -3 * y[0]]

# Condiciones iniciales
y0 = 7  # y(0) = 7
dy0 = 0  # dy/dt(0) = 0

# Puntos de tiempo para evaluar la solución
t = np.linspace(0, np.pi, 100)

# Resolver la ecuación diferencial
sol = sc.odeint(func, [y0, dy0], t)
y = sol[:, 0]
plt.clf()
# Graficar la solución y(t)
plt.plot(t, y)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Solución de la ecuación diferencial')
plt.grid(True)
plt.show()

# Verificar las condiciones iniciales
y_pi = sol[-1, 0]  # Valor de y en t=pi
y_2pi = sol[-1, 1]  # Valor de dy/dt en t=pi

print("y(pi) =", y_pi)
print("dy/dt(pi) =", y_2pi)