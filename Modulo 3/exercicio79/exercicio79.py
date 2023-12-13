# Crie um programa onde o usuario possa digitar varios valores numericos
# e cadastre em uma lista. Caso o numero ja existe la dentro ela nao sera
# adicionado. No final serão exibidos todos os valores unicos digitados em
# ordem crescente

lista = []
continuar = ""
while continuar in "S":
    valor = int(input("Digite uma Valor: "))

    if valor in lista:
        print("Valor ja esta na lista - Nao vou adicionar")
    else:
        lista.append(valor)
    print("*=" * 30)
    continuar = str(input("Quer continuar? [S/N]: ")).upper()[0]

print("*=" * 30)
lista.sort()
print(f"Voce digitou {lista}")
