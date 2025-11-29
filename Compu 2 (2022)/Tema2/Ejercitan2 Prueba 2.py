import numpy as np
import pylab as pl
from scipy import integrate,interpolate

#1)
"""
def f(x):
    return ((2+3*np.sin(2*x))**3)
a=0;b=np.pi/2

#a)Calcular metodo romberg

Ir=integrate.romberg(f,a,b,show=False)
#print(Ir)

#b)Cuadratura

Iq=integrate.quadrature(f,a,b)
print("El valor de la integral por método gaussiano es",Iq[0],"y su error es de",Iq[1],"%")
"""
#2)

h=np.loadtxt("temp_pressure_PP2.txt",float,usecols=0)
T=np.loadtxt("temp_pressure_PP2.txt",float,usecols=1)
p=np.loadtxt("temp_pressure_PP2.txt",float,usecols=2)
p0=100000;R=8.31;cp=2.91
#o(T,p)=T(p/p0)^(R/cp)

def o(T,p):
    return T*(p/p0)**(R/cp)
tp=o(T,p)
Tpfunc=interpolate.interp1d(h,tp,kind="cubic")
#a) Calcular cuál será el valor de la temperatura potencial 
# 𝜃 a 2.2 [𝑘𝑚] y a 5.8 [𝑘𝑚] de altura.
print("La temperatura potencial a 2.2 km será de: ",Tpfunc(2.2),"K")
print("La temperatura potencial a 2.2 km será de: ",Tpfunc(5.8),"K")
#b) Elaborar un gráfico continuo que muestre cómo varía la temperatura potencial 
# 𝜃 respecto a la altura en [𝑘𝑚].

pl.plot(h,tp,"-r",label="T(h)")
pl.xlabel("Altura");pl.ylabel("Temperatura potencial")
pl.grid();pl.legend()

pl.show()