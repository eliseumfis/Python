import numpy as np
import matplotlib.pylab as pl
from scipy import integrate,interpolate

#1)
def T(z):
    def f(t):
        return (t**(z-1) * np.exp(-t))
    return (integrate.quadrature(f,0,15)[0])
#a)

enteros=np.arange(2,11,1)
Tz=[]
for n in enteros:
    tz=(T(n))
    Tz.append(tz)


#b)

vr=[]
for z in enteros:
    l=np.math.factorial(z-1)
    vr.append(l)
ERP=[]

for n in range(0,9,1):
    erp=abs(vr[n]-Tz[n])*100/vr[n]
    ERP.append(erp)
    print("Para z =",enteros[n],"se calcula un error de",erp,"%","de error|")
pl.plot(enteros,ERP,"-r")
pl.scatter(enteros,ERP,color="blue")
pl.xlabel("Números enteros")
pl.ylabel("Error relativo porcentual")
pl.grid()
pl.show()