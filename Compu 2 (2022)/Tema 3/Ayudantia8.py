import numpy as np
from scipy import interpolate
import pylab as pl

v=np.array(np.loadtxt("datos.txt",float,usecols=0))#[m/s]
t=np.array(np.loadtxt("datos.txt",float,usecols=1))#[s]

#a) Calcular aceleracion en t=2-15
tiempos=range(2,16)
h=0.001
func_v=interpolate.interp1d(t,v,kind="cubic")
aceleraciones=[]
for k in tiempos:
    array_x=np.array([k-h,k,k+h])
    array_y=func_v(array_x)
    derivada=np.gradient(array_y,h)[1]
    aceleraciones.append(derivada) 

#b)

func_a=interpolate.interp1d(tiempos,aceleraciones,kind="cubic")
coef=np.polyfit(t,v,1)
ajuste_lineal=np.poly1d(coef)

pl.subplot(1,2,1)
pl.plot(np.linspace(2,15,100),func_v(np.linspace(2,15,100)),"-r",label="Velocidad")    
pl.plot(np.linspace(2,15,100),func_a(np.linspace(2,15,100)),"-b",label="Aceleración")
pl.grid()
pl.xlabel("Tiempo [s]")
pl.legend()

pl.subplot(1,2,2)
pl.scatter(t,v,label="Datos discretos")
pl.plot(np.linspace(0,16,100),ajuste_lineal(np.linspace(0,16,100)))
pl.grid()
pl.xlabel("Tiempos [s]");pl.ylabel("Velocidad [m/s]")
pl.legend()

pl.show()
