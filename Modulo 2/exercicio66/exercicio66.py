# Crie um programa que leia varios numeros inteiros. O programa so vai parar
# quando usuario digitar 999. No final mostre quantos numeros foram digitados
# e qual foi a soma entre eles.

tamanho = soma = 0

while True:
    num = int(input("Digite uma valor, para sair [999]: "))
    if num == 999:
        break
    tamanho += 1
    soma += num
print(f"A soma dos {tamanho} valores é {soma} !")
