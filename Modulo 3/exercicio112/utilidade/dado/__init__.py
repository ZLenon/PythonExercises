def leia_dinheiro(param):
    while True:
        valor = str(input(param)).replace(",", ".").strip()

        if valor.isalpha() or valor == "":
            print(f"\033[91mErro: '{valor}' é um preço invalido!\033[m")
        else:
            break

    return float(valor)
