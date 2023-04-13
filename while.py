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

# def primo(n):
#     qtd_divisores = 0
#     divisor = 1
#     while divisor <= n:
#         if n % divisor == 0:
#             qtd_divisores += 1
#         divisor += 1
#     if qtd_divisores == 2:
#         return True
#     else:
#         return False

'''credito = float(input('Seu crédito: R$ '))
while credito > 0:
    item = float(input('Preço do item: R$ '))
    if item > credito:
        print('Compra negada! Ultrapassa seu crédito.')
        break
    credito -= item
print(f'Crédito restante: R$ {credito:.2f}')
'''
# escreva um trecho de um programa que le e valida se nota digitada de um aluno eta entre 0 e 10
'''nota = int(input())
if nota >= 0 and nota <= 10:
    print('nota válida')
else:
    print('inválida')
'''
# faça um programa que imprima as tauadas de ultiplicação de 1 a 10
# num = 1
# vezes = 1
# while num <= 10:
#     while vezes <= 10:
#         print(num, "x", vezes, "=", num * vezes)
#         vezes += 1
#     num += 1
#     print("tabuada do", num)
#     if vezes == 11:
#         vezes = vezes - 10


# um professor possui n turmas e cada turma possui m alunos. Solicite qu o usuario informe a quantidade de turms e a quantidade de alunos de cada turma.
turmas = int(input("digite o numero de turmas:"))
num = 0
# alunos = int(input())
# construa um programa que leia a nota dos alunos de cada uma das turmas e exiba a media das notas por turma
while turmas != num:
    alunos = int(input('digite o numero de alunos:'))
    print("quantidade de alunos da turma", num + 1, ':', alunos)
    num2 = 0
    while alunos != num2:
        notas = int(input("nota dos alunos:"))
        num2 += 1
    print(notas)
    num += 1


