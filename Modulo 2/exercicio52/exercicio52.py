# Faça um prorgama que leia um numero inteiro
# e diga se ele é ou não um numero primo


num = int(input("Digite um numero inteiro: "))
div = 0
for x in range(1, num + 1):
    if num % x == 0:
        print("\033[33m", end="-")
        div += 1
    else:
        print("\033[31m", end="-")
    print("{}".format(x), end="")
print("\n \33[m O numero {} foi divisivel {} vezes".format(num, div))
if div == 2:
    print("Numero primo")
else:
    print("NÃO é primo")
