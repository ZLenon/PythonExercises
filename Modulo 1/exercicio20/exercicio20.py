# O mesmo professor do desafio anterior quer sortear a ordem de uma
# apresentação de trabalhos dos alunos. Faça um programa que leia
# o nome dos quatro alunos e mostre a ordem sorteada
from random import shuffle

nome1 = str(input("Primeiro Aluno - "))
nome2 = str(input("Segundo Aluno - "))
nome3 = str(input("Terceiro Aluno - "))
nome4 = str(input("Quarto Aluno - "))

lista = [nome1, nome2, nome3, nome4]
shuffle(lista)

print("A ordem de apresentação será ")
print(lista)
