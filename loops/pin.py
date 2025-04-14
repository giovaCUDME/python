#giovanni molinet
#07-04-25

print('BANCO DEL 4°B')

pin = int(input('ingresa tu PIN:'))

while pin !=1234:
    pin = int (input('PIN incorrecto, ingresa tu PIN nuevamente:'))

if pin ==1234:
    print('!PIN aceptado')
    print('Bienvenido a tu cuenta')

