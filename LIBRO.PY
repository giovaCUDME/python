class Libro:
#   titulo = "sin titulo"
#   AttributeErrorpagina = "desconocido"
#   paginas = 0
#   genero = "indefinido"
#   copias_disponible = 0

  def __init__(self, titulo, autor, paginas, genero, copias_disponibles):
      self.titulo = titulo
      self.autor = autor
      self.paginas = paginas
      self.genero = genero
      self.copias_disponibles = copias_disponibles

  def atributos(self):
      print(self.titulo, ":", sep = "")
      print("*Autor:", self.autor)
      print("*Paginas:", self.genero)
      print("*Copias Disponibles", self.copias_disponible)

  def incrementar_copias(self, nuevas_copias):
      self.copias_disponibles = self.copias_disponibles+nuevas_copias
     
  def esta_disponible(self):
      return self.copias_disponibles>0
  
  def agotado(self):
      self.copias_disponibles == 0
      print(self.titulo, "esta agotado")
  
  def prestar (self, copias = 1):
      if self.copias_disponibles >= copias:
          self.copias_disponibles -=copias
          print(f"has prestado{copias} copias(s) de '{self.titulo}'.")
      else:
          print(f"no hay suficientes copias disponibles es '{self.titulo}'para prestar")

mi_libro = Libro("principito", "antoine de saint-Exapury", 154, "cuento", 10) #haci se crea un bojeto de la clase libro
mi_libro.atributos()
mi_libro.agotado() #metodo agotado
print("¿esta disponible?:", mi_libro.esta_disponible())
# mi_libro.incrementar_copias(3)
# print("atributos despues de incremento")
# mi_libro.atributos()
# mi_libro.titulo = "principito" #haci es como se modifican los atributos
# mi_libro.autor = "antoine de saint-Exupery" #haci se modifican los atributos

print("\n --------------------------")
print(mi_libro)
print("el titulo del libro es:", mi_libro.titulo) #esta llamada al atributo titulo
print("el autor dle libro es:", mi_libro.autor) #y esta al atributo autor