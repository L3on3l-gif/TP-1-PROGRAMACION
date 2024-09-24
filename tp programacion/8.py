print("*** Generador de Email ***")
nombre_de_usuario =("Alfredo Vazquez")
empresa = "Instituto Educativo Superior Manuel Belgrano"
extension = (".com.ar")
num = ".".join([palabra.lower() for palabra in nombre_de_usuario.split()])
sep = empresa.split()
empresaini = ".".join([palabra[0].lower() for palabra in sep])
print("Nombre de Usuario:", nombre_de_usuario)
print("Nombre de usuario normalizado:", num)

print("Nombre empresa:", empresa)
print("Extension del dominio:", extension)
print("Dominio de email normalizado:", "@" + empresaini)
print("Email final generado:", num + "@" + empresaini + extension)
