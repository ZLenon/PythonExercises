# Faça um programa que jogue PAR ou IMPAR. O jogo só sera parado quando
# jogador perder, mostrando o total de vitorias que ele conquistou
from random import randint

vitoria = 0
while True:
    player = int(input("Digite um numero: "))
    cpu = randint(0, 11)
    total = cpu + player
    par_impar = " "
    while par_impar not in "pPIi":
        par_impar = str(input("Par ou Impar?")).strip().upper()[0]
    msg = f"Você jogou {player} e o CPU jogou {cpu} a soma é {total} "
    msg += "PAR" if total % 2 == 0 else "IMPAR"
    print(msg)
    if par_impar == "P":
        if total % 2 == 0:
            print("Vitoria!")
            vitoria += 1
        else:
            print("Derrota!")
            break
    if par_impar == "I":
        if total % 2 == 1:
            print("Vitoria!")
            vitoria += 1
        else:
            print("Derrota!")
            break
print(f"Voce venceu {vitoria} vezes")
