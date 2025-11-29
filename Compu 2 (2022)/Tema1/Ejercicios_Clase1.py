#Oscilador armónico cuántico
"""
from math import exp
terms=1000;h=w=1
beta=1/100;S=0.0;Z=0.0
for n in range(terms):
    En=h*w*(n+0.5)
    peso=exp(-beta*En)
    S+=peso*En
    Z+=peso
print(S/Z)
"""
#Escriba programa que tome 3 numeros como entrada: a, b y
#c, e imprima las soluciones de ecuacionn cuadratica
#ax^2 + bx + c = 0 usando la formula estandar:

from cmath import sqrt


a=float(input("Ingrese el valor de a: "));b=float(input("Ingrese el valor de b: "));c=float(input("Ingrese el valor de c: "))
valores=a,b,c
x1=(-b+sqrt(b**2-4*a*c))/2*a;x2=(-b-sqrt(b**2-4*a*c))/2*a
print(x1,x2)