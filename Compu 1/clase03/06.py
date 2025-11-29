from numpy import *
x=range(1,21)
yf=[]

for n in x:
    y=2*n+3
    yf.append(log(y))

print(yf)

from pylab import *
plot(x,yf)
xlabel="X"
ylabel="Log(y)"
title("Chota")
show()