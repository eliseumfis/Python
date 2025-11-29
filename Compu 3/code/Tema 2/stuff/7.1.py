from funciones import dft
import numpy as np
import pylab as plt


#1)

x= np.arange(0,1000.0)
f = np.zeros_like(x) # Entrega arreglo de ceros con mismo tamaño y tipo que x
f[:x.shape[0]//2+1] = -2
f[501:] = 2
print(x.shape[0])

c = dft(f)

plt.clf()
plt.subplot(2,1,1)
plt.plot(x, f, '-b')
plt.xlabel('x'); plt.ylabel('f(x)')

plt.subplot(2,1,2)
plt.plot(range(len(f)//2+1), abs(c), '-r')
plt.xlabel('k'); plt.ylabel('$c_k$')
plt.xlim(0, 50)

