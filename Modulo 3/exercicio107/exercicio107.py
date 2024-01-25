# Crie um modulo chamado (moeda.py) que tenha as funções incorporadas,  aumentar(), diminuir(), dobro(), metade(). Faça tambem um programa que importe esse modulo e use algumas dessas funções.
from utils import moeda


num = int(input("Digite um preço: "))

aumentado = moeda.exercicio107.aumentar(num)
dobro = moeda.exercicio107.dobro(num)
metade = moeda.exercicio107.metade(num)
reduz = moeda.exercicio107.diminuir(num)

print(f"A metade de {num} é {metade}")
print(f"O dobro de {num} é {dobro}")
print(f"Aumentado de 10%, temos {aumentado}")
print(f"Reduzindo 13%, temos {reduz}")
