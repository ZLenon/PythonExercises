lista = [[], []]

for x in range(0, 7):
    valor = int(input(f"Digite o {x}* valor: "))

    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)

print("=*" * 15)
lista[0].sort()
lista[1].sort()
print(f"A lista de pares é {lista[0]}")
print(f"A lista de imparaes é {lista[1]}")
