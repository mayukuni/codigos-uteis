# # 1166
# num1 = int(input())
# num2 = int(input())
# pago = 0
# divida = num1
# cont = 1

# while pago < num1:
#     pago = pago + num2
#     print("pagamento:", cont)
#     print("antes =", divida)
#     divida = divida - num2
#     if num1 - pago < 0:
#         print("depois = 0")
#     else:
#         print("depois =", num1 - pago)
#     print("-----")
#     cont = cont + 1

# # 1270
# num1 = int(input())
# num2 = int(input())
# if num1 > num2:
#     print("Nenhuma tabuada no intervalo!")
# while num1 <= num2:
#     vezes = 1
#     while vezes <= 10:
#         print(num1, "x", vezes, "=", num1 * vezes)
#         vezes += 1
#     num1 += 1
#     print("----------")

# num1 = int(input())
# num2 = int(input())
# if num1 > num2:
#     print("Nenhuma tabuada no intervalo!")
# while num1 <= num2:
#     for i in range(1, 11):
#         print(f'{num1} x {i} = {num1 * i}')
#     num1 += 1
#     print("----------")

# # 1168
# num1 = int(input())
# num2 = int(input())
# cont = 0
# primo = 0
# while num1 <= num2:
#     for i in range(1, num1 + 1):
#         if num1 % i == 0:
#             primo = primo + 1
#     if primo == 2:
#         cont = cont + 1
#         print(num1)
#     num1 = num1 + 1
#     primo = 0
# print(f'primos: {cont}')

# 1283
cont = 0
list = []
sum = 0
while True:
    sec = int(input())
    if sec < 0:
        break
    cont = cont + 1
    sum = sum + sec
    list.append(sec)
media = sum / cont
print(f'MEDIA: {media:.2f}')
for i in list:
    if i < media:
        print(f'{i:.0f}')








