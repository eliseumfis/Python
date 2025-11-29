#1)

import numpy as np

o=428;n=10;I_traps=[]

def f(x):
    return ((x**3)*np.exp(x))/(np.exp(x)-1)**2
for T in range(5,341,5):
    a=1;b=o/T;h=abs(b-a)/n
    suma_trap=0.0
    for k in range(1,n):
        suma_trap+=f(a+k*h)
    I_trap=h*(((f(a)+f(b))/(2)+suma_trap))
    I_traps.append(I_trap)
import pylab as pl
pl.plot(range(5,341,5),I_traps,"-r",label="I")
pl.title("Integrales respecto a temperaturas")
pl.xlabel("Temperatura [K]")
pl.ylabel("Valor I")
pl.grid()
pl.legend()

pl.show()


#2)

n=2;a=0;b=25;h=(b-a)/n
def g(x):
    return np.exp(-x**2)

suma_impar=0
for k in range(1,n,2):
    suma_impar+=g(a+k*h)
suma_par=0
for k in range(2,n-1,2):
    suma_par+=g(a+k*h)

I_simp_1=(h/3)*(g(a)+g(b)+4*suma_impar+2*suma_par)
Iteraciones=0.0

while True:
    n=n*2;h=b/n
    Iteraciones=Iteraciones+1
    suma_impar=0
    for k in range(1,n,2):
       suma_impar+=g(a+k*h)
    suma_par=0
    for k in range(2,n-1,2):
       suma_par+=g(a+k*h)
    I_simp_2=(h/3)*(g(a)+g(b)+4*suma_impar+2*suma_par)

    error_s2=abs(I_simp_2-I_simp_1)/15
    error_rp_s2=error_s2*100/I_simp_2
    if error_rp_s2<10**(-5):
    
        break
    else:
        I_simp_1=I_simp_2
print("Fueron necesarias",Iteraciones,"iteraciones para alcanzar una exactitud del",100-error_s2,"%")

