class Cafe():
    def que_soy(self):
        print("soy un cafe")

class Te():
    def que_soy(self):
        print("soy un Te")

def definicion_bebida(bebida):
    bebida.que_soy()

definicion_bebida(Te())