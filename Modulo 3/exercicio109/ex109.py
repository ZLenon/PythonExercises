# exercicio 107 / 109 refatorando
def juros(num, percent, moeda=False):
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


def desconto(num, percent, moeda=False):
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


def dobro(num, moeda=False):
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


def metade(num, moeda=False):
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
def formacted(valor):
    """
    -> Formata valor em Reis.
    :param valor: float valor a ser formatado.
    :return: string formatada em reais
    """
    float_config = format(float(valor), ".2f")
    result = str(float_config).replace(".", ",")
    return "R$:" + result


# exercicio 109
def porcent_calc(num, percent):
    """
    -> Calcula a taxa de porcentagem.
    :param num: int valor a ser calculado.
    :param percent: int valor da taxa a calcular.
    :return: float equivalente a porcentagem a ser somada
    """
    return num * (percent / 100)
