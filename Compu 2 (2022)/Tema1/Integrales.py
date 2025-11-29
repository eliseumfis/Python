import numpy as np
import matplotlib.pyplot as pl

#Pregunta 1

def f(x):
  return np.exp(2 * x) + 4*x**2 + 2

a = 0; b = 4
valor_r = 1583.31232
lista_trap = []
lista_simp = []
lista_N = []
lista_err_trap = []
lista_err_simp = []

for N in range(2, 31, 2): #Ciclo para N variable
  h = np.abs(b - a) / N
  i1 = 0
  lista_N.append(N)
  for k in range(1, N): #Método Trapezoidal
    i1 += f(a + k*h)
  I = h * ((f(a) + f(b))/2 + i1)
  lista_trap.append(I)
  err_trap = np.abs(valor_r - I) * 100 / valor_r
  lista_err_trap.append(err_trap)

  #Método de Simpson
  
  suma_S_impar = 0

  for i in range(1, N, 2):
    suma_S_impar += f(a + h*i)
  
  suma_S_par = 0

  for j in range(2, N-1, 2):
    suma_S_par += f(a + h*j)
  
  resultado_S = (h/3) * (f(a) + 4*suma_S_impar + 2*suma_S_par + f(b))
  lista_simp.append(resultado_S)
  
  err_simp = np.abs(valor_r - resultado_S) * 100 / valor_r
  lista_err_simp.append(err_simp)


pl.clf()
pl.subplot(1, 2, 1)
pl.plot(range(2, 31, 2), lista_trap, '-b',
        lista_N, lista_simp, '-r')
pl.title('Valores de la integral')
pl.xlabel('N° de secciones');pl.ylabel('Valores de I')
pl.grid()
pl.legend(('trapz','Simp',), loc='best')

pl.subplot(1, 2, 2)
pl.plot(range(2, 31, 2), lista_err_trap, '-b',
        range(2, 31, 2), lista_err_simp, '-r')
pl.xlabel('N° de secciones');pl.ylabel('Err')
pl.title('Error relativo porcentual')
pl.grid()
pl.legend(('trapz','Simp',), loc='best')
pl.show()


#%%

#Pregunta 2


import numpy as np
import matplotlib.pyplot as pl


def f(x):
    return 8*np.exp(x)*(np.sin(x))**2 + np.cos(x)

a = 0 ; b = np.pi / 2 ; N = 4
h = np.abs(b-a)/ N

#Por Trapezoidal
suma = 0
for i in range(1,N):
    suma += f(a+h*i)
resultado_trap1 = h*(((f(a)+f(b))/2) + suma)
while True:
    N = 2*N
    h = np.abs(b-a)/ N
    suma = 0
    for i in range(1,N):
        suma += f(a+h*i)
    resultado_trap2 = h*(((f(a)+f(b))/2) + suma)
    error_t2 = np.abs(resultado_trap2 - resultado_trap1) / 3
    error_rp_t2 = error_t2*100 / resultado_trap2
    if error_rp_t2 < 0.001:
        break
    else:
        resultado_trap1 = resultado_trap2

print("el resultado que cumple la condicion es:",resultado_trap2)
print("el numero de secciones necesarias fue:", N)

#Por Simpson

N = 4 #Se redefinen las variables iniciales.
h = np.abs(b - a) / N
suma_impar = 0

for i in range(1, N, 2):
  suma_impar += f(a + h*i)

suma_par = 0

for j in range(2, N-1, 2):
  suma_par += f(a + h*j)

resultado_simpson = (h / 3) * (f(a) + 4*suma_impar + 2*suma_par + f(b))

while True:

  N = N*2
  h = abs(b - a) / N
  suma_impar = 0

  for i in range(1, N, 2):
    suma_impar += f(a + h*i)

  suma_par = 0

  for j in range(2, N-1, 2):
    suma_par += f(a + h*j)

  resultado_simpson_2 = (h / 3) * (f(a) + 4*suma_impar + 2*suma_par + f(b))

  err_simp_2 = abs(resultado_simpson_2 - resultado_simpson) / 15
  err_rp_simp_2 = err_simp_2 *100 / resultado_simpson_2

  if err_rp_simp_2 < 0.001:
    break
  else:
    resultado_simpson = resultado_simpson_2

print('El resultado que cumplió con la condición es: ', resultado_simpson_2)
print('El número de secciones que cumplió la condición es: ', N)
