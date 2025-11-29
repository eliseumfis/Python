import numpy as np
from pylab import *

dataT1 = np.loadtxt("T1.dat", float)
dataT2 = loadtxt("T2.dat", float)
dataP1 = loadtxt("P1.dat", float)
dataP2 = loadtxt("P2.dat", float)

Densidad1 = []
Densidad2 = []
# 1) Programa que calcule la densidad del aire
for n in dataP1:
    ro = n / (dataT1 * 286, 9)
    Densidad1.append(ro)
for n in dataP2:
    ro = n / (dataT2 * 286, 9)
    Densidad2.append(ro)
print(Densidad1)
