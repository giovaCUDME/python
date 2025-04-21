#giovanni molinet
#21-04-2025
#me gustan las mujeres

def obtener_articulo(opcion):
    if opcion == 1:
        return 'Hamburguesa con queso'
    elif opcion == 2:
        return 'Papas fritas'
    elif opcion == 3:
        return 'Refresco'
    elif opcion == 4:
        return 'Helado'
    elif opcion == 5:
        return 'Galleta'
    else:
        return 'opcion no valida'

articulo = int(input("agrege el numero que desee:"))
print(obtener_articulo(articulo))

