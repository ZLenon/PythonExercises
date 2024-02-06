print("\033[91mTexto em vermelho\033[0m")
print("\033[92mTexto em verde\033[0m")
print("\033[93mTexto em amarelo\033[0m")
print("\033[94mTexto em azul\033[0m")
print("\033[95mTexto em roxo\033[0m")
print("\033[96mTexto em azul marinho\033[0m")


def gera_texto_colorido(texto):
    from random import randint

    num = randint(1, 6)
    print(f"\033[9{num}m{texto}\033[0m")


gera_texto_colorido("Lenon Nascimento Cardoso")
