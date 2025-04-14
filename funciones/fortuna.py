#giovanni molinet
#14-04-2025

import random

respuesta = random.randint(0, 7)

opciones = ['No persigas la felicidad, creala',
           'Todas las cosas son dificiles antes de ser faciles',
           'el pajaro madrugador consigue el gusano, pero el segundo raton consigue el queso',
           'alguien en tu vida necesita una carta de tu parte',
           'No solo pienses. ¡Actua!',
           'Tu corazon se acelera',
           'La fortuna que buscas esta en otra galleta',
           '¡ayuda! ¡Estoy prisionuna panaderia china!']

def fortuna():
    fortuna = random.randint(0, len(opciones)-1)
    print(opciones[fortuna])
    
fortuna()