# Faça um programa que leia tres numeros e mostre qual
# é o maior e qual o menor

num1 = int(input("Digite o Primeiro numero - "))
num2 = int(input("Digite o Segundo numero - "))
num3 = int(input("Digite o Terceiro numero - "))

# verifica o menor
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num2 and num3 < num1:
    menor = num3

# verifica o maior
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

# ---------------------------------------
print("O maior valor é {}".format(maior))
print("O menor valor é {}".format(menor))
