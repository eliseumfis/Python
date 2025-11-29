import numpy as np
import pylab as pl

def f(t):
    return np.exp(-t**2)
simp_r=[];fx=[];xx=[]
for x in np.arange(0,3,0.1):
    xx.append(x)
    a=0;b=x;n=100;h=abs(b-a)/n
    fx.append(f(x))
    #simp
    s_i=0.0
    for k in range(1,n,2):
        s_i+=f(a+k*h)
    s_p=0.0
    for k in range(2,n-1,2):
        s_p+=f(a+k*h)
    E=(h/3)*(f(a)+f(b)+2*s_i+4*s_p)
    simp_r.append(E)

pl.subplot(1,2,1)
pl.plot(xx,simp_r,"-r",label="Método simpson")
pl.xlabel("x")
pl.ylabel("E")
pl.title("E(x)")
pl.grid()
pl.legend()

pl.subplot(1,2,2)
pl.plot(xx,fx,"-b",label="f(x)")
pl.xlabel("x")
pl.ylabel("f")
pl.title("f(x)")
pl.grid()
pl.legend()

pl.show()
