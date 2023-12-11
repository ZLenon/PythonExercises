# Faça um programa que leia 5 valores numericos e guarde em uma lista.
# No final mostre qual foi o maior e menor valor digitados e as suas
# respectivas posições na lista

lista = []
count = menor = maior = 0

while True:
    count += 1
    valor = int(input(f"Digite o {count}* valor: "))
    lista.append(valor)
    if count == 5:
        maior = max(lista)
        indexMaior = lista.index(maior) + 1
        menor = min(lista)
        indexMenor = lista.index(menor) + 1
        break
print(f"A lista é {lista}")
print(f"O menor é {menor} ele se encontra na posição {indexMenor}*")
print(f"O maior é {maior} ele se encontra na posição {indexMaior}*")
