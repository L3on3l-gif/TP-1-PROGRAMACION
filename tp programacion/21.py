a = input("¿Tiene destino Internacional o Nacional su envio?: ")
b = int(input("Ingrese el peso en kilogramos del paquete: "))
costo_tarifas_b = 10
costo_tarifas_a = 20
if(a == "Nacional" and costo_tarifas_b > 0):
    print(f"El destino es {a} y el peso en kilogramos es {b}. Son " + "$10 X Kilo")
    costo_envio = b * costo_tarifas_b
    print("Serian $",costo_envio)
elif(a == "Internacional" and costo_tarifas_a > 0):
    print(f"El destino es {a} y el peso en kilogramos es {b}. Son " + "$20 X Kilo")
    costo_envio = b * costo_tarifas_a
    print("Serian $",costo_envio)
