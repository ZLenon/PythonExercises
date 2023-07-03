# Faça um programa que leia um angulo qualquer e
# mostre na tela o valor do seno, cosseno e tangente desse angulo
import math

angulo = float(input("Digite um algulo qualquer - "))

seno = math.sin(math.radians(angulo))
print("O angulo de {:.2f} tem o seno de {:.2f}".format(angulo, seno))

cosseno = math.cos(math.radians(angulo))
print("O angulo de {:.2f} tem o cosseno de {:.2f}".format(angulo, cosseno))

tangente = math.tan(math.radians(angulo))
print("O angulo de {:.2f} tem o seno de {:.2f}".format(angulo, tangente))
