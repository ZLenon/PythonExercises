# Faça um programa que tenha uma lista chamada numeros e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 numeros e vair colocar dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior
from random import randint
from time import sleep


def sorteia():
    lista = list()
    count = 0
    while True:
        lista.append(randint(1, 9))
        count += 1
        if count >= 5:
            break
    return lista


def somar_par():
    lista = sorteia()
    soma = 0
    print(f"Sorteando {len(lista)} valores da lista: {lista} Pronto!")
    sleep(1)
    for x in lista:
        if x % 2 == 0:
            soma += x
    print(f"Somando os valores pares de {lista}, temos {soma}")


sorteia()
somar_par()
