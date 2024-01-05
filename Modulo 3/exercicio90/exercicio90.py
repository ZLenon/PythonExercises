# Faça um programa que leia nome e media de um aluno, guardando tambem
# a situação em um dicionario. No final,
# mostre o consteudo da estrutura na tela

dicio = dict()

nome = str(input("Nome: "))
media = int(input("Média: "))
pass_fail = "Aprovado" if media >= 6 else "Reprovado"
dicio["nome"] = nome
dicio["media"] = media
dicio["situação"] = pass_fail

print("¨" * 20)
for key, value in dicio.items():
    print(f"{key} é igual a {value}")
