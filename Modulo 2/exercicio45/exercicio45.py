# crie um programa que faça o computador jogar jokenpo com vc

from random import randint

player = int(
    input(
        """ 
[0] - Pedra
[1] - Papel
[2] - Tesoura
"""
    )
)
opcoes = ("Pedra", "Papel", "Tesoura")
cpu = randint(0, 2)

print("O Computador escolheu {}".format(opcoes[cpu]))
print("Jogador escolheu {}".format(opcoes[player]))


if cpu == 0:  # Pedra
    if player == 0:
        print("Empate!!")
    elif player == 1:
        print("Player vence!!!")
    elif player == 2:
        print("Maquina vence!!")
    else:
        print(f"Erro de valor: {player}")
elif cpu == 1:  # Papel
    if player == 0:
        print("Maquina vence!!")
    elif player == 1:
        print("Empate!!")
    elif player == 2:
        print("Player vence!!!")
    else:
        print(f"Erro de valor: {player}")
elif cpu == 2:  # Tesoura
    if player == 0:
        print("Player vence!!!")
    elif player == 1:
        print("Maquina vence!!")
    elif player == 2:
        print("Empate!!")
    else:
        print(f"Erro de valor: {player}")
