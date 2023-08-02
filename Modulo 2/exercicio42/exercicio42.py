# Desenvolva um programa que leia o comprimento de três retas e diga ao
# usuario se elas podem ou não formar um triangulo.
# Mostrar que tipo de triangulo sera formado.abs
# Equilatero - Todos angulos sao iguais
# Isosceles - Dois angulos sao iguais
# Escaleno - Todos angulos sao diferentes
print("==*" * 20)
print("Analizando tres retas de um triangulo")
print("==*" * 20)

lado_1 = float(input("Digite o comprimento do lado 1 - "))
lado_2 = float(input("Digite o comprimento do lado 2 - "))
lado_3 = float(input("Digite o comprimento do lado 3 - "))
soma_1 = lado_1 + lado_2
soma_2 = lado_1 + lado_3
soma_3 = lado_3 + lado_2
if lado_1 < soma_3 and lado_2 < soma_2 and lado_3 < soma_1:
    print("Triangulo Formado com sucesso!!!")
    if lado_1 == lado_2 and lado_2 == lado_3 and lado_3 == lado_1:
        print("Triangulo Equilatero")
    elif lado_1 != lado_2 and lado_2 != lado_3 and lado_3 != lado_1:
        print("Triangulo Escaleno")
    else:
        print("Triangulo Isosceles")
else:
    print("Essas dimensões não formam triangulo!!!")
