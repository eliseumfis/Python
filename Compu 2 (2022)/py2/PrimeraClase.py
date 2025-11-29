import sys as sys
import numpy as np
"""""""""""
print(sys.float_info)
a=10.245
for n in range(300,800):
    print("exponente",n)
    print(a**n)

#CALCULAR FACOTRIAL DE NÚMEROS ENTEROS


def factorial(n):
    f=1
    for k in range(1,n+1):
        f*=k
    return f
for n in range(0,11):
    print("El factorial para",n,"=",factorial(n))


"""""""""
#CALCULAR FACOTRIAL DE NÚMEROS FLOTANTES

def factorial(n):
    f=1.0
    for k in range(1,n+1):
        f*=k
    return f
for n in range(0,200):
    print("El factorial para",n,"=",factorial(n))

print(factorial)

