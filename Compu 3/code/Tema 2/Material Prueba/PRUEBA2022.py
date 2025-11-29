import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import dct, idct
from scipy.fft import fft, fftfreq

#########################################################                         1                      #################################################################

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
axs[1].plot(ak, '-b')
axs[2].plot(xi, yiFS, '-g')

plt.show()


#########################################################                    2                #############################################################################

# Cargar los datos del archivo
data = np.loadtxt('Datos_teo.txt')

# Definir parámetros de tiempo
tiempo_inicial = 0.0
tiempo_final = 1.999
resolucion_temporal = 0.002

tiempo = np.arange(tiempo_inicial, tiempo_final, resolucion_temporal)


# Calcular la transformada de Fourier de los datos
transformada = fft(data)
frecuencias = fftfreq(len(data), d=resolucion_temporal)

# Obtener las frecuencias dominantes
amplitudes = np.abs(transformada)
frecuencias_dominantes = frecuencias[amplitudes > np.max(amplitudes)]  # Ajusta el umbral según necesites

# Imprimir las frecuencias dominantes
print("Frecuencias dominantes:")
for freq in frecuencias_dominantes:
    print(freq,"HZ")

# Crear el gráfico
fig, axs = plt.subplots(2, 1, figsize=(8, 10))

# Primer panel: señal original en función del tiempo
axs[0].plot(tiempo, data)
axs[0].set_xlabel('Tiempo (s)')
axs[0].set_ylabel('Amplitud')
axs[0].set_title('Señal original')

# Segundo panel: espectro de coeficientes de Fourier en función de la frecuencia
axs[1].plot(frecuencias, np.abs(transformada))
axs[1].set_xlabel('Frecuencia (Hz)')
axs[1].set_ylabel('Amplitud')
axs[1].set_title('Espectro de Fourier')

# Tercer panel: ondas dominantes en función del tiempo (intervalo 0.01 s)
intervalo_tiempo = 0.01
indices_intervalo = np.logical_and(tiempo >= 0, tiempo < intervalo_tiempo)

axs[2].plot(tiempo[indices_intervalo], data[indices_intervalo])
axs[2].set_xlabel('Tiempo (s)')
axs[2].set_ylabel('Amplitud')
axs[2].set_title('Ondas dominantes')

# Ajustar el espacio entre los subplots
plt.tight_layout()

# Mostrar el gráfico
plt.show()