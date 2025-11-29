import numpy as np
import pylab as pl


def f(x):  # Función dentro de la integral
    return (x**3) / (np.exp(x) - 1)


# a)
a = 0.05
b = 500  # Límites de integración
trap_r = []
simp_r = []
N = []
W = []
Temp = []  # Listas para guardar valores de variables

for n in range(4, 201, 2):
    N.append(n)
    h = abs(b - a) / n

    # Trapezoidal
    st = 0.0
    for k in range(1, n):
        st += f(a + k * h)
    trap = h * ((f(a) + f(b)) / 2 + st)
    trap_r.append(trap)  # Valores de Integral por método trapezoidal

    # Simpson
    si = 0.0
    for k in range(1, n, 2):
        si += f(a + k * h)
    sp = 0.0
    for k in range(2, n - 1, 2):
        sp += f(a + k * h)
    simp = (h / 3) * (f(a) + f(b) + 4 * si + 2 * sp)
    simp_r.append(simp)  # Valores de Integral por método simpson

# b)

pl.subplot(1, 2, 1)
pl.plot(N, trap_r, "-r", label="Trapezoidal")
pl.plot(N, simp_r, "-b", label="Simpson")
pl.title("Valores de I en función de n")
pl.xlabel("Secciones [n]")
pl.ylabel("I")
pl.grid()
pl.legend()


# c)
n = 200
c = 10 ** (-8)
a = 0.05
b = 500
h = abs(b - a) / n
st = 0.0
for k in range(1, n):
    st += f(a + k * h)
trapp = h * ((f(a) + f(b)) / 2 + st)
for T in range(200, 301, 5):
    Temp.append(T)
    w = c * T**4 * trapp
    W.append(w)
pl.subplot(1, 2, 2)
pl.plot(Temp, W, "-g")
pl.title("W(T)")
pl.xlabel("Temperatura")
pl.ylabel("W")
pl.grid()
pl.tight_layout
pl.show()
