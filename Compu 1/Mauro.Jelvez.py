from numpy import *
from pylab import *

dataT1=loadtxt("T1.dat",float)
dataT2=loadtxt("T2.dat",float)
dataP1=loadtxt("P1.dat",float)
dataP2=loadtxt("P2.dat",float)
T1=dataT1[:]
T2=dataT2[:]

Densidad1=[]
Densidad2=[]
#1) Programa que calcule la densidad del aire
for n in dataP1:
    P=n/(T1*286.9)
    Densidad1.append(P)
for n in dataP2:
    P=n/(T2*286.9)
    Densidad2.append(P)

#2)
PromT1=sum(dataT1)/len(dataT1)
PromT2=sum(dataT2)/len(dataT2)
PromP1=sum(dataP1)/len(dataP1)
PromP2=sum(dataP2)/len(dataP2)
PromD1=sum(Densidad1)/len(Densidad1)
PromD2=sum(Densidad2)/len(Densidad2)

print("El promedio de temperatura, presion y densidad del aire a una altura de 2 metros de altura es",PromT1,"kelvins,",PromP1,"bares y",PromD1,"kg/m**3.")
print("El promedio de temperatura, presion y densidad del aire a una altura de 15 kilometros de altura es",PromT2,"kelvins,",PromP2,"bares y",PromD2,"kg/m**3.")
#3)
plot(Densidad1,"--r")
plot(Densidad2,"-ob")
xlabel("Altura")
ylabel("Densidad")

show()

#4)
print("Se espera tener una mayor de densidad mientras más cerca esté uno del nivel del mar, ya que a mayor altura menor densidad y lamentablemnte mis resultados no coinciden con lo esperado.")


#5)

scatter(dataT1,dataP1)
xlabel("Temperatura a 2 metros de altura")
ylabel("Presion a 2 metros de altura")
show()

scatter(dataT2,dataP2)
xlabel("Temperatura a 15km de altura")
ylabel("Presion a 15km de altura")
show()