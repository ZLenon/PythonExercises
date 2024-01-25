# Crie um modulo chamado (moeda.py) que tenha as funções incorporadas,  aumentar(), diminuir(), dobro(), metade(). Faça tambem um programa que importe esse modulo e use algumas dessas funções.
import ex107

num = int(input("Digite um preço: "))

aumentado = ex107.aumentar(num)
dobro = ex107.dobro(num)
metade = ex107.metade(num)
reduz = ex107.diminuir(num)

print(f"A metade de {num} é {metade}")
print(f"O dobro de {num} é {dobro}")
print(f"Aumentado de 10%, temos {aumentado}")
print(f"Reduzindo 13%, temos {reduz}")
