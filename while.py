'''cont =1
while cont <= 5:
    print(cont)
    cont = cont+1
print("Fim")


cont = 10
while cont <= 15:
    print(cont)
    cont += 1
print("chega")


cont = 1
while cont <= 10:
    print("6 X", cont,"=", 6 * cont)
    cont += 1
print("enough")


num = int(input("Informe seu número:"))
cont = 1
while cont <= 10:
    print(num, "X", cont, "=", num * cont)
    cont += 1
print("cansei")


cont = 10
while cont > 0:
    print(cont)
    cont -= 1
print("aaaaaaaa")


cont = 10
while cont > 0:
    print(cont, end = ",")
    cont -= 1


cont = 1
while cont <= 10:
    num = int(input())
    if num > 10:
        print("Maior do que 10")
    else:
        print("Menor do que 10")
    cont += 1


i = 1
soma = 0
while i < 10:
    num = int(input("digite:"))
    soma = soma + num
    i+=1
print(soma)


cont = 1
num = 0
while cont <= 5:
    age = int(input())
    if age >= 18:
        num += 1
    cont += 1
print("pessoas maiores de 18 anos:", num)
'''

'''Faça um programa que imprime a quantidade de numeros pares entre 100 ate 200, incluindo-os'''
'''
i = 100
qtd = 0
while i <= 200:
    if i % 2 == 0:
        qtd += 1
    i += 1
print(qtd)
'''

'''Um programa que receba a idade, a altura, peso de 10 pessoas. Calcule e mostre:
    a. Quantidade de pessoas com idade superior a 50
    b. Media das alturas das pessoas com idade de 10 a 20 anos
    c. A porcentagem de pessoas com peso inferios a 40 quilos entre todas as pessoas analidasas.'''
'''i = 1
while i <= 10:
    idade = int(input("idade:"))
    peso = int(input("peso:"))
    altura = int(input("altura"))
    
''' 

'''Um progrma que receba 10 numeros e que calcule e mostre a quantidade de numeros entre 30 e 90'''
'''
i = 1
cont = 0
while i <= 10:
    num = int(input())
    if num > 30 and num < 90:
        cont += 1
    i += 1
print(cont)
'''

'''Um programa que verifique se a senha 4531 foi digitada corretamente, caso nao seja deverá solicitar a senha ate acerta-la'''
'''
senha = int(input("Digite a senha:"))
while senha != 4531:
    print("senha incorreta")
    senha = int(input("Digite a senha:"))
print("chega")
'''
'''
Um programa que receba várias idades e que calcule e mostre a média das idades digitadas. Finalize quando o usuário digitar o número 0.
'''
'''
age = int(input("Digite a idade:"))
qtd = 0
soma = 0
while age != 0:
    qtd += 1
    soma = soma + age
    age = int(input("Digite a idade:"))
print(soma / qtd)
'''
'''
Um programa que receba 20 numeros e que aprsente a quantidade de numeros positivos, negativos e igual a zero.
'''
'''
i = 1
positivo = 0
negativo = 0
zero = 0
while i <= 20:
    num = int(input())
    if num > 0:
        positivo += 1
    if num < 0:
        negativo += 1
    if num == 0:
        zero += 1
    i += 1
print(negativo, positivo, zero)
'''    
'''
Um programa que apresente um menu de opçoes para o calculo das seguintes operações entre dois numeros: adição, subtração, multiplicação e divisão. O programa deve possibilitar ao usuario a escolha da operação desejada, a exibição do resultado e a volta do menu de opções. O programa só termina quando for escolhida a opcao de saída
'''
'''
operacao = input("escolha uma das operacoes: adicao, subtracao, divisao ou multiplicacao:")
num1 = int(input())
num2 = int(input())
while operacao != "saida":
    if operacao == "adicao":
        print(num1 + num2)
        input("escolha uma das operacoes: adicao, subtracao, divisao ou multiplicacao:")
        num1 = int(input())
        num2 = int(input())
    if operacao == "subtracao":
        print(num1 - num2)
        input("escolha uma das operacoes: adicao, subtracao, divisao ou multiplicacao:")
    if operacao == "divisao":
        print(num1 / num2)
        input("escolha uma das operacoes: adicao, subtracao, divisao ou multiplicacao:")
    if operacao == "multiplicacao":
        print(num1 * num2)
        input("escolha uma das operacoes: adicao, subtracao, divisao ou multiplicacao:")
print("chega")
'''
total = 0
quero_comprar = True

while quero_comprar:
    preco = float(input('Preco: '))
    total += preco
    opcao = input('Continuar comprando?')
    if opcao != 's':
        quero_comprar = False
print(f'Total da compra: R${total:.2f}')


