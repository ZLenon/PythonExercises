# Faça um programa que tenha uma função notas() que pode receber varias notas de alunos e vai retornar um dicionario com as seguintes informações.
# Quantidade de notas, A maior nota, A menor nota, a Média da turma, A situação (opcional) add tambem docstrings


def notas(*args, sit=False):
    """
    -> Função para analisar notas e situação de varios alunos.
    :param args: uma ou mais notas dos alunos.
    :param sit: valor opcional, indicando se deve ou não adicionar a situaçao.
    :return: dicionario com varias infos sobre situação da turma.
    """
    dicio = dict()
    maior = menor = media = soma = 0
    total = len(args)
    for x in args:
        if x > maior:
            maior = x
        if menor == 0:
            menor = x
        else:
            if x < menor:
                menor = x
        soma += x
    media = soma / total
    dicio["total"] = total
    dicio["maior"] = maior
    dicio["menor"] = menor
    dicio["media"] = round(media, 2)

    if sit == True:
        if media <= 4:
            dicio["situação"] = "Ruim"
        elif media <= 6.5 and media > 4:
            dicio["situação"] = "Razoavel"
        else:
            dicio["situação"] = "Boa"
    return dicio


retorno = notas(9, 10, 5.5, 2.5, 8.5)
print(retorno)
