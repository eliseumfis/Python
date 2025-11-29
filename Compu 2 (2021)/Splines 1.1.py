from numpy import *
from pylab import*
from scipy.interpolate.interpolate import interp1d

##########################1)

#a)Graficar datos discretos

#x=loadtxt("lineal.txt",float,usecols=0) ; y=loadtxt("lineal.txt",float,usecols=1)
#scatter(x,y)
#xlabel("X")
#ylabel("Y")
#show()

#b)Hacer spline lineal

#x1=x[0]
#xf=x[-1]

#x_fl=linspace(x1,xf,100)
#y_fl=interp(x_fl,x,y)

#scatter(x_fl,y_fl)
#show()


########################2)

#a)Encontrar funcion de numpy

#S=interp1d(x,y)
#y_fl2=S(x_fl)

#scatter(x_fl,y_fl2)
#show()


########################3)

x=loadtxt("cubic.txt",float,usecols=0) ; y=loadtxt("cubic.txt",float,usecols=1)
x1=x[0];xf=x[-1]
x_fl=linspace(x1,xf,100)

Z=interp1d(x,y,kind="cubic")

y_fl=Z(x_fl)
scatter(x,y,color="blue")
plot(x_fl,y_fl,color="red")
show()