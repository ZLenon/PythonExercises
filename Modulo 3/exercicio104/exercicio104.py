# Crie um programa que tenha a função leiaInt() que vai funcionar de forma semelhante a função input() do python, so que fazendo a validação para aceitar apenas um valor numerico. Ex n=leiaInt("Digite um numero")


def leia_int(num):
    while True:
        n = input(num)

        if n.isnumeric():
            n = int(n)
            break
        if n.isascii():
            print("\033[0;31mErro!, Digite um numero inteiro valido.\033[m")

    return n


n = leia_int("Digite um numero: ")
print(f"Voce acabou de digitar o numero {n}")
