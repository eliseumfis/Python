#f(x)=e^2x+4x^2+2
#1)Calcular las aproximaciones por Trapezoidal y Simpson, utilizando 2, 4, 6 ... 30 secciones.
from numpy import *
valor_real=1583,31232

#TRAPEZOIDAL
a=0.
b=4.
lista_de_resultados_trapezoidal=[]
lista_de_resultados_simpson=[]
errores_trapezoidal=[]
errores_simp=[]

def f(x):
    return exp(2*x) + 4*x**2+2

for n in range(2,31,2):
    h=abs(b-a)/n
    suma_trapezoidal=0
    
    for i in range(1,n):
        suma_trapezoidal=suma_trapezoidal+f(a+h*i)

    resultado_trapezoidal=h*((f(a)+f(b))/2+suma_trapezoidal)

lista_de_resultados_trapezoidal.append(resultado_trapezoidal)    
error_relativo_porcentual_trap=abs(valor_real-resultado_trapezoidal)*100/valor_real
errores_trapezoidal.append(error_relativo_porcentual_trap)

#SIMPSONS

suma_simp_impar=0

for i in range(1,n,2):
    suma_simp_impar=suma_simp_impar+f(a+h*i)

suma_simpson_par=0

for i in range(2,n-1,2):
    suma_simpson_par=suma_simpson_par+(a+h*i)

resultado_simpson=h/3*(f(a))+4*suma_simp_impar+2*suma_simpson_par+f(b)

lista_de_resultados_simpson.append(resultado_trapezoidal)

error_relativo_porcentual_simpson=abs(valor_real-resultado_simpson)*100/valor_real
errores_simp.append(error_relativo_porcentual_simpson)


#GRAFICOS
from matplotlib import *
from pylab import *

subplot(1,2,1)
plot(range(2,31, 2), lista_de_resultados_trapezoidal, label="Trapezoidal")
plot(range(2,31, 2), lista_de_resultados_simpson, label="Simpson")
xlabel("Número de secciones")
ylabel("Resultados de integral")
legend()

subplot(1,2,2)
plot(range(2,31,2), errores_trapezoidal, label="Errores trapezoidal")
plot(range(2,31,2), errores_simp, label="Errores Simpson")
xlabel("Número de secciones")
ylabel("Errores de integración")
legend()
show()