class Personaje:
    nombre = "Default"
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0
    def __init__ (self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    def atributos (self):
        print(self.nombre, ";", sep= "")
        print("fuerza:", self.fuerza)
        print("inteligencia:", self.inteligencia)
        print("defensa:", self.defensa)
        print("vida:", self.vida)
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
    def esta_vivo(self):
        return self.vida> 0
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto,.")
    def daño (self, enemigo):
        return self.fuerza - enemigo.defensa
    def atacar(self, enemigo):
        daño = self.daño (enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        print("la vida es", enemigo.nombre, "es", enemigo.vida)
        if enemigo.esta_vivo():
            print("la vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

    def get_fuerza(self):
        return self.fuerza
    def set__fuerza(self, fuerza):
        self.fuerza - fuerza


class Guerrero(Personaje):
        def __int__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
            super().__init__(self, nombre, fuerza, inteligencia, defensa, vida)
            self.espada = espada

        def cambiar_arma(self):
            opcion = int(input("elige un arma: (1) acero valyrio, daño 8. (2) matadragones, daño 3:"))
            if opcion == 1:
                self.espada = 8
            elif opcion == 2:
                self.espada = 10
            else:
                print("ingresa una opcion valida")

        def atributos(self):
            super().atributos()
            print("espada:", self.espada)

        def daño (self, enemigo):
            return self.fuerza * self.espada - enemigo.defensa
        
        class magfo(Personaje):
            def __int__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
              super().__init__(nombre, fuerza, inteligencia, defensa, vida, libro)
              self.libro = libro
        def atributos(self):
            super().atributos()
            print("libros", self.libro)
            def daño (self, enemigo):
                return self.inteligencia * self.libro - enemigo.defensa

kaldrogo = Guerrero("kaldrogo", 20, 30, 20, 5)
mi_personaje = Personaje("gico", 10, 20, 10, 100)




kaldrogo.cambiar_arma
kaldrogo.atributos()
print(kaldrogo.espada)





# mi_personaje = Personaje("VictGio", 10, 20, 10, 100)
# mi_enemigo = Personaje("Doom", 8, 5, 3, 5)
# mi_personaje.atacar(mi_enemigo)
# print(mi_personaje.get_fuerza(-5))
# mi_personaje.atributos()
# print(mi_personaje.daño(mi_enemigo))
# mi_personaje.atributos()
# mi_enemigo.atributos()
# mi_personaje.nombre = "VictGio"
# mi_personaje.fuerza = 20
# print(mi_personaje)
# print("el nombre del juego es", mi_personaje.nombre)
# print("la fuerza de mi personaje es", mi_personaje.fuerza)
# mi_personaje.atacar(mi_enemigo)
# mi_personaje.atributos()
# mi_enemigo.atributos()