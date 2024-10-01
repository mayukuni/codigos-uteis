# 1
A = int(input())
B = int(input())
C = int(input())
D = int(input())
DIFERENCA = (A * B) - (C * D)

print("DIFERENCA =", DIFERENCA)

# 2
km = int(input())
litros = float(input())
consumo = km / litros

print("{:.3f} km/l".format(consumo))

# 3
funcionario = int(input())
horas = int(input())
valor = float(input())
salario = horas * valor

print("NUMBER =", funcionario)
print("SALARY = U$ {:.2f}".format(salario))

# 4
vendedor = input()
salario = float(input())
vendas = float(input())
comissao = (vendas / 100) * 15
total = salario + comissao

print("TOTAL = R$ {:.2f}".format(total))

# 5
A = float(input())
B = float(input())
C = float(input())
A, B, C = map(float, input().split())

print("TRIANGULO: {:.3f}".format(A * C / 2))
print("CIRCULO: {:.3f}".format(3.14159 * (C ** 2)))
print("TRAPEZIO: {:.3f}".format(((A + B) * C) / 2))
print("QUADRADO: {:.3f}".format(B ** 2))
print("RETANGULO: {:.3f}".format(A * B))

# 6
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
total = (x2 - x1) ** 2 + (y2 - y1) ** 2

print("{:.4f}".format(total ** 0.5))