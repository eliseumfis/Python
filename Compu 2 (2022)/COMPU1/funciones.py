import numpy as np
import statistics

def cartesian(r,theta):
    x=r*np.cos(theta)
    y=r*np.sin(theta)
    position=[x,y]
    return position

def media(lista):
    return sum(lista)/len(lista)

def desviacionestandar(lista):
    media = sum(lista)/len(lista)
    s = 0
    for i in lista:
        s += (i - media) ** 2
    d = len(lista)-1
    return(np.sqrt(s/d))

lis = [1,2,3,4,5,7]
print(desviacionestandar(lis))
print(statistics.stdev(lis))