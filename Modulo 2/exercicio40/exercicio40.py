# crie um programa que leia duas notas de um aluno e calcule sua media,
# mostrando uma msg no final, de acordo com a media atingida.
# Media abaixo de 5 reprovado
# Media 5 a 6.9 recuperação
# Media acima de 7 aprovado

nota_1 = float(input("Digite a nota 1: - "))
nota_2 = float(input("Digite a nota 2: - "))

media = (nota_1 + nota_2) / 2

print(
    """
    Com as notas {:.1f} e {:.1f} , sua média é de {:.1f}
    """.format(
        nota_1, nota_2, media
    )
)
if media < 5:
    print("Reprovado!!!")
elif media >= 5 and media < 7:
    print("Recuperação!!!")
else:
    print("Aprovado!!!")
