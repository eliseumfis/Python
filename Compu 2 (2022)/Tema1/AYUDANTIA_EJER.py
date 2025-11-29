#1)
import numpy as np
"""

def f(x):
    return np.e**(2*x) + 4**2 + 2
a=0;b=4;vr=1583.31232
trap_r=[];trap_e=[];simp_r=[];simp_e=[]

#a)

for n in range(2,31,2):
    h=abs(b-a)/n
    #Trapezoidal
    strap=0.0
    for k in range(1,n):
        strap+=f(a+k*h)
    trap=h*(((f(a)+f(b))/2 +strap))
    trap_r.append(trap)
    errt=(vr-trap)*100/vr
    trap_e.append(errt)
    #Simpson
    s_i=0.0
    for k in range(1,n,2):
        s_i+=f(a+k*h)
    s_p=0.0
    for k in range(2,n-1,2):
        s_p+=f(a+k*h)
    simp=(h/3)*(f(a)+f(b)+4*s_i+2*s_p)
    simp_r.append(simp)
    errs=(vr-simp)*100/vr
    simp_e.append(errs)

#c)
import pylab as pl

pl.subplot(1,2,1)
pl.plot(range(2,31,2),trap_r,"-r",label="I(n) Trapezoidal")
pl.plot(range(2,31,2),simp_r,"-b",label="I(n) Simpson")
pl.title("Integrales en funcion de n")
pl.xlabel("Número de secciones [n]")
pl.ylabel("Valores de Integral")
pl.grid()
pl.legend()

pl.subplot(1,2,2)
pl.plot(range(2,31,2),trap_e,"-r",label="Error Trapezoidal")
pl.plot(range(2,31,2),simp_e,"-b",label="Error Simpson")
pl.title("Error relativo porcentual")
pl.xlabel("Número de secciones [n]")
pl.ylabel("Error")
pl.grid()
pl.legend()

pl.show()
"""
#2)

def f(x):
    return 8*np.exp(x)*np.sin(x)**2 + np.cos(x)
a=0;b=np.pi/2;n=4;h=abs(b-a)/n
#trapezoidal
st=0.0
for k in range(1,n):
    st+=f(a+k*h)
trap1=h*(0.5*f(a)+0.5*f(b)+st)

while True:
    
    n=n*2;h=abs(b-a)/n
    st=0.0
    for k in range(1,n):
       st+=f(a+k*h)
    trap2=h*(0.5*f(a)+0.5*f(b)+st)
    
    error_practico=abs(trap2-trap1)/3
    errp=error_practico*100/trap2
    if errp<0.001:
        break
    else:
        trap1=trap2
print("El resultado que cumple la condicion por método trapezoidal es:",trap2,"y el número de secciones necesarias fue",n)



