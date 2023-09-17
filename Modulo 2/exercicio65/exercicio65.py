# Crie um programa que leia varios numeros inteiros pelo teclado.
# No final mostre a media, maior, menor. O programa deve perguntar
# ao usuario se ele quer ou não continuar apos cada valor digitado

menor = maior = media = tamanho = soma = 0
yes = "S"

while yes in "Ss":
    num = int(input("Digite um numero: "))
    soma += num
    tamanho += 1
    if tamanho == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    yes = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
media = soma / tamanho
print(
    "Voce digitou {}, a media foi {}, o maior é {}, o menor foi {}".format(
        tamanho, media, maior, menor
    )
)
