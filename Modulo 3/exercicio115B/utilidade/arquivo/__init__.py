caminho = "./Modulo 3/exercicio115B/pessoas.txt"


def cria():
    with open(caminho, "w") as arquivo:
        arquivo.write("")


def leitura():
    with open(caminho, "r") as arquivo:
        info = arquivo.read()
        return info


def escrita(param):
    with open(caminho, "a") as arquivo:
        arquivo.write(param + "\n")


def is_verify():
    from os import path
    from utilidade import menu

    if not path.exists(caminho):
        cria()
        menu.traces_print()
        print("\033[92mArquivo criado com sucesso!\033[m")
