import sys as sys
#for ii in range(300,800):
    #print("exponente",ii)
    #print(5.523**ii)

#CALCULAR FACOTRIAL DE NÚMEROS ENTEROS

def factorial(x):
    f=1
    for k in range(1,x+1):
        f*=k
    return f
for ii in range(0,11):
    print("El factorial para",ii,"=",factorial(ii))

#CALCULAR FACOTRIAL DE NÚMEROS FLOTANTES

def factorial(x):
    f=1.0
    for k in range(1,x+1):
        f*=k
    return f
for ii in range(0,180):
    print("El factorial para",ii,"=",factorial(ii))