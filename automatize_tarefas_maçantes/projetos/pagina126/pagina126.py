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
