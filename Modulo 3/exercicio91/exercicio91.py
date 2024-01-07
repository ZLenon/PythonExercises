# Crie um programa onde 4 jogadores joguem um dados e tenham resultados
# aleatorios. Guarde esses resultados em um dicionario. No final,
# coloque esse dicionario em ordem, sabendo que
# o vencedor tirou o maior numero no dado

from random import randint
from time import sleep
from operator import itemgetter

print("-=" * 6, "Game🎲", "-=" * 6)
game = dict(
    {
        "jogador1": randint(1, 6),
        "jogador2": randint(1, 6),
        "jogador3": randint(1, 6),
        "jogador4": randint(1, 6),
    }
)

for key, value in game.items():
    print(f"{key} jogou o dado e tirou {value}")
    sleep(1)

rank = list()
rank = sorted(game.items(), key=itemgetter(1), reverse=True)
print("¨" * 30)

print("-=" * 5, "Resultado🏆", "-=" * 5)
for index, value in enumerate(rank):
    if index == 0:
        print(f"{value[0]} foi o campeão tirou 🎲{value[1]}")
    else:
        print(f"{value[0]} ficou em {index + 1}, tirou 🎲{value[1]}")
