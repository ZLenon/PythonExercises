# Crie um programa que tenha uma função fatorial() que receba dois paramentros: o primeiro que indique o numero a calcular e outro chamado show, que sera um valor logico Opicional indicado se sera mostrado ou não na tela o processo de calculo do fatorial
def fatorial(num, show=False):
    """
     -> Calcula o fatorial de um numero.
    :param num = O numero a ser calculado.
    :param show =(opcional) mostra ou não a conta.
    return: O valor fatorial de um numero.
    """
    result = 1
    for x in range(num, 0, -1):
        if show:
            print(x, end="")
            if x > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")

        result *= x

    return result


print(fatorial(5))
