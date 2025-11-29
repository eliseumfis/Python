#~$ mkdir FIS-COMP
#~$ mkdir FIS-COMP
#~$ mkdir Complementos
#~$ ls
# Complementos   FIS-COMP
#~$ cd FIS-COMP/
#~/FIS-COMP$ mkdir Python, Linux
#~/FIS-COMP$ ls
#Linux  Python,
#~/FIS-COMP$ rmdir Python,/
#~/FIS-COMP$ ls
#Linux
#~/FIS-COMP$ mkdir Python
#~/FIS-COMP$ cd ..
#~$ ls
# 2021-05-06-103552.term   Complementos   FIS-COMP
#~$ cd Complementos/
#~/Complementos$ mkdir QUIZ Evaluaciones Tareas Ejercicios
#~/Complementos$ ls
#Ejercicios  Evaluaciones  QUIZ  Tareas
#~/Complementos$ rmdir QUIZ/
#~/Complementos$ ls
#Ejercicios  Evaluaciones  Tareas
#~/Complementos$ rm E
#Ejercicios/   Evaluaciones/ 
#~/Complementos$ ls
#Ejercicios  Evaluaciones  Tareas
#~/Complementos$ mv Evaluaciones/ Examen
#~/Complementos$ ls
#Ejercicios  Examen  Tareas
#~/Complementos$ cd Tareas/
#~/Complementos/Tareas$ touch tarea1.txt
#~/Complementos/Tareas$ ls
#tarea1.txt
#~$ cd
#~$ ls
# 2021-05-06-103552.term   Complementos   FIS-COMP  prueba1.py
#~$ mv Complementos/Tareas/tarea1.txt Complementos/Examen/prueba1.txt#


#CONVERTIDOR DE GRADOS C° A FARENHEIT Y KELVIN

C=float(input("Inrese los grados celsius que desea calcular:  "))
print("Su equivalencia en Kelvin es", C+273,"grados")
print("Su equivalencia en Farenheit es", (9/5*C)+32, "grados")


#PAGINA WEB PARA MAYORES DE EDAD

x=int(input("Por favor ingrese su edad:  "))
if x>=18:
    print("La suscripcion se hizo con exito")
while x<18:
    print("No cumples con el rango de edad necesario")
    x=int(input("Por favor ingrese su edad nuevamente :  "))
    if x>=18:
        print("La suscripcion se hizo con exito")


#BLOQUEAR CUENTA TRAS 5 INTENTOS DE CONTRASEÑA FALLIDA
#x=1234

y=int(input("Ingrese su contrasena:  "))
intentos=5

while y!=1234:
    print("Contrasena incorrecta, intentos restantes", intentos-1,)
    intentos=intentos-1
    if intentos==0:
        print("Usaste todos tus intentos")
        break
    y=int(input("Ingrese la contrasena"))

if y==1234:
    print("Contrasena correcta")