import numpy as np
vr=4.4

#a)
a=0;b=2;n=1000;h=abs(b-a)/n
def f(x):
    return x**4 -2*x + 1
#simp
s_i=0.0
for k in range(1,n,2):
    s_i+=f(a+k*h)
s_p=0.0
for k in range(2,n-1,2):
    s_p+=f(a+k*h)
simp=(h/3)*(f(a)+f(b)+4*s_i+2*s_p)
#trap
st=0.0
for k in range(1,n):
    st+=f(a+k*h)
s=(f(a)+f(b))/2
trap=h*(s+st)
#b

erps=abs(vr-simp)*100/vr
erpt=abs(vr-trap)*100/vr

print("El método trapezoidal da un resultado de",trap,"y tiene un",erpt,"%","de error")
print("El método simpson da un resultado de",simp,"y tiene un",erps,"%","de error")
