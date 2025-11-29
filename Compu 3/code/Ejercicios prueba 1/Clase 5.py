from numpy.linalg import eigh, eigvals ###ver ppt
###Ejercico comparar el calculo anterior con estas dos matrices: La primera me dan los mismos 
# valores que la matriz anterior y la segund a es distinta a las dos... ver ppt
### Ejercicio dado los vactores::: Calcular el producto escalar.
a=(1,2,3,4)
b=(2,4,6,8)

###1
import numpy as np

a = np.array([1, 2, 3, 4]) #: np.arange(1,5) : len(a)--> largo o  a.shape[0]
b = np.array([2, 4, 6, 8]) #: np.arange(1,9,2)

product_escalar = np.dot(a, b)

print("opcion 1:", product_escalar) 


###2 
c=0
for ii in range(len(a)):
    c+= a[ii]*b[ii]

print ("Opcion 2:", c)

###3
print("opcion 3:", a@b)


###5
print("opcion 5:", sum(a*b))

### Dada la siguiente matriz cutas columnas son vectores, encuentre e imprima los vectores ortogonales entre si.

import numpy as np
A=np.array([[3,5,2,4,-4,-3], [4,1,0,-3,2,0],[2,3,1,0,1,5]])
#A=([3,4,2],[5,1,3], [2,0,1], [4, -3, 0 ], [-4,2,1], [-3,0,5]) ###Usando ciclo for

for ii in range (A.shape[1]):
    a1=A[:,ii]
    
    for jj in range (ii+1, A.shape[1]):
        if np.dot(a1, A[:,jj]) ==0: #o if abs(np.dot(a1, A[:,jj])) < 10**-15:
            print("Los vectores", a1 ,"y", A[:,jj], "Son ortogonales")

