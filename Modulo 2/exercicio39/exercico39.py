# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora de se alistar ou se ja passou do tempo do alistamento.
# Seu programa tambem devera mostrar o tempo que falta ou que passou do prazo.
from datetime import date

year_now = date.today().year
year = int(input("Digite o ano de Nascimento: - "))
idade = year_now - year

print("Quem nasceu em {} tem {} anos em {}".format(year, idade, year_now))

if idade == 18:
    print("Voce tem de se alistar esse ano!!!")
elif idade < 18:
    print("Faltam {} anos para seu alistamento".format(18 - idade))
else:
    print("Ja se passaram {} anos desde seu alistamento".format(idade - 18))
