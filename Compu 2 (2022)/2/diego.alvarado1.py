from scipy import integrate, interpolate
from numpy import exp,linspace,loadtxt
import pylab as pl
from math import factorial
#Ejercicio 1


A=0
B=15

def funcion (a):
    def r(x):

        return (x**(a-1))*exp(-x)

    return integrate.romberg(r,A,B,show=False)

#Al utilizar la funcion con el valor de a deseado encontrara la integral.




#Ejercicio 2

anos=loadtxt("Npersonas_ciudad.txt",float, usecols=0)

poblacion=loadtxt("Npersonas_ciudad.txt",float, usecols=1)


S=interpolate.interp1d(anos,poblacion,kind='cubic')


print("Poblacion en 1912,1956,1978,1999,2003 respectivamente", S(1912), S(1956), S(1978), S(1999), S(2003))

poblacionestimada=[S(1912),S(1956),S(1978),S(1999),S(2003)]
anos1=[1912,1956,1978,1999,2003]

pl.plot(anos,poblacion,color='black')
pl.scatter(anos1,poblacionestimada,marker='*')
pl.xlabel("Años")
pl.ylabel("Poblacion")
pl.grid()
pl.show()

