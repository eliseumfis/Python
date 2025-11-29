import numpy as np
import pylab as pl

#1)
def f(x):
    return (x**(4) * np.exp(x))/(np.exp(x)-1)**2
n=10;o=428;trap=[];Temp=[]
for T in range(5,340,5):
    Temp.append(T)
    a=1;b=o/T;h=abs(b-a)/n
    st=0.0
    for k in range(1,n):
        st+=f(a+k*h)
    I=h*(1/2*(f(a)+f(b))+st)
    trap.append(I)
pl.plot(Temp,trap,"-r",label="I")
pl.xlabel("T [k]");pl.ylabel("I")
pl.grid()
#pl.show()

#2)
def f(x):
    return np.exp(-x**2)
a=0;b=25;n=2;h=abs(b-a)/n
ex=10**-5
suma_impar=0
for k in range(1,n,2):
    suma_impar+=f(a+k*h)
suma_par=0
for k in range(2,n-1,2):
    suma_par+=f(a+k*h)

I_simp_1=(h/3)*(f(a)+f(b)+4*suma_impar+2*suma_par)
Iteraciones=0.0

while True:
    a=0;b=25;n=n*2;h=abs(b-a)/n
    ex=10**-5
    Iteraciones=Iteraciones+1
    suma_impar=0
    for k in range(1,n,2):
       suma_impar+=f(a+k*h)
    suma_par=0
    for k in range(2,n-1,2):
       suma_par+=f(a+k*h)
    I_simp_2=(h/3)*(f(a)+f(b)+4*suma_impar+2*suma_par)
    er=abs(I_simp_2-I_simp_1)/15
    errp=er*100/I_simp_2
    if errp<ex:
        break
    else:
        I_simp_1=I_simp_2
print("Se necestiaron",Iteraciones,"para alcanzar una exactitud del",100-errp,"%")

