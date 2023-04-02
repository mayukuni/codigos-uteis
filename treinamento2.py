# # 1
# A, B = map(int, input().split())

# if A % B == 0 or B % A == 0:
#     print("Sao Multiplos")
# else:
#     print("Nao sao Multiplos")

# # 2
# month = int(input())

# if month == 1:
#     print("January")
# elif month == 2:
#     print("February")
# elif month == 3:
#     print("March")
# elif month == 4:
#     print("April")
# elif month == 5:
#     print("May")
# elif month == 6:
#     print("June")
# elif month == 7:
#     print("July")
# elif month == 8:
#     print("August")
# elif month == 9:
#     print("September")
# elif month == 10:
#     print("October")
# elif month == 11:
#     print("November")
# elif month == 12:
#     print("December")

# # 3
# value1 = int(input())
# value2 = int(input())
# value3 = int(input())
# value4 = int(input())
# value5 = int(input())

# var = 0

# for i in [value1, value2, value3, value4, value5]:
#     if i % 2 == 0:
#         var += 1

# print(var, "valores pares")

# # 4
# A = int(input())
# B = int(input())
# option = int(input())
# if option == 1:
#     print((A + B) / 2)
# elif option == 2:
#     if A > B:
#         print(A - B)
#     else:
#         print(B - A)
# elif option == 3:
#     print(A * B)
# elif option == 4:
#     if B != 0:
#         print(A / B)
#     else:
#         print("Divisao impossivel")
# else:
#     print("Opcao inválida")

# # 5
# type = int(input())
# value = float(input())
# if type == 1:
#     print("{:.2f}".format(value + (value * 0.03)))
# elif type == 2:
#     print("{:.2f}".format(value + (value * 0.04)))
# else:
#     print("Opcao inválida")

# # 6
# age = int(input())
# height = float(input())
# if age >= 18 and height >= 1.7:
#     print("Handebol, Volei e Basquete")
# elif age >= 16 and height >= 1.7:
#     print("Handebol e Volei")
# elif age >= 14 and height >= 1.5:
#     print("Handebol")
# else: 
#     print("Não pode participar de nenhuma modalidade")
