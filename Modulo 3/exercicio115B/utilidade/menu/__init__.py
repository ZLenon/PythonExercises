from utilidade import arquivo


def leia_int(param):
    while True:
        try:
            inteiro = int(input(param))
        except:
            print("\033[91mErro!: por favor, digite um numero inteiro valido.\033[m")
        else:
            return inteiro


def option_menu():
    while True:
        valor = leia_int("Opção: ")

        traces_print()
        if valor == 1:
            while True:
                print(arquivo.leitura())
                traces_print()
                sair = input("Quer continuar [S/N]? ").strip().upper()[0]
                if sair == "N":
                    break
        elif valor == 2:
            while True:
                nome = input("Nome: ").strip().capitalize()
                idade = input("Idade: ").strip()
                arquivo.escrita(f"Nome: {nome} - Idade: {idade};")
                sair = input("Quer continuar [S/N]? ").strip().upper()[0]
                if sair == "N":
                    break
        else:
            print("Saindo do sistema...", flush=True, end=" ")
            print("Ate logo!")
            break


def traces_print(param=30):
    print("=" * param)


def show_menu(args=list):
    arquivo.is_verify()
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
