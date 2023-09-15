# Faça um programa que leia o sexo de uma pessoa, mas so aceite os valores
# "M" ou "F". Caso esteja errado, peça a digitação novamente
# ate ter um valor correto

sexo = str(input("Digite seu sexo: [M/F]")).strip().upper()[0]

while sexo not in "MF":
    print("Valor invalido!!!!")
    sexo = str(input("Digite seu sexo: [M/F]")).strip().upper()[0]
if sexo == "F":
    print("Feminino")
else:
    print("Masculino")
