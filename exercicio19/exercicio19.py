# Um professor que sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome
#  escolhido
import random

nome1 = str(input("Primeiro Aluno - "))
nome2 = str(input("Segundo Aluno - "))
nome3 = str(input("Terceiro Aluno - "))
nome4 = str(input("Quarto Aluno - "))

lista = [nome1, nome2, nome3, nome4]
sorteado = random.choice(lista)

print("O aluno escolhido foi {}".format(sorteado))
