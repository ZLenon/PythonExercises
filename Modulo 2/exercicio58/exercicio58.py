# Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 10 e peça para o usuario tentar descobrir qual foi o número
# escolhido pelo computador. O programa deverá escrever na tela se o
# usuario venceu ou perdeu.
# Mostrar quantos palpites foram feitos
from random import randint

cpu = randint(0, 10)
count = 0
valid = False

while not valid:
    num = int(input("Digite um numero entre 0 a 10: "))
    count += 1
    if num == cpu:
        valid = True
        print("{} - {}".format(cpu, num))
    else:
        if cpu > num:
            print("Um pouco mais alto")
        elif cpu < num:
            print("Um pouco mais baixo")

print("Acertou!!! voce tentou {} palpites".format(count))
