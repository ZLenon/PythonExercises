# Faça um programa que leia um numero inteiro
# e mostre na tela a sua tabuada, utizando o laço for

num = int(input("Digite o numero da tabuada - "))
print("=*" * 6)
for x in range(0, 11):
    result = x * num
    print("{} x {} = {}".format(num, x, result))

print("=*" * 6)
