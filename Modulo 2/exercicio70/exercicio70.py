# Crie um programa que leia o nome e o preço de varios produtos.
# O programa devera perguntar se o usuario  vai continuar.
# No final mostre:
# Qual é o total gasto na compra,
# Quantos produtos custam mais de R$1000,
# Qual é o nome do produto mais barato

total = maior_mil = qtd = menor = 0
barato = " "
while True:
    name = str(input("Nome do produto: "))
    preco = float(input("Preco R$-"))
    qtd += 1
    total += preco

    if qtd == 1:
        menor = preco
        barato = name
    else:
        if menor > preco:
            menor = preco
            barato = name

    if preco >= 1000:
        maior_mil += 1

    end = " "
    while end not in "SN":
        end = str(input("Quer continuar? [S/N] ")).strip().upper()[0]

    print("*" * 25)
    if end == "N":
        break
print(f"Total gasto R$-{total} em {qtd} produtos")
print(f"A compra possui {maior_mil} produtos mais de R$1000")
print(f"O produto mais barato é {barato} e custa R${menor}")
