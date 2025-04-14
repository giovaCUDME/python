#giovanni molinet
#02-04-25

altura = int(input('¿cual es tu altura? (cm)'))
#crearon una variable para solicitar informacion al usuario
creditos = int(input('¿Cantos credsitos tienes?'))

if altura >= 137 and creditos >= 10:
    print('disfruta tu viaje')
elif altura < 137 and creditos >= 10:
    print('no tienes la altura suficiente')
elif altura >= 137 and creditos < 10:
    print('no tienes el credito suficiente')
else:
    print('no tienes la altura ni el credito suficiente')
