#1)


from numpy import *
T1=loadtxt("Temperatura_Valparaiso.dat")
t=list(T1)

Dias=0
for n in range(len(t)):
    if (n+1)%8==0:
        Dias+=1
print("La temperatura fue estudiada durante",Dias,"dias")

#2)
l=list[T1]
print(l)

#3)

def prm (d):
    promedio=sum(d)/len(d)
    return(promedio)

for d in t:
    print(prm(d))

#5)
for d in t:
    hrs_noche=[]
    noche.append(d[0])
    noche.append(d[1])
    noche.append(d[6])
    noche.append(d[7])
    prm_noche= prm(noche)
    print("La temperatura promedio en la noche es",hrs_noche,"grados")

#6)
for d in t:
     hrs_dia=[]
     hrs_dia.append([2])
     hrs_dia.append([3])
     hrs_dia.append([4])
     hrs_dia.append([5])
     prm_dia=prm(hrs_dia)
     print("La temperartura promedio de dia es",prm_dia,"grados")

#9)
temperatura_reversa=t[::-1]
print(temperatura_reversa)