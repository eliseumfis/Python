import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import dct, idct
from scipy.fft import fft, fftfreq

#########################################################                         1                      #################################################################
"""
data=np.loadtxt("dow2.txt",float)
n_x = data.shape[0]
xi = np.arange(n_x)
yi = np.loadtxt("dow2.txt",float,usecols=0)


ak = dct(yi, norm='ortho')###Coeficientes con dft de scipy

#CALUCLO DE ERROR CON 0.01% DE ERROR

denom = sum(abs(yi)**2)

err = 0.01
err_out = 1
elementos = 10

while(err_out >= err):
	ventana = np.zeros(n_x)
	ventana[:elementos] = 1

	yiDCT = idct(ak * ventana, norm='ortho')

	err_out = sum(abs(yi - yiDCT)**2) / denom * 100

	elementos += 1

print('Error con', elementos, 'coeficientes: ', round(err_out, 4), ' %')

yiFS = np.fft.ifft(ak)

fig, axs = plt.subplots(3)
axs[0].plot(xi, yi, '-r')
axs[0].grid()
axs[1].plot(ak, '-b')
axs[2].plot(xi, yiFS, '-g')


plt.show()
"""

# Cargar los datos del archivo
data = np.loadtxt('Datos_teo.txt')

# Definir parámetros de tiempo
tiempo_inicial = 0.0
tiempo_final = 1.999
resolucion_temporal = 0.002

tiempo = np.arange(tiempo_inicial, tiempo_final, resolucion_temporal)

#pregunta a)
#Calcular dft para los datos 

ck=fft(data)

#frecuencias del espacio

freq=fftfreq(data.size, d=resolucion_temporal)


#Frecuencias dominantes
max_term=[]; ult_term=0 ; ck_abs=abs(ck)
while len(ck_abs)>1:
    term=np.argmax(ck_abs,axis=0)
    #print(term)
    max_term.append(term)
    ck_abs=ck_abs[term+1:]
    ult_term=term
print("Las frecuencias dominantes son:", np.sort(max_term))
