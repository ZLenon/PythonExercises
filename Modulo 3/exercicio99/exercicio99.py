# Faça um programa que tenha uma função maior(), que receba varios paramentros com valores inteiros. seu programa tem que analisae todos os valores e dizer qual deles é o maior
from time import sleep


def maior(*args):
    maximo = count = 0
    print("-=" * 25)
    print("Analisando valores passados...")
    for x in args:
        count += 1
        if x > maximo:
            maximo = x
        sleep(0.5)
        print(x, end=" ", flush=True)
    print(f"Foram informados {count} valores ao todo.")
    print(f"O maior valor informado foi {maximo}.")


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
