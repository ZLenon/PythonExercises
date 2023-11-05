# Crie um programa que simule o funcionamento de um caixa eletronico.
# No inicio, pergunte ao usuario qual sera o valor a ser sacado,
# e programa vai informar quantas cedulas de cada valor serão entregues.
# cedulas de R$ - 50, 20, 10, 1
print("=" * 30)
print("{:^30}".format("BANCO DO BRASIL"))
print("=" * 30)

valor = int(input("Valor a ser sacado R$-"))
ced_50 = ced_20 = ced_10 = ced_1 = 0

while valor > 0:
    if valor >= 50:
        ced_50 += 1
        valor -= 50
    elif valor >= 20:
        ced_20 += 1
        valor -= 20
    elif valor >= 10:
        ced_10 += 1
        valor -= 10
    elif valor >= 1:
        ced_10 += 1
        valor -= 1
    else:
        break
print(f"Cedulas de {ced_50}")
print(f"Cedulas de {ced_20}")
print(f"Cedulas de {ced_10}")
print(f"Cedulas de {ced_1}")
print(f"Valor restante {valor}")
