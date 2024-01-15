# Faça um programa que tenha uma função chamada escreva() que receba um texto qualquer como paramentro e mostre uma mensagem com tamanho adaptavel


def escreva(palavra):
    tama = len(palavra)
    print("~" * tama)
    print(palavra)
    print("~" * tama)


escreva("Lenon Nascimento")
escreva("Curso de python no youtube")
escreva("EBL")
