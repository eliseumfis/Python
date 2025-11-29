from math import *
from numpy import *

#a=0.0
#b=2.0
#def f(x):
    #return x**4-2*x+1

#n=10
#h=(b-a)/n

#s=(0.5*f(a)+0.5*f(b))
#for k in range(1,n):
    #s+=f(a+k*h)
#area=s*h
#print(area)

#error_abs=(area-4.4)/4.4*100
#print(error_abs)

#I=1.640533


#def f(x):
    #return 0.2+25*x-200*x**2+675*x**3-900*x**4+400*x**5
#a=0.0;b=0.8

#for n in range(1,17,2):
    #h=abs(b-a)/n
    #suma_trapezoidal=0

    #for i in range(1,n):
        #suma_trapezoidal+=f(a+i*h)

#area=h*((f(a)+f(b))/2+suma_trapezoidal)

#print(area)

#error=abs(area-I)/I*100

#print(error)
def f(x):
    return 8*exp(x)*sin(x)**2+cos(x)
a=0.0
b=pi/2
n=4
sumatoria=0
h=abs(b-a)/n
for i in range(1,n):
    sumatoria=sumatoria+f(a+h*i)
sumatoria=sumatoria+(f(a)+f(b))/2
print(h*sumatoria)
    





















