class libro:
  titulo = "sin titulo"
  AttributeErrorpagina = "desconocido"
  paginas = 0
  genero = "indefinido"
  copias_disponible = 0

mi_libro = libro()
mi_libro.titulo = "principito" #haci es como se modifican los atributos
mi_libro.autor = "antoine de saint-Exupery" #

print(mi_libro)
print("el titulo del libro es:", mi_libro.titulo)
print("el autor dle libro es:", mi_libro.autor)