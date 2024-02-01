def leia_int(param):
    while True:
        try:
            inteiro = int(input(param))
        except:
            print("\033[91mErro!: por favor, digite um numero inteiro valido.\033[m")
        else:
            return inteiro


def option_menu(param):
    valor = int(input(param))
    if valor == 1:
        print("Opção 1")
    elif valor == 2:
        print("Opção 2")
    else:
        print("Saindo do sistema...", flush=True, end=" ")
        print("Ate logo!")


def show_menu():
    print("¨¨" * 40)
    print("1 - Ver pessoas cadastradas")
    print("2 - Cadastrar nova pessoa")
    print("3 - Sair do sistema")
    print("¨¨" * 40)
