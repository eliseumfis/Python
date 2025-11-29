import numpy as np
#1) Diferencias finitas y adelantadas.

def f(x):
    return 3*np.exp(x) * np.sin(x**3)
h=0.0001
a=4
vr=3231.52905

#ADELANTADA

fa=(f(a+h)-f(a))/h
ea=abs(vr-fa)*100/vr
print("La derivada por diferencia adelantada es:",fa,"y tiene un error del",ea,"%")

#ATRASADA

fat=(f(a)-f(a-h))/h
eat=abs(vr-fat)*100/vr
print("La derivada por diferencia atrasada es:",fat,"y tiene un error del",eat,"%")

#CENTRADA

fc=(f(4+h)-f(4-h))/(2*h)
ec=abs(vr-fc)*100/vr
print("La derivada por diferencia centrada es:",fc,"y tiene un error del",ec,"%")

#2) Aumentar nivel de exactitud

#ADELANTADA

fa=(4*f(a+h)-3*f(a)-f(a+2*h))/(2*h)
ea=abs(vr-fa)*100/vr
print("La derivada por diferencia adelantada más exacta es:",fa,"y tiene un error del",ea,"%")

#ATRASADA

fat=(4*f(a+h)-3*f(a)-f(a+2*h))/(2*h)
eat=abs(vr-fat)*100/vr
print("La derivada por diferencia atrasada más exacta es:",fat,"y tiene un error del",eat,"%")

#CENTRADA

fc=(8*f(a+h)-8*f(a-h)-f(a+2*h)+f(a-2*h))/(12*h)
ec=abs(vr-fc)*100/vr
print("La derivada por diferencia centrada más exacta es:",fc,"y tiene un error del",ec,"%")
