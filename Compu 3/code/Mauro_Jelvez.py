import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import dct, idct
from scipy.fft import fft, fftfreq


########################### 1 ####################
data=np.loadtxt("animal_populations.txt",float)
years=data[:,0]
liebres=data[:,1];linces=data[:,2];zanahorias=data[:,3]
n=np.size(liebres)

# Calcular la transformada de Fourier de los datos
ck = fft(data)
T=1/365
frecuencias_liebres = fftfreq(len(liebres), T)
frecuencia_linces=fftfreq(len(data),T)
pe_lineces=[]
pe_liebres=[]

for k in frecuencias_liebres:
    pe_liebres.append(1/k)
periodoli=sum(pe_liebres)/n
print("El periodo de evolución de las liebres es:",periodoli,"[s]")


for k in frecuencia_linces:
    pe_lineces.append(1/k)
periodolinces=sum(pe_liebres)/n
print("El periodo de evolución de los linces es:",periodolinces,"[s]")

####################### 2 #################################

datos=np.loadtxt("data_signals.txt")

# Definir parámetros de tiempo
tiempo_inicial = 0
tiempo_final = 2.5
sampleo = 0.0025

tiempo = np.arange(tiempo_inicial, tiempo_final, sampleo)

# Calcular la transformada de Fourier de los datos
ck = fft(datos)
frecuencias = fftfreq(len(datos), d=sampleo)

# Obtener las frecuencias dominantes
amplitudes = np.abs(ck)
frecuencias_dominantes = frecuencias[amplitudes < np.max(amplitudes)]

#   a)       Imprimir las frecuencias dominantes
print("Frecuencia dominante:")
for freq in frecuencias_dominantes:
    print(freq,"HZ")



# b)  Imprimir la función con frecuencía mas alta
print("La sinusoidal con más frecuencia posee",np.max(frecuencias_dominantes),"[Hz]")

# Crear el gráfico
fig, axs = plt.subplots(2, 1, figsize=(8, 10))
intervalo_tiempo = 0.5
indices_intervalo = np.logical_and(tiempo >= 0, tiempo < intervalo_tiempo) #np.logical es una funcion que nos ayuda a definir las condiciones del intervalo


# Primer panel: señal original en función del tiempo
axs[0].plot(tiempo[indices_intervalo], datos[indices_intervalo],"-r")
axs[0].set_xlabel("Tiempo (s)")
axs[0].set_ylabel("Amplitud")
axs[0].set_title("Señal original")
axs[0].grid()


# Segundo panel: 

axs[1].plot(frecuencias,amplitudes)
axs[1].set_xlabel('Frecuencia (Hz)')
axs[1].set_ylabel('Amplitud')
axs[1].set_title('Espectro de Fourier')
axs[1].grid()
plt.tight_layout()
plt.show()
