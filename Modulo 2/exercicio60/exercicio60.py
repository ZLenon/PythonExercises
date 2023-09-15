# Faça um programa que leia um numero qualquer e mostre o seu fatorial

# from math import factorial
# fact = factorial(numero_digitado)

num = int(input("Digite um numero: "))
count = num
fac = 1
print("Calculando {}! = ".format(num), end="")
while count > 0:
    print("{}".format(count), end="")
    print(" x " if count > 1 else " = ", end="")
    fac *= count
    count -= 1
print("{}".format(fac))
