#giovanni molinet

cantantes = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"},

   {"nombre": "José José", "pais": "México"},

   {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}

]

# def iterarDiccionario(lista):
#     for diccionario in lista:
#         print("," .join (f"{key} - {value}" for key, value in diccionario.items()))

# IterarDiccionario(cantantes)

def IterarDiccionario2(artista, nac):
    for diccionario in nac:
        if artista in diccionario:
            print(diccionario[artista])

# ejemplo de uso:

IterarDiccionario2("nombre", cantantes)
IterarDiccionario2("pais", cantantes) 