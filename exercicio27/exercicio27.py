# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o utimo nome separadamente.

name = str(input("Digite seu nome - ")).strip().lower()
separa_name = name.split()

print("Seu Primeiro nome é {}".format(separa_name[0].capitalize()))
print("Seu Utimo nome é {} ".format(separa_name[-1].title()))
