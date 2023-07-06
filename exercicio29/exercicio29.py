# Escreva um programa que leia a velocidade de um carro.
# Se ele utrapassar 80km/h, mostre uma msg dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada km acima do limite

velocidade = int(input("Digite a velocidade - "))
valor_multa = 7
multa = 0
if velocidade > 80:
    multa = 7 * (velocidade - 80)
    print("Voce recebeu uma multa sera de {}".format(multa))
else:
    print("Voce não recebeu multa")
