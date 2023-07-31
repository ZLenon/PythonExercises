# Escreva um programa que leia dois numeros inteiros e compare-os,
# mostrando na tela uma dessas mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Os valores são iguais

num_1 = int(input("Digite o primeiro numero: - "))
num_2 = int(input("Digite o segundo numero: - "))

if num_1 > num_2:
    print("O PRIMEIRO valor é maior {}".format(num_1))
elif num_2 > num_1:
    print("O SEGUNDO valor é maior {}".format(num_2))
else:
    print("Os dois numeros são iguais")
