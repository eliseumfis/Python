import numpy as np
import pylab as plt

def fun(x):
    tmp_y = np.zeros_like(x)
    tmp_y = np.cos(2 * x) * np.exp(x)
    return tmp_y

dx = 0.001
L = 4 * np.pi
x = L * np.arange(-1+dx, 1+dx, dx)
f=fun(x)
fFS = 0
k = 60
ak = np.zeros(k)
bk = np.zeros(k)    
for i in range(k):
    argcos = (2 * np.pi * (i) * x) / L
    ai = np.sum(f * np.cos(argcos) * dx)
    ak[i] = ai

    argsin = (2 * np.pi * (i+1) * x) / L
    bi = np.sum(f * np.sin(argsin) * dx)
    bk[i] = bi
    #print(B)

    fFS += ai * np.cos(argcos) + bi * np.sin(argsin)

plt.plot(x, f, '-b')
plt.plot(x, fFS, '-r')
plt.ylabel('f(x)')
plt.xlabel('x')
plt.show()