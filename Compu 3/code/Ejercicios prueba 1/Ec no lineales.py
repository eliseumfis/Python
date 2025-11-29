from scipy.optimize import fsolve
import numpy as np
"""
def f(x):
    return 2 - np.exp(-x) -x
x0=0.5
sol=fsolve(f,x0)
#print("Solucion de ecuacion",sol[0])
#print("Valor de f(x)=",f(sol))

def g(x):
    return np.exp(1- x**2) -x
solu=fsolve(g,0.5)
#print("Solucion de ecuacion",solu[0])
#print("Valor de f(x)=",g(solu))

#ECNOTRAR TODOS LOS VALORES
solvv=fsolve(f,np.array([-5,5]))
print("Soluciones de ecuaciones=",solvv)


def f(x):
    f_0=1-x[0]**2 - x[1]**2
    f_1=-1.1 - x[0]*x[1] - x[1]*x[2]
    f_2=2-x[2]**2 - x[1]**2
    return np.array([f_0,f_1,f_2])
x0=np.array([1,2,3])
sol=fsolve(f,x0)
print(sol)
"""
import numpy as np
def f(x):
    f0 = x[0]**2 + x[1]**2 - 1
    f1 = x[0]*x[1] + x[1]*x[2] + 1.1
    f2 = x[1]**2 + x[2]**2 - 2
    return np.array([f0, f1, f2])
xyz0 = np.array([1, 2, 3])
xyz = fsolve(f, xyz0)
print(xyz)