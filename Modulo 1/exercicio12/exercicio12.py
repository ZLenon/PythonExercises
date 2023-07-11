# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço,
# com 5% de desconto.

preco_produto = float(input("Digite o preço do produto - R$"))
desconto = preco_produto - (preco_produto * 5 / 100)

print(
    "O preço é de R${:.2f} e com desconto fica R${:.2f}".format(
        preco_produto,
        desconto,
    )
)
