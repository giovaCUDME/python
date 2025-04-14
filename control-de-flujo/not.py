#giovanni molinet
#02-04-25

respuesta = input('estas cansado? (si/no):').strip().lower()

cansado = respuesta == 'si'

if not cansado:
    print('!Es hora de programar')

else:
    print('tomate un descanso mi chanchito')