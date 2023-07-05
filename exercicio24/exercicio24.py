# Crie um programa que leia o nome de uma cidade e
# diga se ela começa ou não com o nome SANTO

city = str(input("Digite uam cidade - ")).strip()


if city[0:5].lower() == "santo":
    print("Essa cidade começa com SANTO")
