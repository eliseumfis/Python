from scipy import integrate as inte
from numpy import *
from matplotlib import *
from pylab import *

#1)
#A)
def f(x):
    return (x**3)/(exp(x)-1)

resultado_integral=inte.romberg(f,0.01,100)
print(resultado_integral)

#B)
kb=1.3806488e-23
c=299792458
h=1.054571818e-34

o=((kb**4)/(4*(pi**2)*(c**2)*(h**3)))*resultado_integral
print(o)