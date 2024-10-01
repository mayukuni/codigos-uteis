# num1 = 10
# num2 = 5
# if num1 % num2 > 1:
#     if 3 + 5 / num2 > 4:
#         print(num1)
# else:
#     if num1 // num2 > 1:
#         num2 = num1 + 5
#     else:
#         num1 = num2 + 5
# if 2 + num1 / num2 * 3 >= 18:
#     num2 = num2 % num1
# else:
#     num1 = num1 % num2
# print(num1 + num2)

# exemplo de loop infinito
# cont = 0
# idade = 0
# peso = 0
# while peso < 5:
#     if peso > 5:
#         cont = cont + idade
#     idade = idade + 3
#     idade = int(input("Digite a idade: "))

# def exibe_media(nota1, nota2):
#     media = (nota1 + nota2) / 2
#     print("Média: ", media)
#     return 

if 10 % 11 == 1:
    print("A")
else:
    n1 = 10 % 11
    if n1 % 2 == 0 and n1 % 2 == 1:
        n2 = n1 + 5
    else:
        n2 = 5
n2 = n2 // 2 + 5 * n2 // 3
print(n2)
print(n1)
print(n1 + n2 % 2)
