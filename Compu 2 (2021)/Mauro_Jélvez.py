from numpy import *
from scipy import integrate
from scipy import interpolate

#1)

 
#a)
a=linspace(2,10,50)
x=linspace(0,15,50)

def T(a):
    def f(x):
        return (x**a-1) * (exp(-x))
    resultado_integral= integrate.quadrature(f, 0, 1)[0]
    return resultado_integral

print(T([2,10]))

#b)



#2)

#a)

#Se definen las variables

A_5=loadtxt("Npersonas_ciudad.txt",float,usecols=0)
P_5=loadtxt("Npersonas_ciudad.txt",float,usecols=1)

from numpy import *
from scipy.interpolate import interp1d
from pylab import *

#Se crea un A poblado

A_5_i=A_5[0];A_5_f=A_5[-1]    ;   A_5_POB=linspace(A_5_i,A_5_f,100)

#Se define la función para luego reemplazar los datos

f=interp1d(A_5,P_5,kind="cubic")

Poblacion_1912=f(1912)
Poblacion_1956=f(1956)
Poblacion_1978=f(1978)
Poblacion_1999=f(1999)
Poblacion_2003=f(2003)

print("La población estimada en 1912 era de:", Poblacion_1912,"habitantes")
print("La población estimada en 1956 era de:", Poblacion_1956,"habitantes")
print("La población estimada en 1978 era de:", Poblacion_1978,"habitantes")
print("La población estimada en 1999 era de:", Poblacion_1999,"habitantes")
print("La población estimada en 2003 era de:", Poblacion_2003,"habitantes")

#b) 
#  Definiremos una variable P poblada

P_5_POB=f(A_5_POB)

#Graficar nuestros datos más las población preguntada

scatter(1912,Poblacion_1912,color="red",marker="*")
scatter(1956,Poblacion_1956,color="red",marker="*")
scatter(1978,Poblacion_1978,color="red",marker="*")
scatter(1999,Poblacion_1999,color="red",marker="*")
scatter(2003,Poblacion_2003,color="red",marker="*")
plot(A_5_POB,P_5_POB,color="blue")
xlabel("Años")
ylabel("Población")
legend()
show()