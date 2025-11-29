import numpy as np
import matplotlib.pyplot as plt

######## Calcular serie de Fourier para función triangular ###########
# Definir dominio
dx = 0.001
L = np.pi
x = L*np.arange(-1+dx, 1+dx, dx)
n = x.shape[0]
nquart = int(n/4)

# Definir function
f = np.zeros_like(x) # Entrega arreglo de ceros con mismo tamaño y tipo que x
f[nquart:2*nquart] = (4/n)*np.arange(1,nquart+1)
f[2*nquart:3*nquart] = np.ones(nquart) - (4/n)*np.arange(0,nquart)

plt.clf()
#plt.subplot(2,1,1)
plt.plot(x, f, '-k')
plt.ylabel('f(x)'); plt.xlabel('X')
plt.grid()