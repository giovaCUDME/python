#giovanni molinet
#29/05/2025
#un modulo o 

class TarjetaCredito:
    tarjetas = []
    
    def __init__(self, saldo_pagar=0, limite_credito = 100000, interes = 0.02):
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.interes = interes
        TarjetaCredito.tarjetas.append(self)

    def comprar(self, monto):
        if self.saldo_pagar+monto<=self.limite_credito:
            self.saldo_pagar +=monto
            print(f"Compra realizada: ${monto:,}.nuevo saldo:${self.saldo_pagar:,}")
        else:
            print("tarjeta rechaza, haz alncanzado tu limite de credito.+")
            return self
        
    def pago(self, monto):
        self.saldo_pagar -= monto
        if self.saldo_pagar<0:
            self.saldo =0
            print(f"Pago realizado:${monto:,} nuevo saldo: ${self.saldo_pagar:,}")
            return self #nos permite encadenar los metodos
        
    def mostrar_info_tarjeta(self):
        print("----- Informacion de la tarjeta -----")
        print(f"saldo a pagar:${self.saldo_pagar:,}")
        print(f"Limite de credito:{self.limite_credito}")
        print("------------------------------------")
        return self
    
    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar *self.interes
        print(f"interes cobrado. Nuevo saldo:${self.saldo_pagar:,.2f}")
        return self
    
    @classmethod
    def mostrar_todas_tarjetas(cls):
        for i, tarjeta in enumerate (cls.tarjeta, 1):
            print(f"tarjeta {i:} saldo:${tarjeta.saldo_pagar:,}, limite:${tarjeta.limite_credito:,}, interes:{tarjeta.interes:.2%}")

print("======= tarjeta 1 =======")
tarjeta1 = TarjetaCredito()
tarjeta1.comprar(50000).comprar(20000).pago(10000).cobrar_interes().mostrar_info_tarjeta

print("=================================================")

print("======= tarjeta 2 =======")
tarjeta2 = TarjetaCredito()
tarjeta2.comprar(70000).comprar(50000).pago(40000).cobrar_interes().mostrar_info_tarjeta

print("=================================================")

print("======= tarjeta 3 =======")
tarjeta3 = TarjetaCredito()
tarjeta3.comprar(30000).comprar(300000).cobrar_interes().mostrar_info_tarjeta

print("=================================================")

# tarjeta1 = tarjetaCredito(limite_credito=200000, interes = 0.02)
# tarjeta1.comprar(50000)
# tarjeta1.pago(30000)
# tarjeta1.mostrar_info_tarjeta()
# tarjeta1.cobrar_interes() 