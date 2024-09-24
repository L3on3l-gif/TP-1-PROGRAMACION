nombre = input("Ingrese su nombre de cliente: ")
dias = int(input("¿Cuantos dias va a quedarse?: "))
vistas = input("¿Quiere habitacion con vista al mar?(si-no): ")
if(vistas == "si"):
    print("Se cobraran $5.000 mas por las vistas al mar, quedandole un total de $10.000 por dia.")
else:
    print("Se cobrara en total $10.000 por dia.")



