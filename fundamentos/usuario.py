#giovanni molinet
#esto es un archivo y un modulo
from tarjeta import TarjetaCredito
import tarjeta

class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0
    def agregar_tarjeta(self, tarjeta):
        """Agregar una nueva tarjeta al usuario."""
        self.tarjetas.append(tarjeta)

    def hacer_compra(self, monto, indice_tarjeta=0):
        """Realiza una compra en la tarjeta especificada (por indice)"""
        if 0<= indice_tarjeta < len(self.tarjetas):
            self.tarjetas[indice_tarjeta].pago(monto)
        else:
            print(f"No existe la tarjeta con indice {indice_tarjeta}.")
            return self
        

