# Crie um programa onde 4 jogadores joguem um dados e tenham resultados
# aleatorios. Guarde esses resultados em um dicionario. No final,
# coloque esse dicionario em ordem, sabendo que
# o vencedor tirou o maior numero no dado

from random import randint
from time import sleep
from operator import itemgetter

time = sleep(1)
ranking = dict({"jogador1": randint(1, 6)})
print(ranking)
