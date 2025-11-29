
import numpy as np
def f(x):
    return np.sqrt(1-x**2)
a=-1;b=1;vr=(1/2)*np.pi
trap_r=[];trap_e=[];simp_r=[];simp_e=[];N=[]
#a)
for n in range(10,1001,10):
    h=abs(b-a)/n
    #Trapezoidal
    st=0.0
    for k in range(1,n):
        st+=f(a+k*h)
    trap=h*((f(a)+f(b)/2)+st)
    trap_r.append(trap)
    errt=abs(vr-trap)*100/vr
    trap_e.append(errt)
    #Simpson
    s_i=0.0
    for k in range(1,n,2):
        s_i+=f(a+k*h)
    s_p=0-0
    for k in range(2,n-1,2):
        s_p+=f(a+k*h)
    simp=(h/3)*(f(a)+f(b)+4*s_i+2*s_p)
    simp_r.append(simp)
    errs=abs(vr-simp)*100/vr
    simp_e.append(errs)
print("El valor de la integral por método trapezoidal es",trap,"y tiene un",errt,"%","de error")
print("El valor de la integral por método simpson es",simp,"y tiene un",errs,"%","de error")
#b)
import pylab as pl

pl.subplot(1,2,1)
pl.plot(range(10,1001,10),trap_r,"-r",label="Trapezoidal")
pl.plot(range(10,1001,10),simp_r,"-b",label="Simpson")
pl.title("Integral en función de n")
pl.xlabel("Secciones [n]")
pl.ylabel("I")
pl.legend()

pl.subplot(1,2,2)
pl.plot(range(10,1001,10),trap_e,"-r",label="Error trapezoidal")
pl.plot(range(10,1001,10),simp_e,"-b",label="Error simpson")
pl.title("Error relativo porcentual")
pl.xlabel("Secciones [n]")
pl.ylabel("Error [%]")
pl.legend()

pl.show()


###############################################################################

import numpy as np
def f(t):
    return 1/np.exp(t**2)
trap_r=[];simp_r=[];fx=[]
steps=0.1

for x in np.arange(0,6,0.1):
    fx.append(f(x))
    n=1000
    a=0;b=x;h=abs(b-a)/n
    #trap
    st=0.0
    for k in range(1,n):
        st+=f(a+k*h)
    trap=h*(0.5*f(a)+0.5*f(b)+st)
    trap_r.append(trap)
    #simp
    s_i=0.0
    for k in range(1,n,2):
        s_i+=f(a+k*h)
    s_p=0.0
    for k in range(2,n-1,2):
        s_p+=f(a+k*h)
    simp=(h//3)*(f(a)+f(b)+4*s_i+2*s_p)
    simp_r.append(simp)

import pylab as pl

pl.subplot(1,2,1)
pl.plot(np.arange(1,6,0.1),fx)
pl.title("F(x)")
pl.xlabel("x")
pl.ylabel("Valores de la función en de x")
pl.grid()

pl.subplot(1,2,2)
pl.plot(np.arange(1,6,0.1),trap_r,"-r",label="Trapezoidal")
pl.plot(np.arange(1,6,0.1),simp_r,"-b",label="Simpson")
pl.xlabel("x") 
pl.ylabel("Valor de I")   
pl.title("E(x)") 
pl.grid()
pl.legend() 
pl.show()  


    
