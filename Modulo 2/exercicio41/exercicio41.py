# A confederação Nacional de natação precisa de um programa que leia o ano de
# nascimento de um atleta e mostre sua categoria, de acordo com a idade.
# Ate 9 anos - Mirin
# Ate 14 anos - infantil
# Ate 19 anos - Junior
# Ate 25 anos - Senior
# Acima 25 anos - Master

from datetime import date

year_now = date.today().year
year_birth = int(input("Digite a sua data de Nascimento - "))
age = year_now - year_birth

if age <= 9:
    print("Voce tem {} anos, Sua Categoria é Mirin".format(age))
elif age > 9 and age <= 14:
    print("Voce tem {} anos, Sua Categoria é Infantil".format(age))
elif age > 14 and age <= 19:
    print("Voce tem {} anos, Sua Categoria é Junior".format(age))
elif age > 19 and age <= 25:
    print("Voce tem {} anos, Sua Categoria é Senior".format(age))
else:
    print("Voce tem {} anos, Sua Categoria é Master".format(age))
