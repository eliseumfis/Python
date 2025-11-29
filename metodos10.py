import numpy as np
import matplotlib.pyplot as plt


# Definición de las funciones
def delta_n(x, n):
    return (n / np.sqrt(np.pi)) * np.exp(-(n**2) * x**2)


def delta_tilde_n(k, n):
    return np.exp(-(k**2) / (4 * n**2))


# Rango de valores de x y k
x = np.linspace(-5, 5, 400)
k = np.linspace(-5, 5, 400)

# Valores de n
n_small = 0.5
n_large = 5

# Cálculo de las funciones para n pequeño y grande
delta_n_small = delta_n(x, n_small)
delta_n_large = delta_n(x, n_large)

delta_tilde_n_small = delta_tilde_n(k, n_small)
delta_tilde_n_large = delta_tilde_n(k, n_large)

# Graficar δn(x) para n pequeño y grande
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(x, delta_n_small, label=f"n={n_small}", color="black")
plt.plot(x, delta_n_large, label=f"n={n_large}", color="red")
plt.title(r"$\delta_n(x)$")
plt.xlabel("x")
plt.ylabel(r"$\delta_n(x)$")
plt.grid()
plt.legend()

# Graficar ̃δn(k) para n pequeño y grande
plt.subplot(1, 2, 2)
plt.plot(k, delta_tilde_n_small, label=f"n={n_small}", color="black")
plt.plot(k, delta_tilde_n_large, label=f"n={n_large}", color="red")
plt.title(r"$\widetilde{\delta}_n(k)$")
plt.xlabel("k")
plt.ylabel(r"$\widetilde{\delta}_n(k)$")
plt.grid()
plt.legend()


plt.tight_layout()
plt.show()
