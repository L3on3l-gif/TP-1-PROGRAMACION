USUARIO = "leo89"
CONTRASEÑA = "boina202"
while True:
    a = input("Ingrese el usuario: ")
    b = input("Ingrese la contraseña: ")
    if (a == USUARIO and b == CONTRASEÑA):
        print("Bienvenido al sistema")
        break
    elif(a != USUARIO and b == CONTRASEÑA):
        print("Usuario incorrecto. Intentelo denuevo.")
    elif(b != CONTRASEÑA and a == USUARIO):
        print("Contraseña incorrecta. Intentelo denuevo.")
    elif(a != USUARIO and b != CONTRASEÑA):
        print("Usuario y contraseña incorrectos. Intentelo denuevo.")
