# Faça um programa que leia o nome e peso de varias pessoas
# guardando tudo em uma lista. No final mostre
# Quantas pessoas foram cadastradas
# listagem com as pessoas mais pesada
# listagem com as pessoas mais leve

lista_total = list()

menor_peso = maior_peso = 0

while True:
    nome = str(input("Nome: "))
    peso = float(input("Peso: "))
    continuar = str(input("Quer continuar [S/N]- ")).upper()[0]

    if menor_peso == 0 and maior_peso == 0:
        menor_peso = peso
        maior_peso = peso
        lista_total.append([nome, peso])

    else:
        if peso <= menor_peso:
            menor_peso = peso
            lista_total.append([nome, peso])

        elif peso >= maior_peso:
            maior_peso = peso
            lista_total.append([nome, peso])

    print("=*" * 15)
    if continuar in "N":
        break

print("=*" * 15)
print(f"Menor peso foi {menor_peso}. Peso de ", end="")
for x in lista_total:
    if x[1] <= menor_peso:
        print(x[0])

print(f"Maior peso foi {maior_peso}. Peso de ", end="")
for x in lista_total:
    if x[1] >= maior_peso:
        print(x[0])
