import numpy as np
#1)
A=np.array([[20,10],[17,22]])
B=np.array([350000,500000])
C=np.linalg.solve(A,B)
print("El precio de la pizza es de",C[0],"pesos")
print("El preciod de la lasaña es",C[1],"pesos")
F=np.dot(A,C);print(F)