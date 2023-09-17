# Escreva um programa que leia um numero inteiro e mostre na tela os primeiro
# elementos da sequencia de fibonacci

num = int(input("Digite um numero: "))
termo_1 = 0
termo_2 = 1
count = 3

while count <= num:
    termo_3 = termo_1 + termo_2
    print("{} -".format(termo_3), end="")
    termo_1 = termo_2
    termo_2 = termo_3
    count += 1
print("FIM")
