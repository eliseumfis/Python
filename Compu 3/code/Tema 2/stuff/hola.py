import numpy as np
tiempo_inicial = 0.0
tiempo_final = 1.999
resolucion_temporal = 0.002

tiempo = np.arange(tiempo_inicial, tiempo_final, resolucion_temporal)

intervalo_tiempo = 0.01
indices_intervalo = np.logical_and(tiempo >= 0, tiempo < intervalo_tiempo)
#axs[2].plot(tiempo[indices_intervalo], data[indices_intervalo])



#print(indices_intervalo)

t=np.arange(0,0.01,0.002)
tiemposs=[]
for k in t:
    tiemposs.append(data[k])
