# exercicio 107
def juros(num, percent):
    result = num * (percent / 100)
    return result + num


def desconto(num, percent):
    result = num * (percent / 100)
    return num - result


def dobro(num):
    return num * 2


def metade(num):
    return num / 2


# exercicio 108
def formacted(valor):
    float_config = format(float(valor), ".2f")
    result = str(float_config).replace(".", ",")
    return "R$:" + result
