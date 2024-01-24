# Faça um mini-sistema que utilize o interactive help do python. O usuario vai digitar o comando e o manual vai aparecer. Quando o usuario digitar a palavra "FIM" o programa se encerra. Use cores.


cores = (
    "\033[m",  # 0 - Sem cor
    "\033[0;30;41m",  # 1- Vermelho
    "\033[0;30;42m",  # 2- Verde
    "\033[0;30;43m",  # 3- Amarelo
    "\033[0;30;44m",  # 4- Azul
    "\033[0;30;45m",  # 5- Roxo
    "\033[7;30m",  # 6- Branco
)


def ajuda_help(param):
    titulo(f"Acessando o manual do {param}", 4)
    print(cores[6], end="")
    help(param)
    print(cores[0], end="")


def titulo(msg, cor=0):
    print(cores[cor])
    print("~" * len(msg))
    print(msg)
    print("~" * len(msg))
    print(cores[0])


while True:
    titulo("SISTEMA DE AJUDA PYHELP", 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda_help(comando)

titulo("Até Logo!", 1)
# Apertar a letra Q para conseguir continuar na interface
