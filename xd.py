import numpy as np
import matplotlib.pyplot as plt

# Parámetros
L = 1  # Longitud del primer tubo
x1 = np.linspace(0, 1 * L, 2000)  # Puntos a lo largo del primer y segundo tubo


# Función de la onda estacionaria
def onda_estacionaria(x, L, n):
    k = n * np.pi / L
    return np.sin(k * x)


# Función para extender periódicamente la onda estacionaria
def onda_estacionaria_periodica(x, L, n):
    x_mod = np.mod(x, L)  # Modulo para extender la periodicidad
    return onda_estacionaria(x_mod, L, n)


# Modos a graficar
modos = [1, 2, 5, 10]  # Puedes agregar más modos si lo deseas

# Creación de la figura y el gráfico
plt.figure(figsize=(12, 8))

for n in modos:
    # Generación de las ondas periódicas para cada modo
    onda_L_periodica = onda_estacionaria_periodica(x1, L, n)
    # onda_2L = onda_estacionaria(x1, 2 * L, n)

    # Graficar las ondas
    plt.plot(x1, onda_L_periodica, label=f"Tubo de longitud L , n={n}")
    # plt.plot(x1, onda_2L, label=f"Tubo de longitud 2L, n={n}")

# Personalización del gráfico
plt.title("Ondas Estacionarias en Cuerda de Guitarra")
plt.xlabel("Posición a lo largo de la guitarra")
plt.ylabel("Amplitud")
plt.legend()
plt.grid(True)

# Mostrar gráfico
plt.show()
