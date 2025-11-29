import numpy as np
from scipy import interpolate
import pylab as pl
#1)
v=[1.2,3.4,5.5,8.9,12.3,15.4,17.3]
t=[1.5,2.5,6.6,9.0,11.3,13.5,15.7]


#a) Calcule los datos de velocidad y de aceleración entre los tiempos 1.5 y 15.5, cada 0.25 segundos
tiempos=np.arange(1.5,5.5+0.25,0.25)
h=0.25
funcion_velocidad=interpolate.interp1d(t,v,kind="cubic")
velocidades=[]
aceleraciones=[]
for k in tiempos:
    vel=funcion_velocidad(k)
    velocidades.append(vel)
    array_x=[k,k,k+h]
    array_y=funcion_velocidad(array_x)
    derivadas=np.gradient(array_y,h)[1]
    aceleraciones.append(derivadas)
    print("El valor de la velocidad y aceleración en t=",k,", son respectivamente:",vel,"[m/s] y",derivadas,"[m/s^2]")

#b) Grafique velocidad y aceleración obtenida anteriormente
pl.subplot(1,2,1)
pl.plot(tiempos,velocidades,"*r",label="Datos discretos")
pl.title("V(t) v/s t")
pl.grid()
pl.xlabel("Tiempo [s]");pl.ylabel("Velocidad [m/s]")
pl.legend()

pl.subplot(1,2,2)
pl.plot(tiempos,aceleraciones,"*b",label="Datos discretos")
pl.title("a(t) v/s t")
pl.grid()
pl.xlabel("Tiempo [s]");pl.ylabel("Aceleración [m/s^2]")
pl.legend()
pl.show()

#c y e) Ajuste una curva lineal a los datos de velocidad originales
coef1=np.polyfit(t,v,1)
fv1=np.poly1d(coef1)
ax=fv1(t)
pl.plot(t,fv1(t),"-r",label="Ajuste de curvas de orden 1")
pl.scatter(t,v,color="blue")
pl.title("V(t) v/s t")
pl.grid()
pl.xlabel("Tiempo [s]");pl.ylabel("Velocidad [m/s]")
pl.legend()
pl.show()

#d) Indicar valor de la pendiente de la recta anterior
for k in t:
    arrx=np.array([k-h,k,k+h])
    arry=fv1(arrx)
    m=np.gradient(arry,h)
    print("La pendiente en t=",k," es igual a =",m[1])
print("Como se puede ver la pendiente siempre se mantiene en",1.12811053836399,"y solo varía en los siguientes dos decimales que le siguen.")


