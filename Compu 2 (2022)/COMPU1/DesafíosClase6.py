from numpy import arctan
from math import sqrt,pi 

x=float(input("Ingrese el valor de la coordenada x: "))
y=float(input("Ingrese el valor de la coordenada y: "))

r=sqrt(x**2+y**2)
theta=arctan(y/x)
theta1=theta*180/pi

print("El valor de las coordenadas x,y en coordenas polares son",r,theta1)

n = int(input("valor: "))
while n!=0:
    print(n)
    n -= 1