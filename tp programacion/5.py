print("*** Sistema de Tienda Online ***")
print("Los productos a la venta son los siguiente: Camara digital; Telefono Samsung A12; Laptop; PlayStick")
while True:
    producto = input("Escribe el nombre especifico del producto (o 'salir' para terminar): ")
    if producto == "salir":
        print("Saliendo del programa.")
        break
    if(producto == "Camara digital"):
        print("Producto: Camara digital")
        print("Precio: $399.99")
        print("Cantidad inventario: 20")
        print("Disponible: True")
    elif(producto == "Telefono Samsung A12"):
        print("Producto: Telefono Samsung A12")
        print("Precio: $299.99")
        print("Cantidad inventario: 5")
        print("Disponible: True")
    elif(producto == "Laptop"):
        print("Producto: Laptop")
        print("Precio: $499.99")
        print("Cantidad inventario: 5")
        print("Disponible: True")
    elif(producto == "PlayStick"):
        print("Producto: PlayStick")
        print("Precio: $249.99")
        print("Cantidad inventario: 0")
        print("Disponible: False")
        
