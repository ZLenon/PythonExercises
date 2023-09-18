# Crie um programa que leia varios numeros inteiros pelo teclado.
# No final mostre a media, maior, menor. O programa deve perguntar
# ao usuario se ele quer ou não continuar apos cada valor digitado

menor = maior = media = tamanho = soma = 0
resposta = "S"

while resposta in "Ss":
    num = int(input("Digite um numero: "))
    tamanho += 1
    soma += num
    media = soma / tamanho
    if tamanho == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input("Quer continuar [S/N]: ")).upper().strip()
print("=" * 16)
print("Voce digitou {} numeros".format(tamanho))
print("A soma de todos os numeros é {}".format(soma))
print("A media dos numeros é {}".format(media))
print("O numero maior é {}".format(maior))
print("O numero menor é {}".format(menor))
