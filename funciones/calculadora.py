#giovanni molinet
#16-04-2024

def calculadora (operacion, g, m):
    if operacion == 'suma':
        return g + m
    elif operacion == 'resta':
        return g - m
    elif operacion == 'multiplicacion':
        return g * m
    elif operacion == 'division':
        return g / m
    elif operacion == 'potencia':
        return g ** m
    else:
        return 'operacion invalida'

respuesta = calculadora('suma', 8, 3)
print(respuesta)

respuesta1 = calculadora('resta', 8, 3)
print(respuesta1)

respuesta2 = calculadora('multiplicacion', 8, 3)
print(respuesta2)

respuesta3 = calculadora('division', 8, 3)
print(respuesta3)

respuesta4 = calculadora('potencia', 8, 3)
print(respuesta4) 