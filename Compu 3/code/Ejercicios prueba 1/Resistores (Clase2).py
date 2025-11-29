#Ecuaciones sacadas usando leyes de kirchoff y ohm en un punto (V*-V')/R*
import numpy as np
A=np.array([[4,-1,-1,-1],[-1,3,0,-1],[-1,0,3,-1],[-1,-1,-1,4]],float)
B=np.array([5,0,5,0])
x=np.linalg.solve(A,B)
#print("El resultado para V1 es:",x[0],", el resultado de V2 es:",x[1],", el resultado de V3 es:",x[2],", el resultado de V4 es:",x[3])

#PROBLEMA DE PIZZAS Y LASAÑAS
C=np.array([[20,10],[17,22]],float)
V=np.array([350000,500000])
y=np.linalg.solve(C,V)
print("El precio de las pizzas son:",y[0],"y el precio de la lasaña es:",y[1])
#### Probar que solucion es verdadera ######
F = np.dot(C,y)
print(V)
print(F)