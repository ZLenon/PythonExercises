# Faça um programa que tenha uma função chamada contador() que receba tres parametros: inicio, fim e passo e realize a contagem. Seu programa tem que realizar tres contagens atraves da função criada:
# De 1 ate 10, de 1 em 1
# De 10 ate 0, de 2 em 2
# uma contagem personalizada
from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print("-=" * 20)
    print(f"Contagem de {inicio} ate {fim} de {passo} em {passo}")
    count = 0
    if inicio < fim:
        count = inicio
        while count <= fim:
            print(count, end=" ", flush=True)
            sleep(0.5)
            count += passo
        print("Fim!")

    if inicio > fim:
        count = inicio
        while count >= fim:
            print(count, end=" ", flush=True)
            sleep(0.5)
            count -= passo
        print("Fim!")


contador(1, 10, 1)
contador(10, 1, 2)
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo:"))
contador(inicio, fim, passo)
