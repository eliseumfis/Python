import numpy as np
import pylab as plt

T1 = np.loadtxt("T1.dat", float)
P1 = np.loadtxt("P1.dat", float)  # 2 METROS DE ALTRURA

T2 = np.loadtxt("T2.dat", float)
P2 = np.loadtxt("P2.dat", float)  # 15 KILOMETROS DE ALTURA


# Datos tomados cada 10 minutos
R = 286.9


################ 1)


def ROgasideal(T, P):
    P = P * 100
    return P / (R * T)


RO1 = ROgasideal(T1, P1)
RO2 = ROgasideal(T2, P2)

################# 2)
DATA1 = [T1, P1, RO1]
DATA2 = [T2, P2, RO2]

Prom1 = []
Prom2 = []


def promedio(data):
    return np.mean(data)


for k in DATA1:
    Prom1.append(promedio(k))
for k in DATA2:
    Prom2.append(promedio(k))

print(
    "El promedio de la temperatura en kelvin, la presión en pascales y densidad en kg/m^3 a 2 metros de altura son:",
    Prom1,
)
print(
    "El promedio de la temperatura en kelvin, la presión en pascales y densidad en kg/m^3 a 15 kilómetros de altura son:",
    Prom2,
)

# Hacer gráfico de la densidad del aire en las 2 alturas

time = np.linspace(0, 144, 144)
plt.plot(time, RO1, color="red", label="Densidad a 2 metros de altura")
plt.plot(time, RO2, color="blue", label="Densidad a 15 kilometros de altura")
plt.grid()
plt.legend()
plt.tight_layout()
plt.xlabel("Tiempo [10] min")


plt.show()
