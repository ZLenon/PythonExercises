# Faça um programa que jogue PAR ou IMPAR. O jogo só sera parado quando
# jogador perder, mostrando o total de vitorias que ele conquistou
from random import randint

print("=" * 16)
print("GAME DE PAR ou IMPAR")
print("=" * 16)
total = vitoria = 0

while True:
    try:
        jogador = int(input("Digite um numero: "))
        cpu = randint(0, 11)
        total = cpu + jogador
        par_impar = "PAR" if total % 2 == 0 else "IMPAR"
        opcao = str(input("Escolha PAR ou IMPAR - [P/I] - ")).upper().strip()[0]
        print(f"CPU-{cpu} Jogador-{jogador} -> {total} é {par_impar}")
        if opcao in par_impar:
            vitoria += 1
            print("Venceu!!!")
        else:
            print("Derrota, FIM de jogo!!!")
            print("=" * 16)
            break
        print("=" * 16)
    except ValueError as x:
        print(f"Use numero ao invez de letras. \nO Erro mostrado é - {x}")
print(f"Total de vitorias nessa rodada - {vitoria}")
