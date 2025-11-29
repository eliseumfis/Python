import numpy as np
import matplotlib.pylab as pl
from scipy import integrate,interpolate


#1)
IQ=[]
a=np.pi*(-1);b=np.pi

#a)

for k in range(1,11,1):
    def f(x):
        return np.sin(5*x)*np.sin(k*x)
    Iq=integrate.quadrature(f,a,b)[0]
    IQ.append(Iq)
    print("El valor de la integral cuando k =",k,"es:",Iq)

#b) 

pl.plot(range(1,11,1),IQ,"-r")
pl.scatter(range(1,11,1),IQ,color="blue")
pl.xlabel("Valores de K");pl.ylabel("Valores de I_k")
pl.title("1) I_k v/s K")
pl.grid()
pl.show()

#2)
t=np.loadtxt("velocidades.txt",float,usecols=0)
v=np.loadtxt("velocidades.txt",float,usecols=1)

#a)
s=interpolate.interp1d(t,v,kind="cubic")
t_fl=np.linspace(t[0],t[-1],100);v_fl=s(t_fl)
tiempos=[1.5,12.5,26.7,37.2,44.4,56.7,60.5,76.8,85.3]
Vv=[]
for k in tiempos:
    Vv.append(s(k))
    print("El valor para la velocidad cuanto t =",k,"es:",s(k))
pl.subplot(1,2,1)
pl.plot(tiempos,Vv,"-r")
pl.scatter(tiempos,Vv,color="green")
pl.xlabel("Tiempo [s]");pl.ylabel("Velocidad [m/s]")
pl.title("2a) V v/s t")
pl.grid()



#b)

tt=np.arange(2,101,2)
vvv=[]
Is=[]
for n in tt:
    vvv.append(s(n))
#Is.append(integrate.simps(vv,tt))
coef=np.polyfit(tt,vvv,1)
func=np.poly1d(coef,)
for k in range(2,101,2):
    iss=integrate.quadrature(func,2,k+2)[0]
    Is.append(iss)
    
#c)
pl.subplot(1,2,2)
pl.plot(tt,Is,"-b")
pl.xlabel("Tiempo [s]");pl.ylabel("Posición [m]")
pl.title("2c) x v/s t")
pl.grid()
pl.show()

