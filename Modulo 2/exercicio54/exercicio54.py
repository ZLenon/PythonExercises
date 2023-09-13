# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridad
# e quantas já são maiores
from datetime import date

data_atual = date.today().year
anos = []
maiores = 0
menores = 0
for x in range(0, 7):
    age_in = int(input("Usuario N*{} Digite o seu ano de nascimento: ".format(x + 1)))
    age_real = data_atual - age_in
    anos.append(age_real)

for x in anos:
    if x >= 18:
        maiores += 1
    else:
        menores += 1
print("Total de {} maoires de idade".format(maiores))
print("Total de {} menores de idade".format(menores))
