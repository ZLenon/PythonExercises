# Desenvolva um programa que leia o comprimento de três retas e diga ao
# usuario se elas podem ou não formar um triangulo
print("==*" * 20)
print("Analizando tres retas de um triangulo")
print("==*" * 20)
reta1 = float(input("Digite a primeira reta - "))
reta2 = float(input("Digite a segunda reta - "))
reta3 = float(input("Digite a terceira reta - "))

if reta1 < (reta2 + reta3) and reta2 < (reta3 + reta1) and reta3 < (reta2 + reta1):
    print("Podem formar um triangulo")
else:
    print("Não podem formar um triangulo")
