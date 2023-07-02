# Crie um programa que lei um numero real qualquer pelo teclado
# e mostre na tela a sua porção inteira.
# Ex: 6.127 -> 6
from math import trunc

numFloat = float(input("Digite um numero - "))
numInt = trunc(numFloat)
print("O valor digitado é {} e seu num inteiro é {}".format(numFloat, numInt))
