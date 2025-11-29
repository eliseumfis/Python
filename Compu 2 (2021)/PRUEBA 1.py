
from numpy import *
from math import *
from matplotlib import *
from pylab import *

#1)
#a)
Val_Inte=[]
T=[]
a=1
o_d=428
for tt in range(5,341,5):
    T.append(tt)
    b=o_d/tt
n=10
h=(b-a)/n

def f(x):
    return (x**4*exp(x))/(exp(x)-1)**2

s=0
for i in range(1,n):
        s+=(f(a+h*i)+(f(a)+f(b))/2)*h
print(s)
       
Val_Inte.append(s)
    
        

#b)
plot(Val_Inte,T)
xlabel("Valor integrales")
ylabel("Temperatura en K")
legend()
show()

#2)
a=0
b=25
n=2
def f(x):
    return exp(-x**2)
h=abs(b-a)/n

suma_simp_impar=0

for i in range(1,n,2):
    suma_simp_impar=suma_simp_impar+f(a+h*i)

suma_simpson_par=0

for i in range(2,n-1,2):
    suma_simpson_par=suma_simpson_par+(a+h*i)

resultado_simpson=h/3*(f(a))+4*suma_simp_impar+2*suma_simpson_par+f(b)

























