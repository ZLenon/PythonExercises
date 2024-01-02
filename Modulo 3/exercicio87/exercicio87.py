# Aprimore o exerciicio 86, mostrando no final:
# A soma de todos os valores pares digitados
# A soma dos valores da terceira coluna
# O maior valor da segunda linha

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sun_pair = sum_tird_colum = sum_second_line = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f"Digite valor [{linha},{coluna}]: "))
print("=*" * 15)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]}]", end="")
        if matriz[linha][coluna] % 2 == 0:
            sun_pair += matriz[linha][coluna]

    print()

print("=*" * 15)
print(f"A soma dos valores pares é: {sun_pair}")

for linha in range(0, 3):
    sum_tird_colum += matriz[linha][2]

print(f"A soma dos valores da terceira coluna {sum_tird_colum}")

for linha in range(0, 3):
    for coluna in range(0, 3):
        if matriz[1][coluna] > sum_second_line:
            sum_second_line = matriz[1][coluna]

print(f"O maior valor da segunda linha é: {sum_second_line}")
