###### Variables ######
entero = 1
flotante = 1.5
boolean = True

###### Strings #######
stringg = "Cuando yo la vi"
sss = """
Dije si esa mujer fuera para mí
Perdóname, te lo tenía que decir
Tas' dura, dura, dura
Tú ta' dura mano arriba que tu
te ves bien
"""
print(stringg, sss)
print(len(sss))
# print(sss[5:15])

nombre = "Mauro"
apellido = "Jelvez"
nombrecompleto = f"{nombre} {apellido} {apellido} {"y que pasa chuchetumare"}" # EDITAR STRING O UNIR STRINGS
print(nombrecompleto)


########## Funciones strings ####################
animal = "Perro cULIao"
print(animal.upper()) ##MAYUSCULA
print(animal.lower()) ##MINUSCULA
print(animal.capitalize()) #MAYUSCULA PRIMERA LETRA
print(animal.title())  ##MAYUSCULA PRIMERA LETRA DE CADA PALABRA
print(animal.strip())  ##ELIMINAR ESPACIOS INNECESARIOS
print(animal.strip().capitalize()) ##ENCADENAR METODOS

