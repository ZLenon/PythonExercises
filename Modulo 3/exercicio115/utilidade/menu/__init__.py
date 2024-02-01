def leia_int(param):
    while True:
        try:
            inteiro = int(input(param))
        except:
            print("\033[91mErro!: por favor, digite um numero inteiro valido.\033[m")
        else:
            return inteiro


def option_menu():
    valor = leia_int("Opção: ")
    if valor == 1:
        print("Opção 1")
    elif valor == 2:
        print("Opção 2")
    else:
        print("Saindo do sistema...", flush=True, end=" ")
        print("Ate logo!")


def traces_print(param=30):
    print("=" * param)


def show_menu(args=list):
    traces_print()
    print("MENU".center(25))
    traces_print()
    count = 0
    while True:
        print(f"\033[93m{count + 1}\033[m", " - ", f"\033[94m{args[count]}\033[m")
        count += 1
        if count >= len(args):
            break
    traces_print()
    option_menu()
