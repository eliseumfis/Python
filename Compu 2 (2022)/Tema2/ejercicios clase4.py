import numpy as np
from scipy import interpolate
import pylab as plt
h=np.array([0,2,4,6,7,8,9,10,11])
T=np.array([288.5,280.2,277.4,273.2,269.3,260.4,257.3,250.2,245.1])
P=np.array([1026.24,803,605,400,350,300,250,200,150])

#P=pRT
R=287.05

#Encontrar p y plotear densidad vs altura. Determinar valor de a 5.3 km
densidad=P/R*T
hh=np.arange(0,11.1,0.1)
fden=interpolate.interp1d(h,densidad,kind="cubic")
denHH=fden(hh)
den53=fden(5.3)
print(den53)
print("El valor de densidad en 5.3 km =", den53, "kg/m3")
plt.clf(); plt.plot(denHH, hh, "-k", den53, 5.3, "*r")
plt.xlabel("Densidad [kg/m3]"); plt.ylabel("Altura [km]")
plt.show()