#1)
from scipy import integrate as inte
import numpy as np
import matplotlib.pyplot as pl

"""

m=1

def v(x):
    return x**4
#a) 
a=1

def T(a):
    def f(x):
        return 1/(np.sqrt(v(a)-v(x)))
    I=inte.quadrature(f,0,a)[0]
    return np.sqrt(8*m)*I

print("El valor del periodo cuando la amplitud es igual a 1 es:",T(1))

#b)
TT=[]
for a in np.linspace(0,2,100):
    Tt=T(a)
    TT.append(Tt)
pl.plot(np.linspace(0,2,100),TT,"-r",label="T(a)")
pl.xlabel("Amplitud");pl.ylabel("Periodo")
pl.grid();pl.legend()
pl.show()
"""

#1)
def T(z):
    def f(t):
        return (t**(z-1) * np.exp(-t))
    return inte.quadrature(f,0,15)[0]
#a)
enteros=np.arange(2,11,1)
Tz=[]
for n in enteros:
    Tzz=(T(n))
    Tz.append(Tzz)

#b)

v_real=[]
for z in enteros:
    l=np.math.factorial(z-1)
    v_real.append(l)
pp=[]
for n in range(0,9,1):
    erp=abs(v_real[n]-Tz[n])*100/v_real[n]
    pp.append(erp)
    print("El erp para z=",enteros[n],"es de un",erp)
pl.plot(enteros,pp,"--g")
pl.scatter(enteros,pp,color="red")
pl.grid()
pl.show()