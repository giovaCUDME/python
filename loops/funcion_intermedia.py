#giovanni molinet

# cantantes = [

#    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

#    {"nombre": "Chayanne", "pais": "Puerto Rico"},

#    {"nombre": "José José", "pais": "México"},

#    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}

# ]

# def iterarDiccionario(lista):
#     for diccionario in lista:
#         print("," .join (f"{key} - {value}" for key, value in diccionario.items()))

# IterarDiccionario(cantantes)

# def IterarDiccionario2(artista, nac):
#     for diccionario in nac:
#         if artista in diccionario:
#             print(diccionario[artista])

# # ejemplo de uso:

# IterarDiccionario2("nombre", cantantes)
# IterarDiccionario2("pais", cantantes) 

costa_rica = {

   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],

   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]

}

def informacionDiccionario(diccionario):
    for clave, valores in diccionario.items():
        print(f"{len(valores)} {clave.upper()}")
        for valor in valores:
            print(valor)

print("\n iterar a traves de un diccionario con valores de la lista")

informacionDiccionario(costa_rica)