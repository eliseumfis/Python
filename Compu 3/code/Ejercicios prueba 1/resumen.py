
#      (1) eliminacion gaussiana

from numpy import array, empty,linalg,dot,identity
from scipy.linalg import inv
a = array([[2, 1, 4, 1], [3, 4, -1, -1], [1, -4, 1, 5], [2, -2, 1, 3]], float)
print(a)
v = array([-4, 3, 9, 7], float)
print(v)
n = len(v)

for m in range(n):
    # divide por el elemento diagonal
    div = a[m, m]
    a[m, :] /= div
    v[m] /= div

    # para resta de filas abajo
    for i in range(m + 1, n):
        mult = a[i, m]
        a[i, :] -= mult * a[m, :]
        v[i] -= mult * v[m]

# sustitucion
x = empty(n, float)
for m in range(n - 1, -1, -1):
    x[m] = v[m]

    for i in range(m + 1, n):
        x[m] -= a[m, i] * x[i]

print("las soluciones del sistema de ecuaciones son ", x)


#     (2) funcion linalg.solve de numpy y/o scipy
# primer argumento corresponde a la matriz y el segundo a los coef independientes
#entrega la matriz resultado
c=linalg.solve(a,v)
print("las soluciones son ",c)
#para comprobar ocupamos funcion dot de numpy, el primer argumento corresponde a la matriz principal, el segundo al resultado de las variables,nos debe dar los coeficientes independientes
#dot realiza producto punto entre matrices o vectores
f=dot(a,c)
print(f); print(v)
## revisar

#%%
#    (3) resolucion a traves de matriz inversa x=a^-1
# funcion inv de paquete linalg numpy
x=linalg.inv(a)
print(x)
# entrega la inversa de a
xx=linalg.solve(a,identity(4))  
print(xx)

# ejemplo midiendo errores del calculo
aa=array([[1,2,3],[22,32,42],[55,66,100]],float)
bb=array([1,2,3],float)
sl=linalg.solve(aa,bb)
print("x= ",sl)
print("residuo ",dot(aa,sl)-bb)
# el error se acerca a cero si la solucion es exacta

# para una calculo de matriz 

a=array([[4,-2,1],[3,6,-4],[2,1,8]],float)
ai=linalg.inv(a)
id1=dot(ai,a)
id2=dot(a,ai)
print(id1);print();print(id2)
#%%

#    (4) comparacion de modelos
 
import numpy as np
A = np.array([[4, -1, -1, -1], [-1, 3, 0, -1], [-1, 0, 3, -1], [-1, -1, -1, 4]])
B = np.array([5, 0, 5, 0])
C = np.linalg.solve(A, B) # Metodo 1
D = np.linalg.inv(A).dot(B) # Metodo 2
print(C); print(D)

#%%
### Transformaci ́on pero vector NO es vector propio 
import numpy as np
import matplotlib.pyplot as plt
def plot_vect(x, b, xlim, ylim): 
    plt.clf()
    plt.quiver(0,0,x[0],x[1], color="k", angles="xy",scale_units="xy",scale=1, label="Vector Original") 
    plt.quiver(0,0,b[0],b[1], color="g",angles="xy",scale_units="xy",scale=1, label ="Vector Transformado") 
    plt.title("Vector no es vector propio")
    plt.xlim(xlim); plt.ylim(ylim)
    plt.xlabel("X"); plt.ylabel("Y"); plt.legend()
A = np.array([[2, 0],[0, 1]]); x = np.array([[1],[1]]) 
b = np.dot(A, x)
plot_vect(x, b,(0,3),(0,2))


#vectores y valores propios
import numpy as np
A = np.array([[1,2],[2,1]], float)
x, V = np.linalg.eigh(A)
print("Los autovalores son", x)
print("Los autovectores son", V) ############


print()
a=np.array([[3,5,2,4,-4,-3],[4,1,0,-3,2,0],[2,3,1,0,1,5]],float)
#calcular producto punto entre los vectores columnas

for ii in range(a.shape[1]):
    a1 = a[:,ii]
    for jj in range(ii+1, a.shape[1]):
        if np.dot(a1, a[:,jj]) == 0:
            print("Los vectores ",a1, "y ", a[:,jj], "son ortogonales")
#%%

# resolucion numerica de ecuaciones no lineales 

# metodo de relajacion (por repeticion)
# ecuacion debe estar en la forma x=f(x), si no es posible debe redondearse

# ejemplo
import numpy as np
ii=1
x1 = 2.0; x0 = 0.1 
Er = abs(x1 - x0) 
while (Er > 10**-5):
    x0 = x1
    x1 = 2 - np.exp(-x0)
    Er = abs(x1 - x0)
    ii += 1
    print("Solucion x1 = ", x1) 
    print("Diferencia entre iteraciones = ", Er) 
    print("Iteracion No. ", ii)
    print()
#a traves de funcion fsolve de scipy
#la funcion debe estar en forma f(x)=0
#se define funcion,se da valor inicial para x
#la funcion recibe como primer argumento la funcion y luego el valor inicial

#ejemplo
from scipy.optimize import fsolve 
from numpy import exp
def f(x):
    return 2- exp(-x)-x
x1=fsolve(f,1)
print(x1)

#para escoger el valor inicial utilizamos metodo grafico

import matplotlib.pyplot as plt 
import numpy as np
def f(x):
    return 2 - np.exp(-x) - x 
def g(x):
    return np.log(x) + x**2 - 1
x = np.arange(-4,4,0.1)
plt.clf()
plt.plot(x, f(x), "-b", x, g(x), "-r") 
plt.ylabel("f(x) & g(x)"); plt.xlabel("X") 
plt.axhline(0, -4, 4, color="k") 
plt.legend(("f(x)", "g(x)"), loc=2) 
plt.grid()
 
plt.clf()
def h(x):
    return 2-np.exp(-x)-x
x1=np.arange(-5,5,0.1)
plt.plot(x1,h(x1))
plt.grid()
x2=fsolve(h,np.array([-5,5]))
print()
print(x2[0]);print(x2[1])

#%%

# sistema de ecuaciones no lineales
#el vector xyz0 es arbitrario
import numpy as np
from scipy.optimize import fsolve
def f(x):
    f0=x[0]**2+x[1]**2 -1
    f1= x[0]*x[1]+x[1]*x[2] +1.1 
    f2= x[1]**2 + x[2]**2 -2
    return np.array([f0,f1,f2]) 
xyz0=np.array([1,2,3]) 
xyz=fsolve(f,xyz0)
print(xyz)
#%%

#maximos y minimos de funciones 

import numpy as np
from scipy.optimize import fsolve, fminbound,fmin
x = np.arange(-10, 10, 0.1) 
def f(x):
    return x**2 + 10*np.sin(x)
plt.clf(); plt.plot(x, f(x), "-b")
plt.ylabel("F(x)"); plt.xlabel("X"); plt.hlines(0, -10, 10, colors="k") 
plt.grid()
# Valor inicial
x0 = -10
# M ́ınimo local con fmin
fmini = fmin(f, x0); print("Min. function = ", fmini); print()
# M ́ınimo local con fminbound
rmini = fminbound(f, -10, 0); print("Min. function = ", fmini)
