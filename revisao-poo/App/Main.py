from Conta import Conta
from Cliente import Cliente


class Main:
    pass


print("oii")


teste2 = Cliente("eeeee", "342342342")
teste = Conta(teste2._nome, "34324234234", 432)

print(teste, "id")
print(teste.titular, teste.numero, teste.saldo)
# print(teste2._nome, teste2._telefone)

teste.deposita(100)
teste.saque(50)
teste.extrato()
