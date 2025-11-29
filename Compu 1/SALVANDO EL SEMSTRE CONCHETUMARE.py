from numpy import *
s=0.0
for k in range(1,101):
    s += 1/k
print(s)

x=range(1,20)
yf=[]
for n in x:
    y=2*n+3
    yf.append(log(y))

print(yf)

from pylab import *

plot(x,yf)
xlabel="x"
ylabel="log(y)"
title("mis ganas de verte")
show()



#data=loadtxt("TMP_VALPO.dat",float)

#x=data[:,0]
#y=data[:,1]
#plot(x,y)
#show()

data=loadtxt("stars.dat",float)
x=data[:,0]
y=data[:,1]
scatter(x,y)
xlabel="Temperatura"
ylable="Magnitud"
xlim(0,13000)
ylim(-5,20)
legend()
show()