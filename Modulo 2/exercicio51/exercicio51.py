# Desenvolva um programa que leia o primeiro termo e a razao de uma Progressao
# aritimetica. No final, mostre os 10 primeiros termos dessa progressão

first_term = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao arritimetica: "))
ten_term = (first_term + (10 - 1) * razao) + razao

for x in range(first_term, ten_term, razao):
    print(x)
