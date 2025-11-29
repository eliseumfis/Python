from cmath import pi
import numpy as np
import math as mt

g,M,r=6.67*10**(-11),5.97*10**24,6371*1000

T=float(input("Ingrese el tiempo en segundos: "))
h=(((g*M*T**2)/(4*np.pi**2))**(1/3)-r)
print("La altura es:",h)
T1,T2=1/90*60,1/45*60
