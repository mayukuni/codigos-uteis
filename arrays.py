# numeros = []
# par = []
# impar = []

# print("informe os 10 numeros:")
# for i in range(10):
#     num = int(input())
#     numeros.append(num)
#     if num % 2 == 0:
#         par.append(num)
#     else:
#         impar.append(num)
# print(numeros)
# print(par)
# print(impar)

# FAÇA UMA FUNCAO QUE LEIA UMA LISTA DE 10 NUMEROS INTEIROS, CALCULE E MOSTRE A SOMA DOS QUADRADOS DOS ELEMENTOS DESSA LISTA
# def soma():
#     # numeros = []
#     sum = 0
#     print("informe os 10 numeros:")
#     for i in range(10):
#         num = int(input())
#         # numeros.append(num)
#         quadrado = num ** 2
#         sum += quadrado
#     print(sum)

# soma()

#   CRIE UMA FUNCAO QUE LEIA UMA QUANTIDADE INDETERMINADA DE VALORES INTEIROS, ARMAZENE EM DUAS LISTAS(a E b) E ENCERRE A ENTRADA DE CADA LISTA QUANDO O USUATIO INFORMAR UM VALOR IGUAL A -1 QUE NAO DEVE SER ARMAZENADO. eXIBA O VALOR MÁXIMO E MINIMO DAS DUAS LISTAS
def listas():
    lista1 = []
    lista2 = []
    while True:
        num = float(input())
        if num != -1:
            lista1.append(num)
        else:
            break
    while True:
        num = float(input())
        if num != -1:
            lista2.append(num)
        else:
            break
    print(max(lista1), min(lista1))
    print(max(lista2), min(lista2))

listas()