import numpy as np
import matplotlib.pyplot as plt

# Constantes físicas
h = 6.62607015e-34  # Constante de Planck [J s]
c = 3e8  # Velocidad de la luz en el vacío [m/s]
k = 1.3706503e-23  # Constante de Boltzmann [J/K]

# Temperatura del cuerpo negro
T_s = 5777  # Kelvin
ls_ = 5e-7


# Definición de las funciones Bp y Br
def Bp(T, l):
    return (2 * h * c**2 / l**5) / (np.exp(h * c / (l * k * T)) - 1)


def Br(T, l):
    return (2 * c * k * T) / l**4


ls_range = np.linspace(1e-7, 1e-19, 1000)
plt.plot(ls_range, Bp(T_s, ls_range))
plt.plot(ls_range, Br(T_s, ls_range), "--")
plt.show()
