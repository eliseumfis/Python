# Ejemplo 6.1 del Libro

import numpy as np

def gauss_elim(A, v):
    
    N = len(v)

    # Eliminación Gaussiana
    for m in range(N):
    # Dividir por el elemento de la diagonal
        div = A[m,m]
        A[m,:] = A[m,:]/div
        v[m] = v[m]/div
    	
        # Restar de las filas de abajo
        for ii in range(m+1,N):
            mult = A[ii,m]
            A[ii,:] -= mult*A[m,:] 
            v[ii] -= mult*v[m]
    	
    # Sustitución hacia atrás
    x = np.zeros(N,float)
    for m in range(N-1,-1,-1):
        x[m] = v[m]
    	
        for ii in range(m+1,N):
            x[m] -= A[m,ii]*x[ii]
    
    print("Las soluciones del sist. de ecs son")
    print(x)

# Crear matriz
A = np.array([[2,1,4,1],[3,4,-1,-1],[1,-4,1,5],[2,-2,1,3]],float)
print ("A = ", A)

# Crear vector de valores independientes
v = np.array([-4,3,9,7],float)
print ("v = ", v)

# Ejecutar la función
gauss_elim(A, v)