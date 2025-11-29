from scipy import integrate as inte
from numpy import *
from matplotlib import *
from pylab import *

#EJERCICIO 1

#A)
m=1
def V(x):
    return x**4

def T(a):

    def f(x):
        return 1/sqrt(V(a)-V(x))
    resultado_integral=inte.quadrature(f,0,a)[0]
    return sqrt(8*m)*resultado_integral

print(T(1))

#B)

amplitudes=linspace(0,2,100)
lista_periodos=[]
for amplitud in amplitudes:
    periodo=T(amplitud)
    lista_periodos.append(periodo)

plot(amplitudes,lista_periodos)
xlabel="Amplitudes"
ylabel="Períodos"
legend()
show()