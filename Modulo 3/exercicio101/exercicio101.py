# Crie um programa que tenha uma função chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições


def voto(ano=1900):
    from datetime import date

    age = date.today().year - ano
    obg = " "
    if age >= 18 and age <= 65:
        obg = "Voto Obrigatorio."
    elif age >= 16 and age < 18 or age > 65:
        obg = "Voto Opcional"
    else:
        obg = "Não Vota"
    return f"Com {age} anos: " + obg


print("-=" * 20)
ano = int(input("Em que ano voce nasceu? "))
print(voto(ano))
