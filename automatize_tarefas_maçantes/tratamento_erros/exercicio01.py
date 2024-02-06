# divisão por ZERO, pagina 120


def zero_division(num):
    try:
        return 10 / num
    except ZeroDivisionError as erro:
        print(f"Erro: number not {erro}")


zero_division(0)
