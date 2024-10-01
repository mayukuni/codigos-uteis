# # 1
# num = int(input())
# if num % 2 == 0:
#     num2 = num - 1
# else: 
#     num2 = num - 2

# if num % 2 == 0:
#     num3 = num + 2
# else:
#     num3 = num + 1

# print(num2, num3)

# # 2
# trabalhos = float(input())
# provas = float(input())

# media = (trabalhos + provas) / 2
# if media >= 6:
#     print("aprovado")
# elif (trabalhos + 10) / 2 >= 6:
#     print("talvez com a sub")
# else:
#     print("reprovado")

# 3
dia = input()
num = int(input())
dias = ["domingo", "segunda", "terca", "quarta", "quinta", "sexta", "sabado"]
index = dias.index(dia) + num
if index >= 7:
    index = index - 7
entrega = dias[index]
if dia == entrega:
    print('chega hoje!')
else:
    print('sera entregue ' + entrega)
