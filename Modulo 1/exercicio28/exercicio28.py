# Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 e peça para o usuario tentar descobrir qual foi o número
# escolhido pelo computador. O programa deverá escrever na tela se o
# usuario venceu ou perdeu.
from random import randint
from time import sleep

num_alearoio_pc = randint(0, 5)
print("-=-" * 20)
print(
    """
Tente advinhar o numero entre zero e cinco!!!
"""
)
print("-=-" * 20)
num = int(input("Escreva um numero - "))
print("Carregando....")
sleep(2)
if num == num_alearoio_pc:
    print("Voce acertou o numero realmente era {}".format(num_alearoio_pc))
else:
    print("Voce errou o numero escolhido foi {}".format(num_alearoio_pc))
