import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Parámetros
m = 1  # Masa de la bala de cañón en kg
R = 0.08  # Radio de la bala de cañón en metros
rho = 1.22  # Densidad del aire en kg/m^3
C = 0.47  # Coeficiente de arrastre
g = 9.81  # Aceleración de la gravedad en m/s^2
angle = np.deg2rad(30)  # Ángulo de disparo en radianes
v0 = 100  # Velocidad inicial en m/s

# Función que devuelve las derivadas de x y z con respecto al tiempo
def cannon(r, t):
    x, dxdt, z, dzdt = r
    dx2dt2 = -np.pi * R**2 * rho * C / (2 * m) * dxdt * np.sqrt(dxdt**2 + dzdt**2)
    dz2dt2 = -g - np.pi * R**2 * rho * C / (2 * m) * dzdt * np.sqrt(dxdt**2 + dzdt**2)
    return [dxdt, dx2dt2, dzdt, dz2dt2]

# Condiciones iniciales
x0 = 0
z0 = 0
vx0 = v0 * np.cos(angle)
vz0 = v0 * np.sin(angle)
r0 = [x0, vx0, z0, vz0]

# Tiempo de integración
t = np.linspace(0, 10, 1000)

# Resolver las ecuaciones diferenciales
sol = odeint(cannon, r0, t)

# Extraer las trayectorias x y z
x = sol[:, 0]
z = sol[:, 2]

# Graficar la trayectoria
plt.plot(x, z)
plt.xlabel('x (m)')
plt.ylabel('z (m)')
plt.title('Trayectoria de la bala de cañón')
plt.grid()
plt.show()

# Encontrar el tiempo de impacto con el suelo
index = np.where(z < 0)[0][0]
tiempo_impacto = t[index]

# Encontrar la distancia recorrida en x al llegar al suelo
distancia_recorrida = x[index]

print("Tiempo de impacto con el suelo:", tiempo_impacto, "segundos")
print("Distancia recorrida en x al llegar al suelo:", distancia_recorrida, "metros")
