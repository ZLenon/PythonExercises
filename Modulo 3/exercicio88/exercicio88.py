# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai pergutar quantos jogos serão gerados e vai sortear 6
# numeros entre 1 a 60 para cada jogo cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

count = count2 = 0
lista = []

print("-=" * 17)
print("-=" * 3, "APOSTAS NA MEGA SENA", "-=" * 3)
print("-=" * 17)

cartelas = int(input("Quantos jogos voce quer gerar: "))

while count2 < cartelas:
    count2 += 1
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            count += 1
        if count == 6:
            count = 0
            break
    lista.sort()
    sleep(1)
    print(f"Jogo {count2}: {lista}")
    lista.clear()
print("-=" * 17)
print("-=" * 5, "Boa Sorte", "-=" * 5)
print("-=" * 17)
