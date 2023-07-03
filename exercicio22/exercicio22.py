# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas letra maiusculas, minusculas, quantas letras tem sem espaço,
# quantas letras tem o primeiro nome.

full_name = str(input("Digite seu nome... ")).strip()
name_up = full_name.upper()
name_low = full_name.lower()
name_not_space = len(full_name) - full_name.count(" ")
first_name = full_name.find(" ")

print(
    """Renderizando......
...."""
)
print("Nome em Maiusculo {}".format(name_up))
print("Nome em Minusculo {}".format(name_low))
print("Quantidade de letras {}".format(name_not_space))
print("O Primeiro nome tem {} letras".format(first_name))
