import numpy as np
import pylab as pl
from scipy import integrate
from scipy import interpolate
years=np.loadtxt("Population_per_year.txt",float,usecols=0)#(1900,2020,5)
pob=np.loadtxt("Population_per_year.txt",float,usecols=1)

#a)
x0=years[0];xf=years[-1]
years_f=np.linspace(x0,xf,500)
s=interpolate.interp1d(years,pob,kind="cubic")
y=[1912,1956,1978,1999,2003]
P=[]
for n in range(0,5,1):
    print("La poblacion en",y[n],"es",s(y[n]),"habitantes")
    p=s(y[n])
    P.append(p)

#b)
pl.plot(years_f,s(years_f),"-b")
pl.plot(y,P,"*r")
pl.xlabel("Años");pl.ylabel("")
pl.grid();pl.legend()

pl.show()