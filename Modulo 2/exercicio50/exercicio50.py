# Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for impar, desconsidere-o

cont = 0
soma = 0
for x in range(1, 7):
    num = int(input("Digite um valor"))
    if num % 2 == 0:
        soma += num
        cont += 1
print("soma {} contados {}".format(soma, cont))
