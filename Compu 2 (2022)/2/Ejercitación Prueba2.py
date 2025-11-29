from matplotlib import lines
from numpy import *
from pylab import *

###1) Dentro del archivo datos.txt se encuentran dos columnas de datos: la primera corresponde a mediciones
#del eje X, y la segunda corresponde a mediciones del eje Y. Utilizando dichos datos, desarrollar lo siguiente:

#a) Graficar los datos como puntos discretos.
x=loadtxt("datos.txt",float,usecols=0)
y=loadtxt("datos.txt",float,usecols=1)

scatter(x,y)
show()

#b) Integrar los datos discretos por método Trapezoidal.

from scipy import integrate
from scipy.interpolate.interpolate import interp1d
Int_trapz=integrate.trapz(y,x)
print("El resultado por método trapezoidal es:",Int_trapz)


#c) Integrar los datos discretos por método Simpson.
Int_simp=integrate.simps(y,x)
print("La integral por método simpson es:", Int_simp)


###2) Sea la función f(x) = (2 + 3sin(2x))3 integrada desde x=0 hasta x=pi/2

#a) Calcular valor de la integral por método de Romberg.

#def f(x):
    #return (2+3*sin(2*x))**3
#a=0
#b=pi/2

#Int_rom=integrate.romberg(f,a,b)
#print(Int_rom)

#b) Calcular el valor de la integral por método de Cuadratura Gaussiana. Además, explicitar cuál es el
#error estimado del resultado encontrado.

#Int_gau=integrate.quadrature(f,a,b)
#print(Int_gau)

###############################################################################################################################

#Dentro del archivo mediciones.txt se encuentran dos columnas de datos: la primera corresponde a medi-
#ciones del eje X, y la segunda corresponde a mediciones del eje Y. Utilizando dichos datos, desarrollar los
#siguientes ejercicios:

#1)

#a)Graficar los datos como puntos discretos.
#x=loadtxt("mediciones.txt",float,usecols=0)
#y=loadtxt("mediciones.txt",float,usecols=1)

#scatter(x,y)
#show()


#b) Interpolarlos para obtener una función polinómica p(x) que atraviese a todos los puntos.
#from scipy.interpolate import interp1d

#f=interp1d(x,y,kind="cubic")
#xi=x[0];xf=x[-1]
#x_pob=linspace(xi,xf,100)
#y_pob=f(x_pob)

#c) Graficar la función polinómica p(x) sobre los datos discretos ya graficados.

#plot(x_pob,y_pob)
#show()


#2)

#a) Graficar datos discretos
#x=loadtxt("mediciones.txt",float,usecols=0)
#y=loadtxt("mediciones.txt",float,usecols=1)

#scatter(x,y)
#show()

#b) Ajustar a los datos una curva polinómica de primer grado

#P1=poly1d(polyfit(x,y,1))

#c) Ajustar a los datos una curva polinómica de segundo grado

#P2=poly1d(polyfit(x,y,2))

#d) Ajustar a los datos una curva polinómica de tercer grado

#P3=poly1d(polyfit(x,y,3))

#e) Graficar todo

#plot(x_pob,P1(x_pob),color="red",label="Polinomio grado 1")
#plot(x_pob,P2(x_pob),color="blue",label="Polinomio grado 2")
#plot(x_pob,P3(x_pob),color="green",label="Polinomio grado 3")
#legend()
#show()

###############################################################################################################################


#1)  Dentro del archivo lineal.txt, se encuentran dos columnas de datos: la primera corresponde a mediciones
#en el eje X, y la segunda corresponde a mediciones en el eje Y. Con ellas, desarrollar los siguientes ejercicios:

#a) Graficar datos discretos 

#x=loadtxt("lineal.txt",float,usecols=0)
#y=loadtxt("lineal.txt",float,usecols=1)
#scatter(x,y)
#show()

#b) Utilizando la función interp de numpy, efectuar un Spline Lineal sobre los datos discretos, de tal man-
#era que sea posible dibujar una curva (que en realidad estará compuesta por rectas, y no literalmente
#por "curvas") que atraviese a todos los datos discretos.

#xi=x[0];xf=x[-1]

#x_pob=linspace(xi,xf,100)
#y_pob=interp(x_pob,x,y)

#plot(x_pob,y_pob)
#show()


#2) Utilizando el mismo archivo lineal.txt, desarrollar los siguientes ejercicios:

#a) Graficar los datos como puntos discretos.

#x=loadtxt("lineal.txt",float,usecols=0)
#y=loadtxt("lineal.txt",float,usecols=1)
#scatter(x,y)
#show()

#b) Definir una función llamada S(x) que permita dibujar un Spline Lineal sobre los datos discretos.
#S=interp1d(x,y)
#y_pob=S(x_pob)

#plot(x_pob,y_pob)
#show()

#3) En el archivo cubic.txt se encuentran dos columnas de datos: la primera corresponde a mediciones en el
#eje X, y la segunda corresponde a mediciones en el eje Y. Utilizando estos datos, desarrollar los siguiente
#ejercicios:

#a) Graficar los datos como puntos discretos.

#x=loadtxt("cubic.txt",float,usecols=0)
#y=loadtxt("cubic.txt",float,usecols=1)

#scatter(x,y)
#show()

#b) Definir una función llamada Z(x) que permita dibujar un Spline Cúbico sobre los datos discretos.

#Z=interp1d(x,y,kind="cubic")

#c) Graficar el Spline Cúbico sobre los datos discretos.

#xi=x[0];xf=x[-1]
#x_pob=linspace(xi,xf,100)
#y_pob=Z(x_pob)

#plot(x_pob,y_pob)
#show()

#4) En el archivo temp_pressure_PP2.txt se encuentran tres columnas de datos atmosféricos: la primera
#corresponde a mediciones de altura en [km], la segunda corresponde a mediciones de temperatura en [K], y
#la tercera corresponde a mediciones de presión en [Pa]. Asuma los datos como exactos (¡como si no tuvieran
#error experimental!).
#Ahora, existe una propiedad llamada temperatura potencial, la cual denotaremos por "o". Esta propiedad
#depende tanto de la temperatura como de la presión:
# o(T, p) = T*(p/p_0)**(R/cp)

#p0=100000
#R=8.31
#cp=2.91

#a) Calcular cuál será el valor de la temperatura potencial O a 2.2 [km] y a 5.8 [km] de altura.

#h=loadtxt("temp_pressure_PP2.txt",float,usecols=0)
#T=loadtxt("temp_pressure_PP2.txt",float,usecols=1)
#p=loadtxt("temp_pressure_PP2.txt",float,usecols=2)

#def TP(T,p):
    #o=T*(p/p0)**(R/cp)
    #return o

#Temp_pot_datosconocidos=TP(T,p)

#TP_funcion=interp1d(h,Temp_pot_datosconocidos,kind="cubic")

#print("La temperatura potencial a 2.2 km será de:",TP_funcion(2.2),"K")
#print("La temperatura potencial a 5.8 km será de:",TP_funcion(5.8),"K")

#b) Elaborar un gráfico continuo (¡no de puntos discretos!) que muestre cómo varía la temperatura
#potencial θ respecto a la altura en [km].

#plot(h,TP_funcion(h))
#show()


###############################################################################################################################

#1) Existe un fenómeno físico denominado como oscilación anarmónica, en el cual una partícula oscila con un
#período (que llamaremos "T") que depende de la amplitud de oscilación (que llamaremos "a").
#Esta dependencia está representada por la siguiente ecuación:

#m=1
#def v(x):
    #return x**4

#a) Elaborar una función de Python que, dado un valor para la amplitud "a", calcule su período "T"
#(utilizar Cuadratura Gaussiana para integrar). Utilizar esta función para encontrar el valor del período
#cuando a = 1.

#def T(a):

    #def f(x):
        #return 1/sqrt(v(a)-v(x))
    #resultado_integral=integrate.quadrature(f,0,a)[0]
    #return sqrt(8*m)*resultado_integral

#print("El valor de T cuando a=1 es:", T(1))

#b) Elaborar un gráfico que muestre cómo va cambiando el período "T" a medida que el valor de la amplitud
#"a" va variando desde a = 0 hasta a = 2.

#amplitudes=linspace(0,2,100)
#T_ampl=[]
#for amplitud in amplitudes:
    #periodos=T(amplitud)
    #T_ampl.append(periodos)

#plot(amplitud,T_ampl)
#show()