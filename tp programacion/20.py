from random import randint
a = randint(0, 10)
if(a > 9 and a == 10):
    print(a)
    print("En la clasificacion de letras el numero es una A")
elif(a >= 8 and a < 9):
    print(a)
    print("En la clasificacion de letras el numero es una B")
elif(a >= 7 and a < 8):
    print(a)
    print("En la clasificacion de letras el numero es una C")
elif(a >= 6 and a < 7):
    print(a)
    print("En la clasificacion de letras el numero es una D")
elif(a >= 0 and a < 6):
    print(a)
    print("En la clasificacion de letras el numero es una F")
else:
    print("Valor desconocido")
