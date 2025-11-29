from re import X
import scipy.integrate as inte
import numpy as np
vr=1.640533



x=np.array([0,0.12,0.22,0.32,0.36,0.4,0.44,0.54,0.64,0.7,0.8])

def f(x):
    return 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5
fx=f(x)
###Usando metodo trap ########
Itrap=inte.trapz(fx,x)
#print(Itrap)
#print("El error trapezoidal es de",abs(vr-Itrap)*100/vr,"%")

### Simp meth ####
Isimp=inte.simps(fx,x)
#print(Isimp)
#print("El error simpson es de",abs(vr-Isimp)*100/vr,"%")

#### Romberg meth #######
Iromb=inte.romberg(f,0,0.8,show=False)
#print("El error simpson es de",abs(vr-Iromb)*100/vr,"%")

#####Queadrature meth #########
Iqua=inte.quadrature(f,0,0.8)
Erqua=abs(vr-Iqua[0])*100/vr
#print(Iqua,"error quadratura de",Erqua,"%")

#### Integrales dobles ####
def f(y,x):
    return x*y**2
Int2d=inte.nquad(f,[[0,1],[0,2]])
#print(Int2d[0])

### Ejercicio

data=np.loadtxt("perfil_humedad.txt",float)
pwv1=inte.trapz(data[:,0],data[:,1])/9.81
pwv1=inte.simps(data[:,0],data[:,1])/9.81