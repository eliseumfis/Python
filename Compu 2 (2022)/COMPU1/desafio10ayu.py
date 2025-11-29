import numpy as np
import statistics
from matplotlib import pyplot as pl

def media(lista):
    return(sum(lista)/len(lista))

def desviacionestandar(lista):
    s = 0
    media = sum(lista)/len(lista)
    for i in lista:
        s += (i - media)**2
    d = len(lista)-1
    return(np.sqrt(s/d))

def media(arreglo,fila):
    m = arreglo[fila-1,]
    s = 0
    for i in range(len(m)):
        s += m[i]
    d = len(m)
    return(s/d)

def desviacion(arreglo,fila=1):					
	m = arreglo[fila-1,]
	s = 0
	for r in range(len(m)):             
		s += (m[r]-media(arreglo,fila))**2
	return(np.sqrt(s/(len(m)-1)))

temp = np.loadtxt("TMPVALPO.dat")
#print(temp)
#print(temp.size)
#print(len(temp),len(temp[0]))

print(desviacion(temp,1))

print(temp[0,])
pl.title("Grafico Temperatura en función del tiempo")
pl.xlabel("Tiempo")
pl.ylabel("Temperatura")
pl.plot(temp[0,],label='Primera Fila')
pl.plot(temp[9,],label='Segunda Fila')
pl.plot(temp[4,],label='Tercera Fila')
pl.legend()
pl.savefig("image_final")
pl.show()