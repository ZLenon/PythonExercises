# Crie um programa que leia varios numeros inteiros pelo teclado,
# o programa so vai para quando o usuario digitar o valor 99, que
# é a condição de parada, No final mostre quantos numeros foram digitados
# e qual foi a soma entre eles

num = int(input("Digite um numero ou [999] para parar: "))
total = []
tamanho = 0
soma = 0

while num != 999:
    total.append(num)
    tamanho = len(total)
    soma = sum(total)
    num = int(input("Digite um numero ou [999] para parar: "))

print("Voce digitou {} numeros e a soma entre eles é de {}".format(tamanho, soma))
