import numpy as np
import matplotlib.pyplot as plt

data=np.loadtxt("sunspot.txt",float)

n_x = data.shape[0]
xi = np.arange(n_x)
yi = data[:,1]

ck = np.fft.fft(yi)

#Una vez obtenidos los valores de los coeficientes podemos calcular la inversa con la 
# función ifft que pertenece al mismo módulo fft. Estos valores de la función restaurada los guardaremos en el arreglo yiFS

yiFS = np.fft.ifft(ck)
fig, axs = plt.subplots(3)
axs[0].plot(xi, yi, '-r')
axs[1].plot(ck, '-b')
axs[2].plot(xi, yiFS, '-g')
plt.show()