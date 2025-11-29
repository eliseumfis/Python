#Metodo trapezoidal Ejercicio 1
import pylab as pl
from numpy import exp

I = []

L = range(5,341,5)

N=10

a = 1. 

#Definir funcion.
def f(x):
    return (x**4*exp(x))/((exp(x)-1)**2) 



for T in range (5, 341, 5):
    b = (428/T)
    h = abs(b-a)/N

    trap = 0

    for i in range (1, N):

        trap = trap + f(a+h*i)


    atrapito = h*((f(a) + f(b)) /2 + trap)

    I.append(atrapito)

pl.plot(L,I)
pl.title("Metodo de integracion trapezoidal")
pl.xlabel("Temperatura")
pl.ylabel("Valores de I")
pl.show()




#Metodo Simpson

def E(x):
    return exp(-(x)**2)

n=2
a1 = 0
b1 = 25
h1 = (b1-a1)/n
impar = 0
    
for i in range(1, n, 2): 


    impar = impar + E(a1+h1*i)

    
par = 0
    

for i in range(2, n-1, 2): 
        
      par = par + E(a1+h1*i)

    
simpson = (h1/3)*(E(a1) + 4*impar + 2*par + E(b1))

iteraciones=0

while True:
    
    n = n*2
    h1 = abs(b1-a1)/n

    iteraciones = iteraciones+1

    impar = 0
    for i in range(1, n, 2):
        impar = impar + E(a1+h1*i)

    par = 0
    for i in range(2, n-1, 2):
        par = par + E(a1+h1*i)

    simpson2 = (h1/3)*(E(a1)+4*impar + 2*par + E(b1))

    errorcito = (abs(simpson2 - simpson))/15

    

    if errorcito < 10**(-5):
        print("El numero de iteraciones es:",iteraciones)
        break
    else:

        simpson = simpson2


print("El error fue:",errorcito)



