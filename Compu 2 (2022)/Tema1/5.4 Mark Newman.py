import numpy as np
import pylab as pl

a=0;b=np.pi;n=1000;h=abs(b-a)/n
#####
m=0
x=np.linspace(0,20,100)
def f(theta):
    return np.cos(m*theta-x*np.sin(theta))
s_i=0.0
for k in range(1,n,2):
    s_i+=f(a+k*h)
s_p=0.0
for k in range(2,n-1,2):
    s_p+=f(a+k*h)
j_0=(1/np.pi)*(f(a)+f(b)+4*s_i+2*s_p)
####
m=1
x=np.linspace(0,20,100)
def f(theta):
    return np.cos(m*theta-x*np.sin(theta))
s_i=0.0
for k in range(1,n,2):
    s_i+=f(a+k*h)
s_p=0.0
for k in range(2,n-1,2):
    s_p+=f(a+k*h)
j_1=(1/np.pi)*(f(a)+f(b)+4*s_i+2*s_p)
####
m=2
x=np.linspace(0,20,100)
def f(theta):
    return np.cos(m*theta-x*np.sin(theta))
s_i=0.0
for k in range(1,n,2):
    s_i+=f(a+k*h)
s_p=0.0
for k in range(2,n-1,2):
    s_p+=f(a+k*h)
j_2=(1/np.pi)*(f(a)+f(b)+4*s_i+2*s_p)
pl.plot(x,j_0,"-r",label="J_0")
pl.plot(x,j_1,"-b",label="J_1")
pl.plot(x,j_2,"-g",label="J_2")
pl.title("Funciones de bessel")
pl.xlabel("x")
pl.ylabel("J(m,x)")
pl.grid()
pl.legend()
pl.show()