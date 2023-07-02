# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua area e a quantidade de tinta necessaria para pinta-la,
# sabendo que cada litro de tinta pinta uma area de 2m²

altura = float(input("Digite a Altura - "))
largura = float(input("Digite a largura - "))

metros2 = altura * largura
litros = metros2 / 2
print(
    "Essa parede tem {:.2f}m² e vai precisar de {:.2f} litros de tinta".format(
        metros2, litros
    )
)
