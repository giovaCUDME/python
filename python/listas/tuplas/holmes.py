pistas = ("puerta roja",221,"londres",3.14,"watson",7,"moriarty")

print("🔎¡bienvenido, detective holmes")
print("📜 se ah encotrnado una serie de pistas miesteriosas...")
print("pistas encontradas", pistas)

#📌 Analisis de pistas
print("\n 🕵️ analizando pistas...")

print("\n 🕵️ felicitaciones, detective. ¡has resuelto el analisis de las psitas!")
print("🔐 ahora sigue con las deducciones oara resolver el misterio")


#¿Cual es la primera pista?
print(pistas[0])

#¿Cual es la ultima pista?
print(pistas[-1])

#Cuantas pistas hay en total
print(len(pistas))

#¿Esta la palabra "londres en las pistas?"
print('londres' in pistas)

#Desempaqueta las primeras tres pistas
a, b, c, d, f, g = pistas
print(a,b,c)

#Crea una nueva tupla con pistas nuevas
pistasTeisi = ('edificio', "4:35")

#Encuentra la poscicion de "watson"
print(pistas.index("watson"))

#¿Cuantas veces aparece el numero 7 en las pistas
print(pistas.count("7"))