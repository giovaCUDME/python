#giovanni molinet
#31/03/25
#soy un helicoptero

ph = int(input('ingresa el nivel de ph (0-14):'))

if ph > 7:
    print('basico')
elif ph < 7:
    print('acido')
else:
    print('neutro')