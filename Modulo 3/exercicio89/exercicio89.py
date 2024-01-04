# Crie um programa que leia o nome e duas notas de varios alunos
# e guarde tudo em uma lista composta no final mostre um boletin
# contendo a media de cada um e permita que o usuario possa mostrar
# as notas de cada aluno individualmente.
continuar = ""
ficha = []

print("-=" * 11)
print("-=" * 3, "BOLETIN", "-=" * 4)
while True:
    while True:
        name = str(input("Nome: ")).strip()
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        media = (nota1 + nota2) / 2
        ficha.append([name.capitalize(), [nota1, nota2], media])
        continuar = str(input("Quer continuar: [S/N]")).upper()[0]
        if continuar in "N":
            break

    print("-=" * 12)
    print("No.", "Nome".center(15), "Media".ljust(30))
    print("_" * 30)
    for index, valor in enumerate(ficha):
        print(f"{index}  ", f"{valor[0]}".center(15), f"{valor[-1]}".ljust(30))
    print("_" * 30)
    print("-=" * 4, "MENU", "-=" * 4)
    print("[1] - Ver notas")
    print("[9] - Sair")
    op = int(input("Escolha uma Numero: "))
    if op == 1:
        while True:
            aluno = str(input("Nome do aluno: ")).capitalize().strip()
            print("¨" * 5, "Ficha Aluno", "¨" * 5)
            for valor in ficha:
                if valor[0] == aluno:
                    print(
                        f"""Aluno: {valor[0]}
1-Nota: {valor[1][0]}
2-Nota: {valor[1][1]}
Média: {valor[2]}"""
                    )
                    print("¨" * 25)

            continuar = str(input("Sair da ficha aluno: [S/N]")).upper()[0]
            if continuar in "S":
                break
    if op == 9:
        break

    continuar = str(input("Sair do sistema: [S/N]")).upper()[0]
    if continuar in "S":
        break

print("-=" * 7, "FIM", "-=" * 7)
