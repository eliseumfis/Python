############################################         1)
#Sea la función f(x)=e^2x + 4x^2 + 2, integrada desde 0 a 4.

#a) Calcular las aproximaciones por Trapezoidal y Simpson, utilizando 2, 4, 6 ... 30 secciones. Ir guardando
#los resultados de Trapezoidal en una lista, y los de Simpson en otra lista.

#b) Calcular los errores relativos porcentuales (respecto al valor real de la integral, el cual es 1583,31232)
#para cada una de las aproximaciones del ítem a). Ir guardando los errores relativos porcentuales de las
#aproximaciones Trapezoidales en una lista, y los errores relativos porcentuales de las aproximaciones
#Simpson en otra lista.

#c) Realizar dos gráficos contiguos: el de la izquierda debe ser un gráfico que muestre tanto los resultados
#de Trapezoidal como los de Simpson vs. número de secciones. El de la derecha debe ser un gráfico que
#muestre tanto los errores relativos porcentuales de Trapezoidal como los de Simpson vs. número de
#secciones.




import numpy as np



def f(x):
    return np.exp(2*x) + 4*x**2 + 2
a=0;b=4;vr=1583.31232
trap_r=[];simp_r=[];trap_e=[];simp_e=[];Nn=[]

for n in range(2,31,2):
#1) TRAPEZOIDAL

    h=abs(b-a)/n
    Nn.append(n)
    suma_trap=0.0
    for k in range(1,n):
        suma_trap+=(f(a+k*h))
    I_trap=h*((f(a)+f(b))/(2)+suma_trap)
    trap_r.append(I_trap)
    error_rp=(abs(vr-I_trap)/(vr))*100
    trap_e.append(error_rp)
#2) SIMPSON
    suma_impar=0.0
    for k in range(1,n,2):
        suma_impar+=f(a+k*h)
    
    suma_par=0.0
    for k in range(2,n-1,2):
        suma_par+=f(a+k*h)
    I_simp=(h/3)*(f(a)+f(b)+4*suma_impar+2*suma_par)
    simp_r.append(I_simp)
    error_rps=(abs(vr-I_simp)/vr)*100
    simp_e.append(error_rps)

#Gráficos
import pylab as pl
pl.subplot(1,2,1)
pl.plot(range(2, 31, 2), trap_r, '-b',label="Trapezoidal")
pl.plot(range(2,31,2), simp_r, '-r',label="Simpson")
pl.title('Valores de la integral')
pl.xlabel('N° de secciones');pl.ylabel('Valores de I')
pl.grid()
pl.legend()

pl.subplot(1,2,2)
pl.plot(range(2, 31, 2), trap_e, '-b',label="Trapezoidal")
pl.plot(range(2,31,2), simp_e, '-r',label="Simpson")
pl.title('Error relativo porcentual')
pl.xlabel('N° de secciones');pl.ylabel('Valores de Error')
pl.grid()
pl.legend()

pl.show()



#2)

def f(x):
    return 8*np.exp(x)*np.sin(x)**2 + np.cos(x)
a = 0 ; b = np.pi / 2 ; n = 4
h = np.abs(b-a)/n

#TRAPEZOIDAL
suma=0.0
for k in range(1,n):
    suma+=f(a+k*h)
trap_1=h*((f(a)+f(b)/2)+suma)
while True:
    n=2*n
    h=abs(b-a)/n
    suma=0.0
    for k in range(1,n):
        suma+=f(a+k*h)
    trap_2=h*((f(a)+f(b)/2)+suma)
    error_t2 = np.abs(trap_2 - trap_1) / 3
    error_rp_t2 = error_t2*100 /trap_2
    if error_rp_t2 < 0.001:
        break
    else:
        trap_1 = trap_2
print("El resultado que cumple la condicion por método trapezoidal es:",trap_2,"y el número de secciones necesarias fue",n)


#SIMPSON

n=4;a=0;b=np.pi/2;h=abs(b-a)/n

suma_impar=0.0
for k in range(1,n,2):
        suma_impar+=f(a+k*h)
    
suma_par=0.0
for k in range(2,n-1,2):
        suma_par+=f(a+k*h)
simp_1=(h/3)*(f(a)+f(b)+4*suma_impar+2*suma_par)


while True:
    n=2*n
    h=abs(b-a)/n

    suma_impar=0.0
    for k in range(1,n,2):
        suma_impar+=f(a+k*h)
    
    suma_par=0.0
    for k in range(2,n-1,2):
       suma_par+=f(a+k*h)
    
    simp_2=(h/3)*(f(a)+f(b)+4*suma_impar+2*suma_par)
    
    error_s2=abs(simp_2-simp_1)/15
    error_rp_s2=error_s2*100/simp_2
    if error_rp_s2<0.001:
        break
    else:
        simp_1=simp_2
print("El resultado que cumple la condicion por método trapezoidal es:",simp_2,"y el número de secciones necesarias fue",n)
