import numpy as np
import matplotlib.pylab as pl
import scipy.fftpack as sc

#Cargar datos
datos=np.loadtxt("Datos_teo.txt", float)
#Espaciado de tiempo
t_s=0.002 #[s]

#pregunta a)
#Calcular dft para los datos 

ck=sc.fft(datos)

#frecuencias del espacio

freq=sc.fftfreq(datos.size, d=t_s)

#Frecuencias dominantes
max_term=[]; ult_term=0 ; ck_abs=abs(ck)
while len(ck_abs)>1:
    term=np.argmax(ck_abs,axis=0)
    #print(term)
    max_term.append(term)
    ck_abs=ck_abs[term+1:]
    ult_term=term
print("Las frecuencias dominantes son:", np.sort(max_term))

#sin ruido
ck_clean=np.zeros(ck.size, dtype=complex)
ck_clean[max_term]=ck[max_term]
yn=sc.ifft(ck_clean)
#plot

pl.clf()
fig, ax = pl.subplots(3)
ax[0].plot(np.linspace(0,0.1,1000),datos)
ax[0].grid()
ax[1].plot(abs(ck),'-r')
ax[1].grid()
ax[2].plot(np.linspace(0,0.1,1000),yn,'-g')
ax[2].grid()
