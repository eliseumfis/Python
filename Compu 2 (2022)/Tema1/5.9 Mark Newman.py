
import numpy as np
import pylab as pl
o=428;p=6.022*10**28;v=1*10**(-6);kb=1.28064852*10**(-23);n=50
cv=[];Temp=[]
def f(x):
    return (x**4 * np.exp(x))/(np.exp(x) -1)**2
for T in np.linspace(5,500,50):
    a=1;b=o/T;h=abs(b-a)/n
    Temp.append(T)
    kk=9*v*p*kb*(T/3)**3
    si=0.0
    for k in range(1,n,2):
        si+=f(a+k*h)
    sp=0.0
    for k in range(2,n-1,2):
        sp+=f(a+k*h)
    simp=(h/3)*(f(a)+f(b)+4*si+2*sp)
    cvv=simp*kk
    cv.append(cvv)
pl.plot(Temp,cv)
pl.show()