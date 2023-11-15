# Crie um programa que tenha uma tupla unica com nomes de produtos
# e seus respectivos preços na sequencia. No final mostre uma listagem
# de preços organizando os dados em forma tabular

listagem = (
    "Lapis",
    1.75,
    "Boracha",
    2,
    "Caderno",
    15.9,
    "Estojo",
    25,
    "Transferidor",
    4.2,
    "Compasso",
    9.99,
    "Mochila",
    120.32,
    "Caneta",
    22.30,
    "Livro",
    34.9,
)
print("-=" * 20)
print(f"{'Lista de Preços':^40}")
print("-=" * 20)
for x in range(0, len(listagem)):
    if x % 2 == 0:
        print(f"{listagem[x]:.<30}", end="")
    else:
        print(f"R${float(listagem[x]):>8.2f}")
print("-=" * 20)
