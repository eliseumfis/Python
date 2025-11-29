from numpy import *
import pylab as plt
import math
import scipy 
temps = linspace(5,500,500)

V = 1e-6 # cubic meters
rho = 6.022e28 # m**-3
debye = 428 # K
kB = 1.38064852e-23 # m**2 kg s**-2 K**-1
N = 50 # sample points
a = 0


def dcdt(x):
    return (9*V*rho*kB*(temp/debye)**3)*(x**4*exp(x))/(exp(x)-1)**2


S = list()

for temp in temps:
    b = debye/temp
    S.append(gquad(dcdt,b))

plt.figure(figsize=(7,4))
plt.plot(temps,S,color='purple')
plt.title("Heat capacity of solid aluminum")
plt.xlabel(r"Temperature ($K$)")
plt.ylabel(r"$C_V$ ( $J \cdot K^{-1}$)")
plt.xlim(temps[0],temps[-1])
plt.show()