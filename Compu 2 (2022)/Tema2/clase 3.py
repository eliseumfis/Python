import scipy.integrate as inte 
import numpy as np 

x=np.array([0, 0.12, 0.22, 0.32, 0.36, 0.4, 0.44, 0.54, 0.64, 0.7, 0.8])
def f(x):
    return 0.2+25*x-200*x**2+675*x**3-900*x**4+400*x**5
fx=f(x)
Itrap=inte.trapz(fx,x)
print(Itrap)


#####

from numpy import *
from scipy import *

first=trapz([1,2,3])
second=trapz([1,2,3] , x=[4,6,8])
third=trapz([1,2,3], dx=2) #print(third)
a=arange(6).reshape(2,3) #a
trapz([1.5, 2.5, 3.5])
trapz(a, axis=0)
trapz(a, axis=1)


######


from numpy import *
from scipy import *
def f(x):
    return 0.2+25*x-200*x**2+675*x**3-900*x**4+400*x**5

Vr=1.640533; xx=arange(0, 0.85, 0.05); fx=f(xx)

####Metodo trapezoidal####
Itrap=inte.trapz(fx,xx); Er_Tr=abs(Vr-Itrap)/Vr*100
print("Error M. Trapezoidal=", Er_Tr,"%")

####Metodo simpson####

Isimp = inte.simps(fx,xx); Er_Simp=abs(Vr-Isimp)/Vr*100

print("Error M. Simpson=", Er_Simp,"%")


#######



from numpy import *
from scipy import *


def f(x):
    return 0.2+25*x-200*x**2+675*x**3-900*x**4+400*x**5

Vr= 1.640533

#### Metodo de Romberg ####

IRomb= inte.romberg(f, 0, 0.8, show=True)
Er_Romb=abs(Vr-IRomb)/Vr*100
print("Error M. Romberg=", Er_Romb,"%")


#######



from numpy import *
from scipy import *


def f(x):
    return 0.2+25*x-200*x**2+675*x**3-900*x**4+400*x**5

Iqua = inte.quadrature(f,0, 0.8)
Vr= 1.640533; Er_qua=abs(Vr- Iqua[0])/Vr*100
print("Error M. Q. Gaussiana=",Er_qua,"%")


#####

#### Calculando integrales dobles####
from numpy import *
from scipy import *


def f(x,y):
    return x*y**2 
Int2d=inte.nquad(f, [[0,1] , [0,2]])
print(Int2d)

####


#Ejercicio

#El archivo perfil_humedad.txt contiene datos de razon de mezcla de agua (qv) y presion (p), calcule el agua precipitable (PWV) con la siguiente formula:  PWV= 1/g int(qv), (f,[p0,p1])
from numpy import *
from scipy import integrate as inte
def f(x):
    return x
g=9.81

data = loadtxt('perfil_humedad.txt',float)
pwv1=-inte.trapz(data[:,0], data[:,1])/g ;print(pwv1)
pwv2=-inte.simps(data[:,0], data[:,1])/g ; print(pwv2)
pwv3=-inte.quadrature(f, (data[:,0], data[:,1]), show=True)/g; print(pwv3)
