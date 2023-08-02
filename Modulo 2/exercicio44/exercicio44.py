# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento.
# A vista dinheiro/cheque - 10% desconto
# cartao - 5% desconto
# 2x no cartao - preço normal
# 3x no cartao - 20% de juros

preco = float(input("Digite o valor do produto - "))
forma_pgto = int(
    input(
        """
  [1] - A vista dinheiro
  [2] - A vista no cartão
  [3] - 2x no cartão
  [4] - 3x no cartão
 """
    )
)
if forma_pgto == 1:
    total = preco - (preco * 10 / 100)
elif forma_pgto == 2:
    total = preco - (preco * 5 / 100)
elif forma_pgto == 3:
    total = preco
elif forma_pgto == 4:
    total = preco + (preco * 20 / 100)
    parcelas = int(input("Quantas parcelas? - "))
    print(
        "Sua compra sera parcelada em {}x de {:.2f}".format(parcelas, total / parcelas)
    )
else:
    raise EOFError("Opção invalida!")
print("Sua compra d e R${:.2f} vai custar R${:.2f}".format(preco, total))
