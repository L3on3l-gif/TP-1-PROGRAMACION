from random import randint
a = randint(1, 16)
if(a == 1 or a == 2 or a == 12):
    print(a)
    print("Es un mes de invierno")
elif(a == 3 or a == 4 or a == 5):
    print(a)
    print("Es un mes de primavera")
elif(a == 6 or a == 7 or a == 8):
    print(a)
    print("Es un mes de verano")
elif(a == 9 or a == 10 or a == 11):
    print(a)
    print("Es un mes de otoño")
else:
    print(a)
    print("Estacion desconocida")
