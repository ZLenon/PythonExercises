# Faça um programa que leia de um numero de 0 a 9999 e
# mostre na tela cada um dos digitos separados

numero = int(input("Digite um numero inteiro - "))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print("Analizando o numero {}".format(numero))
print("Carregando ......")
print("Unidade {}".format(unidade))
print("Dezena {}".format(dezena))
print("Centena {}".format(centena))
print("Minhar {}".format(milhar))
