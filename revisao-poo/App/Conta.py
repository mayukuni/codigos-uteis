class Conta:
    def __init__(self, titular, numero, saldo) -> None:
        self.saldo = 0
        self.titular = titular
        self.numero = numero

        @property
        def saldo(self):
            return self.saldo

        @saldo.setter
        def saldo(self, saldo):
            if (saldo < 0):
                print("o saldo nao pode ser negativo")
            else:
                self.saldo = saldo

    def saque(self, valor):
        if (self.saldo >= valor):
            self.saldo -= valor
            print("boaa")
        else:
            print("nao boa")

    def deposita(self, valor):
        self.saldo += valor

    def extrato(self):
        print("Cliente: ", self.titular, "Saldo atual: ", self.saldo)

