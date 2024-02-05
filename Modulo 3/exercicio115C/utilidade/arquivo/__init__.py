caminho = "./Modulo 3/exercicio115C/pessoas.txt"


def cria():
    with open(caminho, "w") as arquivo:
        arquivo.write("")


def leitura():
    with open(caminho, "r") as arquivo:
        info = arquivo.read()
        text_not_space = info.replace("\n", "")
        lista_infos = text_not_space.split(";")
        meu_dict = {}
        for i in range(0, len(lista_infos), 2):
            if i + 1 < len(lista_infos):
                meu_dict[lista_infos[i]] = lista_infos[i + 1]

        for chave, valor in meu_dict.items():
            print(f"{chave}: {valor}")


def escrita(param):
    with open(caminho, "a") as arquivo:
        arquivo.write(param + "\n")
        print(f"Novo Registro adicionado {param}")


def is_verify():
    from os import path
    from utilidade import menu

    if not path.exists(caminho):
        cria()
        menu.traces_print()
        print("\033[92mArquivo criado com sucesso!\033[m")
