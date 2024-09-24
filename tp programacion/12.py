print("Hola! Vamos a crear un ID unico para usted, siga los pasos a continuacion.")
print()
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
añodenaci = int(input("Ingrese su año de nacimiento en numeros: "))
añodenaci_str = str(añodenaci)
from random import randint
a = randint(1, 4235)
id_unico = nombre[0].upper() + nombre[1].upper() + apellido[0].upper() + apellido[1].upper() + añodenaci_str[-2] + añodenaci_str[-1]
print("El ID unico es:", id_unico + str(a))

