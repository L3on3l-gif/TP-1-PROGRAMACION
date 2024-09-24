monto_compra = float(input("Ingrese el monto de su compra: "))
miembro = input("¿Es usted miembro de la tienda? (si/no): ").strip().lower()
descuento = 0
if(monto_compra > 1000 and miembro == "si"):
    descuento = 0.10
elif(miembro == "si"):
    descuento = 0.5
else:
    descuento = 0.0
monto_descuento = monto_compra * descuento
preciofinal = monto_compra - monto_descuento
print("El descuento efectuado es de: ", monto_descuento)
print("El pago final que tiene que depositar es de: ", preciofinal)

    
