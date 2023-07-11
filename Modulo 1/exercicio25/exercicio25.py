# Crie um programa que leia o nome de uma pessoa
#  e diga se ela tem "Silva" no nome


name = str(input("Digite seu Nome - ")).strip()
is_name = "silva" in name.lower()

print("Seu nome tem SILVA? {}".format(is_name))
