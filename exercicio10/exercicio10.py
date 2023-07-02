# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos Dolares ela pode comprar.
# Considere o DOLAR USS1.00 = R$3.27

dinheiro = float(input("Quanto dinheiro voce possui? R$ "))
real = 3.27
dolar = dinheiro / real

print("Com R${:.2f} voce pode comprar U${:.2f}".format(dinheiro, dolar))
