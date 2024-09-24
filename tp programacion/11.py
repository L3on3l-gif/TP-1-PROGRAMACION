print("Las recetas disponibles son: Milanesas, Tarta de pollo, Fideos con estofado de carne")
while True:
    nomrece = input("Ingrese el nombre especifico de la receta que quiere cocinar(Si desea salir del programa ingrese 'salir'): ")
    if(nomrece == "salir"):
        print("Programa finalizado")
        break
    if(nomrece == "Milanesas"):
        print()
        print("Nombre de la receta:", nomrece)
        print("Los ingredientes son: 4 huevos, 2 dientes de ajo, Perejil picado, Sal y pimienta, a gusto, Pan rallado y 1 kilo de nalga o peceto")
        print("El tiempo de preparacion es de 15min")
        print("Dificultad: Facil")
        print()
    elif(nomrece == "Tarta de pollo"):
        print()
        print("Nombre de la receta:", nomrece)
        print("Los ingredientes son: 2 pechugas grandes de pollo cocidas (puede utilizarse cualquier parte del pollo), 1 cebolla picada, 2 dientes de ajo, 2 varas de cebolla de verdeo, 2 huevos, 1/2 morrón rojo, 1 taza de caldo de gallina o verdura, ají molido, ajo en polvo, pimentón, a gusto y 2 tapas pascualina ")
        print("El tiempo de preparacion es de 45min")
        print("Dificultad: Media")
        print()
    elif(nomrece == "Fideos con estofado de carne"):
        print()
        print("Nombre de la receta:", nomrece)
        print("Los ingredientes son: 1/2 kg carne vacuna, 4 papas grandes, 1 cebolla grande, morrón, 2 zanahorias, provenzal, sal a gusto, aceite, 1 hoja laurel, puré de tomate a gusto y fideos de tallarín o el que usted desee")
        print("El tiempo de preparacion es de 40min")
        print("Dificultad: Media")
