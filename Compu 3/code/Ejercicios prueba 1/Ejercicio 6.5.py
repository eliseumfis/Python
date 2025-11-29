from numpy.linalg import solve
from numpy import array
import numpy as np
import cmath as cmt
#Define ctes

R1=R3=R5=1000;R2=R4=R6=2000;C1=1.0*10**(-6);C2=0.5*10**(-6)
xmas=3.0;omega=1000.0

#(1/R1 + 1/R4 + iwC1)x1 - iwC1x2 = x+/R1
#-iwC1x1 + (1/R2 +1/R5 + iwC1 + iwC2)x2 - iwCx3 = x+/R2
#-iwC2x2 + (1/R3 +1/R6 + iwC2)x3 - iwCx3 = x+/R3

A1=array([[1.0/R1 + 1/R4,0,0],[0,1.0/R2 + 1.0/R5,0],[0,0,1.0/R3 +1.0/R6]],float)
A2=array([[omega*C1,-C1*omega,0],[-omega*C1, omega*C1+omega*C2,-omega*C2],[0,-omega*C2,omega*C2]],float)

A=A1+1j*A2
v1=array([xmas/R1,xmas/R2,xmas/R3],float)
#v2=array([xmas/R2,xmas/R2,xmas/R2],float)
#v=v1+1j*v2

xx=solve(A,v1)
print(xx)

for ii in range(3):
    r,phase=cmt.polar(xx[ii])
    print("La amplitud de V",str(ii+1),"=",r,"volts")
    print("La fase de V",str(ii+1),"=",np.degrees(phase))
    print()