#1)
import numpy as np
from scipy import interpolate
import pylab as pl

v=np.loadtxt("datos.txt",float,usecols=0)
t=np.loadtxt("datos.txt",float,usecols=1)

#a) Calcular la aceleracion t=range(2,16,1)

fv=interpolate.interp1d(t,v,kind="cubic")
tiempos=range(2,16)
aceleraciones=[]
h=0.001
for k in tiempos:
    array_x=[k-h,k,k+h]
    array_y=fv(array_x)
    derivadas=np.gradient(array_y,h)[1]
    aceleraciones.append(derivadas)
    print("El valor de la aceleración en t=",k,"es:",derivadas)

#b)
fa=interpolate.interp1d(tiempos,aceleraciones,kind="cubic")
coef=np.polyfit(t,v,1)
ajuste=np.poly1d(coef)

pl.subplot(1,2,1)
pl.plot(np.linspace(2,15,100),fv(np.linspace(2,15,100)),"-r",label="Velocidad")
pl.plot(np.linspace(2,15,100),fa(np.linspace(2,15,100)),"-b",label="Aceleración")
pl.grid()
pl.legend()

pl.subplot(1,2,2)
pl.scatter(t,v,label="Datos discretos")
pl.plot(np.linspace(0,16,100),ajuste(np.linspace(0,16,100)))
pl.grid()
pl.xlabel("Tiempos [s]");pl.ylabel("Velocidad [m/s]")
pl.legend()
pl.show()