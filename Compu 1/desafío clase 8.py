from math import *

# A)

# T=1
G = 6.67 * 10**-11
M = 5.97 * 10**24
R = 6371 * 1000
h = (((G * M * T**2) / 4 * (pi) ** 2) ** 1 / 3 - R) / 1000
print("La altura es", h, "metros")
print("############################################################################")

# B)

T = float(input("Ingrese el tiempo que desea cálcular, para sacar un altura: "))
print(
    "La altura es", (((G * M * T**2) / 4 * (pi) ** 2) ** (1 / 3) - R) / 1000, "metros"
)

# C)CALCULAR ALTITUD DE 2 SATLÉLITES

T1 = 1 / 90 * 60
T2 = 1 / 45 * 60
print(
    "La altura para el primer satélite será:",
    ((((G * M * T1**2) / 4 * (pi) ** 2) ** 1 / 3 - R) / 1000),
    "metros",
)
print(
    "La altura para el segundo satélite será:",
    ((((G * M * T2**2) / 4 * (pi) ** 2) ** 1 / 3 - R) / 1000),
    "metros",
)
# Se concluye que el periodo orbital puede afectar significativamente la altitud de un objeto, debido a los factores que están en juego en la ecuasión.

# D)CALCULAR ALTURA CON 23.93 HRS Y 24 HRS
T1 = 1 / 23.93 * 3600
T2 = 1 / 24 * 3600
print(
    "La altura para T1 es",
    ((((G * M * T1**2) / 4 * (pi) ** 2) ** 1 / 3 - R) / 1000),
    "metros",
)
h1 = (((G * M * T1**2) / 4 * (pi) ** 2) ** 1 / 3 - R) / 1000
print(
    "La altura para T2 es",
    ((((G * M * T2**2) / 4 * (pi) ** 2) ** 1 / 3 - R) / 1000),
    "metros",
)
h2 = (((G * M * T2**2) / 4 * (pi) ** 2) ** 1 / 3 - R) / 1000
print("La diferencia es", h1 - h2, "metros")
# Se concluye que al estar demorarse un poco menos, osea tener mayor velocidad, la fuerza de gravedad no lo atrapa tanto y por eso logra mas altitud.
