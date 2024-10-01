# num = int(input())
# cont = 1
# while cont <= 10:
#     print(num, "x", cont, "=", num * cont)
#     cont += 1

# num = int(input())
# cont = 1
# letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# while cont <= num:
#     print(letras[cont - 1].upper() * cont)
#     cont += 1

# num = 0.00
# soma = 0.00
# while num != -1.0:
#     num = float(input())
#     soma = soma + num
# print("VC$ {:.2f}".format(soma + 1.0))
# print("R$ {:.2f}".format((soma + 1.0) * 2.5))

inicio = int(input())
fim = int(input())
cont = 0
while inicio <= fim:
    if inicio % 4 == 0 and inicio % 100 != 0 or inicio % 400 == 0:
        cont +=1
        print(inicio)
    inicio += 1
print("bissextos:", cont)