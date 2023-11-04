# Crie um programa que leia a idade e o sexo de varias pessoas.
# A cada pessoa cadastrada o programa devera perguntar
# se o usuario que ou não continuar, ao fim mostre
# Quantas pessoas tem 18 anos
# Quantos homens foram cadastrados
# Quantas mulheres tem menos de 18 anos

sum_age = sum_male = sum_female = 0

while True:
    age = int(input("Idade: "))
    sex = str(input("Sexo [H/M]: ")).strip().upper()[0]
    end = str(input("Parar [S/N]: ")).strip().upper()[0]
    if age == 18:
        sum_age += 1
    if sex in "H":
        sum_male += 1
    if sex in "M" and age < 18:
        sum_female += 1
    if end == "S":
        break
    print("*" * 15)

print("*" * 15)
print(f"Pessoas com 18 anos - {sum_age} pessoas")
print(f"Homens cadastrados {sum_male}")
print(f"Mulheres menores de idade {sum_female}")
print("FIM")
