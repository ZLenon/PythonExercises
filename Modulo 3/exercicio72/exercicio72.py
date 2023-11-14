# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
# por extensão de zero ate vinte. Seu programa devera ler um numero pelo
# teclado entre 0 a 20 e mostra por extenso


numeracao = (
    "zero",
    "um",
    "dois",
    "tres",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "onze",
    "doze",
    "treze",
    "quatorze",
    "quinze",
    "dezesseis",
    "dezessete",
    "dezoito",
    "dezenove",
    "vinte",
)

while True:
    num = int(input("Digite um numero entre 0 a 20: "))
    if 0 <= num <= 20:
        break
print(f"O numero digitado é {numeracao[num]}")
