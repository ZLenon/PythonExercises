# Sequência de Collatz Crie uma função chamada collatz() que tenha um parâmetro de nome number. Se number for par, collatz() deverá exibir number // 2 e reatribua esse valor a number. Se number for ímpar, collatz() deverá exibir e reatribua 3 * number + 1. Em seguida, crie um programa que permita que o usuário digite um inteiro e fique chamando collatz() com esse número até a função retornar o valor 1. (De modo bastante surpreendente, essa sequência, na realidade, funciona para qualquer inteiro – cedo ou tarde, ao usar essa sequência, você chegará em 1! Até mesmo os matemáticos não têm muita certeza do motivo. Seu programa está explorando o que chamamos de sequência de Collatz, às vezes chamada de “o mais simples problema matemático impossível”.)
# pagina 126
from time import sleep


def collatz(number):
    print(number, end=" ", flush=True)
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        sleep(1)
        print(number, end=" ", flush=True)


number = int(input("Digite um numero inteiro: "))
collatz(number)
