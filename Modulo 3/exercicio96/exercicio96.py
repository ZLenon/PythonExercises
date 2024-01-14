# Faça um programa que tenha uma função chamada area(), que receba as dimensoẽs de um terreno retangular (largura, altura) e mostre a area do terreno


def area(largura, altura):
    area = largura * altura
    print(f"A area de um terreno {largura}x{altura} é de {area:5.1f}m²")


print("-=" * 5, "Controle de Terrenos", "-=" * 5)
larg = float(input("Largura (m): "))
alt = float(input("Comprimento (m): "))

area(larg, alt)
