# 1
tempo1 = int(input())
tempo2 = int(input())
tempo3 = int(input())

print(tempo1 + tempo2 + tempo3, "minutos")

# 2
polegadas = float(input())

print("{:.3f}".format(polegadas * 2.54))

# 3
preco = float(input())
quantidade = int(input())
desconto = 10 + quantidade
totalInicial = preco * quantidade
totalFinal = totalInicial - (totalInicial * (desconto / 100))

print(totalInicial)
print(totalFinal)
