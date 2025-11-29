#Ecuaciones no lineales
import numpy as np

#def f(x):
    #x=2-np.exp(-x)

x=1
for ii in range(10):
    x=2-np.exp(-x)
    print(x)
""
import numpy as np
ii=1
x1=2.0;x0=0.1
#Er=abs(x1-x0)
Er=1
while(Er>10**-5):
    x0=x1
    x1=2-np.exp(-x0)
    Er=abs(x1-x0)
    ii+=1
    print("Solucion x1=",x1)
    print("Diferencias entre iteraciones=",Er)
    print("Iteracion No.", ii)
    print()

import numpy as np
ii=1
x1=1.0;x0=0.1
#Er=abs(x1-x0)
Er=1
while(Er>10**-6):
    x0=x1
    x1=1-np.exp(-2*x0)
    Er=abs(x1-x0)
    ii+=1
    print("Solucion x1=",x1)
    print("Diferencias entre iteraciones=",Er)
    print("Iteracion No.", ii)
    print()


import numpy as np
from scipy.optimize import fsolve

def f(x):
    return x-2+np.exp(-x)
sol=fsolve(f,1)
print(sol)

def g(x):
    return x-np.exp(1-x**2)
sol1=fsolve(g,1)
print(sol1)

"""
########COMO ESCOGER EL VALOR INICIAL?
#ENCONTRAR TRODAS LAS SOL

import numpy as np
from scipy.optimize import fsolve
def f(x):
    return x-2+np.exp(-x)
sol=fsolve(f,np.array([-3,3]))
print(sol)