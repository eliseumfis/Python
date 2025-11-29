import numpy as np
from numpy.linalg import inv
R1=R3=R5=1000;R2=R4=R6=2000
A1=np.array([[1.0/R1 + 1/R4,0,0],[0,1.0/R2 + 1.0/R5,0],[0,0,1.0/R3 +1.0/R6]],float)

#opcion 1
x1=inv(A1)
#print(x1)

#opcion 2
x2=np.linalg.solve(A1, np.identity(3))
#print(x2)

#   Ejercicio 1 

A=np.array([[1,2,3],[22,32,42],[55,66,100]])
B=np.array([1,2,3])

#opcion 1

X1=np.linalg.solve(A,B)
#print("X=",X1)
#print("Residual=",np.dot(A,X1)-B) (PARA COMPROBAR SI ES CORRECTO)

#opcion 2
X2=np.dot(inv(A),B)
#print("X=",X2)


#EJERCICIO 2

M=np.array([[4,-2,1],[3,6,-4],[2,1,8]],float)
m=inv(M);print(m)
print("Id1=",np.dot(m,M))
print("Id2=",np.dot(M,m))