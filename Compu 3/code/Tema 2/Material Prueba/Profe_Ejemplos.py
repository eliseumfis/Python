

#### Ejemplos de Capítulo 7: Fourier series ######

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


#%%
# Compute Fourier series
A0 = np.sum(f*np.ones_like(x))*dx  # Igual que zeros_like
fFS = A0/2

# Repito el plot de la función
plt.clf()
#plt.subplot(2,1,1)
plt.plot(x, f, '-k')
plt.ylabel('f(x)'); plt.xlabel('X')
plt.grid()

kk = 20

A = np.zeros(kk)
B = np.zeros(kk)
ERR = np.zeros(kk)

for ii in range(kk):
    A[ii] = np.sum(f*np.cos(np.pi*(ii+1)*x/L))*dx  # Inner product
    B[ii] = np.sum(f*np.sin(np.pi*(ii+1)*x/L))*dx
    fFS = fFS + A[ii]*np.cos((ii+1)*np.pi*x/L) + B[ii]*np.sin((ii+1)*np.pi*x/L)
    
    # Plot de cada término de la serie
    plt.plot(x, fFS, '-')

plt.ylabel('f(x) & Fseries'); plt.xlabel('X')

#plt.clf()
#plt.plot(x, f, '-k')
#plt.ylabel('f(x)'); plt.xlabel('X')
#plt.grid()
#
#plt.plot(x, fFS, '-')
#plt.ylabel('f(x) & Fseries'); plt.xlabel('X')



#%%
###### Calcular el error asociado al cálculo de la transformada de Fourier ######
fFS = (A0/2)*np.ones_like(f)
kmax = 20
A = np.zeros(kmax)
B = np.zeros(kmax)
ERR = np.zeros(kmax)

A[0] = A0/2
ERR[0] = np.linalg.norm(f-fFS)/np.linalg.norm(f)

for ii in range(1, kmax):
    A[ii] = np.sum(f*np.cos(np.pi*(ii)*x/L))*dx # Inner product
    B[ii] = np.sum(f*np.sin(np.pi*(ii)*x/L))*dx
    fFS = fFS + A[ii]*np.cos((ii)*np.pi*x/L) + B[ii]*np.sin((ii)*np.pi*x/L)
    ERR[ii] = np.linalg.norm(f-fFS)/np.linalg.norm(f)

    
plt.clf()
plt.plot(np.arange(kmax), ERR, '-k', LineWidth=2)
plt.ylabel('Error'); plt.xlabel('k')














#%%
##### Repetir ejercicio para otra función ######
###### Función cuadrada escalonada  #######
# Define domain
dx = 0.001
L = np.pi
x = L*np.arange(-1+dx, 1+dx, dx)
n = x.shape[0]
nquart = int(n/2)

# Define hat function
f = np.zeros_like(x) # Entrega arreglo de ceros con mismo tamaño y tipo que x
f[:nquart] = -1
f[nquart:] = 1

plt.clf()
#plt.subplot(2,1,1)
plt.plot(x, f, '-k')
plt.ylabel('f(x)'); plt.xlabel('X')
plt.grid()





#%%
# Compute Fourier series
A0 = np.sum(f*np.ones_like(x))*dx  # Igual que zeros_like
fFS = A0/2

# Repito el plot de la función
plt.clf()
#plt.subplot(2,1,1)
plt.plot(x, f, '-k')
plt.ylabel('f(x)'); plt.xlabel('X')
plt.grid()

kk = 50

A = np.zeros(kk)
B = np.zeros(kk)
ERR = np.zeros(kk)

for ii in range(kk):
    A[ii] = np.sum(f*np.cos(np.pi*(ii+1)*x/L))*dx # Inner product
    B[ii] = np.sum(f*np.sin(np.pi*(ii+1)*x/L))*dx
    fFS = fFS + A[ii]*np.cos((ii+1)*np.pi*x/L) + B[ii]*np.sin((ii+1)*np.pi*x/L)
    
    # Plot de cada término de la serie
    plt.plot(x, fFS, '-')

plt.ylabel('f(x) & Fseries'); plt.xlabel('X')






#%%
#################################################
######## Ejemplo para calcular la transformada de Fourier discreta a la 
####### función f(x) = sin(x)
import numpy as np
#from cmath import exp

def dft(y):
    N = len(y)
    # c = np.zeros(N//2+1, complex)
    c = []
    for k in range(N//2+1):
        c1 = 0
        for n in range(N):
            # c[k] += y[n]*np.exp(-2j*np.pi*k*n/N)
            c1 += y[n]*np.exp(-2j*np.pi*k*n/N)
        c.append(c1)
    return c

xx = np.arange(-np.pi, np.pi+0.1, 0.1)

# Function
y = np.sin(xx)
#y = np.cos(xx)
#y = np.cos(2*xx) + np.sin(2*xx)

cc = dft(y) 
print(cc)



















#%%
# Define the inverse DFT
def idft(c):
    N = 2*(len(c) - 1)
    yn = np.zeros(N, complex)
    for n in range(N):
        for k in range(N//2+1):  #
            yn[n] += c[k]*np.exp(2j*np.pi*k*n/N)/(N//2+1)
    return yn

yn = idft(cc)

plt.clf()
plt.plot(xx, y, '-b', xx, yn, '-r')
plt.hlines(0, -np.pi, np.pi, color='k', linewidth=2)
plt.ylabel('Sin(x)'); plt.xlabel('X')
plt.legend(('sin(x)', 'IDFT'), loc=1)















#%%
import os
import numpy as np

os.chdir('/home/julioc/work/Classes/Year-2022/Sem1_LFIS214/scripts')

data = np.loadtxt('pitch.txt', float)

plt.clf()
plt.plot(data)

# DFT function
def dft(y):
    N = len(y)
    c = np.zeros(N//2+1, complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*np.exp(-2j*np.pi*k*n/N)
    return c

c = dft(data)


plt.close('all')
plt.plot(abs(c))
plt.ylabel(r'Abs ($c_k$)')
plt.xlabel('Múltiplos de frecuencia')
plt.xlim(0, 500)












#%%
# Exercise 7.1
import numpy as np

def dft(y):
    N = len(y)
    c = np.zeros(N//2+1, complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*np.exp(-2j*np.pi*k*n/N)
    return c

# a)
#dx = 0.002
#L = np.pi
#x = L*np.arange(-1+dx, 1+dx, dx)
#n = x.shape[0]
#nquart = int(n/2)
#
## Define hat function
#x= np.arange(0,100)
#dx = 0.002
#L = np.pi
#x = L*np.arange(-1+dx, 1+dx, dx)
#n = x.shape[0]
#nquart = int(n/2)
#
##dx = 0.002
#L = np.pi
#x = L*np.arange(-1+dx, 1+dx, dx)
#n = x.shape[0]
#nquart = int(n/2)
#
##f = np.zeros_like(x) # Entrega arreglo de ceros con mismo tamaño y tipo que x
#f[:nquart] = -2
#f[nquart:] = 2

x= np.arange(0,1000.0)
f = np.zeros_like(x) # Entrega arreglo de ceros con mismo tamaño y tipo que x
f[:x.shape[0]//2+1] = -2
f[501:] = 2

c = dft(f)

plt.clf()
plt.subplot(2,1,1)
plt.plot(x, f, '-b')
plt.xlabel('x'); plt.ylabel('f(x)')

plt.subplot(2,1,2)
plt.plot(range(len(f)//2+1), abs(c), '-r')
plt.xlabel('k'); plt.ylabel('$c_k$')
plt.xlim(0, 50)







#%%
###### Repetir ejercicio usando función de Python   ######
x = np.arange(-500, 501)

#### función piecewise crea función onda cuadrada
y = np.piecewise(x, [x < 0, x >= 0], [-2, 2])

c = dft(y)

plt.clf()
plt.subplot(2,1,1)
plt.plot(x, y, '-b')
plt.xlabel('x'); plt.ylabel('f(x)')
plt.tight_layout()

plt.subplot(2,1,2)
plt.plot(range(len(y)//2+1), abs(c), '-r')
plt.xlabel('k'); plt.ylabel('$c_k$')
plt.xlim(0, 50)
plt.tight_layout()












#%%
# b)
# Define domain
dx = 0.002
L = np.pi
x = L*np.arange(-1+dx, 1+dx, dx)
n = x.shape[0]
nquart = int(n/100)

# Define hat function
f = np.zeros_like(x) # Entrega arreglo de ceros con mismo tamaño y tipo que x
for ii in range(0, f.shape[0], 100):
    f[ii:ii+100] = np.array(range(100), int)

c = dft(f)

plt.clf()
plt.subplot(2,1,1)
plt.plot(x, f, '-b')
plt.xlabel('x'); plt.ylabel('f(x)')

plt.subplot(2,1,2)
plt.plot(range(len(f)//2+1), abs(c), '-r')
plt.xlabel('k'); plt.ylabel('$c_k$')
plt.xlim(0, 200)








#%%
####### Repetir ejercicio usando función de Python #######

from scipy import signal

x = np.linspace(0, 1, 1000)
y = signal.sawtooth(2* np.pi* 3* x)

c = dft(y)

plt.clf()
plt.subplot(2,1,1)
plt.plot(x, y, '-b')
plt.xlabel('x'); plt.ylabel('f(x)')

plt.subplot(2,1,2)
plt.plot(range(len(y)//2+1), abs(c), '-r')
plt.xlabel('k'); plt.ylabel('$c_k$')
plt.xlim(0, 200)













#%%
# c)
x = np.linspace(0,1,1000) #(1000)
N = len(x)

# Define hat function
f = np.zeros_like(x) # Entrega arreglo de ceros con mismo tamaño y tipo que x

for ii in range(N):
#    print(ii)
    f[ii] = np.sin(ii*np.pi/N)*np.sin(20*np.pi*ii/N)

def ff(x):
    return np.sin(x*np.pi/N)*np.sin(20*np.pi*x/N)
x = np.arange(2000)
yn = ff(x)

c = dft(yn)

plt.clf()
plt.subplot(2,1,1)
plt.plot(x, yn, '-b')
plt.xlabel('x'); plt.ylabel('f(x)')

plt.subplot(2,1,2)
plt.plot(range(1001), abs(c), '-r')
plt.xlabel('k'); plt.ylabel('$c_k$')
plt.xlim(0, 50)


















#%%
# Exercise 7.2
import os
import numpy as np
import matplotlib.pyplot as plt

os.chdir('/home/julioc/work/Classes/Year-2022/Sem1_LFIS214/scripts')

mon = np.loadtxt('sunspots.txt', int, usecols=0)
sp1 = np.loadtxt('sunspots.txt', float, usecols=1)

# a)
plt.clf()
plt.subplot(2,1,1)
plt.plot(mon, sp1, '-b')
plt.xlabel('Month'); plt.ylabel('Sun spots')
plt.xlim(0, 400)
plt.tight_layout()








#%%
# b)
# Calculate DFT
ck = dft(sp1)

plt.subplot(2,1,2)
plt.plot(range(ck[:].shape[0]), abs(ck[:])**2/10**9, '-r') #**2/10**9
plt.xlabel('k'); plt.ylabel('$c_k^{2} x 10^{-9}$')
plt.xlim(1, 400)
plt.ylim(0, 5)
plt.tight_layout()



#%%

pow_s = abs(ck[1:])**2
freq = pow_s.argmax()
nmons = 1/freq*len(mon[1:])
years = nmons/12
print("El número de manchas solares tiene un período de ", years, "años")


# pow_s = abs(ck)**2
# freq = pow_s.argmax()
# nmons = 1/freq*len(mon)
# years = nmons/12
# print("El número de manchas solares tiene un período de ", years, "años")






#%%
######## Repetir ejercicio 7.2 usando fft y fftfreq ##########
import numpy as np
import matplotlib.pyplot as plt
#from scipy.fft import fft, fftfreq
from scipy.fftpack import fft, fftfreq
import os

os.chdir('/home/julioc/work/Classes/Year-2022/Sem1_LFIS214/scripts')

mon = np.loadtxt('sunspots.txt', int, usecols=0)
sp1 = np.loadtxt('sunspots.txt', float, usecols=1)

# data= np.loadtxt('sunspots.txt', float)
# col1=data[:,0]
# col2=data[:,1]

# Number of sample points
N = len(mon)

# Sample spacing
T = 1.0/12

x = np.linspace(0.0, N*T, N)

yf = fft(sp1)
xf = fftfreq(N, T)[:N//2]

# Plot
# plt.figure(2)
plt.clf()
plt.subplot(2,1,1)
plt.plot(x, sp1, '-b'); plt.ylabel('Sunspots'); plt.xlabel('Years')
plt.xlim(0,50)
plt.tight_layout()

#pow_s = 2.0/N*np.abs(yf[1:N//2])
pow_s = np.abs(yf[1:N//2])

plt.subplot(2,1,2)
plt.plot(xf[1:], pow_s, '-r') #2.0/N* /yf.max()
plt.ylabel('$c_k$'); plt.xlabel('f')
#plt.xlim(0,200)
plt.grid()
plt.tight_layout()

posi = pow_s.argmax()
freq_max = xf[posi]
print("El número de manchas solares tiene un período de ", 1/freq_max, "años")

# freq = pow_s.argmax()
# nmons = 1/freq*len(mon[1:])
# years = nmons/12
# print("El número de manchas solares tiene un período de ", years, "años")








#%%
###############################
####### Clase FFT ##########
##################################
from scipy.fftpack import fft, rfft, ifft, irfft
# from scipy.fft import fft, rfft, ifft
import numpy as np
#from numpy.fft import fft, ifft, rfft

x = np.array([1.0, 2.0, 1.0, -1.0, 1.5, 1.0])

y1 = fft(x)
print("Coeficiente de FFT = ", y1)

y2 = rfft(x)
print("Coeficientes de RFFT = ", y2)

print()

x1 = ifft(y1)
x2 = irfft(y2)
print("Los valores de X = ", x)
print("Los valores de X1 = ", x1)
print("Los valores de X2 = ", x2)











#%%

x = np.array([1.0 , 2.0, 1.0 , -1.0, 1.5, 1.0])
y1 = fft(x)
print("Coeficientes de fft = ", y1)
#print(x.sum())
print()

y2 = rfft(x)
print("Coeficientes de rfft = ", y2)
print()

yinv = ifft(y1)
print("Los valores de x = ", x)
print("Valores de x obtenidos a partir de ifft = ", yinv)













#%%
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq
# from scipy.fft import fft, fftfreq
# Number of sample points
N = 600

# Sample spacing
T = 1.0/1000.0

x = np.linspace(0.0, N*T, N)
y = np.sin(50.0*2.0*np.pi*x) + 0.5*np.sin(80.0*2.0*np.pi*x) + \
 + 0.5*np.sin(100.0*2.0*np.pi*x)

yf = fft(y)
xf = fftfreq(N, T)[:N//2]

# Plot
plt.clf()
plt.subplot(2,1,1)
plt.plot(x, y, '-b'); plt.ylabel('y'); plt.xlabel('x')
plt.tight_layout()

plt.subplot(2,1,2)
plt.plot(xf, 2.0/N*np.abs(yf[0:N//2]), '-r') #2.0/N* /yf.max()
plt.ylabel('$c_k$'); plt.xlabel('f')
plt.xlim(0,200)
plt.grid()
plt.tight_layout()






#%%
from scipy.fftpack import dct, idct
import matplotlib.pyplot as plt
import numpy as np

N = 100
t = np.linspace(0,20,N) #, endpoint=False
x = np.exp(-t/3)*np.cos(2*t)
y = dct(x, norm='ortho')

# Caso reconstruir con primeros 10 elementos
window = np.zeros(N)
window[:10] = 1
yr10 = idct(y*window, norm='ortho')

# Caso recontrucción con 15 primeros elementos
window = np.zeros(N)
window[:15] = 1
yr15 = idct(y*window, norm='ortho')

# Caso reconstruir con primeros 20 elementos
window = np.zeros(N)
window[:20] = 1
yr20 = idct(y*window, norm='ortho')

# Caso reconstruir con primeros 25 elementos
window = np.zeros(N)
window[:25] = 1
yr25 = idct(y*window, norm='ortho')

# Calcular Error relativo
print("Error Relativo con 10 elem = ",sum(abs(x-yr10)**2)/sum(abs(x)**2)*100," %")
print("Error Relativo con 15 elem = ",sum(abs(x-yr15)**2)/sum(abs(x)**2)*100," %")

print("Error Relativo con 20 elem = ",sum(abs(x-yr20)**2)/sum(abs(x)**2)*100," %")
print("Error Relativo con 25 elem = ",sum(abs(x-yr25)**2)/sum(abs(x)**2)*100," %")

plt.clf()
plt.plot(t, x, '-k')
plt.plot(t, yr10, '-b')
plt.plot(t, yr15, '-r')
plt.plot(t, yr20, '-g')
plt.plot(t, yr25, '-m')

plt.legend(['x', '$x_{10}$', '$x_{15}$', '$x_{20}$', '$x_{25}$'])
plt.ylabel('x'); plt.xlabel('t')
plt.grid()



