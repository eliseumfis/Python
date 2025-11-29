# Prueba 3 LFIS-116 2021

# modulos
import numpy as np
import pylab as pl

# Cargar datos
T1 = np.loadtxt("T1.dat")
T2 = np.loadtxt("T2.dat")
P1 = np.loadtxt("P1.dat")
P2 = np.loadtxt("P2.dat")

# 1 Funcion que calcula la densidad del aire


def dens(T, P):
    R = 286.9  # Constante de gas ideal para el aire
    P = P * 100  # Convertir de hPa a Pa
    dd = P / (R * T)
    return dd


# 2 Funcion que calcula el promedio


def meann(X):
    m = np.mean(X)
    return m


var2m = []
var2m.append(meann(T1))
var2m.append(meann(P1))
var2m.append(meann(dens(T1, P1)))

var15k = []
var15k.append(meann(T2))
var15k.append(meann(P2))
var15k.append(meann(dens(T2, P2)))

print(
    "La Presion en hPa, Temperatura en K y la densidad en kg/m3 a dos metros es: ",
    var2m,
)
print(
    "La Presion en hPa, Temperatura en K y la densidad en kg/m3 a 15 kilometros es: ",
    var15k,
)

# 3 Plot densidad del aire
pl.figure(1)
pl.plot(dens(T1, P1), "r", label="Dens. 2m")
pl.plot(dens(T2, P2), "g", label="Dens. 15km")
pl.xlabel("Tiempo [10 min]")
pl.ylabel("Densidad [kg/m3]")
pl.title("Densidad del aire")
pl.legend()
pl.grid()
pl.savefig("Densidad_aire_2m15km.png")

# 4 Sobre la densidad del aire
print(
    "La densidad del aire desciende con la altura, por lo tanto los valores de densidad del aire a 2 metros dene ser mayores a los valores de densidad del aire a 15 km. Los resultados son acorde con la teoria"
)

# 5 Correlación entre la presion y temperatura

# coeficiente de correlacion r
r2m = np.corrcoef(P1, T1)
r2m = r2m[1][0]
r15k = np.corrcoef(P2, T2)
r15k = r15k[1][0]

pl.figure(figsize=[10, 5])
pl.subplot(1, 2, 1)
pl.scatter(P1, T1, color="r")
pl.xlim(908, 911)
pl.ylim(286, 297)
pl.plot([908, 911], [297, 286], "k")
pl.text(909.5, 296, ("R=", str(round(r2m, 2))))
pl.xlabel("[hPa]")
pl.ylabel("[K]")
pl.title("Presion y temperatura a 2 m")
pl.grid()

pl.subplot(1, 2, 2)
pl.scatter(P2, T2, color="g")
pl.xlim(144.084, 144.094)
pl.ylim(208.5, 210.5)
pl.plot([144.084, 144.094], [208.5, 210.5], "k")
pl.text(144.0845, 210.35, ("R=", str(round(r15k, 2))))
pl.xlabel("[hPa]")
pl.ylabel("[K]")
pl.title("Presion y temperatura a 15 km")
pl.grid()
pl.savefig("Correlacion_Press_Temp.png")
pl.show()
