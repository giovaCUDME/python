class libro:
  titulo = "sin titulo"
  AttributeErrorpagina = "desconocido"
  paginas = 0
  genero = "indefinido"
  copias_disponible = 0
  def __init__(self, titulo, autor, paginas, genero, copias_disponibles):
      self.titulo = titulo
      self.autor = autor
      self.paginas = paginas
      self.genero = genero
      self.copias_disponible = copias_disponibles
      

mi_libro = libro()
mi_libro.titulo = "principito" #haci es como se modifican los atributos
mi_libro.autor = "antoine de saint-Exupery" #haci se modifican los atributos

print(mi_libro)
print("el titulo del libro es:", mi_libro.titulo) #esta llamada al atributo titulo
print("el autor dle libro es:", mi_libro.autor) #y esta al atributo autor 6tg6y |                                                  x 