# Crie um programa que leia algo e mostre na tela seus tipo primitivo e
# informações sobre ele

n1 = input("Digite algo ")

print(f"O tipo primitivo é {type(n1)}")
print(f"So tem espaços? {n1.isspace()}")
print(f"É um numero? {n1.isnumeric()}")
print(f"É alfabetico? {n1.isalpha()}")
print(f"É alfanumerico? {n1.isalnum()}")
print(f"Esta em maiusculo? {n1.isupper()}")
print(f"Está em minusculo? {n1.islower()}")
print(f"Esta capitalizado? {n1.istitle()}")
