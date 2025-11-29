import matplotlib.pyplot as plt
import numpy as np

# Parámetros del solenoide
mu_0 = 4 * np.pi * 10**(-7)  # Permeabilidad del vacío en T m/A
n = 1  # Número de espiras por unidad de longitud
I = 1  # Corriente en Amperios
R = 1  # Radio del solenoide

# Crear un array de distancias desde el extremo del solenoide (x) en unidades de R
x_values = np.linspace(0, 5, 100)  # Puedes ajustar el rango según lo que desees graficar

# Calcular la inducción del campo magnético (B) para cada distancia x
B_values = mu_0 * n * I

# Graficar B versus x/R
plt.plot(x_values/R, B_values)
plt.xlabel('x/R')
plt.ylabel('B (Tesla)')
plt.title('Inducción del campo magnético en el solenoide infinitamente largo')
plt.grid(True)
plt.show()