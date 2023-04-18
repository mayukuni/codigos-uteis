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

# # 4 várias formas
# A = float(input())
# intervalo = ""
# if A > 75 and A <= 100:
#     intervalo = "(75,100]"
# elif A > 50 and A <= 75:
#     intervalo = "(50,75]"
# elif A > 25 and A <= 50:
#     intervalo = "(25,50]"
# elif A >= 0 and A <= 25:
#     intervalo = "[0,25]"
# if A < 0 or A > 100:
#     print("Fora de intervalo")
# else:
#     print("Intervalo", intervalo)

# A = float(input())
# intervalo = ["[0,25]", "(25,50]", "(50,75]", "(75,100]"]
# if A > 75 and A <= 100:
#     opa = intervalo[3]
# elif A > 50 and A <= 75:
#     opa = intervalo[2]
# elif A > 25 and A <= 50:
#     opa = intervalo[1]
# elif A >= 0 and A <= 25:
#     opa = intervalo[0]
# if A < 0 or A > 100:
#     print("Fora de intervalo")
# else:
#     print("Intervalo", opa)

# A = float(input())
# if A > 75 and A <= 100:
#     print("Intervalo (75,100]")
# elif A > 50 and A <= 75:
#     print("Intervalo (50,75]")
# elif A > 25 and A <= 50:
#     print("Intervalo (25,50]")
# elif A >= 0 and A <= 25:
#     print("Intervalo [0,25]")
# else:
#     print("Fora de intervalo")

# 5
# A = input()
# B = input()
# C = input()

# tipo1 = ["vertebrado", "invertebrado"]
# tipo2 = ["ave", "mamifero", "inseto", "anelideo"]
# tipo3 = ["carnivoro", "onivoro", "herbivoro", "hematofago"]
# tipo4 = ["aguia", "pomba", "homem", "vaca", "pulga", "lagarta", "sanguessuga", "minhoca"]
# if A == tipo1[0] and B == tipo2[0] and C == tipo3[0]:
#     print(tipo4[0])
# if A == tipo1[0] and B == tipo2[0] and C == tipo3[1]:
#     print(tipo4[1])
# if A == tipo1[0] and B == tipo2[1] and C == tipo3[1]:
#     print(tipo4[2])
# if A == tipo1[0] and B == tipo2[1] and C == tipo3[2]:
#     print(tipo4[3])
# if A == tipo1[1] and B == tipo2[2] and C == tipo3[3]:
#     print(tipo4[4])
# if A == tipo1[1] and B == tipo2[2] and C == tipo3[2]:
#     print(tipo4[5])
# if A == tipo1[1] and B == tipo2[3] and C == tipo3[3]:
#     print(tipo4[6])
# if A == tipo1[1] and B == tipo2[3] and C == tipo3[1]:
#     print(tipo4[7])

# A = input()
# B = input()
# C = input()

# tipoA = ["vertebrado", "invertebrado"]
# tipoB = ["ave", "mamifero", "inseto", "anelideo"]
# tipoC = ["carnivoro", "onivoro", "herbivoro", "hematofago"]
# animal = ["aguia", "pomba", "homem", "vaca", "pulga", "lagarta", "sanguessuga", "minhoca"]
# if A == tipoA[0]:
#     if B == tipoB[0]:
#         if C == tipoC[0]:
#             print(animal[0])
#         if C == tipoC[1]:
#             print(animal[1])
#     if B == tipoB[1]:
#         if C == tipoC[1]:
#             print(animal[2])
#         if C == tipoC[2]:
#             print(animal[3])
# if A == tipoA[1]:
#     if B == tipoB[2]:
#         if C == tipoC[3]:
#             print(animal[4])
#         if C == tipoC[2]:
#             print(animal[5])
#     if B == tipoB[3]:
#         if C == tipoC[3]:
#             print(animal[6])
#         if C == tipoC[1]:
#             print(animal[7])

# 6
# A, B, C, D = map(float, input().split())
# nota1 = A * 2
# nota2 = B * 3
# nota3 = C * 4
# final = (nota1 + nota2 + nota3 + D) / 10
# print("Media: {:.1f}".format(final))
# if final >= 7:
#     print("Aluno aprovado.")
# if final < 5:
#     print("Aluno reprovado.")
# if final >= 5 and final < 7:
#     print("Aluno em exame.")
#     exame = float(input())
#     print("Nota do exame: {:.1f}".format(exame))
#     if (final + exame) / 2 >= 5:
#         print("Aluno aprovado.")
#     else:
#         print("Aluno reprovado.")
#     print("Media final: {:.1f}".format((final + exame) / 2))

# # ????
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

# # ????
# type = int(input())
# value = float(input())
# if type == 1:
#     print("{:.2f}".format(value + (value * 0.03)))
# elif type == 2:
#     print("{:.2f}".format(value + (value * 0.04)))
# else:
#     print("Opcao inválida")

# # ???
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

# def main(num):
#     v1 = num[0]
#     v2 = num[0]
#     for i in range(1, len(num)):
#         if num[i] < v1:
#             v1 = num[i]
#         elif num[i] > v2:
#             v2 = num[i]
#     return v1, v2

# # Vetor com números de 1 a 100
# num = list(range(1, 101))
# v1, v2 = main(num)
# print("v1 =", v1)
# print("v2 =", v2)

