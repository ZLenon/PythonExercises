# exercicio 107 / 109 refatorando
def juros(num=0, percent=0, moeda=False):
    """
    -> Calcula o juros.
    :param num: int valor a ser calculado.
    :param percent: int valor percentual do juros a ser calculado.
    :param moeda: bool ativa a formataçao em R$ 00,00.
    :return: float ou string formatada
    """
    result = porcent_calc(num, percent)
    if moeda == True:
        return formacted(result + num)
    else:
        return result + num


def desconto(num=0, percent=0, moeda=False):
    """
    -> Calcula o desconto.
    :param num: int valor a ser calculado.
    :param percent: int valor percentual do desconto a ser calculado.
    :param moeda: bool ativa a formataçao em R$ 00,00.
    :return: float ou string formatada
    """
    result = porcent_calc(num, percent)
    if moeda == True:
        return formacted(num - result)
    else:
        return num - result


def dobro(num=0, moeda=False):
    """
    -> Calcula o dobro.
    :param num: int valor a ser calculado.
    :param moeda: bool ativa a formataçao em R$ 00,00.
    :return: float ou string formatada
    """
    if moeda == True:
        return formacted(num * 2)
    else:
        return num * 2


def metade(num=0, moeda=False):
    """
    -> Calcula o metade.
    :param num: int valor a ser calculado.
    :param moeda: bool ativa a formataçao em R$ 00,00.
    :return: float ou string formatada
    """
    if moeda == True:
        return formacted(num / 2)
    else:
        return num / 2


# exercicio 108
def formacted(valor=0):
    """
    -> Formata valor em Reis.
    :param valor: float valor a ser formatado.
    :return: string formatada em reais
    """
    float_config = format(float(valor), ".2f")
    result = str(float_config).replace(".", ",")
    return "R$:" + result


# exercicio 109
def porcent_calc(num=0, percent=0):
    """
    -> Calcula a taxa de porcentagem.
    :param num: int valor a ser calculado.
    :param percent: int valor da taxa a calcular.
    :return: float equivalente a porcentagem a ser somada
    """
    return num * (percent / 100)


# exercicio 110
def resumo(valor, aumento=10, redução=5):
    """
    -> Resume a tbulação de valores.
    :param num: int valor a ser calculado.
    :param aumento: int valor de aumento sobre juros.
    :param percent: int valor de desconto a ser calculado.
    :return: exibe os valores formatados.
    """
    result_metade = metade(valor, True)
    result_dobro = dobro(valor, True)
    result_juros = juros(valor, aumento, True)
    result_desconto = desconto(valor, redução, True)
    new_value = formacted(valor)

    print("-" * 30)
    print("Resumo do Valor".center(30))
    print("-" * 30)
    print(f"Preço analisado: \t\033[95m{new_value}\033[m")
    print(f"Dobro do preço: \t\033[91m{result_dobro}\033[m")
    print(f"Metade do Preço: \t\033[92m{result_metade}\033[m")
    print(f"\033[93m{aumento}%\033[m de aumento: \t\033[91m{result_juros}\033[m")
    print(f"\033[93m{redução}%\033[m de redução: \t\033[92m{result_desconto}\033[m")
    print("-" * 30)
