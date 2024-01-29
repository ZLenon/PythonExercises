# Reescreva a função leia_int() que fizemos no desafio 104, incluindo agora a prosibilidade da digitação de um numero de tipo invalido. Aproveite e crie uma tbm uma função leia_float() com a mesma funcionalidade.


def leia_int(param):
    while True:
        try:
            inteiro = int(input(param))
        except:
            print("\033[91mErro!: por favor, digite um numero inteiro valido.\033[m")
        else:
            return inteiro


def leia_float(param):
    while True:
        try:
            value_float = float(input(param))
        except:
            print("\033[91mErro: por favor digite um numero real valido.\033[m")
        else:
            break
    return value_float


num_int = leia_int("Digite um numero inteiro: ")
print("")
num_float = leia_float("Digite um numero Real: ")
print(
    f"\033[93mO valor inteiro digitado foi {num_int} e o valor Real foi {num_float}\033[m"
)
