from scipy.fftpack import dct, idct
import matplotlib.pyplot as plt
import numpy as np

N=500
def f(t):
    
    yi= np.exp(-t/10)*np.sin(2*t)
    return yi
t=np.linspace(0,25,N)
yi=f(t)

ak_sc = dct(yi, norm='ortho')###Coeficientes con dft de scipy

#CALUCLO DE ERROR CON 0.5% DE ERROR

denom = sum(abs(yi)**2)

err = 0.05
err_out = 1
elementos = 10

while(err_out >= err):
	ventana = np.zeros(N)
	ventana[:elementos] = 1

	yiDCT = idct(ak_sc * ventana, norm='ortho')

	err_out = sum(abs(yi - yiDCT)**2) / denom * 100

	elementos += 1

print('Error con', elementos, 'coeficientes: ', round(err_out, 4), ' %')

plt.clf()
plt.plot(t, yi, '-r')
plt.show()