# Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma
# tupla, depois mostre a listagem de numeros gerados e tambem indique
# o menor e o maior valor que estao na tupla

from random import randint

soteados = (
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
)

print("=*" * 20)
print(f"Numeros sorteados foram - {soteados}")
print(f"O maior numero é {max(soteados)}")
print(f"O menor numero é {min(soteados)}")
