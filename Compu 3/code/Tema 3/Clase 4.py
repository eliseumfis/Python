# Escriba un programa que resuelva el sistema de
# ecuaciones siguientes para el movimiento de un
# pendulo de 10 cm de largo:
# d0/dt=w
# dw/dt=g*Sen(0)/l
# Calcular 0(t) para varios periodos del pendulo si este se lanza
# desde un angulo 0 = 179°
# Haga un plot de 0(t) en funcion del t


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
a = 0.0; b = 50.0; N = 500; g0 = 9.81
t = np.linspace(a,b,N); ll = 0.1 # 10 cm longitud
def func(r,t):
    theta = r[0]; omega = r[1]
    dthedt = omega; domedt = - g0/ll*np.sin(theta)
    return np.array([dthedt, domedt],float)

r0 = np.array([np.radians(179), 0.0])
sol = odeint(func, r0, t)
plt.clf()
plt.subplot(2,1,1)
plt.plot(t, np.degrees(sol[:,0]),'orange')
plt.xlabel('t') 
plt.ylabel(r'$theta(t)$')
plt.grid()
plt.subplot(2,1,2); plt.plot(t, sol[:,1],'-c')
plt.xlabel('t') 
plt.ylabel(r'$omega(t)$')
plt.grid()
plt.show()

# La siguiente ODE de 2do orden para el angulo 0 de
#un pendulo que actua bajo la gravedad y la accion de
#la friccion es:
#d^2(0)/dt^2 + b*d0/dt + cSin 0 = 0
#Haga un programa que resuelva esta ecuacion en el intervalo
#entre t = 0 y t = 10
#Haga un grafico 0(t) y w(t) en funcion del tiempo
#Asuma que b = 0.25 y c = 5.0
#En la condicion inicial  0 = pi - 0.1 y w = 0
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t=np.linspace(0,10,101)
b=0.25;c=5.0
r0=[np.pi-0.1,0.0]
def f(r,t):
    theta=r[0];omega=r[1]
    dthdt=omega;dodt=-b*omega-c*np.sin(theta)
    dd=[dthdt,dodt]
    return dd
sol=odeint(f,r0,t)
plt.clf()
plt.plot(t,sol[:,0],"r")
plt.title("Theta(t)° and Omega(t)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Theta° and Omgega")
plt.plot(t,sol[:,1])
plt.grid()
plt.tight_layout()
plt.show()

# Dada la siguiente ecuacion diferencial:
# d^2y/dt^2 + (0.9 + 0.7t)dy/dt + Ky = 0
# Haga un programa que resuelva esta ecuacion en el intervalo
# entre t = 0 y t = 2 para distintos valores de K en 
# el rango 5-30, de 5 en 5
# Plotee en un mismo grafico y(t) en funcion del tiempo para
# cada uno de los valores de K
# En la condicion inicial y(0) = 2 y y'(0) = =-1
r0=[2,-1];t=np.linspace(0,2,100)
def func(r,t,K):
    y=r[0];z=r[1]
    dydt=z;dzdt=-(0.9+0.7*t)*z-K*y
    return np.array([dydt,dzdt],float)

plt.clf()
for i in range(5,35,5):
    sol=odeint(func,r0,t,args=(i,))
    plt.plot(t,sol[:,0],label="K"+str(i))
plt.ylabel("y(t)");plt.xlabel("t");plt.legend()
plt.grid()


# El oscilador armonico simple aparece en muchos problemas de
# fisica. Esta dado por la siguiente expresion:
# d2x/dt2 = -w**2*2*x
# Resuelva esta ecuacion para el caso w = 1 en el rango entre
# t = 0 y t = 50
# Como condicion inicial x(0) = 1 y x'(0) = 0
# Haga un grafico x(t) en funcion del tiempo
# Repita ejercicio usando 2 nuevas condiciones iniciales
# x(0) = 2 y x(0) = 4, para x'(0) = 0
# Que pasa con el periodo de las oscilaciones?

t=np.linspace(0,50,100)
r0=[1,0]
def f(r,t):
    x=r[0];y=r[1];omega=1
    dxdt=y;dydt=-omega**2*x
    return np.array([dxdt,dydt],float)
sol=odeint(f,r0,t)
plt.clf()
plt.plot(t,sol[:,0],color="red",label="Condiciones inciales x=1")
plt.tight_layout()
r0=[2,0]
sol=odeint(f,r0,t)
plt.plot(t,sol[:,0],"b",label="Condiciones inciales x=2")
r0=[4,0]
sol=odeint(f,r0,t)
plt.plot(t,sol[:,0],color="black",label="Condiciones inciales x=4")
plt.title("Posición en función del tiempo")
plt.xlabel("Tiempo [s]")
plt.ylabel("Posición [m]")
plt.legend(('A=1','A=2', 'A=4'),loc=1)
plt.grid()
