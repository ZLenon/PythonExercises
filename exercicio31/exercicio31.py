# Desenvolva um programa que pergunte a distançia de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens de
# até 200km e R$0,45 para viagens mais longas

distancia = int(input("Qual a distancia em KM - "))
preco = 0

if distancia <= 200:
    preco = distancia * 0.5
    print("O preço da passagem sera de {}".format(preco))
else:
    preco = distancia * 0.45
    print("O preço da passagem sera de {}".format(preco))
