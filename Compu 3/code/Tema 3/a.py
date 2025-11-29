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
