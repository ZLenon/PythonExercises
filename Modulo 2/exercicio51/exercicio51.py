# Desenvolva um programa que leia o primeiro termo e a razao de uma Progressao
# aritimetica. No final, mostre os 10 primeiros termos dessa progressão

first_term = int(input("Digite o primeiro termo - "))
razao = int(input("Digite a razao aritimetica - "))

for x in range(first_term, first_term + (10 - 1) * razao, razao):
    print(x)
