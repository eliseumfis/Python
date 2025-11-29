
#Ejemplo 6.1 Nerwman
from numpy import array,empty
A=array([[2,1,4,1],[3,4,-1,-1],[1,-4,1,5],[2,-2,1,3]],float)
print(A)
v=array([-4,3,9,7],float)
print(v)
N=len(v)
#Eliminacion gaussiana
for m in range(N):
    #Divide by the diahonal element
    div=A[m,m]
    A[m,:]/=div
    v[m]/=div
    #NOW SUBSTRACT from the  lower rows
    for ii in range(m+1,N):
        mult=A[ii,m]
        A[ii,:]-=mult*A[m,:]
        v[ii]-=mult*v[m]
#Backsubstitution
x=empty(N,float)
for m in range(N-1,-1,-1):
    x[m]=v[m]

    for ii in range(m+1,N):
        x[m]-=A[m,ii]*x[ii]
print("Las soluciones del sistema de ecuaciones son",x)