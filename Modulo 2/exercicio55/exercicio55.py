# Faça um programa que leia o peso de cinco pessoas,
# mostra qual foi o maior e o menor peso ldisos

todos_pesos = []
menor_peso = 0
maior_peso = 0

for x in range(0, 5):
    peso = float(input("Pessoa N*{} digite seu peso: ".format(x + 1)))
    todos_pesos.append(peso)
    if x == 0:  # primeira interação do for
        maior_peso = peso
        menor_peso = peso
        print(maior_peso, menor_peso)
    else:  # a partir da segunda interação
        if peso > maior_peso:
            maior_peso = peso
        elif peso < menor_peso:
            menor_peso = peso
    print(maior_peso, menor_peso)

print("O maior peso é {}Kg".format(maior_peso))
print("O menor peso é {}Kg".format(menor_peso))
print("Todos os pesos digiados são {}".format(todos_pesos))
