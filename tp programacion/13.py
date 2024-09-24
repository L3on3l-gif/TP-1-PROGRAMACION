usuariocorrect = "admin"
paswordcorrect = "2678"
while True:
    usuario = input("Ingrese el usuario: ")
    contraseña = input("Ingrese la contraseña: ")
    if (usuario == usuariocorrect and contraseña == paswordcorrect):
        print("Datos correctos? True")
        break
    else:
        print("Datos incorrectos, intentelo denuevo")
