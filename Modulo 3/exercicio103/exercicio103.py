# Faça um programa que tenha uma função chamada ficha(), que receba dois paramentros opcionais: o nome de um jogador e quantos gols ele marcou. O programa devera ser capaz de mostrar a fucha do jogador, mesmo que algum dado não tenha sido informado corretamente.


def ficha(name="<desconhecido>", gols=0):
    print("¨" * 60)
    print(f"O jogador {name} fez {gols} gol's no campeonato")


name = str(input("Nome do jogador: "))
gols = str(input("Numero de gols: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if name.strip() == "":
    ficha(gols=gols)
else:
    ficha(name, gols)
