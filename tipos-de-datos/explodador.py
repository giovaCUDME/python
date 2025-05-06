#giovanni molinet, tocar guitarra, 1/03/25

#creo mi lista
comida = ["arroz","carne","fideos","pollo","papas"]

#accedo al ultimo elemento
print(comida[3])

#cambiar el valor
comida[-1]= "chocolate"

print(comida)

#agregar un elemento al final
comida.append("mariscos")

print(comida)

#inserta un elemento en la segunda posicion de la lista
comida.insert(2, "pescado")

print(comida)

#elimina un elemento de la lista usando su valor
eliminar = comida.pop(0)

print(comida)

#encuentra la posicion de un elemento especifico con .index().
indice = comida.index("pollo")

print(indice)

#ordenar la lista alfabeticamente o de menor a mayor si son numeros
comida.sort()
print(comida)

#invierte el orden de la lista
comida.reverse()
print(comida)