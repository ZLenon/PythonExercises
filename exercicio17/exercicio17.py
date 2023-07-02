# Faça um programa que leia o comprimento do cateto oposto e do cateto
# adjacente de um triangulo retangulo, calcule e mostre o comprimento dele.
from math import hypot

cateto_oposto = float(input("Digite o cateto oposto - "))
cateto_adjacente = float(input("Digite o cateto adjacente - "))

hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print("A hipotenusa vai medir - {:.2f}".format(hipotenusa))
