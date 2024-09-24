print("***Sistema e reservacion de Hoteles***")
nombre = input("Ingrese su nombre: ")
dias = int(input("Ingrese la cantidad de dias que quiere estar: "))
vista_al_mar = input("¿Quiere vista al mar? a= SI b= NO: ")
print("Cliente:", nombre)
print("Dias de estancia:", dias)
if (dias == 1):
    print("Tarifa diaria: 240")
elif(dias == 2):
    print("Tarifa diaria: 480")
elif(dias == 3):
    print("Tarifa diaria: 720")
elif(dias == 4):
    print("Tarifa diaria: 960")
elif(dias == 5):
    print("Tarifa diaria: 1200")
elif(dias == 6):
    print("Tarifa diaria: 1440")
else:
    print("Excede la cantidad de dias disponibles")
if(vista_al_mar == "a"):
    print("True")
else:
    print("False")
