import numpy as np
import matplotlib.pylab as pl
from scipy import integrate,interpolate

#1)))


Tt=[]
for a in range(2,11,1):
    def T(a):
        def f(x):
            return (x**(a-1) * np.exp(-x))
        return (integrate.quadrature(f,0,15)[0])
    Tt.append(T(a))
#a)

#print(Tt)

#b)
v_real=[]
enteros=np.arange(2,11,1)
for n in enteros:
    l=np.math.factorial(n-1)
    v_real.append(l)
ERP=[]
for n in range(0,9,1):
    erp=abs(v_real[n]-Tt[n])/v_real[n] *100
    ERP.append(erp)
    print("El erp para a =",enteros[n],"es de un",erp,"%")
pl.subplot(1,2,1)
pl.scatter(enteros,ERP,color="blue")
pl.plot(enteros,ERP,"-r")
pl.xlabel("Valores de a");pl.ylabel("Error relativo porcentual [%]")
pl.title("1)")
pl.grid()




#2)))
year=np.loadtxt("Npersonas_ciudad.txt",float,usecols=0)
pob=np.loadtxt("Npersonas_ciudad.txt",float,usecols=1)
year_fl=np.linspace(year[0],year[-1],1000)
f=interpolate.interp1d(year,pob,kind="cubic")

#a)

y=[1912,1965,1978,1999,2003]
NN=[]
for n in y:
    NN.append(f(n))
    print("En el año",n,"había un poblacion estimada de",f(n))

#b)
pl.subplot(1,2,2)
pl.plot(y,NN,"*r")
pl.plot(year_fl,f(year_fl),"-b")
pl.xlabel("Años");pl.ylabel("Población")
pl.title("2)")
pl.grid()
pl.show()