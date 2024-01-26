# Crie um modulo chamado (moeda.py) que tenha as funções incorporadas,  aumentar(), diminuir(), dobro(), metade(). Faça tambem um programa que importe esse modulo e use algumas dessas funções.
import ex107

num = int(input("Digite um preço: "))


juros = ex107.juros(num, 10)
dobro = ex107.dobro(num)
metade = ex107.metade(num)
desconto = ex107.desconto(num, 13)

print(f"A metade de {num} é {metade}")
print(f"O dobro de {num} é {dobro}")
print(f"Aumento de 10%, temos {juros}")
print(f"Desconto de 13%, temos {desconto}")
