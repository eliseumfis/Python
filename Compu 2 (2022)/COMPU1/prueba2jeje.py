import numpy as np
temp = np.loadtxt("Temperatura_Valparaiso.dat")
#1) Muestre por pantalla cuantos días posee el registro.

d1=temp[0:8];d2=temp[8:16];d3=temp[16:24];d4=temp[24:32];d5=temp[32:40];d6=temp[32:40];d7=temp[48:56];d8=temp[56:64];d9=temp[64:72];d10=temp[72:80];d11=temp[80:88];d12=temp[88:96]
#print("El registro posee",np.size(temp)*3/24,"días")

#2) Cree listas para cada día completo.

d1=temp[0:8];d2=temp[8:16];d3=temp[16:24];d4=temp[24:32];d5=temp[32:40]
d6=temp[32:40];d7=temp[48:56];d8=temp[56:64];d9=temp[64:72];dd10:temp[72:80];d11=temp[80:88];d12=temp[88:96]


#3) Cree una función que calcule el promedio y otra función que calcule la desviación
#estándar
def media(lista):
    return sum(lista)/len(lista)

def desviacionestandar(lista):
    media = sum(lista)/len(lista)
    s = 0
    for i in lista:
        s += (i - media) ** 2
    d = len(lista)-1
    return(np.sqrt(s/d))


#4) Calcular promedio y desviacion estanadar de cada día

#La variable dias representa cada 3 hrs

dias=np.asarray([d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12])
#for n in dias:
    #print("El promedio de temperatura es",media(n))
    #print("La desviación estander es",desviacionestandar(n))

#5) Utilizando las funciones creadas en el punto 2, calcule la temperatura promedio y
#desviación estándar del total de las horas de noche. Considerar dia desde 6pm a 6am

noche=np.delete(dias,(1,2,3,4),axis=1)   
#for n in noche:
    #print("El promedio de la noche es:",media(n),"y su desviacion estandar es:",desviacionestandar(n))

#6) Utilizando las funciones creadas en el punto 2, calcule la temperatura promedio y
#desviación estándar del total de las horas de día.

sunny=dias[:,1:5]
#for n in sunny:
    #print("El promedio de el dia es:",media(n),"y su desviacion estandar es:",desviacionestandar(n))

#7) Que dia fue el más caluroso?

maximos = list(map(lambda x: max(x), sunny))
valmax=None

for n in maximos:   #CICLO PARA ENCONTRAR VALOR MAXIMO EN UNA LISTA
    if (valmax is None or n>valmax):
        valmax=n

print("El valor mas calido fue",valmax) #el dia mas caluroso fue el dia mas caluroso

#8) Que dia fue mas frio?

minimos = list(map(lambda x: min(x), sunny))
valmin=None

for n in minimos:   #CICLO PARA ENCONTRAR VALOR MINIMO EN UNA LISTA
    if (valmin is None or n<valmin):
        valmin=n
print("El valor mas frio es:", valmin) #el dia 12 fue el mas frio

#9) Construya un arreglo con los días inversos, es decir que el día 1 sea el último.
inversos_d=dias[::-1]
#print(inversos_d)

#10) Cree un gráfico simple que muestre la temperatura del archivo original y la temperatura
# de los días inversos construidos en el punto 9.
tiempo=np.linspace([1,12],[1,8],12,96)

import pylab as pl
#pl.subplot(1,2,1)
pl.plot(dias,tiempo)
pl.xlabel("Dias");pl.ylabel("Temperatura");pl.title("Temperatura en función de los 12 dias transcurridos")

pl.subplot(1,2,2)
pl.plot(inversos_d,tiempo)
pl.xlabel("Dias");pl.ylabel("Temperatura");pl.title("Temperatura inversa en función de los 12 dias transcurridos")

pl.show()

