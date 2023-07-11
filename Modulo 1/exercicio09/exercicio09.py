# Faça um programa que leia um numero inteiro
# e mostre na tela a sua tabuada

numInt = int(input("Digite um numero inteiro"))
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numeros:
    result = numInt * num
    print(f"{numInt} * {num} = {result}")
