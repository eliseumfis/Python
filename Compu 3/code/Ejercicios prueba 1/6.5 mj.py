import numpy as np
#Constants
R1=R3=R5=1000;R2=R4=R6=2000
xmas=3;w=1000
c1=1e-6;c2=0.5e-6

#a)

A1=np.array([[1.0/R1 + 1/R4,0,0],[0,1.0/R2 + 1.0/R5,0],[0,0,1.0/R3 +1.0/R6]],float)
A2=np.array([[w*c1,-c1*w,0],[-w*c1, w*c1+w*c2,-w*c2],[0,-w*c2,w*c2]],float)
A=A1+1j*A2
B=np.array([xmas/R1,xmas/R2,xmas/R3],float)
sol=np.linalg.solve(A,B)
for i in np.arange(0,2,1):
    print("El valor de x",i+1,"es =",sol[i])

#b)

def v1(x1):
    return x1
def v2(x2):
    return x2
v0=x0*