import numpy as np
from scipy.optimize import fsolve
print("1)")
print("")
#Datos

c1=250e-6;c2=310e-6
r1=1200;r2=4700;r3=3200
x0=2.5;x3=5
w=350

#a)

print("          a)")
print(" ")
#Matriz de coeficientes de x1 y x2

A=np.array([[1/r1 - c1*w - c2*w, c2*w],[c2*w,1/r2 -c2*w + 1/r3]])

#Matriz de valores

V=np.array([[x3/r1 + c1*w*x0],[x3/r2 + x0/r3]])

sol=np.linalg.solve(A,V)

for i in np.arange(0,2,1):
    print("          El valor de x",i+1,"es =",sol[i])
print( )

#b)
"""
print("b)")
print(" ")

def v1(x1,t):
    return x1*np.exp(-w*t)
def v2(x2,t):
    return x2*np.exp(-w*t)
def v0(t):
    return x0*np.exp(-w*t)
def v3(t):
    return x3*np.exp(-w*t)
sol1=[]
for t in range(0): #Ya que a la hora de hacer el algebra, el factor comun de la exponencial al serlo de todos, se puede cancelar.

    M=np.array([[(v1-v3)/r1 +c1*(v1-v0) + c2*(v1-v2)],[(v2-v3)/r2 + c2*(v2-v1) + (v2-v0)/r3]])
   
    sol11=np.linalg.solve(M,0)
    print(sol11)

"""

#2)
print("2)")
print("")



def m(f1,f2,f3,f4):
    def f1(w,x,y,z):
        return (2*z**2 + 3*z*x -5*y - 4*y*w)
    def f2(w,x,y,z):
        return (3*x*z - 3.4*y*z - np.sin(x) + w**2)
    def f3(w,x,y,z):
        return (x*y - 5*np.cos(2*y) + 2*z**2 - z)
    def f4(w,x,y,z):
        return (3*w - np.exp(-x) - 2*x*z + y*w)
    return  np.array([[f1,f2],[f3,f4]])
k=1
xyz0=np.array([k,k,k,k])
#print(xyz0)
sol11=fsolve(m(),xyz0)