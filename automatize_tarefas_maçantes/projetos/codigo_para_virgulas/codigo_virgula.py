# Crie uma função que aceite um valor de lista como argumento e retorne uma string com todos os itens separados por uma vírgula e um espaço, com and inserido antes do último item. Por exemplo, se passarmos a lista spam anterior à função, 'apples, bananas, tofu, and cats' será retornado. Porém sua função deverá ser capaz de trabalhar com qualquer valor de lista que ela receber


def lista_compras(lista=list):
    for x in lista:
        str(x).replace("\n", ",")
        print(x, end=",")


spam = ["apples", "bananas", "tofu", "cats", "grapes", "orange"]
lista_compras(spam)
